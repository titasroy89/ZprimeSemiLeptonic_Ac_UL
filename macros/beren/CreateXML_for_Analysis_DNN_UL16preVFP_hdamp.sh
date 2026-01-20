#!/bin/bash

#where UHH2 code installed
pathGL_code=/data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/
#where (NOT MERGED) trees after preselection stored
path_data=/data/dust/group/cms/zprime-uhh/Analysis_UL16preVFP_templatemethod/electron/workdir_Analysis_UL16preVFP_electron_templatemethod/uhh2.AnalysisModuleRunner.

mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_DNN_UL16preVFP_electron_templatemethod
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_DNN_UL16preVFP_electron_templatemethod


# MC
for sample_name in TTToSemiLeptonic_UL16preVFP TTToHadronic_UL16preVFP TTTo2L2Nu_UL16preVFP
do
    echo $sample_name
    $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"MC."${sample_name}"*.root" MC_$sample_name.xml
    python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 MC_$sample_name.xml True
done

pwd
cd $pathGL_code/ZprimeSemiLeptonic/macros
