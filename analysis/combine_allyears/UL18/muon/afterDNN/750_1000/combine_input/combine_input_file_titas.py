from ROOT import *
import os
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="muon", type='str',
                  help="Specify which channel Mu or Ele? default is Mu")

(options, args) = parser.parse_args()

finalState = options.channel
inputDir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/"
stackList = {"TTbar", "WJets", "DY", "ST", "Diboson", "QCD", "DATA"}
Mttbar = "750_1000"
combine_file = TFile('DY_%s_%s.root' % (finalState, Mttbar), 'RECREATE')

combine_file.mkdir("DeltaY")


systematic_name_mapping = {
    "mu_reco_": "muonReco",
    "pu_": "pu",
    "prefiring_": "prefiringWeight",
    "mu_id_": "muonID",
    "mu_iso_": "muonIso",
    "mu_trigger_": "muonTrigger",
    "ele_id_" : "electronID", 
    "ele_trigger_": "electronTrigger",
    "ele_reco_": "electronReco",
    "murmuf_up": "murmufUp", 
    "murmuf_none": "murmufNone", 
    "murmuf_down": "murmufDown", 
    "isr_": "isr", 
    "fsr_": "fsr", 
    "btag_cferr1_": "btagCferr1", 
    "btag_cferr2_": "btagCferr2", 
    "btag_hf_": "btagHf",  
    "btag_hfstats1_": "btagHfstats1",
    "btag_hfstats2_": "btagHfstats2", 
    "btag_lf_": "btagLf", 
    "btag_lfstats1_": "btagLfstats1",
    "btag_lfstats2_": "btagLfstats2", 
    "ttag_corr_": "ttagCorr", 
    "ttag_uncorr_": "ttagUncorr"
}



for sample in stackList:
    if sample == "DATA":
        inFile = TFile("%s/%s/workdir_AnalysisDNN_UL18_%s_sys_all/nominal/%s.root"%(inputDir,finalState,finalState,sample),"READ")
        data_obs =inFile.Get("DeltaY_reco_750_1000_muon_data/DeltaY").Clone("data_obs")
        combine_file.cd("DeltaY")
        data_obs.Write("data_obs")
    
    else:
        inFile = TFile("%s/%s/workdir_AnalysisDNN_UL18_%s_sys_all/nominal/%s.root"%(inputDir,finalState,finalState,sample),"READ")
        combine_file.mkdir("DeltaY/%s"%(sample))
        if sample == "TTbar":

        
            h_PP = inFile.Get("DeltaY_reco_SystVariations_P_P_750_1000_muon/DeltaY").Clone()
            h_PN = inFile.Get("DeltaY_reco_SystVariations_P_N_750_1000_muon/DeltaY").Clone()
            h_NP = inFile.Get("DeltaY_reco_SystVariations_N_P_750_1000_muon/DeltaY").Clone()
            h_NN = inFile.Get("DeltaY_reco_SystVariations_N_N_750_1000_muon/DeltaY").Clone()

            Matrix = TH2D("Matrix","", 2, -2.5, 2.5, 2, -2.5, 2.5)

            Matrix.SetBinContent(1, 1, h_NN.Integral())
            Matrix.SetBinContent(1, 2, h_PN.Integral())
            Matrix.SetBinContent(2, 1, h_NP.Integral())
            Matrix.SetBinContent(2, 2, h_PP.Integral())

            ProjX_1 = Matrix.ProjectionX("px1", 1, 1)
            ProjX_2 = Matrix.ProjectionX("px2", 2, 2)

            ProjX_1.GetXaxis().SetTitle("#Delta_Y_{reco}")
            ProjX_2.GetXaxis().SetTitle("#Delta_Y_{reco}")

            combine_file.cd("DeltaY/TTbar")
            ProjX_1.Write("TTbar_1")
            ProjX_2.Write("TTbar_2")

        else:
            nominal_hist = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY").Clone(sample)
            nominal_hist.Write(sample)
        for sys in systematic_name_mapping.keys():
            
            new_sys_name = systematic_name_mapping.get(sys, sys)
            sys_hist_up_name = "%s_%sUp" % (sample, new_sys_name)
            sys_hist_down_name = "%s_%sDown" % (sample, new_sys_name)
            sys_hist_none_name = "%s_%sNone" % (sample, new_sys_name)

            print sys	
        
            if "murmuf_up" in sys:
                sys_hist_up = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%sup"%(sys)).Clone(sys_hist_up_name)
                sys_hist_upnone = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%snone"%(sys)).Clone(sys_hist_none_name)
                sys_hist_up.Write(sys_hist_up_name)
                sys_hist_upnone.Write(sys_hist_none_name)
            elif "murmuf_down" in sys:
                sys_hist_downnone = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%snone"%(sys)).Clone(sys_hist_none_name)
                sys_hist_down = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%sdown"%(sys)).Clone(sys_hist_down_name)
                sys_hist_down.Write(sys_hist_down_name)
                sys_hist_downnone.Write(sys_hist_none_name)
            else:
                sys_hist_down = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%sdown"%(sys)).Clone(sys_hist_down_name)
                sys_hist_up = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%sup"%(sys)).Clone(sys_hist_up_name)
            
            if "murmuf_none" in sys:
                sys_hist_up.Write(sys_hist_up_name)
                sys_hist_down.Write(sys_hist_down_name)
            else:
                sys_hist_up.Write(sys_hist_up_name)
                sys_hist_down.Write(sys_hist_down_name)

combine_file.Close()
