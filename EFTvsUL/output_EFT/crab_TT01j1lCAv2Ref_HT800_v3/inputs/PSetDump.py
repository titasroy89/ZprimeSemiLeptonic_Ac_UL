import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/pnfs/desy.de/cms/tier2/store/user/beozek/0230C4F8-6445-F74C-8409-27F77DFDE107.root'),
    skipEvents = cms.untracked.uint32(0)
)
process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.calibratedEgammaPatSettings = cms.PSet(
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    semiDeterministic = cms.bool(True)
)

process.calibratedEgammaSettings = cms.PSet(
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("reducedEcalRecHitsEE"),
    semiDeterministic = cms.bool(True)
)

process.combinedSecondaryVertexCommon = cms.PSet(
    SoftLeptonFlip = cms.bool(False),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)

process.ecalTrkCombinationRegression = cms.PSet(
    ecalTrkRegressionConfig = cms.PSet(
        ebHighEtForestName = cms.string('electron_eb_ECALTRK'),
        ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt'),
        eeHighEtForestName = cms.string('electron_ee_ECALTRK'),
        eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt'),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        lowEtHighEtBoundary = cms.double(50.0),
        rangeMaxHighEt = cms.double(3.0),
        rangeMaxLowEt = cms.double(3.0),
        rangeMinHighEt = cms.double(-1.0),
        rangeMinLowEt = cms.double(-1.0)
    ),
    ecalTrkRegressionUncertConfig = cms.PSet(
        ebHighEtForestName = cms.string('electron_eb_ECALTRK_var'),
        ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt_var'),
        eeHighEtForestName = cms.string('electron_ee_ECALTRK_var'),
        eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt_var'),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        lowEtHighEtBoundary = cms.double(50.0),
        rangeMaxHighEt = cms.double(0.5),
        rangeMaxLowEt = cms.double(0.5),
        rangeMinHighEt = cms.double(0.0002),
        rangeMinLowEt = cms.double(0.0002)
    ),
    maxEPDiffInSigmaForComb = cms.double(15.0),
    maxEcalEnergyForComb = cms.double(200.0),
    maxRelTrkMomErrForComb = cms.double(10.0),
    minEOverPForComb = cms.double(0.025)
)

process.ghostTrackCommon = cms.PSet(
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

process.mvaEleID_Fall17_iso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_iso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_noIso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_noIso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Spring16_GeneralPurpose_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16GeneralPurposeV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Spring16_HZZ_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16HZZV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Summer16UL_ID_ISO_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. & abs(superCluster.eta) < 0.800', 
        'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
        'pt < 10. & abs(superCluster.eta) >= 1.479', 
        'pt >= 10. & abs(superCluster.eta) < 0.800', 
        'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
        'pt >= 10. & abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Summer16ULIdIso'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Summer17UL_ID_ISO_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. & abs(superCluster.eta) < 0.800', 
        'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
        'pt < 10. & abs(superCluster.eta) >= 1.479', 
        'pt >= 10. & abs(superCluster.eta) < 0.800', 
        'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
        'pt >= 10. & abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Summer17ULIdIso'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Summer18UL_ID_ISO_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. & abs(superCluster.eta) < 0.800', 
        'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
        'pt < 10. & abs(superCluster.eta) >= 1.479', 
        'pt >= 10. & abs(superCluster.eta) < 0.800', 
        'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
        'pt >= 10. & abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Summer18ULIdIso'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_10.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v1p1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v1p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v1p1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.67, 0.54),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.27, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v2'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v2_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(0.42, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(-0.02, -0.26),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_Spring16_nonTrig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring16NonTrigV1'),
    nCategories = cms.int32(2),
    phoIsoCutoff = cms.double(2.5),
    phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz'
    )
)

process.options = cms.untracked.PSet(
    numberOfStreams = cms.untracked.uint32(0),
    wantSummary = cms.untracked.bool(False)
)

process.softPFElectronCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)

process.softPFMuonCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)

process.trackPseudoSelectionBlock = cms.PSet(
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.trackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.trkIsol03CfgV2 = cms.PSet(
    barrelCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.3),
        maxDZ = cms.double(0.1),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    ),
    endcapCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.3),
        maxDZ = cms.double(0.5),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    )
)

process.trkIsol04CfgV2 = cms.PSet(
    barrelCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.4),
        maxDZ = cms.double(0.1),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    ),
    endcapCuts = cms.PSet(
        algosToReject = cms.vstring(),
        allowedQualities = cms.vstring(),
        maxDPtPt = cms.double(0.1),
        maxDR = cms.double(0.4),
        maxDZ = cms.double(0.5),
        minDEta = cms.double(0.005),
        minDR = cms.double(0.0),
        minHits = cms.int32(8),
        minPixelHits = cms.int32(1),
        minPt = cms.double(1.0)
    )
)

process.variableJTAPars = cms.PSet(
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5)
)

process.c_vs_b_vars_vpset = cms.VPSet(
    cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSig_0'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip2dSig_1'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSig_0'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip3dSig_1'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPtRel_0'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPtRel_1'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPPar_0'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPPar_1'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackEtaRel_0'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackEtaRel_1'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDeltaR_0'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDeltaR_1'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackPtRatio_0'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackPtRatio_1'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(0),
        name = cms.string('trackPParRatio_0'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(1),
        name = cms.string('trackPParRatio_1'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackJetDist_0'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackJetDist_1'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDecayLenVal_0'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDecayLenVal_1'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(0),
        name = cms.string('jetNSecondaryVertices'),
        taggingVarName = cms.string('jetNSecondaryVertices')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('jetNTracks'),
        taggingVarName = cms.string('jetNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetEtRatio'),
        taggingVarName = cms.string('trackSumJetEtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetDeltaR'),
        taggingVarName = cms.string('trackSumJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexMass_0'),
        taggingVarName = cms.string('vertexMass')
    ), 
    cms.PSet(
        default = cms.double(-10),
        idx = cms.int32(0),
        name = cms.string('vertexEnergyRatio_0'),
        taggingVarName = cms.string('vertexEnergyRatio')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip2dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip3dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance2dSig_0'),
        taggingVarName = cms.string('flightDistance2dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance3dSig_0'),
        taggingVarName = cms.string('flightDistance3dSig')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexJetDeltaR_0'),
        taggingVarName = cms.string('vertexJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(0),
        idx = cms.int32(0),
        name = cms.string('vertexNTracks_0'),
        taggingVarName = cms.string('vertexNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('massVertexEnergyFraction_0'),
        taggingVarName = cms.string('massVertexEnergyFraction')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexBoostOverSqrtJetPt_0'),
        taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonPtRel_0'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonPtRel_1'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(0),
        name = cms.string('leptonSip3d_0'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(1),
        name = cms.string('leptonSip3d_1'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonDeltaR_0'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonDeltaR_1'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatioRel_0'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatioRel_1'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonEtaRel_0'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonEtaRel_1'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatio_0'),
        taggingVarName = cms.string('leptonRatio')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatio_1'),
        taggingVarName = cms.string('leptonRatio')
    )
)

process.c_vs_l_vars_vpset = cms.VPSet(
    cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSig_0'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip2dSig_1'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSig_0'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip3dSig_1'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPtRel_0'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPtRel_1'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPPar_0'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPPar_1'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackEtaRel_0'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackEtaRel_1'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDeltaR_0'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDeltaR_1'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackPtRatio_0'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackPtRatio_1'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(0),
        name = cms.string('trackPParRatio_0'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(1),
        name = cms.string('trackPParRatio_1'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackJetDist_0'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackJetDist_1'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDecayLenVal_0'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDecayLenVal_1'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(0),
        name = cms.string('jetNSecondaryVertices'),
        taggingVarName = cms.string('jetNSecondaryVertices')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('jetNTracks'),
        taggingVarName = cms.string('jetNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetEtRatio'),
        taggingVarName = cms.string('trackSumJetEtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetDeltaR'),
        taggingVarName = cms.string('trackSumJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexMass_0'),
        taggingVarName = cms.string('vertexMass')
    ), 
    cms.PSet(
        default = cms.double(-10),
        idx = cms.int32(0),
        name = cms.string('vertexEnergyRatio_0'),
        taggingVarName = cms.string('vertexEnergyRatio')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip2dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip3dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance2dSig_0'),
        taggingVarName = cms.string('flightDistance2dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance3dSig_0'),
        taggingVarName = cms.string('flightDistance3dSig')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexJetDeltaR_0'),
        taggingVarName = cms.string('vertexJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(0),
        idx = cms.int32(0),
        name = cms.string('vertexNTracks_0'),
        taggingVarName = cms.string('vertexNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('massVertexEnergyFraction_0'),
        taggingVarName = cms.string('massVertexEnergyFraction')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexBoostOverSqrtJetPt_0'),
        taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonPtRel_0'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonPtRel_1'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(0),
        name = cms.string('leptonSip3d_0'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(1),
        name = cms.string('leptonSip3d_1'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonDeltaR_0'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonDeltaR_1'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatioRel_0'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatioRel_1'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonEtaRel_0'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonEtaRel_1'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatio_0'),
        taggingVarName = cms.string('leptonRatio')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatio_1'),
        taggingVarName = cms.string('leptonRatio')
    )
)

process.mvaConfigsForEleProducer = cms.VPSet(
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16HZZV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16GeneralPurposeV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. & abs(superCluster.eta) < 0.800', 
            'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
            'pt < 10. & abs(superCluster.eta) >= 1.479', 
            'pt >= 10. & abs(superCluster.eta) < 0.800', 
            'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
            'pt >= 10. & abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Summer16ULIdIso'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. & abs(superCluster.eta) < 0.800', 
            'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
            'pt < 10. & abs(superCluster.eta) >= 1.479', 
            'pt >= 10. & abs(superCluster.eta) < 0.800', 
            'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
            'pt >= 10. & abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Summer17ULIdIso'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. & abs(superCluster.eta) < 0.800', 
            'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
            'pt < 10. & abs(superCluster.eta) >= 1.479', 
            'pt >= 10. & abs(superCluster.eta) < 0.800', 
            'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
            'pt >= 10. & abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Summer18ULIdIso'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_10.weights.xml.gz'
        )
    )
)

process.mvaConfigsForPhoProducer = cms.VPSet(
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('Run2Spring16NonTrigV1'),
        nCategories = cms.int32(2),
        phoIsoCutoff = cms.double(2.5),
        phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v1p1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v2'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz'
        )
    )
)

process.puppiCentral = cms.VPSet(cms.PSet(
    algoId = cms.int32(5),
    applyLowPUCorr = cms.bool(True),
    combOpt = cms.int32(0),
    cone = cms.double(0.4),
    rmsPtMin = cms.double(0.1),
    rmsScaleFactor = cms.double(1.0),
    useCharged = cms.bool(True)
))

process.puppiForward = cms.VPSet(cms.PSet(
    algoId = cms.int32(5),
    applyLowPUCorr = cms.bool(True),
    combOpt = cms.int32(0),
    cone = cms.double(0.4),
    rmsPtMin = cms.double(0.5),
    rmsScaleFactor = cms.double(1.0),
    useCharged = cms.bool(False)
))

process.ECFNbeta1Ak8SoftDropCHS = cms.EDProducer("ECFAdder",
    Njets = cms.vuint32(1, 2, 3),
    alpha = cms.double(1),
    beta = cms.double(1),
    cuts = cms.vstring(
        '', 
        '', 
        'pt > 250.000000'
    ),
    ecftype = cms.string('N'),
    src = cms.InputTag("ak8CHSJetsSoftDropforsub")
)


process.ECFNbeta1Ak8SoftDropGen = cms.EDProducer("ECFAdder",
    Njets = cms.vuint32(1, 2, 3),
    alpha = cms.double(1),
    beta = cms.double(1),
    cuts = cms.vstring(
        '', 
        '', 
        'pt > 250.000000'
    ),
    ecftype = cms.string('N'),
    src = cms.InputTag("ak8GenJetsSoftDropforsub")
)


process.ECFNbeta1Ak8SoftDropPuppi = cms.EDProducer("ECFAdder",
    Njets = cms.vuint32(1, 2, 3),
    alpha = cms.double(1),
    beta = cms.double(1),
    cuts = cms.vstring(
        '', 
        '', 
        'pt > 250.000000'
    ),
    ecftype = cms.string('N'),
    src = cms.InputTag("ak8PuppiJetsSoftDropforsub")
)


process.ECFNbeta2Ak8SoftDropCHS = cms.EDProducer("ECFAdder",
    Njets = cms.vuint32(1, 2, 3),
    alpha = cms.double(2.0),
    beta = cms.double(2.0),
    cuts = cms.vstring(
        '', 
        '', 
        'pt > 250.000000'
    ),
    ecftype = cms.string('N'),
    src = cms.InputTag("ak8CHSJetsSoftDropforsub")
)


process.ECFNbeta2Ak8SoftDropGen = cms.EDProducer("ECFAdder",
    Njets = cms.vuint32(1, 2, 3),
    alpha = cms.double(2.0),
    beta = cms.double(2.0),
    cuts = cms.vstring(
        '', 
        '', 
        'pt > 250.000000'
    ),
    ecftype = cms.string('N'),
    src = cms.InputTag("ak8GenJetsSoftDropforsub")
)


process.ECFNbeta2Ak8SoftDropPuppi = cms.EDProducer("ECFAdder",
    Njets = cms.vuint32(1, 2, 3),
    alpha = cms.double(2.0),
    beta = cms.double(2.0),
    cuts = cms.vstring(
        '', 
        '', 
        'pt > 250.000000'
    ),
    ecftype = cms.string('N'),
    src = cms.InputTag("ak8PuppiJetsSoftDropforsub")
)


process.NjettinessAk8CHS = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.8),
    Rcutoff = cms.double(999.0),
    akAxesR0 = cms.double(999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(999),
    src = cms.InputTag("ak8CHSJetsFat")
)


process.NjettinessAk8Gen = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.8),
    Rcutoff = cms.double(999.0),
    akAxesR0 = cms.double(999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(999),
    src = cms.InputTag("ak8GenJetsFat")
)


process.NjettinessAk8Puppi = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.8),
    Rcutoff = cms.double(999.0),
    akAxesR0 = cms.double(999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(999),
    src = cms.InputTag("ak8PuppiJetsFat")
)


process.NjettinessAk8SoftDropCHS = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.8),
    Rcutoff = cms.double(999.0),
    akAxesR0 = cms.double(999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(999),
    src = cms.InputTag("ak8CHSJetsSoftDropforsub")
)


process.NjettinessAk8SoftDropGen = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.8),
    Rcutoff = cms.double(999.0),
    akAxesR0 = cms.double(999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(999),
    src = cms.InputTag("ak8GenJetsSoftDropforsub")
)


process.NjettinessAk8SoftDropPuppi = cms.EDProducer("NjettinessAdder",
    Njets = cms.vuint32(1, 2, 3, 4),
    R0 = cms.double(0.8),
    Rcutoff = cms.double(999.0),
    akAxesR0 = cms.double(999.0),
    axesDefinition = cms.uint32(6),
    beta = cms.double(1.0),
    measureDefinition = cms.uint32(0),
    nPass = cms.int32(999),
    src = cms.InputTag("ak8PuppiJetsSoftDropforsub")
)


process.ak8CHSJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("chs"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8CHSJetsFat = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(120.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("chs"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8CHSJetsSoftDrop = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(120.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("chs"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8CHSJetsSoftDropforsub = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(120.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("chs"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    zcut = cms.double(0.1)
)


process.ak8GenJetsFat = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(120.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8GenJetsSoftDrop = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(120.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8GenJetsSoftDropforsub = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(120.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    zcut = cms.double(0.1)
)


process.ak8PuppiJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("puppi"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PuppiJetsFat = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(120.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("puppi"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.ak8PuppiJetsSoftDrop = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetCollInstanceName = cms.string('SubJets'),
    jetPtMin = cms.double(120.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("puppi"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    writeCompound = cms.bool(True),
    zcut = cms.double(0.1)
)


process.ak8PuppiJetsSoftDropforsub = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    R0 = cms.double(0.8),
    Rho_EtaMax = cms.double(4.4),
    beta = cms.double(0.0),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(120.0),
    jetType = cms.string('PFJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.8),
    src = cms.InputTag("puppi"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    useExplicitGhosts = cms.bool(True),
    useSoftDrop = cms.bool(True),
    voronoiRfact = cms.double(-0.9),
    zcut = cms.double(0.1)
)


process.calibratedElectrons = cms.EDProducer("CalibratedElectronProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    epCombConfig = cms.PSet(
        ecalTrkRegressionConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(3.0),
            rangeMaxLowEt = cms.double(3.0),
            rangeMinHighEt = cms.double(-1.0),
            rangeMinLowEt = cms.double(-1.0)
        ),
        ecalTrkRegressionUncertConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK_var'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt_var'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK_var'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt_var'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(0.5),
            rangeMaxLowEt = cms.double(0.5),
            rangeMinHighEt = cms.double(0.0002),
            rangeMinLowEt = cms.double(0.0002)
        ),
        maxEPDiffInSigmaForComb = cms.double(15.0),
        maxEcalEnergyForComb = cms.double(200.0),
        maxRelTrkMomErrForComb = cms.double(10.0),
        minEOverPForComb = cms.double(0.025)
    ),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("reducedEcalRecHitsEE"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("gedGsfElectrons")
)


process.calibratedPatElectrons = cms.EDProducer("CalibratedPatElectronProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2018_Step2Closure_CoarseEtaR9Gain_v2'),
    epCombConfig = cms.PSet(
        ecalTrkRegressionConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(3.0),
            rangeMaxLowEt = cms.double(3.0),
            rangeMinHighEt = cms.double(-1.0),
            rangeMinLowEt = cms.double(-1.0)
        ),
        ecalTrkRegressionUncertConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK_var'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt_var'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK_var'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt_var'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(0.5),
            rangeMaxLowEt = cms.double(0.5),
            rangeMinHighEt = cms.double(0.0002),
            rangeMinLowEt = cms.double(0.0002)
        ),
        maxEPDiffInSigmaForComb = cms.double(15.0),
        maxEcalEnergyForComb = cms.double(200.0),
        maxRelTrkMomErrForComb = cms.double(10.0),
        minEOverPForComb = cms.double(0.025)
    ),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(False),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("updatedElectrons")
)


process.calibratedPatPhotons = cms.EDProducer("CalibratedPatPhotonProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2018_Step2Closure_CoarseEtaR9Gain_v2'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(False),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("updatedPhotons")
)


process.calibratedPhotons = cms.EDProducer("CalibratedPhotonProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("reducedEcalRecHitsEE"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("gedPhotons")
)


process.convertedPackedPFCandidatePtrs = cms.EDProducer("PFCandidateFwdPtrProducer",
    src = cms.InputTag("convertedPackedPFCandidates")
)


process.convertedPackedPFCandidates = cms.EDProducer("convertPackedCandToPFCand",
    src = cms.InputTag("packedPFCandidates")
)


process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(35.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.4442),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.566)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.004),
                        dEtaInSeedCutValueEE = cms.double(0.006),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.06),
                        dPhiInCutValueEE = cms.double(0.06),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaWithSatCut'),
                        isIgnored = cms.bool(False),
                        maxNrSatCrysIn5x5EB = cms.int32(0),
                        maxNrSatCrysIn5x5EE = cms.int32(0),
                        maxSigmaIEtaIEtaEB = cms.double(9999),
                        maxSigmaIEtaIEtaEE = cms.double(0.03),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('GsfEleFull5x5E2x5OverE5x5WithSatCut'),
                        isIgnored = cms.bool(False),
                        maxNrSatCrysIn5x5EB = cms.int32(0),
                        maxNrSatCrysIn5x5EE = cms.int32(0),
                        minE1x5OverE5x5EB = cms.double(0.83),
                        minE1x5OverE5x5EE = cms.double(-1.0),
                        minE2x5OverE5x5EB = cms.double(0.94),
                        minE2x5OverE5x5EE = cms.double(-1.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.0),
                        constTermEE = cms.double(5),
                        cutName = cms.string('GsfEleHadronicOverEMLinearCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.05),
                        slopeTermEE = cms.double(0.05)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(5.0),
                        constTermEE = cms.double(5.0),
                        cutName = cms.string('GsfEleTrkPtIsoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.0),
                        slopeTermEE = cms.double(0.0),
                        useHEEPIso = cms.bool(True)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.0),
                        constTermEE = cms.double(2.5),
                        cutName = cms.string('GsfEleEmHadD1IsoRhoCut'),
                        energyType = cms.string('EcalTrk'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        rhoConstant = cms.double(0.28),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(50.0),
                        slopeTermEB = cms.double(0.03),
                        slopeTermEE = cms.double(0.03)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.02),
                        dxyCutValueEE = cms.double(0.05),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEcalDrivenCut'),
                        ecalDrivenEB = cms.int32(1),
                        ecalDrivenEE = cms.int32(1),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('heepElectronID-HEEPV70'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('49b6b60e9f16727f241eb34b9d345a8f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00387),
                        dEtaInSeedCutValueEE = cms.double(0.0072),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0716),
                        dPhiInCutValueEE = cms.double(0.147),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0356),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0414),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0875),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.133),
                        isoCutEBLowPt = cms.double(0.133),
                        isoCutEEHighPt = cms.double(0.146),
                        isoCutEELowPt = cms.double(0.146),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0b8456d622494441fe713a6858e0f7c1'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00365),
                        dEtaInSeedCutValueEE = cms.double(0.00625),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0588),
                        dPhiInCutValueEE = cms.double(0.0355),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0309),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0327),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0335),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0718),
                        isoCutEBLowPt = cms.double(0.0718),
                        isoCutEEHighPt = cms.double(0.143),
                        isoCutEELowPt = cms.double(0.143),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('a238ee70910de53d36866e89768500e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00353),
                        dEtaInSeedCutValueEE = cms.double(0.00567),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0499),
                        dPhiInCutValueEE = cms.double(0.0165),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0305),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0278),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0158),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0361),
                        isoCutEBLowPt = cms.double(0.0361),
                        isoCutEEHighPt = cms.double(0.094),
                        isoCutEELowPt = cms.double(0.094),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4acb2d2796efde7fba75380ce8823fc2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00523),
                        dEtaInSeedCutValueEE = cms.double(0.00984),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.159),
                        dPhiInCutValueEE = cms.double(0.157),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0128),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0445),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0962),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.168),
                        isoCutEBLowPt = cms.double(0.168),
                        isoCutEEHighPt = cms.double(0.185),
                        isoCutEELowPt = cms.double(0.185),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('43be9b381a8d9b0910b7f81a5ad8ff3a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9530240956555949 - exp(-pt / 2.7591425841003647) *  0.4669644718545271', 
                        '0.9336564763961019 - exp(-pt /  2.709276284272272) * 0.33512286599215946', 
                        '0.9313133688365339 - exp(-pt / 1.5821934800715558) *  3.8889462619659265', 
                        '0.9825268564943458 - exp(-pt /  8.702601455860762) *  1.1974861596609097', 
                        '0.9727509457929913 - exp(-pt /  8.179525631018565) *  1.7111755094657688', 
                        '0.9562619539540145 - exp(-pt /  8.109845366281608) *   3.013927699126942'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9165112826974601 - exp(-pt / 2.7381703555094217) *    1.03549199648109', 
                        '0.8655738322220173 - exp(-pt / 2.4027944652597073) *  0.7975615613282494', 
                        '-3016.035055227131 - exp(-pt / -52140.61856333602) * -3016.3029387236506', 
                        '0.9616542816132922 - exp(-pt /  8.757943837889817) *  3.1390200321591206', 
                        '0.9319258011430132 - exp(-pt /  8.846057432565809) *  3.5985063793347787', 
                        '0.8899260780999244 - exp(-pt / 10.124234115859881) *   4.352791250718547'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '-0.13285867293779202', 
                        '-0.31765300958836074', 
                        '-0.0799205914718861', 
                        '-0.856871961305474', 
                        '-0.8107642141584835', 
                        '-0.7179265933023059'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9725509559754997 - exp(-pt /  2.976593261509491) *  0.2653858736397496', 
                        '0.9508038141601247 - exp(-pt / 2.6633500558725713) *  0.2355820499260076', 
                        '0.9365037167596238 - exp(-pt / 1.5765442323949856) *   3.067015289215309', 
                        '0.9896562087723659 - exp(-pt / 10.342490511998674) * 0.40204156417414094', 
                        '0.9819232656533827 - exp(-pt /   9.05548836482051) *   0.772674931169389', 
                        '0.9625098201744635 - exp(-pt /   8.42589315557279) *  2.2916152615134173'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9387070396095831 - exp(-pt /   2.6525585228167636) *  0.8222647164151365', 
                        '0.8948802925677235 - exp(-pt /   2.7645670358783523) *  0.4123381218697539', 
                        '-1830.8583661119892 - exp(-pt /   -36578.11055382301) * -1831.2083578116517', 
                        '0.9717674837607253 - exp(-pt /    8.912850985100356) *  1.9712414940437244', 
                        '0.9458745023265976 - exp(-pt /     8.83104420392795) *    2.40849932040698', 
                        '0.8979112012086751 - exp(-pt /    9.814082144168015) *   4.171581694893849'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '-0.09564086146419018', 
                        '-0.28229916981926795', 
                        '-0.05466682296962322', 
                        '-0.833466688584422', 
                        '-0.7677000247570116', 
                        '-0.6917305995653829'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00477),
                        dEtaInSeedCutValueEE = cms.double(0.00868),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.222),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0314),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.298),
                        hadronicOverEMCutValueEE = cms.double(0.101),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.241),
                        eInverseMinusPInverseCutValueEE = cms.double(0.14),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0994),
                        isoCutEBLowPt = cms.double(0.0994),
                        isoCutEEHighPt = cms.double(0.107),
                        isoCutEELowPt = cms.double(0.107),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c1c4c739f1ba0791d40168c123183475'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00311),
                        dEtaInSeedCutValueEE = cms.double(0.00609),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.103),
                        dPhiInCutValueEE = cms.double(0.045),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0298),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.253),
                        hadronicOverEMCutValueEE = cms.double(0.0878),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.134),
                        eInverseMinusPInverseCutValueEE = cms.double(0.13),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0695),
                        isoCutEBLowPt = cms.double(0.0695),
                        isoCutEEHighPt = cms.double(0.0821),
                        isoCutEELowPt = cms.double(0.0821),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('71b43f74a27d2fd3d27416afd22e8692'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00308),
                        dEtaInSeedCutValueEE = cms.double(0.00605),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0816),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0292),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0414),
                        hadronicOverEMCutValueEE = cms.double(0.0641),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0129),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0588),
                        isoCutEBLowPt = cms.double(0.0588),
                        isoCutEEHighPt = cms.double(0.0571),
                        isoCutEELowPt = cms.double(0.0571),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('ca2a9db2976d80ba2c13f9bfccdc32f2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00749),
                        dEtaInSeedCutValueEE = cms.double(0.00895),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.228),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0115),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.037),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.356),
                        hadronicOverEMCutValueEE = cms.double(0.211),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.299),
                        eInverseMinusPInverseCutValueEE = cms.double(0.15),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.175),
                        isoCutEBLowPt = cms.double(0.175),
                        isoCutEEHighPt = cms.double(0.159),
                        isoCutEELowPt = cms.double(0.159),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0025c1841da1ab64a08d703ded72409b'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.940962684155', 
                        '0.899208843708', 
                        '0.758484721184'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('b490bc0b0af2d5f3e9efea562370af2a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.836695742607', 
                        '0.715337944031', 
                        '0.356799721718'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('14c153aaf3c207deb3ad4932586647a7'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
                    mvaCuts = cms.vstring(
                        '-0.211', 
                        '-0.396', 
                        '-0.215', 
                        '-0.870', 
                        '-0.838', 
                        '-0.763'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-HZZ-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('1797cc03eb62387e10266fca72ea10cd'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00377),
                        dEtaInSeedCutValueEE = cms.double(0.00674),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0884),
                        dPhiInCutValueEE = cms.double(0.169),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0112),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0425),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0441),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.111),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.112),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.108),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('5547e2c8b5c222192519c41bff05bc2e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.0032),
                        dEtaInSeedCutValueEE = cms.double(0.00632),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0547),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0106),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0387),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.046),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0275),
                        endcapCE = cms.double(2.52),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.184),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0721),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.0478),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0658),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('48702f025a8df2c527f53927af8b66d0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00255),
                        dEtaInSeedCutValueEE = cms.double(0.00501),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.022),
                        dPhiInCutValueEE = cms.double(0.0236),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0353),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.15),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0188),
                        endcapCE = cms.double(2.06),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.159),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0197),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.0287),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0445),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c06761e199f084f5b0f7868ac48a3e19'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00463),
                        dEtaInSeedCutValueEE = cms.double(0.00814),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.148),
                        dPhiInCutValueEE = cms.double(0.19),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0126),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0457),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.209),
                        eInverseMinusPInverseCutValueEE = cms.double(0.132),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.198),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.203),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('74e217e3ece16b49bd337026a29fc3e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '3.26449620468 - exp(-pt / 3.32657149223) * 8.84669783568', 
                        '2.83557838497 - exp(-pt / 2.15150487651) * 11.0978016567', 
                        '2.91994945177 - exp(-pt / 1.69875477522) * 24.024807824', 
                        '7.1336238874 - exp(-pt / 16.5605268797) * 8.22531222391', 
                        '6.18638275782 - exp(-pt / 15.2694634284) * 7.49764565324', 
                        '5.43175865738 - exp(-pt / 15.4290075949) * 7.56899692285'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '2.77072387339 - exp(-pt / 3.81500912145) * 8.16304860178', 
                        '1.85602317813 - exp(-pt / 2.18697654938) * 11.8568936824', 
                        '1.73489307814 - exp(-pt / 2.0163211971) * 17.013880078', 
                        '5.9175992258 - exp(-pt / 13.4807294538) * 9.31966232685', 
                        '5.01598837255 - exp(-pt / 13.1280451502) * 8.79418193765', 
                        '4.16921343208 - exp(-pt / 13.2017224621) * 9.00720913211'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '0.894411158628', 
                        '0.791966464633', 
                        '1.47104857173', 
                        '-0.293962958665', 
                        '-0.250424758584', 
                        '-0.130985179031'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '3.53495358797 - exp(-pt / 3.07272325141) * 9.94262764352', 
                        '3.06015605623 - exp(-pt / 1.95572234114) * 14.3091184421', 
                        '3.02052519639 - exp(-pt / 1.59784164742) * 28.719380105', 
                        '7.35752275071 - exp(-pt / 15.87907864) * 7.61288809226', 
                        '6.41811074032 - exp(-pt / 14.730562874) * 6.96387331587', 
                        '5.64936312428 - exp(-pt / 16.3664949747) * 7.19607610311'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '2.84704783417 - exp(-pt / 3.32529515837) * 9.38050947827', 
                        '2.03833922005 - exp(-pt / 1.93288758682) * 15.364588247', 
                        '1.82704158461 - exp(-pt / 1.89796754399) * 19.1236071158', 
                        '6.12931925263 - exp(-pt / 13.281753835) * 8.71138432196', 
                        '5.26289004857 - exp(-pt / 13.2154971491) * 8.0997882835', 
                        '4.37338792902 - exp(-pt / 14.0776094696) * 8.48513324496'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '1.26402092475', 
                        '1.17808089508', 
                        '1.33051972806', 
                        '2.36464785939', 
                        '2.07880614597', 
                        '1.08080644615'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wpHZZ'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '0.700642584415', 
                        '0.739335420875', 
                        '1.45390456109', 
                        '-0.146270871164', 
                        '-0.0315850882679', 
                        '-0.0321841194737'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        )
    ),
    physicsObjectSrc = cms.InputTag("updatedElectrons")
)


