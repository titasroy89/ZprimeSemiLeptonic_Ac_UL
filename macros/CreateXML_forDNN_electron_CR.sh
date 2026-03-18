#!/bin/bash

#where UHH2 code installed
pathGL_code=/data/dust/user/titasroy/Ac_UL/CMSSW_10_6_28/src/UHH2
#where (NOT MERGED) trees after selection stored
path_data=/data/dust/user/titasroy/Ac_UL_ntuples/ColorReconnection/Analysis/electron/workdir_Analysis_2016pre_electron_CR/uhh2.AnalysisModuleRunner.

mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL16pre_CR_AnalysisDNN
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL16pre_CR_AnalysisDNN

# MC

for sample_name in TTToSemiLeptonic_CR1_UL16pre TTToSemiLeptonic_CR2_UL16pre TTToSemiLeptonic_erdON_UL16pre

do
    echo $sample_name
    $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"MC."${sample_name}"*.root" MC_$sample_name.xml
    python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 MC_$sample_name.xml True
done

pwd
cd $pathGL_code/ZprimeSemiLeptonic/macros


