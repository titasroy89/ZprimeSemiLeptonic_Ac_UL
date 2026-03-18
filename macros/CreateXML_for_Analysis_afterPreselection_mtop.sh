#!/bin/bash
#where UHH2 code installed
pathGL_code=/data/dust/user/titasroy/Ac_UL/CMSSW_10_6_28/src/UHH2/
#where (NOT MERGED) trees after preselection stored
path_data=/data/dust/group/cms/zprime-uhh/Preselection_TopMass/workdir_Preselection_UL18_mtop173p5/uhh2.AnalysisModuleRunner.

mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_mtop_173p5_preselection
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_mtop_173p5_preselection


# #MC

for sample_name in MC_TTToSemiLeptonic_mtop173p5_UL18 MC_TTToHadronic_mtop173p5_UL18 MC_TTTo2L2Nu_mtop173p5_UL18


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