process.egmPhotonIDs = cms.EDProducer("VersionedPhotonIdProducer",
    physicsObjectIDs = cms.VPSet(
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.105),
                        hadronicOverEMCutValueEE = cms.double(0.029),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0103),
                        cutValueEE = cms.double(0.0276),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.839),
                        constTermEE = cms.double(2.15),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(9.188),
                        constTermEE = cms.double(10.471),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0126),
                        linearPtTermEE = cms.double(0.0119),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.6e-05),
                        quadPtTermEE = cms.double(2.5e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.956),
                        constTermEE = cms.double(4.895),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0035),
                        linearPtTermEE = cms.double(0.004),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('45515ee95e01fa36972ff7ba69186c97'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.035),
                        hadronicOverEMCutValueEE = cms.double(0.027),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0103),
                        cutValueEE = cms.double(0.0271),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.416),
                        constTermEE = cms.double(1.012),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.491),
                        constTermEE = cms.double(9.131),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0126),
                        linearPtTermEE = cms.double(0.0119),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.6e-05),
                        quadPtTermEE = cms.double(2.5e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.952),
                        constTermEE = cms.double(4.095),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.004),
                        linearPtTermEE = cms.double(0.004),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('772f7921fa146b630e4dbe79e475a421'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02),
                        hadronicOverEMCutValueEE = cms.double(0.025),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0103),
                        cutValueEE = cms.double(0.0271),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.158),
                        constTermEE = cms.double(0.575),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.267),
                        constTermEE = cms.double(8.916),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0126),
                        linearPtTermEE = cms.double(0.0119),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.6e-05),
                        quadPtTermEE = cms.double(2.5e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.065),
                        constTermEE = cms.double(3.272),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0035),
                        linearPtTermEE = cms.double(0.004),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('e260fee6f9011fb13ff56d45cccd21c5'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    mvaCuts = cms.vdouble(0.67, 0.54),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('56138c4a3ac3c0bffc7f01c187063102'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    mvaCuts = cms.vdouble(0.27, 0.14),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('1120f91d15f68bf61b5f08958bf4f435'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0597),
                        hadronicOverEMCutValueEE = cms.double(0.0481),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01031),
                        cutValueEE = cms.double(0.03013),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.295),
                        constTermEE = cms.double(1.011),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(10.91),
                        constTermEE = cms.double(5.931),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0148),
                        linearPtTermEE = cms.double(0.0163),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(1.7e-05),
                        quadPtTermEE = cms.double(1.4e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(3.63),
                        constTermEE = cms.double(6.641),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0047),
                        linearPtTermEE = cms.double(0.0034),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('d6ce6a4f3476294bf0a3261e00170daf'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0396),
                        hadronicOverEMCutValueEE = cms.double(0.0219),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01022),
                        cutValueEE = cms.double(0.03001),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.441),
                        constTermEE = cms.double(0.442),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.725),
                        constTermEE = cms.double(1.715),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0148),
                        linearPtTermEE = cms.double(0.0163),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(1.7e-05),
                        quadPtTermEE = cms.double(1.4e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.571),
                        constTermEE = cms.double(3.863),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0047),
                        linearPtTermEE = cms.double(0.0034),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c739cfd0b6287b8586da187c06d4053f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0269),
                        hadronicOverEMCutValueEE = cms.double(0.0213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00994),
                        cutValueEE = cms.double(0.03),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.202),
                        constTermEE = cms.double(0.034),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.264),
                        constTermEE = cms.double(0.586),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0148),
                        linearPtTermEE = cms.double(0.0163),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(1.7e-05),
                        quadPtTermEE = cms.double(1.4e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.362),
                        constTermEE = cms.double(2.617),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0047),
                        linearPtTermEE = cms.double(0.0034),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('bdb623bdb1a15c13545020a919dd9530'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.68, 0.6),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('beb95233f7d1e033ad9e20cf3d804ba0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.2, 0.2),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('36efe663348f95de0bc1cfa8dc7fa8fe'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    mvaCuts = cms.vdouble(0.42, 0.14),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
                isPOGApproved = cms.bool(True)
            ),
            idMD5 = cms.string('3013ddce7a3ad8b54827c29f5d92282e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    mvaCuts = cms.vdouble(-0.02, -0.26),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
                isPOGApproved = cms.bool(True)
            ),
            idMD5 = cms.string('5c06832759b1faf7dd6fc45ed1aef3a2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.04596),
                        hadronicOverEMCutValueEE = cms.double(0.059),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0106),
                        cutValueEE = cms.double(0.0272),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.694),
                        constTermEE = cms.double(2.089),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(24.032),
                        constTermEE = cms.double(19.722),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.01512),
                        linearPtTermEE = cms.double(0.0117),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.259e-05),
                        quadPtTermEE = cms.double(2.3e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.876),
                        constTermEE = cms.double(4.162),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.004017),
                        linearPtTermEE = cms.double(0.0037),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4578dfcceb0bfd1ba5ac28973c843fd0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02197),
                        hadronicOverEMCutValueEE = cms.double(0.0326),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01015),
                        cutValueEE = cms.double(0.0272),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.141),
                        constTermEE = cms.double(1.051),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.189),
                        constTermEE = cms.double(2.718),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.01512),
                        linearPtTermEE = cms.double(0.0117),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.259e-05),
                        quadPtTermEE = cms.double(2.3e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.08),
                        constTermEE = cms.double(3.867),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.004017),
                        linearPtTermEE = cms.double(0.0037),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('28b186c301061395f394a81266c8d7de'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02148),
                        hadronicOverEMCutValueEE = cms.double(0.0321),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00996),
                        cutValueEE = cms.double(0.0271),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.65),
                        constTermEE = cms.double(0.517),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.317),
                        constTermEE = cms.double(2.716),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.01512),
                        linearPtTermEE = cms.double(0.0117),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.259e-05),
                        quadPtTermEE = cms.double(2.3e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.044),
                        constTermEE = cms.double(3.032),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.004017),
                        linearPtTermEE = cms.double(0.0037),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('6f4f0ed6a8bf2de8dcf0bc3349b0546d'),
            isPOGApproved = cms.untracked.bool(True)
        )
    ),
    physicsObjectSrc = cms.InputTag("updatedPhotons")
)


process.egmPhotonIsolation = cms.EDProducer("CITKPFIsolationSumProducer",
    isolationConeDefinitions = cms.VPSet(
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('h+'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('h0'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        ), 
        cms.PSet(
            coneSize = cms.double(0.3),
            isolateAgainst = cms.string('gamma'),
            isolationAlgo = cms.string('PhotonPFIsolationWithMapBasedVeto'),
            miniAODVertexCodes = cms.vuint32(2, 3),
            particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
            vertexIndex = cms.int32(0)
        )
    ),
    srcForIsolationCone = cms.InputTag("packedPFCandidates"),
    srcToIsolate = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.elPFMiniIsoDepositCHSTAND = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedElectrons"),
    trackType = cms.string('candidate')
)


process.elPFMiniIsoDepositNHPFWGT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfWeightedNeutralHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedElectrons"),
    trackType = cms.string('candidate')
)


process.elPFMiniIsoDepositNHSTAND = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedElectrons"),
    trackType = cms.string('candidate')
)


process.elPFMiniIsoDepositPUSTAND = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticles")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedElectrons"),
    trackType = cms.string('candidate')
)


process.elPFMiniIsoDepositPhPFWGT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfWeightedPhotons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedElectrons"),
    trackType = cms.string('candidate')
)


process.elPFMiniIsoDepositPhSTAND = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('PFCandWithSuperClusterExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(0),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        MissHitSCMatch_Veto = cms.bool(True),
        SCMatch_Veto = cms.bool(False),
        inputCandView = cms.InputTag("pfAllPhotons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedElectrons"),
    trackType = cms.string('candidate')
)


process.elPFMiniIsoValueCHSTAND = cms.EDProducer("PFCandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFMiniIsoDepositCHSTAND"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFMiniIsoValueNHPFWGT = cms.EDProducer("PFCandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFMiniIsoDepositNHPFWGT"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFMiniIsoValueNHSTAND = cms.EDProducer("PFCandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFMiniIsoDepositNHSTAND"),
        vetos = cms.vstring(),
        weight = cms.string('1')
    ))
)


process.elPFMiniIsoValuePUSTAND = cms.EDProducer("PFCandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFMiniIsoDepositPUSTAND"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.015)'),
        weight = cms.string('1')
    ))
)


process.elPFMiniIsoValuePhPFWGT = cms.EDProducer("PFCandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFMiniIsoDepositPhPFWGT"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.elPFMiniIsoValuePhSTAND = cms.EDProducer("PFCandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        PivotCoordinatesForEBEE = cms.bool(True),
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("elPFMiniIsoDepositPhSTAND"),
        vetos = cms.vstring('EcalEndcaps:ConeVeto(0.08)'),
        weight = cms.string('1')
    ))
)


process.electronGenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.1),
    src = cms.InputTag("ElectronPhotonGenParticles"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.electronMVATOP = cms.EDProducer("EleBaseMVAValueMapProducer",
    isClassifier = cms.bool(True),
    name = cms.string('electronMVATOP'),
    src = cms.InputTag("slimmedElectronsWithUserData"),
    variables = cms.PSet(
        bTagDeepJetClosestJet = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?max(userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probbb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:problepb\'),0.0):0.0"),
        dxylog = cms.string("log(abs(dB(\'PV2D\')))"),
        dzlog = cms.string("log(abs(dB(\'PVDZ\')))"),
        etaAbs = cms.string('abs(eta)'),
        miniIsoCharged = cms.string("userFloat(\'miniIsoChg\')/pt"),
        miniIsoNeutral = cms.string("(userFloat(\'miniIsoAll\')-userFloat(\'miniIsoChg\'))/pt"),
        mvaIdFall17v2noIso = cms.string("userFloat(\'mvaFall17V2noIso\')"),
        pTRel = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'ptRel\'):0"),
        pt = cms.string("pt/userFloat(\'ecalTrkEnergyPostCorr\')*userFloat(\'ecalTrkEnergyPreCorr\')"),
        ptRatio = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?min(userFloat(\'ptRatio\'),1.5):1.0/(1.0+userFloat(\'PFIsoAll04\')/pt)"),
        relIso = cms.string("userFloat(\'PFIsoAll\')/pt"),
        sip3d = cms.string("abs(dB(\'PV3D\')/edB(\'PV3D\'))"),
        trackMultClosestJet = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'jetNDauChargedMVASel\'):0")
    ),
    variablesOrder = cms.vstring(
        'dxylog', 
        'miniIsoCharged', 
        'miniIsoNeutral', 
        'pTRel', 
        'sip3d', 
        'mvaIdFall17v2noIso', 
        'ptRatio', 
        'bTagDeepJetClosestJet', 
        'pt', 
        'trackMultClosestJet', 
        'etaAbs', 
        'dzlog', 
        'relIso'
    ),
    weightFile = cms.FileInPath('UHH2/common/data/UL16preVFP/TMVA_BDTG_TOP_elec_2016.weights.xml')
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16HZZV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16GeneralPurposeV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. & abs(superCluster.eta) < 0.800', 
                'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
                'pt < 10. & abs(superCluster.eta) >= 1.479', 
                'pt >= 10. & abs(superCluster.eta) < 0.800', 
                'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
                'pt >= 10. & abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Summer16ULIdIso'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_16UL_ID_ISO/EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. & abs(superCluster.eta) < 0.800', 
                'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
                'pt < 10. & abs(superCluster.eta) >= 1.479', 
                'pt >= 10. & abs(superCluster.eta) < 0.800', 
                'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
                'pt >= 10. & abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Summer17ULIdIso'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_17UL_ID_ISO/EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. & abs(superCluster.eta) < 0.800', 
                'pt < 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
                'pt < 10. & abs(superCluster.eta) >= 1.479', 
                'pt >= 10. & abs(superCluster.eta) < 0.800', 
                'pt >= 10. & abs(superCluster.eta) >= 0.800 & abs(superCluster.eta) < 1.479', 
                'pt >= 10. & abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Summer18ULIdIso'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Summer_18UL_ID_ISO/EE_10.weights.xml.gz'
            )
        )
    ),
    src = cms.InputTag(""),
    srcMiniAOD = cms.InputTag("updatedElectrons")
)


process.electronMVAValueMapProducerv2 = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
        )
    )),
    src = cms.InputTag("slimmedElectronsData")
)


process.fixedGridRhoFastjetAll = cms.EDProducer("FixedGridRhoProducerFastjet",
    gridSpacing = cms.double(0.55),
    maxRapidity = cms.double(5.0),
    pfCandidatesTag = cms.InputTag("packedPFCandidates")
)


process.genXCone23TopJets = cms.EDProducer("GenXConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    DRLeptonJet = cms.double(999),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(3),
    RJets = cms.double(1.2),
    RSubJets = cms.double(0.4),
    doLeptonSpecific = cms.bool(True),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    usePseudoXCone = cms.bool(True)
)


process.genXCone2jets04 = cms.EDProducer("GenXConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    DRLeptonJet = cms.double(999),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.4),
    RSubJets = cms.double(0.2),
    doLeptonSpecific = cms.bool(False),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    usePseudoXCone = cms.bool(True)
)


process.genXCone2jets08 = cms.EDProducer("GenXConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    DRLeptonJet = cms.double(999),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.8),
    RSubJets = cms.double(0.4),
    doLeptonSpecific = cms.bool(False),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    usePseudoXCone = cms.bool(True)
)


process.genXCone33TopJets = cms.EDProducer("GenXConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(3),
    RJets = cms.double(1.2),
    RSubJets = cms.double(0.4),
    doLeptonSpecific = cms.bool(False),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    usePseudoXCone = cms.bool(True)
)


process.genXCone3jets04 = cms.EDProducer("GenXConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    DRLeptonJet = cms.double(999),
    NJets = cms.uint32(3),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.4),
    RSubJets = cms.double(0.2),
    doLeptonSpecific = cms.bool(False),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    usePseudoXCone = cms.bool(True)
)


process.genXCone3jets08 = cms.EDProducer("GenXConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    DRLeptonJet = cms.double(999),
    NJets = cms.uint32(3),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.8),
    RSubJets = cms.double(0.4),
    doLeptonSpecific = cms.bool(False),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    usePseudoXCone = cms.bool(True)
)


process.genXCone4jets04 = cms.EDProducer("GenXConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    DRLeptonJet = cms.double(999),
    NJets = cms.uint32(4),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.4),
    RSubJets = cms.double(0.2),
    doLeptonSpecific = cms.bool(False),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    usePseudoXCone = cms.bool(True)
)


process.genXCone4jets08 = cms.EDProducer("GenXConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    DRLeptonJet = cms.double(999),
    NJets = cms.uint32(4),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.8),
    RSubJets = cms.double(0.4),
    doLeptonSpecific = cms.bool(False),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    usePseudoXCone = cms.bool(True)
)


process.heepIDVarValueMaps = cms.EDProducer("ElectronHEEPIDValueMapProducer",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    candVetosAOD = cms.vstring(
        'ELES', 
        'NONE', 
        'NONELES'
    ),
    candVetosMiniAOD = cms.vstring(
        'ELES', 
        'NONE', 
        'NONELES'
    ),
    candsAOD = cms.VInputTag("packedCandsForTkIso", "lostTracksForTkIso", "lostTracksForTkIso:eleTracks"),
    candsMiniAOD = cms.VInputTag("packedPFCandidates", "lostTracks", "lostTracks:eleTracks"),
    dataFormat = cms.int32(2),
    ebRecHitsAOD = cms.InputTag("reducedEcalRecHitsEB"),
    ebRecHitsMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeRecHitsAOD = cms.InputTag("reducedEcalRecHitsEB"),
    eeRecHitsMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    elesAOD = cms.InputTag("gedGsfElectrons"),
    elesMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
    makeTrkIso04 = cms.bool(True),
    trkIso04Config = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.1),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.4),
            maxDZ = cms.double(0.5),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        )
    ),
    trkIsoConfig = cms.PSet(
        barrelCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.1),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        ),
        endcapCuts = cms.PSet(
            algosToReject = cms.vstring(),
            allowedQualities = cms.vstring(),
            maxDPtPt = cms.double(0.1),
            maxDR = cms.double(0.3),
            maxDZ = cms.double(0.5),
            minDEta = cms.double(0.005),
            minDR = cms.double(0.0),
            minHits = cms.int32(8),
            minPixelHits = cms.int32(1),
            minPt = cms.double(1.0)
        )
    )
)


process.hotvrGen = cms.EDProducer("GenHOTVRProducer",
    hotvr_pt_min = cms.double(30),
    max_r = cms.double(1.5),
    min_r = cms.double(0.1),
    mu = cms.double(30),
    rho = cms.double(600),
    src = cms.InputTag("packedGenParticlesForJetsNoNu"),
    theta = cms.double(0.7)
)


process.hotvrPuppi = cms.EDProducer("HOTVRProducer",
    doRekey = cms.bool(True),
    rekeyCandidateSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("puppi")
)


process.isoForEle = cms.EDProducer("EleIsoValueMapProducer",
    EAFile_MiniIso = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
    EAFile_PFIso = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
    relative = cms.bool(False),
    rho_MiniIso = cms.InputTag("fixedGridRhoFastjetAll"),
    rho_PFIso = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedElectronsData")
)


process.isoForMu = cms.EDProducer("MuonIsoValueMapProducer",
    EAFile_MiniIso = cms.FileInPath('PhysicsTools/NanoAOD/data/effAreaMuons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
    relative = cms.bool(False),
    rho_MiniIso = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedMuonsData")
)


process.jetsAk4CHS = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsNewDFTraining","probb"), cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsNewDFTraining","probc"), cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsNewDFTraining","probg"), cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsNewDFTraining","problepb"), cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsNewDFTraining","probbb"), 
        cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsNewDFTraining","probuds")
    ),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsTransientCorrectedSlimmedJetsNewDFTraining")),
    jetSource = cms.InputTag("updatedPatJetsSlimmedJetsNewDFTraining"),
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfDeepFlavourTagInfosSlimmedJetsNewDFTraining"), cms.InputTag("pfDeepCSVTagInfosSlimmedJetsNewDFTraining"), cms.InputTag("pfImpactParameterTagInfosSlimmedJetsNewDFTraining"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosSlimmedJetsNewDFTraining")),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.jetsAk4Puppi = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsPuppiNewDFTraining","probb"), cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsPuppiNewDFTraining","probc"), cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsPuppiNewDFTraining","probg"), cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsPuppiNewDFTraining","problepb"), cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsPuppiNewDFTraining","probbb"), 
        cms.InputTag("pfDeepFlavourJetTagsSlimmedJetsPuppiNewDFTraining","probuds")
    ),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsTransientCorrectedSlimmedJetsPuppiNewDFTraining")),
    jetSource = cms.InputTag("updatedPatJetsSlimmedJetsPuppiNewDFTraining"),
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfDeepFlavourTagInfosSlimmedJetsPuppiNewDFTraining"), cms.InputTag("pfDeepCSVTagInfosSlimmedJetsPuppiNewDFTraining"), cms.InputTag("pfImpactParameterTagInfosSlimmedJetsPuppiNewDFTraining"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosSlimmedJetsPuppiNewDFTraining")),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag(
                "patPuppiJetSpecificProducerjetsAk4Puppi:puppiMultiplicity", "patPuppiJetSpecificProducerjetsAk4Puppi:neutralPuppiMultiplicity", "patPuppiJetSpecificProducerjetsAk4Puppi:neutralHadronPuppiMultiplicity", "patPuppiJetSpecificProducerjetsAk4Puppi:photonPuppiMultiplicity", "patPuppiJetSpecificProducerjetsAk4Puppi:HFHadronPuppiMultiplicity", 
                "patPuppiJetSpecificProducerjetsAk4Puppi:HFEMPuppiMultiplicity"
            )
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.jetsAk8CHS = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAK8PFCHS"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAK8PFCHS"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleInclusiveSecondaryVertexHighEffBJetTags"), 
        cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("softPFMuonBJetTags"), cms.InputTag("softPFElectronBJetTags"), cms.InputTag("pfCombinedMVAV2BJetTags"), 
        cms.InputTag("pfCombinedCvsLJetTags"), cms.InputTag("pfCombinedCvsBJetTags"), cms.InputTag("pfDeepCSVJetTags","probb"), cms.InputTag("pfDeepCSVJetTags","probc"), cms.InputTag("pfDeepCSVJetTags","probudsg"), 
        cms.InputTag("pfDeepCSVJetTags","probbb")
    ),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAK8PFCHS"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAK8PFCHS"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK8PFCHS")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8CHSJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.jetsAk8CHSSubstructure = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbqq"), cms.InputTag("pfMassIndependentDeepDoubleCvBJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfDeepDoubleCvBJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), 
        cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbqq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfDeepDoubleBvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbcq"), 
        cms.InputTag("pfDeepFlavourJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","problepb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassIndependentDeepDoubleCvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepDoubleCvBJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), 
        cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbq"), cms.InputTag("pfParticleNetMassRegressionJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","mass"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
        cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
        cms.InputTag("pfDeepFlavourJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probbb"), cms.InputTag("pfDeepFlavourJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probuds"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbqq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probXqq"), 
        cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWqq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassIndependentDeepDoubleBvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWcq"), 
        cms.InputTag("pfDeepFlavourJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepFlavourJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probg"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbcq"), 
        cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbmu"), cms.InputTag("pfDeepDoubleBvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCD"), 
        cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probXbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), 
        cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWqq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZqq"), cms.InputTag("pfDeepFlavourJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probc"), cms.InputTag("pfDeepDoubleCvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCD"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbta"), 
        cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHqqqq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), 
        cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWcq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbq"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), 
        cms.InputTag("pfDeepDoubleCvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), cms.InputTag("pfMassIndependentDeepDoubleCvBJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWcq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHqqqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), 
        cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
        cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbel"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZqq"), cms.InputTag("pfMassIndependentDeepDoubleCvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCD"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probXcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHqqqq"), 
        cms.InputTag("pfMassIndependentDeepDoubleBvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCD"), cms.InputTag("pfMassDecorrelatedParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","XqqvsQCD"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","WvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","ZHccvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","ZvsQCD"), 
        cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","ZbbvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","bbvsLight"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","ccvsLight"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","H4qvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","ZbbvsQCD"), 
        cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","ZHbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","TvsQCD"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","HccvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","HbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","WvsQCD"), 
        cms.InputTag("pfParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","ZbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","HbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","H4qvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","WvsQCD"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","TvsQCD"), 
        cms.InputTag("pfMassDecorrelatedParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","XccvsQCD"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","ZvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","H4qvsQCD"), cms.InputTag("pfMassDecorrelatedParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","XbbvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","TvsQCD"), 
        cms.InputTag("pfParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","HbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","ZvsQCD")
    ),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsTransientCorrectedPackedPatJetsAk8CHSJetsNewDFTraining")),
    jetSource = cms.InputTag("updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining"),
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(
        cms.InputTag("pfParticleNetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"), cms.InputTag("pfDeepDoubleXTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining"), cms.InputTag("pfImpactParameterAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining"), cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining"), 
        cms.InputTag("pfDeepBoostedJetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"), cms.InputTag("pfDeepFlavourTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"), cms.InputTag("pfDeepCSVTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"), cms.InputTag("pfImpactParameterTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosPackedPatJetsAk8CHSJetsNewDFTraining")
    ),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.jetsAk8Puppi = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        cms.InputTag("pfDeepFlavourJetTagsRekeyPatJetsAK8PFPUPPINewDFTraining","probb"), cms.InputTag("pfDeepFlavourJetTagsRekeyPatJetsAK8PFPUPPINewDFTraining","probc"), cms.InputTag("pfDeepFlavourJetTagsRekeyPatJetsAK8PFPUPPINewDFTraining","probg"), cms.InputTag("pfDeepFlavourJetTagsRekeyPatJetsAK8PFPUPPINewDFTraining","problepb"), cms.InputTag("pfDeepFlavourJetTagsRekeyPatJetsAK8PFPUPPINewDFTraining","probbb"), 
        cms.InputTag("pfDeepFlavourJetTagsRekeyPatJetsAK8PFPUPPINewDFTraining","probuds")
    ),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsTransientCorrectedRekeyPatJetsAK8PFPUPPINewDFTraining")),
    jetSource = cms.InputTag("updatedPatJetsRekeyPatJetsAK8PFPUPPINewDFTraining"),
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfDeepFlavourTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining"), cms.InputTag("pfDeepCSVTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining"), cms.InputTag("pfImpactParameterTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining")),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag(
                "patPuppiJetSpecificProducerjetsAk8Puppi:puppiMultiplicity", "patPuppiJetSpecificProducerjetsAk8Puppi:neutralPuppiMultiplicity", "patPuppiJetSpecificProducerjetsAk8Puppi:neutralHadronPuppiMultiplicity", "patPuppiJetSpecificProducerjetsAk8Puppi:photonPuppiMultiplicity", "patPuppiJetSpecificProducerjetsAk8Puppi:HFHadronPuppiMultiplicity", 
                "patPuppiJetSpecificProducerjetsAk8Puppi:HFEMPuppiMultiplicity"
            )
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.jetsAk8PuppiSubstructure = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbqq"), cms.InputTag("pfMassIndependentDeepDoubleCvBJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfDeepDoubleCvBJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), 
        cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbqq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfDeepDoubleBvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbcq"), 
        cms.InputTag("pfDeepFlavourJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","problepb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassIndependentDeepDoubleCvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepDoubleCvBJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), 
        cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbq"), cms.InputTag("pfParticleNetMassRegressionJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","mass"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
        cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
        cms.InputTag("pfDeepFlavourJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probbb"), cms.InputTag("pfDeepFlavourJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probuds"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbqq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probXqq"), 
        cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWqq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassIndependentDeepDoubleBvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWcq"), 
        cms.InputTag("pfDeepFlavourJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepFlavourJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probg"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbcq"), 
        cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbmu"), cms.InputTag("pfDeepDoubleBvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCD"), 
        cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probXbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), 
        cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWqq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZqq"), cms.InputTag("pfDeepFlavourJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probc"), cms.InputTag("pfDeepDoubleCvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCD"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbta"), 
        cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHqqqq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), 
        cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWcq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbq"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), 
        cms.InputTag("pfDeepDoubleCvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), cms.InputTag("pfMassIndependentDeepDoubleCvBJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWcq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHqqqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), 
        cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
        cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbel"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZqq"), cms.InputTag("pfMassIndependentDeepDoubleCvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCD"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probXcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHqqqq"), 
        cms.InputTag("pfMassIndependentDeepDoubleBvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCD"), cms.InputTag("pfMassDecorrelatedParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","XqqvsQCD"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","WvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","ZHccvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","ZvsQCD"), 
        cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","ZbbvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","bbvsLight"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","ccvsLight"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","H4qvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","ZbbvsQCD"), 
        cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","ZHbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","TvsQCD"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","HccvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","HbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","WvsQCD"), 
        cms.InputTag("pfParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","ZbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","HbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","H4qvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","WvsQCD"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","TvsQCD"), 
        cms.InputTag("pfMassDecorrelatedParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","XccvsQCD"), cms.InputTag("pfParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","ZvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","H4qvsQCD"), cms.InputTag("pfMassDecorrelatedParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","XbbvsQCD"), cms.InputTag("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","TvsQCD"), 
        cms.InputTag("pfParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","HbbvsQCD"), cms.InputTag("pfDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","ZvsQCD")
    ),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")),
    jetSource = cms.InputTag("updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(
        cms.InputTag("pfParticleNetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"), cms.InputTag("pfDeepDoubleXTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"), cms.InputTag("pfImpactParameterAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"), cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"), 
        cms.InputTag("pfDeepBoostedJetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"), cms.InputTag("pfDeepFlavourTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"), cms.InputTag("pfDeepCSVTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"), cms.InputTag("pfImpactParameterTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
    ),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag(
                "patPuppiJetSpecificProducerupdatedPatJetsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining:puppiMultiplicity", "patPuppiJetSpecificProducerupdatedPatJetsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining:neutralPuppiMultiplicity", "patPuppiJetSpecificProducerupdatedPatJetsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining:neutralHadronPuppiMultiplicity", "patPuppiJetSpecificProducerupdatedPatJetsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining:photonPuppiMultiplicity", "patPuppiJetSpecificProducerupdatedPatJetsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining:HFHadronPuppiMultiplicity", 
                "patPuppiJetSpecificProducerupdatedPatJetsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining:HFEMPuppiMultiplicity"
            )
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.muPFMiniIsoDepositCHSTAND = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllChargedHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedMuons"),
    trackType = cms.string('candidate')
)


process.muPFMiniIsoDepositNHPFWGT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfWeightedNeutralHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedMuons"),
    trackType = cms.string('candidate')
)


