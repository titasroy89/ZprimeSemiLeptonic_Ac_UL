from ROOT import *
import os
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="muon",type='str',
                     help="Specify which channel Mu or Ele? default is Mu" )


(options, args) = parser.parse_args()

finalState = options.channel
inputDir="/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/"
stackList= {"Wjets","DY","ST","Diboson","QCD","DATA"}
Mttbar="0_500"
combine_file = TFile('DY_%s_%s.root'%(finalState,Mttbar),'RECREATE')

systematics ={"mu_reco_","pu_","prefiring_","mu_id_","mu_trigger_","ele_id_","ele_trigger_","ele_reco_","murmuf_up","murmuf_none","murmuf_down","isr_","fsr_","btag_cferr1_","btag_hf_","btag_hfstats1_","btag_hfstats2_","btag_lf_","btag_lfstats1_","btag_lfstats2_","ttag_corr_","ttag_uncorr_"}
for sample in stackList:
	combine_file.mkdir("DeltaY")

	if sample=="DATA":
		inFile = TFile("/nfs/dust/cms/user/titasroy/Ac_UL/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/uhh2.AnalysisModuleRunner.DATA.SingleMuon.root","READ")
		data_obs =inFile.Get("DeltaY_reco_SystVariations_0_500_muon/DeltaY").Clone("data_obs")
		combine_file.cd("DeltaY")
		data_obs.Write("data_obs")
	else:
		inFile = TFile("%s/%s/workdir_AnalysisDNN_UL18_%s_sys/nominal/%s.root"%(inputDir,finalState,finalState,sample),"READ")
		nominal_hist=inFile.Get("DeltaY_reco_SystVariations_0_500_muon/DeltaY").Clone("nominal")
                combine_file.mkdir("DeltaY/%s"%(sample))
                combine_file.cd("DeltaY/%s"%(sample))
		nominal_hist.Write("%s_nominal"%(sample))
		for sys in systematics:
			print sys	
		#	print "DeltaY_reco_SystVariations_0_500_muon/DeltaY_%sup"%(sys)
                 #       print "DeltaY_reco_SystVariations_0_500_muon/DeltaY_%sdown"%(sys) 
			if "murmuf_up" in sys:
				 sys_hist_up = inFile.Get("DeltaY_reco_SystVariations_0_500_muon/DeltaY_%sup"%(sys)).Clone("%s_up"%(sys))
				 sys_hist_upnone = inFile.Get("DeltaY_reco_SystVariations_0_500_muon/DeltaY_%snone"%(sys)).Clone("%s_none"%(sys))
				 sys_hist_up.Write("%s_%s_up"%(sample,sys))
				 sys_hist_upnone.Write("%s_%s_none"%(sample,sys))
			elif "murmuf_down" in sys:
				sys_hist_downnone = inFile.Get("DeltaY_reco_SystVariations_0_500_muon/DeltaY_%snone"%(sys)).Clone("%s_none"%(sys))
				sys_hist_down = inFile.Get("DeltaY_reco_SystVariations_0_500_muon/DeltaY_%sdown"%(sys)).Clone("%s_down"%(sys))
				sys_hist_down.Write("%s_%s_down"%(sample,sys))
				sys_hist_downnone.Write("%s_%s_none"%(sample,sys))
                        else:
	        		sys_hist_down = inFile.Get("DeltaY_reco_SystVariations_0_500_muon/DeltaY_%sdown"%(sys)).Clone("%s_down"%(sys))
				sys_hist_up = inFile.Get("DeltaY_reco_SystVariations_0_500_muon/DeltaY_%sup"%(sys)).Clone("%s_up"%(sys))
			if "murmuf_none" in sys:
				 sys_hist_up.Write("%s_%s_up"%(sample,sys))
				 sys_hist_down.Write("%s_%s_down"%(sample,sys))
			else:
				sys_hist_up.Write("%s_%sup"%(sample,sys))
				sys_hist_down.Write("%s_%sdown"%(sample,sys))
	
combine_file.Close()	
