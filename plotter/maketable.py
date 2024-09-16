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


leptons=["electron","muon"]
years=["2016","2017","2018"]
regions=["0_500","500_750","750_1000","1000_1500","1500Inf"]


all_samples=["MC.TTbar","MC.WJets","MC.DYJets","MC.ST","MC.QCD","MC.Diboson","Total","DATA.DATA"]
sample_names=["MC.TTbar","MC.WJets","MC.DYJets","MC.ST","MC.QCD","MC.Diboson","DATA.DATA"]
# hist["muon"]["2018"][sample]["0_500"]
hist={}
x_err={}
file={}
for lep in leptons:
    hist[lep]={}
    x_err[lep]={}
    file[lep]={}
    for year in years:
        hist[lep][year]={}
        x_err[lep][year]={}
        file[lep][year]={}
        for sample in all_samples:
            hist[lep][year][sample]={}
            x_err[lep][year][sample]={}
            file[lep][year][sample]={}
            for mass in regions:
                hist[lep][year][sample][mass]={}
                x_err[lep][year][sample][mass]={}

latex_names={"MC.TTbar":"$ttbar$",
             "MC.ST":"Single Top",
             "MC.WJets":"W+jets",
             "MC.DYJets":"Drell-Yan",
             "MC.QCD": "Multi-Jet",
             "MC.Diboson":"Diboson",
             "Total":"TOTAL",
             "DATA.DATA":"DATA",
}

import ctypes
for lep in leptons:
    for year in years:
        for sample in sample_names:
            fileDir ="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/%s/%s/workdir_AnalysisDNN_%s_%s/NOMINAL/"%(year,lep,year,lep)
            file[lep][year][sample]=TFile("%s/uhh2.AnalysisModuleRunner.%s.root"%(fileDir,sample),"read")
            for mass in regions:
                print(lep,year,mass,sample)
                error=ctypes.c_double(0.)
                hist[lep][year][sample][mass]=file[lep][year][sample].Get("DeltaY_reco_%s_SR_General/DeltaY_reco"%(mass))
                # print(hist[lep][year][mass][sample].ClassName())
                print(hist[lep][year][sample][mass].Integral())
                hist[lep][year][sample][mass].IntegralAndError(1,2,error,"")
                x_err[lep][year][sample][mass]=error.value

# debug
# print(hist["electron"]["2018"]["1500Inf"]["MC.TTbar"].Integral())
# print(hist["muon"]["2017"][sample]["0_500"].Integral())
# print(hist[lep]["2016"][mass][sample].Integral())
# print(hist['muon']['2016']['MC.TTbar']['0_500'].Integral()) 
# print(hist["electron"]["2018"][sample]["0_500"].Integral())
# print(hist["electron"]["2017"][sample]["0_500"].Integral())
# print(hist["electron"]['2016']['MC.TTbar']['0_500'].Integral())

for lep in leptons:
    for year in years:
        for mass in regions:
            hist[lep][year]["Total"][mass]=hist[lep][year]["MC.TTbar"][mass].Clone("TOTAL")
            for sample in ['MC.ST','MC.WJets','MC.DYJets','MC.Diboson','MC.QCD']:
                hist[lep][year]["Total"][mass].Add(hist[lep][year][sample][mass])
                error=ctypes.c_double(0.)
                hist[lep][year]["Total"][mass].IntegralAndError(1,2,error,"")
                x_err[lep][year]["Total"][mass]=error.value





table=''
table +=  '\begin{tabular}{|l c c c c c c |} \n'
table +=  '\hline\n'
table +=  'Process &  $\mu_{2018}$ & $\mu_{2017}$ & $\mu_{2016}$ & $e_{2018}$ & $e_{2017}$ & $e_{2016}$ \\\\ \n'
table +=  '\hline\n'
table +=  '\multicolumn{7}{| c | }{} \\ \n'
table +=  '\multicolumn{7}{| c | }{$\mttbar \in[0,500] \GeV$}\\ \n'
table +=  '\multicolumn{7}{| c | }{} \\ \hline'
table +=  '\rule{-2pt}{11pt} \\ \hline \n'
for sample in all_samples:
        print(sample)
        table += '%s & $%.2f \pm %.2lf$  & $%.2f \\pm %.2lf$ & $%.2f \\pm %.2lf$ & $%.2f \\pm %.2lf$ & $%.2f \\pm %.2lf$ & $%.2f \\pm %.2lf$  \\\\ \n' % (latex_names[sample],hist["muon"]["2016"][sample]['0_500'].Integral() , x_err["muon"]["2016"][sample]['0_500'], hist["muon"]["2017"][sample]['0_500'].Integral(), x_err["muon"]["2017"][sample]["0_500"], hist["muon"]["2018"][sample]["0_500"].Integral(), x_err["muon"]["2018"][sample]["0_500"], hist["electron"]["2016"][sample]["0_500"].Integral(), x_err["electron"]["2016"][sample]["0_500"], hist["electron"]["2017"][sample]["0_500"].Integral(), x_err["electron"]["2017"][sample]["0_500"], hist["electron"]["2018"][sample]["0_500"].Integral(), x_err["electron"]["2018"][sample]["0_500"])