process.muPFMiniIsoDepositNHSTAND = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllNeutralHadrons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedMuons"),
    trackType = cms.string('candidate')
)


process.muPFMiniIsoDepositPUSTAND = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfPileUpAllChargedParticles")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedMuons"),
    trackType = cms.string('candidate')
)


process.muPFMiniIsoDepositPhPFWGT = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfWeightedPhotons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedMuons"),
    trackType = cms.string('candidate')
)


process.muPFMiniIsoDepositPhSTAND = cms.EDProducer("CandIsoDepositProducer",
    ExtractorPSet = cms.PSet(
        ComponentName = cms.string('CandViewExtractor'),
        DR_Max = cms.double(0.4),
        DR_Veto = cms.double(1e-05),
        DepositLabel = cms.untracked.string(''),
        Diff_r = cms.double(99999.99),
        Diff_z = cms.double(99999.99),
        inputCandView = cms.InputTag("pfAllPhotons")
    ),
    MultipleDepositsFlag = cms.bool(False),
    src = cms.InputTag("slimmedMuons"),
    trackType = cms.string('candidate')
)


process.muPFMiniIsoValueCHSTAND = cms.EDProducer("CandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFMiniIsoDepositCHSTAND"),
        vetos = cms.vstring(
            '0.0001', 
            'Threshold(0.0)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMiniIsoValueNHPFWGT = cms.EDProducer("CandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFMiniIsoDepositNHPFWGT"),
        vetos = cms.vstring(
            '0.01', 
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMiniIsoValueNHSTAND = cms.EDProducer("CandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFMiniIsoDepositNHSTAND"),
        vetos = cms.vstring(
            '0.01', 
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMiniIsoValuePUSTAND = cms.EDProducer("CandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFMiniIsoDepositPUSTAND"),
        vetos = cms.vstring(
            '0.01', 
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMiniIsoValuePhPFWGT = cms.EDProducer("CandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFMiniIsoDepositPhPFWGT"),
        vetos = cms.vstring(
            '0.01', 
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muPFMiniIsoValuePhSTAND = cms.EDProducer("CandIsolatorFromDepositsMINIISO",
    deposits = cms.VPSet(cms.PSet(
        dRmax = cms.double(0.2),
        dRmin = cms.double(0.05),
        kTfac = cms.double(10.0),
        mode = cms.string('sum'),
        skipDefaultVeto = cms.bool(True),
        src = cms.InputTag("muPFMiniIsoDepositPhSTAND"),
        vetos = cms.vstring(
            '0.01', 
            'Threshold(0.5)'
        ),
        weight = cms.string('1')
    ))
)


process.muonGenJets = cms.EDProducer("FastjetJetProducer",
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    Ghost_EtaMax = cms.double(5.0),
    Rho_EtaMax = cms.double(4.4),
    doAreaDiskApprox = cms.bool(False),
    doAreaFastjet = cms.bool(True),
    doPUOffsetCorr = cms.bool(False),
    doPVCorrection = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    inputEMin = cms.double(0.0),
    inputEtMin = cms.double(0.0),
    jetAlgorithm = cms.string('AntiKt'),
    jetPtMin = cms.double(10.0),
    jetType = cms.string('GenJet'),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    minSeed = cms.uint32(14327),
    rParam = cms.double(0.1),
    src = cms.InputTag("MuonPhotonGenParticles"),
    srcPVs = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useDeterministicSeed = cms.bool(True),
    voronoiRfact = cms.double(-0.9)
)


process.muonMVATOP = cms.EDProducer("MuonBaseMVAValueMapProducer",
    isClassifier = cms.bool(True),
    name = cms.string('muonMVATOP'),
    src = cms.InputTag("slimmedMuonsWithUserData"),
    variables = cms.PSet(
        bTagDeepJetClosestJet = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?max(userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probbb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:probb\')+userCand(\'jetForLepJetVar\').bDiscriminator(\'pfDeepFlavourJetTags:problepb\'),0.0):0.0"),
        dxylog = cms.string("log(abs(dB(\'PV2D\')))"),
        dzlog = cms.string("log(abs(dB(\'PVDZ\')))"),
        etaAbs = cms.string('abs(eta)'),
        miniIsoCharged = cms.string("userFloat(\'miniIsoChg\')/pt"),
        miniIsoNeutral = cms.string("(userFloat(\'miniIsoAll\')-userFloat(\'miniIsoChg\'))/pt"),
        pTRel = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'ptRel\'):0"),
        pt = cms.string('pt'),
        ptRatio = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?min(userFloat(\'ptRatio\'),1.5):1.0/(1.0+(pfIsolationR04().sumChargedHadronPt + max(pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - pfIsolationR04().sumPUPt/2,0.0))/pt)"),
        relIso = cms.string('(pfIsolationR03().sumChargedHadronPt + max(pfIsolationR03().sumNeutralHadronEt + pfIsolationR03().sumPhotonEt - pfIsolationR03().sumPUPt/2,0.0))/pt'),
        segmentCompatibility = cms.string('segmentCompatibility'),
        sip3d = cms.string("abs(dB(\'PV3D\')/edB(\'PV3D\'))"),
        trackMultClosestJet = cms.string("?userCand(\'jetForLepJetVar\').isNonnull()?userFloat(\'jetNDauChargedMVASel\'):0")
    ),
    variablesOrder = cms.vstring(
        'dxylog', 
        'miniIsoCharged', 
        'miniIsoNeutral', 
        'pTRel', 
        'sip3d', 
        'segmentCompatibility', 
        'ptRatio', 
        'bTagDeepJetClosestJet', 
        'pt', 
        'trackMultClosestJet', 
        'etaAbs', 
        'dzlog', 
        'relIso'
    ),
    weightFile = cms.FileInPath('UHH2/common/data/UL16preVFP/TMVA_BDTG_TOP_muon_2016.weights.xml')
)


process.packedPatJetsAk8CHSJets = cms.EDProducer("JetSubstructurePacker",
    algoLabels = cms.vstring('SoftDropCHS'),
    algoTags = cms.VInputTag(cms.InputTag("patJetsAk8CHSJetsSoftDropPacked")),
    distMax = cms.double(0.8),
    fixDaughters = cms.bool(False),
    jetSrc = cms.InputTag("patJetsAk8CHSJetsFat")
)


process.particleFlowTmpPtrs = cms.EDProducer("PFCandidateFwdPtrProducer",
    src = cms.InputTag("particleFlowTmp")
)


process.patJetCorrFactorsAK8PFCHS = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK8PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8CHSJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAK8PFPUPPI = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK8PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PuppiJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8CHSJetsFat = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK8PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8CHSJetsFat"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8CHSJetsSoftDrop = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK8PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8CHSJetsSoftDrop"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8CHSJetsSoftDropSubjets = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8CHSJetsSoftDrop","SubJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8PuppiJetsFat = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK8PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PuppiJetsFat"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8PuppiJetsSoftDrop = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK8PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PuppiJetsSoftDrop"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("packedPatJetsAk8CHSJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("patJetsAk8CHSJetsSoftDropSubjets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("patJetsAk8PuppiJetsSoftDropSubjets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("rekeyPackedPatJetsAk8PuppiJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsRekeyPatJetsAK8PFPUPPINewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("rekeyPatJetsAK8PFPUPPI"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsSlimmedJetsNewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsSlimmedJetsPuppiNewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJetsPuppi"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsTransientCorrectedPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK8PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsPatJetsAk8CHSJetsSoftDropSubjets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsPatJetsAk8PuppiJetsSoftDropSubjets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK8PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsTransientCorrectedRekeyPatJetsAK8PFPUPPINewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK8PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsRekeyPatJetsAK8PFPUPPINewDFTraining"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsTransientCorrectedSlimmedJetsNewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsSlimmedJetsNewDFTraining"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsTransientCorrectedSlimmedJetsPuppiNewDFTraining = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFPuppi'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsSlimmedJetsPuppiNewDFTraining"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetFlavourAssociationAK8PFCHS = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8CHSJets"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.patJetFlavourAssociationAK8PFPUPPI = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8PuppiJets"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.patJetFlavourAssociationAk8CHSJetsFat = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8CHSJetsFat"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.patJetFlavourAssociationAk8CHSJetsSoftDrop = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8CHSJetsSoftDrop"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.patJetFlavourAssociationAk8CHSJetsSoftDropSubjets = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    groomedJets = cms.InputTag("ak8CHSJetsSoftDrop"),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8CHSJetsFat"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8),
    subjets = cms.InputTag("ak8CHSJetsSoftDrop","SubJets")
)


process.patJetFlavourAssociationAk8PuppiJetsFat = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8PuppiJetsFat"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.patJetFlavourAssociationAk8PuppiJetsSoftDrop = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8)
)


process.patJetFlavourAssociationAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetFlavourClustering",
    bHadrons = cms.InputTag("patJetPartons","bHadrons"),
    cHadrons = cms.InputTag("patJetPartons","cHadrons"),
    ghostRescaling = cms.double(1e-18),
    groomedJets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    hadronFlavourHasPriority = cms.bool(False),
    jetAlgorithm = cms.string('AntiKt'),
    jets = cms.InputTag("ak8PuppiJetsFat"),
    leptons = cms.InputTag("patJetPartons","leptons"),
    partons = cms.InputTag("patJetPartons","physicsPartons"),
    rParam = cms.double(0.8),
    subjets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets")
)


process.patJetFlavourAssociationLegacyAK8PFCHS = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAK8PFCHS")
)


process.patJetFlavourAssociationLegacyAK8PFPUPPI = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAK8PFPUPPI")
)


process.patJetFlavourAssociationLegacyAk8CHSJetsFat = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8CHSJetsFat")
)


process.patJetFlavourAssociationLegacyAk8CHSJetsSoftDrop = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8CHSJetsSoftDrop")
)


process.patJetFlavourAssociationLegacyAk8CHSJetsSoftDropSubjets = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8CHSJetsSoftDropSubjets")
)


process.patJetFlavourAssociationLegacyAk8PuppiJetsFat = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8PuppiJetsFat")
)


process.patJetFlavourAssociationLegacyAk8PuppiJetsSoftDrop = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8PuppiJetsSoftDrop")
)


process.patJetFlavourAssociationLegacyAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetFlavourIdentifier",
    physicsDefinition = cms.bool(False),
    srcByReference = cms.InputTag("patJetPartonAssociationLegacyAk8PuppiJetsSoftDropSubjets")
)


process.patJetGenJetMatchAK8PFCHS = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("slimmedGenJetsAK8"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8CHSJets")
)


process.patJetGenJetMatchAK8PFPUPPI = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("slimmedGenJetsAK8"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJets")
)


process.patJetGenJetMatchAk8CHSJetsFat = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak8GenJetsFat"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8CHSJetsFat")
)


process.patJetGenJetMatchAk8CHSJetsSoftDrop = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("slimmedGenJets"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8CHSJetsSoftDrop")
)


process.patJetGenJetMatchAk8CHSJetsSoftDropSubjets = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak8GenJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8CHSJetsSoftDrop","SubJets")
)


process.patJetGenJetMatchAk8PuppiJetsFat = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak8GenJetsFat"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsFat")
)


process.patJetGenJetMatchAk8PuppiJetsSoftDrop = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("slimmedGenJets"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsSoftDrop")
)


process.patJetGenJetMatchAk8PuppiJetsSoftDropSubjets = cms.EDProducer("GenJetMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("ak8GenJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(0.8),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets")
)


process.patJetPartonAssociationLegacyAK8PFCHS = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8CHSJets"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAK8PFPUPPI = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8PuppiJets"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8CHSJetsFat = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8CHSJetsFat"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8CHSJetsSoftDrop = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8CHSJetsSoftDrop"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8CHSJetsSoftDropSubjets = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8CHSJetsSoftDrop","SubJets"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8PuppiJetsFat = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8PuppiJetsFat"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8PuppiJetsSoftDrop = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonAssociationLegacyAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetPartonMatcher",
    coneSizeToAssociate = cms.double(0.3),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    partons = cms.InputTag("patJetPartonsLegacy")
)


process.patJetPartonMatchAK8PFCHS = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5, 
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8CHSJets")
)


process.patJetPartonMatchAK8PFPUPPI = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5, 
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJets")
)


process.patJetPartonMatchAk8CHSJetsFat = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5, 
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8CHSJetsFat")
)


process.patJetPartonMatchAk8CHSJetsSoftDrop = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5, 
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8CHSJetsSoftDrop")
)


process.patJetPartonMatchAk8CHSJetsSoftDropSubjets = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5, 
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8CHSJetsSoftDrop","SubJets")
)


process.patJetPartonMatchAk8PuppiJetsFat = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5, 
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsFat")
)


process.patJetPartonMatchAk8PuppiJetsSoftDrop = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5, 
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsSoftDrop")
)


process.patJetPartonMatchAk8PuppiJetsSoftDropSubjets = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("prunedGenParticles"),
    maxDPtRel = cms.double(3.0),
    maxDeltaR = cms.double(0.4),
    mcPdgId = cms.vint32(
        1, 2, 3, 4, 5, 
        21
    ),
    mcStatus = cms.vint32(3, 23),
    resolveAmbiguities = cms.bool(True),
    resolveByMatchQuality = cms.bool(False),
    src = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets")
)


process.patJetPartons = cms.EDProducer("HadronAndPartonSelector",
    fullChainPhysPartons = cms.bool(True),
    particles = cms.InputTag("prunedGenParticles"),
    partonMode = cms.string('Auto'),
    src = cms.InputTag("generator")
)


process.patJetPartonsLegacy = cms.EDProducer("PartonSelector",
    src = cms.InputTag("prunedGenParticles"),
    withLeptons = cms.bool(False)
)


process.patJetsAK8PFPUPPI = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAK8PFPUPPI"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAK8PFPUPPI"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(False),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        cms.InputTag("pfJetBProbabilityBJetTags"), cms.InputTag("pfJetProbabilityBJetTags"), cms.InputTag("pfTrackCountingHighEffBJetTags"), cms.InputTag("pfSimpleSecondaryVertexHighEffBJetTags"), cms.InputTag("pfSimpleInclusiveSecondaryVertexHighEffBJetTags"), 
        cms.InputTag("pfCombinedSecondaryVertexV2BJetTags"), cms.InputTag("pfCombinedInclusiveSecondaryVertexV2BJetTags"), cms.InputTag("softPFMuonBJetTags"), cms.InputTag("softPFElectronBJetTags"), cms.InputTag("pfCombinedMVAV2BJetTags"), 
        cms.InputTag("pfCombinedCvsLJetTags"), cms.InputTag("pfCombinedCvsBJetTags"), cms.InputTag("pfDeepCSVJetTags","probb"), cms.InputTag("pfDeepCSVJetTags","probc"), cms.InputTag("pfDeepCSVJetTags","probudsg"), 
        cms.InputTag("pfDeepCSVJetTags","probbb")
    ),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAK8PFPUPPI"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAK8PFPUPPI"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAK8PFPUPPI")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PuppiJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8CHSJetsFat = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8CHSJetsFat"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8CHSJetsFat"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8CHSJetsFat"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8CHSJetsFat"), cms.InputTag("pfDeepCSVJetTagsAk8CHSJetsFat","probbb"), cms.InputTag("pfDeepCSVJetTagsAk8CHSJetsFat","probb")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8CHSJetsFat"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8CHSJetsFat"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8CHSJetsFat")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8CHSJetsFat"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(
        cms.InputTag("pfImpactParameterTagInfosAk8CHSJetsFat"), cms.InputTag("pfSecondaryVertexTagInfosAk8CHSJetsFat"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsFat"), cms.InputTag("softPFMuonsTagInfosAk8CHSJetsFat"), cms.InputTag("softPFElectronsTagInfosAk8CHSJetsFat"), 
        cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8CHSJetsFat"), cms.InputTag("pfImpactParameterCA15TagInfosAk8CHSJetsFat"), cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsFat"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8CHSJetsFat"), cms.InputTag("pfImpactParameterAK8TagInfosAk8CHSJetsFat"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsFat"), cms.InputTag("pfDeepCSVTagInfosAk8CHSJetsFat")
    ),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8CHSJetsSoftDrop = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8CHSJetsSoftDrop"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8CHSJetsSoftDrop"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8CHSJetsSoftDrop"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8CHSJetsSoftDrop"), cms.InputTag("pfDeepCSVJetTagsAk8CHSJetsSoftDrop","probbb"), cms.InputTag("pfDeepCSVJetTagsAk8CHSJetsSoftDrop","probb")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8CHSJetsSoftDrop"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8CHSJetsSoftDrop"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8CHSJetsSoftDrop")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8CHSJetsSoftDrop"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(
        cms.InputTag("pfImpactParameterTagInfosAk8CHSJetsSoftDrop"), cms.InputTag("pfSecondaryVertexTagInfosAk8CHSJetsSoftDrop"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsSoftDrop"), cms.InputTag("softPFMuonsTagInfosAk8CHSJetsSoftDrop"), cms.InputTag("softPFElectronsTagInfosAk8CHSJetsSoftDrop"), 
        cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8CHSJetsSoftDrop"), cms.InputTag("pfImpactParameterCA15TagInfosAk8CHSJetsSoftDrop"), cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsSoftDrop"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8CHSJetsSoftDrop"), cms.InputTag("pfImpactParameterAK8TagInfosAk8CHSJetsSoftDrop"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsSoftDrop"), cms.InputTag("pfDeepCSVTagInfosAk8CHSJetsSoftDrop")
    ),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8CHSJetsSoftDropPacked = cms.EDProducer("BoostedJetMerger",
    jetSrc = cms.InputTag("patJetsAk8CHSJetsSoftDrop"),
    subjetSrc = cms.InputTag("rekeyUpdatedPatJetsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets")
)


process.patJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8CHSJetsSoftDropSubjets","SubJets"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8CHSJetsSoftDropSubjets"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfDeepCSVJetTagsAk8CHSJetsSoftDropSubjets","probbb"), cms.InputTag("pfDeepCSVJetTagsAk8CHSJetsSoftDropSubjets","probb")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8CHSJetsSoftDropSubjets"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8CHSJetsSoftDropSubjets"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8CHSJetsSoftDropSubjets")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8CHSJetsSoftDrop","SubJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(
        cms.InputTag("pfImpactParameterTagInfosAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfSecondaryVertexTagInfosAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsSoftDropSubjets"), cms.InputTag("softPFMuonsTagInfosAk8CHSJetsSoftDropSubjets"), cms.InputTag("softPFElectronsTagInfosAk8CHSJetsSoftDropSubjets"), 
        cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfImpactParameterCA15TagInfosAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfImpactParameterAK8TagInfosAk8CHSJetsSoftDropSubjets"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfDeepCSVTagInfosAk8CHSJetsSoftDropSubjets")
    ),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8PuppiJetsFat = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8PuppiJetsFat"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8PuppiJetsFat"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8PuppiJetsFat"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsFat"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsFat","probbb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsFat","probb")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8PuppiJetsFat"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8PuppiJetsFat"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8PuppiJetsFat")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PuppiJetsFat"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(
        cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsFat"), cms.InputTag("pfSecondaryVertexTagInfosAk8PuppiJetsFat"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsFat"), cms.InputTag("softPFMuonsTagInfosAk8PuppiJetsFat"), cms.InputTag("softPFElectronsTagInfosAk8PuppiJetsFat"), 
        cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsFat"), cms.InputTag("pfImpactParameterCA15TagInfosAk8PuppiJetsFat"), cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsFat"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsFat"), cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsFat"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsFat"), cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsFat")
    ),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8PuppiJetsSoftDrop = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8PuppiJetsSoftDrop"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8PuppiJetsSoftDrop"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(False),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8PuppiJetsSoftDrop"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDrop"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probbb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDrop","probb")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8PuppiJetsSoftDrop"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8PuppiJetsSoftDrop"),
    getJetMCFlavour = cms.bool(False),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8PuppiJetsSoftDrop")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PuppiJetsSoftDrop"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(
        cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfSecondaryVertexTagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("softPFMuonsTagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("softPFElectronsTagInfosAk8PuppiJetsSoftDrop"), 
        cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfImpactParameterCA15TagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDrop"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDrop"), cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsSoftDrop")
    ),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patJetsAk8PuppiJetsSoftDropPacked = cms.EDProducer("BoostedJetMerger",
    jetSrc = cms.InputTag("patJetsAk8PuppiJetsSoftDrop"),
    subjetSrc = cms.InputTag("rekeyUpdatedPatJetsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets")
)


process.patJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("PATJetProducer",
    JetFlavourInfoSource = cms.InputTag("patJetFlavourAssociationAk8PuppiJetsSoftDropSubjets","SubJets"),
    JetPartonMapSource = cms.InputTag("patJetFlavourAssociationLegacyAk8PuppiJetsSoftDropSubjets"),
    addAssociatedTracks = cms.bool(False),
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addEfficiencies = cms.bool(False),
    addGenJetMatch = cms.bool(True),
    addGenPartonMatch = cms.bool(True),
    addJetCharge = cms.bool(False),
    addJetCorrFactors = cms.bool(True),
    addJetFlavourInfo = cms.bool(True),
    addJetID = cms.bool(False),
    addPartonJetMatch = cms.bool(False),
    addResolutions = cms.bool(False),
    addTagInfos = cms.bool(True),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probbb"), cms.InputTag("pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets","probb")),
    efficiencies = cms.PSet(

    ),
    embedGenJetMatch = cms.bool(True),
    embedGenPartonMatch = cms.bool(True),
    embedPFCandidates = cms.bool(False),
    genJetMatch = cms.InputTag("patJetGenJetMatchAk8PuppiJetsSoftDropSubjets"),
    genPartonMatch = cms.InputTag("patJetPartonMatchAk8PuppiJetsSoftDropSubjets"),
    getJetMCFlavour = cms.bool(True),
    jetChargeSource = cms.InputTag(""),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsAk8PuppiJetsSoftDropSubjets")),
    jetIDMap = cms.InputTag("ak4JetID"),
    jetSource = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    partonJetSource = cms.InputTag("NOT_IMPLEMENTED"),
    resolutions = cms.PSet(

    ),
    tagInfoSources = cms.VInputTag(
        cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfSecondaryVertexTagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("softPFMuonsTagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("softPFElectronsTagInfosAk8PuppiJetsSoftDropSubjets"), 
        cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfImpactParameterCA15TagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDropSubjets"), 
        cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsSoftDropSubjets")
    ),
    trackAssociationSource = cms.InputTag(""),
    useLegacyJetMCFlavour = cms.bool(False),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.patPuppiJetSpecificProducerjetsAk4Puppi = cms.EDProducer("PATPuppiJetSpecificProducer",
    src = cms.InputTag("updatedPatJetsSlimmedJetsPuppiNewDFTraining")
)


process.patPuppiJetSpecificProducerjetsAk8Puppi = cms.EDProducer("PATPuppiJetSpecificProducer",
    src = cms.InputTag("updatedPatJetsRekeyPatJetsAK8PFPUPPINewDFTraining")
)


process.patPuppiJetSpecificProducerupdatedPatJetsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("PATPuppiJetSpecificProducer",
    src = cms.InputTag("updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
)


process.pfBoostedDoubleSVAK8TagInfosAk8CHSJetsFat = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsFat"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8CHSJetsSoftDrop = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsSoftDrop"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsSoftDropSubjets"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsFat = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsFat"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDrop"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDropSubjets"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVCA15TagInfosAk8CHSJetsFat = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(1.5),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(1.0),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsFat"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVCA15TagInfosAk8CHSJetsSoftDrop = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(1.5),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(1.0),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsSoftDrop"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVCA15TagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(1.5),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(1.0),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsSoftDropSubjets"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsFat = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(1.5),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(1.0),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsFat"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(1.5),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(1.0),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsSoftDrop"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(1.5),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(1.0),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsSoftDropSubjets"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVTagInfosCHS = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsFat"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSVTagInfosPuppi = cms.EDProducer("BoostedDoubleSVProducer",
    R0 = cms.double(0.8),
    beta = cms.double(1.0),
    maxSVDeltaRToJet = cms.double(0.7),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsFat"),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8CHSJetsFat = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8CHSJetsFat"))
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8CHSJetsSoftDrop = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8CHSJetsSoftDrop"))
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8CHSJetsSoftDropSubjets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8CHSJetsSoftDropSubjets"))
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsFat = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsFat"))
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDrop = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDrop"))
)


process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexAK8Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDropSubjets"))
)


process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8CHSJetsFat = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexCA15Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8CHSJetsFat"))
)


process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8CHSJetsSoftDrop = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexCA15Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8CHSJetsSoftDrop"))
)


process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8CHSJetsSoftDropSubjets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexCA15Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8CHSJetsSoftDropSubjets"))
)


process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8PuppiJetsFat = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexCA15Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsFat"))
)


process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8PuppiJetsSoftDrop = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexCA15Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsSoftDrop"))
)


process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('candidateBoostedDoubleSecondaryVertexCA15Computer'),
    tagInfos = cms.VInputTag(cms.InputTag("pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsSoftDropSubjets"))
)


process.pfDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbcq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbqq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('TvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbcq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWcq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWqq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('WvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWcq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZqq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), 
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('HbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHqqqq"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('H4qvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHqqqq"))
        )
    )
)


process.pfDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbcq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbqq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('TvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbcq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWcq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWqq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('WvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWcq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZqq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), 
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('HbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHqqqq"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('H4qvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHqqqq"))
        )
    )
)


