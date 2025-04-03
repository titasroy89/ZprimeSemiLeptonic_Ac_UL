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
gROOT.SetBatch(True)

YesLog = True
NoLog=False
padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
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
H = 600;
W = 800;

stackList_orig={"Before":"Before","After":"After"}
# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W
legendHeightPer = 0.04
legList = stackList_orig.keys() 
#legList.reverse()

legendStart = 0.69
legendEnd = 0.97-(R/W)
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

canvas.cd()
pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
pad1.SetLeftMargin( L/W )
pad1.SetRightMargin( R/W )
pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
pad1.SetFillColor(0)
pad1.SetBorderMode(0)
pad1.SetFrameFillStyle(0)
pad1.SetFrameBorderMode(0)
pad1.SetTickx(1)
pad1.SetTicky(1)

pad1.Draw()
#
canvas.cd()
pad1.GetWh()



canvas.ResetDrawn()

# fileDir="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/Analysis/2018/muon/workdir_Analysis_UL17_muon_old/NOMINAL/"
fileDir="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2017/muon/workdir_AnalysisDNN_2017_muon_tight_btag/NOMINAL/"
# fileDir="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2017/muon/workdir_AnalysisDNN_2017_muon/NOMINAL/"
# pattern=".TTTo"
# matching_files = [f for f in os.listdir(fileDir) if pattern in f]
# print(matching_files)
histograms=["CHS_matched_pt_jet","CHS_matched_eta_jet","CHS_matched_deltaRmin_CHS_Puppi","pt_jet","eta_jet"]
histos_before=[]
histos_after=[]
histogram_map={"CHSMatch":["CHS_matched_pt_jet","CHS_matched_eta_jet","CHS_matched_deltaRmin_CHS_Puppi","pt_jet","eta_jet"],
               "CHS_Before_General":["CHS_pt_jet","CHS_eta_jet","dRmin_CHS_Puppi","pt_jet","eta_jet"]}

f="uhh2.AnalysisModuleRunner.MC.TTbar.root"
hist_after={"CHS_matched_pt_jet":"CHS_pt_jet",
            "CHS_matched_eta_jet":"CHS_eta_jet",
            "CHS_matched_deltaRmin_CHS_Puppi":"dRmin_CHS_Puppi",
            "pt_jet":"pt_jet",
            "eta_jet":"eta_jet",
            }
print(hist_after["CHS_matched_pt_jet"])
# for f in matching_files:
file=TFile("%s/%s"%(fileDir,f),'read')

# hist_pt1=file.Get("Btags1_General/pt_jet1")
# hist_pt2=file.Get("Btags1_General/pt_jet2")
# hist_pt=file.Get("Btags1_General/pt_jet")
# legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
# legend.SetNColumns(2)
# legend.SetBorderSize(0)
# legend.SetFillColor(0)

# hist_pt1.SetLineColor(kRed)
# hist_pt2.SetLineColor(kBlue)
# hist_pt.SetLineColor(kGreen)

# hist_pt.Draw("hist")
# hist_pt2.Draw("hist,same")
# hist_pt1.Draw("hist,same")
# legend.AddEntry(hist_pt1,"Jet1 Pt after Btagging",'f')

# legend.AddEntry(hist_pt2,"Jet2 Pt after Btagging",'f')
# legend.AddEntry(hist_pt,"All Jet Pt after Btagging",'f')
# legend.Draw()
# canvas.SaveAs("Btagged_pt.pdf")
# canvas.Clear()

# sys.exit()

print(file)
# histos_before=[]
bins_jetpt=[]
# for i in range(0,3.0,60):
# 	bins_jetpt.append(float(i))
# print((bins_jetpt))



# for hist in histograms:
# legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
# legend.SetNColumns(2)
# legend.SetBorderSize(0)
# legend.SetFillColor(0)
# # hist_after=hist.strip("matched_")
# histos_after=file.Get("CHSMatch/CHS_matched_deltaRmin_CHS_Puppi")
# # histos_after=histos_after.Rebin(2)
# bin1=histos_after.GetNbinsX()

# histos_before=file.Get("CHS_Before_General/dRmin_CHS_Puppi")
# bin2=histos_before.GetNbinsX()
# print("two bins are: ", bin1, bin2)
# # print("CHSMatch_beformatching/"%(hist))
# histos_before.SetLineColor(kBlue)
# histos_after.SetLineColor(kRed)
# # legend.AddEntry(histos_before,"Before Matching",'f')
# # legend.AddEntry(histos_after,"After Matching",'f')
# histos_before.GetXaxis().SetTitle("#DeltaR(CHS,Puppi)")
# # histos_before.Draw("hist")
# histos_after.Draw("hist")
# CMS_lumi.CMS_lumi(canvas, 5, 11)
# legend.Draw()
# canvas.SetLogy(1)
# canvas.SaveAs("deltaR_chs.pdf")
# canvas.Clear()



legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
legend.SetNColumns(2)
legend.SetBorderSize(0)
legend.SetFillColor(0)


# pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
# pad1.SetLeftMargin( L/W )
# pad1.SetRightMargin( R/W )
# pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
# pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
# pad1.SetFillColor(0)
# pad1.SetBorderMode(0)
# pad1.SetFrameFillStyle(0)
# pad1.SetFrameBorderMode(0)
# pad1.SetTickx(1)
# pad1.SetTicky(1)

# pad1.Draw()
#
canvas.cd()
# pad1.GetWh()
histograms=["CHS_matched_N_Jets_NotTight_1", "CHS_matched_N_Jets_NotTight_2", "CHS_matched_N_Jets_NotTight_3","CHS_matched_N_Jets_NotTight_all", "CHS_matched_N_Jets_NotTight","CHS_matched_N_Jets_Tight_1", "CHS_matched_N_Jets_Tight_2", "CHS_matched_N_Jets_Tight_3","CHS_matched_N_Jets_Tight_all", "CHS_matched_N_Jets_Tight"]
print("about to make ID plots")
# for reg in ["CHSMatch_afterBTag"]:
for reg in ["CHSMatch"]:
    # for hist in ["diff_pt","diff_eta","diff_pt_bin1","diff_eta_bin1","diff_pt_bin2","diff_eta_bin2","diff_pt_bin3","diff_eta_bin3"]:
    # for hist in ["bjet1_pt","bjet2_pt","bjet_pt"]:
    for hist in ["ratio_diff_bjet_pt"]:
        legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
        legend.SetNColumns(2)
        legend.SetBorderSize(0)
        legend.SetFillColor(0)
        hist_puppi=file.Get("%s/%s"%(reg,hist))
        # print("%s/Puppi_%s"%(reg,hist))
        # hist_chs=file.Get("%s/CHS_%s"%(reg,hist))
        # print("bin1 in puppi: ",hist_puppi.GetBinContent(1))
        # print("bin1 in chs: ",hist_chs.GetBinContent(1))

        hist_puppi.SetLineColor(kBlue)
        # hist_chs.SetLineColor(kRed)
        # print("chs:",hist, hist_chs.Integral())
        # print("puppi:",hist, hist_puppi.Integral())
      
        # legend.AddEntry(hist_puppi,"Puppi",'f')
        # legend.AddEntry(hist_chs,"CHS",'f')
        
        # maxVal=hist_chs.GetMaximum()
        # if "eta" in hist:
        #     hist_chs.GetXaxis().SetTitle("#eta jets")
        #     hist_chs.GetXaxis().SetRangeUser(-2.5,2.5)
        # else:
        #     hist_chs.GetXaxis().SetTitle("p_{T} jets")
        #     hist_chs.GetXaxis().SetRangeUser(0,1500)
        # hist_chs.SetMaximum(2.7*maxVal)
        # hist_chs.Draw("hist")
        hist_puppi.Draw("hist")
        CMS_lumi.CMS_lumi(canvas, 5, 11)
        # legend.Draw()
        canvas.SetLogy(1)
        canvas.SaveAs("afterDNN_tight_%s_%s.pdf"%(hist,reg))
        canvas.Clear()







sys.exit() 
       
       
       
       
        # if reg=="CHSMatch":
        #     # hist_chs=hist_chs.Rebin(3,"",array('d',[0.,50.,100.,1500]))
        #     # hist_puppi=hist_puppi.Rebin(3,"",array('d',[0.,50.,100.,1500]))
        #     print("bin 1 for puppi: ",hist_puppi.GetBinContent(1))
        #     print("bin 1 for chs: ",hist_chs.GetBinContent(1))
        #     # hist_chs.Add(hist_puppi,-1)
        #     hist_diff=hist_chs.Clone("diff")
        #     for i in range(hist_chs.GetNbinsX()):
        #         hist_diff.SetBinContent(i+1,abs(hist_puppi.GetBinContent(i+1)-hist_chs.GetBinContent(i+1)))
        #     # print("diff: ",hist_chs.GetBinContent(1))
        #     hist_diff.Draw("hist")
        #     if "eta" in hist:
        #         hist_diff.GetXaxis().SetTitle("#Delta(#etaCHS,#etaPuppi)")
        #     else:
        #         hist_diff.GetXaxis().SetTitle("#Delta(p_{T}CHS,p_{T}Puppi) GeV")
        #     canvas.SetLogy(1)
        #     canvas.SaveAs("diff%s_%s_origbins.pdf"%(hist,reg))
        #     canvas.Clear()

