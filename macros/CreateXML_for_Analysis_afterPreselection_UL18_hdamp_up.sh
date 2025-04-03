#!/bin/bash

#where UHH2 code installed
pathGL_code=/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/
#where (NOT MERGED) trees after preselection stored
path_data=/nfs/dust/cms/group/zprime-uhh/Presel_UL18_hdamp_up/workdir_Preselection_UL18_hdamp_up/uhh2.AnalysisModuleRunner.

mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_preselection_hdamp_up
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_preselection_hdamp_up


# MC
for sample_name in TTToSemiLeptonic_UL18 TTToHadronic_UL18 TTTo2L2Nu_UL18
do
    echo $sample_name
    $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"MC."${sample_name}"*.root" MC_$sample_name.xml
    python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 MC_$sample_name.xml True
done

pwd
cd $pathGL_code/ZprimeSemiLeptonic/macros
