#!/bin/bash
#where UHH2 code installed
pathGL_code=/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/
#where (NOT MERGED) trees after preselection stored
path_data=/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_unfolding/UL18/preselection/workdir_Preselection_UL18_NumberOfEvents_new/uhh2.AnalysisModuleRunner.
#path_data=/nfs/dust/cms/group/zprime-uhh/Analysis_UL18/electron/workdir_Zprime_Analysis_UL18_electron/uhh2.AnalysisModuleRunner.

mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_numberofevents
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_numberofevents
#mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_electron
#cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_electron


# #MC

for sample_name in TTToSemiLeptonic_UL18

do
    echo $sample_name

       $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"MC."${sample_name}"*.root" MC_$sample_name.xml
       python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 MC_$sample_name.xml True
done

# # #DATA
#for sample_name in DATA_EGamma_RunA_UL18_blinded DATA_EGamma_RunB_UL18_blinded DATA_EGamma_RunC_UL18_blinded DATA_EGamma_RunD_UL18_blinded 
# for sample_name in DATA_SingleMuon_RunB_UL18_blinded DATA_SingleMuon_RunC_UL18_blinded DATA_SingleMuon_RunD_UL18_blinded  

# do
#     echo $sample_name 
#     $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"DATA."${sample_name}"*.root" $sample_name.xml
#     python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 $sample_name.xml True

# done

pwd
cd $pathGL_code/ZprimeSemiLeptonic/macros