# sys.exit()

hist_ratio_eta=["ratio_chs_puppi_eta_bin1","ratio_chs_puppi_eta_bin2","ratio_chs_puppi_eta_bin3"]
hist_ratio_pt=["ratio_chs_puppi_pt_bin1","ratio_chs_puppi_pt_bin2","ratio_chs_puppi_pt_bin3"]
hist_frac_ratio_eta_chs=["ratio_chs_eta_bin1","ratio_chs_eta_bin2","ratio_chs_eta_bin3"]
hist_frac_ratio_pt_chs=["ratio_chs_pt_bin1","ratio_chs_pt_bin2","ratio_chs_pt_bin3"]
hist_frac_ratio_eta_puppi=["ratio_puppi_eta_bin1","ratio_puppi_eta_bin2","ratio_puppi_eta_bin3"]
hist_frac_ratio_pt_puppi=["ratio_puppi_pt_bin1","ratio_puppi_pt_bin2","ratio_puppi_pt_bin3"]
hist_btag_pt=["diff_pt_btag_1", "diff_pt_btag_2", "diff_pt_btag_3"] 
pt_jets=["pt_jet1","pt_jet", "pt_jet2"]
diff_bjet=["diff_bjet_pt", "diff_bjet_pt_low"]
for reg in ["CHSMatch_afterBTag"]:
    legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
    legend.SetNColumns(2)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    for hist in ["diff_bjet_pt"]:
        legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
        legend.SetNColumns(2)
        legend.SetBorderSize(0)
        legend.SetFillColor(0)
        # hist_puppi=file.Get("%s/%s"%(reg,hist))
        # print("for puppi: ", "%s/%s"%(reg,hist))
        # if reg=="CHS_Before_General":
        #     hist_chs=file.Get("%s/CHS_%s"%(reg,hist))
        # else:
        if "_1" in hist:
            hist_1=file.Get("%s/%s"%(reg,hist))
            print("%s/%s"%(reg,hist))
        if "_2" in hist:
            hist_2=file.Get("%s/%s"%(reg,hist))
        if "_3" in hist:
            hist_3=file.Get("%s/%s"%(reg,hist))
    # hist_1.GetXaxis().SetRangeUser(0,2.5)
    if "chs_puppi_eta" in hist:
        hist_1.GetXaxis().SetTitle("CHS #eta/Puppi #eta")
    if "diff_pt" in hist:
        hist_1.GetXaxis().SetTitle("CHS p_{T}-Puppi p_{T}")
    if "chs_eta" in hist:
        hist_1.GetXaxis().SetTitle("(CHS #eta-Puppi #eta)/CHS #eta")
    if "ratio_chs_pt" in hist:
        hist_1.GetXaxis().SetTitle("(CHS p_{T}-Puppi p_{T})/CHS p_{T}")
    if "ratio_chs_eta" in hist:
        hist_1.GetXaxis().SetTitle("(CHS #eta-Puppi #eta)/CHS #eta")
    if "ratio_puppi_pt" in hist:
        hist_1.GetXaxis().SetTitle("(CHS p_{T}-Puppi p_{T})/Puppi p_{T}")
    if "ratio_puppi_eta" in hist:
        hist_1.GetXaxis().SetTitle("(CHS #eta-Puppi #eta)/Puppi #eta")
    # hist_2.GetXaxis().SetRangeUser(-2.5,20)
    # hist_3.GetXaxis().SetRangeUser(-20,20)
    hist_1.SetMaximum(2.3*hist_1.GetMaximum())
    hist_1.SetLineColor(kRed)
    hist_2.SetLineColor(kBlue)
    hist_3.SetLineColor(kGreen)
    legend.AddEntry(hist_1,"Puppi Jet: 0 <p_{T}<50 GeV",'f')
    legend.AddEntry(hist_2,"Puppi Jet: 50<p_{T}<100 GeV",'f')
    legend.AddEntry(hist_3,"Puppi Jet: p_{T}>100",'f')
    hist_1.Draw("hist")
    hist_2.Draw("hist,same")
    hist_3.Draw("hist,same")
    legend.Draw("same")
    canvas.SetLogy(0)
    canvas.SaveAs("%s_%s_btag_bins_old.pdf"%(hist,reg))
    canvas.Clear()







    
        
        








    




