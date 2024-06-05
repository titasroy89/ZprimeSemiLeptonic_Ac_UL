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

padRatio = 0.25
padOverlap = 0.15

padGap = 0.01
parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel",default="muon",type='str',
                  help="what channel?")
parser.add_option("-y", "--year", dest="year", default="UL17",type='str',
                  help="don't print status messages to stdout")
# parser.add_option("-eft", "--eft", dest="eft", action='store_false',type='str',
#                   help="print eft vars?")

(options, args) = parser.parse_args()
eft=False
channel = options.channel
year=options.year
# eft=options.eft
# eft=False
path="%s_%s"%(channel,year)
if os.path.exists(path):
	print("output directory exists")
else:
	os.mkdir(path)
if (channel=="electron" or channel=="muon"):
	# fileDir ="/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/{}/{}/workdir_AnalysisDNN_{}_{}_kinematics/nominal".format(year,channel,year,channel)
	fileDir ="/nfs/dust/cms/group/zprime-uhh/Analysis_UL17/muon"
else:
	fileDir ="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/%s/lepton/"%(year)

print(fileDir)

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
if year=="UL18":
	period=6
elif year=="UL17":
    	period=5
elif "2016" in year:
	period=4
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
# light_blue = TColor.GetColor(135, 206, 235)
# stackList_orig={"TTbar":[kRed],"WJets":[kGreen], "DY":[kYellow], "Diboson":[kOrange], "QCD":[light_blue],"ST":[kBlue]}
stackList_orig={"TTbar":[kRed],"WJets":[kGreen], "DY":[kGreen], "Diboson":[kGreen], "QCD":[kGreen],"ST":[kBlue]}

#stackList_orig=OrderedDict()

