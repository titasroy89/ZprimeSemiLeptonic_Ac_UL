#!/usr/bin/env bash
date

# rm comb*
# rm higgs*
# rm Ac.pdf
# rm r_neg.pdf
# rm impacts.json

declare -a POIS=(
  "r_neg"
  "Ac"
)

export WORKSPACE=Ac_UL18_500_750.root
export VERBOSITY=0

export SetParameters="rgx{r.+}=1,Ac=0.7"
export SetParametersExplicit="r_neg=1,Ac=0.7"
export SetParameterRanges="rgx{r.+}=0.5,2:Ac=-5,5"
export redefineSignalPOIs="Ac,r_neg"



export ASIMOV="-t -1"

# echo
# echo
# echo "STAT ONLY UNCERTAINTY (ALL NUISANCES FROZEN) - performs another MultiDimFit, but this time with all constrained nuisance parameters frozen (--freezeParameters allConstrainedNuisances). This can provide insight into how the fit behaves when the nuisances are not allowed to float."
# echo
# echo
# combine -M MultiDimFit --algo singles -d $WORKSPACE -v 6 --redefineSignalPOIs $redefineSignalPOIs --setParameterRanges $SetParameterRanges --setParameters $SetParameters --robustFit 1 --cminDefaultMinimizerStrategy 0 -m 125 --saveWorkspace -n _paramFit_Test_allConstrainedNuisancesFrozen --freezeParameters allConstrainedNuisances $ASIMOV
# echo
# echo
# echo "SYST ONLY UNCERTAINTY (ALL STATS FROZEN)"
# echo
# echo

# combine -M MultiDimFit --algo singles -d $WORKSPACE -v $VERBOSITY --redefineSignalPOIs $redefineSignalPOIs --setParameterRanges $SetParameterRanges --setParameters $SetParameters --robustFit 1 --cminDefaultMinimizerStrategy 0 -m 125 --saveWorkspace -n _paramFit_Test_allStatsFrozen --freezeParameters prop_bin* $ASIMOV

echo
echo
echo "STAT ONLY UNCERTAINTY (ALL NUISANCES FROZEN) - performs another MultiDimFit, but this time with all constrained nuisance parameters frozen (--freezeParameters allConstrainedNuisances). This can provide insight into how the fit behaves when the nuisances are not allowed to float."
echo
echo
combine -M MultiDimFit --algo singles -d $WORKSPACE -v $VERBOSITY --redefineSignalPOIs $redefineSignalPOIs --setParameterRanges $SetParameterRanges --setParameters $SetParameters --robustFit 1 --cminDefaultMinimizerStrategy 0 -m 125 --saveWorkspace -n _paramFit_Test_allConstrainedNuisancesFrozen --freezeParameters Others_norm,ST_norm,TTbar_norm,btagCferr1,btagCferr2,btagHf,btagHfstats1,btagHfstats2,btagLf,btagLfstats1,btagLfstats2,eleID,eleReco,eleTrigger,fsr,isr,jec,jer_UL18,lumi_corr_161718,lumi_corr_1718,lumi_uncorr_18,muonIDStat,muonIDSyst,muonIsoStat,muonIsoSyst,muonTriggerStat,muonTriggerSyst,murmuf,pdf,prefiringWeight,pu,tmistag,ttagCorr,ttagUncorr $ASIMOV


