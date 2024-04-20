#!/bin/bash

text2workspace.py datacard_UL18_ele.txt -o Ac_UL18_ele.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel -m 125 --PO map='.*/TTbar_1:r_neg[1,0,20]' --PO map='.*/TTbar_2:r_pos=expr;;r_pos("62583734000/63057134000*@0*(1+@1)/(1-@1)",r_neg,Ac[-2,-5,0])' --PO verbose 
