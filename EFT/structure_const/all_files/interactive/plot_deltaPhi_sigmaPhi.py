# This script:
#   - Loads the computed EFT structure constants (saved as a .npy file).
#   - Retrieves Delta_phi and Sigma_phi (branches) from the TTree "AnalysisTree"
#   - For each event, it gets the SM weight from genInfo->systweights()[202] (SM)
#     and computes the EFT weight for chosen Wilson coefficient values.
#   - It then fills histograms for SM and EFT distributions and creates ratio plots.
  
# Usage:
#   python plot_deltaPhi_sigmaPhi.py <structure_constants.npy> <myFile.root> [--custom-wc] [--print-only] [--compare-ctGRe1] [--sigma-phi-only] [--delta-phi-only] [--output-root <output.root>] [--output-dir <output_dir>]
# /data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_deltaPhi_sigmaPhi_ttree/uhh2.AnalysisModuleRunner.MC.MC_EFT_Mttbar_900-Inf_UL17_5.root
#python plot_deltaPhi_sigmaPhi.py structure_constant_spincor.npy /data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_deltaPhi_sigmaPhi_ttree/uhh2.AnalysisModuleRunner.MC.MC_EFT_Mttbar_900-Inf_UL17_5.root

# Options:
#   --custom-wc: Use custom Wilson coefficient values defined in CUSTOM_WC_VALUES
#   --print-only: Just print weights for the first 10 events instead of making plots
#   --compare-ctGRe1: Compare calculated weights for ctGRe=1 with weights from the ROOT file
#   --sigma-phi-only: Plot only the Sigma_phi variable
#   --delta-phi-only: Plot only the Delta_phi variable

import sys
import ROOT
import numpy as np
from itertools import combinations # To generate combinations of Wilson coefficients
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from array import array

# Define custom Wilson coefficient values here
CUSTOM_WC_VALUES = {
    "ctGRe": 5.0,
    "ctGIm": 0.0,
    "cQj18": 0.0,
    "cQj38": 0.0,
    "cQj11": 0.0,
    "cQj31": 0.0,
    "ctu8": 0.0,
    "ctd8": 0.0,
    "ctj8": 0.0,
    "cQu8": 0.0,
    "cQd8": 0.0,
    "ctu1": 0.0,
    "ctd1": 0.0,
    "ctj1": 0.0,
    "cQu1": 0.0,
    "cQd1": 0.0,
}

# Dictionary of Wilson coefficients and their indices
WC_INDICES = {
    "ctGRe": 0, "ctGIm": 1, "cQj18": 2, "cQj38": 3,
    "cQj11": 4, "cQj31": 5, "ctu8": 6, "ctd8": 7,
    "ctj8": 8, "cQu8": 9, "cQd8": 10, "ctu1": 11,
    "ctd1": 12, "ctj1": 13, "cQu1": 14, "cQd1": 15
}

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)

# 1. This function calculates the EFT weight for a single event
def event_weights_lin_quad(structure_constants, wc_values):

    # an array of structure constants (for one event, length = poly_dim)
    # and a chosen Wilson coefficient vector (wc_values, length 16),
    # returns the EFT weight for that event.
    
    # weight = c0 + (linear term) + (quadratic term)

    # wc_values: The 16 Wilson coefficient values to evaluate

    # Converts input to numpy array and extracts the constant term (SM point)
    sc = np.array(structure_constants)  # shape (poly_dim,)
    c0 = sc[0]

    # Extracts the linear coefficients and calculates the linear term using dot product
    num_WCs = len(wc_values)
    s_linear = sc[1:1+num_WCs] #extracts the linear coefficients from index 1 to num_WCs
    w_linear = np.dot(s_linear, wc_values) #calculates the linear term

    # Quadratic terms - squared terms and cross terms
    quad_terms = [x**2 for x in wc_values] #calculates the squared terms
    for i, j in combinations(range(num_WCs), 2): #calculates the cross terms
        quad_terms.append(wc_values[i] * wc_values[j])
    # Extracts quadratic coefficients and calculates the quadratic term 
    idx_quad_start = 1 + num_WCs #index of the first quadratic coefficient  
    s_quad = sc[idx_quad_start:] #extracts the quadratic coefficients
    w_quad = np.dot(s_quad, quad_terms) #calculates the quadratic term

    return c0 + w_linear + w_quad

# 2. Function to load structure constants
def load_structure_constants(fname):
    arr = np.load(fname)
    print("Loaded structure constants from", fname, "with shape:", arr.shape)
    return arr

# Function to compare calculated weights with weights from the ROOT file for ctGRe=1
def compare_ctGRe1_weights(tree, structures, num_events=10):    
    # Set up WC values for ctGRe=1
    num_WCs = 16
    wc_values = [0.0] * num_WCs
    wc_values[0] = 1.0  # index 0 is ctGRe
    
    print("\nComparing weights for ctGRe=1 (all others 0):")
    print("%-10s %-15s %-15s %-15s %-15s" % ("Event", "SM Weight", "Calculated", "From ROOT", "Ratio (Calc/ROOT)"))
    print("-" * 75)
    
    # The index for ctGRe=1 in the ROOT file is 203 (203 + 0)
    ctGRe1_index = 203
    
    nentries = min(num_events, tree.GetEntries())
    for ientry in range(nentries):
        tree.GetEntry(ientry)
        event_struct = structures[ientry]
        
        # Calculate weight using our function
        calculated_weight = event_weights_lin_quad(event_struct, wc_values)
        
        # Get weight from ROOT file
        root_weight = tree.genInfo.systweights()[ctGRe1_index]
        
        # Calculate ratio
        ratio = calculated_weight / root_weight if root_weight != 0 else float('nan')
        
        print("%-10d %-15.6g %-15.6g %-15.6g %-15.6g" % (
            ientry, tree.genInfo.systweights()[202], calculated_weight, root_weight, ratio))

