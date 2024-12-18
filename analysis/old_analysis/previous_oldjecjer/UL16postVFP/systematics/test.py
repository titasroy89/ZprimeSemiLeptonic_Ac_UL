import ROOT
import os
from numpy import log10

ROOT.gROOT.SetBatch(True)

# Systematics for muons
systematic_name_mapping_muon = {
    "pu",
    "prefiringWeight",
    "muonID", 
    "muonTrigger",
    "muonReco",
    "muonIso", 
    "btagCferr1", 
    "btagCferr2", 
    "btagHf",  
    "btagHfstats1",
    "btagHfstats2", 
    "btagLf", 
    "btagLfstats1",
    "btagLfstats2", 
    "ttagCorr", 
    "ttagUncorr", 
    "tmistag"
}

# Systematics for electrons
systematic_name_mapping_electron = {
    "pu",
    "prefiringWeight",
    "electronID", 
    "electronTrigger",
    "electronReco",
    "electronIso", 
    "btagCferr1", 
    "btagCferr2", 
    "btagHf",  
    "btagHfstats1",
    "btagHfstats2", 
    "btagLf", 
    "btagLfstats1",
    "btagLfstats2", 
    "ttagCorr", 
    "ttagUncorr", 
    "tmistag"
}

# Systematics for TT samples (muon)
systematic_name_mapping_tt_muon = {
    "muonReco",
    "pu",
    "prefiringWeight",
    "muonID", 
    "muonTrigger",
    "muonIso",
    "isr", 
    "fsr", 
    "btagCferr1", 
    "btagCferr2", 
    "btagHf",  
    "btagHfstats1",
    "btagHfstats2", 
    "btagLf", 
    "btagLfstats1",
    "btagLfstats2", 
    "ttagCorr", 
    "ttagUncorr", 
    "tmistag",
    "jec",
    "jer",
    "murmuf",
    "pdf"
}

# Systematics for TT samples (electron)
systematic_name_mapping_tt_electron = {
    "electronReco",
    "pu",
    "prefiringWeight",
    "electronID", 
    "electronTrigger",
    "electronIso",
    "isr", 
    "fsr", 
    "btagCferr1", 
    "btagCferr2", 
    "btagHf",  
    "btagHfstats1",
    "btagHfstats2", 
    "btagLf", 
    "btagLfstats1",
    "btagLfstats2", 
    "ttagCorr", 
    "ttagUncorr", 
    "tmistag",
    "jec",
    "jer",
    "murmuf",
    "pdf"
}

samples_tt = {"TTbar_1", "TTbar_2"}
samples = {"ST", "Others"}

input_directory = "../combine_input/individual_files"
output_directory = "output_plots"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

def systematics_plot(file, output_dir, sample, systematics):
    hist1_name = "{}_{}Up".format(sample, systematics)
    hist2_name = "{}_{}Down".format(sample, systematics)
    hist3_name = "{}".format(sample)
    hist1 = file.Get(hist1_name)
    hist2 = file.Get(hist2_name)
    hist3 = file.Get(hist3_name)
    print("Working on: ", sample, systematics)
    
    if not hist1 or not hist2 or not hist3:
        print("Error: Could not find one or more histograms for {}, {}".format(sample, systematics))
        return

    hist1.SetLineColor(ROOT.kBlue)
    hist1.SetLineWidth(2)
    hist2.SetLineColor(ROOT.kRed)
    hist2.SetLineWidth(2)
    hist3.SetLineColor(ROOT.kOrange)
    hist3.SetLineWidth(2)
    
    max_value = max(hist1.GetMaximum(), hist2.GetMaximum(), hist3.GetMaximum())
    min_value = min(hist1.GetMaximum(), hist2.GetMaximum(), hist3.GetMaximum())

    hist1.GetYaxis().SetRangeUser(min_value*0.7, max_value*1.1)

    canvas = ROOT.TCanvas("canvas", "Overlayed Histograms", 800, 600)
    canvas.SetLogy()

    hist1.Draw("HIST")
    hist2.Draw("HIST SAME")
    hist3.Draw("HIST SAME")

    legend = ROOT.TLegend(0.7, 0.8, 0.9, 0.9)
    legend.AddEntry(hist1, "{}_{}Up".format(sample, systematics), "l")
    legend.AddEntry(hist2, "{}_{}Down".format(sample, systematics), "l")
    legend.AddEntry(hist3, "{}".format(sample), "l")
    legend.Draw()

    canvas.Update()

    canvas.SaveAs(os.path.join(output_dir, "{}_{}.png".format(sample, systematics)))

input_files = [f for f in os.listdir(input_directory) if f.endswith('.root')]

for input_file in input_files:
    file_path = os.path.join(input_directory, input_file)
    file = ROOT.TFile(file_path, "READ")
    
    output_dir = os.path.join(output_directory, os.path.splitext(input_file)[0])
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    if 'muon' in input_file:
        # Run for muons
        for sample in samples:
            for systematics in systematic_name_mapping_muon:
                systematics_plot(file, output_dir, sample, systematics)

        for sample in samples_tt:
            for systematics in systematic_name_mapping_tt_muon:
                systematics_plot(file, output_dir, sample, systematics)
    
    elif 'ele' in input_file or 'electron' in input_file:
        # Run for electrons
        for sample in samples:
            for systematics in systematic_name_mapping_electron:
                systematics_plot(file, output_dir, sample, systematics)

        for sample in samples_tt:
            for systematics in systematic_name_mapping_tt_electron:
                systematics_plot(file, output_dir, sample, systematics)
    
    file.Close()
