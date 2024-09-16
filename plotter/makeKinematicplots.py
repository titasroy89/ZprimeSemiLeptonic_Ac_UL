from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, gROOT, gStyle, kRed, kGreen, kBlue, kGray, kBlack, TObject, TColor
from optparse import OptionParser
from numpy import log10
from array import array
import os

padRatio = 0.25
padOverlap = 0.15
padGap = 0.01

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel", default="muon", type='str', help="What channel?")
parser.add_option("-y", "--year", dest="year", default="UL17", type='str', help="Year of data")

(options, args) = parser.parse_args()
channel = options.channel
year = options.year

# Define analysis and preselection runs
analysis_runs = ["UL16", "UL17", "UL18","all"]
preselection_runs = ["Preselection_UL16", "Preselection_UL17", "Preselection_UL18"]

# Determine run type based on the year
if year in analysis_runs:
    run_type = "analysis"
elif year in preselection_runs:
    run_type = "preselection"
else:
    raise ValueError("Year must be one of the defined analysis or preselection runs")

# Create output directory if it doesn't exist
path = "%s_%s" % (channel, year)
if not os.path.exists(path):
    os.mkdir(path)

# Set the file directory based on the run type
if channel in ["electron", "muon"]:
    if run_type == "analysis":
        fileDir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/{year}/{channel}/workdir_AnalysisDNN_{year}_{channel}_chargecheck/nominal".format(year=year, channel=channel)
    elif run_type == "preselection":
        fileDir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/{year}/Preselection/workdir_Preselection_{year}_chargecheck/nominal".format(year=year)
else:
    fileDir = "/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/%s/lepton/"%(year)

print(fileDir)

gROOT.SetBatch(True)

# ========================= CMS Style =====================
import CMS_lumi
from Style import *

thestyle = Style()

HasCMSStyle = False
style = None
if os.path.isfile('tdrstyle.C'):
    ROOT.gROOT.ProcessLine('.L tdrstyle.C')
    ROOT.setTDRStyle()
    HasCMSStyle = True
    if os.path.isfile('CMSTopStyle.cc'):
        gROOT.ProcessLine('.L CMSTopStyle.cc+')
        style = CMSTopStyle()
        style.setupICHEPv1()
if not HasCMSStyle:
    thestyle.SetStyle()

ROOT.gROOT.ForceStyle()

_channelText = "#mu+jets" if channel == "muon" else "e+jets" if channel == "electron" else "l+jets"
CMS_lumi.channelText = _channelText
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True

period = 6 if year == "UL18" else 5 if year == "UL17" else 4 if "UL16" in year else 6

H = 600
W = 800
T = 0.08 * H
B = 0.12 * H
L = 0.12 * W
R = 0.1 * W

stackList = {"TTbar": [kRed], "WJets": [kGreen], "ST": [kBlue]}
stackList_orig = {"TTbar": [kRed], "WJets": [kGreen], "DYJets": [kGreen], "Diboson": [kGreen], "QCD": [kGreen], "ST": [kBlue]}

legendHeightPer = 0.04
legendStart = 0.69
legendEnd = 0.97 - (R / W)

legList = stackList.keys()

