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


fileDir="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/muon/workdir_AnalysisDNN_2018_muonlow1/NOMINAL/"
directories=["TwoDCut_Muon_General"]#,"TwoDCut_Ele_General"]
histograms=["reliso_mu1","dRmin_mu1_jet","dRmin_ptrel_mu1","dRmin_pt_mu1","ptrel_pt_mu1"]
for hist in histograms:
    file_ttbar = TFile("%s/uhh2.AnalysisModuleRunner.MC.TTbar.root"%(fileDir),"read")
    file_QCD = TFile("%s/uhh2.AnalysisModuleRunner.MC.QCD.root"%(fileDir),"read")
    # print(file_ttbar)
    # print(file_QCD)
    temp_hist="DNN_output0_General/%s_match"%(hist)
    # print(temp_hist)
    hist_ttbar=file_ttbar.Get(temp_hist)
    hist_ttbar.SetDirectory(0)
    
    # print(hist_ttbar.ClassName())
    temp_hist_qcd="DNN_output0_General/%s"%(hist)
    # print(temp_hist_qcd)
    hist_qcd=file_QCD.Get(temp_hist_qcd)
    # print(temp_hist_qcd)
    print(hist_ttbar.Integral(), hist_qcd.Integral())
    hist_qcd.SetDirectory(0)
    hist_qcd.Add(hist_ttbar)
    hist_ttbar.Divide(hist_qcd)
    hist_ttbar.Draw("colz")
    canvas.SaveAs("%s_signal_bkg.pdf"%(hist))
    
