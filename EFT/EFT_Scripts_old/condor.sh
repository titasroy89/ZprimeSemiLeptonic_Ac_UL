# #!/bin/bash
# source /cvmfs/grid.desy.de/etc/profile.d/grid-ui-env.sh
# source /cvmfs/cms.cern.ch/cmsset_default.sh

# # export SCRAM_ARCH=slc7_amd64_gcc820
# scramv1 project CMSSW CMSSW_10_6_28 # cmsrel is an alias not on the workers
# cd CMSSW_10_6_28/src/
# eval `scramv1 runtime -sh` # cmsenv is an alias not on the workers
# echo $CMSSW_BASE "is the CMSSW we created on the local worker node"
# cd ${_CONDOR_SCRATCH_DIR}
# pwd

# root_file_path="/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/${1}"

# xrdcp -f /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/invariantmass.py .
# python invariantmass.py "$root_file_path"

#!/bin/bash
# condor.sh

# Load necessary environment
source /cvmfs/grid.desy.de/etc/profile.d/grid-ui-env.sh
source /cvmfs/cms.cern.ch/cmsset_default.sh

# Initialize CMSSW environment
scramv1 project CMSSW CMSSW_10_6_28
cd CMSSW_10_6_28/src/
eval `scramv1 runtime -sh`
echo $CMSSW_BASE "is the CMSSW we created on the local worker node"
cd ${_CONDOR_SCRATCH_DIR}
pwd

# Receive the ROOT file name and Process ID as arguments
root_file_name="$1"
process_id="$2"
root_file_path="/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/${root_file_name}"

# Run the analysis script with the specified ROOT file
python invariantmass.py "$root_file_path"

# Rename output files to include the job's Process ID for uniqueness
mv mttbar.png mttbar_${process_id}.png
mv histograms.root histograms_${process_id}.root
