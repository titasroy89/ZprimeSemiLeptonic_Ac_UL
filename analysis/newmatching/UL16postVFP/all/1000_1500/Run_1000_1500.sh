#!/bin/bash

text2workspace.py datacard_UL16postVFP_1000_1500.txt -o Ac_UL16postVFP_1000_1500.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 --PO map='.*/TTbar_1:r_neg[1,0,20]' --PO map='.*/TTbar_2:r_pos=expr;;r_pos("356167550/359614660*@0*(100+@1)/(100-@1)",r_neg,Ac[-2,-5,0])' --PO verbose 