# Function to just print weights for the first few events
def print_event_weights(tree, structures, num_events=10):
    # Set up WC values
    num_WCs = 16
    wc_values = [0.0] * num_WCs
    
    # Use custom WC values defined at the top of the script
    for name, value in CUSTOM_WC_VALUES.items():
        if name in WC_INDICES:
            wc_values[WC_INDICES[name]] = value
    
    # Print the WC configuration being used
    print("\nUsing Wilson coefficient configuration:")
    active_wcs = []
    for idx, val in enumerate(wc_values):
        if val != 0:
            wc_name = [name for name, i in WC_INDICES.items() if i == idx][0]
            print("  %s = %g" % (wc_name, val))
            active_wcs.append("%s=%g" % (wc_name, val))
    
    if not active_wcs:
        print("  All WCs set to 0 (SM)")
    
    # Print weights for the first few events
    print("\nWeights for the first %d events:" % num_events)
    print("%-10s %-15s %-15s %-15s" % ("Event", "SM Weight", "EFT Weight", "Ratio (EFT/SM)"))
    print("-" * 60)
    
    nentries = min(num_events, tree.GetEntries())
    for ientry in range(nentries):
        tree.GetEntry(ientry)
        event_struct = structures[ientry]
        
        eft_weight = event_weights_lin_quad(event_struct, wc_values)
        sm_weight = tree.genInfo.systweights()[202]
        
        ratio = eft_weight / sm_weight if sm_weight != 0 else float('nan')
        
        print("%-10d %-15.6g %-15.6g %-15.6g" % (ientry, sm_weight, eft_weight, ratio))

