#!/bin/bash

echo "Starting job on " `date` #Date/time of start of job
echo "Running on: `uname -a`" #Condor job is running on this node

source /cvmfs/grid.desy.de/etc/profile.d/grid-ui-env.sh

# xrdcp -s root://dcache-cms-xrootd.desy.de//nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/CMSSW_10_6_28.tar.gz .

xrdcp -s /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/CMSSW_10_6_28.tar.gz .

source /cvmfs/cms.cern.ch/cmsset_default.sh

pwd

tar -zxvf CMSSW_10_6_28.tar.gz
rm CMSSW_10_6_4.tgz

cd /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2

scramv1 b ProjectRename # this handles linking the already compiled code - do NOT recompile
eval `scramv1 runtime -sh` # cmsenv is an alias not on the workers
echo $CMSSW_BASE "is the CMSSW we have on the local worker node"

pwd
export SCRAM_ARCH=slc7_amd64_gcc820
scramv1 project CMSSW CMSSW_10_6_28 # cmsrel is an alias not on the workers

cd /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2

echo "Arguments passed to the job, $1 and then $2: "
echo $1
echo $2

pwd
# job=$1

# xrdcp -f /core/python/ntuplewriter_mc_2018.py
cmsRun /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/core/python/ntuplewriter_mc_UL18.py $1 $2
