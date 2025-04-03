#!/bin/bash

text2workspace.py datacard_muon.txt -o Ac_muon.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 --PO map='.*/TTbar_1:r_neg[1,0,20]' --PO map='.*/TTbar_2:r_pos=expr;;r_pos("96743537873/97477290562*@0*(100+@1)/(100-@1)",r_neg,Ac[-2,-5,0])' --PO verbose 

# 58359824300/58742677800
# 30766401800/31040952200
# 5541712810/5592335780
# 1816934760/1838918690
# 258664203/262406092
# =
# 96743537873/97477290562