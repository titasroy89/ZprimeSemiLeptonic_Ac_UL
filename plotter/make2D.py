from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F
from ROOT import *
import os
import math
import sys
from optparse import OptionParser
from sys import argv
from numpy import log10
from array import array
from collections import OrderedDict
H = 600;
W = 800;


# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W
canvas = TCanvas('c1','c1',W,H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(1)


# fileDir ="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/muon/workdir_AnalysisDNN_2018_muon_dY/NOMINAL/"
fileDir="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/electron/workdir_AnalysisDNN_2018_electron/NOMINAL/"
directories=["DNN_output1_General","DNN_output1_chi2_General"]
#directories=["TwoDCut_Muon_low1_General","TwoDCut_Muon_General"]#,"TwoDCut_Ele_General"]
#directories=["DNN_output0_General","DNN_output1_General","DNN_output2_General","DNN_output0_TopTag_General","DNN_output0_NoTopTag_General"]
histograms=["dRmin_ptrel_ele1"]#,"dRmin_pt_ele1","ptrel_pt_ele1","reliso_ele1","dRmin_ele1_jet","ptrel_ele1_jet"]
# histograms=["dRmin_ptrel_mu1"]#,"dRmin_pt_mu1","ptrel_pt_mu1","reliso_mu1","dRmin_mu1_jet","ptrel_mu1_jet","pt_mu1"]
# histograms=["reliso_mu1","dRmin_mu1_jet","dRmin_ptrel_mu1","dRmin_pt_mu1","ptrel_pt_mu1"]
#istograms=["pt_mu1","reliso_mu1",""]
# histograms=["dRmin_ptrel_mu1","reliso_mu1","dRmin_mu1_jet","ptrel_mu1_jet"]

#TTbar_files=["semi1","other","semi2","semi3","semi4"]

histo_={}

#for ttbar in TTbar_files:
#	histo_[ttbar]={}
for dir in directories:
   # 		histo_[ttbar][dir]={}
	histo_[dir]={}
    	for histo in histograms:
        	#	histo_[ttbar][dir][histo]=[]
        	histo_[dir][histo]=[]
#for ttbar in TTbar_files:
for dir in directories:
	for histo in histograms:
 #       		file_ = TFile("%s/uhh2.AnalysisModuleRunner.MC.TTbar_%s.root"%(fileDir,ttbar),"read")
        	file_ = TFile("%s/uhh2.AnalysisModuleRunner.MC.QCD.root"%(fileDir),"read")
        	#	print("%s/uhh2.AnalysisModuleRunner.MC.TTbar_%s.root"%(fileDir,ttbar))
        # print("%s/uhh2.AnalysisModuleRunner.MC.TTbar.root"%(fileDir))
        	temp_hist="%s/%s"%(dir,histo)
        	#	print(temp_hist)
        	#histo_[ttbar][dir][histo]=file_.Get(temp_hist)
        	#histo_[ttbar][dir][histo].SetDirectory(0)
        	histo_[dir][histo]=file_.Get(temp_hist)
        	histo_[dir][histo].SetDirectory(0)
        	if "_pt" in histo:
         		histo_[dir][histo].Draw("colz")
            		#histo_[ttbar][dir][histo].Draw("colz")
        	else:
            		histo_[dir][histo].Draw("hist")
            		#histo_[ttbar][dir][histo].Draw("hist")

        # print("making histos:", dir, histo, histo_[ttbar][dir][histo].ClassName())
# print(histo_[ttbar][dir][histo].ClassName())
    #   histo_[ttbar][dir][histo].ClassName()

#for ttbar in TTbar_files[1:]:
 #    for dir in directories:
  #       for histo in histograms:
   #          print("adding histos: ", ttbar, dir, histo)
#             # print("adding to: ", ttbar)
#             print("adding: ", histo_[ttbar][dir][histo])
    #         histo_["semi1"][dir][histo].Add(histo_[ttbar][dir][histo])

for dir in directories:
     for histo in histograms:
         # if "_pt" in histo:
         if "_pt" in histo:
     #        histo_["semi1"][dir][histo].Draw("colz")
         	histo_[dir][histo].Draw("colz")
         else:
             #histo_["semi1"][dir][histo].Draw("hist")
	        histo_[dir][histo].Draw("hist")

         canvas.SaveAs("%s_%s_ele_qcd.pdf"%(dir,histo))