echo "SYST ONLY UNCERTAINTY (ALL Stats FROZEN)"
# combine -M MultiDimFit --algo singles -d $WORKSPACE -v $VERBOSITY --redefineSignalPOIs $redefineSignalPOIs --setParameterRanges $SetParameterRanges --setParameters $SetParameters --robustFit 1 --cminDefaultMinimizerStrategy 0 -m 125 --saveWorkspace -n _paramFit_Test_allStatsFrozen --freezeParameters prop_binch1_muon_UL18_500_750_SR_bin0_Others,prop_binch1_muon_UL18_500_750_CR1_bin0_ST $ASIMOV
combine -M MultiDimFit --algo singles -d $WORKSPACE -v $VERBOSITY --redefineSignalPOIs $redefineSignalPOIs --setParameterRanges $SetParameterRanges --setParameters $SetParameters --robustFit 1 --cminDefaultMinimizerStrategy 0 -m 125 --saveWorkspace -n _paramFit_Test_allStatsFrozen --freezeParameters prop_binch1_muon_UL18_500_750_CR1_bin0_Others,prop_binch1_muon_UL18_500_750_CR1_bin0_ST,prop_binch1_muon_UL18_500_750_CR1_bin0_TTbar_1,prop_binch1_muon_UL18_500_750_CR1_bin0_TTbar_2,prop_binch1_muon_UL18_500_750_CR1_bin1_Others,prop_binch1_muon_UL18_500_750_CR1_bin1_ST,prop_binch1_muon_UL18_500_750_CR1_bin1_TTbar_1,prop_binch1_muon_UL18_500_750_CR1_bin1_TTbar_2,prop_binch1_muon_UL18_500_750_CR2_bin0_Others,prop_binch1_muon_UL18_500_750_CR2_bin0_ST,prop_binch1_muon_UL18_500_750_CR2_bin0_TTbar_1,prop_binch1_muon_UL18_500_750_CR2_bin0_TTbar_2,prop_binch1_muon_UL18_500_750_CR2_bin1_Others,prop_binch1_muon_UL18_500_750_CR2_bin1_ST,prop_binch1_muon_UL18_500_750_CR2_bin1_TTbar_1,prop_binch1_muon_UL18_500_750_CR2_bin1_TTbar_2,prop_binch1_muon_UL18_500_750_SR_bin0_Others,prop_binch1_muon_UL18_500_750_SR_bin0_ST,prop_binch1_muon_UL18_500_750_SR_bin0_TTbar_1,prop_binch1_muon_UL18_500_750_SR_bin0_TTbar_2,prop_binch1_muon_UL18_500_750_SR_bin1_Others,prop_binch1_muon_UL18_500_750_SR_bin1_ST,prop_binch1_muon_UL18_500_750_SR_bin1_TTbar_1,prop_binch1_muon_UL18_500_750_SR_bin1_TTbar_2,prop_binch2_ele_UL18_500_750_CR1_bin0_Others,prop_binch2_ele_UL18_500_750_CR1_bin0_ST,prop_binch2_ele_UL18_500_750_CR1_bin0_TTbar_1,prop_binch2_ele_UL18_500_750_CR1_bin0_TTbar_2,prop_binch2_ele_UL18_500_750_CR1_bin1_Others,prop_binch2_ele_UL18_500_750_CR1_bin1_ST,prop_binch2_ele_UL18_500_750_CR1_bin1_TTbar_1,prop_binch2_ele_UL18_500_750_CR1_bin1_TTbar_2,prop_binch2_ele_UL18_500_750_CR2_bin0_Others,prop_binch2_ele_UL18_500_750_CR2_bin0_ST,prop_binch2_ele_UL18_500_750_CR2_bin0_TTbar_1,prop_binch2_ele_UL18_500_750_CR2_bin0_TTbar_2,prop_binch2_ele_UL18_500_750_CR2_bin1_Others,prop_binch2_ele_UL18_500_750_CR2_bin1_ST,prop_binch2_ele_UL18_500_750_CR2_bin1_TTbar_1,prop_binch2_ele_UL18_500_750_CR2_bin1_TTbar_2,prop_binch2_ele_UL18_500_750_SR_bin0_Others,prop_binch2_ele_UL18_500_750_SR_bin0_ST,prop_binch2_ele_UL18_500_750_SR_bin0_TTbar_1,prop_binch2_ele_UL18_500_750_SR_bin0_TTbar_2,prop_binch2_ele_UL18_500_750_SR_bin1_Others,prop_binch2_ele_UL18_500_750_SR_bin1_ST,prop_binch2_ele_UL18_500_750_SR_bin1_TTbar_1,prop_binch2_ele_UL18_500_750_SR_bin1_TTbar_2 $ASIMOV