process.pfDeepBoostedJetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepBoostedJetTagInfoProducer",
    flip_ip_sign = cms.bool(False),
    include_neutrals = cms.bool(True),
    jet_radius = cms.double(0.8),
    jets = cms.InputTag("updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining"),
    max_jet_eta = cms.double(99),
    min_jet_pt = cms.double(150),
    min_pt_for_track_properties = cms.double(-1),
    min_puppi_wgt = cms.double(0.01),
    pf_candidates = cms.InputTag("packedPFCandidates"),
    puppi_value_map = cms.InputTag(""),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    sip3dSigMax = cms.double(-1),
    sort_by_sip2dsig = cms.bool(False),
    use_puppiP4 = cms.bool(True),
    vertex_associator = cms.InputTag(""),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepBoostedJetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepBoostedJetTagInfoProducer",
    flip_ip_sign = cms.bool(False),
    include_neutrals = cms.bool(True),
    jet_radius = cms.double(0.8),
    jets = cms.InputTag("updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    max_jet_eta = cms.double(99),
    min_jet_pt = cms.double(150),
    min_pt_for_track_properties = cms.double(-1),
    min_puppi_wgt = cms.double(0.01),
    pf_candidates = cms.InputTag("packedPFCandidates"),
    puppi_value_map = cms.InputTag(""),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    sip3dSigMax = cms.double(-1),
    sort_by_sip2dsig = cms.bool(False),
    use_puppiP4 = cms.bool(True),
    vertex_associator = cms.InputTag(""),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring(
        'probTbcq', 
        'probTbqq', 
        'probTbc', 
        'probTbq', 
        'probWcq', 
        'probWqq', 
        'probZbb', 
        'probZcc', 
        'probZqq', 
        'probHbb', 
        'probHcc', 
        'probHqqqq', 
        'probQCDbb', 
        'probQCDcc', 
        'probQCDb', 
        'probQCDc', 
        'probQCDothers'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet.onnx'),
    preprocessParams = cms.PSet(
        input_names = cms.vstring(
            'pfcand', 
            'sv'
        ),
        pfcand = cms.PSet(
            input_shape = cms.vuint32(1, 42, 100, 1),
            var_infos = cms.PSet(
                pfcand_VTX_ass = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(7.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_abseta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.632648706436),
                    norm_factor = cms.double(1.59032225958),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagEtaRel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.19703966379),
                    norm_factor = cms.double(0.521026991705),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagJetDistVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.000215483247302),
                    norm_factor = cms.double(161.385119349),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagPParRatio = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.839023888111),
                    norm_factor = cms.double(1.19186117841),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagPtRatio = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0173742230982),
                    norm_factor = cms.double(4.25351138308),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip2dSig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.41174531059),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip2dVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(495.583709284),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip3dSig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(0.831133090749),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip3dVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(233.664322627),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_charge = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_deltaR = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.252654820681),
                    norm_factor = cms.double(3.50836328292),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_detadeta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.15567200254e-08),
                    norm_factor = cms.double(1644010.14927),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dlambdadz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.2810873784e-07),
                    norm_factor = cms.double(268715.13012),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dphidphi = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.130510352e-08),
                    norm_factor = cms.double(796482.476472),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dphidxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-9.61654578191e-08),
                    norm_factor = cms.double(204149.346943),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dptdpt = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(4.11880840545e-08),
                    norm_factor = cms.double(66429.1000843),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_drminsv = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.192182734609),
                    norm_factor = cms.double(2.38205282141),
                    replace_inf_value = cms.double(-1),
                    upper_bound = cms.double(5)
                ),
                pfcand_drsubjet1 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.258241385221),
                    norm_factor = cms.double(2.92607580997),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_drsubjet2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.305164307356),
                    norm_factor = cms.double(2.88195895791),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(415.415835966),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxydxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.32332170578e-07),
                    norm_factor = cms.double(45949.2394216),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxydz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(10598589.4298),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxysig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.54565964258),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(264.770519024),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dzdz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.58729170607e-06),
                    norm_factor = cms.double(36545.958354),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dzsig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.23840120847),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_erel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-5.38221979141),
                    norm_factor = cms.double(0.556499386531),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_etarel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.00711047858931),
                    norm_factor = cms.double(4.2642743837),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_hcalFrac = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isChargedHad = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isEl = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isGamma = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isMu = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isNeutralHad = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_lostInnerHits = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_normchi2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(2.0),
                    norm_factor = cms.double(0.00100300902708),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_phirel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.71389010575e-05),
                    norm_factor = cms.double(4.22784626632),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_pt_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.03476798534),
                    norm_factor = cms.double(0.542224410728),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_ptrel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-5.37407469749),
                    norm_factor = cms.double(0.554677114485),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_puppiw = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.0),
                    norm_factor = cms.double(255.000015199),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_quality = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(5.0),
                    norm_factor = cms.double(0.2),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                )
            ),
            var_length = cms.uint32(100),
            var_names = cms.vstring(
                'pfcand_pt_log', 
                'pfcand_ptrel_log', 
                'pfcand_erel_log', 
                'pfcand_phirel', 
                'pfcand_etarel', 
                'pfcand_deltaR', 
                'pfcand_abseta', 
                'pfcand_puppiw', 
                'pfcand_drminsv', 
                'pfcand_drsubjet1', 
                'pfcand_drsubjet2', 
                'pfcand_charge', 
                'pfcand_isMu', 
                'pfcand_isEl', 
                'pfcand_isChargedHad', 
                'pfcand_isGamma', 
                'pfcand_isNeutralHad', 
                'pfcand_hcalFrac', 
                'pfcand_VTX_ass', 
                'pfcand_lostInnerHits', 
                'pfcand_normchi2', 
                'pfcand_quality', 
                'pfcand_dz', 
                'pfcand_dzsig', 
                'pfcand_dxy', 
                'pfcand_dxysig', 
                'pfcand_dptdpt', 
                'pfcand_detadeta', 
                'pfcand_dphidphi', 
                'pfcand_dxydxy', 
                'pfcand_dzdz', 
                'pfcand_dxydz', 
                'pfcand_dphidxy', 
                'pfcand_dlambdadz', 
                'pfcand_btagEtaRel', 
                'pfcand_btagPtRatio', 
                'pfcand_btagPParRatio', 
                'pfcand_btagSip2dVal', 
                'pfcand_btagSip2dSig', 
                'pfcand_btagSip3dVal', 
                'pfcand_btagSip3dSig', 
                'pfcand_btagJetDistVal'
            )
        ),
        sv = cms.PSet(
            input_shape = cms.vuint32(1, 15, 7, 1),
            var_infos = cms.PSet(
                sv_abseta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.616221785545),
                    norm_factor = cms.double(1.49676942133),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_costhetasvpv = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.999747157097),
                    norm_factor = cms.double(174.907183727),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_d3d = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.5242870152),
                    norm_factor = cms.double(0.255813267634),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_d3dsig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.12465429306),
                    norm_factor = cms.double(0.0238374692882),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_deltaR = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.140969499946),
                    norm_factor = cms.double(4.30546783192),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_dxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.387232214212),
                    norm_factor = cms.double(0.360931771841),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_dxysig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.11130714417),
                    norm_factor = cms.double(0.0238327380073),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_erel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-2.82667005062),
                    norm_factor = cms.double(0.704463981589),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                sv_etarel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.0037129354896),
                    norm_factor = cms.double(6.99426943996),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_mass = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.34319722652),
                    norm_factor = cms.double(0.368495534421),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_normchi2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.819934427738),
                    norm_factor = cms.double(0.725797320076),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_ntracks = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(3.0),
                    norm_factor = cms.double(0.5),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_phirel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.000521215377375),
                    norm_factor = cms.double(7.16761972364),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_pt_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(3.64881515503),
                    norm_factor = cms.double(0.725050067872),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                sv_ptrel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-2.81496477127),
                    norm_factor = cms.double(0.701236308041),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                )
            ),
            var_length = cms.uint32(7),
            var_names = cms.vstring(
                'sv_pt_log', 
                'sv_ptrel_log', 
                'sv_erel_log', 
                'sv_phirel', 
                'sv_etarel', 
                'sv_deltaR', 
                'sv_abseta', 
                'sv_mass', 
                'sv_ntracks', 
                'sv_normchi2', 
                'sv_dxy', 
                'sv_dxysig', 
                'sv_d3d', 
                'sv_d3dsig', 
                'sv_costhetasvpv'
            )
        )
    ),
    preprocess_json = cms.string(''),
    src = cms.InputTag("pfDeepBoostedJetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining")
)


process.pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring(
        'probTbcq', 
        'probTbqq', 
        'probTbc', 
        'probTbq', 
        'probWcq', 
        'probWqq', 
        'probZbb', 
        'probZcc', 
        'probZqq', 
        'probHbb', 
        'probHcc', 
        'probHqqqq', 
        'probQCDbb', 
        'probQCDcc', 
        'probQCDb', 
        'probQCDc', 
        'probQCDothers'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet.onnx'),
    preprocessParams = cms.PSet(
        input_names = cms.vstring(
            'pfcand', 
            'sv'
        ),
        pfcand = cms.PSet(
            input_shape = cms.vuint32(1, 42, 100, 1),
            var_infos = cms.PSet(
                pfcand_VTX_ass = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(7.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_abseta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.632648706436),
                    norm_factor = cms.double(1.59032225958),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagEtaRel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.19703966379),
                    norm_factor = cms.double(0.521026991705),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagJetDistVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.000215483247302),
                    norm_factor = cms.double(161.385119349),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagPParRatio = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.839023888111),
                    norm_factor = cms.double(1.19186117841),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagPtRatio = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0173742230982),
                    norm_factor = cms.double(4.25351138308),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip2dSig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.41174531059),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip2dVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(495.583709284),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip3dSig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(0.831133090749),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip3dVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(233.664322627),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_charge = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_deltaR = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.252654820681),
                    norm_factor = cms.double(3.50836328292),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_detadeta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.15567200254e-08),
                    norm_factor = cms.double(1644010.14927),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dlambdadz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.2810873784e-07),
                    norm_factor = cms.double(268715.13012),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dphidphi = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.130510352e-08),
                    norm_factor = cms.double(796482.476472),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dphidxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-9.61654578191e-08),
                    norm_factor = cms.double(204149.346943),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dptdpt = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(4.11880840545e-08),
                    norm_factor = cms.double(66429.1000843),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_drminsv = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.192182734609),
                    norm_factor = cms.double(2.38205282141),
                    replace_inf_value = cms.double(-1),
                    upper_bound = cms.double(5)
                ),
                pfcand_drsubjet1 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.258241385221),
                    norm_factor = cms.double(2.92607580997),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_drsubjet2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.305164307356),
                    norm_factor = cms.double(2.88195895791),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(415.415835966),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxydxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.32332170578e-07),
                    norm_factor = cms.double(45949.2394216),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxydz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(10598589.4298),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxysig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.54565964258),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(264.770519024),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dzdz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.58729170607e-06),
                    norm_factor = cms.double(36545.958354),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dzsig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.23840120847),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_erel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-5.38221979141),
                    norm_factor = cms.double(0.556499386531),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_etarel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.00711047858931),
                    norm_factor = cms.double(4.2642743837),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_hcalFrac = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isChargedHad = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isEl = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isGamma = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isMu = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_isNeutralHad = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_lostInnerHits = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_normchi2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(2.0),
                    norm_factor = cms.double(0.00100300902708),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_phirel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.71389010575e-05),
                    norm_factor = cms.double(4.22784626632),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_pt_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.03476798534),
                    norm_factor = cms.double(0.542224410728),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_ptrel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-5.37407469749),
                    norm_factor = cms.double(0.554677114485),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_puppiw = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.0),
                    norm_factor = cms.double(255.000015199),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_quality = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(5.0),
                    norm_factor = cms.double(0.2),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                )
            ),
            var_length = cms.uint32(100),
            var_names = cms.vstring(
                'pfcand_pt_log', 
                'pfcand_ptrel_log', 
                'pfcand_erel_log', 
                'pfcand_phirel', 
                'pfcand_etarel', 
                'pfcand_deltaR', 
                'pfcand_abseta', 
                'pfcand_puppiw', 
                'pfcand_drminsv', 
                'pfcand_drsubjet1', 
                'pfcand_drsubjet2', 
                'pfcand_charge', 
                'pfcand_isMu', 
                'pfcand_isEl', 
                'pfcand_isChargedHad', 
                'pfcand_isGamma', 
                'pfcand_isNeutralHad', 
                'pfcand_hcalFrac', 
                'pfcand_VTX_ass', 
                'pfcand_lostInnerHits', 
                'pfcand_normchi2', 
                'pfcand_quality', 
                'pfcand_dz', 
                'pfcand_dzsig', 
                'pfcand_dxy', 
                'pfcand_dxysig', 
                'pfcand_dptdpt', 
                'pfcand_detadeta', 
                'pfcand_dphidphi', 
                'pfcand_dxydxy', 
                'pfcand_dzdz', 
                'pfcand_dxydz', 
                'pfcand_dphidxy', 
                'pfcand_dlambdadz', 
                'pfcand_btagEtaRel', 
                'pfcand_btagPtRatio', 
                'pfcand_btagPParRatio', 
                'pfcand_btagSip2dVal', 
                'pfcand_btagSip2dSig', 
                'pfcand_btagSip3dVal', 
                'pfcand_btagSip3dSig', 
                'pfcand_btagJetDistVal'
            )
        ),
        sv = cms.PSet(
            input_shape = cms.vuint32(1, 15, 7, 1),
            var_infos = cms.PSet(
                sv_abseta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.616221785545),
                    norm_factor = cms.double(1.49676942133),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_costhetasvpv = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.999747157097),
                    norm_factor = cms.double(174.907183727),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_d3d = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.5242870152),
                    norm_factor = cms.double(0.255813267634),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_d3dsig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.12465429306),
                    norm_factor = cms.double(0.0238374692882),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_deltaR = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.140969499946),
                    norm_factor = cms.double(4.30546783192),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_dxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.387232214212),
                    norm_factor = cms.double(0.360931771841),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_dxysig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.11130714417),
                    norm_factor = cms.double(0.0238327380073),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_erel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-2.82667005062),
                    norm_factor = cms.double(0.704463981589),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                sv_etarel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.0037129354896),
                    norm_factor = cms.double(6.99426943996),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_mass = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.34319722652),
                    norm_factor = cms.double(0.368495534421),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_normchi2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.819934427738),
                    norm_factor = cms.double(0.725797320076),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_ntracks = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(3.0),
                    norm_factor = cms.double(0.5),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_phirel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.000521215377375),
                    norm_factor = cms.double(7.16761972364),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_pt_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(3.64881515503),
                    norm_factor = cms.double(0.725050067872),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                sv_ptrel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-2.81496477127),
                    norm_factor = cms.double(0.701236308041),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                )
            ),
            var_length = cms.uint32(7),
            var_names = cms.vstring(
                'sv_pt_log', 
                'sv_ptrel_log', 
                'sv_erel_log', 
                'sv_phirel', 
                'sv_etarel', 
                'sv_deltaR', 
                'sv_abseta', 
                'sv_mass', 
                'sv_ntracks', 
                'sv_normchi2', 
                'sv_dxy', 
                'sv_dxysig', 
                'sv_d3d', 
                'sv_d3dsig', 
                'sv_costhetasvpv'
            )
        )
    ),
    preprocess_json = cms.string(''),
    src = cms.InputTag("pfDeepBoostedJetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
)


process.pfDeepCSVJetTagsAk8CHSJetsFat = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("pfDeepCSVTagInfosAk8CHSJetsFat"),
    toAdd = cms.PSet(

    )
)


process.pfDeepCSVJetTagsAk8CHSJetsSoftDrop = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("pfDeepCSVTagInfosAk8CHSJetsSoftDrop"),
    toAdd = cms.PSet(

    )
)


process.pfDeepCSVJetTagsAk8CHSJetsSoftDropSubjets = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("pfDeepCSVTagInfosAk8CHSJetsSoftDropSubjets"),
    toAdd = cms.PSet(

    )
)


process.pfDeepCSVJetTagsAk8PuppiJetsFat = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsFat"),
    toAdd = cms.PSet(

    )
)


process.pfDeepCSVJetTagsAk8PuppiJetsSoftDrop = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsSoftDrop"),
    toAdd = cms.PSet(

    )
)


process.pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("DeepFlavourJetTagsProducer",
    NNConfig = cms.FileInPath('RecoBTag/Combined/data/DeepCSV_PhaseI.json'),
    checkSVForDefaults = cms.bool(True),
    meanPadding = cms.bool(True),
    src = cms.InputTag("pfDeepCSVTagInfosAk8PuppiJetsSoftDropSubjets"),
    toAdd = cms.PSet(

    )
)


process.pfDeepCSVTagInfosAk8CHSJetsFat = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsFat")
)


process.pfDeepCSVTagInfosAk8CHSJetsSoftDrop = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsSoftDrop")
)


process.pfDeepCSVTagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    fatJets = cms.InputTag("ak8CHSJetsFat"),
    groomedFatJets = cms.InputTag("ak8CHSJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.8),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsSoftDropSubjets"),
    useSVClustering = cms.bool(True)
)


process.pfDeepCSVTagInfosAk8PuppiJetsFat = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsFat")
)


process.pfDeepCSVTagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDrop")
)


process.pfDeepCSVTagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    fatJets = cms.InputTag("ak8PuppiJetsFat"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.8),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDropSubjets"),
    useSVClustering = cms.bool(True)
)


process.pfDeepCSVTagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosPackedPatJetsAk8CHSJetsNewDFTraining")
)


process.pfDeepCSVTagInfosPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosPatJetsAk8CHSJetsSoftDropSubjets")
)


process.pfDeepCSVTagInfosPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosPatJetsAk8PuppiJetsSoftDropSubjets")
)


process.pfDeepCSVTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
)


process.pfDeepCSVTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining")
)


process.pfDeepCSVTagInfosSlimmedJetsNewDFTraining = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosSlimmedJetsNewDFTraining")
)


process.pfDeepCSVTagInfosSlimmedJetsPuppiNewDFTraining = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosSlimmedJetsPuppiNewDFTraining")
)


process.pfDeepDoubleBvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probQCD', 
        'probHbb'
    ),
    flavor = cms.string('BvL'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDB.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfDeepDoubleBvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probQCD', 
        'probHbb'
    ),
    flavor = cms.string('BvL'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDB.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfDeepDoubleCvBJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probHbb', 
        'probHcc'
    ),
    flavor = cms.string('CvB'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDCvB.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfDeepDoubleCvBJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probHbb', 
        'probHcc'
    ),
    flavor = cms.string('CvB'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDCvB.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfDeepDoubleCvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probQCD', 
        'probHcc'
    ),
    flavor = cms.string('CvL'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDC.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfDeepDoubleCvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probQCD', 
        'probHcc'
    ),
    flavor = cms.string('CvL'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDC.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfDeepDoubleXTagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepDoubleXTagInfoProducer",
    jet_radius = cms.double(0.8),
    jets = cms.InputTag("updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining"),
    min_candidate_pt = cms.double(0.95),
    min_jet_pt = cms.double(150),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfBoostedDoubleSVAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepDoubleXTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepDoubleXTagInfoProducer",
    jet_radius = cms.double(0.8),
    jets = cms.InputTag("updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    min_candidate_pt = cms.double(0.95),
    min_jet_pt = cms.double(150),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfBoostedDoubleSVAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepFlavourJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepFlavourONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probb', 
        'probbb', 
        'problepb', 
        'probc', 
        'probuds', 
        'probg'
    ),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3', 
        'input_4', 
        'input_5'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV03_10X_training/model.onnx'),
    output_names = cms.vstring('ID_pred/Softmax:0'),
    src = cms.InputTag("pfDeepFlavourTagInfosPackedPatJetsAk8CHSJetsNewDFTraining")
)


process.pfDeepFlavourJetTagsPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("DeepFlavourONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probb', 
        'probbb', 
        'problepb', 
        'probc', 
        'probuds', 
        'probg'
    ),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3', 
        'input_4', 
        'input_5'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV03_10X_training/model.onnx'),
    output_names = cms.vstring('ID_pred/Softmax:0'),
    src = cms.InputTag("pfDeepFlavourTagInfosPatJetsAk8CHSJetsSoftDropSubjets")
)


process.pfDeepFlavourJetTagsPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("DeepFlavourONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probb', 
        'probbb', 
        'problepb', 
        'probc', 
        'probuds', 
        'probg'
    ),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3', 
        'input_4', 
        'input_5'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV03_10X_training/model.onnx'),
    output_names = cms.vstring('ID_pred/Softmax:0'),
    src = cms.InputTag("pfDeepFlavourTagInfosPatJetsAk8PuppiJetsSoftDropSubjets")
)


process.pfDeepFlavourJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepFlavourONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probb', 
        'probbb', 
        'problepb', 
        'probc', 
        'probuds', 
        'probg'
    ),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3', 
        'input_4', 
        'input_5'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV03_10X_training/model.onnx'),
    output_names = cms.vstring('ID_pred/Softmax:0'),
    src = cms.InputTag("pfDeepFlavourTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
)


process.pfDeepFlavourJetTagsRekeyPatJetsAK8PFPUPPINewDFTraining = cms.EDProducer("DeepFlavourONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probb', 
        'probbb', 
        'problepb', 
        'probc', 
        'probuds', 
        'probg'
    ),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3', 
        'input_4', 
        'input_5'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV03_10X_training/model.onnx'),
    output_names = cms.vstring('ID_pred/Softmax:0'),
    src = cms.InputTag("pfDeepFlavourTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining")
)


process.pfDeepFlavourJetTagsSlimmedJetsNewDFTraining = cms.EDProducer("DeepFlavourONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probb', 
        'probbb', 
        'problepb', 
        'probc', 
        'probuds', 
        'probg'
    ),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3', 
        'input_4', 
        'input_5'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV03_10X_training/model.onnx'),
    output_names = cms.vstring('ID_pred/Softmax:0'),
    src = cms.InputTag("pfDeepFlavourTagInfosSlimmedJetsNewDFTraining")
)


process.pfDeepFlavourJetTagsSlimmedJetsPuppiNewDFTraining = cms.EDProducer("DeepFlavourONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probb', 
        'probbb', 
        'problepb', 
        'probc', 
        'probuds', 
        'probg'
    ),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3', 
        'input_4', 
        'input_5'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV03_10X_training/model.onnx'),
    output_names = cms.vstring('ID_pred/Softmax:0'),
    src = cms.InputTag("pfDeepFlavourTagInfosSlimmedJetsPuppiNewDFTraining")
)


process.pfDeepFlavourTagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepFlavourTagInfoProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    compute_probabilities = cms.bool(False),
    fallback_puppi_weight = cms.bool(False),
    fallback_vertex_association = cms.bool(False),
    flip = cms.bool(False),
    jet_radius = cms.double(0.4),
    jets = cms.InputTag("updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining"),
    max_jet_eta = cms.double(2.5),
    min_candidate_pt = cms.double(0.95),
    min_jet_pt = cms.double(15),
    puppi_value_map = cms.InputTag("puppi"),
    run_deepVertex = cms.bool(False),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfDeepCSVTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    vertex_associator = cms.InputTag("primaryVertexAssociation","original"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepFlavourTagInfosPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("DeepFlavourTagInfoProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    compute_probabilities = cms.bool(False),
    fallback_puppi_weight = cms.bool(False),
    fallback_vertex_association = cms.bool(False),
    flip = cms.bool(False),
    jet_radius = cms.double(0.4),
    jets = cms.InputTag("updatedPatJetsPatJetsAk8CHSJetsSoftDropSubjets"),
    max_jet_eta = cms.double(2.5),
    min_candidate_pt = cms.double(0.95),
    min_jet_pt = cms.double(15),
    puppi_value_map = cms.InputTag("puppi"),
    run_deepVertex = cms.bool(False),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfDeepCSVTagInfosPatJetsAk8CHSJetsSoftDropSubjets"),
    vertex_associator = cms.InputTag("primaryVertexAssociation","original"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepFlavourTagInfosPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("DeepFlavourTagInfoProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    compute_probabilities = cms.bool(False),
    fallback_puppi_weight = cms.bool(False),
    fallback_vertex_association = cms.bool(False),
    flip = cms.bool(False),
    jet_radius = cms.double(0.4),
    jets = cms.InputTag("updatedPatJetsPatJetsAk8PuppiJetsSoftDropSubjets"),
    max_jet_eta = cms.double(2.5),
    min_candidate_pt = cms.double(0.95),
    min_jet_pt = cms.double(15),
    puppi_value_map = cms.InputTag("puppi"),
    run_deepVertex = cms.bool(False),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfDeepCSVTagInfosPatJetsAk8PuppiJetsSoftDropSubjets"),
    vertex_associator = cms.InputTag("primaryVertexAssociation","original"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepFlavourTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepFlavourTagInfoProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    compute_probabilities = cms.bool(False),
    fallback_puppi_weight = cms.bool(False),
    fallback_vertex_association = cms.bool(False),
    flip = cms.bool(False),
    jet_radius = cms.double(0.4),
    jets = cms.InputTag("updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    max_jet_eta = cms.double(2.5),
    min_candidate_pt = cms.double(0.95),
    min_jet_pt = cms.double(15),
    puppi_value_map = cms.InputTag("puppi"),
    run_deepVertex = cms.bool(False),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfDeepCSVTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    vertex_associator = cms.InputTag("primaryVertexAssociation","original"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepFlavourTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining = cms.EDProducer("DeepFlavourTagInfoProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    compute_probabilities = cms.bool(False),
    fallback_puppi_weight = cms.bool(False),
    fallback_vertex_association = cms.bool(False),
    flip = cms.bool(False),
    jet_radius = cms.double(0.4),
    jets = cms.InputTag("updatedPatJetsRekeyPatJetsAK8PFPUPPINewDFTraining"),
    max_jet_eta = cms.double(2.5),
    min_candidate_pt = cms.double(0.95),
    min_jet_pt = cms.double(15),
    puppi_value_map = cms.InputTag("puppi"),
    run_deepVertex = cms.bool(False),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfDeepCSVTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining"),
    vertex_associator = cms.InputTag("primaryVertexAssociation","original"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepFlavourTagInfosSlimmedJetsNewDFTraining = cms.EDProducer("DeepFlavourTagInfoProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    compute_probabilities = cms.bool(False),
    fallback_puppi_weight = cms.bool(False),
    fallback_vertex_association = cms.bool(False),
    flip = cms.bool(False),
    jet_radius = cms.double(0.4),
    jets = cms.InputTag("updatedPatJetsSlimmedJetsNewDFTraining"),
    max_jet_eta = cms.double(2.5),
    min_candidate_pt = cms.double(0.95),
    min_jet_pt = cms.double(15),
    puppi_value_map = cms.InputTag(""),
    run_deepVertex = cms.bool(False),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfDeepCSVTagInfosSlimmedJetsNewDFTraining"),
    vertex_associator = cms.InputTag(""),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfDeepFlavourTagInfosSlimmedJetsPuppiNewDFTraining = cms.EDProducer("DeepFlavourTagInfoProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    compute_probabilities = cms.bool(False),
    fallback_puppi_weight = cms.bool(False),
    fallback_vertex_association = cms.bool(False),
    flip = cms.bool(False),
    jet_radius = cms.double(0.4),
    jets = cms.InputTag("updatedPatJetsSlimmedJetsPuppiNewDFTraining"),
    max_jet_eta = cms.double(2.5),
    min_candidate_pt = cms.double(0.95),
    min_jet_pt = cms.double(15),
    puppi_value_map = cms.InputTag(""),
    run_deepVertex = cms.bool(False),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfDeepCSVTagInfosSlimmedJetsPuppiNewDFTraining"),
    vertex_associator = cms.InputTag(""),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfImpactParameterAK8TagInfosAk8CHSJetsFat = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8CHSJetsFat"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosAk8CHSJetsSoftDrop = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8CHSJetsSoftDrop"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8CHSJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosAk8PuppiJetsFat = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsFat"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    maxDeltaR = cms.double(0.8),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterCA15TagInfosAk8CHSJetsFat = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8CHSJetsFat"),
    maxDeltaR = cms.double(1.5),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterCA15TagInfosAk8CHSJetsSoftDrop = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8CHSJetsSoftDrop"),
    maxDeltaR = cms.double(1.5),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterCA15TagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8CHSJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(1.5),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterCA15TagInfosAk8PuppiJetsFat = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsFat"),
    maxDeltaR = cms.double(1.5),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterCA15TagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    maxDeltaR = cms.double(1.5),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterCA15TagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(False),
    computeProbabilities = cms.bool(False),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(1.5),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8CHSJetsFat = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8CHSJetsFat"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8CHSJetsSoftDrop = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8CHSJetsSoftDrop"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8CHSJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8PuppiJetsFat = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsFat"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    explicitJTA = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsPatJetsAk8CHSJetsSoftDropSubjets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsPatJetsAk8PuppiJetsSoftDropSubjets"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsRekeyPatJetsAK8PFPUPPINewDFTraining"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosSlimmedJetsNewDFTraining = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsSlimmedJetsNewDFTraining"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfImpactParameterTagInfosSlimmedJetsPuppiNewDFTraining = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsSlimmedJetsPuppiNewDFTraining"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsFat = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8CHSJetsFat"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8CHSJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    fatJets = cms.InputTag("ak8CHSJetsFat"),
    groomedFatJets = cms.InputTag("ak8CHSJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8CHSJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsFat = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsFat"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    fatJets = cms.InputTag("ak8PuppiJetsFat"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.8),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.8),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.8),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsFat = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterCA15TagInfosAk8CHSJetsFat"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(1.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterCA15TagInfosAk8CHSJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(1.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(1.5),
    fatJets = cms.InputTag("ak8CHSJetsFat"),
    groomedFatJets = cms.InputTag("ak8CHSJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterCA15TagInfosAk8CHSJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(1.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsFat = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterCA15TagInfosAk8PuppiJetsFat"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(1.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterCA15TagInfosAk8PuppiJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(1.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(1.5),
    fatJets = cms.InputTag("ak8PuppiJetsFat"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterCA15TagInfosAk8PuppiJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(1.5),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(1.5),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsFat = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8CHSJetsFat"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8CHSJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    fatJets = cms.InputTag("ak8CHSJetsFat"),
    groomedFatJets = cms.InputTag("ak8CHSJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8CHSJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsFat = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsFat"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    fatJets = cms.InputTag("ak8PuppiJetsFat"),
    groomedFatJets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    jetAlgorithm = cms.string('AntiKt'),
    minimumTrackWeight = cms.double(0.5),
    rParam = cms.double(0.8),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    useSVClustering = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosPatJetsAk8CHSJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosPatJetsAk8PuppiJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosSlimmedJetsNewDFTraining = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosSlimmedJetsNewDFTraining"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfInclusiveSecondaryVertexFinderTagInfosSlimmedJetsPuppiNewDFTraining = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosSlimmedJetsPuppiNewDFTraining"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('TvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('WvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZHbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('HbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHqqqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('H4qvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHqqqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZHccvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('bbvsLight'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ccvsLight'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"))
        )
    )
)


process.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('TvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('WvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWcq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZHbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('HbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHqqqq"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('H4qvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHqqqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZHccvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('bbvsLight'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ccvsLight'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), cms.InputTag("pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"))
        )
    )
)


process.pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring(
        'probTbcq', 
        'probTbqq', 
        'probTbc', 
        'probTbq', 
        'probWcq', 
        'probWqq', 
        'probZbb', 
        'probZcc', 
        'probZqq', 
        'probHbb', 
        'probHcc', 
        'probHqqqq', 
        'probQCDbb', 
        'probQCDcc', 
        'probQCDb', 
        'probQCDc', 
        'probQCDothers'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet.onnx'),
    preprocessParams = cms.PSet(
        input_names = cms.vstring(
            'pfcand', 
            'sv'
        ),
        pfcand = cms.PSet(
            input_shape = cms.vuint32(1, 36, 100, 1),
            var_infos = cms.PSet(
                pfcand_VTX_ass = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(7.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_abseta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.632648706436),
                    norm_factor = cms.double(1.59032225958),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagEtaRel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.19703966379),
                    norm_factor = cms.double(0.521026991705),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagJetDistVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.000215483247302),
                    norm_factor = cms.double(161.385119349),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagPParRatio = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.839023888111),
                    norm_factor = cms.double(1.19186117841),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagPtRatio = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0173742230982),
                    norm_factor = cms.double(4.25351138308),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip2dSig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.41174531059),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip2dVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(495.583709284),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip3dSig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(0.831133090749),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip3dVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(233.664322627),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_charge = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_deltaR = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.252654820681),
                    norm_factor = cms.double(3.50836328292),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_detadeta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.15567200254e-08),
                    norm_factor = cms.double(1644010.14927),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dlambdadz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.2810873784e-07),
                    norm_factor = cms.double(268715.13012),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dphidphi = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.130510352e-08),
                    norm_factor = cms.double(796482.476472),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dphidxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-9.61654578191e-08),
                    norm_factor = cms.double(204149.346943),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dptdpt = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(4.11880840545e-08),
                    norm_factor = cms.double(66429.1000843),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_drminsv = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.192182734609),
                    norm_factor = cms.double(2.38205282141),
                    replace_inf_value = cms.double(-1),
                    upper_bound = cms.double(5)
                ),
                pfcand_drsubjet1 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.258241385221),
                    norm_factor = cms.double(2.92607580997),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_drsubjet2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.305164307356),
                    norm_factor = cms.double(2.88195895791),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(415.415835966),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxydxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.32332170578e-07),
                    norm_factor = cms.double(45949.2394216),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxydz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(10598589.4298),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxysig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.54565964258),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(264.770519024),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dzdz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.58729170607e-06),
                    norm_factor = cms.double(36545.958354),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dzsig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.23840120847),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_erel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-5.38221979141),
                    norm_factor = cms.double(0.556499386531),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_etarel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.00711047858931),
                    norm_factor = cms.double(4.2642743837),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_lostInnerHits = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_normchi2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(2.0),
                    norm_factor = cms.double(0.00100300902708),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_phirel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.71389010575e-05),
                    norm_factor = cms.double(4.22784626632),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_pt_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.03476798534),
                    norm_factor = cms.double(0.542224410728),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_ptrel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-5.37407469749),
                    norm_factor = cms.double(0.554677114485),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_puppiw = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.0),
                    norm_factor = cms.double(255.000015199),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_quality = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(5.0),
                    norm_factor = cms.double(0.2),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                )
            ),
            var_length = cms.uint32(100),
            var_names = cms.vstring(
                'pfcand_pt_log', 
                'pfcand_ptrel_log', 
                'pfcand_erel_log', 
                'pfcand_phirel', 
                'pfcand_etarel', 
                'pfcand_deltaR', 
                'pfcand_abseta', 
                'pfcand_puppiw', 
                'pfcand_drminsv', 
                'pfcand_drsubjet1', 
                'pfcand_drsubjet2', 
                'pfcand_charge', 
                'pfcand_VTX_ass', 
                'pfcand_lostInnerHits', 
                'pfcand_normchi2', 
                'pfcand_quality', 
                'pfcand_dz', 
                'pfcand_dzsig', 
                'pfcand_dxy', 
                'pfcand_dxysig', 
                'pfcand_dptdpt', 
                'pfcand_detadeta', 
                'pfcand_dphidphi', 
                'pfcand_dxydxy', 
                'pfcand_dzdz', 
                'pfcand_dxydz', 
                'pfcand_dphidxy', 
                'pfcand_dlambdadz', 
                'pfcand_btagEtaRel', 
                'pfcand_btagPtRatio', 
                'pfcand_btagPParRatio', 
                'pfcand_btagSip2dVal', 
                'pfcand_btagSip2dSig', 
                'pfcand_btagSip3dVal', 
                'pfcand_btagSip3dSig', 
                'pfcand_btagJetDistVal'
            )
        ),
        sv = cms.PSet(
            input_shape = cms.vuint32(1, 15, 7, 1),
            var_infos = cms.PSet(
                sv_abseta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.616221785545),
                    norm_factor = cms.double(1.49676942133),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_costhetasvpv = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.999747157097),
                    norm_factor = cms.double(174.907183727),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_d3d = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.5242870152),
                    norm_factor = cms.double(0.255813267634),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_d3dsig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.12465429306),
                    norm_factor = cms.double(0.0238374692882),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_deltaR = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.140969499946),
                    norm_factor = cms.double(4.30546783192),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_dxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.387232214212),
                    norm_factor = cms.double(0.360931771841),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_dxysig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.11130714417),
                    norm_factor = cms.double(0.0238327380073),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_erel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-2.82667005062),
                    norm_factor = cms.double(0.704463981589),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                sv_etarel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.0037129354896),
                    norm_factor = cms.double(6.99426943996),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_mass = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.34319722652),
                    norm_factor = cms.double(0.368495534421),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_normchi2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.819934427738),
                    norm_factor = cms.double(0.725797320076),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_ntracks = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(3.0),
                    norm_factor = cms.double(0.5),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_phirel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.000521215377375),
                    norm_factor = cms.double(7.16761972364),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_pt_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(3.64881515503),
                    norm_factor = cms.double(0.725050067872),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                sv_ptrel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-2.81496477127),
                    norm_factor = cms.double(0.701236308041),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                )
            ),
            var_length = cms.uint32(7),
            var_names = cms.vstring(
                'sv_pt_log', 
                'sv_ptrel_log', 
                'sv_erel_log', 
                'sv_phirel', 
                'sv_etarel', 
                'sv_deltaR', 
                'sv_abseta', 
                'sv_mass', 
                'sv_ntracks', 
                'sv_normchi2', 
                'sv_dxy', 
                'sv_dxysig', 
                'sv_d3d', 
                'sv_d3dsig', 
                'sv_costhetasvpv'
            )
        )
    ),
    preprocess_json = cms.string(''),
    src = cms.InputTag("pfDeepBoostedJetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining")
)


