#!/usr/bin/python

""" Utility script that prints the cos theta ranges used for ecal/hcal barrel/endcap
    event selection while calibrating
    @author Remi Ete, DESY
"""

from calibration.GeometryInterface import *
from calibration.GearConverter import *
import argparse

parser = argparse.ArgumentParser("Running energy calibration:",
                                     formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("--compactFile", action="store", default="",
                        help="The compact XML file", required = True)

parser.add_argument("--gearConverterPlugin", action="store", default="default",
                        help="The gear plugin to convert the conmpact file to gear file", required = False)

parsed = parser.parse_args()

gearConverter = GearConverter()
gearConverter.setCompactFile(parsed.compactFile)
gearConverter.setPluginName(parsed.gearConverterPlugin)
gearFile = gearConverter.convertToGear()
geo = GeometryInterface(gearFile)

ddgeo = DDGeometryInterface(parsed.compactFile)


ebmin, ebmax = geo.getEcalBarrelCosThetaRange()
eemin, eemax = geo.getEcalEndcapCosThetaRange()
hbmin, hbmax = geo.getHcalBarrelCosThetaRange()
hemin, hemax = geo.getHcalEndcapCosThetaRange()
efactor = geo.getEcalGeometryFactor()
hfactor = geo.getHcalGeometryFactor()

print "======= Using Gear ======"
print "Ecal barrel cos theta range : [{0},{1}]".format(ebmin, ebmax)
print "Ecal endcap cos theta range : [{0},{1}]".format(eemin, eemax)
print "Hcal barrel cos theta range : [{0},{1}]".format(hbmin, hbmax)
print "Hcal endcap cos theta range : [{0},{1}]".format(hemin, hemax)
print "Ecal/Hcal geometry factors  : {0} / {1}".format(efactor, hfactor)

ddebmin, ddebmax = ddgeo.getEcalBarrelCosThetaRange()
ddeemin, ddeemax = ddgeo.getEcalEndcapCosThetaRange()
ddhbmin, ddhbmax = ddgeo.getHcalBarrelCosThetaRange()
ddhemin, ddhemax = ddgeo.getHcalEndcapCosThetaRange()
ddefactor = ddgeo.getEcalGeometryFactor()
ddhfactor = ddgeo.getHcalGeometryFactor()

print "======= Using DD4hep ======"
print "Ecal barrel cos theta range : [{0},{1}]".format(ddebmin, ddebmax)
print "Ecal endcap cos theta range : [{0},{1}]".format(ddeemin, ddeemax)
print "Hcal barrel cos theta range : [{0},{1}]".format(ddhbmin, ddhbmax)
print "Hcal endcap cos theta range : [{0},{1}]".format(ddhemin, ddhemax)
print "Ecal/Hcal geometry factors  : {0} / {1}".format(ddefactor, ddhfactor)

#