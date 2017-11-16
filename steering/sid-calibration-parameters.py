""" Parameter set used for calibrating SiD detector with the reconstruction chain in SiDPerformance.
    Supported models:
       - SiD_o2_v02
       - SiD_o3_v02
    Calibration for other models may be supported if the Marlin reco chain remains the same.
    For alternative support, please read the documentation in the 'doc' directory
    @author Remi Ete, DESY
"""

calibrationParameters = []

# calo hit digitization
calibrationParameters.append( ("ECalBarrelDigi", "calibration_mip", "EcalBarrelMip") )
calibrationParameters.append( ("ECalEndcapDigi", "calibration_mip", "EcalEndcapMip") )
calibrationParameters.append( ("HCalBarrelDigi", "calibration_mip", "HcalBarrelMip") )
calibrationParameters.append( ("HCalEndcapDigi", "calibration_mip", "HcalEndcapMip") )

# calo hit reconstruction
calibrationParameters.append( ("ECalBarrelReco", "calibration_factorsMipGev", "EcalBarrelEnergyFactors") )
calibrationParameters.append( ("ECalEndcapReco", "calibration_factorsMipGev", "EcalEndcapEnergyFactors") )
calibrationParameters.append( ("HCalBarrelReco", "calibration_factorsMipGev", "HcalBarrelEnergyFactors") )
calibrationParameters.append( ("HCalEndcapReco", "calibration_factorsMipGev", "HcalEndcapEnergyFactors") )

# muon calibration
calibrationParameters.append( ("MyDDSimpleMuonDigi", "CalibrMUON", "MuonCalibration") )

# PandoraPFA constants
calibrationParameters.append( ("MyDDMarlinPandora", "ECalToMipCalibration", "PandoraEcalToMip") )
calibrationParameters.append( ("MyDDMarlinPandora", "HCalToMipCalibration", "PandoraHcalToMip") )
calibrationParameters.append( ("MyDDMarlinPandora", "MuonToMipCalibration", "PandoraMuonToMip") )
calibrationParameters.append( ("MyDDMarlinPandora", "ECalToEMGeVCalibration", "PandoraEcalToEMScale") )
calibrationParameters.append( ("MyDDMarlinPandora", "HCalToEMGeVCalibration", "PandoraHcalToEMScale") )
calibrationParameters.append( ("MyDDMarlinPandora", "ECalToHadGeVCalibrationBarrel", "PandoraEcalToHadBarrelScale") )
calibrationParameters.append( ("MyDDMarlinPandora", "ECalToHadGeVCalibrationEndCap", "PandoraEcalToHadEndcapScale") )
calibrationParameters.append( ("MyDDMarlinPandora", "HCalToHadGeVCalibration", "PandoraHcalToHadScale") )


#
