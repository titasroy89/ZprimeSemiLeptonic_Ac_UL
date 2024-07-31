#!/bin/bash

year="UL18" # UL16preVFP UL16postVFP UL17 UL18
channel="muon" # electron / muon

# where UHH2 code is installed
UHH_dir="/nfs/dust/cms/user/titasroy/Ac_UL/CMSSW_10_6_28/src/UHH2/"

#where (NOT MERGED) trees after preselection stored
input_dir="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/${channel}/workdir_Analysis_${year}_${channel}_low1/uhh2.AnalysisModuleRunner."
# input_dir="/nfs/dust/cms/group/zprime-uhh/Analysis_${year}/${channel}/workdir_Analysis_${year}_${channel}/uhh2.AnalysisModuleRunner."
echo $input_dir
# output dir
output_dir=$UHH_dir/ZprimeSemiLeptonic/data/Skimming_datasets_isolow_${year}_${channel}

if [ -d "${output_dir}" ]; then
    echo "output directory exists, will be deleted..."
    rm -r ${output_dir}
fi
echo "(re)create output directory..."
mkdir ${output_dir}
cd ${output_dir}

# MC
#for mc_name in TTToSemiLeptonic_${year} TTToHadronic_${year} TTTo2L2Nu_${year} WJetsToLNu_HT-70To100_${year} WJetsToLNu_HT-100To200_${year} WJetsToLNu_HT-200To400_${year} WJetsToLNu_HT-400To600_${year} WJetsToLNu_HT-600To800_${year} WJetsToLNu_HT-800To1200_${year} WJetsToLNu_HT-1200To2500_${year} WJetsToLNu_HT-2500ToInf_${year} DYJetsToLL_M-50_HT-70to100_${year} DYJetsToLL_M-50_HT-100to200_${year} DYJetsToLL_M-50_HT-200to400_${year} DYJetsToLL_M-50_HT-400to600_${year} DYJetsToLL_M-50_HT-600to800_${year} DYJetsToLL_M-50_HT-800to1200_${year} DYJetsToLL_M-50_HT-1200to2500_${year} DYJetsToLL_M-50_HT-2500toInf_${year} WW_${year} WZ_${year} ZZ_${year} ST_tW_antitop_5f_NoFullyHadronicDecays_${year} ST_tW_top_5f_NoFullyHadronicDecays_${year} ST_t-channel_antitop_4f_InclusiveDecays_${year} ST_t-channel_top_4f_InclusiveDecays_${year} ST_s-channel_4f_leptonDecays_${year} QCD_HT50to100_${year} QCD_HT100to200_${year} QCD_HT200to300_${year} QCD_HT300to500_${year} QCD_HT500to700_${year} QCD_HT700to1000_${year} QCD_HT1000to1500_${year} QCD_HT1500to2000_${year} QCD_HT2000toInf_${year} 

for mc_name in TTToSemiLeptonic_${year} TTToHadronic_${year} TTTo2L2Nu_${year} WJetsToLNu_HT-70To100_${year} WJetsToLNu_HT-100To200_${year} WJetsToLNu_HT-200To400_${year} WJetsToLNu_HT-400To600_${year} WJetsToLNu_HT-600To800_${year} WJetsToLNu_HT-800To1200_${year} WJetsToLNu_HT-1200To2500_${year} WJetsToLNu_HT-2500ToInf_${year} DYJetsToLL_M-50_HT-70to100_${year} DYJetsToLL_M-50_HT-100to200_${year} DYJetsToLL_M-50_HT-200to400_${year} DYJetsToLL_M-50_HT-400to600_${year} DYJetsToLL_M-50_HT-600to800_${year} DYJetsToLL_M-50_HT-800to1200_${year} DYJetsToLL_M-50_HT-1200to2500_${year} DYJetsToLL_M-50_HT-2500toInf_${year} WW_${year} WZ_${year} ZZ_${year} ST_t-channel_antitop_4f_InclusiveDecays_${year} ST_t-channel_top_4f_InclusiveDecays_${year} ST_s-channel_4f_leptonDecays_${year} QCD_HT50to100_${year} QCD_HT100to200_${year} QCD_HT200to300_${year} QCD_HT300to500_${year} QCD_HT500to700_${year} QCD_HT700to1000_${year} QCD_HT1000to1500_${year} QCD_HT1500to2000_${year} QCD_HT2000toInf_${year} ST_tW_top_5f_NoFullyHadronicDecays_PDFWeights_${year} ST_tW_antitop_5f_NoFullyHadronicDecays_PDFWeights_${year}
# for mc_name in ST_tW_antitop_5f_NoFullyHadronicDecays_PDFWeights_${year}
#for mc_name in TTToSemiLeptonic_${year} TTToHadronic_${year} TTTo2L2Nu_${year} QCD_HT50to100_${year} QCD_HT100to200_${year} QCD_HT200to300_${year} QCD_HT300to500_${year} QCD_HT500to700_${year} QCD_HT700to1000_${year} QCD_HT1000to1500_${year} QCD_HT1500to2000_${year} QCD_HT2000toInf_${year} 
#for mc_name in ST_tW_antitop_5f_NoFullyHadronicDecays_PDFWeights_${year}  ST_tW_antitop_5f_NoFullyHadronicDecays_PDFWeights_${year}
do
    echo $mc_name
    $UHH_dir/scripts/create-dataset-xmlfile ${input_dir}"MC."${mc_name}"*.root" "MC_"$mc_name.xml
    nice -n 10 python $UHH_dir/scripts/crab/readaMCatNloEntries.py 10 "MC_"$mc_name.xml True
