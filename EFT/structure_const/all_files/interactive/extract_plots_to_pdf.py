"""
Script to extract plots from ROOT files and save them as PDFs.
This script will:
1. Open a ROOT file containing histograms
2. Extract all histograms and save them as PDFs with the exact same formatting as in the original scripts
3. Organize the PDFs in the same directory structure as the original scripts

Usage:
    python extract_plots_to_pdf.py <input_root_file> [--output-dir <output_directory>]
    python extract_plots_to_pdf.py combined_output_v1/root_files/uhh2.AnalysisModuleRunner.MC.MC_EFT_Mttbar_0-700_UL17_36_all_plots.root --output-dir plots_with_extractplotscript
"""

import os
import sys
import glob
import argparse
import ROOT

ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True) 

def extract_and_save_plots(root_file_path, output_dir):
    # Extract plots from ROOT file and save them as PDFs.
    if not os.path.exists(root_file_path):
        print("Error: ROOT file not found: {}".format(root_file_path))
        return False
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create subdirectories for different plot types
    deltaY_dir = os.path.join(output_dir, "deltaY_plots")
    delta_phi_dir = os.path.join(output_dir, "delta_phi_plots")
    sigma_phi_dir = os.path.join(output_dir, "sigma_phi_plots")
    
    for directory in [deltaY_dir, delta_phi_dir, sigma_phi_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    # Open ROOT file
    root_file = ROOT.TFile.Open(root_file_path, "READ")
    if not root_file or root_file.IsZombie():
        print("Error: Could not open ROOT file: {}".format(root_file_path))
        return False
    
    # List of Wilson coefficients
    WC_NAMES = [
        "ctGRe", "ctGIm", "cQj38", "cQj18", "ctj8", "cQu8", 
        "ctu8", "cQd8", "ctd8", "cQj31", "cQj11", "ctj1", 
        "cQu1", "ctu1", "cQd1", "ctd1"
    ]
    
    print("Scanning ROOT file for histograms...")
    num_plots_saved = 0
    
    # Process deltaY plots
    print("\nProcessing deltaY plots...")
    for wc_name in WC_NAMES:
        print("  Processing Wilson coefficient: {}".format(wc_name))
        
        # Get the SM histogram (nonnormalized)
        h_sm_name = "hDeltaY_SM_{}".format(wc_name)
        h_sm = root_file.Get(h_sm_name)
        already_normalized = False
        
        # If nonnormalized histogram not found, try normalized version
        if not h_sm:
            h_sm_name = "hDeltaY_SM_norm_{}".format(wc_name)
            h_sm = root_file.Get(h_sm_name)
            print("  Trying normalized SM histogram: {}".format(h_sm_name))
            already_normalized = True
            
        if not h_sm:
            print("  Warning: SM histogram not found, skipping {}".format(wc_name))
            continue
            
        # Get the EFT histogram (nonnormalized)
        h_eft_name = "hDeltaY_EFT_{}".format(wc_name)
        h_eft = root_file.Get(h_eft_name)
        
        # If nonnormalized histogram not found, try normalized version
        if not h_eft:
            h_eft_name = "hDeltaY_EFT_norm_{}".format(wc_name)
            h_eft = root_file.Get(h_eft_name)
            print("  Trying normalized EFT histogram: {}".format(h_eft_name))
            
        if not h_eft:
            print("  Warning: EFT histogram not found, skipping {}".format(wc_name))
            continue
            
        # Clone histograms
        h_sm_clone = h_sm.Clone("h_sm_clone_deltaY")
        h_eft_clone = h_eft.Clone("h_eft_clone_deltaY_{}".format(wc_name))
        
        # Create normalized versions
        h_sm_norm = h_sm_clone.Clone("h_sm_norm_deltaY")
        h_eft_norm = h_eft_clone.Clone("h_eft_norm_deltaY_{}".format(wc_name))
        
        # Normalize histograms if they aren't already normalized
        if not already_normalized:
            if h_sm_norm.Integral() > 0:
                h_sm_norm.Scale(1.0 / h_sm_norm.Integral())
            if h_eft_norm.Integral() > 0:
                h_eft_norm.Scale(1.0 / h_eft_norm.Integral())
        
        # Create overlay plot
        c_overlay = ROOT.TCanvas("c_overlay_deltaY_{}".format(wc_name), "DeltaY Overlay", 800, 600)
        c_overlay.SetLeftMargin(0.15)
        c_overlay.SetRightMargin(0.05)
        c_overlay.SetTopMargin(0.08)
        c_overlay.SetBottomMargin(0.12)
        
        # Style for SM histogram
        h_sm_norm.SetTitle("")
        h_sm_norm.GetXaxis().SetTitle("#DeltaY_{reco}")
        h_sm_norm.GetYaxis().SetTitle("Normalized Events")
        h_sm_norm.GetYaxis().SetTitleOffset(1.5)
        h_sm_norm.GetYaxis().SetRangeUser(0, 0.3)
        h_sm_norm.SetLineColor(ROOT.kBlack)
        h_sm_norm.SetLineWidth(2)
        h_sm_norm.SetMarkerStyle(20)
        h_sm_norm.SetMarkerSize(0.8)
        h_sm_norm.SetMarkerColor(ROOT.kBlack)
        
        # Style for EFT histogram
        h_eft_norm.SetLineColor(ROOT.kRed)
        h_eft_norm.SetLineWidth(2)
        h_eft_norm.SetMarkerStyle(21)
        h_eft_norm.SetMarkerSize(0.8)
        h_eft_norm.SetMarkerColor(ROOT.kRed)
        
        # Draw histograms
        h_sm_norm.Draw("HIST E1")
        h_eft_norm.Draw("HIST E1 SAME")
        
        # Add legend
        legend = ROOT.TLegend(0.65, 0.75, 0.85, 0.85)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        legend.AddEntry(h_sm_norm, "SM", "l")
        legend.AddEntry(h_eft_norm, wc_name + " = 10", "l")
        legend.Draw()
        
        # Add CMS text
        cms_text = ROOT.TLatex()
        cms_text.SetNDC()
        cms_text.SetTextSize(0.04)
        cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
        
        # Save overlay plot
        overlay_pdf = os.path.join(deltaY_dir, "deltaY_overlay_{}.pdf".format(wc_name))
        c_overlay.SaveAs(overlay_pdf)
        num_plots_saved += 1
        
        # Create ratio plot
        c_ratio = ROOT.TCanvas("c_ratio_deltaY_{}".format(wc_name), "DeltaY Ratio", 800, 600)
        c_ratio.SetLeftMargin(0.15)
        c_ratio.SetRightMargin(0.05)
        c_ratio.SetTopMargin(0.08)
        c_ratio.SetBottomMargin(0.12)
        c_ratio.SetGridy()
        
        # Create ratio histogram from normalized histograms
        h_ratio = h_eft_norm.Clone("h_ratio_deltaY_{}".format(wc_name))
        h_ratio.Divide(h_sm_norm)
        
        # Style for ratio histogram
        h_ratio.SetTitle("")
        h_ratio.GetXaxis().SetTitle("#DeltaY_{reco}")
        h_ratio.GetYaxis().SetTitle("EFT/SM")
        h_ratio.GetYaxis().SetTitleOffset(1.5)
        h_ratio.GetYaxis().SetRangeUser(0, 2.5)
        h_ratio.SetLineColor(ROOT.kBlue)
        h_ratio.SetLineWidth(2)
        h_ratio.SetMarkerStyle(20)
        h_ratio.SetMarkerSize(0.8)
        h_ratio.SetMarkerColor(ROOT.kBlue)
        
        # Draw ratio histogram
        h_ratio.Draw("HIST E1")
        
        # Add horizontal line at y=1
        line = ROOT.TLine(-3, 1, 3, 1)
        line.SetLineStyle(2)
        line.SetLineColor(ROOT.kBlack)
        line.SetLineWidth(2)
        line.Draw("SAME")
        
        # Add CMS text
        cms_text = ROOT.TLatex()
        cms_text.SetNDC()
        cms_text.SetTextSize(0.04)
        cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
        
        # Save ratio plot
        ratio_pdf = os.path.join(deltaY_dir, "deltaY_ratio_{}.pdf".format(wc_name))
        c_ratio.SaveAs(ratio_pdf)
        num_plots_saved += 1
    
    # Process deltaPhi plots
    print("\nProcessing deltaPhi plots...")
    for wc_name in WC_NAMES:
        print("  Processing Wilson coefficient: {}".format(wc_name))
        
        # Get the SM histogram (nonnormalized)
        h_sm_name = "hDeltaPhi_SM_{}".format(wc_name)
        h_sm = root_file.Get(h_sm_name)
        already_normalized = False
        
        # If nonnormalized histogram not found, try normalized version
        if not h_sm:
            h_sm_name = "hDeltaPhi_SM_norm_{}".format(wc_name)
            h_sm = root_file.Get(h_sm_name)
            print("  Trying normalized SM histogram: {}".format(h_sm_name))
            already_normalized = True
            
        if not h_sm:
            print("  Warning: SM histogram not found, skipping {}".format(wc_name))
            continue
            
        # Get the EFT histogram (nonnormalized)
        h_eft_name = "hDeltaPhi_EFT_{}".format(wc_name)
        h_eft = root_file.Get(h_eft_name)
        
        # If nonnormalized histogram not found, try normalized version
        if not h_eft:
            h_eft_name = "hDeltaPhi_EFT_norm_{}".format(wc_name)
            h_eft = root_file.Get(h_eft_name)
            print("  Trying normalized EFT histogram: {}".format(h_eft_name))
            
        if not h_eft:
            print("  Warning: EFT histogram not found, skipping {}".format(wc_name))
            continue
            
        # Clone histograms to avoid modifying originals
        h_sm_clone = h_sm.Clone("h_sm_clone_deltaPhi")
        h_eft_clone = h_eft.Clone("h_eft_clone_deltaPhi_{}".format(wc_name))
        
        # Create normalized versions
        h_sm_norm = h_sm_clone.Clone("h_sm_norm_deltaPhi")
        h_eft_norm = h_eft_clone.Clone("h_eft_norm_deltaPhi_{}".format(wc_name))
        
        # Normalize histograms if they aren't already normalized
        if not already_normalized:
            if h_sm_norm.Integral() > 0:
                h_sm_norm.Scale(1.0 / h_sm_norm.Integral())
            if h_eft_norm.Integral() > 0:
                h_eft_norm.Scale(1.0 / h_eft_norm.Integral())
        
        # Create overlay plot
        c_overlay = ROOT.TCanvas("c_overlay_deltaPhi_{}".format(wc_name), "DeltaPhi Overlay", 800, 600)
        c_overlay.SetLeftMargin(0.15)
        c_overlay.SetRightMargin(0.05)
        c_overlay.SetTopMargin(0.08)
        c_overlay.SetBottomMargin(0.12)
        
        # Style for SM histogram
        h_sm_norm.SetTitle("")
        h_sm_norm.GetXaxis().SetTitle("#Delta#phi")
        h_sm_norm.GetYaxis().SetTitle("Normalized Events")
        h_sm_norm.GetYaxis().SetTitleOffset(1.5)
        h_sm_norm.GetYaxis().SetRangeUser(0.03, 0.1)
        h_sm_norm.SetLineColor(ROOT.kBlack)
        h_sm_norm.SetLineWidth(2)
        h_sm_norm.SetMarkerStyle(20)
        h_sm_norm.SetMarkerSize(0.8)
        h_sm_norm.SetMarkerColor(ROOT.kBlack)
        
        # Style for EFT histogram
        h_eft_norm.SetLineColor(ROOT.kRed)
        h_eft_norm.SetLineWidth(2)
        h_eft_norm.SetMarkerStyle(21)
        h_eft_norm.SetMarkerSize(0.8)
        h_eft_norm.SetMarkerColor(ROOT.kRed)
        
        # Draw histograms
        h_sm_norm.Draw("HIST E1")
        h_eft_norm.Draw("HIST E1 SAME")
        
        # Add legend
        legend = ROOT.TLegend(0.65, 0.75, 0.85, 0.85)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        legend.AddEntry(h_sm_norm, "SM", "l")
        legend.AddEntry(h_eft_norm, wc_name + " = 10", "l")
        legend.Draw()
        
        # Add CMS text
        cms_text = ROOT.TLatex()
        cms_text.SetNDC()
        cms_text.SetTextSize(0.04)
        cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
        
        # Save overlay plot
        overlay_pdf = os.path.join(delta_phi_dir, "deltaPhi_overlay_{}.pdf".format(wc_name))
        c_overlay.SaveAs(overlay_pdf)
        num_plots_saved += 1
        
        # Create ratio plot
        c_ratio = ROOT.TCanvas("c_ratio_deltaPhi_{}".format(wc_name), "DeltaPhi Ratio", 800, 600)
        c_ratio.SetLeftMargin(0.15)
        c_ratio.SetRightMargin(0.05)
        c_ratio.SetTopMargin(0.08)
        c_ratio.SetBottomMargin(0.12)
        c_ratio.SetGridy()
        
        # Create ratio histogram from normalized histograms
        h_ratio = h_eft_norm.Clone("h_ratio_deltaPhi_{}".format(wc_name))
        h_ratio.Divide(h_sm_norm)
        
        # Style for ratio histogram
        h_ratio.SetTitle("")
        h_ratio.GetXaxis().SetTitle("#Delta#phi")
        h_ratio.GetYaxis().SetTitle("EFT/SM")
        h_ratio.GetYaxis().SetTitleOffset(1.5)
        h_ratio.GetYaxis().SetRangeUser(0.9, 1.1)
        h_ratio.SetLineColor(ROOT.kBlue)
        h_ratio.SetLineWidth(2)
        h_ratio.SetMarkerStyle(20)
        h_ratio.SetMarkerSize(0.8)
        h_ratio.SetMarkerColor(ROOT.kBlue)
        
        # Draw ratio histogram
        h_ratio.Draw("HIST E1")
        
        # Add horizontal line at y=1
        line = ROOT.TLine(-3.2, 1, 3.2, 1)
        line.SetLineStyle(2)
        line.SetLineColor(ROOT.kBlack)
        line.SetLineWidth(2)
        line.Draw("SAME")
        
        # Add CMS text
        cms_text = ROOT.TLatex()
        cms_text.SetNDC()
        cms_text.SetTextSize(0.04)
        cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
        
        # Save ratio plot
        ratio_pdf = os.path.join(delta_phi_dir, "deltaPhi_ratio_{}.pdf".format(wc_name))
        c_ratio.SaveAs(ratio_pdf)
        num_plots_saved += 1
    
    # Process sigmaPhi plots
    print("\nProcessing sigmaPhi plots...")
    for wc_name in WC_NAMES:
        print("  Processing Wilson coefficient: {}".format(wc_name))
        
        # Get the SM histogram (non-normalized)
        h_sm_name = "hSigmaPhi_SM_{}".format(wc_name)
        h_sm = root_file.Get(h_sm_name)
        already_normalized = False
        
        # If non-normalized histogram not found, try normalized version
        if not h_sm:
            h_sm_name = "hSigmaPhi_SM_norm_{}".format(wc_name)
            h_sm = root_file.Get(h_sm_name)
            print("  Trying normalized SM histogram: {}".format(h_sm_name))
            already_normalized = True
            
        if not h_sm:
            print("  Warning: SM histogram not found, skipping {}".format(wc_name))
            continue
            
        # Get the EFT histogram (nonnormalized)
        h_eft_name = "hSigmaPhi_EFT_{}".format(wc_name)
        h_eft = root_file.Get(h_eft_name)
        
        # If nonnormalized histogram not found, try normalized version
        if not h_eft:
            h_eft_name = "hSigmaPhi_EFT_norm_{}".format(wc_name)
            h_eft = root_file.Get(h_eft_name)
            print("  Trying normalized EFT histogram: {}".format(h_eft_name))
            
        if not h_eft:
            print("  Warning: EFT histogram not found, skipping {}".format(wc_name))
            continue
            
        # Clone histograms to avoid modifying originals
        h_sm_clone = h_sm.Clone("h_sm_clone_sigmaPhi")
        h_eft_clone = h_eft.Clone("h_eft_clone_sigmaPhi_{}".format(wc_name))
        
        # Create normalized versions
        h_sm_norm = h_sm_clone.Clone("h_sm_norm_sigmaPhi")
        h_eft_norm = h_eft_clone.Clone("h_eft_norm_sigmaPhi_{}".format(wc_name))
        
        # Normalize histograms if they aren't already normalized
        if not already_normalized:
            if h_sm_norm.Integral() > 0:
                h_sm_norm.Scale(1.0 / h_sm_norm.Integral())
            if h_eft_norm.Integral() > 0:
                h_eft_norm.Scale(1.0 / h_eft_norm.Integral())
        
        # Create overlay plot
        c_overlay = ROOT.TCanvas("c_overlay_sigmaPhi_{}".format(wc_name), "SigmaPhi Overlay", 800, 600)
        c_overlay.SetLeftMargin(0.15)
        c_overlay.SetRightMargin(0.05)
        c_overlay.SetTopMargin(0.08)
        c_overlay.SetBottomMargin(0.12)
        
        # Style for SM histogram
        h_sm_norm.SetTitle("")
        h_sm_norm.GetXaxis().SetTitle("#sigma#phi")
        h_sm_norm.GetYaxis().SetTitle("Normalized Events")
        h_sm_norm.GetYaxis().SetTitleOffset(1.5)
        h_sm_norm.GetYaxis().SetRangeUser(0.03, 0.1)
        h_sm_norm.SetLineColor(ROOT.kBlack)
        h_sm_norm.SetLineWidth(2)
        h_sm_norm.SetMarkerStyle(20)
        h_sm_norm.SetMarkerSize(0.8)
        h_sm_norm.SetMarkerColor(ROOT.kBlack)
        
        # Style for EFT histogram
        h_eft_norm.SetLineColor(ROOT.kRed)
        h_eft_norm.SetLineWidth(2)
        h_eft_norm.SetMarkerStyle(21)
        h_eft_norm.SetMarkerSize(0.8)
        h_eft_norm.SetMarkerColor(ROOT.kRed)
        
        # Draw histograms
        h_sm_norm.Draw("HIST E1")
        h_eft_norm.Draw("HIST E1 SAME")
        
        # Add legend
        legend = ROOT.TLegend(0.65, 0.75, 0.85, 0.85)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        legend.AddEntry(h_sm_norm, "SM", "l")
        legend.AddEntry(h_eft_norm, wc_name + " = 10", "l")
        legend.Draw()
        
        # Add CMS text
        cms_text = ROOT.TLatex()
        cms_text.SetNDC()
        cms_text.SetTextSize(0.04)
        cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
        
        # Save overlay plot
        overlay_pdf = os.path.join(sigma_phi_dir, "sigmaPhi_overlay_{}.pdf".format(wc_name))
        c_overlay.SaveAs(overlay_pdf)
        num_plots_saved += 1
        
        # Create ratio plot
        c_ratio = ROOT.TCanvas("c_ratio_sigmaPhi_{}".format(wc_name), "SigmaPhi Ratio", 800, 600)
        c_ratio.SetLeftMargin(0.15)
        c_ratio.SetRightMargin(0.05)
        c_ratio.SetTopMargin(0.08)
        c_ratio.SetBottomMargin(0.12)
        c_ratio.SetGridy()
        
        # Create ratio histogram from normalized histograms
        h_ratio = h_eft_norm.Clone("h_ratio_sigmaPhi_{}".format(wc_name))
        h_ratio.Divide(h_sm_norm)
        
        # Style for ratio histogram
        h_ratio.SetTitle("")
        h_ratio.GetXaxis().SetTitle("#sigma#phi")
        h_ratio.GetYaxis().SetTitle("EFT/SM")
        h_ratio.GetYaxis().SetTitleOffset(1.5)
        h_ratio.GetYaxis().SetRangeUser(0.9, 1.1)
        h_ratio.SetLineColor(ROOT.kBlue)
        h_ratio.SetLineWidth(2)
        h_ratio.SetMarkerStyle(20)
        h_ratio.SetMarkerSize(0.8)
        h_ratio.SetMarkerColor(ROOT.kBlue)
        
        # Draw ratio histogram
        h_ratio.Draw("HIST E1")
        
        # Add horizontal line at y=1
        line = ROOT.TLine(-3.2, 1, 3.2, 1)
        line.SetLineStyle(2)
        line.SetLineColor(ROOT.kBlack)
        line.SetLineWidth(2)
        line.Draw("SAME")
        
        # Add CMS text
        cms_text = ROOT.TLatex()
        cms_text.SetNDC()
        cms_text.SetTextSize(0.04)
        cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
        
        # Save ratio plot
        ratio_pdf = os.path.join(sigma_phi_dir, "sigmaPhi_ratio_{}.pdf".format(wc_name))
        c_ratio.SaveAs(ratio_pdf)
        num_plots_saved += 1
    
    root_file.Close()
    
    print("\nExtraction complete! Saved {} plots from {}".format(num_plots_saved, root_file_path))
    print("All plots have been extracted and saved to: {}".format(output_dir))
    
    return True

def process_all_root_files(input_path, output_dir):
    #Process all ROOT files in a directory or a single ROOT file.
    if os.path.isdir(input_path):
        # Process all ROOT files in the directory
        root_files = glob.glob(os.path.join(input_path, "*.root"))
        if not root_files:
            print("No ROOT files found in directory: {}".format(input_path))
            return False
        
        print("Found {} ROOT files to process".format(len(root_files)))
        for i, root_file in enumerate(root_files):
            print("\nProcessing file [{}/{}]: {}".format(i+1, len(root_files), os.path.basename(root_file)))
            extract_and_save_plots(root_file, output_dir)
        
        return True
    elif os.path.isfile(input_path) and input_path.endswith(".root"):
        # Process a single ROOT file
        return extract_and_save_plots(input_path, output_dir)
    else:
        print("Error: Input path is not a ROOT file or directory: {}".format(input_path))
        return False

def main():
    parser = argparse.ArgumentParser(description="Extract plots from ROOT files and save them as PDFs")
    parser.add_argument("input_path", help="Path to ROOT file or directory containing ROOT files")
    parser.add_argument("--output-dir", default="extracted_plots", help="Output directory for PDF plots")
    
    args = parser.parse_args()
    
    # Process the input path
    success = process_all_root_files(args.input_path, args.output_dir)
    
    if success:
        print("\nAll plots have been extracted and saved to: {}".format(args.output_dir))
    else:
        print("\nFailed to extract plots. Please check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 