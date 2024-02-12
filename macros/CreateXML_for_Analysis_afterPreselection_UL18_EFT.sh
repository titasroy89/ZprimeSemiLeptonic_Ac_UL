#!/bin/bash

#where UHH2 code installed
pathGL_code=/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/
#where (NOT MERGED) trees after preselection stored
path_data=/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/EFT_output/combined/

mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_EFT_samples
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_EFT_samples

# MC
for sample_name in EFT_sample
do
    echo $sample_name

       $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"*.root" $sample_name.xml
       python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 $sample_name.xml True
done

pwd
cd $pathGL_code/ZprimeSemiLeptonic/macros
