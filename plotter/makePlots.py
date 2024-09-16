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

#import cms_figure

padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel",default="muon",type='str',
                  help="what channel?")
parser.add_option("-y", "--year", dest="year", default="2018",type='str',
                  help="don't print status messages to stdout")
# parser.add_option("-eft", "--eft", dest="eft", action='store_false',type='str',
#                   help="print eft vars?")

(options, args) = parser.parse_args()
eft=False
channel = options.channel
year=options.year
# eft=options.eft
# eft=False
path="%s_%s_Plots_Sept"%(channel,year)
#if channel=="muon" and year=="2018":
#	path="muon_ext_2018"
print(path)
if os.path.exists(path):
	print("output directory exists")
else:
	os.mkdir(path)
if (channel=="electron" or channel=="muon"):
	#fileDir ="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/%s/%s/workdir_AnalysisDNN_%s_%s_dY/NOMINAL/"%(year,channel,year,channel)
        fileDir="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/%s/%s/workdir_AnalysisDNN_%s_%s//NOMINAL_Sept11/"%(year,channel,year, channel)
else:
	fileDir ="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/%s/lepton/"%(year)

# if channel=="muon" and year=="2018":
	# fileDir="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/muon/workdir_AnalysisDNN_2018_muonlow1/NOMINAL/"

print(fileDir)
print eft
#sys.exit()

gROOT.SetBatch(True)

YesLog = True
NoLog=False



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


#print stackList
if channel=="muon":
	_channelText = "#mu+jets"
elif(channel=="electron"):
	_channelText="e+jets"
elif(channel=="lepton"):
	_channelText="l+jets"


CMS_lumi.channelText = _channelText
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True
period=6
if year=="2018":
	period=6
elif year=="2017":
	period=5
elif "2016" in year:
	period=4
elif "all" in year:
	period=8
H = 600;
W = 800;


# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

stackList = { "TTbar":[kRed],"WJets":[kGreen], "ST":[kBlue]}

# SetOwnership(canvas, False)
# SetOwnership(canvasRatio, False)
# SetOwnership(pad1, False)
# SetOwnership(pad2, False)


legendHeightPer = 0.04
legList = stackList.keys() 
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

canvasRatio = TCanvas('c1Ratio','c1Ratio',W,H)
canvasRatio.SetFillColor(0)
canvasRatio.SetBorderMode(0)
canvasRatio.SetFrameFillStyle(0)
canvasRatio.SetFrameBorderMode(0)
canvasRatio.SetLeftMargin( L/W )
canvasRatio.SetRightMargin( R/W )
canvasRatio.SetTopMargin( T/H )
canvasRatio.SetBottomMargin( B/H )
canvasRatio.SetTickx(1)
canvasRatio.SetTicky(1)
canvasRatio.Draw()
canvasRatio.cd()


pad1 = TPad("zxc_p1","zxc_p1",0,padRatio-padOverlap,1,1)
pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
pad1.SetLeftMargin( L/W )
pad1.SetRightMargin( R/W )
pad1.SetTopMargin( T/H/(1-padRatio+padOverlap) )
pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
pad2.SetLeftMargin( L/W )
pad2.SetRightMargin( R/W )
pad2.SetTopMargin( (padOverlap)/(padRatio+padOverlap) )
pad2.SetBottomMargin( B/H/(padRatio+padOverlap) )
pad1.SetFillColor(0)
pad1.SetBorderMode(0)
pad1.SetFrameFillStyle(0)
pad1.SetFrameBorderMode(0)
pad1.SetTickx(1)
pad1.SetTicky(1)

pad2.SetFillColor(0)
pad2.SetFillStyle(4000)
pad2.SetBorderMode(0)
pad2.SetFrameFillStyle(0)
pad2.SetFrameBorderMode(0)
pad2.SetTickx(1)
pad2.SetTicky(1)


canvasRatio.cd()
pad1.Draw()
pad2.Draw()


canvas.cd()


canvas.ResetDrawn()

