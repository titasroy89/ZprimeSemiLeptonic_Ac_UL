# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/pythia_fragment.py --python_filename nanogen_cfg.py --eventcontent NANOAODGEN --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAOD --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=123 --fileout file:nanogen_123.root --conditions 106X_mcRun2_asymptotic_v13 --beamspot Realistic25ns13TeV2016Collision --step LHE,GEN,NANOGEN --geometry DB:Extended --era Run2_2016 --no_exec --mc -n 1000000
import os
import FWCore.ParameterSet.VarParsing as VarParsing

options = VarParsing.VarParsing ('standard')
options.register('gridpack',  '/nfs/dust/cms/user/beozek/EFT/CMSSW_10_6_26/src/EFT_gen_old/EFT_samples/scripts_plots_new_samples/input_files/CA/TT01j1lCA_HT500_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz',  VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string,  "Which Gridpack?")
options.register('outputDir', 'srm://dcache-se-cms.desy.de:8443/pnfs/desy.de/cms/tier2/store/user/beozek/', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string,  "Where to store the output root file?")
options.maxEvents=1000000  # maxEvents is a registered option. 

if not 'ipython' in VarParsing.sys.argv[0]: options.parseArguments()
else: print "No parsing of arguments!"

options.outputDir = os.path.expandvars( options.outputDir )

if not os.path.isdir(options.outputDir):
    os.makedirs(options.outputDir)

#options.gridpack  = os.path.expandvars( options.gridpack )
options.gridpack  = os.path.expandvars( options.gridpack )

import FWCore.ParameterSet.Config as cms

# from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANOGEN',eras.Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
# process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeV2016Collision_cfi')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2018Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('PhysicsTools.NanoAOD.nanogen_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/pythia_fragment.py nevts:1000000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODGENoutput = cms.OutputModule("NanoAODOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:nanogen_123.root'),
    outputCommands = process.NANOAODGENEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_v13', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'JetMatching:setMad = off', 
            'JetMatching:scheme = 1', 
            'JetMatching:merge = on', 
            'JetMatching:jetAlgorithm = 2', 
            'JetMatching:etaJetMax = 5.', 
            'JetMatching:coneRadius = 1.', 
            'JetMatching:slowJetPower = 1', 
            'JetMatching:qCut = 10.', 
            'JetMatching:nQmatch = 5', 
            'JetMatching:nJetMax = 1', 
            'JetMatching:doShowerKt = off'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118', 
            'SigmaTotal:mode = 0', 
            'SigmaTotal:sigmaEl = 21.89', 
            'SigmaTotal:sigmaTot = 100.309', 
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    # args = cms.vstring('/nfs/dust/cms/user/beozek/EFT/CMSSW_10_6_26/src/EFT_gen_old/EFT_samples/scripts_plots_new_samples/input_files/CA/TT01j1lCA_HT500_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz'),
    args = cms.vstring(options.gridpack),
    nEvents = cms.untracked.uint32(1000000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.nanoAOD_step = cms.Path(process.nanogenSequence)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODGENoutput_step = cms.EndPath(process.NANOAODGENoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.nanoAOD_step,process.endjob_step,process.NANOAODGENoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path).insert(0, process.generator)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nanogen_cff
from PhysicsTools.NanoAOD.nanogen_cff import customizeNanoGEN 

#call to customisation function customizeNanoGEN imported from PhysicsTools.NanoAOD.nanogen_cff
process = customizeNanoGEN(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=123
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
named_weights = [
"dummy # Name of first argument seems to be rwgt_1. Add dummy to fix it.",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_2p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_1p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_2p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_1p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_2p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_1p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_2p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_1p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_2p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_1p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_2p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_1p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_2p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_1p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_2p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_1p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_2p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_1p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_2p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_1p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_2p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_1p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_2p_ctj1_0p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_1p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_1p_ctj1_0p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_2p_cQu1_0p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_1p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_1p_cQu1_0p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_2p_cQd1_0p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_1p_cQd1_1p",
"ctGRe_0p_cQj18_0p_cQj38_0p_cQj11_0p_cjj31_0p_ctu8_0p_ctd8_0p_ctj8_0p_cQu8_0p_cQd8_0p_ctu1_0p_ctd1_0p_ctj1_0p_cQu1_0p_cQd1_2p",
]
process.genWeightsTable.namedWeightIDs = named_weights
process.genWeightsTable.namedWeightLabels = named_weights
