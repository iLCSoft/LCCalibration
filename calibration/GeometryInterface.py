

from math import *
import os
from calibration.XmlTools import *
import subprocess
import ROOT
from ROOT import gROOT
gROOT.SetBatch(1)
import DD4hep
import DDRec
import calibration.SystemOfUnits as ddunits

class DDGeometryInterface(object):
    def __init__(self, compactFile):
        self._compactFile = compactFile
        DD4hep.setPrintLevel(DD4hep.OutputLevel.ERROR)
        self._description = DD4hep.Detector.getInstance()
        self._description.fromXML(self._compactFile)
        
    def _getDetector(self, dname):
        return self._description.detector(dname)
    
    def getCaloExtent(self, dname, ext):
        detector = self._getDetector(dname)
        data = DDRec.LayeredCalorimeterData(detector)
        return data.extent[ext]/ddunits.mm

    def getCaloInnerR(self, dname):
        return self.getCaloExtent(dname, 0)

    def getCaloOuterR(self, dname):
        return self.getCaloExtent(dname, 1)
    
    def getCaloInnerZ(self, dname):
        return self.getCaloExtent(dname, 2)
    
    def getCaloOuterZ(self, dname) :
        return self.getCaloExtent(dname, 3)
    
    def getEcalBarrelCosThetaRange(self, dname="EcalBarrel") :
        ecalBarrelOuterR = float(self.getCaloOuterR(dname))
        ecalBarrelOuterZ = float(self.getCaloOuterZ(dname))
        maxCosTheta = cos(atan( ecalBarrelOuterR / ecalBarrelOuterZ ))
        return 0.05, maxCosTheta
    
    def getEcalEndcapCosThetaRange(self, dname="EcalEndcap") :
        ecalEndcapOuterR = float(self.getCaloOuterR(dname))
        ecalEndcapOuterZ = float(self.getCaloOuterZ(dname))
        ecalEndcapInnerR = float(self.getCaloInnerR(dname))
        ecalEndcapInnerZ = float(self.getCaloInnerZ(dname))
        minCosTheta = cos(atan( ecalEndcapOuterR / ecalEndcapOuterZ ))
        maxCosTheta = cos(atan( ecalEndcapInnerR / ecalEndcapInnerZ ))
        return minCosTheta, maxCosTheta

    def getHcalBarrelCosThetaRange(self, dname="HcalBarrel") :
        hcalBarrelOuterR = float(self.getCaloOuterR(dname))
        hcalBarrelOuterZ = float(self.getCaloOuterZ(dname))
        maxCosTheta = cos(atan( hcalBarrelOuterR / hcalBarrelOuterZ ))
        return 0.05, maxCosTheta

    def getHcalEndcapCosThetaRange(self, dname="HcalEndcap") :
        hcalEndcapOuterR = float(self.getCaloOuterR(dname))
        hcalEndcapOuterZ = float(self.getCaloOuterZ(dname))
        hcalEndcapInnerR = float(self.getCaloInnerR(dname))
        hcalEndcapInnerZ = float(self.getCaloInnerZ(dname))
        minCosTheta = cos(atan( hcalEndcapOuterR / hcalEndcapOuterZ ))
        maxCosTheta = cos(atan( hcalEndcapInnerR / hcalEndcapInnerZ ))
        return minCosTheta, maxCosTheta
    
    """ Calculates and returns the following factor :
        f = (Abs_endcap / Abs_ring) * (Sens_ring / Sens_endcap)
    """
    def getCalorimeterGeometryFactor(self, endcapName, ringName):
        endcapDetector = self._getDetector(endcapName)
        plugDetector = self._getDetector(ringName)
        endcapAbsorberSum = 0
        endcapSensitiveSum = 0
        plugAbsorberSum = 0
        plugSensitiveSum = 0
        endcapData = DDRec.LayeredCalorimeterData(endcapDetector)
        plugData = DDRec.LayeredCalorimeterData(plugDetector)
            
        for layer in endcapData.layers:
            totalThickness = (layer.inner_thickness+layer.inner_thickness)/ddunits.mm
            senitiveThickness = layer.sensitive_thickness/ddunits.mm
            absorberThickness = totalThickness - senitiveThickness
            endcapAbsorberSum = endcapAbsorberSum + absorberThickness
            endcapSensitiveSum = endcapSensitiveSum + senitiveThickness

        for layer in plugData.layers:
            totalThickness = (layer.inner_thickness+layer.inner_thickness)/ddunits.mm
            senitiveThickness = layer.sensitive_thickness/ddunits.mm
            absorberThickness = totalThickness - senitiveThickness
            plugAbsorberSum = plugAbsorberSum + absorberThickness
            plugSensitiveSum = plugSensitiveSum + senitiveThickness
        
        return (endcapAbsorberSum / plugAbsorberSum) * (plugSensitiveSum / endcapSensitiveSum) 
        
        
    """ Calculates and returns the following factor in the ecal
        f = (Abs_endcap / Abs_ring) * (Sens_ring / Sens_endcap)
    """
    def getEcalGeometryFactor(self, ecname="EcalEndcap", ername="EcalPlug"):
        return self.getCalorimeterGeometryFactor(ecname, ername)
    
    """ Calculates and returns the following factor in the hcal
        f = (Abs_endcap / Abs_ring) * (Sens_ring / Sens_endcap)
    """
    def getHcalGeometryFactor(self, hcname="HcalEndcap", hrname="HcalRing"):
        return self.getCalorimeterGeometryFactor(hcname, hrname)