# 3. Create plots for Delta_phi variable
def plot_delta_phi(tree, structures, wc_index, wc_name, output_dir="delta_phi_plots", use_custom_wc=False, output_root_file=None):
    # Create histograms for Delta_phi
    hDeltaPhi_SM = ROOT.TH1F("hDeltaPhi_SM_%s" % wc_name, "SM #Delta#phi;#Delta#phi;Events", 16, -3.2, 3.2)
    hDeltaPhi_EFT = hDeltaPhi_SM.Clone("hDeltaPhi_EFT_%s" % wc_name)
    hDeltaPhi_SM_norm = hDeltaPhi_SM.Clone("hDeltaPhi_SM_norm_%s" % wc_name)
    hDeltaPhi_EFT_norm = hDeltaPhi_SM.Clone("hDeltaPhi_EFT_norm_%s" % wc_name)
    
    # Set up WC values
    num_WCs = 16
    wc_values = [0.0] * num_WCs
    
    if use_custom_wc:
        # Use custom WC values defined at the top of the script
        for name, value in CUSTOM_WC_VALUES.items():
            if name in WC_INDICES:
                wc_values[WC_INDICES[name]] = value
        plot_title = "Custom WCs"
    else:
        # Use default (single WC = 10)
        wc_values[wc_index] = 10.0
        plot_title = "%s = 10" % wc_name
    
    # Print the WC configuration being used
    print("\nUsing Wilson coefficient configuration:")
    active_wcs = []
    for idx, val in enumerate(wc_values):
        if val != 0:
            wc_name_for_idx = [name for name, i in WC_INDICES.items() if i == idx][0]
            print("  %s = %g" % (wc_name_for_idx, val))
            active_wcs.append("%s=%g" % (wc_name_for_idx, val))
    
    if not active_wcs:
        print("  All WCs set to 0 (SM)")
        plot_title = "SM"
    
    # Fill histograms
    nentries = tree.GetEntries()
    for ientry in range(nentries):
        tree.GetEntry(ientry)
        event_struct = structures[ientry]
        
        eft_weight = event_weights_lin_quad(event_struct, wc_values)
        sm_weight = tree.genInfo.systweights()[202]
        
        if sm_weight == 0:
            continue
            
        delta_phi = tree.Delta_phi
        hDeltaPhi_SM.Fill(delta_phi, sm_weight)
        hDeltaPhi_EFT.Fill(delta_phi, eft_weight)
    
    # Normalize histograms
    if hDeltaPhi_SM.Integral() > 0:
        hDeltaPhi_SM_norm.Add(hDeltaPhi_SM)
        hDeltaPhi_SM_norm.Scale(1.0 / hDeltaPhi_SM_norm.Integral())
    
    if hDeltaPhi_EFT.Integral() > 0:
        hDeltaPhi_EFT_norm.Add(hDeltaPhi_EFT)
        hDeltaPhi_EFT_norm.Scale(1.0 / hDeltaPhi_EFT_norm.Integral())
    
    # Create ratio histogram
    hRatio_norm = hDeltaPhi_EFT_norm.Clone("hRatio_norm_deltaPhi_%s" % wc_name)
    hRatio_norm.Divide(hDeltaPhi_SM_norm)
    
    # Create canvas for overlay plot
    c_overlay = ROOT.TCanvas("c_overlay_%s" % wc_name, "Delta Phi: EFT vs SM (%s)" % wc_name, 800, 600)
    c_overlay.SetLeftMargin(0.15)
    c_overlay.SetRightMargin(0.05)
    
    # Set up normalized histograms
    hDeltaPhi_SM_norm.SetTitle("")
    hDeltaPhi_SM_norm.GetXaxis().SetTitle("#Delta#phi")
    hDeltaPhi_SM_norm.GetYaxis().SetTitle("Normalized Events")
    hDeltaPhi_SM_norm.GetYaxis().SetTitleOffset(1.5)
    hDeltaPhi_SM_norm.GetYaxis().SetRangeUser(0.03, 0.1)
    
    # Style for SM histogram
    hDeltaPhi_SM_norm.SetLineColor(ROOT.kBlack)
    hDeltaPhi_SM_norm.SetLineWidth(2)
    hDeltaPhi_SM_norm.SetMarkerStyle(20)  # Filled circle
    hDeltaPhi_SM_norm.SetMarkerSize(0.8)
    hDeltaPhi_SM_norm.SetMarkerColor(ROOT.kBlack)
    
    # Style for EFT histogram
    hDeltaPhi_EFT_norm.SetLineColor(ROOT.kRed)
    hDeltaPhi_EFT_norm.SetLineWidth(2)
    hDeltaPhi_EFT_norm.SetMarkerStyle(21)  # Filled square
    hDeltaPhi_EFT_norm.SetMarkerSize(0.8)
    hDeltaPhi_EFT_norm.SetMarkerColor(ROOT.kRed)
    
    # Draw normalized distributions with lines and points
    # First draw histograms as lines
    hDeltaPhi_SM_norm.Draw("E1 HIST")  # Draw line with error bars
    hDeltaPhi_EFT_norm.Draw("E1 HIST SAME")  # Draw the EFT line with error bars
    
    # Then add points on top
    hDeltaPhi_SM_norm.Draw("E1 P SAME")  # Add SM points with error bars
    hDeltaPhi_EFT_norm.Draw("E1 P SAME")  # Add EFT points with error bars
    
    # Add legend
    leg = ROOT.TLegend(0.65, 0.75, 0.89, 0.89)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.AddEntry(hDeltaPhi_SM_norm, "SM", "lp")  # l for line, p for point
    leg.AddEntry(hDeltaPhi_EFT_norm, plot_title, "lp")
    leg.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    # Create canvas for ratio plot
    c_ratio = ROOT.TCanvas("c_ratio_%s" % wc_name, "Delta Phi: EFT/SM Ratio (%s)" % wc_name, 800, 600)
    c_ratio.SetLeftMargin(0.15)
    c_ratio.SetGridy()
    
    # Style for ratio plot
    hRatio_norm.SetTitle("")
    hRatio_norm.GetXaxis().SetTitle("#Delta#phi")
    hRatio_norm.GetYaxis().SetTitle("EFT/SM (normalized)")
    hRatio_norm.GetYaxis().SetTitleOffset(1.5)
    hRatio_norm.GetYaxis().SetRangeUser(0.8, 1.2)
    hRatio_norm.SetLineColor(ROOT.kBlue)
    hRatio_norm.SetLineWidth(2)
    hRatio_norm.SetMarkerStyle(20)  # Filled circle
    hRatio_norm.SetMarkerSize(0.8)
    hRatio_norm.SetMarkerColor(ROOT.kBlue)
    
    # Draw ratio with line and points
    hRatio_norm.Draw("E1 HIST")  # Draw with error bars and line
    hRatio_norm.Draw("E1 P SAME")  # Add points with error bars
    
    # Add horizontal line at 1
    line = ROOT.TLine(hRatio_norm.GetXaxis().GetXmin(), 1, hRatio_norm.GetXaxis().GetXmax(), 1)
    line.SetLineStyle(2)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)
    line.Draw("same")
    
    # Add CMS text
    cms_text_ratio = ROOT.TLatex()
    cms_text_ratio.SetNDC()
    cms_text_ratio.SetTextSize(0.05)
    cms_text_ratio.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a descriptive filename based on the WC configuration
    if use_custom_wc:
        filename_suffix = "_".join(active_wcs).replace("=", "_").replace(".", "p")
        if not filename_suffix:
            filename_suffix = "SM"
    else:
        filename_suffix = wc_name
    
    # Save plots
    c_overlay.SaveAs(os.path.join(output_dir, "DeltaPhi_EFT_vs_SM_%s.pdf" % filename_suffix))
    c_ratio.SaveAs(os.path.join(output_dir, "DeltaPhi_EFT_vs_SM_normalized_ratio_%s.pdf" % filename_suffix))
    
    # Clean up
    c_overlay.Close()
    c_ratio.Close()

    # If output_root_file is provided, save histograms to it
    if output_root_file:
        output_root_file.cd()
        hDeltaPhi_SM.Write()
        hDeltaPhi_EFT.Write()
        # Don't save normalized histograms to ROOT file
        # hDeltaPhi_SM_norm.Write()
        # hDeltaPhi_EFT_norm.Write()
        # hRatio_norm.Write()

