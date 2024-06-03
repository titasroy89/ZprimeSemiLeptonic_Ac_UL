#!/bin/bash

text2workspace.py datacard_UL18_ele_1500Inf.txt -o Ac_UL18_ele_1500Inf.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 --PO map='.*/TTbar_1:r_neg[1,0,20]' --PO map='.*/TTbar_2:r_pos=expr;;r_pos("166470640/169478980*@0*(100+@1)/(100-@1)",r_neg,Ac[-2,-5,0])' --PO verbose 
