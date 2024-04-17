#!/bin/bash

text2workspace.py datacard_UL18_muon_0_750.txt -o Ac_UL18_muon_0_750.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 --PO map='.*/TTbar_1:r_neg[1,0,20]' --PO map='.*/TTbar_2:r_pos=expr;;r_pos("57570360000/57998213000*@0*(1+@1)/(1-@1)",r_neg,Ac[-2,-5,0])' --PO verbose 

# 19833969000+37736391000
# 57570360000

# 20006527000+37991686000
# 57998213000