stackList_orig={"TTbar":[kRed],"WJets":[kGreen], "DYJets":[kGreen], "Diboson":[kGreen], "QCD":[kYellow],"ST":[kBlue],"ST_tW":[kBlue],"ST_s":[kBlue],"ST_t":[kBlue]}

#stackList_orig=OrderedDict()

# if eft:
histograms_eft={"DeltaY_reco":["\DeltaY ", "Events", 2, [-2.5,2.5]],
		"DeltaY_reco_s2":["\DeltaY (t_{h}(p_T)<150 GeV,\Sigma \phi<0 )", "Events", 2, [-2.5,2.5]],
		"DeltaY_reco_s1":["\DeltaY (t_{h}(p_T)<150 GeV,\Sigma \phi>0 )", "Events", 2, [-2.5,2.5]],
		"DeltaY_reco_d2":["\DeltaY (t_{h}(p_T)<150 GeV,\Delta \phi<0 )", "Events", 2, [-2.5,2.5]],
		"DeltaY_reco_d1":["\DeltaY (t_{h}(p_T)<150 GeV,\Delta \phi>0 )", "Events", 2, [-2.5,2.5]],
		"Delta_phi_high":["\DeltaY (t_{h}(p_T)>150 GeV )", "Events", 2, [-2.5,2.5]],
		"Delta_phi_low":["\DeltaY (t_{h}(p_T)<150 GeV )", "Events", 2, [-2.5,2.5]],
		"Sigma_phi":["\Sigma \phi", "Events", 16, [-3.2,3.2]],
		"Sigma_phi_high":["\Sigma \phi (top_{h}(p_{T})>150 GeV)", "Events", 16, [-3.2,3.2]],
		"Sigma_phi_low":["\Sigma \phi (top_{h}(p_{T})<150 GeV)", "Events", 16, [-3.2,3.2]],
		"Sigma_phi_1":["\Sigma \phi (top_{h}(p_{T})>150 GeV,\DeltaY > 0)", "Events", 16, [-3.2,3.2]],
		"Sigma_phi_2":["\Sigma \phi (top_{h}(p_{T})>150 GeV,\DeltaY < 0)", "Events", 16, [-3.2,3.2]],
		"Delta_phi":["\Delta \phi", "Events", 16, [-3.2,3.2]],
		"Delta_phi_high":["\Delta \phi (top_{h}(p_{T})>150 GeV)", "Events", 16, [-3.2,3.2]],
		"Delta_phi_low":["\Delta \phi (top_{h}(p_{T})<150 GeV)", "Events", 16, [-3.2,3.2]],
		"Delta_phi_1":["\Delta \phi (top_{h}(p_{T})>150 GeV,\DeltaY > 0)", "Events", 16, [-3.2,3.2]],
		"Delta_phi_2":["\Delta \phi (top_{h}(p_{T})>150 GeV,\DeltaY < 0)", "Events", 16, [-3.2,3.2]],
}
# bins_jetpt=[0.,20.,40.,60.,80.,100.,120.,140.,160.,180.,200.,220.,240.,260.,280.,300.,320.,340.,360.,380.,400.,420.,440.,460.,480.,500.,520.,.,750.,800.,900.]
bins_mttbar=[0.,180.,360.,540.,720.,1000.,1500.,6000.]
bins_mttbar_rebin=[]
bins_jetpt=[]
for i in range(0,900,20):
	bins_jetpt.append(float(i))
print(len(bins_jetpt))
# sys.exit()
for i in range(100,3501,50):
	bins_mttbar_rebin.append(float(i))
# bins_mttbar_rebin.append(3100.)
# bins_mttbar_rebin.append(3200.)
# bins_mttbar_rebin.append(3300.)
# bins_mttbar_rebin.append(3400.)
# bins_mttbar_rebin.append(3500.)


