#!/bin/bash
cat /etc/redhat-release
echo $APPTAINER_CONTAINER
#source /cvmfs/cms.cern.ch/cmsset_default.sh
#cd /data/dust/user/titasroy/Ac_UL/CMSSW_10_6_28
#cmsenv
#source /data/dust/user/titasroy/Ac_UL/SFrame/setup.sh
#cd -
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH_STORED:$LD_LIBRARY_PATH
#export PATH=$PATH_STORED:$PATH
WORKDIR=$PWD
source /data/dust/user/titasroy/setup_UL_Ac.sh
cd $WORKDIR
# echo "**** BEGIN ENV"
# printenv
# echo "**** END ENV"
#ldd $(which sframe_main)
sframe_main $1
        