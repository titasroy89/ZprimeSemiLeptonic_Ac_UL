#!/bin/bash
#where UHH2 code installed
pathGL_code=/data/dust/user/titasroy/Ac_UL/CMSSW_10_6_28/src/UHH2/
#where (NOT MERGED) trees after preselection stored
path_data=/data/dust/group/cms/zprime-uhh/Preselection_CR/workdir_Preselection_UL16pre_CR/uhh2.AnalysisModuleRunner.

mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL16pre_CR_afterpresel
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL16pre_CR_afterpresel


# #MC

for sample_name in MC_TTToSemiLeptonic_erdON_UL16preVFP MC_TTToSemiLeptonic_CR1_UL16preVFP MC_TTToSemiLeptonic_CR2_UL16preVFP


do
    echo $sample_name

       $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"MC."${sample_name}"*.root" MC_$sample_name.xml
       python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 MC_$sample_name.xml True
done

## # #DATA
#for sample_name in DATA_SingleMuon_RunA_UL18 DATA_SingleMuon_RunB_UL18 DATA_SingleMuon_RunC_UL18 DATA_SingleMuon_RunD_UL18 DATA_EGamma_RunA_UL18 DATA_EGamma_RunB_UL18 DATA_EGamma_RunC_UL18 DATA_EGamma_RunD_UL18
#
#do
#    echo $sample_name 
#    $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"DATA."${sample_name}"*.root" $sample_name.xml
#    python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 $sample_name.xml True
#
#done
    
pwd
cd $pathGL_code/ZprimeSemiLeptonic/macros