# 4. Create plots for Sigma_phi variable
def plot_sigma_phi(tree, structures, wc_index, wc_name, output_dir="sigma_phi_plots", use_custom_wc=False, output_root_file=None):
    # Create histograms for Sigma_phi
    hSigmaPhi_SM = ROOT.TH1F("hSigmaPhi_SM_%s" % wc_name, "SM #Sigma#phi;#Sigma#phi;Events", 16, -3.2, 3.2)
    hSigmaPhi_EFT = hSigmaPhi_SM.Clone("hSigmaPhi_EFT_%s" % wc_name)
    hSigmaPhi_SM_norm = hSigmaPhi_SM.Clone("hSigmaPhi_SM_norm_%s" % wc_name)
    hSigmaPhi_EFT_norm = hSigmaPhi_SM.Clone("hSigmaPhi_EFT_norm_%s" % wc_name)
    
    # Set up WC values
    num_WCs = 16
    wc_values = [0.0] * num_WCs
    
    if use_custom_wc:
        # Use custom WC values defined at the top of the script
        for name, value in CUSTOM_WC_VALUES.items():
            if name in WC_INDICES:
                wc_values[WC_INDICES[name]] = value
        plot_title = "Custom WCs"
    else:
        # Use default (single WC = 10)
        wc_values[wc_index] = 10.0
        plot_title = "%s = 10" % wc_name
    
    # Print the WC configuration being used
    print("\nUsing Wilson coefficient configuration:")
    active_wcs = []
    for idx, val in enumerate(wc_values):
        if val != 0:
            wc_name_for_idx = [name for name, i in WC_INDICES.items() if i == idx][0]
            print("  %s = %g" % (wc_name_for_idx, val))
            active_wcs.append("%s=%g" % (wc_name_for_idx, val))
    
    if not active_wcs:
        print("  All WCs set to 0 (SM)")
        plot_title = "SM"
    
    # Fill histograms
    nentries = tree.GetEntries()
    for ientry in range(nentries):
        tree.GetEntry(ientry)
        event_struct = structures[ientry]
        
        eft_weight = event_weights_lin_quad(event_struct, wc_values)
        sm_weight = tree.genInfo.systweights()[202]
        
        if sm_weight == 0:
            continue
            
        sigma_phi = tree.Sigma_phi
        hSigmaPhi_SM.Fill(sigma_phi, sm_weight)
        hSigmaPhi_EFT.Fill(sigma_phi, eft_weight)
    
    # Normalize histograms
    if hSigmaPhi_SM.Integral() > 0:
        hSigmaPhi_SM_norm.Add(hSigmaPhi_SM)
        hSigmaPhi_SM_norm.Scale(1.0 / hSigmaPhi_SM_norm.Integral())
    
    if hSigmaPhi_EFT.Integral() > 0:
        hSigmaPhi_EFT_norm.Add(hSigmaPhi_EFT)
        hSigmaPhi_EFT_norm.Scale(1.0 / hSigmaPhi_EFT_norm.Integral())
    
    # Create ratio histogram
    hRatio_norm = hSigmaPhi_EFT_norm.Clone("hRatio_norm_sigmaPhi_%s" % wc_name)
    hRatio_norm.Divide(hSigmaPhi_SM_norm)
    
    # Create canvas for overlay plot
    c_overlay = ROOT.TCanvas("c_overlay_%s" % wc_name, "Sigma Phi: EFT vs SM (%s)" % wc_name, 800, 600)
    c_overlay.SetLeftMargin(0.15)
    c_overlay.SetRightMargin(0.05)
    
    # Set up normalized histograms
    hSigmaPhi_SM_norm.SetTitle("")
    hSigmaPhi_SM_norm.GetXaxis().SetTitle("#Sigma#phi")
    hSigmaPhi_SM_norm.GetYaxis().SetTitle("Normalized Events")
    hSigmaPhi_SM_norm.GetYaxis().SetTitleOffset(1.5)
    hSigmaPhi_SM_norm.GetYaxis().SetRangeUser(0.03, 0.1)
    
    # Style for SM histogram
    hSigmaPhi_SM_norm.SetLineColor(ROOT.kBlack)
    hSigmaPhi_SM_norm.SetLineWidth(2)
    hSigmaPhi_SM_norm.SetMarkerStyle(20)  # Filled circle
    hSigmaPhi_SM_norm.SetMarkerSize(0.8)
    hSigmaPhi_SM_norm.SetMarkerColor(ROOT.kBlack)
    
    # Style for EFT histogram
    hSigmaPhi_EFT_norm.SetLineColor(ROOT.kRed)
    hSigmaPhi_EFT_norm.SetLineWidth(2)
    hSigmaPhi_EFT_norm.SetMarkerStyle(21)  # Filled square
    hSigmaPhi_EFT_norm.SetMarkerSize(0.8)
    hSigmaPhi_EFT_norm.SetMarkerColor(ROOT.kRed)
    
    # Draw normalized distributions with lines and points
    # First draw histograms as lines
    hSigmaPhi_SM_norm.Draw("E1 HIST")  # Draw line with error bars
    hSigmaPhi_EFT_norm.Draw("E1 HIST SAME")  # Draw the EFT line with error bars
    
    # Then add points on top
    hSigmaPhi_SM_norm.Draw("E1 P SAME")  # Add SM points with error bars
    hSigmaPhi_EFT_norm.Draw("E1 P SAME")  # Add EFT points with error bars
    
    # Add legend
    leg = ROOT.TLegend(0.65, 0.75, 0.89, 0.89)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.AddEntry(hSigmaPhi_SM_norm, "SM", "lp")  # l for line, p for point
    leg.AddEntry(hSigmaPhi_EFT_norm, plot_title, "lp")
    leg.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    # Create canvas for ratio plot
    c_ratio = ROOT.TCanvas("c_ratio_%s" % wc_name, "Sigma Phi: EFT/SM Ratio (%s)" % wc_name, 800, 600)
    c_ratio.SetLeftMargin(0.15)
    c_ratio.SetGridy()
    
    # Style for ratio plot
    hRatio_norm.SetTitle("")
    hRatio_norm.GetXaxis().SetTitle("#Sigma#phi")
    hRatio_norm.GetYaxis().SetTitle("EFT/SM (normalized)")
    hRatio_norm.GetYaxis().SetTitleOffset(1.5)
    hRatio_norm.GetYaxis().SetRangeUser(0.8, 1.2)
    hRatio_norm.SetLineColor(ROOT.kBlue)
    hRatio_norm.SetLineWidth(2)
    hRatio_norm.SetMarkerStyle(20)  # Filled circle
    hRatio_norm.SetMarkerSize(0.8)
    hRatio_norm.SetMarkerColor(ROOT.kBlue)
    
    # Draw ratio with line and points
    hRatio_norm.Draw("E1 HIST")  # Draw with error bars and line
    hRatio_norm.Draw("E1 P SAME")  # Add points with error bars
    
    # Add horizontal line at 1
    line = ROOT.TLine(hRatio_norm.GetXaxis().GetXmin(), 1, hRatio_norm.GetXaxis().GetXmax(), 1)
    line.SetLineStyle(2)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)
    line.Draw("same")
    
    # Add CMS text
    cms_text_ratio = ROOT.TLatex()
    cms_text_ratio.SetNDC()
    cms_text_ratio.SetTextSize(0.05)
    cms_text_ratio.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a descriptive filename based on the WC configuration
    if use_custom_wc:
        filename_suffix = "_".join(active_wcs).replace("=", "_").replace(".", "p")
        if not filename_suffix:
            filename_suffix = "SM"
    else:
        filename_suffix = wc_name
    
    # Save plots
    c_overlay.SaveAs(os.path.join(output_dir, "SigmaPhi_EFT_vs_SM_%s.pdf" % filename_suffix))
    c_ratio.SaveAs(os.path.join(output_dir, "SigmaPhi_EFT_vs_SM_normalized_ratio_%s.pdf" % filename_suffix))
    
    # Clean up
    c_overlay.Close()
    c_ratio.Close()

    # If output_root_file is provided, save histograms to it
    if output_root_file:
        output_root_file.cd()
        hSigmaPhi_SM.Write()
        hSigmaPhi_EFT.Write()
        # Don't save normalized histograms to ROOT file
        # hSigmaPhi_SM_norm.Write()
        # hSigmaPhi_EFT_norm.Write()
        # hRatio_norm.Write()

