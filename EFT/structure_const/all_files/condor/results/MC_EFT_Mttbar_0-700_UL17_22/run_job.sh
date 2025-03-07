#!/bin/bash
# Setup CMSSW environment
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src
eval `scramv1 runtime -sh`
cd /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/structure_const/all_files/condor
echo 'Running: python /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/structure_const/all_files/condor/process_all_samples.py --input-dir /data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_deltaPhi_sigmaPhi_ttree --output-dir /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/structure_const/all_files/condor/results/MC_EFT_Mttbar_0-700_UL17_22 --file-pattern 'uhh2.AnalysisModuleRunner.MC.MC_EFT_Mttbar_0-700_UL17_22.root' --variables DeltaYreco Delta_phi Sigma_phi'
python /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/structure_const/all_files/condor/process_all_samples.py --input-dir /data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_deltaPhi_sigmaPhi_ttree --output-dir /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/structure_const/all_files/condor/results/MC_EFT_Mttbar_0-700_UL17_22 --file-pattern 'uhh2.AnalysisModuleRunner.MC.MC_EFT_Mttbar_0-700_UL17_22.root' --variables DeltaYreco Delta_phi Sigma_phi