done

# DATA
 if [ ${channel} = "electron" ]; then
     if [ ${year} = "UL18" ]; then
         for data_name in EGamma_RunA_${year} EGamma_RunB_${year} EGamma_RunC_${year} EGamma_RunD_${year}
         do
             echo $data_name
             $UHH_dir/scripts/create-dataset-xmlfile ${input_dir}"DATA."${data_name}"*.root" DATA_$data_name.xml
             nice -n 10 python $UHH_dir/scripts/crab/readaMCatNloEntries.py 10 DATA_$data_name.xml True
         done
     elif [ ${year} = "UL16postVFP" ]; then
         for data_name in DATA_SingleElectron_RunF_${year} DATA_SingleElectron_RunG_${year} DATA_SingleElectron_RunH_${year}
         do
             echo $data_name
             $UHH_dir/scripts/create-dataset-xmlfile ${input_dir}"DATA."${data_name}"*.root" DATA_$data_name.xml
             nice -n 10 python $UHH_dir/scripts/crab/readaMCatNloEntries.py 10 DATA_$data_name.xml True
         done
     else
         for data_name in DATA_SingleElectron_RunB_${year} DATA_SingleElectron_RunC_${year} DATA_SingleElectron_RunD_${year} DATA_SingleElectron_RunE_${year} DATA_SingleElectron_RunF_${year} DATA_SinglePhoton_RunB_${year} DATA_SinglePhoton_RunC_${year} DATA_SinglePhoton_RunD_${year} DATA_SinglePhoton_RunE_${year} DATA_SinglePhoton_RunF_${year}
         do
             echo $data_name
             $UHH_dir/scripts/create-dataset-xmlfile ${input_dir}"DATA."${data_name}"*.root" DATA_$data_name.xml
             nice -n 10 python $UHH_dir/scripts/crab/readaMCatNloEntries.py 10 DATA_$data_name.xml True
         done
     fi
 elif [ ${channel} = "muon" ]; then
     if [ ${year} = "UL18" ]; then
         for data_name in SingleMuon_RunA_${year} SingleMuon_RunB_${year} SingleMuon_RunC_${year} SingleMuon_RunD_${year}
         do
             echo $data_name
             $UHH_dir/scripts/create-dataset-xmlfile ${input_dir}"DATA."${data_name}"*.root" DATA_$data_name.xml
             nice -n 10 python $UHH_dir/scripts/crab/readaMCatNloEntries.py 10 DATA_$data_name.xml True
         done
     elif [ ${year} = "UL16postVFP" ]; then
         for data_name in SingleMuon_RunF_${year} SingleMuon_RunG_${year} SingleMuon_RunH_${year}
         do
             echo $data_name
             $UHH_dir/scripts/create-dataset-xmlfile ${input_dir}"DATA."${data_name}"*.root" DATA_$data_name.xml
             nice -n 10 python $UHH_dir/scripts/crab/readaMCatNloEntries.py 10 DATA_$data_name.xml True
         done
     else
         for data_name in DATA_SingleMuon_RunB_${year} DATA_SingleMuon_RunC_${year} DATA_SingleMuon_RunD_${year} DATA_SingleMuon_RunE_${year} DATA_SingleMuon_RunF_${year}
         do
             echo $data_name
             $UHH_dir/scripts/create-dataset-xmlfile ${input_dir}"DATA."${data_name}"*.root" DATA_$data_name.xml
             nice -n 10 python $UHH_dir/scripts/crab/readaMCatNloEntries.py 10 DATA_$data_name.xml True
         done
     fi
 fi

echo "output dir: ${output_dir}"
cd $UHH_dir/ZprimeSemiLeptonic/macros
