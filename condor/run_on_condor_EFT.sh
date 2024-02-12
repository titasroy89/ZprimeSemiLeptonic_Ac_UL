#!/bin/bash

# Display start date/time and node information
echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node

# Setup the CMS and GRID environment
source /cvmfs/grid.desy.de/etc/profile.d/grid-ui-env.sh
source /cvmfs/cms.cern.ch/cmsset_default.sh

pwd

# Go to the CMSSW environment directory
cd /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2
eval `scramv1 runtime -sh` # cmsenv is an alias not on the workers
echo $CMSSW_BASE "is the CMSSW we have on the local worker node"

pwd
export SCRAM_ARCH=slc7_amd64_gcc820
# scramv1 project CMSSW CMSSW_10_6_28 # cmsrel is an alias not on the workers

cd /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2

INPUT_FILE="$1"
OUTPUT_FILE="$2"

# Check if INPUT_FILE variable is provided
if [ -z "$INPUT_FILE" ]; then
    echo "Error: No input file provided."
    exit 1
fi

echo "Input files, $INPUT_FILE: "

pwd

cmsRun /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/core/python/ntuplewriter_mc_UL18_3.py inputFiles=file:$INPUT_FILE outputFile=$OUTPUT_FILE

echo "Job completed on $(date)"