# This function creates a combined ratio plot for all 16 Wilson coefficients for Delta_phi
def create_combined_delta_phi_ratio_plot(tree, structures, output_dir="delta_phi_plots", use_custom_wc=False, output_root_file=None):

    # Dictionary of Wilson coefficients and their indices
    wc_dict = {
        "ctGRe": 0,
        "ctGIm": 1,
        "ctW": 2,
        "ctp": 3,
        "cpQM": 4,
        "cpQ3": 5,
        "cpt": 6,
        "cptb": 7,
        "cQl3i": 8,
        "cQlMi": 9,
        "cQei": 10,
        "ctli": 11,
        "ctei": 12,
        "ctlSi": 13,
        "ctlTi": 14,
        "cQj18": 15
    }
    
    # Define colors for different WCs
    colors = [
        ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kMagenta+1,
        ROOT.kCyan+2, ROOT.kOrange+7, ROOT.kViolet-3, ROOT.kSpring+9,
        ROOT.kTeal+1, ROOT.kYellow+2, ROOT.kAzure+1, ROOT.kPink+7,
        ROOT.kOrange-3, ROOT.kBlue-7, ROOT.kRed-7, ROOT.kGreen-7
    ]

    # Create histograms for SM and EFT
    h_SM = ROOT.TH1F("h_SM_deltaPhi", "SM #Delta#phi", 20, -3.15, 3.15)
    
    # Dictionary to store EFT histograms
    h_EFT_dict = {}
    
    # List to store ratio histograms
    ratio_hists = []
    
    # Fill SM histogram
    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        
        # Get structure constants for this event
        event_structs = structures[i]
        
        # Calculate SM weight (all WC=0)
        sm_weight = event_weights_lin_quad(event_structs, [0.0] * 16)
        
        # Fill SM histogram
        h_SM.Fill(tree.Delta_phi, sm_weight)
    
    # Normalize SM histogram
    h_SM.Scale(1.0 / h_SM.Integral())
    
    # Create and fill EFT histograms for each Wilson coefficient
    i = 0
    for wc_name, wc_index in wc_dict.items():
        # Create histogram for this WC
        h_EFT = ROOT.TH1F("h_EFT_deltaPhi_" + wc_name, "EFT #Delta#phi " + wc_name, 20, -3.15, 3.15)
        h_EFT_dict[wc_name] = h_EFT
        
        # Set up WC values (only this WC=10, others=0)
        wc_values = [0.0] * 16
        wc_values[wc_index] = 10.0
        
        # Fill EFT histogram
        for j in range(tree.GetEntries()):
            tree.GetEntry(j)
            
            # Get structure constants for this event
            event_structs = structures[j]
            
            # Calculate EFT weight
            eft_weight = event_weights_lin_quad(event_structs, wc_values)
            
            # Fill EFT histogram
            h_EFT.Fill(tree.Delta_phi, eft_weight)
        
        # Normalize EFT histogram
        h_EFT.Scale(1.0 / h_EFT.Integral())
        
        # Create ratio histogram
        hRatio = h_EFT.Clone("hRatio_norm_deltaPhi_" + wc_name)
        hRatio.SetTitle("EFT/SM Ratio for " + wc_name)
        hRatio.Divide(h_SM)
        
        # Set ratio histogram style
        color = colors[i % len(colors)]  # Ensure we don't go out of bounds
        hRatio.SetLineColor(color)
        hRatio.SetLineWidth(2)
        hRatio.SetMarkerStyle(20 + i % 10)
        hRatio.SetMarkerSize(0.8)
        hRatio.SetMarkerColor(color)
        
        # Remove error bars for combined ratio plot
        for bin in range(1, hRatio.GetNbinsX() + 1):
            hRatio.SetBinError(bin, 0)
        
        # Add to list of ratio histograms
        ratio_hists.append(hRatio)
        i += 1
    
    # Create canvas for ratio plot
    c_ratio = ROOT.TCanvas("c_ratio_deltaPhi", "Ratio Plot", 1000, 800)
    c_ratio.SetLeftMargin(0.15)
    c_ratio.SetRightMargin(0.20)
    c_ratio.SetGridy()
    
    # Create a dummy histogram for the axes
    h_dummy = ROOT.TH1F("h_dummy_deltaPhi", "", 20, -3.15, 3.15)
    h_dummy.SetTitle("")
    h_dummy.GetXaxis().SetTitle("#Delta#phi")
    h_dummy.GetYaxis().SetTitle("EFT/SM (normalized)")
    h_dummy.GetYaxis().SetTitleOffset(1.5)
    h_dummy.GetYaxis().SetRangeUser(0.8, 1.2)
    h_dummy.SetStats(0)
    h_dummy.Draw()
    
    # Create legend
    legend = ROOT.TLegend(0.82, 0.15, 0.95, 0.85)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    
    # Draw ratio histograms
    for hRatio in ratio_hists:
        hRatio.Draw("HIST SAME")
        hRatio.Draw("P SAME")  # Add points
        
        # Extract WC name from histogram title
        title = hRatio.GetTitle()
        wc_name = title.split()[-1]
        legend.AddEntry(hRatio, wc_name, "lp")
    
    # Draw horizontal line at y=1
    line = ROOT.TLine(-3.15, 1.0, 3.15, 1.0)
    line.SetLineStyle(2)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)
    line.Draw("SAME")
    
    # Draw legend
    legend.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    # Save canvas as PDF
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    c_ratio.SaveAs(os.path.join(output_dir, "ratio_plot_deltaPhi.pdf"))
    
    # No need to save histograms to ROOT file - they're already saved by the individual plot functions
    
    return ratio_hists

