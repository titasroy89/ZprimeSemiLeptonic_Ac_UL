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

systematics = {"mu_reco_", "pu_", "prefiring_", "mu_id_", "mu_trigger_", "ele_id_", "ele_trigger_", "ele_reco_",
               "murmuf_up", "murmuf_none", "murmuf_down", "isr_", "fsr_", "btag_cferr1_", "btag_hf_", "btag_hfstats1_",
               "btag_hfstats2_", "btag_lf_", "btag_lfstats1_", "btag_lfstats2_", "ttag_corr_", "ttag_uncorr_"}

for sample in stackList:
    if sample == "DATA":
        inFile = TFile("%s/%s/workdir_AnalysisDNN_UL18_%s_sys_all/nominal/%s.root"%(inputDir,finalState,finalState,sample),"READ")
        data_obs =inFile.Get("DeltaY_reco_750_1000_muon_data/DeltaY").Clone("data_obs")
        combine_file.cd("DeltaY")
        data_obs.Write("data_obs")
    
    elif sample == "TTbar":
        inFile = TFile("%s/%s/workdir_AnalysisDNN_UL18_%s_sys_all/nominal/%s.root"%(inputDir,finalState,finalState,sample),"READ")
		
        combine_file.mkdir("DeltaY/%s"%(sample))
        
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
        inFile = TFile("%s/%s/workdir_AnalysisDNN_UL18_%s_sys_all/nominal/%s.root"%(inputDir,finalState,finalState,sample),"READ")
        nominal_hist=inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY").Clone("nominal")
        combine_file.mkdir("DeltaY/%s"%(sample))
        combine_file.cd("DeltaY/%s"%(sample))
        nominal_hist.Write("%s_nominal"%(sample))
        for sys in systematics:
            print sys	
            if "murmuf_up" in sys:
                sys_hist_up = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%sup"%(sys)).Clone("%s_up"%(sys))
                sys_hist_upnone = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%snone"%(sys)).Clone("%s_none"%(sys))
                sys_hist_up.Write("%s_%s_up"%(sample,sys))
                sys_hist_upnone.Write("%s_%s_none"%(sample,sys))
            elif "murmuf_down" in sys:
                sys_hist_downnone = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%snone"%(sys)).Clone("%s_none"%(sys))
                sys_hist_down = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%sdown"%(sys)).Clone("%s_down"%(sys))
                sys_hist_down.Write("%s_%s_down"%(sample,sys))
                sys_hist_downnone.Write("%s_%s_none"%(sample,sys))
            else:
                sys_hist_down = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%sdown"%(sys)).Clone("%s_down"%(sys))
                sys_hist_up = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY_%sup"%(sys)).Clone("%s_up"%(sys))
            
            if "murmuf_none" in sys:
                sys_hist_up.Write("%s_%s_up"%(sample,sys))
                sys_hist_down.Write("%s_%s_down"%(sample,sys))
            else:
                sys_hist_up.Write("%s_%sup"%(sample,sys))
                sys_hist_down.Write("%s_%sdown"%(sample,sys))

combine_file.Close()
