# This script:
#   - Loads the computed EFT structure constants (saved as a .npy file).
#   - Retrieves DeltaYreco (branch) from the TTree "AnalysisTree"
#   - For each event, it gets the SM weight from genInfo->systweights()[202] (SM)
#     and computes the EFT weight for a chosen Wilson coefficient (here we set cQd1 = 10, all others 0).
#   - It then fills two histograms: one for the SM dY distribution and one reweighted for EFT.
#   - Finally, it creates a ratio plot (EFT/SM).
  
# Usage:
#   python plot_deltaY_shape.py <structure_constants.npy> /data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_ttree/uhh2.AnalysisModuleRunner.MC.MC_EFT_Mttbar_0-700_UL17_2.root


import sys
import ROOT
import numpy as np
from itertools import combinations # To generate combinations of Wilson coefficients
import os

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
    print "Loaded structure constants from", fname, "with shape:", arr.shape
    return arr

# 3. Main script
# This function creates normalized distribution and ratio plots for a single Wilson coefficient
def plot_single_wc(tree, structures, wc_index, wc_name, output_dir="plots"):

    hDeltaY_SM = ROOT.TH1F("hDeltaY_SM_%s" % wc_name, "SM #DeltaY_{reco};#DeltaY_{reco};Events", 40, -5, 5)
    hDeltaY_EFT = hDeltaY_SM.Clone("hDeltaY_EFT_%s" % wc_name)
    hDeltaY_SM_norm = hDeltaY_SM.Clone("hDeltaY_SM_norm_%s" % wc_name)
    hDeltaY_EFT_norm = hDeltaY_SM.Clone("hDeltaY_EFT_norm_%s" % wc_name)
    
    # Set up WC values (one WC = 10, others = 0)
    num_WCs = 16
    wc_values = [0.0] * num_WCs
    wc_values[wc_index] = 10.0
    
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
    hRatio_norm = hDeltaY_EFT_norm.Clone("hRatio_norm_%s" % wc_name)
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
    
    # Set all bin errors to zero to remove error bars
    for i in range(1, hDeltaY_SM_norm.GetNbinsX() + 1):
        hDeltaY_SM_norm.SetBinError(i, 0)
        hDeltaY_EFT_norm.SetBinError(i, 0)
    
    # Draw normalized distributions with lines and points
    # First draw histograms as lines
    hDeltaY_SM_norm.Draw("HIST")  # Draw just the line
    hDeltaY_EFT_norm.Draw("HIST SAME")  # Draw the EFT line
    
    # Then add points on top
    hDeltaY_SM_norm.Draw("P SAME")  # Add SM points
    hDeltaY_EFT_norm.Draw("P SAME")  # Add EFT points
    
    # Add legend
    leg = ROOT.TLegend(0.65, 0.75, 0.89, 0.89)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.AddEntry(hDeltaY_SM_norm, "SM", "lp")  # l for line, p for point
    leg.AddEntry(hDeltaY_EFT_norm, "%s = 10" % wc_name, "lp")
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
    hRatio_norm.GetYaxis().SetRangeUser(0.5, 1.5)
    hRatio_norm.SetLineColor(ROOT.kBlue)
    hRatio_norm.SetLineWidth(2)
    hRatio_norm.SetMarkerStyle(20)  # Filled circle
    hRatio_norm.SetMarkerSize(0.8)
    hRatio_norm.SetMarkerColor(ROOT.kBlue)
    
    # Set all bin errors to zero for ratio
    for i in range(1, hRatio_norm.GetNbinsX() + 1):
        hRatio_norm.SetBinError(i, 0)
    
    # Draw ratio with line and points
    hRatio_norm.Draw("HIST")  # Draw line first
    hRatio_norm.Draw("P SAME")  # Add points on top
    
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
    
    # Save plots
    c_overlay.SaveAs(os.path.join(output_dir, "DeltaY_reco_EFT_vs_SM_normalized_overlay_%s.pdf" % wc_name))
    c_ratio.SaveAs(os.path.join(output_dir, "DeltaY_reco_EFT_vs_SM_normalized_ratio_%s.pdf" % wc_name))
    
    # Clean up
    c_overlay.Close()
    c_ratio.Close()

