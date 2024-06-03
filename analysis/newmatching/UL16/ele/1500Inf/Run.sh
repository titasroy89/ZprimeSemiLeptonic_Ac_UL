#!/bin/bash

text2workspace.py datacard_UL16_ele_1500Inf.txt -o Ac_UL16_1500Inf.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 --PO map='.*/TTbar_1:r_neg[1,0,20]' --PO map='.*/TTbar_2:r_pos=expr;;r_pos("106197944/107311316*@0*(100+@1)/(100-@1)",r_neg,Ac[-2,-5,0])' --PO verbose 
