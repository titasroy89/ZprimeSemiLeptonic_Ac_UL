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
parser.add_option("-y", "--year", dest="year", default="2018",type='str',
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
channel = options.channel
year=options.year
path="%s_%s"%(channel,year)
if os.path.exists(path):
	print("output directory exists")
else:
	os.mkdir(path)
if (channel=="electron" or channel=="muon"):
	fileDir ="/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/%s/%s/workdir_AnalysisDNN_%s_%s_dY/NOMINAL_eft/"%(year,channel,year,channel)
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
if year=="2018":
	period=6
elif year=="2017":
	period=5
elif year=="2016pre" or year=="2016post" or year=="2016_post_pre_added" :
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

stackList_orig={"TTbar":[kRed],"WJets":[kGreen], "DYJets":[kGreen], "Diboson":[kGreen], "QCD":[kGreen],"ST":[kBlue]}

#stackList_orig=OrderedDict()
histograms={"DeltaY_reco":["\DeltaY ", "Events", 2, [-2.5,2.5]],
			"DeltaY_reco_s2":["\DeltaY (t_{h}(p_T)<150 GeV,\Sigma \phi<0 )", "Events", 2, [-2.5,2.5]],
			"DeltaY_reco_s1":["\DeltaY (t_{h}(p_T)<150 GeV,\Sigma \phi>0 )", "Events", 2, [-2.5,2.5]],
			"DeltaY_reco_d2":["\DeltaY (t_{h}(p_T)<150 GeV,\Delta \phi<0 )", "Events", 2, [-2.5,2.5]],
			"DeltaY_reco_d1":["\DeltaY (t_{h}(p_T)<150 GeV,\Delta \phi>0 )", "Events", 2, [-2.5,2.5]],
			"Sigma_phi":["\Sigma \phi", "Events", 16, [-3.2,3.2]],
			"Sigma_phi_high":["\Sigma \phi (top_{h}(p_T)>150 GeV)", "Events", 16, [-3.2,3.2]],
			"Sigma_phi_low":["\Sigma \phi (top_{h}(p_T)<150 GeV)", "Events", 16, [-3.2,3.2]],
			"Sigma_phi_1":["\Sigma \phi (top_{h}(p_T)>150 GeV,\DeltaY > 0)", "Events", 16, [-3.2,3.2]],
			"Sigma_phi_2":["\Sigma \phi (top_{h}(p_T)>150 GeV,\DeltaY < 0)", "Events", 16, [-3.2,3.2]],
			"Delta_phi":["\Delta \phi", "Events", 16, [-3.2,3.2]],
			"Delta_phi_high":["\Delta \phi (top_{h}(p_T)>150 GeV)", "Events", 16, [-3.2,3.2]],
			"Delta_phi_low":["\Delta \phi (top_{h}(p_T)<150 GeV)", "Events", 16, [-3.2,3.2]],
			"Delta_phi_1":["\Delta \phi (top_{h}(p_T)>150 GeV,\DeltaY > 0)", "Events", 16, [-3.2,3.2]],
			"Delta_phi_2":["\Delta \phi (top_{h}(p_T)>150 GeV,\DeltaY < 0)", "Events", 16, [-3.2,3.2]],
			"M_Zprime":["M_{t#bar{t}} [GeV]", "Events", 280, [0, 6000]],
 			"M_Zprime_rebin": ["M_{t#bar{t}} [GeV]","Events", 140, [0, 6000]],
 			"M_Zprime_rebin2": ["M_{t#bar{t}} [GeV]","Events", 70, [0, 6000]],
			"M_Zprime_rebin3": ["M_{t#bar{t}} [GeV]","Events", 35, [0, 6000]],
			"N_jets": ["N_{jets}","Events", 21, [-0.5, 20.5]],
			"pt_jet1" :["p_{T}^{jet 1} [GeV]","Events", 45, [0, 900]],
}
if channel=="muon" or channel=="lepton":
	histograms.update({"dRmin_mu_jet": ["#DeltaR_{min}(#mu, jet)","Events", 60, [0, 3]],
				      "pt_mu": ["Muon p_{T} [GeV]","Events",90,[ 0, 900]]
					  })
else:
	histograms.update({"dRmin_ele_jet": ["#DeltaR_{min}(e, jet)","Events", 60, [0, 3]],
				      "pt_ele": ["Electron p_{T} [GeV]","Events",90,[ 0, 900]]
					   })
categories=["output0","output1","output2"]
test_sample = ('ST', 'WJets', 'DYJets', 'Diboson','QCD','TTbar')
#for key in test_tuple: print(test_dict[key])
file={}
histo_={}
print("working from directory: ",fileDir)
#print(dict(stackList_orig))

hist_combined={}
for cat in categories:
	hist_combined[cat]={}
	for sample in test_sample:
		hist_combined[cat][sample]=TH1F("hist_combined","hist_combined",36,1.,37.)
histos=["DeltaY_reco_1","DeltaY_reco_2","Sigma_phi_1","Sigma_phi_2"]
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
			if histo=="DeltaY_reco_1":
				for i in range(histo_[sample].GetNbinsX()):
					hist_combined[cat][sample].SetBinContent(1+i,histo_[sample].GetBinContent(i+1))
					hist_combined[cat][sample].SetBinError(1+i,histo_[sample].GetBinError(i+1))
			elif histo=="DeltaY_reco_2":
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
		if sample=="TTbar":
			print("adding sample: ",sample)
			legend.AddEntry(hist_combined[cat][sample],"t#bar{t}",'f')
		elif sample=="WJets":
			print("adding sample: ",sample)
			legend.AddEntry(hist_combined[cat][sample],"W+jets",'f')
		elif sample=="ST":
			print("adding sample: ",sample)
			legend.AddEntry(hist_combined[cat][sample],"ST",'f')
		print("going to stack")
		stack.Add(hist_combined[cat][sample])

	legend.SetTextSize(0.05)
	legend.Draw("SAME")
	canvas.cd()
	stack.Draw("HIST")
	canvas.cd()
	canvas.ResetDrawn()
	canvas.Draw()
	canvas.cd()
	errorban=stack.GetStack().Last().Clone("errorban")
	errorban.Sumw2()
	errorban.SetLineColor(kGray+2)
	errorban.SetFillColor(kGray+2)
	errorban.SetFillStyle(3245)
	errorban.SetMarkerSize(0)
	legend.AddEntry(errorban,"MC tot. unc.",'f')
	legend.SetTextSize(0.05)
	legend.Draw("SAME")
	log=0
	maxVal =stack.GetMaximum()
	minVal = max(stack.GetStack()[0].GetMinimum(),1)
	if log:
		print("making log plots")
		stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
	else:
		print("making linear plots")
		stack.SetMaximum(1.7*maxVal)
	print("max is: ",maxVal )
	stack.SetMinimum(minVal)
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
		canvas.SaveAs("%s_%s/efthist_%s_log.pdf"%(channel,year,cat))
	else:
		canvas.SaveAs("%s_%s/efthist_%s_linear.pdf"%(channel,year,cat))
	canvas.Clear()
	pad2.cd()


# sys.exit()
file={}
histo={}







for hist in histograms:
	if "Delta" in hist or "Sigma" in hist: 
		print("hist is DeltaY")
		for cat in categories:
			print("this is ",cat)
			stack = THStack("hs","stack")
			legend = TLegend(2*legendStart - legendEnd , 0.99 - (T/H)/(1.-padRatio+padOverlap) - legendHeightPer/(1.-padRatio+padOverlap)*round((len(legList)+1)/2.), legendEnd, 0.99-(T/H)/(1.-padRatio+padOverlap))
			legend.SetNColumns(2)
			legend.SetBorderSize(0)
			legend.SetFillColor(0)
			for sample in test_sample:
				file[sample] = TFile("%s/uhh2.AnalysisModuleRunner.MC.%s.root"%(fileDir,sample),"read")
				temp_hist="DNN_%s_General/%s"%(cat,hist)
				histo[sample]=file[sample].Get(temp_hist)
				histo[sample].GetXaxis().SetRangeUser(histograms[hist][3][0],(histograms[hist][3][1]))
				histo[sample].SetFillColor(stackList_orig[sample][0])
				histo[sample].SetLineColor(stackList_orig[sample][0])
				print("sample is: ", sample)
				print("with events: ", histo[sample].Integral())
				if sample=="TTbar":
					legend.AddEntry(histo[sample],"t#bar{t}",'f')
				elif sample=="WJets":
					legend.AddEntry(histo[sample],"W+jets",'f')
				elif sample=="ST":
					legend.AddEntry(histo[sample],"ST",'f')
				stack.Add(histo[sample])
			print("maximum is: ",stack.GetMaximum())
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
				print("making log plots")
				stack.SetMaximum(10**(1.5*log10(maxVal) - 0.5*log10(minVal)))
			else:
				print("making linear plots")
				stack.SetMaximum(1.7*maxVal)
			print("max is: ",maxVal )
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
				canvas.SaveAs("%s_%s/%s_%s_log.pdf"%(channel,year,hist,cat))
			else:
				canvas.SaveAs("%s_%s/%s_%s_linear.pdf"%(channel,year,hist,cat))
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
				print("sample is: ", sample)
				file[sample] = TFile("%s/uhh2.AnalysisModuleRunner.MC.%s.root"%(fileDir,sample),"read")
				temp_hist="DNN_%s_General/%s"%(cat,hist)
				histo[sample]=file[sample].Get(temp_hist)
				histo[sample].GetXaxis().SetRangeUser(histograms[hist][3][0],(histograms[hist][3][1]))				
				histo[sample].SetFillColor(stackList_orig[sample][0])
				histo[sample].SetLineColor(stackList_orig[sample][0])
				if sample=="TTbar":
					legendR.AddEntry(histo[sample],"t#bar{t}",'f')
				elif sample=="WJets":
					legendR.AddEntry(histo[sample],"W+jets",'f')
				elif sample=="ST":
					legendR.AddEntry(histo[sample],"ST",'f')
				
				stack.Add(histo[sample])
			file_data=TFile("%s/uhh2.AnalysisModuleRunner.DATA.DATA.root"%(fileDir),"read")
			print(file_data)
			print(temp_hist)
			dataHist=file_data.Get(temp_hist)

			print("data: ", dataHist.Integral())
			dataHist.SetMarkerColor(kBlack)
			dataHist.SetLineColor(kBlack)
			dataHist.SetYTitle(histograms[hist][1])     
			dataHist.Draw("pe,x0")
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
				stack.SetMaximum(1.7*maxVal)
			stack.SetMinimum(minVal)

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
				canvasRatio.SaveAs("%s_%s/%s_%s_log.pdf"%(channel,year,hist,cat))
			else:
				canvasRatio.SaveAs("%s_%s/%s_%s_linear.pdf"%(channel,year,hist,cat))