canvas = TCanvas('c1', 'c1', W, H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin(L / W)
canvas.SetRightMargin(R / W)
canvas.SetTopMargin(T / H)
canvas.SetBottomMargin(B / H)
canvas.SetTickx(1)

canvasRatio = TCanvas('c1Ratio', 'c1Ratio', W, H)
canvasRatio.SetFillColor(0)
canvasRatio.SetBorderMode(0)
canvasRatio.SetFrameFillStyle(0)
canvasRatio.SetFrameBorderMode(0)
canvasRatio.SetLeftMargin(L / W)
canvasRatio.SetRightMargin(R / W)
canvasRatio.SetTopMargin(T / H)
canvasRatio.SetBottomMargin(B / H)
canvasRatio.SetTickx(1)
canvasRatio.SetTicky(1)
canvasRatio.Draw()
canvasRatio.cd()

pad1 = TPad("zxc_p1", "zxc_p1", 0, padRatio - padOverlap, 1, 1)
pad2 = TPad("qwe_p2", "qwe_p2", 0, 0, 1, padRatio + padOverlap)
pad1.SetLeftMargin(L / W)
pad1.SetRightMargin(R / W)
pad1.SetTopMargin(T / H / (1 - padRatio + padOverlap))
pad1.SetBottomMargin((padOverlap + padGap) / (1 - padRatio + padOverlap))
pad1.SetFillColor(0)
pad1.SetTickx(1)
pad1.SetTicky(1)

pad2.SetLeftMargin(L / W)
pad2.SetRightMargin(R / W)
pad2.SetTopMargin(padOverlap / (padRatio + padOverlap))
pad2.SetBottomMargin(B / H / (padRatio + padOverlap))
pad2.SetFillColor(0)
pad2.SetFillStyle(4000)
pad2.SetTickx(1)
pad2.SetTicky(1)

canvasRatio.cd()
pad1.Draw()
pad2.Draw()
# ========================= CMS Style =====================
histograms={
    		"DeltaY_reco":["\DeltaY ", "Events", 2, [-2.5,2.5]],
			# "M_Zprime":["M_{t#bar{t}} [GeV]", "Events", 280, [0, 6000]],
 			# "M_Zprime_rebin": ["M_{t#bar{t}} [GeV]","Events", 140, [0, 6000]],
 			# "M_Zprime_rebin2": ["M_{t#bar{t}} [GeV]","Events", 70, [0, 6000]],
			# "M_Zprime_rebin3": ["M_{t#bar{t}} [GeV]","Events", 35, [0, 6000],bins_mttbar,7],
			# "N_jets": ["N_{jets}","Events", 21, [-0.5, 20.5]],
			# "pt_jet1" :["p_{T}^{jet 1} [GeV]","Events", 45, [0, 900],bins_jetpt,30],
			# "deepjetbscore_jet1":["DeepJet b-tag score AK4 jet 1","Events", 20, [0, 1]],
			# "deepjetbscore_jet":["DeepJet b-tag score AK4 jets","Events", 20, [0, 1]],
			"N_lep_charge":["Lepton charge ", "Events", 2, [-2.0,2.0]],
}

if channel == "muon":
    histograms.update({
        "N_mu_charge": ["Muon charge ", "Events", 2, [-1.0, 1.0]],
    })

elif channel == "electron":
    histograms.update({
        "N_ele_charge": ["Electron charge ", "Events", 2, [-1.0, 1.0]],
    })

elif channel == "lepton":
    histograms.update({
        "dRmin_ele_jet": ["#DeltaR_{min}(e, jet)", "Events", 60, [0, 3]],
        "pt_ele": ["Electron p_{T} [GeV]", "Events", 90, [0, 900]],
        "dRmin_mu_jet": ["#DeltaR_{min}(#mu, jet)", "Events", 60, [0, 3]],
        "pt_mu": ["Muon p_{T} [GeV]", "Events", 90, [0, 900]],
    })

categories = ["Input", "MET"] if run_type == "preselection" else ["Weights_Init", "AfterBaseline", "AfterChi2", "DNN_output0", "DNN_output1", "DNN_output2"]
test_sample = ['TTbar', 'ST', 'WJets', 'DYJets', 'Diboson', 'QCD']

file = {}
histo = {}

print("Working from directory: ", fileDir)

for hist in histograms:
    print("hist is: ", hist)
    for cat in categories:
        stack = THStack("hs", "stack")
        legendR = TLegend(2 * legendStart - legendEnd, 0.99 - (T / H) / (1. - padRatio + padOverlap) - legendHeightPer / (1. - padRatio + padOverlap) * round((len(legList) + 1) / 2.) - 0.1, legendEnd, 0.99 - (T / H) / (1. - padRatio + padOverlap))
        legendR.SetNColumns(2)
        legendR.SetBorderSize(0)
        legendR.SetFillColorAlpha(0, 0.35)

        for sample in test_sample:
            print("sample is: ", sample, cat, hist)
            file[sample] = TFile("%s/uhh2.AnalysisModuleRunner.MC.%s.root" % (fileDir, sample), "read")
            temp_hist = "%s_General/%s" % (cat, hist)
            histo[sample] = file[sample].Get(temp_hist)

            if not histo[sample] or not histo[sample].InheritsFrom("TH1"):
                print("WARNING! Histogram %s for sample %s does not exist or is not a TH1 object" % (temp_hist, sample))
                continue

            histo[sample].GetXaxis().SetRangeUser(histograms[hist][3][0], histograms[hist][3][1])
            histo[sample].SetFillColor(stackList_orig[sample][0])
            histo[sample].SetLineColor(stackList_orig[sample][0])

            if sample == "TTbar":
                legendR.AddEntry(histo[sample], "t#bar{t}", 'f')
            elif sample == "WJets":
                legendR.AddEntry(histo[sample], "W+jets", 'f')
            elif sample == "ST":
                legendR.AddEntry(histo[sample], "ST", 'f')

            stack.Add(histo[sample])
            stack.SetMinimum(0.0)

        file_data = TFile("%s/uhh2.AnalysisModuleRunner.DATA.DATA.root" % fileDir, "read")
        dataHist = file_data.Get(temp_hist)

        if not dataHist or not dataHist.InheritsFrom("TH1"):
            print("Warning: Histogram %s for data does not exist or is not a TH1 object" % temp_hist)
            continue

        dataHist.SetMarkerColor(kBlack)
        dataHist.SetLineColor(kBlack)
        dataHist.SetYTitle(histograms[hist][1])
        dataHist.Draw("pe,x0")
        stack.SetMinimum(0.0)
        stack.Draw("HIST,SAME")

        errorban = stack.GetStack().Last().Clone("errorban")
        errorban.Sumw2()
        errorban.SetLineColor(kGray + 2)
        errorban.SetFillColor(kGray + 2)
        errorban.SetFillStyle(3245)
        errorban.SetMarkerSize(0)
        errorban.Draw("E2,SAME")
        legendR.AddEntry(errorban, "MC tot. unc.", 'f')

        oneLine = TF1("oneline", "1", -9e9, 9e9)
        oneLine.SetLineColor(kBlack)
        oneLine.SetLineWidth(1)
        oneLine.SetLineStyle(2)

        maxVal = stack.GetMaximum()
        minVal = max(stack.GetStack()[0].GetMinimum(), 1)
        log = 0
        if log:
            stack.SetMaximum(10**(1.5 * log10(maxVal) - 0.5 * log10(minVal)))
        else:
            stack.SetMaximum(2.3 * maxVal)
        stack.SetMinimum(0.0)

        errorband = stack.GetStack().Last().Clone("error")
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

        stack.Draw("HIST")
        stack.GetXaxis().SetTitle('')
        stack.GetYaxis().SetTitle(dataHist.GetYaxis().GetTitle())
        stack.SetTitle('')
        stack.GetXaxis().SetLabelSize(0)
        stack.GetYaxis().SetLabelSize(gStyle.GetLabelSize() / (1. - padRatio + padOverlap))
        stack.GetYaxis().SetTitleSize(gStyle.GetTitleSize() / (1. - padRatio + padOverlap))
        stack.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset() * (1. - padRatio + padOverlap))
        stack.GetYaxis().SetMaxDigits(4)
        stack.GetYaxis().SetTitle("Events")
        stack.SetMinimum(0.0)
        dataHist.Draw("E,X0,SAME")

        errorban.Draw("E2,SAME")
        legendR.AddEntry(dataHist, "Data", 'pe')

        ratio = dataHist.Clone("temp")
        temp = stack.GetStack().Last().Clone("temp")
        for i_bin in range(1, temp.GetNbinsX() + 1):
            temp.SetBinError(i_bin, 0.)
        ratio.Divide(temp)
        ratio.GetXaxis().SetLabelSize(gStyle.GetLabelSize() / (padRatio + padOverlap))
        ratio.GetYaxis().SetLabelSize(gStyle.GetLabelSize() / (padRatio + padOverlap))
        ratio.GetXaxis().SetTitleSize(gStyle.GetTitleSize() / (padRatio + padOverlap))
        ratio.GetYaxis().SetTitleSize(gStyle.GetTitleSize() / (padRatio + padOverlap))
        ratio.GetYaxis().SetTitleOffset(gStyle.GetTitleYOffset() * (padRatio + padOverlap - padGap))
        ratio.GetYaxis().SetRangeUser(0.3, 1.7)
        ratio.GetYaxis().SetNdivisions(504)
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
            if errorban.GetBinContent(i) == 0:
                errorband.SetBinError(i, 0)
            else:
                errorband.SetBinError(i, errorban.GetBinError(i) / errorban.GetBinContent(i))
        errorband.Draw('e2,same')
        oneLine.Draw("same")
        canvasRatio.Update()
        canvasRatio.RedrawAxis()
        if log:
            canvasRatio.SaveAs("%s_%s/%s_%s_log_AM.pdf" % (channel, year, hist, cat))
        else:
            canvasRatio.SaveAs("%s_%s/%s_%s_linear_AM.pdf" % (channel, year, hist, cat))
