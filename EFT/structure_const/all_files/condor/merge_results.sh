#!/bin/bash

# This script merges the results from all batch jobs

# Setup CMSSW environment
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src
eval `scramv1 runtime -sh`
cd /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/structure_const/all_files/condor

# Merge structure constants
python /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/structure_const/all_files/condor/process_all_samples.py --input-dir /data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_deltaPhi_sigmaPhi_ttree --output-dir /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/structure_const/all_files/condor/results --plot-only --merge-plots --variables DeltaYreco Delta_phi Sigma_phi --file-pattern 'uhh2.AnalysisModuleRunner.MC.*.root'

echo 'All results merged successfully!'
