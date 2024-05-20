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

export SetParameters="rgx{r.+}=1,Ac=0.72"
export SetParametersExplicit="r_neg=1,Ac=0.72"
export SetParameterRanges="rgx{r.+}=0.5,2:Ac=-5,5"
export redefineSignalPOIs="Ac,r_neg"




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