# This function creates a combined ratio plot for all 16 Wilson coefficients for Sigma_phi
def create_combined_sigma_phi_ratio_plot(tree, structures, output_dir="sigma_phi_plots", use_custom_wc=False, output_root_file=None):

    # Dictionary of Wilson coefficients and their indices
    wc_dict = {
        "ctGRe": 0,
        "ctGIm": 1,
        "ctW": 2,
        "ctp": 3,
        "cpQM": 4,
        "cpQ3": 5,
        "cpt": 6,
        "cptb": 7,
        "cQl3i": 8,
        "cQlMi": 9,
        "cQei": 10,
        "ctli": 11,
        "ctei": 12,
        "ctlSi": 13,
        "ctlTi": 14,
        "cQj18": 15
    }
    
    # Define colors for different WCs
    colors = [
        ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kMagenta+1,
        ROOT.kCyan+2, ROOT.kOrange+7, ROOT.kViolet-3, ROOT.kSpring+9,
        ROOT.kTeal+1, ROOT.kYellow+2, ROOT.kAzure+1, ROOT.kPink+7,
        ROOT.kOrange-3, ROOT.kBlue-7, ROOT.kRed-7, ROOT.kGreen-7
    ]

    # Create histograms for SM and EFT
    h_SM = ROOT.TH1F("h_SM_sigmaPhi", "SM #sigma#phi", 20, 0, 3.15)
    
    # Dictionary to store EFT histograms
    h_EFT_dict = {}
    
    # List to store ratio histograms
    ratio_hists = []
    
    # Fill SM histogram
    for i in range(tree.GetEntries()):
        tree.GetEntry(i)
        
        # Get structure constants for this event
        event_structs = structures[i]
        
        # Calculate SM weight (all WC=0)
        sm_weight = event_weights_lin_quad(event_structs, [0.0] * 16)
        
        # Fill SM histogram
        h_SM.Fill(tree.Sigma_phi, sm_weight)
    
    # Normalize SM histogram
    h_SM.Scale(1.0 / h_SM.Integral())
    
    # Create and fill EFT histograms for each Wilson coefficient
    i = 0
    for wc_name, wc_index in wc_dict.items():
        # Create histogram for this WC
        h_EFT = ROOT.TH1F("h_EFT_sigmaPhi_" + wc_name, "EFT #sigma#phi " + wc_name, 20, 0, 3.15)
        h_EFT_dict[wc_name] = h_EFT
        
        # Set up WC values (only this WC=10, others=0)
        wc_values = [0.0] * 16
        wc_values[wc_index] = 10.0
        
        # Fill EFT histogram
        for j in range(tree.GetEntries()):
            tree.GetEntry(j)
            
            # Get structure constants for this event
            event_structs = structures[j]
            
            # Calculate EFT weight
            eft_weight = event_weights_lin_quad(event_structs, wc_values)
            
            # Fill EFT histogram
            h_EFT.Fill(tree.Sigma_phi, eft_weight)
        
        # Normalize EFT histogram
        h_EFT.Scale(1.0 / h_EFT.Integral())
        
        # Create ratio histogram
        hRatio = h_EFT.Clone("hRatio_norm_sigmaPhi_" + wc_name)
        hRatio.SetTitle("EFT/SM Ratio for " + wc_name)
        hRatio.Divide(h_SM)
        
        # Set ratio histogram style
        color = colors[i % len(colors)]  # Ensure we don't go out of bounds
        hRatio.SetLineColor(color)
        hRatio.SetLineWidth(2)
        hRatio.SetMarkerStyle(20 + i % 10)
        hRatio.SetMarkerSize(0.8)
        hRatio.SetMarkerColor(color)
        
        # Remove error bars for combined ratio plot
        for bin in range(1, hRatio.GetNbinsX() + 1):
            hRatio.SetBinError(bin, 0)
        
        # Add to list of ratio histograms
        ratio_hists.append(hRatio)
        i += 1
    
    # Create canvas for ratio plot
    c_ratio = ROOT.TCanvas("c_ratio_sigmaPhi", "Ratio Plot", 1000, 800)
    c_ratio.SetLeftMargin(0.15)
    c_ratio.SetRightMargin(0.20)
    c_ratio.SetGridy()
    
    # Create a dummy histogram for the axes
    h_dummy = ROOT.TH1F("h_dummy_sigmaPhi", "", 20, 0, 3.15)
    h_dummy.SetTitle("")
    h_dummy.GetXaxis().SetTitle("#sigma#phi")
    h_dummy.GetYaxis().SetTitle("EFT/SM (normalized)")
    h_dummy.GetYaxis().SetTitleOffset(1.5)
    h_dummy.GetYaxis().SetRangeUser(0.8, 1.2)
    h_dummy.SetStats(0)
    h_dummy.Draw()
    
    # Create legend
    legend = ROOT.TLegend(0.82, 0.15, 0.95, 0.85)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    
    # Draw ratio histograms
    for hRatio in ratio_hists:
        hRatio.Draw("HIST SAME")
        hRatio.Draw("P SAME")  # Add points
        
        # Extract WC name from histogram title
        title = hRatio.GetTitle()
        wc_name = title.split()[-1]
        legend.AddEntry(hRatio, wc_name, "lp")
    
    # Draw horizontal line at y=1
    line = ROOT.TLine(0, 1.0, 3.15, 1.0)
    line.SetLineStyle(2)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)
    line.Draw("SAME")
    
    # Draw legend
    legend.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    # Save canvas as PDF
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    c_ratio.SaveAs(os.path.join(output_dir, "ratio_plot_sigmaPhi.pdf"))
    
    # No need to save histograms to ROOT file - they're already saved by the individual plot functions
    
    return ratio_hists