process.pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring(
        'probTbcq', 
        'probTbqq', 
        'probTbc', 
        'probTbq', 
        'probWcq', 
        'probWqq', 
        'probZbb', 
        'probZcc', 
        'probZqq', 
        'probHbb', 
        'probHcc', 
        'probHqqqq', 
        'probQCDbb', 
        'probQCDcc', 
        'probQCDb', 
        'probQCDc', 
        'probQCDothers'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepBoostedJet/V02/decorrelated/resnet.onnx'),
    preprocessParams = cms.PSet(
        input_names = cms.vstring(
            'pfcand', 
            'sv'
        ),
        pfcand = cms.PSet(
            input_shape = cms.vuint32(1, 36, 100, 1),
            var_infos = cms.PSet(
                pfcand_VTX_ass = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(7.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_abseta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.632648706436),
                    norm_factor = cms.double(1.59032225958),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagEtaRel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.19703966379),
                    norm_factor = cms.double(0.521026991705),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagJetDistVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.000215483247302),
                    norm_factor = cms.double(161.385119349),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagPParRatio = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.839023888111),
                    norm_factor = cms.double(1.19186117841),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagPtRatio = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0173742230982),
                    norm_factor = cms.double(4.25351138308),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip2dSig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.41174531059),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip2dVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(495.583709284),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip3dSig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(0.831133090749),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_btagSip3dVal = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(233.664322627),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_charge = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_deltaR = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.252654820681),
                    norm_factor = cms.double(3.50836328292),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_detadeta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.15567200254e-08),
                    norm_factor = cms.double(1644010.14927),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dlambdadz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.2810873784e-07),
                    norm_factor = cms.double(268715.13012),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dphidphi = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.130510352e-08),
                    norm_factor = cms.double(796482.476472),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dphidxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-9.61654578191e-08),
                    norm_factor = cms.double(204149.346943),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dptdpt = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(4.11880840545e-08),
                    norm_factor = cms.double(66429.1000843),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_drminsv = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.192182734609),
                    norm_factor = cms.double(2.38205282141),
                    replace_inf_value = cms.double(-1),
                    upper_bound = cms.double(5)
                ),
                pfcand_drsubjet1 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.258241385221),
                    norm_factor = cms.double(2.92607580997),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_drsubjet2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.305164307356),
                    norm_factor = cms.double(2.88195895791),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(415.415835966),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxydxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.32332170578e-07),
                    norm_factor = cms.double(45949.2394216),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxydz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(10598589.4298),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dxysig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.54565964258),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(264.770519024),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dzdz = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.58729170607e-06),
                    norm_factor = cms.double(36545.958354),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_dzsig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.0),
                    norm_factor = cms.double(1.23840120847),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_erel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-5.38221979141),
                    norm_factor = cms.double(0.556499386531),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_etarel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.00711047858931),
                    norm_factor = cms.double(4.2642743837),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_lostInnerHits = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.0),
                    norm_factor = cms.double(1.0),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_normchi2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(2.0),
                    norm_factor = cms.double(0.00100300902708),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_phirel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-1.71389010575e-05),
                    norm_factor = cms.double(4.22784626632),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_pt_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.03476798534),
                    norm_factor = cms.double(0.542224410728),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_ptrel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-5.37407469749),
                    norm_factor = cms.double(0.554677114485),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                pfcand_puppiw = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.0),
                    norm_factor = cms.double(255.000015199),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                pfcand_quality = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(5.0),
                    norm_factor = cms.double(0.2),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                )
            ),
            var_length = cms.uint32(100),
            var_names = cms.vstring(
                'pfcand_pt_log', 
                'pfcand_ptrel_log', 
                'pfcand_erel_log', 
                'pfcand_phirel', 
                'pfcand_etarel', 
                'pfcand_deltaR', 
                'pfcand_abseta', 
                'pfcand_puppiw', 
                'pfcand_drminsv', 
                'pfcand_drsubjet1', 
                'pfcand_drsubjet2', 
                'pfcand_charge', 
                'pfcand_VTX_ass', 
                'pfcand_lostInnerHits', 
                'pfcand_normchi2', 
                'pfcand_quality', 
                'pfcand_dz', 
                'pfcand_dzsig', 
                'pfcand_dxy', 
                'pfcand_dxysig', 
                'pfcand_dptdpt', 
                'pfcand_detadeta', 
                'pfcand_dphidphi', 
                'pfcand_dxydxy', 
                'pfcand_dzdz', 
                'pfcand_dxydz', 
                'pfcand_dphidxy', 
                'pfcand_dlambdadz', 
                'pfcand_btagEtaRel', 
                'pfcand_btagPtRatio', 
                'pfcand_btagPParRatio', 
                'pfcand_btagSip2dVal', 
                'pfcand_btagSip2dSig', 
                'pfcand_btagSip3dVal', 
                'pfcand_btagSip3dSig', 
                'pfcand_btagJetDistVal'
            )
        ),
        sv = cms.PSet(
            input_shape = cms.vuint32(1, 15, 7, 1),
            var_infos = cms.PSet(
                sv_abseta = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.616221785545),
                    norm_factor = cms.double(1.49676942133),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_costhetasvpv = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.999747157097),
                    norm_factor = cms.double(174.907183727),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_d3d = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.5242870152),
                    norm_factor = cms.double(0.255813267634),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_d3dsig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.12465429306),
                    norm_factor = cms.double(0.0238374692882),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_deltaR = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.140969499946),
                    norm_factor = cms.double(4.30546783192),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_dxy = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.387232214212),
                    norm_factor = cms.double(0.360931771841),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_dxysig = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(9.11130714417),
                    norm_factor = cms.double(0.0238327380073),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_erel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-2.82667005062),
                    norm_factor = cms.double(0.704463981589),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                sv_etarel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-0.0037129354896),
                    norm_factor = cms.double(6.99426943996),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_mass = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(1.34319722652),
                    norm_factor = cms.double(0.368495534421),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_normchi2 = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.819934427738),
                    norm_factor = cms.double(0.725797320076),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_ntracks = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(3.0),
                    norm_factor = cms.double(0.5),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_phirel = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(0.000521215377375),
                    norm_factor = cms.double(7.16761972364),
                    replace_inf_value = cms.double(0),
                    upper_bound = cms.double(5)
                ),
                sv_pt_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(3.64881515503),
                    norm_factor = cms.double(0.725050067872),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                ),
                sv_ptrel_log = cms.PSet(
                    lower_bound = cms.double(-5),
                    median = cms.double(-2.81496477127),
                    norm_factor = cms.double(0.701236308041),
                    replace_inf_value = cms.double(-99),
                    upper_bound = cms.double(5)
                )
            ),
            var_length = cms.uint32(7),
            var_names = cms.vstring(
                'sv_pt_log', 
                'sv_ptrel_log', 
                'sv_erel_log', 
                'sv_phirel', 
                'sv_etarel', 
                'sv_deltaR', 
                'sv_abseta', 
                'sv_mass', 
                'sv_ntracks', 
                'sv_normchi2', 
                'sv_dxy', 
                'sv_dxysig', 
                'sv_d3d', 
                'sv_d3dsig', 
                'sv_costhetasvpv'
            )
        )
    ),
    preprocess_json = cms.string(''),
    src = cms.InputTag("pfDeepBoostedJetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
)


process.pfMassDecorrelatedParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probXbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('XbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probXbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probXcc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('XccvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probXcc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probXqq"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('XqqvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probXqq"))
        )
    )
)


process.pfMassDecorrelatedParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probXbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('XbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probXbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probXcc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('XccvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probXcc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probXqq"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('XqqvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probXqq"))
        )
    )
)


process.pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring(
        'probXbb', 
        'probXcc', 
        'probXqq', 
        'probQCDbb', 
        'probQCDcc', 
        'probQCDb', 
        'probQCDc', 
        'probQCDothers'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/ParticleNetAK8/MD-2prong/V01/particle-net.onnx'),
    preprocessParams = cms.PSet(

    ),
    preprocess_json = cms.string('RecoBTag/Combined/data/ParticleNetAK8/MD-2prong/V01/preprocess.json'),
    src = cms.InputTag("pfParticleNetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining")
)


process.pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring(
        'probXbb', 
        'probXcc', 
        'probXqq', 
        'probQCDbb', 
        'probQCDcc', 
        'probQCDb', 
        'probQCDc', 
        'probQCDothers'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/ParticleNetAK8/MD-2prong/V01/particle-net.onnx'),
    preprocessParams = cms.PSet(

    ),
    preprocess_json = cms.string('RecoBTag/Combined/data/ParticleNetAK8/MD-2prong/V01/preprocess.json'),
    src = cms.InputTag("pfParticleNetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
)


process.pfMassIndependentDeepDoubleBvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probQCD', 
        'probHbb'
    ),
    flavor = cms.string('BvL'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDB_mass_independent.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfMassIndependentDeepDoubleBvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probQCD', 
        'probHbb'
    ),
    flavor = cms.string('BvL'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDB_mass_independent.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfMassIndependentDeepDoubleCvBJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probHbb', 
        'probHcc'
    ),
    flavor = cms.string('CvB'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDCvB_mass_independent.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfMassIndependentDeepDoubleCvBJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probHbb', 
        'probHcc'
    ),
    flavor = cms.string('CvB'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDCvB_mass_independent.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfMassIndependentDeepDoubleCvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probQCD', 
        'probHcc'
    ),
    flavor = cms.string('CvL'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDC_mass_independent.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosPackedPatJetsAk8CHSJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfMassIndependentDeepDoubleCvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepDoubleXONNXJetTagsProducer",
    flav_names = cms.vstring(
        'probQCD', 
        'probHcc'
    ),
    flavor = cms.string('CvL'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDC_mass_independent.onnx'),
    output_names = cms.vstring(),
    src = cms.InputTag("pfDeepDoubleXTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    version = cms.string('V1')
)


process.pfNoPileUp = cms.EDProducer("TPPFCandidatesOnPFCandidates",
    bottomCollection = cms.InputTag("convertedPackedPFCandidatePtrs"),
    enable = cms.bool(True),
    name = cms.untracked.string('pileUpOnPFCandidates'),
    topCollection = cms.InputTag("pfPileUp"),
    verbose = cms.untracked.bool(False)
)


process.pfParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbcq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbqq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('TvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbcq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probTbqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWcq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWqq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('WvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWcq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probWqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZqq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), 
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probZbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('HbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('HccvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHcc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHqqqq"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('H4qvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining","probHqqqq"))
        )
    )
)


process.pfParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BTagProbabilityToDiscriminator",
    discriminators = cms.VPSet(
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbcq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbqq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('TvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbcq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probTbqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWcq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWqq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), 
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('WvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWcq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probWqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZqq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), 
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZqq"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('ZbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probZbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('HbbvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHbb"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('HccvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHcc"))
        ), 
        cms.PSet(
            denominator = cms.VInputTag(
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHqqqq"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDbb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDcc"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDb"), cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDc"), 
                cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probQCDothers")
            ),
            name = cms.string('H4qvsQCD'),
            numerator = cms.VInputTag(cms.InputTag("pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining","probHqqqq"))
        )
    )
)


process.pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring(
        'probTbcq', 
        'probTbqq', 
        'probTbc', 
        'probTbq', 
        'probTbel', 
        'probTbmu', 
        'probTbta', 
        'probWcq', 
        'probWqq', 
        'probZbb', 
        'probZcc', 
        'probZqq', 
        'probHbb', 
        'probHcc', 
        'probHqqqq', 
        'probQCDbb', 
        'probQCDcc', 
        'probQCDb', 
        'probQCDc', 
        'probQCDothers'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/ParticleNetAK8/General/V01/particle-net.onnx'),
    preprocessParams = cms.PSet(

    ),
    preprocess_json = cms.string('RecoBTag/Combined/data/ParticleNetAK8/General/V01/preprocess.json'),
    src = cms.InputTag("pfParticleNetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining")
)


process.pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring(
        'probTbcq', 
        'probTbqq', 
        'probTbc', 
        'probTbq', 
        'probTbel', 
        'probTbmu', 
        'probTbta', 
        'probWcq', 
        'probWqq', 
        'probZbb', 
        'probZcc', 
        'probZqq', 
        'probHbb', 
        'probHcc', 
        'probHqqqq', 
        'probQCDbb', 
        'probQCDcc', 
        'probQCDb', 
        'probQCDc', 
        'probQCDothers'
    ),
    model_path = cms.FileInPath('RecoBTag/Combined/data/ParticleNetAK8/General/V01/particle-net.onnx'),
    preprocessParams = cms.PSet(

    ),
    preprocess_json = cms.string('RecoBTag/Combined/data/ParticleNetAK8/General/V01/preprocess.json'),
    src = cms.InputTag("pfParticleNetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
)


process.pfParticleNetMassRegressionJetTagsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring('mass'),
    model_path = cms.FileInPath('RecoBTag/Combined/data/ParticleNetAK8/MassRegression/V01/particle-net.onnx'),
    preprocessParams = cms.PSet(

    ),
    preprocess_json = cms.string('RecoBTag/Combined/data/ParticleNetAK8/MassRegression/V01/preprocess.json'),
    src = cms.InputTag("pfParticleNetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining")
)


process.pfParticleNetMassRegressionJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("BoostedJetONNXJetTagsProducer",
    debugMode = cms.untracked.bool(False),
    flav_names = cms.vstring('mass'),
    model_path = cms.FileInPath('RecoBTag/Combined/data/ParticleNetAK8/MassRegression/V01/particle-net.onnx'),
    preprocessParams = cms.PSet(

    ),
    preprocess_json = cms.string('RecoBTag/Combined/data/ParticleNetAK8/MassRegression/V01/preprocess.json'),
    src = cms.InputTag("pfParticleNetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
)


process.pfParticleNetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("DeepBoostedJetTagInfoProducer",
    flip_ip_sign = cms.bool(False),
    include_neutrals = cms.bool(True),
    jet_radius = cms.double(0.8),
    jets = cms.InputTag("updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining"),
    max_jet_eta = cms.double(99),
    min_jet_pt = cms.double(150),
    min_pt_for_track_properties = cms.double(-1),
    min_puppi_wgt = cms.double(0.01),
    pf_candidates = cms.InputTag("packedPFCandidates"),
    puppi_value_map = cms.InputTag(""),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    sip3dSigMax = cms.double(-1),
    sort_by_sip2dsig = cms.bool(False),
    use_puppiP4 = cms.bool(False),
    vertex_associator = cms.InputTag(""),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfParticleNetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("DeepBoostedJetTagInfoProducer",
    flip_ip_sign = cms.bool(False),
    include_neutrals = cms.bool(True),
    jet_radius = cms.double(0.8),
    jets = cms.InputTag("updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining"),
    max_jet_eta = cms.double(99),
    min_jet_pt = cms.double(150),
    min_pt_for_track_properties = cms.double(-1),
    min_puppi_wgt = cms.double(0.01),
    pf_candidates = cms.InputTag("packedPFCandidates"),
    puppi_value_map = cms.InputTag(""),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    sip3dSigMax = cms.double(-1),
    sort_by_sip2dsig = cms.bool(False),
    use_puppiP4 = cms.bool(False),
    vertex_associator = cms.InputTag(""),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfPileUp = cms.EDProducer("PFPileUp",
    Enable = cms.bool(True),
    PFCandidates = cms.InputTag("convertedPackedPFCandidatePtrs"),
    Vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    checkClosestZVertex = cms.bool(True),
    verbose = cms.untracked.bool(False)
)


process.pfSecondaryVertexTagInfosAk8CHSJetsFat = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8CHSJetsFat"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfSecondaryVertexTagInfosAk8CHSJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8CHSJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfSecondaryVertexTagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8CHSJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfSecondaryVertexTagInfosAk8PuppiJetsFat = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsFat"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfSecondaryVertexTagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDrop"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfSecondaryVertexTagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("secondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(False),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(3.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.65),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.pfWeightedNeutralHadrons = cms.EDProducer("DeltaBetaWeights",
    chargedFromPU = cms.InputTag("pfPileUpAllChargedParticles"),
    chargedFromPV = cms.InputTag("pfAllChargedParticles"),
    src = cms.InputTag("pfAllNeutralHadrons")
)


process.pfWeightedPhotons = cms.EDProducer("DeltaBetaWeights",
    chargedFromPU = cms.InputTag("pfPileUpAllChargedParticles"),
    chargedFromPV = cms.InputTag("pfAllChargedParticles"),
    src = cms.InputTag("pfAllPhotons")
)


process.photonIDValueMapProducer = cms.EDProducer("PhotonIDValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
    pfCandidates = cms.InputTag("particleFlow"),
    pfCandidatesMiniAOD = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag(""),
    srcMiniAOD = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.photonMVAValueMapProducer = cms.EDProducer("PhotonMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('Run2Spring16NonTrigV1'),
            nCategories = cms.int32(2),
            phoIsoCutoff = cms.double(2.5),
            phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v1p1'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v2'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz'
            )
        )
    ),
    src = cms.InputTag(""),
    srcMiniAOD = cms.InputTag("updatedPhotons")
)


process.prefiringweight = cms.EDProducer("L1PrefiringWeightProducer",
    DataEraECAL = cms.string('None'),
    DataEraMuon = cms.string('20172018'),
    DoMuons = cms.bool(True),
    PrefiringRateSystematicUnctyECAL = cms.double(0.2),
    PrefiringRateSystematicUnctyMuon = cms.double(0.2),
    TheJets = cms.InputTag("slimmedJets"),
    TheMuons = cms.InputTag("slimmedMuons"),
    ThePhotons = cms.InputTag("slimmedPhotons"),
    UseJetEMPt = cms.bool(False)
)


process.prunedPrunedGenParticles = cms.EDProducer("GenParticlePruner",
    select = cms.vstring(
        'drop *', 
        'keep status == 3', 
        'keep 20 <= status <= 30', 
        'keep 11 <= abs(pdgId) <= 16 && numberOfMothers()==1 && abs(mother().pdgId()) >= 23 && abs(mother().pdgId()) <= 25', 
        'keep 11 <= abs(pdgId) <= 16 && numberOfMothers()==1 && abs(mother().pdgId()) == 6', 
        'keep 11 <= abs(pdgId) <= 16 && numberOfMothers()==1 && abs(mother().pdgId()) == 42', 
        'drop 11 <= abs(pdgId) <= 16 && numberOfMothers() == 1 && abs(mother().pdgId())==6', 
        'keep 11 <= abs(pdgId) <= 16 && numberOfMothers() == 1 && abs(mother().pdgId())==6 && mother().numberOfDaughters() > 2 && abs(mother().daughter(0).pdgId()) != 24 && abs(mother().daughter(1).pdgId()) != 24 && abs(mother().daughter(2).pdgId()) != 24'
    ),
    src = cms.InputTag("prunedGenParticles")
)


process.ptRatioRelForEle = cms.EDProducer("ElectronJetVarProducer",
    srcJet = cms.InputTag("jetsAk4CHS"),
    srcLep = cms.InputTag("slimmedElectronsData"),
    srcVtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.ptRatioRelForMu = cms.EDProducer("MuonJetVarProducer",
    srcJet = cms.InputTag("jetsAk4CHS"),
    srcLep = cms.InputTag("slimmedMuonsData"),
    srcVtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.puppi = cms.EDProducer("PuppiProducer",
    DeltaZCut = cms.double(0.3),
    DeltaZCutForChargedFromPUVtxs = cms.double(0.2),
    EtaMaxCharged = cms.double(99999.0),
    EtaMinUseDeltaZ = cms.double(0.0),
    MinPuppiWeight = cms.double(0.01),
    NumOfPUVtxsForCharged = cms.uint32(0),
    PtMaxCharged = cms.double(0.0),
    PtMaxNeutrals = cms.double(200.0),
    PtMaxNeutralsStartSlope = cms.double(0.0),
    UseDeltaZCut = cms.bool(True),
    UseFromPVLooseTight = cms.bool(False),
    algos = cms.VPSet(
        cms.PSet(
            EtaMaxExtrap = cms.double(2.0),
            MedEtaSF = cms.vdouble(1.0),
            MinNeutralPt = cms.vdouble(0.2),
            MinNeutralPtSlope = cms.vdouble(0.015),
            RMSEtaSF = cms.vdouble(1.0),
            etaMax = cms.vdouble(2.5),
            etaMin = cms.vdouble(0.0),
            ptMin = cms.vdouble(0.0),
            puppiAlgos = cms.VPSet(cms.PSet(
                algoId = cms.int32(5),
                applyLowPUCorr = cms.bool(True),
                combOpt = cms.int32(0),
                cone = cms.double(0.4),
                rmsPtMin = cms.double(0.1),
                rmsScaleFactor = cms.double(1.0),
                useCharged = cms.bool(True)
            ))
        ), 
        cms.PSet(
            EtaMaxExtrap = cms.double(2.0),
            MedEtaSF = cms.vdouble(0.9, 0.75),
            MinNeutralPt = cms.vdouble(1.7, 2.0),
            MinNeutralPtSlope = cms.vdouble(0.08, 0.08),
            RMSEtaSF = cms.vdouble(1.2, 0.95),
            etaMax = cms.vdouble(3.0, 10.0),
            etaMin = cms.vdouble(2.5, 3.0),
            ptMin = cms.vdouble(0.0, 0.0),
            puppiAlgos = cms.VPSet(cms.PSet(
                algoId = cms.int32(5),
                applyLowPUCorr = cms.bool(True),
                combOpt = cms.int32(0),
                cone = cms.double(0.4),
                rmsPtMin = cms.double(0.5),
                rmsScaleFactor = cms.double(1.0),
                useCharged = cms.bool(False)
            ))
        )
    ),
    applyCHS = cms.bool(True),
    candName = cms.InputTag("packedPFCandidates"),
    clonePackedCands = cms.bool(True),
    invertPuppi = cms.bool(False),
    puppiDiagnostics = cms.bool(False),
    puppiForLeptons = cms.bool(False),
    useExistingWeights = cms.bool(True),
    useExp = cms.bool(False),
    useWeightsNoLep = cms.bool(False),
    vertexName = cms.InputTag("offlineSlimmedPrimaryVertices"),
    vtxNdofCut = cms.int32(4),
    vtxZCut = cms.double(24)
)


process.rekeyPackedPatJetsAk8PuppiJets = cms.EDProducer("JetSubstructurePacker",
    algoLabels = cms.vstring('SoftDropPuppi'),
    algoTags = cms.VInputTag(cms.InputTag("patJetsAk8PuppiJetsSoftDropPacked")),
    distMax = cms.double(0.8),
    fixDaughters = cms.bool(False),
    jetSrc = cms.InputTag("rekeyPatJetsAk8PuppiJetsFat")
)


process.rekeyPatJetsAK8PFPUPPI = cms.EDProducer("RekeyJets",
    candidateSrc = cms.InputTag("packedPFCandidates"),
    jetSrc = cms.InputTag("patJetsAK8PFPUPPI")
)


process.rekeyPatJetsAk8PuppiJetsFat = cms.EDProducer("RekeyJets",
    candidateSrc = cms.InputTag("packedPFCandidates"),
    jetSrc = cms.InputTag("patJetsAk8PuppiJetsFat")
)


process.rekeyUpdatedPatJetsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("RekeyJets",
    candidateSrc = cms.InputTag("packedPFCandidates"),
    jetSrc = cms.InputTag("updatedPatJetsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets")
)


process.rekeyUpdatedPatJetsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("RekeyJets",
    candidateSrc = cms.InputTag("packedPFCandidates"),
    jetSrc = cms.InputTag("updatedPatJetsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets")
)


process.slimmedElectrons = cms.EDProducer("ModifiedElectronProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
                    electronSrc = cms.InputTag("updatedElectrons")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    PhotonMVAEstimatorRunIIFall17v1p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    PhotonMVAEstimatorRunIIFall17v2Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
                    electronSrc = cms.InputTag("updatedElectrons")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    PhotonMVAEstimatorRunIIFall17v2Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-vetoBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-vetoBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-looseBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-mediumBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tightBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-vetoBitmap"),
                    electronSrc = cms.InputTag("updatedElectrons"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70Bitmap")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromUIntToIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tightBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tightBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-looseBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-mediumBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tightBitmap"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto"),
                    electronSrc = cms.InputTag("updatedElectrons"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70"),
                    mvaEleID_Fall17_iso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp80"),
                    mvaEleID_Fall17_iso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp90"),
                    mvaEleID_Fall17_iso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wpLoose"),
                    mvaEleID_Fall17_iso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp80"),
                    mvaEleID_Fall17_iso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp90"),
                    mvaEleID_Fall17_iso_V2_wpHZZ = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpHZZ"),
                    mvaEleID_Fall17_iso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpLoose"),
                    mvaEleID_Fall17_noIso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp80"),
                    mvaEleID_Fall17_noIso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp90"),
                    mvaEleID_Fall17_noIso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wpLoose"),
                    mvaEleID_Fall17_noIso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp80"),
                    mvaEleID_Fall17_noIso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp90"),
                    mvaEleID_Fall17_noIso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wpLoose"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp80"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp90"),
                    mvaEleID_Spring16_HZZ_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-HZZ-V1-wpLoose")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromEGIDValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-loose"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-medium"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tight"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-loose"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-medium"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tight"),
                    mvaPhoID_RunIIFall17_v1p1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp80"),
                    mvaPhoID_RunIIFall17_v1p1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp90"),
                    mvaPhoID_RunIIFall17_v2_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp80"),
                    mvaPhoID_RunIIFall17_v2_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp90"),
                    mvaPhoID_Spring16_nonTrig_V1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp80"),
                    mvaPhoID_Spring16_nonTrig_V1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp90"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    ecalEnergyErrPostCorr = cms.InputTag("calibratedPatElectrons","ecalEnergyErrPostCorr"),
                    ecalEnergyErrPreCorr = cms.InputTag("calibratedPatElectrons","ecalEnergyErrPreCorr"),
                    ecalEnergyPostCorr = cms.InputTag("calibratedPatElectrons","ecalEnergyPostCorr"),
                    ecalEnergyPreCorr = cms.InputTag("calibratedPatElectrons","ecalEnergyPreCorr"),
                    ecalTrkEnergyErrPostCorr = cms.InputTag("calibratedPatElectrons","ecalTrkEnergyErrPostCorr"),
                    ecalTrkEnergyErrPreCorr = cms.InputTag("calibratedPatElectrons","ecalTrkEnergyErrPreCorr"),
                    ecalTrkEnergyPostCorr = cms.InputTag("calibratedPatElectrons","ecalTrkEnergyPostCorr"),
                    ecalTrkEnergyPreCorr = cms.InputTag("calibratedPatElectrons","ecalTrkEnergyPreCorr"),
                    electronSrc = cms.InputTag("updatedElectrons"),
                    energyScaleDown = cms.InputTag("calibratedPatElectrons","energyScaleDown"),
                    energyScaleGainDown = cms.InputTag("calibratedPatElectrons","energyScaleGainDown"),
                    energyScaleGainUp = cms.InputTag("calibratedPatElectrons","energyScaleGainUp"),
                    energyScaleStatDown = cms.InputTag("calibratedPatElectrons","energyScaleStatDown"),
                    energyScaleStatUp = cms.InputTag("calibratedPatElectrons","energyScaleStatUp"),
                    energyScaleSystDown = cms.InputTag("calibratedPatElectrons","energyScaleSystDown"),
                    energyScaleSystUp = cms.InputTag("calibratedPatElectrons","energyScaleSystUp"),
                    energyScaleUp = cms.InputTag("calibratedPatElectrons","energyScaleUp"),
                    energyScaleValue = cms.InputTag("calibratedPatElectrons","energyScaleValue"),
                    energySigmaDown = cms.InputTag("calibratedPatElectrons","energySigmaDown"),
                    energySigmaPhiDown = cms.InputTag("calibratedPatElectrons","energySigmaPhiDown"),
                    energySigmaPhiUp = cms.InputTag("calibratedPatElectrons","energySigmaPhiUp"),
                    energySigmaRhoDown = cms.InputTag("calibratedPatElectrons","energySigmaRhoDown"),
                    energySigmaRhoUp = cms.InputTag("calibratedPatElectrons","energySigmaRhoUp"),
                    energySigmaUp = cms.InputTag("calibratedPatElectrons","energySigmaUp"),
                    energySigmaValue = cms.InputTag("calibratedPatElectrons","energySigmaValue"),
                    energySmearNrSigma = cms.InputTag("calibratedPatElectrons","energySmearNrSigma")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    ecalEnergyErrPostCorr = cms.InputTag("calibratedPatPhotons","ecalEnergyErrPostCorr"),
                    ecalEnergyErrPreCorr = cms.InputTag("calibratedPatPhotons","ecalEnergyErrPreCorr"),
                    ecalEnergyPostCorr = cms.InputTag("calibratedPatPhotons","ecalEnergyPostCorr"),
                    ecalEnergyPreCorr = cms.InputTag("calibratedPatPhotons","ecalEnergyPreCorr"),
                    energyScaleDown = cms.InputTag("calibratedPatPhotons","energyScaleDown"),
                    energyScaleGainDown = cms.InputTag("calibratedPatPhotons","energyScaleGainDown"),
                    energyScaleGainUp = cms.InputTag("calibratedPatPhotons","energyScaleGainUp"),
                    energyScaleStatDown = cms.InputTag("calibratedPatPhotons","energyScaleStatDown"),
                    energyScaleStatUp = cms.InputTag("calibratedPatPhotons","energyScaleStatUp"),
                    energyScaleSystDown = cms.InputTag("calibratedPatPhotons","energyScaleSystDown"),
                    energyScaleSystUp = cms.InputTag("calibratedPatPhotons","energyScaleSystUp"),
                    energyScaleUp = cms.InputTag("calibratedPatPhotons","energyScaleUp"),
                    energyScaleValue = cms.InputTag("calibratedPatPhotons","energyScaleValue"),
                    energySigmaDown = cms.InputTag("calibratedPatPhotons","energySigmaDown"),
                    energySigmaPhiDown = cms.InputTag("calibratedPatPhotons","energySigmaPhiDown"),
                    energySigmaPhiUp = cms.InputTag("calibratedPatPhotons","energySigmaPhiUp"),
                    energySigmaRhoDown = cms.InputTag("calibratedPatPhotons","energySigmaRhoDown"),
                    energySigmaRhoUp = cms.InputTag("calibratedPatPhotons","energySigmaRhoUp"),
                    energySigmaUp = cms.InputTag("calibratedPatPhotons","energySigmaUp"),
                    energySigmaValue = cms.InputTag("calibratedPatPhotons","energySigmaValue"),
                    energySmearNrSigma = cms.InputTag("calibratedPatPhotons","energySmearNrSigma"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                epCombConfig = cms.PSet(
                    ecalTrkRegressionConfig = cms.PSet(
                        ebHighEtForestName = cms.string('electron_eb_ECALTRK'),
                        ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt'),
                        eeHighEtForestName = cms.string('electron_ee_ECALTRK'),
                        eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt'),
                        forceHighEnergyTrainingIfSaturated = cms.bool(False),
                        lowEtHighEtBoundary = cms.double(50.0),
                        rangeMaxHighEt = cms.double(3.0),
                        rangeMaxLowEt = cms.double(3.0),
                        rangeMinHighEt = cms.double(-1.0),
                        rangeMinLowEt = cms.double(-1.0)
                    ),
                    ecalTrkRegressionUncertConfig = cms.PSet(
                        ebHighEtForestName = cms.string('electron_eb_ECALTRK_var'),
                        ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt_var'),
                        eeHighEtForestName = cms.string('electron_ee_ECALTRK_var'),
                        eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt_var'),
                        forceHighEnergyTrainingIfSaturated = cms.bool(False),
                        lowEtHighEtBoundary = cms.double(50.0),
                        rangeMaxHighEt = cms.double(0.5),
                        rangeMaxLowEt = cms.double(0.5),
                        rangeMinHighEt = cms.double(0.0002),
                        rangeMinLowEt = cms.double(0.0002)
                    ),
                    maxEPDiffInSigmaForComb = cms.double(15.0),
                    maxEcalEnergyForComb = cms.double(200.0),
                    maxRelTrkMomErrForComb = cms.double(10.0),
                    minEOverPForComb = cms.double(0.025)
                ),
                modifierName = cms.string('EGEtScaleSysModifier'),
                overrideExistingValues = cms.bool(True),
                uncertFunc = cms.PSet(
                    highEt = cms.double(46.5),
                    highEtUncert = cms.double(-0.002),
                    lowEt = cms.double(43.5),
                    lowEtUncert = cms.double(0.002),
                    name = cms.string('UncertFuncV1')
                )
            )
        )
    ),
    src = cms.InputTag("updatedElectrons")
)


process.slimmedElectronsData = cms.EDProducer("PATElectronUserData",
    effAreas_file = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
    src = cms.InputTag("slimmedElectrons"),
    vmaps_double = cms.vstring(
        'elPFMiniIsoValueCHSTAND', 
        'elPFMiniIsoValueNHSTAND', 
        'elPFMiniIsoValuePhSTAND', 
        'elPFMiniIsoValuePUSTAND', 
        'elPFMiniIsoValueNHPFWGT', 
        'elPFMiniIsoValuePhPFWGT'
    )
)


process.slimmedElectronsUSER = cms.EDProducer("PATElectronUserDataEmbedder",
    src = cms.InputTag("slimmedElectronsWithUserData"),
    userFloats = cms.PSet(
        mvaTOP = cms.InputTag("electronMVATOP")
    )
)


process.slimmedElectronsWithUserData = cms.EDProducer("PATElectronUserDataEmbedder",
    src = cms.InputTag("slimmedElectronsData"),
    userCands = cms.PSet(
        jetForLepJetVar = cms.InputTag("ptRatioRelForEle","jetForLepJetVar")
    ),
    userFloats = cms.PSet(
        PFIsoAll = cms.InputTag("isoForEle","PFIsoAll"),
        PFIsoAll04 = cms.InputTag("isoForEle","PFIsoAll04"),
        PFIsoChg = cms.InputTag("isoForEle","PFIsoChg"),
        jetNDauChargedMVASel = cms.InputTag("ptRatioRelForEle","jetNDauChargedMVASel"),
        miniIsoAll = cms.InputTag("isoForEle","miniIsoAll"),
        miniIsoChg = cms.InputTag("isoForEle","miniIsoChg"),
        mvaFall17V2noIso = cms.InputTag("electronMVAValueMapProducerv2","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
        ptRatio = cms.InputTag("ptRatioRelForEle","ptRatio"),
        ptRel = cms.InputTag("ptRatioRelForEle","ptRel")
    )
)


process.slimmedMuonsData = cms.EDProducer("PATMuonUserData",
    src = cms.InputTag("slimmedMuons"),
    vmaps_double = cms.vstring(
        'muPFMiniIsoValueCHSTAND', 
        'muPFMiniIsoValueNHSTAND', 
        'muPFMiniIsoValuePhSTAND', 
        'muPFMiniIsoValuePUSTAND', 
        'muPFMiniIsoValueNHPFWGT', 
        'muPFMiniIsoValuePhPFWGT'
    )
)


process.slimmedMuonsUSER = cms.EDProducer("PATMuonUserDataEmbedder",
    src = cms.InputTag("slimmedMuonsWithUserData"),
    userFloats = cms.PSet(
        mvaTOP = cms.InputTag("muonMVATOP")
    )
)


process.slimmedMuonsWithUserData = cms.EDProducer("PATMuonUserDataEmbedder",
    src = cms.InputTag("slimmedMuonsData"),
    userCands = cms.PSet(
        jetForLepJetVar = cms.InputTag("ptRatioRelForMu","jetForLepJetVar")
    ),
    userFloats = cms.PSet(
        jetNDauChargedMVASel = cms.InputTag("ptRatioRelForMu","jetNDauChargedMVASel"),
        miniIsoAll = cms.InputTag("isoForMu","miniIsoAll"),
        miniIsoChg = cms.InputTag("isoForMu","miniIsoChg"),
        ptRatio = cms.InputTag("ptRatioRelForMu","ptRatio"),
        ptRel = cms.InputTag("ptRatioRelForMu","ptRel")
    )
)


process.slimmedPhotonsUSER = cms.EDProducer("ModifiedPhotonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Values = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
                    electronSrc = cms.InputTag("updatedElectrons")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    PhotonMVAEstimatorRunIIFall17v1p1Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
                    PhotonMVAEstimatorRunIIFall17v2Values = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    ElectronMVAEstimatorRun2Fall17IsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17IsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    ElectronMVAEstimatorRun2Fall17NoIsoV2Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    ElectronMVAEstimatorRun2Spring16HZZV1Categories = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Categories"),
                    electronSrc = cms.InputTag("updatedElectrons")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    PhotonMVAEstimatorRun2Spring16NonTrigV1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    PhotonMVAEstimatorRunIIFall17v1p1Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
                    PhotonMVAEstimatorRunIIFall17v2Categories = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-vetoBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-looseBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tightBitmap"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-vetoBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-looseBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-mediumBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tightBitmap"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-vetoBitmap"),
                    electronSrc = cms.InputTag("updatedElectrons"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70Bitmap")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromUIntToIntValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tightBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-looseBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-mediumBitmap"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tightBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-looseBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-mediumBitmap"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tightBitmap"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    cutBasedElectronID_Fall17_94X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose"),
                    cutBasedElectronID_Fall17_94X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium"),
                    cutBasedElectronID_Fall17_94X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight"),
                    cutBasedElectronID_Fall17_94X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto"),
                    cutBasedElectronID_Fall17_94X_V2_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose"),
                    cutBasedElectronID_Fall17_94X_V2_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium"),
                    cutBasedElectronID_Fall17_94X_V2_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight"),
                    cutBasedElectronID_Fall17_94X_V2_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto"),
                    cutBasedElectronID_Summer16_80X_V1_loose = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose"),
                    cutBasedElectronID_Summer16_80X_V1_medium = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium"),
                    cutBasedElectronID_Summer16_80X_V1_tight = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight"),
                    cutBasedElectronID_Summer16_80X_V1_veto = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto"),
                    electronSrc = cms.InputTag("updatedElectrons"),
                    heepElectronID_HEEPV70 = cms.InputTag("egmGsfElectronIDs","heepElectronID-HEEPV70"),
                    mvaEleID_Fall17_iso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp80"),
                    mvaEleID_Fall17_iso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp90"),
                    mvaEleID_Fall17_iso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wpLoose"),
                    mvaEleID_Fall17_iso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp80"),
                    mvaEleID_Fall17_iso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp90"),
                    mvaEleID_Fall17_iso_V2_wpHZZ = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpHZZ"),
                    mvaEleID_Fall17_iso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpLoose"),
                    mvaEleID_Fall17_noIso_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp80"),
                    mvaEleID_Fall17_noIso_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp90"),
                    mvaEleID_Fall17_noIso_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wpLoose"),
                    mvaEleID_Fall17_noIso_V2_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp80"),
                    mvaEleID_Fall17_noIso_V2_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp90"),
                    mvaEleID_Fall17_noIso_V2_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wpLoose"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp80 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp80"),
                    mvaEleID_Spring16_GeneralPurpose_V1_wp90 = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp90"),
                    mvaEleID_Spring16_HZZ_V1_wpLoose = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-HZZ-V1-wpLoose")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromEGIDValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    cutBasedPhotonID_Fall17_94X_V1_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-loose"),
                    cutBasedPhotonID_Fall17_94X_V1_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-medium"),
                    cutBasedPhotonID_Fall17_94X_V1_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tight"),
                    cutBasedPhotonID_Fall17_94X_V2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose"),
                    cutBasedPhotonID_Fall17_94X_V2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium"),
                    cutBasedPhotonID_Fall17_94X_V2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight"),
                    cutBasedPhotonID_Spring16_V2p2_loose = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-loose"),
                    cutBasedPhotonID_Spring16_V2p2_medium = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-medium"),
                    cutBasedPhotonID_Spring16_V2p2_tight = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tight"),
                    mvaPhoID_RunIIFall17_v1p1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp80"),
                    mvaPhoID_RunIIFall17_v1p1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v1p1-wp90"),
                    mvaPhoID_RunIIFall17_v2_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp80"),
                    mvaPhoID_RunIIFall17_v2_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp90"),
                    mvaPhoID_Spring16_nonTrig_V1_wp80 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp80"),
                    mvaPhoID_Spring16_nonTrig_V1_wp90 = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp90"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                electron_config = cms.PSet(
                    ecalEnergyErrPostCorr = cms.InputTag("calibratedPatElectrons","ecalEnergyErrPostCorr"),
                    ecalEnergyErrPreCorr = cms.InputTag("calibratedPatElectrons","ecalEnergyErrPreCorr"),
                    ecalEnergyPostCorr = cms.InputTag("calibratedPatElectrons","ecalEnergyPostCorr"),
                    ecalEnergyPreCorr = cms.InputTag("calibratedPatElectrons","ecalEnergyPreCorr"),
                    ecalTrkEnergyErrPostCorr = cms.InputTag("calibratedPatElectrons","ecalTrkEnergyErrPostCorr"),
                    ecalTrkEnergyErrPreCorr = cms.InputTag("calibratedPatElectrons","ecalTrkEnergyErrPreCorr"),
                    ecalTrkEnergyPostCorr = cms.InputTag("calibratedPatElectrons","ecalTrkEnergyPostCorr"),
                    ecalTrkEnergyPreCorr = cms.InputTag("calibratedPatElectrons","ecalTrkEnergyPreCorr"),
                    electronSrc = cms.InputTag("updatedElectrons"),
                    energyScaleDown = cms.InputTag("calibratedPatElectrons","energyScaleDown"),
                    energyScaleGainDown = cms.InputTag("calibratedPatElectrons","energyScaleGainDown"),
                    energyScaleGainUp = cms.InputTag("calibratedPatElectrons","energyScaleGainUp"),
                    energyScaleStatDown = cms.InputTag("calibratedPatElectrons","energyScaleStatDown"),
                    energyScaleStatUp = cms.InputTag("calibratedPatElectrons","energyScaleStatUp"),
                    energyScaleSystDown = cms.InputTag("calibratedPatElectrons","energyScaleSystDown"),
                    energyScaleSystUp = cms.InputTag("calibratedPatElectrons","energyScaleSystUp"),
                    energyScaleUp = cms.InputTag("calibratedPatElectrons","energyScaleUp"),
                    energyScaleValue = cms.InputTag("calibratedPatElectrons","energyScaleValue"),
                    energySigmaDown = cms.InputTag("calibratedPatElectrons","energySigmaDown"),
                    energySigmaPhiDown = cms.InputTag("calibratedPatElectrons","energySigmaPhiDown"),
                    energySigmaPhiUp = cms.InputTag("calibratedPatElectrons","energySigmaPhiUp"),
                    energySigmaRhoDown = cms.InputTag("calibratedPatElectrons","energySigmaRhoDown"),
                    energySigmaRhoUp = cms.InputTag("calibratedPatElectrons","energySigmaRhoUp"),
                    energySigmaUp = cms.InputTag("calibratedPatElectrons","energySigmaUp"),
                    energySigmaValue = cms.InputTag("calibratedPatElectrons","energySigmaValue"),
                    energySmearNrSigma = cms.InputTag("calibratedPatElectrons","energySmearNrSigma")
                ),
                modifierName = cms.string('EGExtraInfoModifierFromFloatValueMaps'),
                overrideExistingValues = cms.bool(True),
                photon_config = cms.PSet(
                    ecalEnergyErrPostCorr = cms.InputTag("calibratedPatPhotons","ecalEnergyErrPostCorr"),
                    ecalEnergyErrPreCorr = cms.InputTag("calibratedPatPhotons","ecalEnergyErrPreCorr"),
                    ecalEnergyPostCorr = cms.InputTag("calibratedPatPhotons","ecalEnergyPostCorr"),
                    ecalEnergyPreCorr = cms.InputTag("calibratedPatPhotons","ecalEnergyPreCorr"),
                    energyScaleDown = cms.InputTag("calibratedPatPhotons","energyScaleDown"),
                    energyScaleGainDown = cms.InputTag("calibratedPatPhotons","energyScaleGainDown"),
                    energyScaleGainUp = cms.InputTag("calibratedPatPhotons","energyScaleGainUp"),
                    energyScaleStatDown = cms.InputTag("calibratedPatPhotons","energyScaleStatDown"),
                    energyScaleStatUp = cms.InputTag("calibratedPatPhotons","energyScaleStatUp"),
                    energyScaleSystDown = cms.InputTag("calibratedPatPhotons","energyScaleSystDown"),
                    energyScaleSystUp = cms.InputTag("calibratedPatPhotons","energyScaleSystUp"),
                    energyScaleUp = cms.InputTag("calibratedPatPhotons","energyScaleUp"),
                    energyScaleValue = cms.InputTag("calibratedPatPhotons","energyScaleValue"),
                    energySigmaDown = cms.InputTag("calibratedPatPhotons","energySigmaDown"),
                    energySigmaPhiDown = cms.InputTag("calibratedPatPhotons","energySigmaPhiDown"),
                    energySigmaPhiUp = cms.InputTag("calibratedPatPhotons","energySigmaPhiUp"),
                    energySigmaRhoDown = cms.InputTag("calibratedPatPhotons","energySigmaRhoDown"),
                    energySigmaRhoUp = cms.InputTag("calibratedPatPhotons","energySigmaRhoUp"),
                    energySigmaUp = cms.InputTag("calibratedPatPhotons","energySigmaUp"),
                    energySigmaValue = cms.InputTag("calibratedPatPhotons","energySigmaValue"),
                    energySmearNrSigma = cms.InputTag("calibratedPatPhotons","energySmearNrSigma"),
                    photonSrc = cms.InputTag("updatedPhotons")
                )
            ), 
            cms.PSet(
                epCombConfig = cms.PSet(
                    ecalTrkRegressionConfig = cms.PSet(
                        ebHighEtForestName = cms.string('electron_eb_ECALTRK'),
                        ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt'),
                        eeHighEtForestName = cms.string('electron_ee_ECALTRK'),
                        eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt'),
                        forceHighEnergyTrainingIfSaturated = cms.bool(False),
                        lowEtHighEtBoundary = cms.double(50.0),
                        rangeMaxHighEt = cms.double(3.0),
                        rangeMaxLowEt = cms.double(3.0),
                        rangeMinHighEt = cms.double(-1.0),
                        rangeMinLowEt = cms.double(-1.0)
                    ),
                    ecalTrkRegressionUncertConfig = cms.PSet(
                        ebHighEtForestName = cms.string('electron_eb_ECALTRK_var'),
                        ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt_var'),
                        eeHighEtForestName = cms.string('electron_ee_ECALTRK_var'),
                        eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt_var'),
                        forceHighEnergyTrainingIfSaturated = cms.bool(False),
                        lowEtHighEtBoundary = cms.double(50.0),
                        rangeMaxHighEt = cms.double(0.5),
                        rangeMaxLowEt = cms.double(0.5),
                        rangeMinHighEt = cms.double(0.0002),
                        rangeMinLowEt = cms.double(0.0002)
                    ),
                    maxEPDiffInSigmaForComb = cms.double(15.0),
                    maxEcalEnergyForComb = cms.double(200.0),
                    maxRelTrkMomErrForComb = cms.double(10.0),
                    minEOverPForComb = cms.double(0.025)
                ),
                modifierName = cms.string('EGEtScaleSysModifier'),
                overrideExistingValues = cms.bool(True),
                uncertFunc = cms.PSet(
                    highEt = cms.double(46.5),
                    highEtUncert = cms.double(-0.002),
                    lowEt = cms.double(43.5),
                    lowEtUncert = cms.double(0.002),
                    name = cms.string('UncertFuncV1')
                )
            )
        )
    ),
    src = cms.InputTag("updatedPhotons")
)


process.softPFElectronsTagInfosAk8CHSJetsFat = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.4),
    MaxSip3Dsig = cms.double(200),
    electrons = cms.InputTag("slimmedElectrons"),
    jets = cms.InputTag("ak8CHSJetsFat"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFElectronsTagInfosAk8CHSJetsSoftDrop = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.4),
    MaxSip3Dsig = cms.double(200),
    electrons = cms.InputTag("slimmedElectrons"),
    jets = cms.InputTag("ak8CHSJetsSoftDrop"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFElectronsTagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.4),
    MaxSip3Dsig = cms.double(200),
    electrons = cms.InputTag("slimmedElectrons"),
    jets = cms.InputTag("ak8CHSJetsSoftDrop","SubJets"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFElectronsTagInfosAk8PuppiJetsFat = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.4),
    MaxSip3Dsig = cms.double(200),
    electrons = cms.InputTag("slimmedElectrons"),
    jets = cms.InputTag("ak8PuppiJetsFat"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFElectronsTagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.4),
    MaxSip3Dsig = cms.double(200),
    electrons = cms.InputTag("slimmedElectrons"),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFElectronsTagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("SoftPFElectronTagInfoProducer",
    DeltaRElectronJet = cms.double(0.4),
    MaxSip3Dsig = cms.double(200),
    electrons = cms.InputTag("slimmedElectrons"),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFMuonsTagInfosAk8CHSJetsFat = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIpsig = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak8CHSJetsFat"),
    muonPt = cms.double(2.0),
    muonSIPsig = cms.double(200.0),
    muons = cms.InputTag("slimmedMuons"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFMuonsTagInfosAk8CHSJetsSoftDrop = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIpsig = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak8CHSJetsSoftDrop"),
    muonPt = cms.double(2.0),
    muonSIPsig = cms.double(200.0),
    muons = cms.InputTag("slimmedMuons"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFMuonsTagInfosAk8CHSJetsSoftDropSubjets = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIpsig = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak8CHSJetsSoftDrop","SubJets"),
    muonPt = cms.double(2.0),
    muonSIPsig = cms.double(200.0),
    muons = cms.InputTag("slimmedMuons"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFMuonsTagInfosAk8PuppiJetsFat = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIpsig = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak8PuppiJetsFat"),
    muonPt = cms.double(2.0),
    muonSIPsig = cms.double(200.0),
    muons = cms.InputTag("slimmedMuons"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFMuonsTagInfosAk8PuppiJetsSoftDrop = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIpsig = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop"),
    muonPt = cms.double(2.0),
    muonSIPsig = cms.double(200.0),
    muons = cms.InputTag("slimmedMuons"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.softPFMuonsTagInfosAk8PuppiJetsSoftDropSubjets = cms.EDProducer("SoftPFMuonTagInfoProducer",
    filterIpsig = cms.double(4.0),
    filterPromptMuons = cms.bool(False),
    filterRatio1 = cms.double(0.4),
    filterRatio2 = cms.double(0.7),
    jets = cms.InputTag("ak8PuppiJetsSoftDrop","SubJets"),
    muonPt = cms.double(2.0),
    muonSIPsig = cms.double(200.0),
    muons = cms.InputTag("slimmedMuons"),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.updatedElectrons = cms.EDProducer("ModifiedElectronProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(cms.PSet(
            allowGsfTrackForConvs = cms.bool(False),
            beamspot = cms.InputTag("offlineBeamSpot"),
            conversions = cms.InputTag("reducedEgamma","reducedConversions"),
            ecalRecHitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
            ecalRecHitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
            eleCollVMsAreKeyedTo = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
            eleTrkIso = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso"),
            eleTrkIso04 = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso04"),
            modifierName = cms.string('EG9X105XObjectUpdateModifier'),
            phoChargedHadIso = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
            phoChargedHadPFPVIso = cms.InputTag("egmPhotonIsolation","h+-DR030-"),
            phoChargedHadWorstVtxConeVetoIso = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolationConeVeto"),
            phoChargedHadWorstVtxIso = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
            phoCollVMsAreKeyedTo = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
            phoNeutralHadIso = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
            phoPhotonIso = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
            updateChargedHadPFPVIso = cms.bool(True)
        ))
    ),
    src = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsPackedPatJetsAk8CHSJetsNewDFTraining")),
    jetSource = cms.InputTag("packedPatJetsAk8CHSJets"),
    printWarning = cms.bool(False),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsPatJetsAk8CHSJetsSoftDropSubjets")),
    jetSource = cms.InputTag("patJetsAk8CHSJetsSoftDropSubjets"),
    printWarning = cms.bool(False),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsPatJetsAk8PuppiJetsSoftDropSubjets")),
    jetSource = cms.InputTag("patJetsAk8PuppiJetsSoftDropSubjets"),
    printWarning = cms.bool(False),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")),
    jetSource = cms.InputTag("rekeyPackedPatJetsAk8PuppiJets"),
    printWarning = cms.bool(False),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsRekeyPatJetsAK8PFPUPPINewDFTraining = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsRekeyPatJetsAK8PFPUPPINewDFTraining")),
    jetSource = cms.InputTag("rekeyPatJetsAK8PFPUPPI"),
    printWarning = cms.bool(False),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsSlimmedJetsNewDFTraining = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsSlimmedJetsNewDFTraining")),
    jetSource = cms.InputTag("slimmedJets"),
    printWarning = cms.bool(False),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsSlimmedJetsPuppiNewDFTraining = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsSlimmedJetsPuppiNewDFTraining")),
    jetSource = cms.InputTag("slimmedJetsPuppi"),
    printWarning = cms.bool(False),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8CHSJetsSoftDropSubjets","probb"), cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8CHSJetsSoftDropSubjets","probc"), cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8CHSJetsSoftDropSubjets","probg"), cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8CHSJetsSoftDropSubjets","problepb"), cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8CHSJetsSoftDropSubjets","probbb"), 
        cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8CHSJetsSoftDropSubjets","probuds")
    ),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets")),
    jetSource = cms.InputTag("updatedPatJetsPatJetsAk8CHSJetsSoftDropSubjets"),
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfDeepFlavourTagInfosPatJetsAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfDeepCSVTagInfosPatJetsAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfImpactParameterTagInfosPatJetsAk8CHSJetsSoftDropSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosPatJetsAk8CHSJetsSoftDropSubjets")),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(
        cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8PuppiJetsSoftDropSubjets","probb"), cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8PuppiJetsSoftDropSubjets","probc"), cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8PuppiJetsSoftDropSubjets","probg"), cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8PuppiJetsSoftDropSubjets","problepb"), cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8PuppiJetsSoftDropSubjets","probbb"), 
        cms.InputTag("pfDeepFlavourJetTagsPatJetsAk8PuppiJetsSoftDropSubjets","probuds")
    ),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets")),
    jetSource = cms.InputTag("updatedPatJetsPatJetsAk8PuppiJetsSoftDropSubjets"),
    printWarning = cms.bool(True),
    sort = cms.bool(True),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfDeepFlavourTagInfosPatJetsAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfDeepCSVTagInfosPatJetsAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfImpactParameterTagInfosPatJetsAk8PuppiJetsSoftDropSubjets"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosPatJetsAk8PuppiJetsSoftDropSubjets")),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPhotons = cms.EDProducer("ModifiedPhotonProducer",
    modifierConfig = cms.PSet(
        modifications = cms.VPSet(cms.PSet(
            allowGsfTrackForConvs = cms.bool(False),
            beamspot = cms.InputTag("offlineBeamSpot"),
            conversions = cms.InputTag("reducedEgamma","reducedConversions"),
            ecalRecHitsEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
            ecalRecHitsEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
            eleCollVMsAreKeyedTo = cms.InputTag("slimmedElectrons","","@skipCurrentProcess"),
            eleTrkIso = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso"),
            eleTrkIso04 = cms.InputTag("heepIDVarValueMaps","eleTrkPtIso04"),
            modifierName = cms.string('EG9X105XObjectUpdateModifier'),
            phoChargedHadIso = cms.InputTag("photonIDValueMapProducer","phoChargedIsolation"),
            phoChargedHadPFPVIso = cms.InputTag("egmPhotonIsolation","h+-DR030-"),
            phoChargedHadWorstVtxConeVetoIso = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolationConeVeto"),
            phoChargedHadWorstVtxIso = cms.InputTag("photonIDValueMapProducer","phoWorstChargedIsolation"),
            phoCollVMsAreKeyedTo = cms.InputTag("slimmedPhotons","","@skipCurrentProcess"),
            phoNeutralHadIso = cms.InputTag("photonIDValueMapProducer","phoNeutralHadronIsolation"),
            phoPhotonIso = cms.InputTag("photonIDValueMapProducer","phoPhotonIsolation"),
            updateChargedHadPFPVIso = cms.bool(True)
        ))
    ),
    src = cms.InputTag("slimmedPhotons","","@skipCurrentProcess")
)


