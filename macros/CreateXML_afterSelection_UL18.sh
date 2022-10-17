#!/bin/bash

#where UHH2 code installed
pathGL_code=/nfs/dust/cms/user/deleokse/RunII_106_v2/CMSSW_10_6_28/src/UHH2/
#where (NOT MERGED) trees after preselection stored
#path_data=/nfs/dust/cms/group/zprime-uhh/Analysis_UL18/muon/workdir_Zprime_Analysis_UL18_muon/uhh2.AnalysisModuleRunner.
path_data=/nfs/dust/cms/group/zprime-uhh/Analysis_UL18/electron/workdir_Analysis_UL18_electron/uhh2.AnalysisModuleRunner.

#mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_muon/
#cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_muon/
mkdir $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_electron/
cd $pathGL_code/ZprimeSemiLeptonic/data/Skimming_datasets_UL18_electron/


# MC
for sample_name in TTToSemiLeptonic_UL18 TTToHadronic_UL18 TTTo2L2Nu_UL18 WJetsToLNu_HT-70To100_UL18 WJetsToLNu_HT-100To200_UL18 WJetsToLNu_HT-200To400_UL18 WJetsToLNu_HT-400To600_UL18 WJetsToLNu_HT-600To800_UL18 WJetsToLNu_HT-800To1200_UL18 WJetsToLNu_HT-1200To2500_UL18 WJetsToLNu_HT-2500ToInf_UL18 DYJetsToLL_M-50_HT-70to100_UL18 DYJetsToLL_M-50_HT-100to200_UL18 DYJetsToLL_M-50_HT-200to400_UL18 DYJetsToLL_M-50_HT-400to600_UL18 DYJetsToLL_M-50_HT-600to800_UL18 DYJetsToLL_M-50_HT-800to1200_UL18 DYJetsToLL_M-50_HT-1200to2500_UL18 DYJetsToLL_M-50_HT-2500toInf_UL18 WW_UL18 WZ_UL18 ZZ_UL18 ST_tW_antitop_5f_NoFullyHadronicDecays_UL18 ST_tW_top_5f_NoFullyHadronicDecays_UL18 ST_t-channel_antitop_4f_InclusiveDecays_UL18 ST_t-channel_top_4f_InclusiveDecays_UL18 ST_s-channel_4f_leptonDecays_UL18 QCD_HT50to100_UL18 QCD_HT100to200_UL18 QCD_HT200to300_UL18 QCD_HT300to500_UL18 QCD_HT500to700_UL18 QCD_HT700to1000_UL18 QCD_HT1000to1500_UL18 QCD_HT1500to2000_UL18 QCD_HT2000toInf_UL18 ALP_ttbar_signal_UL18 ALP_ttbar_interference_UL18 HscalarToTTTo1L1Nu2J_m365_w36p5_res_UL18 HscalarToTTTo1L1Nu2J_m400_w40p0_res_UL18 HscalarToTTTo1L1Nu2J_m500_w50p0_res_UL18 HscalarToTTTo1L1Nu2J_m600_w60p0_res_UL18 HscalarToTTTo1L1Nu2J_m800_w80p0_res_UL18 HscalarToTTTo1L1Nu2J_m1000_w100p0_res_UL18 HscalarToTTTo1L1Nu2J_m365_w36p5_int_UL18 HscalarToTTTo1L1Nu2J_m400_w40p0_int_UL18 HscalarToTTTo1L1Nu2J_m500_w50p0_int_UL18 HscalarToTTTo1L1Nu2J_m600_w60p0_int_UL18 HscalarToTTTo1L1Nu2J_m800_w80p0_int_UL18 HscalarToTTTo1L1Nu2J_m1000_w100p0_int_UL18 HpseudoToTTTo1L1Nu2J_m365_w36p5_res_UL18 HpseudoToTTTo1L1Nu2J_m400_w40p0_res_UL18 HpseudoToTTTo1L1Nu2J_m500_w50p0_res_UL18 HpseudoToTTTo1L1Nu2J_m600_w60p0_res_UL18 HpseudoToTTTo1L1Nu2J_m800_w80p0_res_UL18 HpseudoToTTTo1L1Nu2J_m1000_w100p0_res_UL18 HpseudoToTTTo1L1Nu2J_m365_w36p5_int_UL18 HpseudoToTTTo1L1Nu2J_m400_w40p0_int_UL18 HpseudoToTTTo1L1Nu2J_m500_w50p0_int_UL18 HpseudoToTTTo1L1Nu2J_m600_w60p0_int_UL18 HpseudoToTTTo1L1Nu2J_m800_w80p0_int_UL18 HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_UL18 HscalarToTTTo1L1Nu2J_m365_w91p25_res_UL18 HscalarToTTTo1L1Nu2J_m400_w100p0_res_UL18 HscalarToTTTo1L1Nu2J_m500_w125p0_res_UL18 HscalarToTTTo1L1Nu2J_m600_w150p0_res_UL18 HscalarToTTTo1L1Nu2J_m800_w200p0_res_UL18 HscalarToTTTo1L1Nu2J_m1000_w250p0_res_UL18 HscalarToTTTo1L1Nu2J_m365_w91p25_int_UL18 HscalarToTTTo1L1Nu2J_m400_w100p0_int_UL18 HscalarToTTTo1L1Nu2J_m500_w125p0_int_UL18 HscalarToTTTo1L1Nu2J_m600_w150p0_int_UL18 HscalarToTTTo1L1Nu2J_m800_w200p0_int_UL18 HscalarToTTTo1L1Nu2J_m1000_w250p0_int_UL18 HpseudoToTTTo1L1Nu2J_m365_w91p25_res_UL18 HpseudoToTTTo1L1Nu2J_m400_w100p0_res_UL18 HpseudoToTTTo1L1Nu2J_m500_w125p0_res_UL18 HpseudoToTTTo1L1Nu2J_m600_w150p0_res_UL18 HpseudoToTTTo1L1Nu2J_m800_w200p0_res_UL18 HpseudoToTTTo1L1Nu2J_m1000_w250p0_res_UL18 HpseudoToTTTo1L1Nu2J_m365_w91p25_int_UL18 HpseudoToTTTo1L1Nu2J_m400_w100p0_int_UL18 HpseudoToTTTo1L1Nu2J_m500_w125p0_int_UL18 HpseudoToTTTo1L1Nu2J_m600_w150p0_int_UL18 HpseudoToTTTo1L1Nu2J_m800_w200p0_int_UL18 HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_UL18 HscalarToTTTo1L1Nu2J_m365_w9p125_res_UL18 HscalarToTTTo1L1Nu2J_m400_w10p0_res_UL18 HscalarToTTTo1L1Nu2J_m500_w12p5_res_UL18 HscalarToTTTo1L1Nu2J_m600_w15p0_res_UL18 HscalarToTTTo1L1Nu2J_m800_w20p0_res_UL18 HscalarToTTTo1L1Nu2J_m1000_w25p0_res_UL18 HscalarToTTTo1L1Nu2J_m365_w9p125_int_UL18 HscalarToTTTo1L1Nu2J_m400_w10p0_int_UL18 HscalarToTTTo1L1Nu2J_m500_w12p5_int_UL18 HscalarToTTTo1L1Nu2J_m600_w15p0_int_UL18 HscalarToTTTo1L1Nu2J_m800_w20p0_int_UL18 HscalarToTTTo1L1Nu2J_m1000_w25p0_int_UL18 HpseudoToTTTo1L1Nu2J_m365_w9p125_res_UL18 HpseudoToTTTo1L1Nu2J_m400_w10p0_res_UL18 HpseudoToTTTo1L1Nu2J_m500_w12p5_res_UL18 HpseudoToTTTo1L1Nu2J_m600_w15p0_res_UL18 HpseudoToTTTo1L1Nu2J_m800_w20p0_res_UL18 HpseudoToTTTo1L1Nu2J_m1000_w25p0_res_UL18 HpseudoToTTTo1L1Nu2J_m365_w9p125_int_UL18 HpseudoToTTTo1L1Nu2J_m400_w10p0_int_UL18 HpseudoToTTTo1L1Nu2J_m500_w12p5_int_UL18 HpseudoToTTTo1L1Nu2J_m600_w15p0_int_UL18 HpseudoToTTTo1L1Nu2J_m800_w20p0_int_UL18 HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_UL18 RSGluonToTT_M-500_UL18 RSGluonToTT_M-1000_UL18 RSGluonToTT_M-1500_UL18 RSGluonToTT_M-2000_UL18 RSGluonToTT_M-2500_UL18 RSGluonToTT_M-3000_UL18 RSGluonToTT_M-3500_UL18 RSGluonToTT_M-4000_UL18 RSGluonToTT_M-4500_UL18 RSGluonToTT_M-5000_UL18 RSGluonToTT_M-5500_UL18 RSGluonToTT_M-6000_UL18 ZPrimeToTT_M400_W40_UL18 ZPrimeToTT_M500_W50_UL18 ZPrimeToTT_M600_W60_UL18 ZPrimeToTT_M700_W70_UL18 ZPrimeToTT_M800_W80_UL18 ZPrimeToTT_M900_W90_UL18 ZPrimeToTT_M1000_W100_UL18 ZPrimeToTT_M1200_W120_UL18 ZPrimeToTT_M1400_W140_UL18 ZPrimeToTT_M1600_W160_UL18 ZPrimeToTT_M1800_W180_UL18 ZPrimeToTT_M2000_W200_UL18 ZPrimeToTT_M2500_W250_UL18 ZPrimeToTT_M3000_W300_UL18 ZPrimeToTT_M3500_W350_UL18 ZPrimeToTT_M4000_W400_UL18 ZPrimeToTT_M4500_W450_UL18 ZPrimeToTT_M5000_W500_UL18 ZPrimeToTT_M6000_W600_UL18 ZPrimeToTT_M7000_W700_UL18 ZPrimeToTT_M8000_W800_UL18 ZPrimeToTT_M9000_W900_UL18 ZPrimeToTT_M400_W120_UL18 ZPrimeToTT_M500_W150_UL18 ZPrimeToTT_M600_W180_UL18 ZPrimeToTT_M700_W210_UL18 ZPrimeToTT_M800_W240_UL18 ZPrimeToTT_M900_W270_UL18 ZPrimeToTT_M1000_W300_UL18 ZPrimeToTT_M1200_W360_UL18 ZPrimeToTT_M1400_W420_UL18 ZPrimeToTT_M1600_W480_UL18 ZPrimeToTT_M1800_W540_UL18 ZPrimeToTT_M2000_W600_UL18 ZPrimeToTT_M2500_W750_UL18 ZPrimeToTT_M3000_W900_UL18 ZPrimeToTT_M3500_W1050_UL18 ZPrimeToTT_M4000_W1200_UL18 ZPrimeToTT_M4500_W1350_UL18 ZPrimeToTT_M5000_W1500_UL18 ZPrimeToTT_M6000_W1800_UL18 ZPrimeToTT_M7000_W2100_UL18 ZPrimeToTT_M8000_W2400_UL18 ZPrimeToTT_M9000_W2700_UL18 ZPrimeToTT_M400_W4_UL18 ZPrimeToTT_M500_W5_UL18 ZPrimeToTT_M600_W6_UL18 ZPrimeToTT_M700_W7_UL18 ZPrimeToTT_M800_W8_UL18 ZPrimeToTT_M900_W9_UL18 ZPrimeToTT_M1000_W10_UL18 ZPrimeToTT_M1200_W12_UL18 ZPrimeToTT_M1400_W14_UL18 ZPrimeToTT_M1600_W16_UL18 ZPrimeToTT_M1800_W18_UL18 ZPrimeToTT_M2000_W20_UL18 ZPrimeToTT_M2500_W25_UL18 ZPrimeToTT_M3000_W30_UL18 ZPrimeToTT_M3500_W35_UL18 ZPrimeToTT_M4000_W40_UL18 ZPrimeToTT_M4500_W45_UL18 ZPrimeToTT_M5000_W50_UL18 ZPrimeToTT_M6000_W60_UL18 ZPrimeToTT_M7000_W70_UL18 ZPrimeToTT_M8000_W80_UL18 ZPrimeToTT_M9000_W90_UL18

do
    echo $sample_name
    $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"MC."${sample_name}"*.root" MC_$sample_name.xml
    python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 MC_$sample_name.xml True
done

# DATA
for sample_name in DATA_EGamma_RunA_UL18 DATA_EGamma_RunB_UL18 DATA_EGamma_RunC_UL18 DATA_EGamma_RunD_UL18
#for sample_name in DATA_SingleMuon_RunA_UL18 DATA_SingleMuon_RunB_UL18 DATA_SingleMuon_RunC_UL18 DATA_SingleMuon_RunD_UL18
do
    echo $sample_name
    $pathGL_code/scripts/create-dataset-xmlfile ${path_data}"DATA."${sample_name}"*.root" $sample_name.xml
    python $pathGL_code/scripts/crab/readaMCatNloEntries.py 10 $sample_name.xml True
done
pwd
cd $pathGL_code/ZprimeSemiLeptonic/macros