table +=  '\multicolumn{7}{| c | }{} \\ \n'
table +=  '\multicolumn{7}{| c | }{$\mttbar \in[500,750] \GeV$}\\ \n'
table +=  '\multicolumn{7}{| c | }{} \\ \hline \n'
for sample in all_samples:
        print(sample)
        table += '%s & $%.2f \pm %.2f$  & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ \\\\ \n' % (latex_names[sample],hist["muon"]["2016"][sample]["500_750"].Integral() , x_err["muon"]["2016"][sample]["500_750"], hist["muon"]["2017"][sample]["500_750"].Integral(), x_err["muon"]["2017"][sample]["500_750"], hist["muon"]["2018"][sample]["500_750"].Integral(), x_err["muon"]["2018"][sample]["500_750"], hist["electron"]["2016"][sample]["500_750"].Integral(), x_err["electron"]["2016"][sample]["500_750"], hist["electron"]["2017"][sample]["500_750"].Integral(), x_err["electron"]["2017"][sample]["500_750"], hist["electron"]["2018"][sample]["500_750"].Integral(), x_err["electron"]["2018"][sample]["500_750"])
table +=  '\multicolumn{7}{| c | }{} \\ \n'
table +=  '\multicolumn{7}{| c | }{$\mttbar \in[750,1000] \GeV$}\\ \n'
table +=  '\multicolumn{7}{| c | }{} \\ \hline \n'
for sample in all_samples:
        print(sample)
        table += '%s & $%.2f \pm %.2f$  & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ \\\\ \n' % (latex_names[sample],hist["muon"]["2016"][sample]["750_1000"].Integral() , x_err["muon"]["2016"][sample]["750_1000"], hist["muon"]["2017"][sample]["750_1000"].Integral(), x_err["muon"]["2017"][sample]["750_1000"], hist["muon"]["2018"][sample]["750_1000"].Integral(), x_err["muon"]["2018"][sample]["750_1000"], hist["electron"]["2016"][sample]["750_1000"].Integral(), x_err["electron"]["2016"][sample]["750_1000"], hist["electron"]["2017"][sample]["750_1000"].Integral(), x_err["electron"]["2017"][sample]["750_1000"], hist["electron"]["2018"][sample]["750_1000"].Integral(), x_err["electron"]["2018"][sample]["750_1000"])
table +=  '\multicolumn{7}{| c | }{} \\ \n'
table +=  '\multicolumn{7}{| c | }{$\mttbar \in[1000,1500] \GeV$}\\ \n'
table +=  '\multicolumn{7}{| c | }{} \\ \hline \n'
for sample in all_samples:
        print(sample)
        table += '%s & $%.2f \pm %.2f$  & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ \\\\ \n' % (latex_names[sample],hist["muon"]["2016"][sample]["1000_1500"].Integral() , x_err["muon"]["2016"][sample]["1000_1500"], hist["muon"]["2017"][sample]["1000_1500"].Integral(), x_err["muon"]["2017"][sample]["1000_1500"], hist["muon"]["2018"][sample]["1000_1500"].Integral(), x_err["muon"]["2018"][sample]["1000_1500"], hist["electron"]["2016"][sample]["1000_1500"].Integral(), x_err["electron"]["2016"][sample]["1000_1500"], hist["electron"]["2017"][sample]["1000_1500"].Integral(), x_err["electron"]["2017"][sample]["1000_1500"], hist["electron"]["2018"][sample]["1000_1500"].Integral(), x_err["electron"]["2018"][sample]["1000_1500"])
table +=  '\multicolumn{7}{| c | }{} \\ \n'
table +=  '\multicolumn{7}{| c | }{$\mttbar \in[1500,Inf] \GeV$}\\ \n'
table +=  '\multicolumn{7}{| c | }{} \\ \hline \n'
for sample in all_samples:
        print(sample)
        table += '%s & $%.2f \pm %.2f$  & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ & $%.2f \\pm %.2f$ \\\\ \n' % (latex_names[sample],hist["muon"]["2016"][sample]["1500Inf"].Integral() , x_err["muon"]["2016"][sample]["1500Inf"], hist["muon"]["2017"][sample]["1500Inf"].Integral(), x_err["muon"]["2017"][sample]["1500Inf"], hist["muon"]["2018"][sample]["1500Inf"].Integral(), x_err["muon"]["2018"][sample]["1500Inf"], hist["electron"]["2016"][sample]["1500Inf"].Integral(), x_err["electron"]["2016"][sample]["1500Inf"], hist["electron"]["2017"][sample]["1500Inf"].Integral(), x_err["electron"]["2017"][sample]["1500Inf"], hist["electron"]["2018"][sample]["1500Inf"].Integral(), x_err["electron"]["2018"][sample]["1500Inf"])
table += '\\hline \n'
table +=  '\end{tabular}'
table = table.replace("$0.0 \pm 0.0$","---")
print(table)
