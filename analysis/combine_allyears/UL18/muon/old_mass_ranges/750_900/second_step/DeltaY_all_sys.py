#! /usr/bin/env python
from ROOT import *
import ROOT
import sys
import numpy

# As an input, Higgs Combine takes a txt based file containing the observed and expected yields.

# list of DeltaY ROOT files 
input_files = {
    "dY_UL18_muon_750_900_TTbar.root": "TTbar", 
    } 
input_files2 = {
    "dY_UL18_muon_750_900_WJets.root": "WJets",
    "dY_UL18_muon_750_900_ST.root": "ST",
    "dY_UL18_muon_750_900_Diboson.root": "Diboson",
    "dY_UL18_muon_750_900_DY.root": "DY",
    "dY_UL18_muon_750_900_QCD.root": "QCD",
    }
input_files3 = {
    "dY_UL18_muon_750_900_DATA.root": "data_obs" }


# Output ROOT file
output_file = ROOT.TFile("dY_UL18_muon_750_900.root", "RECREATE")

#in this following function, my aim is to loop through each bin of the histograms and get the bin content and calculate the weighted histograms for up and down variation with these values. 

# add scale factors HERE !!
scale_factors_nominal = [
    "weight_pu",
    "weight_sfelec_id",
    "weight_sfelec_reco",
    "weight_sfmu_id",
    "weight_sfmu_trigger",
    "prefiringWeight",
    "weight_btagdisc_central"
]

scale_factors_up = {
    "weight_pu_up" : "puUp",
    "weight_sfelec_id_up" : "elecIDUp",
    "weight_sfelec_reco_up": "elecRecoUp",
    "weight_sfmu_id_up" : "muonIDUp",
    "weight_sfmu_trigger_up" : "muonTriggerUp",
    "prefiringWeightUp" : "prefiringWeightUp"
    
}

scale_factors_up_division = {
    "weight_pu_up" : "weight_pu",
    "weight_sfelec_id_up" : "weight_sfelec_id",
    "weight_sfelec_reco_up": "weight_sfelec_reco",
    "weight_sfmu_id_up" : "weight_sfmu_id",
    "weight_sfmu_trigger_up" : "weight_sfmu_trigger",
    "prefiringWeightUp" : "prefiringWeight"
    
}

scale_factors_down = {
    "weight_pu_down" : "puDown",
    "weight_sfelec_id_down" : "elecIDDown",
    "weight_sfelec_reco_down": "elecRecoDown",
    "weight_sfmu_id_down" : "muonIDDown",
    "weight_sfmu_trigger_down" : "muonTriggerDown",
    "prefiringWeightDown" : "prefiringWeightDown"
    
}

scale_factors_down_division = {
    "weight_pu_down" : "weight_pu",
    "weight_sfelec_id_down" : "weight_sfelec_id",
    "weight_sfelec_reco_down": "weight_sfelec_reco",
    "weight_sfmu_id_down" : "weight_sfmu_id",
    "weight_sfmu_trigger_down" : "weight_sfmu_trigger",
    "prefiringWeightDown" : "prefiringWeight"
    
}


# Next step is to loop over the input root files and create the histograms that will be saved to combine root file