# print bins_mttbar_rebin
# # sys.exit()
# print(len(bins_mttbar_rebin))
histograms={ "M_Zprime":["M_{t#bar{t}} [GeV]", "Events", 160, [300, 3500]],
  	    "M_Zprime_rebin": ["M_{t#bar{t}} [GeV]","Events", 160, [250, 3500], bins_mttbar_rebin,len(bins_mttbar_rebin)-1],
  	    # "M_Zprime_rebin2": ["M_{t#bar{t}} [GeV]","Events", 70, [300, 3500]],
        # "M_Zprime_rebin3": ["M_{t#bar{t}} [GeV]","Events", 35, [0, 6000],bins_mttbar,7],
 	    # "DeltaY_reco":["\DeltaY ", "Events", 2, [-2.5,2.5]],
 	    # "N_jets": ["N_{jets}","Events", 9, [1.5, 10.5]],
 	    "pt_jet1" :["p_{T}^{jet 1} [GeV]","Events", 45, [0, 900],bins_jetpt,len(bins_jetpt)-1],
 	    # "deepjetbscore_jet1":["DeepJet b-tag score AK4 jet 1","Events", 20, [0, 1]],
 	    # "deepjetbscore_jet":["DeepJet b-tag score AK4 jets","Events", 20, [0, 1]],
 	    # "N_lep_charge":["Lepton charge ", "Events", 2, [-2.0,2.0]],
 }

# sys.exit()
if channel=="muon" :
 	histograms.update({
 					  "dRmin_mu1_jet": ["#DeltaR_{min}(#mu, jet)","Events", 60, [0, 3]],
					  "pt_mu1": ["Muon p_{T} [GeV]","Events",90,[ 0, 900]],
					#   "ptrel_mu1_jet":["p_{T}^{rel}(#mu, jet)","Events", 50, [0, 500]],
					#   "dRmin_ptrel_mu1":["p_{T}^{rel}(#mu1, jet) vs. #DeltaR_{min}(#mu1, jet)","Events",60,[ 0, 3], 50, [0, 500]],
					# #   "pt_mu_lowpt": ["Muon p_{T} [GeV]","Events",90,[ 0, 900]],
					#   "pt_mu_midpt": ["Muon p_{T} [GeV]","Events",90,[ 0, 900]],
					#   "N_mu_charge":["Electron charge ", "Events", 2, [-1.0,1.0]],
 					  })
# elif(channel=="electron" ):
#  	histograms.update({
#  					  "dRmin_ele1_jet": ["#DeltaR_{min}(e, jet)","Events", 60, [0, 3]],
#  				      "pt_ele1": ["Electron p_{T} [GeV]","Events",90,[ 0, 900]],
# 					#   "ptrel_ele1_jet":["p_{T}^{rel}(e, jet)","Events", 50, [0, 500]],
# 					#   "dRmin_ptrel_ele1":["p_{T}^{rel}(e1, jet) vs. #DeltaR_{min}(e1, jet)","Events",60,[ 0, 3], 50, [0, 500]],

# 					#   "pt_ele_lowpt": ["Electron p_{T} [GeV]","Events",90,[ 0, 900]],
# 					#   "pt_ele_midpt": ["Electron p_{T} [GeV]","Events",90,[ 0, 900]],
# 					#   "pt_ele_highpt": ["Electron p_{T} [GeV]","Events",90,[ 0, 900]],
# # 					#   "N_ele_charge":["Electron charge ", "Events", 2, [-1.0,1.0]],
#  					   })
# elif(channel=="lepton"):
# 	histograms.update({"dRmin_ele_jet": ["#DeltaR_{min}(e, jet)","Events", 60, [0, 3]],
# 				      "pt_ele": ["Electron p_{T} [GeV]","Events",90,[ 0, 900]],
# 					  "dRmin_mu_jet": ["#DeltaR_{min}(#mu, jet)","Events", 60, [0, 3]],
# 				      "pt_mu": ["Muon p_{T} [GeV]","Events",90,[ 0, 900]],
# 					   })

