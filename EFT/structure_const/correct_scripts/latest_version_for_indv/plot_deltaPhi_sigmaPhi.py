# This script:
#   - Loads the computed EFT structure constants (saved as a .npy file).
#   - Retrieves Delta_phi and Sigma_phi (branches) from the TTree "AnalysisTree"
#   - For each event, it gets the SM weight from genInfo->systweights()[202] (SM)
#     and computes the EFT weight for chosen Wilson coefficient values.
#   - It then fills histograms for SM and EFT distributions and creates ratio plots.
  
# Usage:
#   python plot_deltaPhi_sigmaPhi.py <structure_constants.npy> <myFile.root> [--custom-wc] [--print-only] [--compare-ctGRe1] [--sigma-phi-only] [--delta-phi-only]
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

    # Given an array of structure constants (for one event; length = poly_dim)
    # and a chosen Wilson-coefficient vector (wc_values, length 16),
    # returns the EFT weight for that event.
    
    # weight = c0 + (linear term) + (quadratic term)

    # structure_constants is array of coefficients for the polynimial (poly_dim,)
    # wc_values: The 16 Wilson coefficient values to evaluate

    # Converts input to numpy array and extracts the constant term (SM point)
    sc = np.array(structure_constants)  # shape (poly_dim,)
    c0 = sc[0]

    # Extracts the linear coefficients and calculates the linear term using dot product
    num_WCs = len(wc_values)
    s_linear = sc[1:1+num_WCs]
    w_linear = np.dot(s_linear, wc_values)

    # Quadratic terms - squared terms and cross terms
    quad_terms = [x**2 for x in wc_values]
    for i, j in combinations(range(num_WCs), 2):
        quad_terms.append(wc_values[i] * wc_values[j])
    # Extracts quadratic coefficients and calculates the quadratic term 
    idx_quad_start = 1 + num_WCs
    s_quad = sc[idx_quad_start:]
    w_quad = np.dot(s_quad, quad_terms)
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
def plot_delta_phi(tree, structures, wc_index, wc_name, output_dir="delta_phi_plots", use_custom_wc=False):
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
    hRatio = hDeltaPhi_EFT_norm.Clone("hRatio_norm_%s" % wc_name)
    hRatio.Divide(hDeltaPhi_SM_norm)
    
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
    hRatio.SetTitle("")
    hRatio.GetXaxis().SetTitle("#Delta#phi")
    hRatio.GetYaxis().SetTitle("EFT/SM (normalized)")
    hRatio.GetYaxis().SetTitleOffset(1.5)
    hRatio.GetYaxis().SetRangeUser(0.8, 1.2)
    hRatio.SetLineColor(ROOT.kBlue)
    hRatio.SetLineWidth(2)
    hRatio.SetMarkerStyle(20)  # Filled circle
    hRatio.SetMarkerSize(0.8)
    hRatio.SetMarkerColor(ROOT.kBlue)
    
    # Draw ratio with line and points
    hRatio.Draw("E1 HIST")  # Draw with error bars and line
    hRatio.Draw("E1 P SAME")  # Add points with error bars
    
    # Add horizontal line at 1
    line = ROOT.TLine(hRatio.GetXaxis().GetXmin(), 1, hRatio.GetXaxis().GetXmax(), 1)
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
    c_overlay.SaveAs(os.path.join(output_dir, "DeltaPhi_EFT_vs_SM_normalized_overlay_%s.pdf" % filename_suffix))
    c_ratio.SaveAs(os.path.join(output_dir, "DeltaPhi_EFT_vs_SM_normalized_ratio_%s.pdf" % filename_suffix))
    
    # Clean up
    c_overlay.Close()
    c_ratio.Close()

