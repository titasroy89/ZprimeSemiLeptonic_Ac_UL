# This script:
#   - Loads the computed EFT structure constants (saved as a .npy file).
#   - Retrieves DeltaYreco (branch) from the TTree "AnalysisTree"
#   - For each event, it gets the SM weight from genInfo->systweights()[202] (SM)
#     and computes the EFT weight for a chosen Wilson coefficient (here we set cQd1 = 10, all others 0).
#   - It then fills two histograms: one for the SM dY distribution and one reweighted for EFT.
#   - Finally, it creates a ratio plot (EFT/SM).
  
# Usage:
#   python plot_deltaY_shape.py <structure_constants.npy> <myFile.root> [--custom-wc] [--print-only] [--compare-ctGRe1] [--compare-cQj18] [--output-root <output.root>] [--output-dir <output_dir>]
#/data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_ttree/uhh2.AnalysisModuleRunner.MC.MC_EFT_Mttbar_0-700_UL17_2.root

# Options:
#   --custom-wc: Use custom Wilson coefficient values defined in CUSTOM_WC_VALUES
#   --print-only: Just print weights for the first 10 events instead of making plots
#   --compare-ctGRe1: Compare calculated weights for ctGRe=1 with weights from the ROOT file
#   --compare-cQj18: Compare calculated weights for cQj18=1 with weights from the ROOT file
#   --output-root: Save histograms to a ROOT file
#   --output-dir: Save PDF plots to a directory

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
    "ctGRe": 1.0,
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
    "cQd1": 0.0
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

# Function to compare calculated weights with weights from the ROOT file for cQj18=1
def compare_cQj18_weights(tree, structures, num_events=10):    
    # Set up WC values for cQj18=1
    num_WCs = 16
    wc_values = [0.0] * num_WCs
    wc_values[2] = 1.0  # index 2 is cQj18
    
    print("\nComparing weights for cQj18=1 (all others 0):")
    print("%-10s %-15s %-15s %-15s %-15s" % ("Event", "SM Weight", "Calculated", "From ROOT", "Ratio (Calc/ROOT)"))
    print("-" * 75)
    
    # The index for cQj18=1 in the ROOT file is 205 (203 + 2)
    cQj18_index = 205
    
    nentries = min(num_events, tree.GetEntries())
    for ientry in range(nentries):
        tree.GetEntry(ientry)
        event_struct = structures[ientry]
        
        # Calculate weight using our function
        calculated_weight = event_weights_lin_quad(event_struct, wc_values)
        
        # Get weight from ROOT file
        root_weight = tree.genInfo.systweights()[cQj18_index]
        
        # Calculate ratio
        ratio = calculated_weight / root_weight if root_weight != 0 else float('nan')
        
        print("%-10d %-15.6g %-15.6g %-15.6g %-15.6g" % (
            ientry, tree.genInfo.systweights()[202], calculated_weight, root_weight, ratio))