# categories=["Weights_TopTag_SF","TwoDCut_low1","TwoDCut_low1","DNN_output0","DNN_output1","DNN_output2","DNN_output0_TopTag","DNN_output0_NoTopTag"]
categories=["DNN_output0","DNN_output1","DNN_output2"]
# ,"DNN_output0_nochi2","DNN_output1","DNN_output1_chi2","DNN_output2_chi2","DNN_output2","DNN_output0_TopTag","DNN_output0_NoTopTag"]
# ,"Chi2_passes","Chi2_inverse"]

#test_sample = ['TTbar','ST_s','ST_t','ST_tW', 'WJets', 'DYJets', 'Diboson','QCD']
test_sample = ['TTbar','ST', 'WJets', 'DYJets', 'Diboson','QCD']
#for key in test_tuple: print(test_dict[key])
file={}
histo_={}


bins_Zprime7 = {0,400,600,800,1000,1200,1400,1600,1800,2000,2500,3000,3500,4000,5000}


print("working from directory: ",fileDir)
#print(dict(stackList_orig))
if (channel=="muon" and year=="2018"):
	hist_combined={}
	for cat in categories:
		hist_combined[cat]={}
		for sample in test_sample:
			hist_combined[cat][sample]=TH1F("hist_combined","hist_combined",36,1.,37.)

if ( channel=="muon" and year=="2019"):
	# print("checking eft vars")
	# histos=["DeltaY_reco_d1","DeltaY_reco_d2","Sigma_phi_1","Sigma_phi_2"]
	for cat in categories:
		stack = THStack("hs","stack")
		legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
		legend.SetNColumns(2)
		legend.SetBorderSize(0)
		legend.SetFillColor(0)
		# print(cat)
		for sample in test_sample:
			for histo in histograms:
				file[sample] = TFile("%s/uhh2.AnalysisModuleRunner.MC.%s.root"%(fileDir,sample),"read")
				temp_hist="%s_General/%s"%(cat,histo)
				print(file[sample].Get(temp_hist))
				print(temp_hist)  
				histo_[sample]=file[sample].Get(temp_hist)
				if histo=="DeltaY_reco_d1":
					for i in range(histo_[sample].GetNbinsX()):
						hist_combined[cat][sample].SetBinContent(1+i,histo_[sample].GetBinContent(i+1))
						hist_combined[cat][sample].SetBinError(1+i,histo_[sample].GetBinError(i+1))
				elif histo=="DeltaY_reco_d2":
					for i in range(histo_[sample].GetNbinsX()):
						hist_combined[cat][sample].SetBinContent(3+i,histo_[sample].GetBinContent(i+1))
						hist_combined[cat][sample].SetBinError(3+i,histo_[sample].GetBinError(i+1))
				elif histo=="Sigma_phi_1":
					for i in range(histo_[sample].GetNbinsX()):
						hist_combined[cat][sample].SetBinContent(5+i,histo_[sample].GetBinContent(i+1))	
						hist_combined[cat][sample].SetBinError(5+i,histo_[sample].GetBinError(i+1))	
				elif histo=="Sigma_phi_2":
					for i in range(histo_[sample].GetNbinsX()):
						hist_combined[cat][sample].SetBinContent(21+i,histo_[sample].GetBinContent(i+1))	
						hist_combined[cat][sample].SetBinError(21+i,histo_[sample].GetBinError(i+1))		
			hist_combined[cat][sample].SetFillColor(stackList_orig[sample][0])
			hist_combined[cat][sample].SetLineColor(stackList_orig[sample][0])	
			# hist_combined[cat][sample].GetXaxis().SetRangeUser(0,)	
			if sample=="TTbar":
				# print("adding sample: ",sample)
				legend.AddEntry(hist_combined[cat][sample],"t#bar{t}",'f')
			elif sample=="WJets":
				# print("adding sample: ",sample)
				legend.AddEntry(hist_combined[cat][sample],"W+jets",'f')
			elif sample=="ST":
				# print("adding sample: ",sample)
				legend.AddEntry(hist_combined[cat][sample],"ST",'f')
			# print("going to stack")
			stack.Add(hist_combined[cat][sample])
			# stack.SetMinimum(0.0)
		canvas.cd()
		canvas.ResetDrawn()
		canvas.Draw()
		canvas.cd()
		# canvas.SetLogy()
		errorban=stack.GetStack().Last().Clone("errorban")
		errorban.Sumw2()
		errorban.SetLineColor(kGray+2)
		errorban.SetFillColor(kGray+2)
		errorban.SetFillStyle(3245)
		errorban.SetMarkerSize(0)
		legend.AddEntry(errorban,"MC tot. unc.",'f')
		legend.SetTextSize(0.05)
		legend.Draw()
		
		log=1
		maxVal =stack.GetMaximum()
		minVal = max(stack.GetStack()[0].GetMinimum(),1)
		if log:
			# print("making log plots")
			stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
		else:
			# print("making linear plots")
			stack.SetMaximum(1.7*maxVal)
		# print("max is: ",maxVal )
		stack.SetMinimum(minVal)
		stack.Draw()
		stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
		stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
		stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
		stack.GetYaxis().SetTitle("Events")
		stack.GetXaxis().SetTitle("bins for fitting")
		stack.GetYaxis().SetMaxDigits(4)
		stack.GetYaxis().SetRangeUser(0,2.5*maxVal)
		
		stack.GetYaxis().SetRangeUser(0,2.5*maxVal)
		# legend.SetTextSize(0.05)
		# legend.Draw("SAME")
		errorban.Draw("E2,SAME")
		CMS_lumi.CMS_lumi(canvas, period, 11)
		if log:
			canvas.SaveAs("%s_%s/efthist_%s_log.pdf"%(channel,year,cat))
		else:
			canvas.SaveAs("%s_%s/efthist_%s_linear.pdf"%(channel,year,cat))
		canvas.Clear()
		pad2.cd()