if eft:
	histograms={"DeltaY_reco_s2":["\DeltaY (t_{h}(p_T)<150 GeV,\Sigma \phi<0 )", "Events", 2, [-2.5,2.5]],
			"DeltaY_reco_s1":["\DeltaY (t_{h}(p_T)<150 GeV,\Sigma \phi>0 )", "Events", 2, [-2.5,2.5]],
			"DeltaY_reco_d2":["\DeltaY (t_{h}(p_T)<150 GeV,\Delta \phi<0 )", "Events", 2, [-2.5,2.5]],
			"DeltaY_reco_d1":["\DeltaY (t_{h}(p_T)<150 GeV,\Delta \phi>0 )", "Events", 2, [-2.5,2.5]],
			"DeltaY_reco_high":["\DeltaY (t_{h}(p_T)>150 GeV )", "Events", 2, [-2.5,2.5]],
			"DeltaY_reco_low":["\DeltaY (t_{h}(p_T)<150 GeV )", "Events", 2, [-2.5,2.5]],
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
bins_jetpt=[0.,20.,40.,60.,80.,100.,120.,140.,160.,180.,200.,220.,240.,260.,280.,300.,320.,340.,360.,380.,400.,420.,460.,500.,550.,600.,650.,700.,750.,800.,900.]
bins_mttbar=[0.,180.,360.,540.,720.,1000.,1500.,6000.]

histograms={
    # "DeltaY_reco":["\DeltaY ", "Events", 2, [-2.5,2.5]],
			# "M_Zprime":["M_{t#bar{t}} [GeV]", "Events", 280, [0, 6000]],
 			# "M_Zprime_rebin": ["M_{t#bar{t}} [GeV]","Events", 140, [0, 6000]],
 			# "M_Zprime_rebin2": ["M_{t#bar{t}} [GeV]","Events", 70, [0, 6000]],
			# "M_Zprime_rebin3": ["M_{t#bar{t}} [GeV]","Events", 35, [0, 6000],bins_mttbar,7],
			# "N_jets": ["N_{jets}","Events", 21, [-0.5, 20.5]],
			# "pt_jet1" :["p_{T}^{jet 1} [GeV]","Events", 45, [0, 900],bins_jetpt,30],
			# "deepjetbscore_jet1":["DeepJet b-tag score AK4 jet 1","Events", 20, [0, 1]],
			# "deepjetbscore_jet":["DeepJet b-tag score AK4 jets","Events", 20, [0, 1]],
			# "N_lep_charge":["Lepton charge ", "Events", 2, [-2.0,2.0]],
}

# sys.exit()
if channel=="muon" :
	histograms.update({
					#   "dRmin_mu_jet": ["#DeltaR_{min}(#mu, jet)","Events", 60, [0, 3]],
				    #   "pt_mu": ["Muon p_{T} [GeV]","Events",90,[ 0, 900]],
					#   "N_mu_charge":["Muon charge ", "Events", 2, [-1.0,1.0]],
       				"DeltaY_reco":["\DeltaY ", "Events", 2, [-2.5,2.5]],
					"N_lep_charge":["Lepton charge ", "Events", 2, [-2.0,2.0]],
					  })
elif(channel=="electron" ):
	histograms.update({
					  "dRmin_ele_jet": ["#DeltaR_{min}(e, jet)","Events", 60, [0, 3]],
				      "pt_ele": ["Electron p_{T} [GeV]","Events",90,[ 0, 900]],
					#   "N_ele_charge":["Electron charge ", "Events", 2, [-1.0,1.0]],
					   })
elif(channel=="lepton"):
	histograms.update({"dRmin_ele_jet": ["#DeltaR_{min}(e, jet)","Events", 60, [0, 3]],
				      "pt_ele": ["Electron p_{T} [GeV]","Events",90,[ 0, 900]],
					  "dRmin_mu_jet": ["#DeltaR_{min}(#mu, jet)","Events", 60, [0, 3]],
				      "pt_mu": ["Muon p_{T} [GeV]","Events",90,[ 0, 900]],
					   })

categories=["DNN_output0","DNN_output1","DNN_output2"]
# ,"Chi2_passes","Chi2_inverse"]

test_sample = ['TTbar','ST', 'WJets', 'DY', 'Diboson','QCD']
#for key in test_tuple: print(test_dict[key])
file={}
histo_={}
print("working from directory: ",fileDir)
#print(dict(stackList_orig))
if (channel=="muon" and year=="UL18"):
	hist_combined={}
	for cat in categories:
		hist_combined[cat]={}
		for sample in test_sample:
			hist_combined[cat][sample]=TH1F("hist_combined","hist_combined",36,1.,37.)

if (channel=="muon" and year=="UL18"):
	print("shouldnt be here")
	histos=["DeltaY_reco_d1","DeltaY_reco_d2","Sigma_phi_1","Sigma_phi_2"]
	for cat in categories:
		stack = THStack("hs","stack")
		legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
		legend.SetNColumns(2)
		legend.SetBorderSize(0)
		legend.SetFillColor(0)
		print(cat)
		for sample in test_sample:
			for histo in histos:
				file[sample] = TFile("%s/uhh2.AnalysisModuleRunner.MC.%s.root"%(fileDir,sample),"read")
				temp_hist="DNN_%s_General/%s"%(cat,histo)
				print(file[sample].Get(temp_hist))
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
				print("adding sample: ",sample)
				legend.AddEntry(hist_combined[cat][sample],"t#bar{t}",'f')
			elif sample=="WJets":
				print("adding sample: ",sample)
				legend.AddEntry(hist_combined[cat][sample],"W+jets + Others",'f')
			elif sample=="ST":
				print("adding sample: ",sample)
				legend.AddEntry(hist_combined[cat][sample],"ST",'f')
			# elif sample=="DY":
			# 	print("adding sample: ",sample)
			# 	legend.AddEntry(hist_combined[cat][sample],"DY",'f')
			# elif sample=="Diboson":
			# 	print("adding sample: ",sample)
			# 	legend.AddEntry(hist_combined[cat][sample],"Diboson",'f')			# print("going to stack")
			# elif sample=="QCD":
			# 	print("adding sample: ",sample)
			# 	legend.AddEntry(hist_combined[cat][sample],"QCD",'f')
			stack.Add(hist_combined[cat][sample])
			stack.SetMinimum(0.0)
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
		stack.Draw("HIST,SAME")
		log=0
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
		stack.Draw("HIST")
		stack.GetYaxis().SetRangeUser(0,2.5*maxVal)
		# legend.SetTextSize(0.05)
		# legend.Draw("SAME")
		errorban.Draw("E2,SAME")
		CMS_lumi.CMS_lumi(canvas, period, 11)
		if log:
			canvas.SaveAs("%s_%s/efthist_%s_log_AM.pdf"%(channel,year,cat))
		else:
			canvas.SaveAs("%s_%s/efthist_%s_linear_AM.pdf"%(channel,year,cat))
		canvas.Clear()
		pad2.cd()


# sys.exit()
file={}
histo={}





# Set Y-axis size adjustments
y_label_size = 0.04  # Decrease this value to make the labels smaller
y_title_size = 0.05  # Decrease this value to make the title smaller
y_title_offset = 1.2  # Adjust this value if needed

# Existing code setting up stackList_orig, histograms, etc.

for hist in histograms:
	print("hist is: ",hist)
	for cat in categories:
		if "Sigma" in hist or ("DeltaY_reco" in hist and "output0" in cat):
			print("this is ",cat)
			stack = THStack("hs","stack")
			legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
			legend.SetNColumns(2)
			legend.SetBorderSize(0)
			legend.SetFillColor(0)
			for sample in test_sample:
				file[sample] = TFile("%s/uhh2.AnalysisModuleRunner.MC.%s.root"%(fileDir,sample),"read")
				temp_hist="%s_General/%s"%(cat,hist)
				print(temp_hist, sample)
				histo[sample]=file[sample].Get(temp_hist)
				histo[sample].GetXaxis().SetRangeUser(histograms[hist][3][0],(histograms[hist][3][1]))
				histo[sample].SetFillColor(stackList_orig[sample][0])
				histo[sample].SetLineColor(stackList_orig[sample][0])
				print("sample is: ", sample)
				# print("with events: ", histo[sample].Integral())
				if sample=="TTbar":
					legend.AddEntry(histo[sample],"t#bar{t}",'f')
				elif sample=="WJets":
					legend.AddEntry(histo[sample],"W+jets + Others",'f')
				elif sample=="ST":
					legend.AddEntry(histo[sample],"ST",'f')
				# elif sample=="DY":
				# 	print("adding sample: ",sample)
				# 	legend.AddEntry(histo[cat][sample],"DYJets",'f')
				# elif sample=="Diboson":
				# 	print("adding sample: ",sample)
				# 	legend.AddEntry(histo[cat][sample],"Diboson",'f')
				# elif sample=="QCD":
				# 	print("adding sample: ",sample)
				# 	legend.AddEntry(histo[cat][sample],"QCD",'f')
				stack.Add(histo[sample])
				stack.SetMinimum(0.0)
			# print("maximum is: ",stack.GetMaximum())
			canvas.cd()
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
			stack.GetXaxis().SetTitle(histograms[hist][0])
			stack.GetYaxis().SetMaxDigits(4)
			stack.GetYaxis().SetRangeUser(0,2.5*maxVal)
			#stack.GetYaxis().SetMoreLogLabels()
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
				canvas.SaveAs("%s_%s/%s_%s_log_AM.pdf"%(channel,year,hist,cat))
			else:
				canvas.SaveAs("%s_%s/%s_%s_linear_AM.pdf"%(channel,year,hist,cat))
			canvas.Clear()
			pad2.cd()
	
	
	
	else:
		print("hist is: ",hist)
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
				histo[sample]=file[sample].Get(temp_hist)
				# print("histo[sample]", histo[sample])
				histo[sample].GetXaxis().SetRangeUser(histograms[hist][3][0],(histograms[hist][3][1]))
				histo[sample].SetFillColor(stackList_orig[sample][0])
				histo[sample].SetLineColor(stackList_orig[sample][0])
				if "M_Zprime_rebin3" in hist or "pt_jet1" in hist:
					# print(histograms[hist][5],histograms[hist][4])

					histo[sample]=histo[sample].Rebin(histograms[hist][5],"",array('d',histograms[hist][4]))
					
				if sample=="TTbar":
					legendR.AddEntry(histo[sample],"t#bar{t}",'f')
				elif sample=="WJets":
					legendR.AddEntry(histo[sample],"W+jets",'f')
				elif sample=="ST":
					legendR.AddEntry(histo[sample],"ST",'f')
				if "DeltaY" in hist:
					if ("output1" in cat or  "output2" in cat):
						print(sample, cat,histo[sample].GetBinContent(1),histo[sample].GetBinContent(2))
				
				stack.Add(histo[sample])
				stack.SetMinimum(0.0)
			file_data=TFile("%s/uhh2.AnalysisModuleRunner.DATA.DATA.root"%(fileDir),"read")
			# print(file_data)
			# print(temp_hist)
			dataHist=file_data.Get(temp_hist)
			if "M_Zprime_rebin3" in hist or "pt_jet1" in hist:
				# print(histograms[hist][5],histograms[hist][4])
				dataHist=dataHist.Rebin(histograms[hist][5],"",array('d',histograms[hist][4]))

			# print("data: ", dataHist.Integral())
			dataHist.SetMarkerColor(kBlack)
			dataHist.SetLineColor(kBlack)
			dataHist.SetYTitle(histograms[hist][1])     
			dataHist.Draw("pe,x0")
			stack.SetMinimum(0.)
			stack.Draw("HIST,SAME")

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
				

			maxVal =stack.GetMaximum()
			minVal = 1
			minVal = max(stack.GetStack()[0].GetMinimum(),1)
			log=0
			if log:
				stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
			else:
				stack.SetMaximum(2.3*maxVal)
			#stack.SetMinimum(minVal)
			stack.SetMinimum(0.0)

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

			pad1.Draw()
			pad2.Draw()

			pad1.cd()

			pad1.SetLogy(log)

			y2 = pad1.GetY2()

			stack.Draw("HIST")
			stack.GetXaxis().SetTitle('')
			stack.GetYaxis().SetTitle(dataHist.GetYaxis().GetTitle())

			stack.SetTitle('')
			stack.GetXaxis().SetLabelSize(0)
			stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(1.-padRatio+padOverlap))
			stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(1.-padRatio+padOverlap))
			stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(1.-padRatio+padOverlap))
			stack.GetYaxis().SetMaxDigits(4)
			stack.GetYaxis().SetTitle("Events")
			# stack.GetYaxis().SetRangeUser(0,1.7*maxVal)
			stack.SetMinimum(0.)
			dataHist.Draw("E,X0,SAME")

			errorban.Draw("E2,SAME")

			legendR.AddEntry(dataHist, "Data", 'pe')

			ratio = dataHist.Clone("temp")
			temp = stack.GetStack().Last().Clone("temp")

			for i_bin in range(1,temp.GetNbinsX()+1):
					temp.SetBinError(i_bin,0.)

			ratio = dataHist.Clone("temp")
			ratio.Divide(temp)
			ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
			ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize()/(padRatio+padOverlap))
			ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
			ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize()/(padRatio+padOverlap))
			ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset()*(padRatio+padOverlap-padGap))
			ratio.GetYaxis().SetRangeUser(0.3,1.7)
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
				canvasRatio.SaveAs("%s_%s/%s_%s_log_AM.pdf"%(channel,year,hist,cat))
			else:
				canvasRatio.SaveAs("%s_%s/%s_%s_linear_AM.pdf"%(channel,year,hist,cat))