def main():
    # Check command line arguments
    if len(sys.argv) < 3:
        print("Usage: python plot_deltaPhi_sigmaPhi.py <structure_constants.npy> <myFile.root> [--custom-wc] [--print-only] [--compare-ctGRe1] [--sigma-phi-only] [--delta-phi-only] [--output-root <output.root>] [--output-dir <output_dir>]")
        sys.exit(1)
    
    struct_file = sys.argv[1]
    root_file = sys.argv[2]
    
    # Parse command line options
    use_custom_wc = "--custom-wc" in sys.argv
    print_only = "--print-only" in sys.argv
    compare_ctGRe1 = "--compare-ctGRe1" in sys.argv
    sigma_phi_only = "--sigma-phi-only" in sys.argv
    delta_phi_only = "--delta-phi-only" in sys.argv
    combined_only = "--combined-only" in sys.argv
    
    # Check for output ROOT file option
    output_root_filename = None
    output_root_file = None
    if "--output-root" in sys.argv:
        try:
            output_root_idx = sys.argv.index("--output-root")
            output_root_filename = sys.argv[output_root_idx + 1]
            
            # Check if the file already exists and open in UPDATE mode if it does
            if os.path.exists(output_root_filename):
                output_root_file = ROOT.TFile(output_root_filename, "UPDATE")
                print("Will update existing ROOT file:", output_root_filename)
            else:
                output_root_file = ROOT.TFile(output_root_filename, "RECREATE")
                print("Will create new ROOT file:", output_root_filename)
                
        except (IndexError, ValueError):
            print("Error: --output-root option requires a filename")
            sys.exit(1)
    
    # Check for output directory option
    output_dir = None
    if "--output-dir" in sys.argv:
        try:
            output_dir_idx = sys.argv.index("--output-dir")
            output_dir = sys.argv[output_dir_idx + 1]
            print("Will save PDF plots to directory:", output_dir)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
        except (IndexError, ValueError):
            print("Error: --output-dir option requires a directory path")
            sys.exit(1)
    
    # Load structure constants
    structures = load_structure_constants(struct_file)
    
    f = ROOT.TFile.Open(root_file)
    if not f or f.IsZombie():
        print("Error: Cannot open file", root_file)
        sys.exit(1)
    
    # Get TTree
    tree = f.Get("AnalysisTree")
    if not tree:
        print("Error: Cannot find TTree 'AnalysisTree'")
        sys.exit(1)
    
    # Dictionary of Wilson coefficients and their indices
    WC_NAMES = {
        0: "ctGRe", 1: "ctGIm", 2: "cQj18", 3: "cQj38",
        4: "cQj11", 5: "cQj31", 6: "ctu8", 7: "ctd8",
        8: "ctj8", 9: "cQu8", 10: "cQd8", 11: "ctu1",
        12: "ctd1", 13: "ctj1", 14: "cQu1", 15: "cQd1"
    }
    
    if compare_ctGRe1:
        # Compare calculated weights with weights from the ROOT file for ctGRe=1
        compare_ctGRe1_weights(tree, structures)
    elif print_only:
        # Just print weights for the first few events
        print_event_weights(tree, structures)
    else:
        # Create plots for each Wilson coefficient
        print("\nGenerating plots...")
        
        # Decide which plots to create based on command line options
        create_delta_phi = not sigma_phi_only
        create_sigma_phi = not delta_phi_only
        
        if create_delta_phi and create_sigma_phi:
            print("Creating plots for both Delta_phi and Sigma_phi")
        elif create_delta_phi:
            print("Creating plots for Delta_phi only")
        elif create_sigma_phi:
            print("Creating plots for Sigma_phi only")
        
        # Comment out these lines to skip individual plots
        if not combined_only:
            for wc_index, wc_name in WC_NAMES.items():
                print("Processing %s (index %d)..." % (wc_name, wc_index))
                
                # Create Delta_phi plots if requested
                if create_delta_phi:
                    delta_phi_dir = output_dir if output_dir else "delta_phi_plots"
                    if not os.path.exists(delta_phi_dir):
                        os.makedirs(delta_phi_dir)
                    plot_delta_phi(tree, structures, wc_index, wc_name, delta_phi_dir, use_custom_wc, output_root_file)
                    print("  Delta_phi plots saved in: %s" % delta_phi_dir)
                
                # Create Sigma_phi plots if requested
                if create_sigma_phi:
                    sigma_phi_dir = output_dir if output_dir else "sigma_phi_plots"
                    if not os.path.exists(sigma_phi_dir):
                        os.makedirs(sigma_phi_dir)
                    plot_sigma_phi(tree, structures, wc_index, wc_name, sigma_phi_dir, use_custom_wc, output_root_file)
                    print("  Sigma_phi plots saved in: %s" % sigma_phi_dir)
        
        # Create combined ratio plots
        if create_delta_phi:
            print("\nGenerating combined ratio plot for Delta_phi...")
            delta_phi_dir = output_dir if output_dir else "delta_phi_plots"
            create_combined_delta_phi_ratio_plot(tree, structures, delta_phi_dir, use_custom_wc, output_root_file)
            print("  Combined Delta_phi ratio plot saved in: %s" % delta_phi_dir)
        
        if create_sigma_phi:
            print("\nGenerating combined ratio plot for Sigma_phi...")
            sigma_phi_dir = output_dir if output_dir else "sigma_phi_plots"
            create_combined_sigma_phi_ratio_plot(tree, structures, sigma_phi_dir, use_custom_wc, output_root_file)
            print("  Combined Sigma_phi ratio plot saved in: %s" % sigma_phi_dir)
    
    if output_root_file:
        output_root_file.Close()
        print("All histograms saved to ROOT file:", output_root_filename)
    
    f.Close()

if __name__ == "__main__":
    main() 