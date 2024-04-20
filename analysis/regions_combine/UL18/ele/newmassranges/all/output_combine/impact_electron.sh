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

export WORKSPACE=Ac_UL18_ele.root
export VERBOSITY=0

export SetParameters="rgx{r.+}=1,Ac=0.7"
export SetParametersExplicit="r_neg=1,Ac=0.7"
export SetParameterRanges="rgx{r.+}=0.5,2:Ac=-5,5"
export redefineSignalPOIs="Ac,r_neg"



export ASIMOV="-t -1"

# combine -M MultiDimFit -d $WORKSPACE --algo grid --points 100 -P Ac --floatOtherPOIs 1 --setParameterRanges Ac=-30,4 -n AcScan


echo
echo
echo "CREATE PLOTS"
echo
echo
for POI in ${POIS[@]}; do
  plotImpacts.py -i impacts.json -o $POI --POI $POI
done
echo
echo
