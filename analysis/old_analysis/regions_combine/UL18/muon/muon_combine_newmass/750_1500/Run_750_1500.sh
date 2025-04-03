#!/bin/bash

text2workspace.py datacard_UL18_muon_750_1500.txt -o Ac_UL18_muon_750_1500.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 --PO map='.*/TTbar_1:r_neg[1,0,20]' --PO map='.*/TTbar_2:r_pos=expr;;r_pos("4742971100/4787850200*@0*(1+@1)/(1-@1)",r_neg,Ac[-2,-5,0])' --PO verbose 

# 1172683500+3570287600
# 4742971100

# 3601730000+1186120200
# 4787850200