# 4. Create plots for Sigma_phi variable
def plot_sigma_phi(tree, structures, wc_index, wc_name, output_dir="sigma_phi_plots", use_custom_wc=False):
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
    hRatio = hSigmaPhi_EFT_norm.Clone("hRatio_norm_%s" % wc_name)
    hRatio.Divide(hSigmaPhi_SM_norm)
    
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
    hRatio.SetTitle("")
    hRatio.GetXaxis().SetTitle("#Sigma#phi")
    hRatio.GetYaxis().SetTitle("EFT/SM (normalized)")
    hRatio.GetYaxis().SetTitleOffset(1.5)
    hRatio.GetYaxis().SetRangeUser(0.8, 1.2)
    hRatio.SetLineColor(ROOT.kBlue)
    hRatio.SetLineWidth(2)
    hRatio.SetMarkerStyle(20)  # Filled circle
    hRatio.SetMarkerSize(0.8)
    hRatio.SetMarkerColor(ROOT.kBlue)
    
    # Draw ratio with line and points
    hRatio.Draw("E1 HIST")  # Draw with error bars and line
    hRatio.Draw("E1 P SAME")  # Add points with error bars
    
    # Add horizontal line at 1
    line = ROOT.TLine(hRatio.GetXaxis().GetXmin(), 1, hRatio.GetXaxis().GetXmax(), 1)
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
    c_overlay.SaveAs(os.path.join(output_dir, "SigmaPhi_EFT_vs_SM_normalized_overlay_%s.pdf" % filename_suffix))
    c_ratio.SaveAs(os.path.join(output_dir, "SigmaPhi_EFT_vs_SM_normalized_ratio_%s.pdf" % filename_suffix))
    
    # Clean up
    c_overlay.Close()
    c_ratio.Close()