for input_file_name,histogram_name in input_files.items():
        
    root_file = ROOT.TFile(input_file_name, "READ")

    hist1 = root_file.Get("px1")
    hist2 = root_file.Get("px2")
    
    # scale_factor_hist = root_file.Get("weight_pu")
    # scale_factor_hist_up = root_file.Get("weight_pu_up")
    # scale_factor_hist_down = root_file.Get("weight_pu_down")
    
    # scale_factor_hist_mean = scale_factor_hist.GetMean()
    # scale_factor_hist_up_mean = scale_factor_hist_up.GetMean()
    # scale_factor_hist_down_mean = scale_factor_hist_down.GetMean()
    

    if hist1:
        
        # The Clone() method creates a copy of the histogram. One can save multiple histograms with the same name from different input files in the same output file.
        # Clone the histogram and give it a different name
        output_file.cd()
        
        hist1_org = hist1.Clone(histogram_name + "_1_original")
        hist1_org.Write()
        hist1_nominal = hist1.Clone(histogram_name + "_1")

        for sf in scale_factors_nominal:
            scale_factor_hist_nominal = root_file.Get(sf)
            scale_factor_hist_nominal_mean = scale_factor_hist_nominal.GetMean()
            
            hist1_nominal.Scale(scale_factor_hist_nominal_mean)
        
        hist1_nominal.Write()
            
        for sf,name in scale_factors_up.items():
            scale_factor_hist_up = root_file.Get(sf)
            
            scale_factor_hist_up_mean = scale_factor_hist_up.GetMean()
            
            scale_factor_hist_up_div = root_file.Get(scale_factors_up_division[sf])
            
            scale_factor_hist_up_div_mean = 1/scale_factor_hist_up_div.GetMean()
            
            final_SF = scale_factor_hist_up_mean * scale_factor_hist_up_div_mean
            
            hist1_up = hist1_nominal.Clone(histogram_name + "_1_" + name)
            hist1_up.Scale(final_SF)
            hist1_up.Write()
            
        for sf,name in scale_factors_down.items():
            scale_factor_hist_down = root_file.Get(sf)
            scale_factor_hist_down_mean = scale_factor_hist_down.GetMean()
            
            scale_factor_hist_down_div = root_file.Get(scale_factors_down_division[sf])
            scale_factor_hist_down_div_mean = 1/scale_factor_hist_down_div.GetMean()
            final_SF = scale_factor_hist_down_mean * scale_factor_hist_down_div_mean
        
            hist1_down = hist1_nominal.Clone(histogram_name + "_1_" + name)
            hist1_down.Scale(scale_factor_hist_down_mean)
            hist1_down.Write()
    
    if hist2:
        # The Clone() method creates a copy of the histogram. One can save multiple histograms with the same name from different input files in the same output file.
        # Clone the histogram and give it a different name
        output_file.cd()
        
        hist2_org = hist2.Clone(histogram_name + "_2_original")
        hist2_org.Write()
        hist2_nominal = hist2.Clone(histogram_name + "_2")
        
        for sf in scale_factors_nominal:
            scale_factor_hist_nominal = root_file.Get(sf)
            scale_factor_hist_nominal_mean = scale_factor_hist_nominal.GetMean()
            
            hist2_nominal.Scale(scale_factor_hist_nominal_mean)
        
        hist2_nominal.Write()
    
            
        for sf,name in scale_factors_up.items():
            scale_factor_hist_up = root_file.Get(sf)
            scale_factor_hist_up_mean = scale_factor_hist_up.GetMean()
            
            scale_factor_hist_up_div = root_file.Get(scale_factors_up_division[sf])
            scale_factor_hist_up_div_mean = 1/scale_factor_hist_up_div.GetMean()
            final_SF = scale_factor_hist_up_mean * scale_factor_hist_up_div_mean
            
            hist2_up = hist2_nominal.Clone(histogram_name + "_2_" + name)
            hist2_up.Scale(final_SF)
            hist2_up.Write()
        
        for sf,name in scale_factors_down.items():
            scale_factor_hist_down = root_file.Get(sf)
            scale_factor_hist_down_mean = scale_factor_hist_down.GetMean()
        
            scale_factor_hist_down_div = root_file.Get(scale_factors_down_division[sf])
            scale_factor_hist_down_div_mean = 1/scale_factor_hist_down_div.GetMean()
            final_SF = scale_factor_hist_down_mean * scale_factor_hist_down_div_mean
            
            hist2_down = hist2_nominal.Clone(histogram_name + "_2_" + name)
            hist2_down.Scale(final_SF)
            hist2_down.Write()
        
    root_file.Close()
    
for input_file_name2,histogram_name in input_files2.items():
    
    root_file = ROOT.TFile(input_file_name2, "READ")
    
  
    # Getting DeltaY histogram from the file
    hist3 = root_file.Get("DeltaY_reco")

    if hist3:
        output_file.cd()
           
        hist3_org = hist3.Clone(histogram_name + "_original")
        hist3_org.Write()
        hist3_nominal = hist3.Clone(histogram_name )
        
        for sf in scale_factors_nominal:
            scale_factor_hist_nominal = root_file.Get(sf)
            scale_factor_hist_nominal_mean = scale_factor_hist_nominal.GetMean()
            
            hist3_nominal.Scale(scale_factor_hist_nominal_mean)
        
        hist3_nominal.Write()

            
        for sf,name in scale_factors_up.items():
            scale_factor_hist_up = root_file.Get(sf)
            scale_factor_hist_up_mean = scale_factor_hist_up.GetMean()
            
            scale_factor_hist_up_div = root_file.Get(scale_factors_up_division[sf])
            scale_factor_hist_up_div_mean = 1/scale_factor_hist_up_div.GetMean()
            final_SF = scale_factor_hist_up_mean * scale_factor_hist_up_div_mean
            
            hist3_up = hist3_nominal.Clone(histogram_name + "_" + name)
            hist3_up.Scale(final_SF)
            hist3_up.Write()
        
        for sf,name in scale_factors_down.items():
            scale_factor_hist_down = root_file.Get(sf)
            scale_factor_hist_down_mean = scale_factor_hist_down.GetMean()
        
            scale_factor_hist_down_div = root_file.Get(scale_factors_down_division[sf])
            scale_factor_hist_down_div_mean = 1/scale_factor_hist_down_div.GetMean()
            final_SF = scale_factor_hist_down_mean * scale_factor_hist_down_div_mean
            
            hist3_down = hist3_nominal.Clone(histogram_name + "_" + name)
            hist3_down.Scale(final_SF)
            hist3_down.Write()
            
    root_file.Close()

# Once there is data:
for input_file_name3,histogram_name in input_files3.items():
    
    root_file = ROOT.TFile(input_file_name3, "READ")
  
    # Getting DeltaY histogram from the file
    hist4 = root_file.Get("DeltaY_reco")

    if hist4:
        output_file.cd()
      
        hist4_nominal = hist4.Clone(histogram_name)
        hist4_nominal.Write()
        
    root_file.Close()

# Close the output file
output_file.Close()
