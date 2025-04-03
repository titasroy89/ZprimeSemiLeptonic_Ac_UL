from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F,TH2F
from ROOT import *
import os
import math
import sys
from optparse import OptionParser
from sys import argv
from numpy import log10
from array import array
from collections import OrderedDict
import CMS_lumi

from Style import *

thestyle = Style()

HasCMSStyle = False
style = None
if os.path.isfile('tdrstyle.C'):
    ROOT.gROOT.ProcessLine('.L tdrstyle.C')
    ROOT.setTDRStyle()
    #print ("Found tdrstyle.C file, using this style.")
    HasCMSStyle = True
    if os.path.isfile('CMSTopStyle.cc'):
        gROOT.ProcessLine('.L CMSTopStyle.cc+')
        style = CMSTopStyle()
        style.setupICHEPv1()
        #print "Found CMSTopStyle.cc file, use TOP style if requested in xml file."
if not HasCMSStyle:
    #print "Using default style defined in cuy package."
    thestyle.SetStyle()

ROOT.gROOT.ForceStyle()


file_toppt = TFile("/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/electron/workdir_AnalysisDNN_2018_electron/NOMINAL_toppt/uhh2.AnalysisModuleRunner.MC.TTbar.root","read")
file_nominal = TFile("/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/electron/workdir_AnalysisDNN_2018_electron/NOMINAL/uhh2.AnalysisModuleRunner.MC.TTbar.root" ,"read")

gROOT.SetBatch(True)
histogram = "DNN_output0_General/M_Zprime_rebin"
histo_nominal=file_nominal.Get(histogram)
histo_top=file_toppt.Get(histogram)
H = 600;
W = 800;
stackList = { "TTbar":[kRed],"TTbar_pt":[kMagenta-10]}#"ST":[kBlue]}

# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W
padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
legendHeightPer = 0.04
legList = stackList.keys() 
#legList.reverse()

legendStart = 0.69
legendEnd = 0.97-(R/W)

legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legend.SetNColumns(2)
legend.SetBorderSize(0)
legend.SetFillColor(0)

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

file_toppt = TFile("/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/electron/workdir_AnalysisDNN_2018_electron/NOMINAL_toppt/uhh2.AnalysisModuleRunner.MC.TTbar.root","read")
file_nominal = TFile("/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/electron/workdir_AnalysisDNN_2018_electron/NOMINAL/uhh2.AnalysisModuleRunner.MC.TTbar.root" ,"read")

histogram = "DNN_output0_General/M_Zprime_rebin"
histo_nominal=file_nominal.Get(histogram)
histo_top=file_toppt.Get(histogram)
# histo_nominal.SetFillColor(stackList["TTbar"][0])
# histo_top.SetFillColor(stackList["TTbar_pt"][0])
histo_nominal.SetLineColor(stackList["TTbar"][0])
histo_nominal.SetLineWidth(1)
histo_top.SetLineColor(stackList["TTbar_pt"][0])
histo_top.SetLineStyle(10)
histo_top.SetLineWidth(1)

legend.AddEntry(histo_nominal,"t#bar{t}",'l')
legend.AddEntry(histo_top,"t#bar{t} top p_{T}",'l')

errorban=histo_nominal.Clone("errorban")
errorban.Sumw2()
errorban.SetLineColor(kBlack)
errorban.SetLineWidth(5)
errorban.SetFillColor(kBlack)
errorban.SetFillStyle(3245)
# errorban.SetFillStyle(3344)
errorban.SetMarkerSize(0)
legend.AddEntry(errorban,"syst incl Q2",'f')
canvas.cd()

histo_nominal.Draw("hist,same")
histo_top.Draw("hist,same")
errorban.Draw("E2,SAME")
legend.SetTextSize(0.05)
legend.Draw("same")

CMS_lumi.CMS_lumi(canvas, 6, 11)
canvas.SaveAs("TopPt_linear.pdf")




