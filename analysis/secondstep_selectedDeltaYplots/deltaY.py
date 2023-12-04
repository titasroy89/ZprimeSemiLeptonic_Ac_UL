#! /usr/bin/env python
from ROOT import *
import ROOT
import sys
import numpy

# As an input, Higgs Combine takes a txt based file containing the observed and expected yields.


# list of DeltaY ROOT files 
input_files = {
    "DeltaY_UL18_muon_750_900_TTbar.root": "TTbar", 
    } 
input_files2 = {
    "DeltaY_UL18_muon_750_900_WJets.root": "WJets",
    "DeltaY_UL18_muon_750_900_ST.root": "ST",
    "DeltaY_UL18_muon_750_900_DATA.root": "data_obs",
    "DeltaY_UL18_muon_750_900_Diboson.root": "Diboson",
    "DeltaY_UL18_muon_750_900_DY.root": "DY",
    "DeltaY_UL18_muon_750_900_QCD.root": "QCD",
    }


# Output ROOT file
output_file = ROOT.TFile("DeltaY_UL18_muon_750_900.root", "RECREATE")

#in this following function, my aim is to loop through each bin of the histograms and get the bin content and calculate the weighted histograms for up and down variation with these values. 

def apply_scale_factor(hist, scale_factor_hist, operation):
    
    # iterate through each bin of the histogram. bin numbering in root starts from 1.
    # .GetNbinsX() - number of bins on the x-axis. +1 at the end is for adding the last bin.
    for i in range(1, hist.GetNbinsX() + 1):  
        #GetBinContent(i) gets the value of the bin i from histogram hist
        bin_content = hist.GetBinContent(i)
        bin_error = hist.GetBinError(i)
        scale_factor = scale_factor_hist.GetBinContent(i)
        # hist.SetBinContent(i, bin_content*scale_factor)
        # hist.SetBinError(i, bin_error*scale_factor)
        if operation == "add":
            #hist.SetBinContent(bin(int),content). this is used to set the value of a bin in the hist. 
            hist.SetBinContent(i, bin_content + bin_content*scale_factor)
            hist.SetBinError(i, bin_error + bin_error*scale_factor)
        elif operation == "subtract":
            hist.SetBinContent(i, bin_content - bin_content*scale_factor)
            hist.SetBinError(i, bin_error - bin_error*scale_factor) 

    return hist

# Next step is to loop over the input root files and create the histograms that will be saved to combine root file

for input_file_name,histogram_name in input_files.items():
    
    root_file = ROOT.TFile(input_file_name, "READ")

    hist1 = root_file.Get("px1")
    hist2 = root_file.Get("px2")
    scale_factor_hist_up = root_file.Get("weight_pu_up")
    scale_factor_hist_down = root_file.Get("weight_pu_down")

    if hist1:
        # The Clone() method creates a copy of the histogram. One can save multiple histograms with the same name from different input files in the same output file.
        # Clone the histogram and give it a different name
        output_file.cd()
        hist_clone_nominal = hist1.Clone(histogram_name + "_1")
        # Writing the histogram to the output file
        hist_clone_nominal.Write()
        if scale_factor_hist_up:
            
            hist1_up = apply_scale_factor(hist1.Clone(), scale_factor_hist_up, "add")
            hist_clone_up = hist1_up.Clone(histogram_name + "_1_puUp")
            hist_clone_up.Write()
        if scale_factor_hist_down:
            hist1_down = apply_scale_factor(hist1.Clone(), scale_factor_hist_down, "subtract")
            hist_clone_down = hist1_down.Clone(histogram_name + "_1_puDown")
            hist_clone_down.Write()
        
    
    if hist2:
        # The Clone() method creates a copy of the histogram. One can save multiple histograms with the same name from different input files in the same output file.
        # Clone the histogram and give it a different name
        output_file.cd()
        hist_clone_nominal = hist2.Clone(histogram_name + "_2")
        hist_clone_nominal.Write()
        
        if scale_factor_hist_up:
            hist2_up = apply_scale_factor(hist2.Clone(), scale_factor_hist_up, "add")
            hist_clone_up = hist2_up.Clone(histogram_name + "_2_puUp")
            hist_clone_up.Write()
        if scale_factor_hist_down:
            hist2_down = apply_scale_factor(hist2.Clone(), scale_factor_hist_down, "subtract")
            hist_clone_down = hist2_down.Clone(histogram_name + "_2_pu_down")
            hist_clone_down.Write()
        
    root_file.Close()
    
for input_file_name2,histogram_name in input_files2.items():
    
    root_file = ROOT.TFile(input_file_name2, "READ")

    # Getting DeltaY histogram from the file
    hist3 = root_file.Get("DeltaY_reco_mass")
    
    scale_factor_hist_up = root_file.Get("weight_pu_up")  
    scale_factor_hist_down = root_file.Get("weight_pu_down")
    
    if hist3:
        output_file.cd()
        hist_clone_nominal = hist3.Clone(histogram_name)
        hist_clone_nominal.Write()
        
        if scale_factor_hist_up:
            hist3_up = apply_scale_factor(hist3.Clone(), scale_factor_hist_up, "add")
            hist_clone_up = hist3_up.Clone(histogram_name + "_pu_up")
            hist_clone_up.Write()
        if scale_factor_hist_down:
            hist3_down = apply_scale_factor(hist3.Clone(), scale_factor_hist_down, "subtract")
            hist_clone_down = hist3_down.Clone(histogram_name + "_pu_down")
            hist_clone_down.Write()
        
    root_file.Close()
    


# Close the output file
output_file.Close()
