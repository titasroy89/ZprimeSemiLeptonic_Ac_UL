import FWCore.ParameterSet.Config as cms

process = cms.Process("LHEMttbarAnalysis")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)  # Adjust as needed
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer20UL17MiniAODv2/TTtoLNu2Q-1Jets-smeft_MTT-0to700_TuneCP5_13TeV_madgraphMLM-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/130000/6AB430F5-FBE6-3F47-8841-2179251E6432.root'
    )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('mttbar.root')
)

process.lheMttbarAnalyzer = cms.EDAnalyzer('LHEMttbarAnalyzer')

process.p = cms.Path(process.lheMttbarAnalyzer)
