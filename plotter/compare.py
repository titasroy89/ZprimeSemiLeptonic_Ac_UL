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

#import cms_figure



categories=["output0","output1","output2"]
test_sample = ['MC.ST', 'MC.WJets', 'MC.DY', 'MC.Diboson','MC.QCD','MC.TTbar','DATA.DATA']
for year in ['18']:#,'17','16pre','16post']:
    for channel in ['muon']:	
        for cat in categories:
            for sample in test_sample:
                if '16' in year:
                    file_zprime=TFile("/nfs/dust/cms/group/zprime-uhh/AnalysisDNN_UL%sVFP/%s/uhh2.AnalysisModuleRunner.%s.root"%(year,channel,sample))
                else:
                    file_zprime=TFile("/nfs/dust/cms/group/zprime-uhh/AnalysisDNN_UL%s/%s/uhh2.AnalysisModuleRunner.%s.root"%(year,channel,sample))
                # print(file_zprime)
                hist_zprime=file_zprime.Get("DNN_%s_General/M_Zprime"%(cat))
                # print(hist_zprime.ClassName())
                if 'DY' in sample:
                    file_Ac=TFile("/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/20%s/%s/workdir_AnalysisDNN_20%s_%s/NOMINAL/uhh2.AnalysisModuleRunner.%sJets.root"%(year,channel,year,channel,sample))
                else:
                    file_Ac=TFile("/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/20%s/%s/workdir_AnalysisDNN_20%s_%s/NOMINAL_toppt/uhh2.AnalysisModuleRunner.%s.root"%(year,channel,year,channel,sample))

                # print(file_Ac)

                hist_Ac=file_Ac.Get("DNN_%s_General/M_Zprime"%(cat))
                # print(hist_Ac.ClassName())
                # print(hist_zprime.ClassName())
                print(cat,year,channel,sample,hist_zprime.Integral(),hist_Ac.Integral())
				
