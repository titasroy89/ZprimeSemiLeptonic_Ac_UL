#!/bin/bash
#where UHH2 code installed
pathGL_code=/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/
#where (NOT MERGED) trees after preselection stored
path_data=/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/Preselection/workdir_EFT_preselection/uhh2.AnalysisModuleRunner.MC.
#path_data=/nfs/dust/cms/group/zprime-uhh/Analysis_UL18/electron/workdir_Zprime_Analysis_UL18_electron/uhh2.AnalysisModuleRunner.

mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_EFT_afterpreselection
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_EFT_afterpreselection
#mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_electron
#cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_electron


# #MC

for sample_name in EFT_sample

do
    echo $sample_name

       $pathGL_code/scripts/create-dataset-xmlfile ${path_data}${sample_name}"*.root" MC_$sample_name.xml
       python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 MC_$sample_name.xml True
done


pwd
cd $pathGL_code/ZprimeSemiLeptonic/macros
