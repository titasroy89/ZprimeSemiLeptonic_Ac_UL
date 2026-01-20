#!/bin/bash

#where UHH2 code installed
pathGL_code=/data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/

path_data=/data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL17/muon/workdir_Analysis_UL17_muon_templatemethod_Madgraph/uhh2.AnalysisModuleRunner.

mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL17_forAnalysisDNN_muon_templatemethod_madgraph
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL17_forAnalysisDNN_muon_templatemethod_madgraph

# MC
for sample_name in TTJets_Madgraph_UL17
do
    echo $sample_name
    $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"MC."${sample_name}"*.root" MC_$sample_name.xml
    python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 MC_$sample_name.xml True
done


pwd
cd $pathGL_code/ZprimeSemiLeptonic/macros