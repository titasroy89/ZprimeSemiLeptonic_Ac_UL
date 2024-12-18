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

export WORKSPACE=Ac_UL18_muon.root
export VERBOSITY=0

export SetParameters="rgx{r.+}=1,Ac=0.64"
export SetParametersExplicit="r_neg=1,Ac=0.64"
export SetParameterRanges="rgx{r.+}=0.5,2:Ac=-5,5"
export redefineSignalPOIs="Ac,r_neg"



export ASIMOV="-t -1"

# combine -M MultiDimFit -d $WORKSPACE --algo grid --points 100 -P Ac --floatOtherPOIs 1 --setParameterRanges Ac=-30,4 -n AcScan


echo
echo
echo "STAT ONLY UNCERTAINTY (ALL NUISANCES FROZEN) - performs another MultiDimFit, but this time with all constrained nuisance parameters frozen (--freezeParameters allConstrainedNuisances). This can provide insight into how the fit behaves when the nuisances are not allowed to float."
echo
echo
combine -M MultiDimFit --algo singles -d $WORKSPACE -v $VERBOSITY --redefineSignalPOIs $redefineSignalPOIs --setParameterRanges $SetParameterRanges --setParameters $SetParameters --robustFit 1 --cminDefaultMinimizerStrategy 0 -m 125 --saveWorkspace -n _paramFit_Test_allConstrainedNuisancesFrozen --freezeParameters Others_norm,ST_norm,TTbar_norm,btagCferr1,btagCferr2,btagHf,btagHfstats1,btagHfstats2,btagLf,btagLfstats1,btagLfstats2,eleID,eleReco,eleTrigger,fsr,isr,jec,jer_UL18,lumi_corr_161718,lumi_corr_1718,lumi_uncorr_18,muonIDStat,muonIDSyst,muonIsoStat,muonIsoSyst,muonTriggerStat,muonTriggerSyst,murmuf,pdf,prefiringWeight,pu,tmistag,ttagCorr,ttagUncorr $ASIMOV


echo "SYST ONLY UNCERTAINTY (ALL Stats FROZEN)"
# combine -M MultiDimFit --algo singles -d $WORKSPACE -v $VERBOSITY --redefineSignalPOIs $redefineSignalPOIs --setParameterRanges $SetParameterRanges --setParameters $SetParameters --robustFit 1 --cminDefaultMinimizerStrategy 0 -m 125 --saveWorkspace -n _paramFit_Test_allStatsFrozen --freezeParameters prop_binch1_muon_UL18_0_500_SR_bin0_Others,prop_binele_UL18_SR_bin0_ST $ASIMOV
combine -M MultiDimFit --algo singles -d $WORKSPACE -v $VERBOSITY --redefineSignalPOIs $redefineSignalPOIs --setParameterRanges $SetParameterRanges --setParameters $SetParameters --robustFit 1 --cminDefaultMinimizerStrategy 0 -m 125 --saveWorkspace -n _paramFit_Test_allStatsFrozen --freezeParameters prop_binmuon_UL18_SR_bin0_Others,prop_binmuon_UL18_SR_bin0_ST,prop_binmuon_UL18_SR_bin0_TTbar_1,prop_binmuon_UL18_SR_bin0_TTbar_2,prop_binmuon_UL18_SR_bin1_Others,prop_binmuon_UL18_SR_bin1_ST,prop_binmuon_UL18_SR_bin1_TTbar_1,prop_binmuon_UL18_SR_bin1_TTbar_2 $ASIMOV