# 3. Main script
# This function creates normalized distribution and ratio plots for a single Wilson coefficient
def plot_single_wc(tree, structures, wc_index, wc_name, output_dir="plots", use_custom_wc=False, output_root_file=None):

    hDeltaY_SM = ROOT.TH1F("hDeltaY_SM_%s" % wc_name, "SM #DeltaY_{reco};#DeltaY_{reco};Events", 14, -3, 3)
    hDeltaY_EFT = hDeltaY_SM.Clone("hDeltaY_EFT_%s" % wc_name)
    hDeltaY_SM_norm = hDeltaY_SM.Clone("hDeltaY_SM_norm_%s" % wc_name)
    hDeltaY_EFT_norm = hDeltaY_SM.Clone("hDeltaY_EFT_norm_%s" % wc_name)
    
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
            
        deltaY = tree.DeltaY_reco
        hDeltaY_SM.Fill(deltaY, sm_weight)
        hDeltaY_EFT.Fill(deltaY, eft_weight)
    
    # Normalize histograms
    if hDeltaY_SM.Integral() > 0:
        hDeltaY_SM_norm.Add(hDeltaY_SM)
        hDeltaY_SM_norm.Scale(1.0 / hDeltaY_SM_norm.Integral())
    
    if hDeltaY_EFT.Integral() > 0:
        hDeltaY_EFT_norm.Add(hDeltaY_EFT)
        hDeltaY_EFT_norm.Scale(1.0 / hDeltaY_EFT_norm.Integral())
    
    # Create ratio histogram
    hRatio_norm = hDeltaY_EFT_norm.Clone("hRatio_norm_deltaY_%s" % wc_name)
    hRatio_norm.Divide(hDeltaY_SM_norm)
    
    # Create canvas for overlay plot
    c_overlay = ROOT.TCanvas("c_overlay_%s" % wc_name, "DeltaY Reco: EFT vs SM (%s)" % wc_name, 800, 600)
    c_overlay.SetLeftMargin(0.15)
    c_overlay.SetRightMargin(0.05)
    
    # Set up normalized histograms
    hDeltaY_SM_norm.SetTitle("")
    hDeltaY_SM_norm.GetXaxis().SetTitle("#DeltaY_{reco}")
    hDeltaY_SM_norm.GetYaxis().SetTitle("Normalized Events")
    hDeltaY_SM_norm.GetYaxis().SetTitleOffset(1.5)
    
    # Style for SM histogram
    hDeltaY_SM_norm.SetLineColor(ROOT.kBlack)
    hDeltaY_SM_norm.SetLineWidth(2)
    hDeltaY_SM_norm.SetMarkerStyle(20)  # Filled circle
    hDeltaY_SM_norm.SetMarkerSize(0.8)
    hDeltaY_SM_norm.SetMarkerColor(ROOT.kBlack)
    
    # Style for EFT histogram
    hDeltaY_EFT_norm.SetLineColor(ROOT.kRed)
    hDeltaY_EFT_norm.SetLineWidth(2)
    hDeltaY_EFT_norm.SetMarkerStyle(21)  # Filled square
    hDeltaY_EFT_norm.SetMarkerSize(0.8)
    hDeltaY_EFT_norm.SetMarkerColor(ROOT.kRed)
    
    # Set y-axis range from 0 to 0.4
    hDeltaY_SM_norm.GetYaxis().SetRangeUser(0, 0.4)
    
    # Draw normalized distributions with lines, points and error bars
    hDeltaY_SM_norm.Draw("HIST")  # Draw histogram with line
    hDeltaY_SM_norm.Draw("E1 SAME")  # Add error bars
    hDeltaY_EFT_norm.Draw("HIST SAME")  # Draw histogram with line
    hDeltaY_EFT_norm.Draw("E1 SAME")  # Add error bars
    
    # Add legend
    leg = ROOT.TLegend(0.65, 0.75, 0.89, 0.89)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.AddEntry(hDeltaY_SM_norm, "SM", "lep")  # l for line, p for point, e for error
    leg.AddEntry(hDeltaY_EFT_norm, plot_title, "lep")
    leg.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    # Create canvas for ratio plot
    c_ratio = ROOT.TCanvas("c_ratio_%s" % wc_name, "DeltaY Reco: EFT/SM Ratio (%s)" % wc_name, 800, 600)
    c_ratio.SetLeftMargin(0.15)
    c_ratio.SetRightMargin(0.05)
    c_ratio.SetGridy()
    
    # Style for ratio plot
    hRatio_norm.SetTitle("")
    hRatio_norm.GetXaxis().SetTitle("#DeltaY_{reco}")
    hRatio_norm.GetYaxis().SetTitle("EFT/SM (normalized)")
    hRatio_norm.GetYaxis().SetTitleOffset(1.5)
    hRatio_norm.GetYaxis().SetRangeUser(0, 1.5)
    hRatio_norm.SetLineColor(ROOT.kBlue)
    hRatio_norm.SetLineWidth(2)
    hRatio_norm.SetMarkerStyle(20)  # Filled circle
    hRatio_norm.SetMarkerSize(0.8)
    hRatio_norm.SetMarkerColor(ROOT.kBlue)
    
    # Draw ratio with error bars and line
    hRatio_norm.Draw("HIST")  # Draw histogram with line
    hRatio_norm.Draw("E1 SAME")  # Add error bars
    
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
    c_overlay.SaveAs(os.path.join(output_dir, "DeltaY_reco_EFT_vs_SM_%s.pdf" % filename_suffix))
    c_ratio.SaveAs(os.path.join(output_dir, "DeltaY_reco_EFT_vs_SM_normalized_ratio_%s.pdf" % filename_suffix))
    
    # If output_root_file is provided, save histograms to it
    if output_root_file:
        output_root_file.cd()
        hDeltaY_SM.Write()
        hDeltaY_EFT.Write()
        # Don't save normalized histograms to ROOT file
        # hDeltaY_SM_norm.Write()
        # hDeltaY_EFT_norm.Write()
        # hRatio_norm.Write()
    
    # Clean up
    c_overlay.Close()
    c_ratio.Close()

