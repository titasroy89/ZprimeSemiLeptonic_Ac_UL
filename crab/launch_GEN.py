from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration

import imp, os, sys
from optparse import OptionParser
import re

cfgPath    = os.path.expandvars("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/crab/")
allConfigs = [ x.split(".")[0] for x in os.listdir( cfgPath ) if x.endswith(".py") ]

parser = OptionParser(usage="python launch.py [options] component1 [ component2 ...]", \
                          description="Launch heppy jobs with CRAB3. Components correspond to the variables defined in heppy_samples.py (their name attributes)")
parser.add_option("--production_label", dest="production_label",                                  default="heppy", help="production label")
parser.add_option("--remoteDir",        dest="remoteDir",                                         default="",      help="remote subdirectory")
parser.add_option("--unitsPerJob",      dest="unitsPerJob",      type=int,                        default=1,       help="Nr. of units (files) / crab job")
parser.add_option("--totalUnits",       dest="totalUnits",       type=int,                        default=None,    help="Total nr. of units (files)")
parser.add_option("--config",           dest="config",                     choices = allConfigs,                   help="Which config?")
parser.add_option("--publish",          action='store_true',                                      default=False,   help="Publish on dbs?")
parser.add_option("--dryrun",           action='store_true',                                      default=False,   help="Test script?")
parser.add_option("--gridpackDir",      dest="gridpackDir",                                       default=None,    help="gridpack directory for gen production")
parser.add_option("--gridpack",         dest="gridpack",                                          default=None,    help="gridpack name for gen production")
( options, args ) = parser.parse_args()

print "## Starting submission to crab for gridpack %s ##"%(options.gridpack)

# GEN production using gridpacks
# cfgFile      = os.path.join( cfgPath, "%s.py" % options.config )

# run in CMSSW_9_3_1
config = Configuration()

config.section_("General")
config.General.requestName = "tmp"
config.General.workArea = 'crab_' + options.production_label
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
# config.JobType.psetName = cfgFile
config.JobType.psetName = 'nanogen_cfg.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.allowUndistributedCMSSW = True
#config.JobType.numCores = 1
config.JobType.maxMemoryMB = 3500 #for genToReco

config.section_("Data")
config.Data.splitting = 'EventBased'

config.Data.unitsPerJob = options.unitsPerJob
config.Data.totalUnits  = options.totalUnits
config.Data.publication = options.publish
config.Data.publishDBS = 'phys03'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.section_("Site")
config.Site.storageSite = 'T2_DE_DESY'
#config.Site.whitelist = ['T2_*']

config.section_("User")

config.Data.outputDatasetTag     = options.production_label
config.General.requestName       = options.production_label
config.Data.outputPrimaryDataset = config.General.requestName # dataset name

if options.gridpack.startswith("root://"):
    if os.path.exists("myscript.sh"):
        os.remove("myscript.sh")
    with open("myscript.sh",'w') as f:
        #f.write( "xrdcp {gridpack} gridpack.tar.xz\ncmsRun -j FrameworkJobReport.xml -p PSet.py".format(gridpack=options.gridpack) )
        f.write( """sleep  $[ ( $RANDOM % 100 ) ]s
icnt=0
while [[ $icnt -lt 4 ]]; do
        xrdcp -t 30 {gridpack} gridpack.tar.xz
     if [[ $rc -eq 0 ]]; then
        break
     fi
     sleep 10

    icnt=$((icnt+1))
done
cmsRun -j FrameworkJobReport.xml -p PSet.py
""".format(gridpack=options.gridpack) )
    config.JobType.scriptExe = 'myscript.sh'
elif options.gridpack.startswith("https://"):
    if os.path.exists("myscript.sh"):
        os.remove("myscript.sh")
    with open("myscript.sh",'w') as f:
        #f.write( "xrdcp {gridpack} gridpack.tar.xz\ncmsRun -j FrameworkJobReport.xml -p PSet.py".format(gridpack=options.gridpack) )
        f.write( """sleep  $[ ( $RANDOM % 100 ) ]s
icnt=0
while [[ $icnt -lt 4 ]]; do
         curl -L  -o gridpack.tar.xz {gridpack} 
     if [[ $rc -eq 0 ]]; then
        break
     fi
     sleep 10

    icnt=$((icnt+1))
done
cmsRun -j FrameworkJobReport.xml -p PSet.py
""".format(gridpack=options.gridpack) )
    config.JobType.scriptExe = 'myscript.sh'
else:
    gridpackFile = os.path.expandvars( os.path.join( options.gridpackDir, options.gridpack ) )
    config.JobType.inputFiles        = [gridpackFile] if not gridpackFile.startswith('/cvmfs/') else []
    config.JobType.pyCfgParams = ['gridpack=../'+options.gridpack if not gridpackFile.startswith('/cvmfs/') else 'gridpack='+gridpackFile]

if options.dryrun:
    print "Processing %s" %( options.gridpack )
    print "## Dryrun, continue..."
    sys.exit(0)

crabCommand('submit', config=config)