# This function creates a combined ratio plot for all 16 Wilson coefficients for Delta_phi
def create_combined_delta_phi_ratio_plot(tree, structures, output_dir="delta_phi_plots", use_custom_wc=False):

    # Dictionary of Wilson coefficients and their indices
    WC_NAMES = {
        0: "ctGRe", 1: "ctGIm", 2: "cQj18", 3: "cQj38",
        4: "cQj11", 5: "cQj31", 6: "ctu8", 7: "ctd8",
        8: "ctj8", 9: "cQu8", 10: "cQd8", 11: "ctu1",
        12: "ctd1", 13: "ctj1", 14: "cQu1", 15: "cQd1"
    }
    
    # Create canvas for combined ratio plot
    c_combined = ROOT.TCanvas("c_combined_delta_phi_ratio", "Delta Phi: All EFT/SM Ratios", 1000, 800)
    c_combined.SetLeftMargin(0.15)
    c_combined.SetRightMargin(0.20) 
    c_combined.SetGridy()
    
    h_dummy = ROOT.TH1F("h_dummy_delta_phi", "", 16, -3.2, 3.2)
    h_dummy.SetTitle("")
    h_dummy.GetXaxis().SetTitle("#Delta#phi")
    h_dummy.GetYaxis().SetTitle("EFT/SM (normalized)")
    h_dummy.GetYaxis().SetTitleOffset(1.5)
    h_dummy.GetYaxis().SetRangeUser(0.8, 1.2)
    h_dummy.SetStats(0)
    h_dummy.Draw()
    
    leg = ROOT.TLegend(0.82, 0.15, 0.95, 0.85)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    
    # Define colors for different WCs
    colors = [
        ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kMagenta+1,
        ROOT.kCyan+2, ROOT.kOrange+7, ROOT.kViolet-3, ROOT.kSpring+9,
        ROOT.kTeal+1, ROOT.kYellow+2, ROOT.kAzure+1, ROOT.kPink+7,
        ROOT.kOrange-3, ROOT.kBlue-7, ROOT.kRed-7, ROOT.kGreen-7
    ]
    
    ratio_hists = []
    
    # First, create and fill the SM histogram 
    print("Creating SM histogram for Delta_phi ratio calculations...")
    hDeltaPhi_SM = ROOT.TH1F("hDeltaPhi_SM_combined", "SM #Delta#phi", 16, -3.2, 3.2)
    
    # Fill SM histogram 
    nentries = tree.GetEntries()
    print("Processing %d events for SM histogram..." % nentries)
    for ientry in range(nentries):
        if ientry % 10000 == 0 and ientry > 0:
            print("  Processed %d / %d events" % (ientry, nentries))
        tree.GetEntry(ientry)
        sm_weight = tree.genInfo.systweights()[202]
        if sm_weight == 0:
            continue
        delta_phi = tree.Delta_phi
        hDeltaPhi_SM.Fill(delta_phi, sm_weight)
    
    # Normalize SM histogram
    if hDeltaPhi_SM.Integral() > 0:
        hDeltaPhi_SM.Scale(1.0 / hDeltaPhi_SM.Integral())
    
    # Loop through all Wilson coefficients
    for wc_index, wc_name in WC_NAMES.items():
        # Skip if using custom WC and this is not one of the custom ones
        if use_custom_wc and wc_name not in CUSTOM_WC_VALUES:
            continue
            
        print("  Creating ratio histogram for %s..." % wc_name)
        
        # Set up WC values (all 0 except the one we're looking at)
        wc_values = np.zeros(16)
        
        if use_custom_wc:
            # Use the custom value for this WC
            wc_values[wc_index] = CUSTOM_WC_VALUES[wc_name]
        else:
            # Default: set the WC to 10
            wc_values[wc_index] = 10.0
            
        # Create and fill EFT histogram
        hDeltaPhi_EFT = ROOT.TH1F("hDeltaPhi_EFT_%s" % wc_name, "EFT #Delta#phi (%s)" % wc_name, 16, -3.2, 3.2)
        
        # Loop through events
        for i in range(tree.GetEntries()):
            tree.GetEntry(i)
            
            # Get Delta_phi value
            delta_phi = getattr(tree, "Delta_phi")
            
            # Get structure constants for this event
            event_structures = structures[i]
            
            # Calculate weight
            weight = event_weights_lin_quad(event_structures, wc_values)
            
            # Fill histogram
            hDeltaPhi_EFT.Fill(delta_phi, weight)
            
        # Normalize EFT histogram
        if hDeltaPhi_EFT.Integral() > 0:
            hDeltaPhi_EFT.Scale(1.0 / hDeltaPhi_EFT.Integral())
            
        # Create ratio histogram
        hRatio = hDeltaPhi_EFT.Clone("hRatio_delta_phi_%s" % wc_name)
        hRatio.Divide(hDeltaPhi_SM)
        
        # Set ratio plot range
        hRatio.GetYaxis().SetRangeUser(0.8, 1.2)
        
        # Style for ratio histogram
        hRatio.SetLineColor(colors[wc_index])
        hRatio.SetLineWidth(2)
        hRatio.SetMarkerStyle(20)
        hRatio.SetMarkerSize(0.8)
        hRatio.SetMarkerColor(colors[wc_index])
        
        # Store for later
        ratio_hists.append(hRatio)
        
        # Add to legend
        leg.AddEntry(hRatio, wc_name, "lp")
    
    # Draw the combined ratio plots
    for ratio_hist in ratio_hists:
        # Set all bin errors to zero to remove error bars
        for i in range(1, ratio_hist.GetNbinsX() + 1):
            ratio_hist.SetBinError(i, 0)
        ratio_hist.Draw("HIST SAME")  # Draw line
        ratio_hist.Draw("P SAME")     # Add points
    
    # Draw reference line at y=1
    line = ROOT.TLine(-3.2, 1, 3.2, 1)
    line.SetLineStyle(2)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)
    line.Draw("same")
    
    # Draw the legend
    leg.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a descriptive filename based on the WC configuration
    if use_custom_wc:
        active_wcs = []
        for name, value in CUSTOM_WC_VALUES.items():
            if value != 0 and name in WC_INDICES:
                active_wcs.append("%s=%g" % (name, value))
        
        filename_suffix = "_".join(active_wcs).replace("=", "_").replace(".", "p")
        if not filename_suffix:
            filename_suffix = "SM"
        c_combined.SaveAs(os.path.join(output_dir, "DeltaPhi_EFT_vs_SM_all_ratios_%s.pdf" % filename_suffix))
    else:
        c_combined.SaveAs(os.path.join(output_dir, "DeltaPhi_EFT_vs_SM_all_ratios.pdf"))
    
    c_combined.Close()