process.xconeCHS = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(3),
    RJets = cms.double(1.2),
    RSubJets = cms.double(0.4),
    src = cms.InputTag("chs"),
    usePseudoXCone = cms.bool(True)
)


process.xconeCHS2jets04 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.4),
    RSubJets = cms.double(0.2),
    src = cms.InputTag("chs"),
    usePseudoXCone = cms.bool(True)
)


process.xconeCHS2jets08 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.8),
    RSubJets = cms.double(0.4),
    src = cms.InputTag("chs"),
    usePseudoXCone = cms.bool(True)
)


process.xconeCHS3jets04 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(3),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.4),
    RSubJets = cms.double(0.2),
    src = cms.InputTag("chs"),
    usePseudoXCone = cms.bool(True)
)


process.xconeCHS3jets08 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(3),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.8),
    RSubJets = cms.double(0.4),
    src = cms.InputTag("chs"),
    usePseudoXCone = cms.bool(True)
)


process.xconeCHS4jets04 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(4),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.4),
    RSubJets = cms.double(0.2),
    src = cms.InputTag("chs"),
    usePseudoXCone = cms.bool(True)
)


process.xconeCHS4jets08 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(4),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.8),
    RSubJets = cms.double(0.4),
    src = cms.InputTag("chs"),
    usePseudoXCone = cms.bool(True)
)


process.xconePUPPI2jets04 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.4),
    RSubJets = cms.double(0.2),
    doRekey = cms.bool(True),
    rekeyCandidateSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("puppi"),
    usePseudoXCone = cms.bool(True)
)


process.xconePUPPI2jets08 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.8),
    RSubJets = cms.double(0.4),
    doRekey = cms.bool(True),
    rekeyCandidateSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("puppi"),
    usePseudoXCone = cms.bool(True)
)


process.xconePUPPI3jets04 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(3),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.4),
    RSubJets = cms.double(0.2),
    doRekey = cms.bool(True),
    rekeyCandidateSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("puppi"),
    usePseudoXCone = cms.bool(True)
)


process.xconePUPPI3jets08 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(3),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.8),
    RSubJets = cms.double(0.4),
    doRekey = cms.bool(True),
    rekeyCandidateSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("puppi"),
    usePseudoXCone = cms.bool(True)
)


process.xconePUPPI4jets04 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(4),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.4),
    RSubJets = cms.double(0.2),
    doRekey = cms.bool(True),
    rekeyCandidateSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("puppi"),
    usePseudoXCone = cms.bool(True)
)


process.xconePUPPI4jets08 = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(4),
    NSubJets = cms.uint32(1),
    RJets = cms.double(0.8),
    RSubJets = cms.double(0.4),
    doRekey = cms.bool(True),
    rekeyCandidateSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("puppi"),
    usePseudoXCone = cms.bool(True)
)


process.xconePuppi = cms.EDProducer("XConeProducer",
    BetaJets = cms.double(2.0),
    BetaSubJets = cms.double(2.0),
    NJets = cms.uint32(2),
    NSubJets = cms.uint32(3),
    RJets = cms.double(1.2),
    RSubJets = cms.double(0.4),
    doRekey = cms.bool(True),
    printWarning = cms.bool(False),
    rekeyCandidateSrc = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("puppi"),
    usePseudoXCone = cms.bool(True)
)


process.ElectronPhotonGenParticles = cms.EDFilter("CandPtrSelector",
    cut = cms.string('(abs(pdgId) == 11) || (abs(pdgId) == 22 && numberOfMothers()==1 && abs(mother().pdgId()) == 11)'),
    src = cms.InputTag("packedGenParticles")
)


process.MuonPhotonGenParticles = cms.EDFilter("CandPtrSelector",
    cut = cms.string('(abs(pdgId) == 13) || (abs(pdgId) == 22 && numberOfMothers()==1 && abs(mother().pdgId()) == 13)'),
    src = cms.InputTag("packedGenParticles")
)


process.MyNtuple = cms.EDFilter("NtupleWriter",
    GenHOTVR_sources = cms.VInputTag(cms.InputTag("hotvrGen")),
    GenTopJets = cms.VPSet(
        cms.PSet(
            ecf_beta1_source = cms.string('ECFNbeta1Ak8SoftDropGen'),
            ecf_beta2_source = cms.string('ECFNbeta2Ak8SoftDropGen'),
            gentopjet_source = cms.string('genjetsAk8SubstructureSoftDrop'),
            njettiness_source = cms.string('NjettinessAk8SoftDropGen'),
            subjet_source = cms.string('ak8GenJetsSoftDrop'),
            substructure_variables_source = cms.string('ak8GenJetsSoftDropforsub')
        ), 
        cms.PSet(
            ecf_beta1_source = cms.string(''),
            ecf_beta2_source = cms.string(''),
            gentopjet_source = cms.string('genjetsAk8Substructure'),
            njettiness_source = cms.string('NjettinessAk8Gen'),
            subjet_source = cms.string(''),
            substructure_variables_source = cms.string('ak8GenJetsFat')
        )
    ),
    GenXCone_dijet_sources = cms.VInputTag(
        cms.InputTag("genXCone2jets04"), cms.InputTag("genXCone3jets04"), cms.InputTag("genXCone4jets04"), cms.InputTag("genXCone2jets08"), cms.InputTag("genXCone3jets08"), 
        cms.InputTag("genXCone4jets08")
    ),
    GenXCone_sources = cms.VInputTag(cms.InputTag("genXCone33TopJets")),
    HOTVR_sources = cms.VInputTag(cms.InputTag("hotvrPuppi")),
    TopJets = cms.VPSet(
        cms.PSet(
            ecf_beta1_source = cms.string('ECFNbeta1Ak8SoftDropCHS'),
            ecf_beta2_source = cms.string('ECFNbeta2Ak8SoftDropCHS'),
            higgstag_name = cms.string('pfBoostedDoubleSecondaryVertexAK8BJetTags'),
            higgstag_source = cms.string('patJetsAk8CHSJetsFat'),
            higgstaginfo_source = cms.string('pfBoostedDoubleSVTagInfosCHS'),
            njettiness_groomed_source = cms.string('NjettinessAk8SoftDropCHS'),
            njettiness_source = cms.string('NjettinessAk8CHS'),
            softdropmass_source = cms.string('patJetsAk8CHSJetsSoftDropPacked'),
            subjet_source = cms.string('SoftDropCHS'),
            substructure_groomed_variables_source = cms.string('ak8CHSJetsSoftDropforsub'),
            substructure_variables_source = cms.string('ak8CHSJetsFat'),
            topjet_source = cms.string('jetsAk8CHSSubstructure')
        ), 
        cms.PSet(
            ecf_beta1_source = cms.string('ECFNbeta1Ak8SoftDropPuppi'),
            ecf_beta2_source = cms.string('ECFNbeta2Ak8SoftDropPuppi'),
            higgstag_name = cms.string('pfBoostedDoubleSecondaryVertexAK8BJetTags'),
            higgstag_source = cms.string('patJetsAk8PuppiJetsFat'),
            higgstaginfo_source = cms.string('pfBoostedDoubleSVTagInfosPuppi'),
            njettiness_groomed_source = cms.string('NjettinessAk8SoftDropPuppi'),
            njettiness_source = cms.string('NjettinessAk8Puppi'),
            softdropmass_source = cms.string('patJetsAk8PuppiJetsSoftDropPacked'),
            subjet_source = cms.string('SoftDropPuppi'),
            substructure_groomed_variables_source = cms.string('ak8PuppiJetsSoftDropforsub'),
            substructure_variables_source = cms.string('ak8PuppiJetsFat'),
            topjet_source = cms.string('jetsAk8PuppiSubstructure')
        )
    ),
    XCone_dijet_sources = cms.VInputTag(
        cms.InputTag("xconeCHS2jets04"), cms.InputTag("xconeCHS3jets04"), cms.InputTag("xconeCHS4jets04"), cms.InputTag("xconeCHS2jets08"), cms.InputTag("xconeCHS3jets08"), 
        cms.InputTag("xconeCHS4jets08"), cms.InputTag("xconePUPPI2jets04"), cms.InputTag("xconePUPPI3jets04"), cms.InputTag("xconePUPPI4jets04"), cms.InputTag("xconePUPPI2jets08"), 
        cms.InputTag("xconePUPPI3jets08"), cms.InputTag("xconePUPPI4jets08")
    ),
    XCone_sources = cms.VInputTag(cms.InputTag("xconePuppi"), cms.InputTag("xconeCHS")),
    compressionAlgorithm = cms.string('LZMA'),
    compressionLevel = cms.int32(9),
    doAllPFParticles = cms.bool(False),
    doEcalBadCalib = cms.bool(False),
    doElectrons = cms.bool(True),
    doGenHOTVR = cms.bool(True),
    doGenInfo = cms.bool(True),
    doGenJetConstituentsMinJetPt = cms.double(-1),
    doGenJetConstituentsNjets = cms.uint32(0),
    doGenJets = cms.bool(True),
    doGenMET = cms.bool(True),
    doGenTopJetConstituentsMinJetPt = cms.double(-1),
    doGenTopJetConstituentsNjets = cms.uint32(0),
    doGenTopJets = cms.bool(True),
    doGenXCone = cms.bool(True),
    doGenXCone_dijet = cms.bool(False),
    doGenhotvrJetConstituentsMinJetPt = cms.double(-1),
    doGenhotvrJetConstituentsNjets = cms.uint32(0),
    doGenxconeDijetJetConstituentsMinJetPt = cms.double(-1),
    doGenxconeDijetJetConstituentsNjets = cms.uint32(0),
    doGenxconeJetConstituentsMinJetPt = cms.double(-1),
    doGenxconeJetConstituentsNjets = cms.uint32(0),
    doHOTVR = cms.bool(True),
    doJets = cms.bool(True),
    doL1TriggerObjects = cms.bool(False),
    doMET = cms.bool(True),
    doMuons = cms.bool(True),
    doPFJetConstituentsMinJetPt = cms.double(-1),
    doPFJetConstituentsNjets = cms.uint32(0),
    doPFTopJetConstituentsMinJetPt = cms.double(-1),
    doPFTopJetConstituentsNjets = cms.uint32(0),
    doPFhotvrJetConstituentsMinJetPt = cms.double(-1),
    doPFhotvrJetConstituentsNjets = cms.uint32(0),
    doPFxconeDijetJetConstituentsMinJetPt = cms.double(-1),
    doPFxconeDijetJetConstituentsNjets = cms.uint32(0),
    doPFxconeJetConstituentsMinJetPt = cms.double(-1),
    doPFxconeJetConstituentsNjets = cms.uint32(0),
    doPV = cms.bool(True),
    doPhotons = cms.bool(True),
    doPrefire = cms.bool(True),
    doRho = cms.untracked.bool(True),
    doStableGenParticles = cms.bool(False),
    doTaus = cms.bool(False),
    doTopJets = cms.bool(True),
    doTrigger = cms.bool(True),
    doXCone = cms.bool(True),
    doXCone_dijet = cms.bool(False),
    ecalBadCalib_source = cms.InputTag("ecalBadCalibReducedMINIAODFilter"),
    electron_IDtags = cms.vstring(
        'cutBasedElectronID-Summer16-80X-V1-veto', 
        'cutBasedElectronID-Summer16-80X-V1-loose', 
        'cutBasedElectronID-Summer16-80X-V1-medium', 
        'cutBasedElectronID-Summer16-80X-V1-tight', 
        'mvaEleID-Spring16-GeneralPurpose-V1-wp90', 
        'mvaEleID-Spring16-GeneralPurpose-V1-wp80', 
        'cutBasedElectronID-Fall17-94X-V2-veto', 
        'cutBasedElectronID-Fall17-94X-V2-loose', 
        'cutBasedElectronID-Fall17-94X-V2-medium', 
        'cutBasedElectronID-Fall17-94X-V2-tight', 
        'heepElectronID-HEEPV70', 
        'mvaEleID-Fall17-noIso-V2-wp90', 
        'mvaEleID-Fall17-noIso-V2-wp80', 
        'mvaEleID-Fall17-noIso-V2-wpLoose', 
        'mvaEleID-Fall17-iso-V2-wp90', 
        'mvaEleID-Fall17-iso-V2-wp80', 
        'mvaEleID-Fall17-iso-V2-wpLoose'
    ),
    electron_source = cms.InputTag("slimmedElectronsUSER"),
    extra_trigger_bits = cms.VInputTag(),
    fileName = cms.string('Ntuple.root'),
    genjet_etamax = cms.double(5.0),
    genjet_ptmin = cms.double(10.0),
    genjet_sources = cms.vstring(
        'slimmedGenJets', 
        'slimmedGenJetsAK8'
    ),
    genmet_sources = cms.vstring('slimmedMETs'),
    genparticle_source = cms.InputTag("prunedPrunedGenParticles"),
    gentopjet_etamax = cms.double(5.0),
    gentopjet_ptmin = cms.double(150.0),
    jet_etamax = cms.double(999.0),
    jet_ptmin = cms.double(10.0),
    jet_sources = cms.vstring(
        'jetsAk4CHS', 
        'jetsAk4Puppi', 
        'jetsAk8CHS', 
        'jetsAk8Puppi'
    ),
    l1EGSrc = cms.InputTag("caloStage2Digis","EGamma"),
    l1EtSumSrc = cms.InputTag("caloStage2Digis","EtSum"),
    l1GtSrc = cms.InputTag("gtStage2Digis"),
    l1JetSrc = cms.InputTag("caloStage2Digis","Jet"),
    l1MuonSrc = cms.InputTag("gmtStage2Digis","Muon"),
    l1TauSrc = cms.InputTag("caloStage2Digis","Tau"),
    met_sources = cms.vstring(
        'slimmedMETs', 
        'slimmedMETsPuppi'
    ),
    metfilter_bits = cms.InputTag("TriggerResults","","PAT"),
    muon_sources = cms.vstring('slimmedMuonsUSER'),
    pf_collection_source = cms.InputTag("packedPFCandidates"),
    photon_IDtags = cms.vstring(
        'cutBasedPhotonID-Spring16-V2p2-loose', 
        'cutBasedPhotonID-Spring16-V2p2-medium', 
        'cutBasedPhotonID-Spring16-V2p2-tight', 
        'mvaPhoID-Spring16-nonTrig-V1-wp90', 
        'mvaPhoID-Spring16-nonTrig-V1-wp80', 
        'cutBasedPhotonID-Fall17-94X-V2-loose', 
        'cutBasedPhotonID-Fall17-94X-V2-medium', 
        'cutBasedPhotonID-Fall17-94X-V2-tight', 
        'mvaPhoID-RunIIFall17-v2-wp80', 
        'mvaPhoID-RunIIFall17-v2-wp90'
    ),
    photon_sources = cms.InputTag("slimmedPhotonsUSER"),
    prefire_source = cms.string('prefiringweight'),
    pv_sources = cms.vstring('offlineSlimmedPrimaryVertices'),
    rho_source = cms.InputTag("fixedGridRhoFastjetAll"),
    save_lepton_keys = cms.bool(True),
    save_photon_keys = cms.bool(True),
    stablegenparticle_source = cms.InputTag("packedGenParticlesForJetsNoNu"),
    tau_etamax = cms.double(999.0),
    tau_ptmin = cms.double(0.0),
    tau_sources = cms.vstring('slimmedTaus'),
    topjet_etamax = cms.double(5.0),
    topjet_ptmin = cms.double(150.0),
    triggerObjects_sources = cms.vstring(),
    trigger_bits = cms.InputTag("TriggerResults","","HLT"),
    trigger_objects = cms.InputTag("slimmedPatTrigger"),
    trigger_prefixes = cms.vstring(
        'HLT_', 
        'Flag_'
    ),
    year = cms.string('2018')
)


process.chs = cms.EDFilter("CandPtrSelector",
    cut = cms.string('fromPV(0) > 0'),
    src = cms.InputTag("packedPFCandidates")
)


process.packedGenParticlesForJetsNoNu = cms.EDFilter("CandPtrSelector",
    cut = cms.string('abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16'),
    src = cms.InputTag("packedGenParticles")
)


process.pfAllChargedHadrons = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211, 
        2212, -2212
    ),
    src = cms.InputTag("pfNoPileUp")
)


process.pfAllChargedParticles = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13
    ),
    src = cms.InputTag("pfNoPileUp")
)


process.pfAllNeutralHadrons = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(111, 130, 310, 2112),
    src = cms.InputTag("pfNoPileUp")
)


process.pfAllPhotons = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(22),
    src = cms.InputTag("pfNoPileUp")
)


process.pfPileUpAllChargedParticles = cms.EDFilter("PFCandidateFwdPtrCollectionPdgIdFilter",
    makeClones = cms.bool(True),
    pdgId = cms.vint32(
        211, -211, 321, -321, 999211, 
        2212, -2212, 11, -11, 13, 
        -13
    ),
    src = cms.InputTag("pfPileUp")
)


process.selectedUpdatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsTransientCorrectedPackedPatJetsAk8CHSJetsNewDFTraining")
)


process.selectedUpdatedPatJetsPatJetsAk8CHSJetsSoftDropSubjets = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets")
)


process.selectedUpdatedPatJetsPatJetsAk8PuppiJetsSoftDropSubjets = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets")
)


process.selectedUpdatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining")
)


process.selectedUpdatedPatJetsRekeyPatJetsAK8PFPUPPINewDFTraining = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsTransientCorrectedRekeyPatJetsAK8PFPUPPINewDFTraining")
)


process.selectedUpdatedPatJetsSlimmedJetsNewDFTraining = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsTransientCorrectedSlimmedJetsNewDFTraining")
)


process.selectedUpdatedPatJetsSlimmedJetsPuppiNewDFTraining = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsTransientCorrectedSlimmedJetsPuppiNewDFTraining")
)


process.content = cms.EDAnalyzer("EventContentAnalyzer")


process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('miniaod.root'),
    outputCommands = cms.untracked.vstring(
        'drop *', 
        'drop *', 
        'keep *_slimmedPhotons_*_*', 
        'keep *_slimmedOOTPhotons_*_*', 
        'keep *_slimmedElectrons_*_*', 
        'keep *_slimmedMuons_*_*', 
        'keep recoTrackExtras_slimmedMuonTrackExtras_*_*', 
        'keep TrackingRecHitsOwned_slimmedMuonTrackExtras_*_*', 
        'keep SiPixelClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*', 
        'keep SiStripClusteredmNewDetSetVector_slimmedMuonTrackExtras_*_*', 
        'keep *_slimmedTaus_*_*', 
        'keep *_slimmedTausBoosted_*_*', 
        'keep *_slimmedCaloJets_*_*', 
        'keep *_slimmedJets_*_*', 
        'drop recoBaseTagInfosOwned_slimmedJets_*_*', 
        'keep *_slimmedJetsAK8_*_*', 
        'drop recoBaseTagInfosOwned_slimmedJetsAK8_*_*', 
        'keep *_slimmedJetsPuppi_*_*', 
        'keep *_slimmedMETs_*_*', 
        'keep *_slimmedMETsNoHF_*_*', 
        'keep *_slimmedMETsPuppi_*_*', 
        'keep *_slimmedSecondaryVertices_*_*', 
        'keep *_slimmedLambdaVertices_*_*', 
        'keep *_slimmedKshortVertices_*_*', 
        'keep *_slimmedJetsAK8PFPuppiSoftDropPacked_SubJets_*', 
        'keep recoPhotonCores_reducedEgamma_*_*', 
        'keep recoGsfElectronCores_reducedEgamma_*_*', 
        'keep recoConversions_reducedEgamma_*_*', 
        'keep recoSuperClusters_reducedEgamma_*_*', 
        'keep recoCaloClusters_reducedEgamma_*_*', 
        'keep EcalRecHitsSorted_reducedEgamma_*_*', 
        'keep recoGsfTracks_reducedEgamma_*_*', 
        'keep HBHERecHitsSorted_reducedEgamma_*_*', 
        'keep *_slimmedHcalRecHits_*_*', 
        'drop *_*_caloTowers_*', 
        'drop *_*_pfCandidates_*', 
        'drop *_*_genJets_*', 
        'keep *_offlineBeamSpot_*_*', 
        'keep *_offlineSlimmedPrimaryVertices_*_*', 
        'keep patPackedCandidates_packedPFCandidates_*_*', 
        'keep *_isolatedTracks_*_*', 
        'keep *_oniaPhotonCandidates_*_*', 
        'keep *_bunchSpacingProducer_*_*', 
        'keep double_fixedGridRhoAll__*', 
        'keep double_fixedGridRhoFastjetAll__*', 
        'keep double_fixedGridRhoFastjetAllTmp__*', 
        'keep double_fixedGridRhoFastjetAllCalo__*', 
        'keep double_fixedGridRhoFastjetCentral_*_*', 
        'keep double_fixedGridRhoFastjetCentralCalo__*', 
        'keep double_fixedGridRhoFastjetCentralChargedPileUp__*', 
        'keep double_fixedGridRhoFastjetCentralNeutral__*', 
        'keep *_slimmedPatTrigger_*_*', 
        'keep patPackedTriggerPrescales_patTrigger__*', 
        'keep patPackedTriggerPrescales_patTrigger_l1max_*', 
        'keep patPackedTriggerPrescales_patTrigger_l1min_*', 
        'keep *_l1extraParticles_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep GlobalExtBlkBXVector_simGtExtUnprefireable_*_*', 
        'keep *_gtStage2Digis__*', 
        'keep *_gmtStage2Digis_Muon_*', 
        'keep *_caloStage2Digis_Jet_*', 
        'keep *_caloStage2Digis_Tau_*', 
        'keep *_caloStage2Digis_EGamma_*', 
        'keep *_caloStage2Digis_EtSum_*', 
        'keep *_TriggerResults_*_HLT', 
        'keep *_TriggerResults_*_*', 
        'keep patPackedCandidates_lostTracks_*_*', 
        'keep HcalNoiseSummary_hcalnoise__*', 
        'keep recoCSCHaloData_CSCHaloData_*_*', 
        'keep recoBeamHaloSummary_BeamHaloSummary_*_*', 
        'keep LumiScalerss_scalersRawToDigi_*_*', 
        'keep CTPPSLocalTrackLites_ctppsLocalTrackLiteProducer_*_*', 
        'keep recoForwardProtons_ctppsProtons_*_*', 
        'keep recoTracks_displacedStandAloneMuons__*', 
        'keep *_prefiringweight_*_*', 
        'keep *_packedPFCandidates_hcalDepthEnergyFractions_*', 
        'keep patPackedGenParticles_packedGenParticles_*_*', 
        'keep recoGenParticles_prunedGenParticles_*_*', 
        'keep *_packedPFCandidateToGenAssociation_*_*', 
        'keep *_lostTracksToGenAssociation_*_*', 
        'keep LHEEventProduct_*_*_*', 
        'keep GenFilterInfo_*_*_*', 
        'keep GenLumiInfoHeader_generator_*_*', 
        'keep GenLumiInfoProduct_*_*_*', 
        'keep GenEventInfoProduct_generator_*_*', 
        'keep recoGenParticles_genPUProtons_*_*', 
        'keep *_slimmedGenJetsFlavourInfos_*_*', 
        'keep *_slimmedGenJets__*', 
        'keep *_slimmedGenJetsAK8__*', 
        'keep *_slimmedGenJetsAK8SoftDropSubJets__*', 
        'keep *_genMetTrue_*_*', 
        'keep LHERunInfoProduct_*_*_*', 
        'keep GenRunInfoProduct_*_*_*', 
        'keep *_genParticles_xyz0_*', 
        'keep *_genParticles_t0_*', 
        'keep PileupSummaryInfos_slimmedAddPileupInfo_*_*', 
        'keep L1GtTriggerMenuLite_l1GtTriggerMenuLite__*', 
        'keep *_patJetsAk8CHS*_*_*', 
        'keep *_patJetsAk8Puppi*_*_*', 
        'keep *_patJetsCa15CHS*_*_*', 
        'keep *_NjettinessAk8CHS_*_*', 
        'keep *_NjettinessAk8Puppi_*_*', 
        'keep *_NjettinessCa15CHS_*_*', 
        'keep *_NjettinessCa15SoftDropCHS_*_*', 
        'keep *_patJetsAk8CHSJetsSoftDropPacked_*_*', 
        'keep *_patJetsAk8CHSJetsSoftDropSubjets_*_*', 
        'keep *_patJetsAk8PuppiJetsSoftDropPacked_*_*', 
        'keep *_patJetsAk8PuppiJetsSoftDropSubjets_*_*', 
        'keep *_patJetsCa15CHSJetsSoftDropPacked_*_*', 
        'keep *_patJetsCa15CHSJetsSoftDropSubjets_*_*', 
        'keep *_patJetsAk8CHSJetsPrunedPacked_*_*', 
        'keep *_patJetsAk8CHSJetsPrunedSubjets_*_*', 
        'keep *_prunedPrunedGenParticles_*_*', 
        'keep *_egmGsfElectronIDs_*_*', 
        'drop *_selectedAK8PFPUPPI_tagInfos_*', 
        'drop *_selectedAK8PFCHS_tagInfos_*'
    )
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(250)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GEMGeometryESModule = cms.ESProducer("GEMGeometryESModule",
    useDDD = cms.bool(False)
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.candidateBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT_PhaseI_v1.weights.xml.gz')
)


process.candidateBoostedDoubleSecondaryVertexCA15Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_CA15_BDT_v3.weights.xml.gz')
)


process.candidateChargeBTagComputer = cms.ESProducer("CandidateChargeBTagESProducer",
    gbrForestLabel = cms.string(''),
    jetChargeExp = cms.double(0.8),
    svChargeExp = cms.double(0.5),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/ChargeBTag_4sep_2016.weights.xml.gz')
)