class GeometryInterface(object) :
    def __init__(self, gearFile):
        self._gearFile = gearFile
        parser = createXMLParser()
        self._xmlTree = etree.parse(self._gearFile, parser)
    
    def _getGearDetector(self, dname, dtype) :
        elements = self._xmlTree.xpath("//gear/detectors/detector[@name='{0}'][@geartype='{1}']".format(dname, dtype))
        return None if not len(elements) else elements[0] 
    
    def getDetectorDimmensions(self, dname, dtype) :
        detector = self._getGearDetector(dname, dtype)
        if detector is not None :
            return detector.find("dimensions")
        return None
    
    def getDetectorInnerR(self, dname, dtype) :
        dimensions = self.getDetectorDimmensions(dname, dtype)
        if dimensions is not None :
            return dimensions.get("inner_r")
    
    def getDetectorOuterR(self, dname, dtype) :
        dimensions = self.getDetectorDimmensions(dname, dtype)
        if dimensions is not None :
            outerR = dimensions.get("outer_r")
            if outerR is not None :
                return float(outerR)
            else :
                innerR = float(self.getDetectorInnerR(dname, dtype))
                layers = dimensions.getparent().findall("layer")
                outerR = innerR
                for l in layers :
                    repeat = int(l.get("repeat"))
                    thickness = float(l.get("thickness"))
                    outerR = outerR + repeat*thickness
                return outerR
        return None
    
    def getDetectorInnerZ(self, dname, dtype) :
        dimensions = self.getDetectorDimmensions(dname, dtype)
        if dimensions is not None :
            return dimensions.get("inner_z")
        
    def getDetectorOuterZ(self, dname, dtype) :
        dimensions = self.getDetectorDimmensions(dname, dtype)
        if dimensions is not None :
            outerZ = dimensions.get("outer_z")
            if outerZ is not None :
                return float(outerZ)
            else :
                innerZ = float(self.getDetectorInnerZ(dname, dtype))
                layers = dimensions.getparent().findall("layer")
                outerZ = innerZ
                for l in layers :
                    repeat = int(l.get("repeat"))
                    thickness = float(l.get("thickness"))
                    outerZ = outerZ + repeat*thickness
                return outerZ
        return None

    def getEcalBarrelCosThetaRange(self) :
        ecalBarrelOuterR = float(self.getDetectorOuterR("EcalBarrel", "CalorimeterParameters"))
        ecalBarrelOuterZ = float(self.getDetectorOuterZ("EcalBarrel", "CalorimeterParameters"))
        maxCosTheta = cos(atan( ecalBarrelOuterR / ecalBarrelOuterZ ))
        return 0.05, maxCosTheta
    
    def getEcalEndcapCosThetaRange(self) :
        ecalEndcapOuterR = float(self.getDetectorOuterR("EcalEndcap", "CalorimeterParameters"))
        ecalEndcapOuterZ = float(self.getDetectorOuterZ("EcalEndcap", "CalorimeterParameters"))
        ecalEndcapInnerR = float(self.getDetectorInnerR("EcalEndcap", "CalorimeterParameters"))
        ecalEndcapInnerZ = float(self.getDetectorInnerZ("EcalEndcap", "CalorimeterParameters"))
        minCosTheta = cos(atan( ecalEndcapOuterR / ecalEndcapOuterZ ))
        maxCosTheta = cos(atan( ecalEndcapInnerR / ecalEndcapInnerZ ))
        return minCosTheta, maxCosTheta

    def getHcalBarrelCosThetaRange(self) :
        hcalBarrelOuterR = float(self.getDetectorOuterR("HcalBarrel", "CalorimeterParameters"))
        hcalBarrelOuterZ = float(self.getDetectorOuterZ("HcalBarrel", "CalorimeterParameters"))
        maxCosTheta = cos(atan( hcalBarrelOuterR / hcalBarrelOuterZ ))
        return 0.05, maxCosTheta

    def getHcalEndcapCosThetaRange(self) :
        hcalEndcapOuterR = float(self.getDetectorOuterR("HcalEndcap", "CalorimeterParameters"))
        hcalEndcapOuterZ = float(self.getDetectorOuterZ("HcalEndcap", "CalorimeterParameters"))
        hcalEndcapInnerR = float(self.getDetectorInnerR("HcalEndcap", "CalorimeterParameters"))
        hcalEndcapInnerZ = float(self.getDetectorInnerZ("HcalEndcap", "CalorimeterParameters"))
        minCosTheta = cos(atan( hcalEndcapOuterR / hcalEndcapOuterZ ))
        maxCosTheta = cos(atan( hcalEndcapInnerR / hcalEndcapInnerZ ))
        return minCosTheta, maxCosTheta
    
    """ Calculates and returns the following factor :
        f = (Abs_endcap / Abs_ring) * (Sens_ring / Sens_endcap)
    """
    def getCalorimeterGeometryFactor(self, endcapName, ringName):
        endcapDetector = self._getGearDetector(endcapName, "CalorimeterParameters")
        plugDetector = self._getGearDetector(ringName, "CalorimeterParameters")
        endcapAbsorberSum = 0
        endcapSensitiveSum = 0
        plugAbsorberSum = 0
        plugSensitiveSum = 0
        endcapLayers = endcapDetector.findall("layer")
        plugLayers = plugDetector.findall("layer")
        
        if not len(plugLayers) or not len(endcapLayers):
            raise RuntimeError("Couldn't evaluate geometry factory ! Layer list is empty")
            
        for layer in endcapLayers:
            repeat = int(layer.get("repeat"))
            absorberThickness = float(layer.get("absorberThickness"))
            thickness = float(layer.get("thickness"))
            senitiveThickness = thickness - absorberThickness
            endcapAbsorberSum = endcapAbsorberSum + absorberThickness*repeat
            endcapSensitiveSum = endcapSensitiveSum + senitiveThickness*repeat
            
        for layer in plugLayers:
            repeat = int(layer.get("repeat"))
            absorberThickness = float(layer.get("absorberThickness"))
            thickness = float(layer.get("thickness"))
            senitiveThickness = thickness - absorberThickness
            plugAbsorberSum = plugAbsorberSum + absorberThickness*repeat
            plugSensitiveSum = plugSensitiveSum + senitiveThickness*repeat
            
        return (endcapAbsorberSum / plugAbsorberSum) * (plugSensitiveSum / endcapSensitiveSum) 
        
        
    """ Calculates and returns the following factor in the ecal
        f = (Abs_endcap / Abs_ring) * (Sens_ring / Sens_endcap)
    """
    def getEcalGeometryFactor(self):
        return self.getCalorimeterGeometryFactor("EcalEndcap", "EcalPlug")
    
    """ Calculates and returns the following factor in the hcal
        f = (Abs_endcap / Abs_ring) * (Sens_ring / Sens_endcap)
    """
    def getHcalGeometryFactor(self):
        return self.getCalorimeterGeometryFactor("HcalEndcap", "HcalRing")
        
#