# This function creates a combined ratio plot for all 16 Wilson coefficients for Sigma_phi
def create_combined_sigma_phi_ratio_plot(tree, structures, output_dir="sigma_phi_plots", use_custom_wc=False):

    # Dictionary of Wilson coefficients and their indices
    WC_NAMES = {
        0: "ctGRe", 1: "ctGIm", 2: "cQj18", 3: "cQj38",
        4: "cQj11", 5: "cQj31", 6: "ctu8", 7: "ctd8",
        8: "ctj8", 9: "cQu8", 10: "cQd8", 11: "ctu1",
        12: "ctd1", 13: "ctj1", 14: "cQu1", 15: "cQd1"
    }
    
    # Create canvas for combined ratio plot
    c_combined = ROOT.TCanvas("c_combined_sigma_phi_ratio", "Sigma Phi: All EFT/SM Ratios", 1000, 800)
    c_combined.SetLeftMargin(0.15)
    c_combined.SetRightMargin(0.20) 
    c_combined.SetGridy()
    
    h_dummy = ROOT.TH1F("h_dummy_sigma_phi", "", 16, -3.2, 3.2)
    h_dummy.SetTitle("")
    h_dummy.GetXaxis().SetTitle("#Sigma#phi")
    h_dummy.GetYaxis().SetTitle("EFT/SM (normalized)")
    h_dummy.GetYaxis().SetTitleOffset(1.5)
    h_dummy.GetYaxis().SetRangeUser(0.8, 1.2)
    h_dummy.SetStats(0)
    h_dummy.Draw()
    
    leg = ROOT.TLegend(0.82, 0.15, 0.95, 0.85)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    
    # Define colors for different WCs
    colors = [
        ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kMagenta+1,
        ROOT.kCyan+2, ROOT.kOrange+7, ROOT.kViolet-3, ROOT.kSpring+9,
        ROOT.kTeal+1, ROOT.kYellow+2, ROOT.kAzure+1, ROOT.kPink+7,
        ROOT.kOrange-3, ROOT.kBlue-7, ROOT.kRed-7, ROOT.kGreen-7
    ]
    
    ratio_hists = []
    
    # First, create and fill the SM histogram 
    print("Creating SM histogram for Sigma_phi ratio calculations...")
    hSigmaPhi_SM = ROOT.TH1F("hSigmaPhi_SM_combined", "SM #Sigma#phi", 16, -3.2, 3.2)
    
    # Fill SM histogram 
    nentries = tree.GetEntries()
    print("Processing %d events for SM histogram..." % nentries)
    for ientry in range(nentries):
        if ientry % 10000 == 0 and ientry > 0:
            print("  Processed %d / %d events" % (ientry, nentries))
        tree.GetEntry(ientry)
        sm_weight = tree.genInfo.systweights()[202]
        if sm_weight == 0:
            continue
        sigma_phi = tree.Sigma_phi
        hSigmaPhi_SM.Fill(sigma_phi, sm_weight)
    
    # Normalize SM histogram
    if hSigmaPhi_SM.Integral() > 0:
        hSigmaPhi_SM.Scale(1.0 / hSigmaPhi_SM.Integral())
    
    # Loop through all Wilson coefficients
    for wc_index, wc_name in WC_NAMES.items():
        # Skip if using custom WC and this is not one of the custom ones
        if use_custom_wc and wc_name not in CUSTOM_WC_VALUES:
            continue
            
        print("  Creating ratio histogram for %s..." % wc_name)
        
        # Set up WC values (all 0 except the one we're looking at)
        wc_values = np.zeros(16)
        
        if use_custom_wc:
            # Use the custom value for this WC
            wc_values[wc_index] = CUSTOM_WC_VALUES[wc_name]
        else:
            # Default: set the WC to 10
            wc_values[wc_index] = 10.0
            
        # Create and fill EFT histogram
        hSigmaPhi_EFT = ROOT.TH1F("hSigmaPhi_EFT_%s" % wc_name, "EFT #Sigma#phi (%s)" % wc_name, 16, -3.2, 3.2)
        
        # Loop through events
        for i in range(tree.GetEntries()):
            tree.GetEntry(i)
            
            # Get Sigma_phi value
            sigma_phi = getattr(tree, "Sigma_phi")
            
            # Get structure constants for this event
            event_structures = structures[i]
            
            # Calculate weight
            weight = event_weights_lin_quad(event_structures, wc_values)
            
            # Fill histogram
            hSigmaPhi_EFT.Fill(sigma_phi, weight)
            
        # Normalize EFT histogram
        if hSigmaPhi_EFT.Integral() > 0:
            hSigmaPhi_EFT.Scale(1.0 / hSigmaPhi_EFT.Integral())
            
        # Create ratio histogram
        hRatio = hSigmaPhi_EFT.Clone("hRatio_sigma_phi_%s" % wc_name)
        hRatio.Divide(hSigmaPhi_SM)
        
        # Set ratio plot range
        hRatio.GetYaxis().SetRangeUser(0.8, 1.2)
        
        # Style for ratio histogram
        hRatio.SetLineColor(colors[wc_index])
        hRatio.SetLineWidth(2)
        hRatio.SetMarkerStyle(20)
        hRatio.SetMarkerSize(0.8)
        hRatio.SetMarkerColor(colors[wc_index])
        
        # Store for later
        ratio_hists.append(hRatio)
        
        # Add to legend
        leg.AddEntry(hRatio, wc_name, "lp")
    
    # Draw the combined ratio plots
    for ratio_hist in ratio_hists:
        # Set all bin errors to zero to remove error bars
        for i in range(1, ratio_hist.GetNbinsX() + 1):
            ratio_hist.SetBinError(i, 0)
        ratio_hist.Draw("HIST SAME")  # Draw line
        ratio_hist.Draw("P SAME")     # Add points
    
    # Draw reference line at y=1
    line = ROOT.TLine(-3.2, 1, 3.2, 1)
    line.SetLineStyle(2)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)
    line.Draw("same")
    
    # Draw the legend
    leg.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a descriptive filename based on the WC configuration
    if use_custom_wc:
        active_wcs = []
        for name, value in CUSTOM_WC_VALUES.items():
            if value != 0 and name in WC_INDICES:
                active_wcs.append("%s=%g" % (name, value))
        
        filename_suffix = "_".join(active_wcs).replace("=", "_").replace(".", "p")
        if not filename_suffix:
            filename_suffix = "SM"
        c_combined.SaveAs(os.path.join(output_dir, "SigmaPhi_EFT_vs_SM_all_ratios_%s.pdf" % filename_suffix))
    else:
        c_combined.SaveAs(os.path.join(output_dir, "SigmaPhi_EFT_vs_SM_all_ratios.pdf"))
    
    c_combined.Close()

