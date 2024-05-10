import ROOT
import math
from numpy import log10

ROOT.gROOT.SetBatch(True)

systematic_name_mapping = {
    # "muonReco",
    # "pu",
    # "prefiringWeight",
    # "muonID", 
    # "muonTrigger",
    # "muonReco",
    # "muonIso",
    # "isr", 
    # "fsr", 
    # "btagCferr1", 
    # "btagCferr2", 
    # "btagHf",  
    # "btagHfstats1",
    # "btagHfstats2", 
    # "btagLf", 
    # "btagLfstats1",
    # "btagLfstats2", 
    # "ttagCorr", 
    # "ttagUncorr", 
    # "tmistag",
    "jec",
    "jer",
    "murmuf",
    "pdf"
    
}

file = ROOT.TFile("dY_UL18_muon_500_750.root", "READ")

def systematics_plot(region, sample, systematics):
    hist1_name = "{}/{}_{}Up".format(region, sample, systematics)
    hist2_name = "{}/{}_{}Down".format(region, sample, systematics)
    hist3_name = "{}/{}".format(region, sample)
    hist1 = file.Get(hist1_name)
    hist2 = file.Get(hist2_name)
    hist3 = file.Get(hist3_name)
    print("Working on: ", sample, region, systematics)


    hist1.SetLineColor(ROOT.kBlue)
    hist1.SetLineWidth(2)
    hist2.SetLineColor(ROOT.kRed)
    hist2.SetLineWidth(2)
    hist3.SetLineColor(ROOT.kOrange)
    hist3.SetLineWidth(2)
    
    max_value = max(hist1.GetMaximum(), hist2.GetMaximum(), hist3.GetMaximum())
    min_value = min(hist1.GetMaximum(), hist2.GetMaximum(), hist3.GetMaximum())
    # print(max_value)
    
    # hist1.GetYaxis().SetRangeUser(min_value*0.7, max_value*1.1)
    # hist1.GetYaxis().SetRangeUser(0,10**(1.5*log10(max_value) - 0.5*log10(min_value)))

    canvas = ROOT.TCanvas("canvas", "Overlayed Histograms", 800, 600)
    canvas.SetLogy()

    hist1.Draw("HIST")
    hist2.Draw("HIST SAME")
    hist3.Draw("HIST SAME")

    legend = ROOT.TLegend(0.7, 0.8, 0.9, 0.9)
    legend.AddEntry(hist1, "{}_{}_{}Up".format(region, sample, systematics, "l"))
    legend.AddEntry(hist2, "{}_{}_{}Down".format(region, sample, systematics), "l")
    legend.AddEntry(hist3, "{}_{}".format(region, sample), "l")
    legend.Draw()

    canvas.Update()

    canvas.SaveAs("{}_{}_{}.png".format(region, sample, systematics))

regions = {"SR", "CR1", "CR2"}
# samples = {"TTbar_1", "TTbar_2", "ST", "Others"}
samples = {"TTbar_1", "TTbar_2"}

for sample in samples:
    for region in regions:
        for systematics in systematic_name_mapping:
            systematics_plot(region, sample, systematics)


file.Close()