# sys.exit()



file={}
histo={}

# Scale factors for Asimov post fits
SFs={"TTbar":[1-2.78e-11,1-2.48e-9],
    "WJets": [1-7.27e-12,1-2.49e-9],
	"ST": [1-2.54e-12,1-3.16e-9],
	}


print eft

if (eft):
	print("what???")
	for hist in histograms_eft:
		for cat in categories:
			# if "Sigma" in hist or ("DeltaY_reco" in hist and "output0" in cat):
			print("in here",cat)
			stack = THStack("hs","stack")
			legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
			legend.SetNColumns(2)
			legend.SetBorderSize(0)
			legend.SetFillColor(0)
			for sample in test_sample:
				file[sample] = TFile("%s/uhh2.AnalysisModuleRunner.MC.%s.root"%(fileDir,sample),"read")
				temp_hist="%s_General/%s"%(cat,hist)
				# print("%s/uhh2.AnalysisModuleRunner.MC.%s.root"%(fileDir,sample))
				# print(temp_hist, sample)
				histo[sample]=file[sample].Get(temp_hist)
				histo[sample].GetXaxis().SetRangeUser(histograms_eft[hist][3][0],(histograms_eft[hist][3][1]))
				if "dRmin_ptrel" in hist:
					histo[sample].GetXaxis().SetRangeUser(histograms_eft[hist][5][0],(histograms_eft[hist][5][1]))
				histo[sample].SetFillColor(stackList_orig[sample][0])
				histo[sample].SetLineColor(stackList_orig[sample][0])
				# print("sample is: ", sample)
				# print("with events: ", histo[sample].Integral())
				
				if sample=="TTbar":
					if channel=="ele":
						histo[sample].Scale(SFs[sample][0])
					else:
						histo[sample].Scale(SFs[sample][1])
					legend.AddEntry(histo[sample],"t#bar{t}",'f')
				elif sample=="WJets":
					if channel=="ele":
						histo[sample].Scale(SFs[sample][0])
					else:
						histo[sample].Scale(SFs[sample][1])
					legend.AddEntry(histo[sample],"Others",'f')
				elif sample=="ST":
					if channel=="ele":
						histo[sample].Scale(SFs[sample][0])
					else:
						histo[sample].Scale(SFs[sample][1])
					legend.AddEntry(histo[sample],"ST-s",'f')
				# elif sample=="ST_tW":
				# 	legend.AddEntry(histo[sample],"ST-tW",'f')
				# elif sample=="ST_t":
				# 	legend.AddEntry(histo[sample],"ST-t",'f')
				
				stack.Add(histo[sample])
				stack.SetMinimum(0.0)
			# print("maximum is: ",stack.GetMaximum())
			canvas.cd()
			if "dRmin_ptrel" in hist:
				stack.Draw("colz")
			else:
				stack.Draw("HIST")
			canvas.cd()
			canvas.ResetDrawn()
			# canvas.SetLogy()
			canvas.Draw()
			canvas.cd()
			errorban=stack.GetStack().Last().Clone("errorban")
			errorban.Sumw2()
			errorban.SetLineColor(kGray+2)
			errorban.SetFillColor(kGray+2)
			errorban.SetFillStyle(3245)
			errorban.SetMarkerSize(0)
			# errorban.Draw("E2,SAME")
			log=0
			legend.AddEntry(errorban,"MC tot. unc.",'f')
			maxVal =stack.GetMaximum()
			minVal = max(stack.GetStack()[0].GetMinimum(),1)
			# stack.GetYaxis().SetTitle(histograms[hist][1])
			if log:
				# print("making log plots")
				stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
			else:
				# print("making linear plots")
				stack.SetMaximum(1.7*maxVal)
			# print("max is: ",maxVal )
			stack.SetMinimum(minVal)
			#stack.GetXaxis().SetLabelSize(0)
			# stack.GetYaxis().SetRangeUser(1,10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
			stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
			stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
			stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
			stack.GetYaxis().SetTitle("Events")
			stack.GetXaxis().SetTitle(histograms_eft[hist][0])
			stack.GetYaxis().SetMaxDigits(4)
			stack.GetYaxis().SetRangeUser(0,2.5*maxVal)
			#stack.GetYaxis().SetMoreLogLabels()
			if "dRmin_ptrel" in hist:
				stack.Draw("colz")
			else:
				stack.Draw("HIST")
			# stack.Draw("HIST")stack.GetYaxis().SetRangeUser(1,10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
			stack.GetYaxis().SetRangeUser(0,2.5*maxVal)
			# stack.Draw("HIST")
			#pad1.cd()
			#pad1.Draw()
			#pad1.cd()
			#pad1.SetLogy(log)
			# stack.Draw("HIST")
			legend.SetTextSize(0.05)
			legend.Draw("SAME")
			errorban.Draw("E2,SAME")
			CMS_lumi.CMS_lumi(canvas, period, 11)
			# legend.SetTextSize(0.05)
			# legend.Draw("SAME")
			if log:
				canvas.SaveAs("%s/%s_%s_MConly_log.pdf"%(path,hist,cat))
			else:
				canvas.SaveAs("%s/%s_%s_MConly_linear.pdf"%(path,hist,cat))
			canvas.Clear()
			pad2.cd()
		
	