# This function creates a combined ratio plot for all 16 Wilson coefficients
def create_combined_ratio_plot(tree, structures, output_dir="plots"):

    # Dictionary of Wilson coefficients and their indices
    WC_NAMES = {
        0: "ctGRe", 1: "ctGIm", 2: "cQj18", 3: "cQj38",
        4: "cQj11", 5: "cQj31", 6: "ctu8", 7: "ctd8",
        8: "ctj8", 9: "cQu8", 10: "cQd8", 11: "ctu1",
        12: "ctd1", 13: "ctj1", 14: "cQu1", 15: "cQd1"
    }
    
    # Create canvas for combined ratio plot
    c_combined = ROOT.TCanvas("c_combined_ratio", "DeltaY Reco: All EFT/SM Ratios", 1000, 800)
    c_combined.SetLeftMargin(0.15)
    c_combined.SetRightMargin(0.20) 
    c_combined.SetGridy()
    
    h_dummy = ROOT.TH1F("h_dummy", "", 40, -5, 5)
    h_dummy.SetTitle("")
    h_dummy.GetXaxis().SetTitle("#DeltaY_{reco}")
    h_dummy.GetYaxis().SetTitle("EFT/SM (normalized)")
    h_dummy.GetYaxis().SetTitleOffset(1.5)
    h_dummy.GetYaxis().SetRangeUser(0.0, 2.0)
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
    print "Creating SM histogram for ratio calculations..."
    hDeltaY_SM = ROOT.TH1F("hDeltaY_SM_combined", "SM #DeltaY_{reco}", 40, -5, 5)
    
    # Fill SM histogram 
    nentries = tree.GetEntries()
    print "Processing %d events for SM histogram..." % nentries
    for ientry in range(nentries):
        if ientry % 10000 == 0 and ientry > 0:
            print "  Processed %d / %d events" % (ientry, nentries)
        tree.GetEntry(ientry)
        sm_weight = tree.genInfo.systweights()[202]
        if sm_weight == 0:
            continue
        deltaY = tree.DeltaY_reco
        hDeltaY_SM.Fill(deltaY, sm_weight)
    
    # Normalize SM histogram
    if hDeltaY_SM.Integral() > 0:
        hDeltaY_SM.Scale(1.0 / hDeltaY_SM.Integral())
    
    # Now process each Wilson coefficient
    print "Creating EFT histograms for all Wilson coefficients..."
    for i, (wc_index, wc_name) in enumerate(WC_NAMES.items()):
        print "Processing %s (index %d)..." % (wc_name, wc_index)
        
        # Create EFT histogram
        hDeltaY_EFT = ROOT.TH1F("hDeltaY_EFT_%s" % wc_name, "EFT #DeltaY_{reco}", 40, -5, 5)
        
        # Set up WC values (one WC = 10, others = 0)
        num_WCs = 16
        wc_values = [0.0] * num_WCs
        wc_values[wc_index] = 10.0
        
        # Fill EFT histogram
        for ientry in range(nentries):
            tree.GetEntry(ientry)
            event_struct = structures[ientry]
            
            eft_weight = event_weights_lin_quad(event_struct, wc_values)
            deltaY = tree.DeltaY_reco
            hDeltaY_EFT.Fill(deltaY, eft_weight)
        
        # Normalize EFT histogram
        if hDeltaY_EFT.Integral() > 0:
            hDeltaY_EFT.Scale(1.0 / hDeltaY_EFT.Integral())
        
        # Create ratio histogram
        hRatio = hDeltaY_EFT.Clone("hRatio_%s" % wc_name)
        hRatio.Divide(hDeltaY_SM)
        
        # Set all bin errors to zero
        for j in range(1, hRatio.GetNbinsX() + 1):
            hRatio.SetBinError(j, 0)
        
        # Style for ratio histogram
        color = colors[i]
        hRatio.SetLineColor(color)
        hRatio.SetLineWidth(2)
        hRatio.SetMarkerStyle(20 + i % 10) 
        hRatio.SetMarkerSize(0.8)
        hRatio.SetMarkerColor(color)
        
        hRatio.Draw("HIST SAME")
        hRatio.Draw("P SAME")
        
        leg.AddEntry(hRatio, wc_name, "lp")
        
        ratio_hists.append(hRatio)
    
    line = ROOT.TLine(-5, 1, 5, 1)
    line.SetLineStyle(2)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)
    line.Draw("same")
    
    leg.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    c_combined.SaveAs(os.path.join(output_dir, "DeltaY_reco_EFT_vs_SM_all_ratios.pdf"))
    
    c_combined.Close()

def main():
    if len(sys.argv) < 3:
        print "Usage: python plot_deltaY_shape.py <structure_constants.npy> <myFile.root>"
        sys.exit(1)
    
    struct_file = sys.argv[1]
    root_file = sys.argv[2]
    
    # Load structure constants
    structures = load_structure_constants(struct_file)
    
    f = ROOT.TFile.Open(root_file)
    if not f or f.IsZombie():
        print "Error: Cannot open file", root_file
        sys.exit(1)
    
    # Get TTree
    tree = f.Get("AnalysisTree")
    if not tree:
        print "Error: Cannot find TTree 'AnalysisTree'"
        sys.exit(1)
    
    # Dictionary of Wilson coefficients and their indices
    WC_NAMES = {
        0: "ctGRe", 1: "ctGIm", 2: "cQj18", 3: "cQj38",
        4: "cQj11", 5: "cQj31", 6: "ctu8", 7: "ctd8",
        8: "ctj8", 9: "cQu8", 10: "cQd8", 11: "ctu1",
        12: "ctd1", 13: "ctj1", 14: "cQu1", 15: "cQd1"
    }
    
    # Create output directory
    output_dir = "deltaY_plots"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Comment out individual WC plots to speed up the process
    # # Create plots for each Wilson coefficient
    # print "\nGenerating plots for all Wilson coefficients..."
    # for wc_index, wc_name in WC_NAMES.items():
    #     print "Processing %s (index %d)..." % (wc_name, wc_index)
    #     plot_single_wc(tree, structures, wc_index, wc_name, output_dir)

    
    # ratio plot
    print "\nGenerating combined ratio plot for all Wilson coefficients..."
    create_combined_ratio_plot(tree, structures, output_dir)
    
    print "\nAll plots saved in directory:", output_dir
    f.Close()

if __name__ == "__main__":
    main()
