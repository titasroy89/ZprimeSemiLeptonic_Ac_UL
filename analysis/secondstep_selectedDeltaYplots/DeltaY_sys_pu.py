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
    "DeltaY_UL18_muon_750_900_Diboson.root": "Diboson",
    "DeltaY_UL18_muon_750_900_DY.root": "DY",
    "DeltaY_UL18_muon_750_900_QCD.root": "QCD",
    }
input_files3 = {
    "DeltaY_UL18_muon_750_900_DATA.root": "data_obs" }


# Output ROOT file
output_file = ROOT.TFile("DeltaY_UL18_muon_750_900.root", "RECREATE")

#in this following function, my aim is to loop through each bin of the histograms and get the bin content and calculate the weighted histograms for up and down variation with these values. 



# Next step is to loop over the input root files and create the histograms that will be saved to combine root file

for input_file_name,histogram_name in input_files.items():
        
    root_file = ROOT.TFile(input_file_name, "READ")

    hist1 = root_file.Get("px1")
    hist2 = root_file.Get("px2")
    scale_factor_hist = root_file.Get("weight_pu")
    scale_factor_hist_up = root_file.Get("weight_pu_up")
    scale_factor_hist_down = root_file.Get("weight_pu_down")
    
    scale_factor_hist_mean = scale_factor_hist.GetMean()
    scale_factor_hist_up_mean = scale_factor_hist_up.GetMean()
    scale_factor_hist_down_mean = scale_factor_hist_down.GetMean()
    

    if hist1:
        
        # The Clone() method creates a copy of the histogram. One can save multiple histograms with the same name from different input files in the same output file.
        # Clone the histogram and give it a different name
        output_file.cd()
        
        hist1_nominal = hist1.Clone(histogram_name + "_1")
        hist1_nominal.Scale(scale_factor_hist_mean)
        hist1_nominal.Write()
        
        hist1_up = hist1.Clone(histogram_name + "_1_puUp")
        hist1_up.Scale(scale_factor_hist_up_mean)
        hist1_up.Write()
        
        hist1_down = hist1.Clone(histogram_name + "_1_puDown")
        hist1_down.Scale(scale_factor_hist_down_mean)
        hist1_down.Write()
    
    if hist2:
        # The Clone() method creates a copy of the histogram. One can save multiple histograms with the same name from different input files in the same output file.
        # Clone the histogram and give it a different name
        output_file.cd()
        
        hist2_nominal = hist2.Clone(histogram_name + "_2")
        hist2_nominal.Scale(scale_factor_hist_mean)
        hist2_nominal.Write()
       
        hist2_up = hist2.Clone(histogram_name + "_2_puUp")
        hist2_up.Scale(scale_factor_hist_up_mean)
        hist2_up.Write()
        
        hist2_down = hist2.Clone(histogram_name + "_2_puDown")
        hist2_down.Scale(scale_factor_hist_down_mean)
        hist2_down.Write()
        
    root_file.Close()
    
for input_file_name2,histogram_name in input_files2.items():
    
    root_file = ROOT.TFile(input_file_name2, "READ")
    
  
    # Getting DeltaY histogram from the file
    hist3 = root_file.Get("DeltaY_reco_mass")
    
    scale_factor_hist = root_file.Get("weight_pu")
    scale_factor_hist_up = root_file.Get("weight_pu_up")
    scale_factor_hist_down = root_file.Get("weight_pu_down")
    
    scale_factor_hist_mean = scale_factor_hist.GetMean()
    scale_factor_hist_up_mean = scale_factor_hist_up.GetMean()
    scale_factor_hist_down_mean = scale_factor_hist_down.GetMean()

    
    if hist3:
        output_file.cd()
      
        hist3_nominal = hist3.Clone(histogram_name)
        hist3_nominal.Scale(scale_factor_hist_mean)
        hist3_nominal.Write()
       
        hist3_up = hist3.Clone(histogram_name + "_puUp")
        hist3_up.Scale(scale_factor_hist_up_mean)
        hist3_up.Write()
        
        hist3_down = hist3.Clone(histogram_name + "_puDown")
        hist3_down.Scale(scale_factor_hist_down_mean)
        hist3_down.Write()
        
    root_file.Close()
    
for input_file_name3,histogram_name in input_files3.items():
    
    root_file = ROOT.TFile(input_file_name3, "READ")
  
    # Getting DeltaY histogram from the file
    hist4 = root_file.Get("DeltaY_reco_mass")

    if hist4:
        output_file.cd()
      
        hist4_nominal = hist4.Clone(histogram_name)
        hist4_nominal.Write()
        
    root_file.Close()

# Close the output file
output_file.Close()