def main():
    # Check command line arguments
    if len(sys.argv) < 3:
        print("Usage: python plot_deltaPhi_sigmaPhi.py <structure_constants.npy> <myFile.root> [options]")
        print("Options:")
        print("  --custom-wc         Use custom Wilson coefficient values defined in the script")
        print("  --print-only        Only print weights for the first 10 events (no plots)")
        print("  --compare-ctGRe1    Compare calculated weights for ctGRe=1 with weights from ROOT file")
        print("  --sigma-phi-only    Only create Sigma_phi plots")
        print("  --delta-phi-only    Only create Delta_phi plots")
        print("  --combined-only     Only create combined ratio plots (skip individual plots)")
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
                    delta_phi_dir = "delta_phi_plots"
                    plot_delta_phi(tree, structures, wc_index, wc_name, delta_phi_dir, use_custom_wc)
                    print("  Delta_phi plots saved in: %s" % delta_phi_dir)
                
                # Create Sigma_phi plots if requested
                if create_sigma_phi:
                    sigma_phi_dir = "sigma_phi_plots"
                    plot_sigma_phi(tree, structures, wc_index, wc_name, sigma_phi_dir, use_custom_wc)
                    print("  Sigma_phi plots saved in: %s" % sigma_phi_dir)
        
        # Create combined ratio plots
        if create_delta_phi:
            print("\nGenerating combined ratio plot for Delta_phi...")
            delta_phi_dir = "delta_phi_plots"
            create_combined_delta_phi_ratio_plot(tree, structures, delta_phi_dir, use_custom_wc)
            print("  Combined Delta_phi ratio plot saved in: %s" % delta_phi_dir)
        
        if create_sigma_phi:
            print("\nGenerating combined ratio plot for Sigma_phi...")
            sigma_phi_dir = "sigma_phi_plots"
            create_combined_sigma_phi_ratio_plot(tree, structures, sigma_phi_dir, use_custom_wc)
            print("  Combined Sigma_phi ratio plot saved in: %s" % sigma_phi_dir)
    
    f.Close()

if __name__ == "__main__":
    main() 