process.candidateCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    gbrForestLabel = cms.string('btag_CombinedMVAv2_BDT'),
    jetTagComputers = cms.vstring(
        'candidateJetProbabilityComputer', 
        'candidateJetBProbabilityComputer', 
        'candidateCombinedSecondaryVertexV2Computer', 
        'softPFMuonComputer', 
        'softPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.candidateCombinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'
    ),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexSoftLeptonCvsLComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonCvsLESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVRecoVertexNoSoftLeptonCvsL', 
        'CombinedSVPseudoVertexNoSoftLeptonCvsL', 
        'CombinedSVNoVertexNoSoftLeptonCvsL', 
        'CombinedSVRecoVertexSoftMuonCvsL', 
        'CombinedSVPseudoVertexSoftMuonCvsL', 
        'CombinedSVNoVertexSoftMuonCvsL', 
        'CombinedSVRecoVertexSoftElectronCvsL', 
        'CombinedSVPseudoVertexSoftElectronCvsL', 
        'CombinedSVNoVertexSoftElectronCvsL'
    ),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateGhostTrackComputer = cms.ESProducer("CandidateGhostTrackESProducer",
    calibrationRecords = cms.vstring(
        'GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    recordLabel = cms.string(''),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True)
)


process.candidateJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    gbrForestLabel = cms.string('btag_CombinedMVAv2_BDT'),
    jetTagComputers = cms.vstring(
        'candidateNegativeOnlyJetProbabilityComputer', 
        'candidateNegativeOnlyJetBProbabilityComputer', 
        'candidateNegativeCombinedSecondaryVertexV2Computer', 
        'negativeSoftPFMuonComputer', 
        'negativeSoftPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.candidateNegativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D2ndComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D3rdComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    gbrForestLabel = cms.string('btag_CombinedMVAv2_BDT'),
    jetTagComputers = cms.vstring(
        'candidatePositiveOnlyJetProbabilityComputer', 
        'candidatePositiveOnlyJetBProbabilityComputer', 
        'candidatePositiveCombinedSecondaryVertexV2Computer', 
        'negativeSoftPFMuonComputer', 
        'negativeSoftPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.candidatePositiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateSimpleSecondaryVertex2TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateSimpleSecondaryVertex3TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateTrackCounting3D2ndComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateTrackCounting3D3rdComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.charmTagsComputerCvsB = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(True),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_b_PhaseI.xml')
)


process.charmTagsComputerCvsL = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(True),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_udsg_PhaseI.xml')
)


process.charmTagsNegativeComputerCvsB = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(True),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(True),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(True),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(-2.0),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(True)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_b_PhaseI.xml')
)


process.charmTagsNegativeComputerCvsL = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(True),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(True),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(True),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(-2.0),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(True)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_udsg_PhaseI.xml')
)


process.charmTagsPositiveComputerCvsB = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(True),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_b_PhaseI.xml')
)


process.charmTagsPositiveComputerCvsL = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(True),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_udsg_PhaseI.xml')
)


process.combinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    jetTagComputers = cms.vstring(
        'jetProbabilityComputer', 
        'jetBProbabilityComputer', 
        'combinedSecondaryVertexV2Computer', 
        'softPFMuonComputer', 
        'softPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.combinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.doubleVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    minVertices = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.ghostTrackComputer = cms.ESProducer("GhostTrackESProducer",
    calibrationRecords = cms.vstring(
        'GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    recordLabel = cms.string(''),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True)
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(False),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.impactParameterMVAComputer = cms.ESProducer("GenericMVAJetTagESProducer",
    calibrationRecord = cms.string('ImpactParameterMVA'),
    recordLabel = cms.string(''),
    useCategories = cms.bool(False)
)


process.jetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.jetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    jetTagComputers = cms.vstring(
        'negativeOnlyJetProbabilityComputer', 
        'negativeOnlyJetBProbabilityComputer', 
        'negativeCombinedSecondaryVertexV2Computer', 
        'negativeSoftPFMuonComputer', 
        'negativeSoftPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.negativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.negativeOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.negativeSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.negativeTrackCounting3D2ndComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.negativeTrackCounting3D3rdComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.positiveCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    jetTagComputers = cms.vstring(
        'positiveOnlyJetProbabilityComputer', 
        'positiveOnlyJetBProbabilityComputer', 
        'positiveCombinedSecondaryVertexV2Computer', 
        'positiveSoftPFMuonComputer', 
        'positiveSoftPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.positiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.positiveOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.positiveSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    siPixelQualityLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.simpleSecondaryVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.simpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.softPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.softPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackCounting3D2ndComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackCounting3D3rdComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.BTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('102X_upgrade2018_realistic_v15'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(100.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(True),
    useHFUpgrade = cms.bool(True),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(False),
    useLayer0Weight = cms.bool(True)
)


process.prefer("es_hardcode")

process.egmPhotonIsolationMiniAODTask = cms.Task(process.egmPhotonIsolation)


process.egammaUpdatorTask = cms.Task(process.egmPhotonIsolationMiniAODTask, process.heepIDVarValueMaps, process.photonIDValueMapProducer, process.updatedElectrons, process.updatedPhotons)


process.egmGsfElectronIDTask = cms.Task(process.egmGsfElectronIDs, process.electronMVAValueMapProducer)


process.patAlgosToolsTask = cms.Task(process.patJetCorrFactorsAK8PFCHS, process.patJetCorrFactorsAK8PFPUPPI, process.patJetCorrFactorsAk8CHSJetsFat, process.patJetCorrFactorsAk8CHSJetsSoftDrop, process.patJetCorrFactorsAk8CHSJetsSoftDropSubjets, process.patJetCorrFactorsAk8PuppiJetsFat, process.patJetCorrFactorsAk8PuppiJetsSoftDrop, process.patJetCorrFactorsAk8PuppiJetsSoftDropSubjets, process.patJetCorrFactorsPackedPatJetsAk8CHSJetsNewDFTraining, process.patJetCorrFactorsPatJetsAk8CHSJetsSoftDropSubjets, process.patJetCorrFactorsPatJetsAk8PuppiJetsSoftDropSubjets, process.patJetCorrFactorsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.patJetCorrFactorsRekeyPatJetsAK8PFPUPPINewDFTraining, process.patJetCorrFactorsSlimmedJetsNewDFTraining, process.patJetCorrFactorsSlimmedJetsPuppiNewDFTraining, process.patJetCorrFactorsTransientCorrectedPackedPatJetsAk8CHSJetsNewDFTraining, process.patJetCorrFactorsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets, process.patJetCorrFactorsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets, process.patJetCorrFactorsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.patJetCorrFactorsTransientCorrectedRekeyPatJetsAK8PFPUPPINewDFTraining, process.patJetCorrFactorsTransientCorrectedSlimmedJetsNewDFTraining, process.patJetCorrFactorsTransientCorrectedSlimmedJetsPuppiNewDFTraining, process.patJetFlavourAssociationAK8PFCHS, process.patJetFlavourAssociationAK8PFPUPPI, process.patJetFlavourAssociationAk8CHSJetsFat, process.patJetFlavourAssociationAk8CHSJetsSoftDrop, process.patJetFlavourAssociationAk8CHSJetsSoftDropSubjets, process.patJetFlavourAssociationAk8PuppiJetsFat, process.patJetFlavourAssociationAk8PuppiJetsSoftDrop, process.patJetFlavourAssociationAk8PuppiJetsSoftDropSubjets, process.patJetFlavourAssociationLegacyAK8PFCHS, process.patJetFlavourAssociationLegacyAK8PFPUPPI, process.patJetFlavourAssociationLegacyAk8CHSJetsFat, process.patJetFlavourAssociationLegacyAk8CHSJetsSoftDrop, process.patJetFlavourAssociationLegacyAk8CHSJetsSoftDropSubjets, process.patJetFlavourAssociationLegacyAk8PuppiJetsFat, process.patJetFlavourAssociationLegacyAk8PuppiJetsSoftDrop, process.patJetFlavourAssociationLegacyAk8PuppiJetsSoftDropSubjets, process.patJetGenJetMatchAK8PFCHS, process.patJetGenJetMatchAK8PFPUPPI, process.patJetGenJetMatchAk8CHSJetsFat, process.patJetGenJetMatchAk8CHSJetsSoftDrop, process.patJetGenJetMatchAk8CHSJetsSoftDropSubjets, process.patJetGenJetMatchAk8PuppiJetsFat, process.patJetGenJetMatchAk8PuppiJetsSoftDrop, process.patJetGenJetMatchAk8PuppiJetsSoftDropSubjets, process.patJetPartonAssociationLegacyAK8PFCHS, process.patJetPartonAssociationLegacyAK8PFPUPPI, process.patJetPartonAssociationLegacyAk8CHSJetsFat, process.patJetPartonAssociationLegacyAk8CHSJetsSoftDrop, process.patJetPartonAssociationLegacyAk8CHSJetsSoftDropSubjets, process.patJetPartonAssociationLegacyAk8PuppiJetsFat, process.patJetPartonAssociationLegacyAk8PuppiJetsSoftDrop, process.patJetPartonAssociationLegacyAk8PuppiJetsSoftDropSubjets, process.patJetPartonMatchAK8PFCHS, process.patJetPartonMatchAK8PFPUPPI, process.patJetPartonMatchAk8CHSJetsFat, process.patJetPartonMatchAk8CHSJetsSoftDrop, process.patJetPartonMatchAk8CHSJetsSoftDropSubjets, process.patJetPartonMatchAk8PuppiJetsFat, process.patJetPartonMatchAk8PuppiJetsSoftDrop, process.patJetPartonMatchAk8PuppiJetsSoftDropSubjets, process.patJetPartons, process.patJetPartonsLegacy, process.patJetsAK8PFPUPPI, process.patJetsAk8CHSJetsFat, process.patJetsAk8CHSJetsSoftDrop, process.patJetsAk8CHSJetsSoftDropSubjets, process.patJetsAk8PuppiJetsFat, process.patJetsAk8PuppiJetsSoftDrop, process.patJetsAk8PuppiJetsSoftDropSubjets, process.pfBoostedDoubleSVAK8TagInfosAk8CHSJetsFat, process.pfBoostedDoubleSVAK8TagInfosAk8CHSJetsSoftDrop, process.pfBoostedDoubleSVAK8TagInfosAk8CHSJetsSoftDropSubjets, process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsFat, process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDrop, process.pfBoostedDoubleSVAK8TagInfosAk8PuppiJetsSoftDropSubjets, process.pfBoostedDoubleSVAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfBoostedDoubleSVAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfBoostedDoubleSVCA15TagInfosAk8CHSJetsFat, process.pfBoostedDoubleSVCA15TagInfosAk8CHSJetsSoftDrop, process.pfBoostedDoubleSVCA15TagInfosAk8CHSJetsSoftDropSubjets, process.pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsFat, process.pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsSoftDrop, process.pfBoostedDoubleSVCA15TagInfosAk8PuppiJetsSoftDropSubjets, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8CHSJetsFat, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8CHSJetsSoftDrop, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8CHSJetsSoftDropSubjets, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsFat, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDrop, process.pfBoostedDoubleSecondaryVertexAK8BJetTagsAk8PuppiJetsSoftDropSubjets, process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8CHSJetsFat, process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8CHSJetsSoftDrop, process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8CHSJetsSoftDropSubjets, process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8PuppiJetsFat, process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8PuppiJetsSoftDrop, process.pfBoostedDoubleSecondaryVertexCA15BJetTagsAk8PuppiJetsSoftDropSubjets, process.pfDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepBoostedJetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepBoostedJetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepCSVJetTagsAk8CHSJetsFat, process.pfDeepCSVJetTagsAk8CHSJetsSoftDrop, process.pfDeepCSVJetTagsAk8CHSJetsSoftDropSubjets, process.pfDeepCSVJetTagsAk8PuppiJetsFat, process.pfDeepCSVJetTagsAk8PuppiJetsSoftDrop, process.pfDeepCSVJetTagsAk8PuppiJetsSoftDropSubjets, process.pfDeepCSVTagInfosAk8CHSJetsFat, process.pfDeepCSVTagInfosAk8CHSJetsSoftDrop, process.pfDeepCSVTagInfosAk8CHSJetsSoftDropSubjets, process.pfDeepCSVTagInfosAk8PuppiJetsFat, process.pfDeepCSVTagInfosAk8PuppiJetsSoftDrop, process.pfDeepCSVTagInfosAk8PuppiJetsSoftDropSubjets, process.pfDeepCSVTagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepCSVTagInfosPatJetsAk8CHSJetsSoftDropSubjets, process.pfDeepCSVTagInfosPatJetsAk8PuppiJetsSoftDropSubjets, process.pfDeepCSVTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepCSVTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining, process.pfDeepCSVTagInfosSlimmedJetsNewDFTraining, process.pfDeepCSVTagInfosSlimmedJetsPuppiNewDFTraining, process.pfDeepDoubleBvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepDoubleBvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepDoubleCvBJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepDoubleCvBJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepDoubleCvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepDoubleCvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepDoubleXTagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepDoubleXTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepFlavourJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepFlavourJetTagsPatJetsAk8CHSJetsSoftDropSubjets, process.pfDeepFlavourJetTagsPatJetsAk8PuppiJetsSoftDropSubjets, process.pfDeepFlavourJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepFlavourJetTagsRekeyPatJetsAK8PFPUPPINewDFTraining, process.pfDeepFlavourJetTagsSlimmedJetsNewDFTraining, process.pfDeepFlavourJetTagsSlimmedJetsPuppiNewDFTraining, process.pfDeepFlavourTagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfDeepFlavourTagInfosPatJetsAk8CHSJetsSoftDropSubjets, process.pfDeepFlavourTagInfosPatJetsAk8PuppiJetsSoftDropSubjets, process.pfDeepFlavourTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfDeepFlavourTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining, process.pfDeepFlavourTagInfosSlimmedJetsNewDFTraining, process.pfDeepFlavourTagInfosSlimmedJetsPuppiNewDFTraining, process.pfImpactParameterAK8TagInfosAk8CHSJetsFat, process.pfImpactParameterAK8TagInfosAk8CHSJetsSoftDrop, process.pfImpactParameterAK8TagInfosAk8CHSJetsSoftDropSubjets, process.pfImpactParameterAK8TagInfosAk8PuppiJetsFat, process.pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDrop, process.pfImpactParameterAK8TagInfosAk8PuppiJetsSoftDropSubjets, process.pfImpactParameterAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfImpactParameterAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfImpactParameterCA15TagInfosAk8CHSJetsFat, process.pfImpactParameterCA15TagInfosAk8CHSJetsSoftDrop, process.pfImpactParameterCA15TagInfosAk8CHSJetsSoftDropSubjets, process.pfImpactParameterCA15TagInfosAk8PuppiJetsFat, process.pfImpactParameterCA15TagInfosAk8PuppiJetsSoftDrop, process.pfImpactParameterCA15TagInfosAk8PuppiJetsSoftDropSubjets, process.pfImpactParameterTagInfosAk8CHSJetsFat, process.pfImpactParameterTagInfosAk8CHSJetsSoftDrop, process.pfImpactParameterTagInfosAk8CHSJetsSoftDropSubjets, process.pfImpactParameterTagInfosAk8PuppiJetsFat, process.pfImpactParameterTagInfosAk8PuppiJetsSoftDrop, process.pfImpactParameterTagInfosAk8PuppiJetsSoftDropSubjets, process.pfImpactParameterTagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfImpactParameterTagInfosPatJetsAk8CHSJetsSoftDropSubjets, process.pfImpactParameterTagInfosPatJetsAk8PuppiJetsSoftDropSubjets, process.pfImpactParameterTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfImpactParameterTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining, process.pfImpactParameterTagInfosSlimmedJetsNewDFTraining, process.pfImpactParameterTagInfosSlimmedJetsPuppiNewDFTraining, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsFat, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsSoftDrop, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8CHSJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsFat, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDrop, process.pfInclusiveSecondaryVertexFinderAK8TagInfosAk8PuppiJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderAK8TagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfInclusiveSecondaryVertexFinderAK8TagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsFat, process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsSoftDrop, process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8CHSJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsFat, process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsSoftDrop, process.pfInclusiveSecondaryVertexFinderCA15TagInfosAk8PuppiJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsFat, process.pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsSoftDrop, process.pfInclusiveSecondaryVertexFinderTagInfosAk8CHSJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsFat, process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDrop, process.pfInclusiveSecondaryVertexFinderTagInfosAk8PuppiJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderTagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfInclusiveSecondaryVertexFinderTagInfosPatJetsAk8CHSJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderTagInfosPatJetsAk8PuppiJetsSoftDropSubjets, process.pfInclusiveSecondaryVertexFinderTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfInclusiveSecondaryVertexFinderTagInfosRekeyPatJetsAK8PFPUPPINewDFTraining, process.pfInclusiveSecondaryVertexFinderTagInfosSlimmedJetsNewDFTraining, process.pfInclusiveSecondaryVertexFinderTagInfosSlimmedJetsPuppiNewDFTraining, process.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfMassDecorrelatedDeepBoostedDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfMassDecorrelatedDeepBoostedJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfMassDecorrelatedDeepBoostedJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfMassDecorrelatedParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfMassDecorrelatedParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfMassDecorrelatedParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfMassDecorrelatedParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfMassIndependentDeepDoubleBvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfMassIndependentDeepDoubleBvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfMassIndependentDeepDoubleCvBJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfMassIndependentDeepDoubleCvBJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfMassIndependentDeepDoubleCvLJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfMassIndependentDeepDoubleCvLJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfParticleNetDiscriminatorsJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfParticleNetDiscriminatorsJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfParticleNetJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfParticleNetJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfParticleNetMassRegressionJetTagsPackedPatJetsAk8CHSJetsNewDFTraining, process.pfParticleNetMassRegressionJetTagsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfParticleNetTagInfosPackedPatJetsAk8CHSJetsNewDFTraining, process.pfParticleNetTagInfosRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfSecondaryVertexTagInfosAk8CHSJetsFat, process.pfSecondaryVertexTagInfosAk8CHSJetsSoftDrop, process.pfSecondaryVertexTagInfosAk8CHSJetsSoftDropSubjets, process.pfSecondaryVertexTagInfosAk8PuppiJetsFat, process.pfSecondaryVertexTagInfosAk8PuppiJetsSoftDrop, process.pfSecondaryVertexTagInfosAk8PuppiJetsSoftDropSubjets, process.selectedUpdatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining, process.selectedUpdatedPatJetsPatJetsAk8CHSJetsSoftDropSubjets, process.selectedUpdatedPatJetsPatJetsAk8PuppiJetsSoftDropSubjets, process.selectedUpdatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.selectedUpdatedPatJetsRekeyPatJetsAK8PFPUPPINewDFTraining, process.selectedUpdatedPatJetsSlimmedJetsNewDFTraining, process.selectedUpdatedPatJetsSlimmedJetsPuppiNewDFTraining, process.softPFElectronsTagInfosAk8CHSJetsFat, process.softPFElectronsTagInfosAk8CHSJetsSoftDrop, process.softPFElectronsTagInfosAk8CHSJetsSoftDropSubjets, process.softPFElectronsTagInfosAk8PuppiJetsFat, process.softPFElectronsTagInfosAk8PuppiJetsSoftDrop, process.softPFElectronsTagInfosAk8PuppiJetsSoftDropSubjets, process.softPFMuonsTagInfosAk8CHSJetsFat, process.softPFMuonsTagInfosAk8CHSJetsSoftDrop, process.softPFMuonsTagInfosAk8CHSJetsSoftDropSubjets, process.softPFMuonsTagInfosAk8PuppiJetsFat, process.softPFMuonsTagInfosAk8PuppiJetsSoftDrop, process.softPFMuonsTagInfosAk8PuppiJetsSoftDropSubjets, process.updatedPatJetsPackedPatJetsAk8CHSJetsNewDFTraining, process.updatedPatJetsPatJetsAk8CHSJetsSoftDropSubjets, process.updatedPatJetsPatJetsAk8PuppiJetsSoftDropSubjets, process.updatedPatJetsRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.updatedPatJetsRekeyPatJetsAK8PFPUPPINewDFTraining, process.updatedPatJetsSlimmedJetsNewDFTraining, process.updatedPatJetsSlimmedJetsPuppiNewDFTraining, process.updatedPatJetsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets, process.updatedPatJetsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets)


process.egammaPostRecoPatUpdatorTask = cms.Task(process.slimmedElectrons)


process.pfNoPileUpTask = cms.Task(process.pfNoPileUp, process.pfPileUp)


process.egmPhotonIDTask = cms.Task(process.egmPhotonIDs, process.photonMVAValueMapProducer)


process.egammaVIDTask = cms.Task(process.egmGsfElectronIDTask, process.egmPhotonIDTask)


process.egammaScaleSmearTask = cms.Task(process.calibratedPatElectrons, process.calibratedPatPhotons)


process.egammaUpdatorSeq = cms.Sequence(process.egammaUpdatorTask)


process.pfDeltaBetaWeightingSequence = cms.Sequence(process.pfWeightedPhotons+process.pfWeightedNeutralHadrons)


process.pfSelectorsSequence = cms.Sequence(process.pfAllChargedParticles+process.pfAllChargedHadrons+process.pfAllNeutralHadrons+process.pfAllPhotons+process.pfPileUpAllChargedParticles)


process.muonPFMiniIsoSequencePFWGT = cms.Sequence(process.muPFMiniIsoDepositNHPFWGT+process.muPFMiniIsoDepositPhPFWGT+(process.muPFMiniIsoValueNHPFWGT+process.muPFMiniIsoValuePhPFWGT))


process.egmGsfElectronIDSequence = cms.Sequence(process.egmGsfElectronIDTask)


process.muonPFMiniIsoSequenceSTAND = cms.Sequence(process.muPFMiniIsoDepositCHSTAND+process.muPFMiniIsoDepositNHSTAND+process.muPFMiniIsoDepositPhSTAND+process.muPFMiniIsoDepositPUSTAND+(process.muPFMiniIsoValueCHSTAND+process.muPFMiniIsoValueNHSTAND+process.muPFMiniIsoValuePhSTAND+process.muPFMiniIsoValuePUSTAND))


process.egmPhotonIsolationMiniAODSequence = cms.Sequence(process.egmPhotonIsolationMiniAODTask)


process.egmPhotonIDSequence = cms.Sequence(process.egmPhotonIDTask)


process.egammaVIDSeq = cms.Sequence(process.egammaVIDTask)


process.egammaScaleSmearSeq = cms.Sequence(process.egammaScaleSmearTask)


process.egammaPostRecoPatUpdatorSeq = cms.Sequence(process.egammaPostRecoPatUpdatorTask)


process.elecPFMiniIsoSequencePFWGT = cms.Sequence(process.elPFMiniIsoDepositNHPFWGT+process.elPFMiniIsoDepositPhPFWGT+(process.elPFMiniIsoValueNHPFWGT+process.elPFMiniIsoValuePhPFWGT))


process.pfNoPileUpSequence = cms.Sequence(process.pfNoPileUpTask)


process.elecPFMiniIsoSequenceSTAND = cms.Sequence(process.elPFMiniIsoDepositCHSTAND+process.elPFMiniIsoDepositNHSTAND+process.elPFMiniIsoDepositPhSTAND+process.elPFMiniIsoDepositPUSTAND+(process.elPFMiniIsoValueCHSTAND+process.elPFMiniIsoValueNHSTAND+process.elPFMiniIsoValuePhSTAND+process.elPFMiniIsoValuePUSTAND))


process.pfCandidatesByTypeSequence = cms.Sequence(process.convertedPackedPFCandidates+process.convertedPackedPFCandidatePtrs+process.pfNoPileUpSequence+process.pfSelectorsSequence)


process.egammaPostRecoSeq = cms.Sequence(process.egammaUpdatorSeq+process.egammaScaleSmearSeq+process.egammaVIDSeq+process.egammaPostRecoPatUpdatorSeq)


process.p = cms.Path(process.prefiringweight+process.egammaPostRecoSeq+process.MyNtuple, cms.Task(process.ECFNbeta1Ak8SoftDropCHS, process.ECFNbeta1Ak8SoftDropGen, process.ECFNbeta1Ak8SoftDropPuppi, process.ECFNbeta2Ak8SoftDropCHS, process.ECFNbeta2Ak8SoftDropGen, process.ECFNbeta2Ak8SoftDropPuppi, process.ElectronPhotonGenParticles, process.MuonPhotonGenParticles, process.NjettinessAk8CHS, process.NjettinessAk8Gen, process.NjettinessAk8Puppi, process.NjettinessAk8SoftDropCHS, process.NjettinessAk8SoftDropGen, process.NjettinessAk8SoftDropPuppi, process.ak8CHSJets, process.ak8CHSJetsFat, process.ak8CHSJetsSoftDrop, process.ak8CHSJetsSoftDropforsub, process.ak8GenJetsFat, process.ak8GenJetsSoftDrop, process.ak8GenJetsSoftDropforsub, process.ak8PuppiJets, process.ak8PuppiJetsFat, process.ak8PuppiJetsSoftDrop, process.ak8PuppiJetsSoftDropforsub, process.chs, process.convertedPackedPFCandidatePtrs, process.convertedPackedPFCandidates, process.elPFMiniIsoDepositCHSTAND, process.elPFMiniIsoDepositNHPFWGT, process.elPFMiniIsoDepositNHSTAND, process.elPFMiniIsoDepositPUSTAND, process.elPFMiniIsoDepositPhPFWGT, process.elPFMiniIsoDepositPhSTAND, process.elPFMiniIsoValueCHSTAND, process.elPFMiniIsoValueNHPFWGT, process.elPFMiniIsoValueNHSTAND, process.elPFMiniIsoValuePUSTAND, process.elPFMiniIsoValuePhPFWGT, process.elPFMiniIsoValuePhSTAND, process.electronGenJets, process.electronMVATOP, process.electronMVAValueMapProducerv2, process.genXCone23TopJets, process.genXCone2jets04, process.genXCone2jets08, process.genXCone33TopJets, process.genXCone3jets04, process.genXCone3jets08, process.genXCone4jets04, process.genXCone4jets08, process.hotvrGen, process.hotvrPuppi, process.isoForEle, process.isoForMu, process.jetsAk4CHS, process.jetsAk4Puppi, process.jetsAk8CHS, process.jetsAk8CHSSubstructure, process.jetsAk8Puppi, process.jetsAk8PuppiSubstructure, process.muPFMiniIsoDepositCHSTAND, process.muPFMiniIsoDepositNHPFWGT, process.muPFMiniIsoDepositNHSTAND, process.muPFMiniIsoDepositPUSTAND, process.muPFMiniIsoDepositPhPFWGT, process.muPFMiniIsoDepositPhSTAND, process.muPFMiniIsoValueCHSTAND, process.muPFMiniIsoValueNHPFWGT, process.muPFMiniIsoValueNHSTAND, process.muPFMiniIsoValuePUSTAND, process.muPFMiniIsoValuePhPFWGT, process.muPFMiniIsoValuePhSTAND, process.muonGenJets, process.muonMVATOP, process.packedGenParticlesForJetsNoNu, process.packedPatJetsAk8CHSJets, process.patJetsAk8CHSJetsSoftDropPacked, process.patJetsAk8PuppiJetsSoftDropPacked, process.patPuppiJetSpecificProducerjetsAk4Puppi, process.patPuppiJetSpecificProducerjetsAk8Puppi, process.patPuppiJetSpecificProducerupdatedPatJetsTransientCorrectedRekeyPackedPatJetsAk8PuppiJetsNewDFTraining, process.pfAllChargedHadrons, process.pfAllChargedParticles, process.pfAllNeutralHadrons, process.pfAllPhotons, process.pfBoostedDoubleSVTagInfosCHS, process.pfBoostedDoubleSVTagInfosPuppi, process.pfNoPileUp, process.pfPileUp, process.pfPileUpAllChargedParticles, process.pfWeightedNeutralHadrons, process.pfWeightedPhotons, process.prefiringweight, process.prunedPrunedGenParticles, process.ptRatioRelForEle, process.ptRatioRelForMu, process.puppi, process.rekeyPackedPatJetsAk8PuppiJets, process.rekeyPatJetsAK8PFPUPPI, process.rekeyPatJetsAk8PuppiJetsFat, process.rekeyUpdatedPatJetsTransientCorrectedPatJetsAk8CHSJetsSoftDropSubjets, process.rekeyUpdatedPatJetsTransientCorrectedPatJetsAk8PuppiJetsSoftDropSubjets, process.slimmedElectronsData, process.slimmedElectronsUSER, process.slimmedElectronsWithUserData, process.slimmedMuonsData, process.slimmedMuonsUSER, process.slimmedMuonsWithUserData, process.slimmedPhotonsUSER, process.xconeCHS, process.xconeCHS2jets04, process.xconeCHS2jets08, process.xconeCHS3jets04, process.xconeCHS3jets08, process.xconeCHS4jets04, process.xconeCHS4jets08, process.xconePUPPI2jets04, process.xconePUPPI2jets08, process.xconePUPPI3jets04, process.xconePUPPI3jets08, process.xconePUPPI4jets04, process.xconePUPPI4jets08, process.xconePuppi), process.patAlgosToolsTask)


process.genjetsAk8Substructure = cms.EDAlias(
    ak8GenJetsFat = cms.VPSet(cms.PSet(
        type = cms.string('recoGenJets')
    ))
)

process.genjetsAk8SubstructureSoftDrop = cms.EDAlias(
    ak8GenJetsSoftDropforsub = cms.VPSet(cms.PSet(
        type = cms.string('recoGenJets')
    ))
)

