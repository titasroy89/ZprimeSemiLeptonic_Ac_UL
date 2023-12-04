#!/bin/bash
rm Ac_muon_750_900.root
echo "removed old root file"

text2workspace.py datacard_750_900_DeltaY.txt -o Ac_muon_750_900.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 --PO map='.*/Ttbar_1:r_neg[1,0,20]' --PO map='.*/Ttbar_2:r_pos=expr;;r_pos("226663/208023*@0*(100+@1)/(100-@1)",r_neg,Ac[-2,-5,0])' --PO verbose --X-allow-no-signal 