# This function creates a combined ratio plot for all 16 Wilson coefficients
def create_combined_ratio_plot(tree, structures, output_dir="plots", use_custom_wc=False, output_root_file=None):

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
    h_SM = ROOT.TH1F("h_SM_deltaY", "SM #DeltaY", 20, -2.5, 2.5)
    
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
        h_SM.Fill(tree.DeltaY_reco, sm_weight)
    
    # Normalize SM histogram
    h_SM.Scale(1.0 / h_SM.Integral())
    
    # Create and fill EFT histograms for each Wilson coefficient
    i = 0
    for wc_name, wc_index in wc_dict.items():
        # Create histogram for this WC
        h_EFT = ROOT.TH1F("h_EFT_deltaY_" + wc_name, "EFT #DeltaY " + wc_name, 20, -2.5, 2.5)
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
            h_EFT.Fill(tree.DeltaY_reco, eft_weight)
        
        # Normalize EFT histogram
        h_EFT.Scale(1.0 / h_EFT.Integral())
        
        # Create ratio histogram
        hRatio = h_EFT.Clone("hRatio_norm_deltaY_" + wc_name)
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
    c_ratio = ROOT.TCanvas("c_ratio_deltaY", "Ratio Plot", 1000, 800)
    c_ratio.SetLeftMargin(0.15)
    c_ratio.SetRightMargin(0.20)
    c_ratio.SetGridy()
    
    # Create a dummy histogram for the axes
    h_dummy = ROOT.TH1F("h_dummy_deltaY", "", 20, -2.5, 2.5)
    h_dummy.SetTitle("")
    h_dummy.GetXaxis().SetTitle("#DeltaY_{reco}")
    h_dummy.GetYaxis().SetTitle("EFT/SM (normalized)")
    h_dummy.GetYaxis().SetTitleOffset(1.5)
    h_dummy.GetYaxis().SetRangeUser(0.5, 1.5)
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
    line = ROOT.TLine(-2.5, 1.0, 2.5, 1.0)
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
    c_ratio.SaveAs(os.path.join(output_dir, "ratio_plot_deltaY.pdf"))
    
    # No need to save histograms to ROOT file - they're already saved by the individual plot functions
    
    return ratio_hists

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

def main():
    if len(sys.argv) < 3:
        print("Usage: python plot_deltaY_shape.py <structure_constants.npy> <myFile.root> [--custom-wc] [--print-only] [--compare-ctGRe1] [--compare-cQj18] [--output-root <output.root>] [--output-dir <output_dir>]")
        sys.exit(1)
    
    struct_file = sys.argv[1]
    root_file = sys.argv[2]
    
    # Parse command line options
    use_custom_wc = "--custom-wc" in sys.argv
    print_only = "--print-only" in sys.argv
    compare_ctGRe1 = "--compare-ctGRe1" in sys.argv
    compare_cQj18 = "--compare-cQj18" in sys.argv
    
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
    output_dir = "deltaY_plots"  # Default
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
    elif compare_cQj18:
        # Compare calculated weights with weights from the ROOT file for cQj18=1
        compare_cQj18_weights(tree, structures)
    elif print_only:
        # Just print weights for the first few events
        print_event_weights(tree, structures)
    else:
        # Create output directory
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Create plots for each Wilson coefficient
        print("\nGenerating plots for all Wilson coefficients...")
        for wc_index, wc_name in WC_NAMES.items():
            print("Processing %s (index %d)..." % (wc_name, wc_index))
            plot_single_wc(tree, structures, wc_index, wc_name, output_dir, use_custom_wc, output_root_file)

        
        # ratio plot
        print("\nGenerating combined ratio plot for all Wilson coefficients...")
        create_combined_ratio_plot(tree, structures, output_dir, use_custom_wc, output_root_file)
        
        print("\nAll plots saved in directory:", output_dir)
        if output_root_file:
            output_root_file.Close()
            print("All histograms saved to ROOT file:", output_root_filename)
    f.Close()

if __name__ == "__main__":
    main()