# sys.exit()	
for hist in histograms:
	for cat in categories:
		stack = THStack("hs","stack")
		legendR = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.)-0.1, legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
		legendR.SetNColumns(2)
		legendR.SetBorderSize(0)
		legendR.SetFillColorAlpha(0,0.35)
		for sample in test_sample:
			print("sample is: ", sample,cat,hist)
			file[sample] = TFile("%s/uhh2.AnalysisModuleRunner.MC.%s.root"%(fileDir,sample),"read")
			temp_hist="%s_General/%s"%(cat,hist)
			print(temp_hist)
			histo[sample]=file[sample].Get(temp_hist)
			if "N_jets" in hist:
				print("NJets hist: ",histograms[hist][3][0],histograms[hist][3][1])
			histo[sample].GetXaxis().SetRangeUser(histograms[hist][3][0],histograms[hist][3][1])
			if "dRmin_ptrel" in hist:
				histo[sample].GetYaxis().SetRangeUser(histograms[hist][5][0],histograms[hist][5][1])
			histo[sample].SetFillColor(stackList_orig[sample][0])
			histo[sample].SetLineColor(stackList_orig[sample][0])
			if "M_Zprime_rebin3" in hist or (hist=="M_Zprime_rebin") or "pt_jet1" in hist:
				# print(histograms[hist][5],histograms[hist][4])
				
				histo[sample]=histo[sample].Rebin(histograms[hist][5],"",array('d',histograms[hist][4]))
			
			if sample=="TTbar":
				# if channel=="ele":
				# 	histo[sample].Scale(SFs[sample][0])
				# else:
				# 	histo[sample].Scale(SFs[sample][1])
				legendR.AddEntry(histo[sample],"t#bar{t}",'f')
			elif sample=="WJets":
				# if channel=="ele":
				# 	histo[sample].Scale(SFs[sample][0])
				# else:
				# 	histo[sample].Scale(SFs[sample][1])
				legendR.AddEntry(histo[sample],"Others",'f')
			elif sample=="ST":
				# if channel=="ele":
				# 	histo[sample].Scale(SFs[sample][0])
				# else:
				# 	histo[sample].Scale(SFs[sample][1])
				legendR.AddEntry(histo[sample],"ST",'f')
			# elif sample=="QCD":
			#  	legendR.AddEntry(histo[sample],"QCD",'f')
			# elif sample=="ST_s":
			# 	legendR.AddEntry(histo[sample],"ST-s",'f')
			# elif sample=="ST_tW":
			# 	legendR.AddEntry(histo[sample],"ST-tW",'f')
			# elif sample=="ST_t":
			# 	legendR.AddEntry(histo[sample],"ST-t",'f')
			
			# if "DeltaY" in hist:
			# 	if ("output1" in cat or  "output2" in cat):
			# 		# print(sample, cat,histo[sample].GetBinContent(1),histo[sample].GetBinContent(2))
			
			stack.Add(histo[sample])
			stack.SetMinimum(0.0)
		file_data=TFile("%s/uhh2.AnalysisModuleRunner.DATA.DATA.root"%(fileDir),"read")
		# print(file_data)
		print(temp_hist)
		dataHist=file_data.Get(temp_hist)
		print("data: ",dataHist.GetBinContent(1),dataHist.GetBinContent(2))
		print(hist,cat,sample)
		dataHist.GetXaxis().SetRangeUser(histograms[hist][3][0],(histograms[hist][3][1]))
		if "M_Zprime_rebin3" in hist or (hist=="M_Zprime_rebin") or "pt_jet1" in hist:
			# print(histograms[hist][5],histograms[hist][4])
			dataHist=dataHist.Rebin(histograms[hist][5],"",array('d',histograms[hist][4]))

		# print("data: ", dataHist.Integral())
		dataHist.SetMarkerStyle(20)
		dataHist.SetMarkerColor(kBlack)
		dataHist.SetMarkerSize(0.8)
		dataHist.SetLineColor(kBlack)
		dataHist.SetYTitle(histograms[hist][1])     
		dataHist.Draw("pe,x0")
		stack.SetMinimum(0.)
		# stack.Draw("HIST,SAME")

		errorban=stack.GetStack().Last().Clone("errorban")
		errorban.Sumw2()
		errorban.SetLineColor(kGray+2)
		errorban.SetFillColor(kGray+2)
		errorban.SetFillStyle(3245)
		errorban.SetMarkerSize(0)
		errorban.Draw("E2,SAME")
		legendR.AddEntry(errorban,"MC tot. unc.",'f')

		oneLine = TF1("oneline","1",-9e9,9e9)
		oneLine.SetLineColor(kBlack)
		oneLine.SetLineWidth(1)
		oneLine.SetLineStyle(2)
			

		# maxVal =stack.GetMaximum()
		# minVal = 1
		minVal = max(stack.GetStack()[0].GetMinimum(),1)
		# if "Zprime" in hist:
		#	log=1
		# else:
		# 	log=0
		# if "N_jets" in hist:
		# 	log=0
		# else:
		log=0
		maxVal =stack.GetMaximum()
		minVal = max(stack.GetStack()[0].GetMinimum(),1)
			
		if log:
		
			stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
		else:
			
			stack.SetMaximum(2.1*maxVal)
		
		# stack.SetMinimum(minVal)
		# if log:
		# 	stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
		# else:
		# 	stack.SetMaximum(2.3*maxVal)
		stack.Draw("HIST")
		stack.GetXaxis().SetLabelSize(0)
		stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
		stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
		stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
		stack.GetYaxis().SetMaxDigits(5)
		stack.GetYaxis().SetTitle("Events")
		stack.SetMinimum(minVal)
		#stack.SetMinimum(minVal)
		# stack.SetMinimum(0.0)
		
		errorband=stack.GetStack().Last().Clone("error")
		errorband.Sumw2()
		errorband.SetLineColor(kBlack)
		errorband.SetFillColor(kBlack)
		errorband.SetFillStyle(3245)
		errorband.SetMarkerSize(0)
		errorband.SetLineColor(0)


		canvas.Clear()
		canvasRatio.cd()
		canvasRatio.ResetDrawn()
		canvasRatio.Draw()
		canvasRatio.cd()
		# log=1
		pad1.Draw()
		pad2.Draw()

		pad1.cd()
		pad1.SetLogy(log)
		if "dRmin_ptrel" in hist:
			stack.Draw("colz")
		else:
			stack.Draw("HIST")
		dataHist.Draw("E,X0,SAME")
		errorban.Draw("E2,SAME")
		# print("draw done")
		legendR.AddEntry(dataHist, "Data", 'pe')
		# pad1.SetLogy(1)
		ratio = dataHist.Clone("temp")
		temp = stack.GetStack().Last().Clone("temp")

		for i_bin in range(1,temp.GetNbinsX()+1):
				temp.SetBinError(i_bin,0.)

		ratio = dataHist.Clone("temp")
		ratio.Divide(temp)
		print("ratio: ", ratio.GetBinContent(1), ratio.GetBinContent(2))
		ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
		ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
		ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
		ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
		ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
		ratio.GetYaxis().SetRangeUser(0.2,1.8)
		ratio.GetYaxis().SetNdivisions(504)
		#print(histograms[hist])
		ratio.GetXaxis().SetTitle(histograms[hist][0])
		ratio.GetYaxis().SetTitle("Data/MC")
		CMS_lumi.CMS_lumi(pad1, period, 11)
		legendR.SetTextSize(0.05)
		legendR.Draw()
		pad2.cd()
		ratio.SetMarkerStyle(dataHist.GetMarkerStyle())
		ratio.SetMarkerSize(dataHist.GetMarkerSize())
		ratio.SetLineColor(kBlack)
		ratio.SetMarkerColor(kBlack)
		ratio.SetLineWidth(dataHist.GetLineWidth())
		ratio.Draw('e,x0')
		errorband.Divide(temp)
		# if "rebin2" in hist and "DNN_output0" in cat:
		#     for i in range(1, ratio.GetNbinsX() + 1):
				# print("bin, data, MC, ratio: " ,i, dataHist.GetBinContent(i), stack.GetStack().Last().GetBinContent(i), ratio.GetBinContent(i))



		for i in range(1, errorband.GetNbinsX() + 1):
			if(errorban.GetBinContent(i) == 0):
				errorband.SetBinError(i,0)
			else:
				errorband.SetBinError(i, errorban.GetBinError(i)/errorban.GetBinContent(i))

		errorband.Draw('e2,same')
		

		oneLine.Draw("same")
			
		canvasRatio.Update()
		canvasRatio.RedrawAxis()
		if log:
			canvasRatio.SaveAs("%s/%s_%s_log.pdf"%(path,hist,cat))
		else:
			canvasRatio.SaveAs("%s/%s_%s_linear.pdf"%(path,hist,cat))
