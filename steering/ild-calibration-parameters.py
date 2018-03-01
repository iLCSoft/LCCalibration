""" Parameter set used for calibrating ILD models with the reconstruction chain in ILDConfig.
    Supported models:
       - ILD_l4_v02
       - ILD_s4_v02
    Calibration for other models may be supported if the Marlin reco chain remains the same.
    For alternative support, please read the documentation in the 'doc' directory
    @author Remi Ete, DESY
"""

calibrationParameters = []

# calo hit digitization
calibrationParameters.append( ("MyEcalBarrelDigi", "calibration_mip", "EcalBarrelMip") )
calibrationParameters.append( ("MyEcalEndcapDigi", "calibration_mip", "EcalEndcapMip") )
calibrationParameters.append( ("MyEcalRingDigi",   "calibration_mip", "EcalRingMip") )
calibrationParameters.append( ("MyHcalBarrelDigi", "calibration_mip", "HcalBarrelMip") )
calibrationParameters.append( ("MyHcalEndcapDigi", "calibration_mip", "HcalEndcapMip") )
calibrationParameters.append( ("MyHcalRingDigi",   "calibration_mip", "HcalRingMip") )

# calo hit reconstruction
calibrationParameters.append( ("MyEcalBarrelReco", "calibration_factorsMipGev", "EcalBarrelEnergyFactors") )
calibrationParameters.append( ("MyEcalEndcapReco", "calibration_factorsMipGev", "EcalEndcapEnergyFactors") )
calibrationParameters.append( ("MyEcalRingReco",   "calibration_factorsMipGev", "EcalRingEnergyFactors") )
calibrationParameters.append( ("MyHcalBarrelReco", "calibration_factorsMipGev", "HcalBarrelEnergyFactors") )
calibrationParameters.append( ("MyHcalEndcapReco", "calibration_factorsMipGev", "HcalEndcapEnergyFactors") )
calibrationParameters.append( ("MyHcalRingReco",   "calibration_factorsMipGev", "HcalRingEnergyFactors") )

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
calibrationParameters.append( ("MyDDMarlinPandora", "SoftwareCompensationWeights", "PandoraSoftwareCompensationWeights") )


#
