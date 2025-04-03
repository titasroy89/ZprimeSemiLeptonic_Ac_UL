#!/usr/bin/env python
"""
Script to create combined ratio plots from existing ROOT files.
This script reads the individual ratio histograms from ROOT files and creates combined plots with all 16 Wilson coefficients on the same canvas.

Usage:
    python create_combined_plots.py <input_root_file> [--output-dir <output_directory>]
    single root file: python create_combined_plots.py combined_output/root_files/uhh2.AnalysisModuleRunner.MC.MC_EFT_Mttbar_0-700_UL17_8_plots.root --output-dir combined_plots/Mttbar_0-700
    directory: python create_combined_plots.py combined_output/root_files/ --output-dir combined_plots
"""

import os
import sys
import glob
import argparse
import ROOT

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True) 

# Dictionary of Wilson coefficients and their indices
WC_NAMES = [
    "ctGRe", "ctGIm", "cQj18", "cQj38",
    "cQj11", "cQj31", "ctu8", "ctd8",
    "ctj8", "cQu8", "cQd8", "ctu1",
    "ctd1", "ctj1", "cQu1", "cQd1"
]

def create_combined_ratio_plot(root_file, variable, output_dir):
    #Create a combined ratio plot for a specific variable.
    # Define colors for different WCs
    colors = [
        ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kMagenta+1,
        ROOT.kCyan+2, ROOT.kOrange+7, ROOT.kViolet-3, ROOT.kSpring+9,
        ROOT.kTeal+1, ROOT.kYellow+2, ROOT.kAzure+1, ROOT.kPink+7,
        ROOT.kOrange-3, ROOT.kBlue-7, ROOT.kRed-7, ROOT.kGreen-7
    ]
    
    # Create canvas for combined ratio plot
    c_combined = ROOT.TCanvas("c_combined_{}".format(variable), "Combined {} Ratio Plot".format(variable), 1000, 800)
    c_combined.SetLeftMargin(0.15)
    c_combined.SetRightMargin(0.20)
    c_combined.SetGridy()
    
    if variable == "deltaY":
        h_dummy = ROOT.TH1F("h_dummy_" + variable, "", 14, -3, 3)
        x_title = "#DeltaY_{reco}"
        y_range_min = 0
        y_range_max = 2.7
    elif variable == "deltaPhi":
        h_dummy = ROOT.TH1F("h_dummy_" + variable, "", 16, -3.2, 3.2)
        x_title = "#Delta#phi"
        y_range_min = 0.9
        y_range_max = 1.1
    elif variable == "sigmaPhi":
        h_dummy = ROOT.TH1F("h_dummy_" + variable, "", 16, -3.2, 3.2)
        x_title = "#sigma#phi"
        y_range_min = 0.9
        y_range_max = 1.1
    else:
        print("Unknown variable: {}".format(variable))
        return
    
    h_dummy.SetTitle("")
    h_dummy.GetXaxis().SetTitle(x_title)
    h_dummy.GetYaxis().SetTitle("EFT/SM (normalized)")
    h_dummy.GetYaxis().SetTitleOffset(1.5)
    h_dummy.GetYaxis().SetRangeUser(y_range_min, y_range_max)
    h_dummy.SetStats(0)
    h_dummy.Draw()
    
    # Create legend
    leg = ROOT.TLegend(0.82, 0.15, 0.95, 0.85)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    
    # Get SM histogram first (we'll need it for each ratio)
    if variable == "deltaY":
        sm_hist_prefix = "hDeltaY_SM_"
    elif variable == "deltaPhi":
        sm_hist_prefix = "hDeltaPhi_SM_"
    elif variable == "sigmaPhi":
        sm_hist_prefix = "hSigmaPhi_SM_"
    
    # Try to get the SM histogram (both normalized and nonnormalized)
    sm_hist = None
    sm_already_normalized = False
    
    # First try with the first WC name (they should all have the same SM histogram)
    sm_hist_name = sm_hist_prefix + WC_NAMES[0]
    print("Trying to find SM histogram: {}".format(sm_hist_name))
    sm_hist = root_file.Get(sm_hist_name)
    
    # If not found, try normalized version
    if not sm_hist:
        sm_hist_name = sm_hist_prefix + "norm_" + WC_NAMES[0]
        print("Trying to find SM histogram: {}".format(sm_hist_name))
        sm_hist = root_file.Get(sm_hist_name)
        if sm_hist:
            sm_already_normalized = True
            print("Using normalized SM histogram: {}".format(sm_hist_name))
    
    # If still not found, try without WC name
    if not sm_hist:
        sm_hist_name = sm_hist_prefix.rstrip("_")
        print("Trying to find SM histogram: {}".format(sm_hist_name))
        sm_hist = root_file.Get(sm_hist_name)
    
    # If still not found, try normalized version without WC name
    if not sm_hist:
        sm_hist_name = sm_hist_prefix.rstrip("_") + "_norm"
        print("Trying to find SM histogram: {}".format(sm_hist_name))
        sm_hist = root_file.Get(sm_hist_name)
        if sm_hist:
            sm_already_normalized = True
            print("Using normalized SM histogram: {}".format(sm_hist_name))
    
    # Try with h_ prefix instead of h prefix
    if not sm_hist and variable == "sigmaPhi":
        sm_hist_name = "h_SM_sigmaPhi"
        print("Trying to find SM histogram: {}".format(sm_hist_name))
        sm_hist = root_file.Get(sm_hist_name)
    
    # Try with h_ prefix and normalized
    if not sm_hist and variable == "sigmaPhi":
        sm_hist_name = "h_SM_sigmaPhi_norm"
        print("Trying to find SM histogram: {}".format(sm_hist_name))
        sm_hist = root_file.Get(sm_hist_name)
        if sm_hist:
            sm_already_normalized = True
            print("Using normalized SM histogram: {}".format(sm_hist_name))
    
    # Last resort: list all keys in the file to find potential matches
    if not sm_hist:
        print("Could not find SM histogram with standard naming patterns. Listing all keys:")
        for key in root_file.GetListOfKeys():
            key_name = key.GetName()
            if "SM" in key_name and variable.lower() in key_name.lower():
                print("  Potential match: {}".format(key_name))
                # Try this key
                sm_hist = root_file.Get(key_name)
                if sm_hist:
                    sm_hist_name = key_name
                    print("Using histogram: {}".format(sm_hist_name))
                    # Check if it's normalized
                    if "norm" in key_name.lower():
                        sm_already_normalized = True
                    break
    
    if not sm_hist:
        print("Error: Could not find SM histogram for {}".format(variable))
        return
    
    # Clone SM histogram
    sm_hist_clone = sm_hist.Clone("sm_hist_clone_" + variable)
    
    # Normalize SM histogram if not already normalized
    if not sm_already_normalized and sm_hist_clone.Integral() > 0:
        sm_hist_clone.Scale(1.0 / sm_hist_clone.Integral())
    
    # Get and draw all ratio histograms
    ratio_hists = []
    for i, wc_name in enumerate(WC_NAMES):
        # First try to get the ratio histogram directly
        hist_name = "hRatio_norm_{}_{}".format(variable, wc_name)
        hist = root_file.Get(hist_name)
        
        # If ratio histogram exists, use it
        if hist:
            print("Using existing ratio histogram: {}".format(hist_name))
            ratio_hist = hist.Clone("ratio_{}_{}_combined".format(variable, wc_name))
        else:
            # Otherwise, try to get the EFT histogram and create the ratio
            if variable == "deltaY":
                eft_hist_name = "hDeltaY_EFT_{}".format(wc_name)
            elif variable == "deltaPhi":
                eft_hist_name = "hDeltaPhi_EFT_{}".format(wc_name)
            elif variable == "sigmaPhi":
                eft_hist_name = "hSigmaPhi_EFT_{}".format(wc_name)
            
            print("Trying to find EFT histogram: {}".format(eft_hist_name))
            eft_hist = root_file.Get(eft_hist_name)
            eft_already_normalized = False
            
            # If not found, try normalized version
            if not eft_hist:
                if variable == "deltaY":
                    eft_hist_name = "hDeltaY_EFT_norm_{}".format(wc_name)
                elif variable == "deltaPhi":
                    eft_hist_name = "hDeltaPhi_EFT_norm_{}".format(wc_name)
                elif variable == "sigmaPhi":
                    eft_hist_name = "hSigmaPhi_EFT_norm_{}".format(wc_name)
                
                print("Trying to find EFT histogram: {}".format(eft_hist_name))
                eft_hist = root_file.Get(eft_hist_name)
                if eft_hist:
                    eft_already_normalized = True
                    print("Using normalized EFT histogram: {}".format(eft_hist_name))
            
            # Try with h_ prefix instead of h prefix
            if not eft_hist and variable == "sigmaPhi":
                eft_hist_name = "h_EFT_sigmaPhi_{}".format(wc_name)
                print("Trying to find EFT histogram: {}".format(eft_hist_name))
                eft_hist = root_file.Get(eft_hist_name)
            
            # Try with h_ prefix and normalized
            if not eft_hist and variable == "sigmaPhi":
                eft_hist_name = "h_EFT_sigmaPhi_{}_norm".format(wc_name)
                print("Trying to find EFT histogram: {}".format(eft_hist_name))
                eft_hist = root_file.Get(eft_hist_name)
                if eft_hist:
                    eft_already_normalized = True
                    print("Using normalized EFT histogram: {}".format(eft_hist_name))
            
            # Last resort: list all keys in the file to find potential matches
            if not eft_hist:
                print("Could not find EFT histogram with standard naming patterns for {}. Listing potential matches:".format(wc_name))
                for key in root_file.GetListOfKeys():
                    key_name = key.GetName()
                    if "EFT" in key_name and variable.lower() in key_name.lower() and wc_name in key_name:
                        print("  Potential match: {}".format(key_name))
                        # Try this key
                        eft_hist = root_file.Get(key_name)
                        if eft_hist:
                            eft_hist_name = key_name
                            print("Using histogram: {}".format(eft_hist_name))
                            # Check if it's normalized
                            if "norm" in key_name.lower():
                                eft_already_normalized = True
                            break
            
            if not eft_hist:
                print("Warning: Could not find EFT histogram for {} {}".format(variable, wc_name))
                continue
            
            # Clone EFT histogram
            eft_hist_clone = eft_hist.Clone("eft_hist_clone_{}_{}".format(variable, wc_name))
            
            # Normalize EFT histogram if not already normalized
            if not eft_already_normalized and eft_hist_clone.Integral() > 0:
                eft_hist_clone.Scale(1.0 / eft_hist_clone.Integral())
            
            # Create ratio histogram
            ratio_hist = eft_hist_clone.Clone("ratio_{}_{}_combined".format(variable, wc_name))
            ratio_hist.Divide(sm_hist_clone)
        
        # Set style for ratio histogram
        color = colors[i % len(colors)]  # Ensure we don't go out of bounds
        ratio_hist.SetLineColor(color)
        ratio_hist.SetLineWidth(2)
        ratio_hist.SetMarkerStyle(20 + i % 10)
        ratio_hist.SetMarkerSize(0.8)
        ratio_hist.SetMarkerColor(color)
        
        # Remove error bars for combined plot
        for bin in range(1, ratio_hist.GetNbinsX() + 1):
            ratio_hist.SetBinError(bin, 0)
        
        # Draw the histogram
        ratio_hist.Draw("HIST SAME")
        ratio_hist.Draw("P SAME")  # Add points
        
        # Add to legend
        leg.AddEntry(ratio_hist, wc_name + " = 10", "lp")
        
        # Store for later
        ratio_hists.append(ratio_hist)
    
    # Draw horizontal line at y=1
    if variable == "deltaY":
        line = ROOT.TLine(-3, 1, 3, 1)
    elif variable == "deltaPhi":
        line = ROOT.TLine(-3.2, 1, 3.2, 1)
    elif variable == "sigmaPhi":
        line = ROOT.TLine(-3.2, 1, 3.2, 1)
    
    line.SetLineStyle(2)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)
    line.Draw("same")
    
    # Draw legend
    leg.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save canvas as PDF
    output_file = os.path.join(output_dir, "combined_{}_ratio_plot.pdf".format(variable))
    c_combined.SaveAs(output_file)
    print("Saved combined {} ratio plot to {}".format(variable, output_file))
    
    return c_combined

