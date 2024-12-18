import ROOT
import os
from numpy import log10

ROOT.gROOT.SetBatch(True)

systematic_name_mapping_muon = {
    "pu",
    "prefiringWeight",
    "muonID", 
    "muonTrigger",
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

systematic_name_mapping_electron = {
    "pu",
    "prefiringWeight",
    "eleID", 
    "eleTrigger",
    "eleReco",
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
    "pu",
    "prefiringWeight",
    "eleID", 
    "eleTrigger",
    "eleReco",
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

# Function to plot the systematics
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
    
    # Check for empty histograms
    if hist1.GetEntries() == 0 or hist2.GetEntries() == 0 or hist3.GetEntries() == 0:
        print("Warning: Empty histogram found for {sample}, {systematics}".format(sample, systematics))
        return
    
    hist1.SetLineColor(ROOT.kBlue)
    hist1.SetLineWidth(2)
    hist2.SetLineColor(ROOT.kRed)
    hist2.SetLineWidth(2)
    hist3.SetLineColor(ROOT.kOrange)
    hist3.SetLineWidth(2)

    max_value = max(hist1.GetMaximum(), hist2.GetMaximum(), hist3.GetMaximum())
    min_value = min(hist1.GetMinimum(), hist2.GetMinimum(), hist3.GetMinimum())
    
    # # For log scale, ensure min_value is positive
    # if min_value <= 0:
    #     min_value = 1e-3
    
    hist1.GetYaxis().SetRangeUser(min_value*0.7, max_value*1.1)
    
    canvas = ROOT.TCanvas("canvas", "Overlayed Histograms", 800, 600)
    # canvas.SetLogy()
    
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

# General function to handle both muon and electron systematics
def handle_systematics(file, output_dir, systematic_mapping, systematic_mapping_tt):
    for sample in samples:
        for systematics in systematic_mapping:
            systematics_plot(file, output_dir, sample, systematics)

    for sample in samples_tt:
        for systematics in systematic_mapping_tt:
            systematics_plot(file, output_dir, sample, systematics)

# Processing the input files
input_files = [f for f in os.listdir(input_directory) if f.endswith('.root')]

for input_file in input_files:
    file_path = os.path.join(input_directory, input_file)
    file = ROOT.TFile(file_path, "READ")
    
    output_dir = os.path.join(output_directory, os.path.splitext(input_file)[0])
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Run for muons
    if 'muon' in input_file:
        print("Muon file: ", input_file)
        handle_systematics(file, output_dir, systematic_name_mapping_muon, systematic_name_mapping_tt_muon)
    
    # Run for electrons
    elif 'ele' in input_file or 'electron' in input_file:
        print("Electron file: ", input_file)
        handle_systematics(file, output_dir, systematic_name_mapping_electron, systematic_name_mapping_tt_electron)
    
    file.Close()