def process_root_file(root_file_path, output_dir):
    # Process a ROOT file and create combined ratio plots for all variables.
    # Open the ROOT file
    root_file = ROOT.TFile.Open(root_file_path, "READ")
    if not root_file or root_file.IsZombie():
        print("Error: Could not open ROOT file: {}".format(root_file_path))
        return False
    
    # Create combined ratio plots for each variable
    create_combined_ratio_plot(root_file, "deltaY", output_dir)
    create_combined_ratio_plot(root_file, "deltaPhi", output_dir)
    create_combined_ratio_plot(root_file, "sigmaPhi", output_dir)
    
    root_file.Close()
    
    return True

def main():
    parser = argparse.ArgumentParser(description="Create combined ratio plots from ROOT files")
    parser.add_argument("input_path", help="Path to ROOT file or directory containing ROOT files")
    parser.add_argument("--output-dir", default="combined_plots", help="Output directory for PDF plots")
    
    args = parser.parse_args()
    
    # Process the input path
    if os.path.isdir(args.input_path):
        # Process all ROOT files in the directory
        root_files = glob.glob(os.path.join(args.input_path, "*.root"))
        if not root_files:
            print("No ROOT files found in directory: {}".format(args.input_path))
            return False
        
        print("Found {} ROOT files to process".format(len(root_files)))
        for i, root_file in enumerate(root_files):
            print("\nProcessing file [{}/{}]: {}".format(i+1, len(root_files), os.path.basename(root_file)))
            file_output_dir = os.path.join(args.output_dir, os.path.splitext(os.path.basename(root_file))[0])
            process_root_file(root_file, file_output_dir)
    
    elif os.path.isfile(args.input_path) and args.input_path.endswith(".root"):
        # Process a single ROOT file
        process_root_file(args.input_path, args.output_dir)
    
    else:
        print("Error: Input path is not a ROOT file or directory: {}".format(args.input_path))
        return False
    
    print("\nAll combined ratio plots have been created in: {}".format(args.output_dir))
    return True

if __name__ == "__main__":
    main() 