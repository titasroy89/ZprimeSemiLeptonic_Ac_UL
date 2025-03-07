#!/usr/bin/env python

from __future__ import division, print_function  # For Python 2 compatibility

import os
import sys
import glob
import subprocess
import argparse
import numpy as np
import ROOT
from itertools import combinations

def event_weights_lin_quad(structure_constants, wc_values):
    """
    Given an array of structure constants (for one event; length = poly_dim)
    and a chosen Wilson-coefficient vector (wc_values, length 16),
    returns the EFT weight for that event.
    
    weight = c0 + (linear term) + (quadratic term)
    """
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

def load_structure_constants(fname):
    """Load structure constants from a .npy file"""
    arr = np.load(fname)
    print("Loaded structure constants from", fname, "with shape:", arr.shape)
    return arr

def combine_structure_constants(structure_files):
    """Combine structure constants from multiple files"""
    all_structures = []
    for fname in structure_files:
        structures = np.load(fname)
        all_structures.append(structures)
    
    # Concatenate all structures
    combined = np.concatenate(all_structures, axis=0)
    print("Combined {0} structure constant files, total events: {1}".format(len(structure_files), len(combined)))
    return combined

def create_histograms(root_files, structure_files, output_dir, variables=None, wc_values=None):
    """
    Create histograms for all specified variables using the structure constants
    
    Parameters:
    - root_files: List of ROOT files
    - structure_files: List of structure constant files
    - output_dir: Directory to save output
    - variables: List of variables to plot (default: ['DeltaYreco', 'Delta_phi', 'Sigma_phi'])
    - wc_values: Dictionary of Wilson coefficient values to use (default: all 0 except one at a time)
    """
    if variables is None:
        variables = ['DeltaYreco', 'Delta_phi', 'Sigma_phi']
    
    # Dictionary of Wilson coefficients and their indices
    WC_NAMES = {
        0: "ctGRe", 1: "ctGIm", 2: "cQj18", 3: "cQj38",
        4: "cQj11", 5: "cQj31", 6: "ctu8", 7: "ctd8",
        8: "ctj8", 9: "cQu8", 10: "cQd8", 11: "ctu1",
        12: "ctd1", 13: "ctj1", 14: "cQu1", 15: "cQd1"
    }
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create subdirectories for each variable
    for var in variables:
        var_dir = os.path.join(output_dir, "{0}_plots".format(var))
        if not os.path.exists(var_dir):
            os.makedirs(var_dir)
    
    # Set ROOT to batch mode
    ROOT.gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetOptTitle(0)
    
    # Create output ROOT file
    output_file = os.path.join(output_dir, "combined_histograms.root")
    out_f = ROOT.TFile(output_file, "RECREATE")
    
    # Create histograms for each variable
    histograms = {}
    for var in variables:
        # Define histogram parameters based on variable
        if var == 'DeltaYreco':
            bins, xmin, xmax = 14, -3, 3
            x_title = "#Delta y_{reco}"
        elif var == 'Delta_phi':
            bins, xmin, xmax = 16, -3.2, 3.2
            x_title = "#Delta#phi"
        elif var == 'Sigma_phi':
            bins, xmin, xmax = 16, -3.2, 3.2
            x_title = "#Sigma#phi"
        else:
            bins, xmin, xmax = 20, -5, 5
            x_title = var
        
        # Create SM histogram
        histograms["{0}_SM".format(var)] = ROOT.TH1F("h_{0}_SM".format(var), "SM {0}".format(x_title), bins, xmin, xmax)
    
    # Process each ROOT file and corresponding structure constants
    for i, (root_file, structure_file) in enumerate(zip(root_files, structure_files)):
        print("\nProcessing file {0}/{1}: {2}".format(i+1, len(root_files), os.path.basename(root_file)))
        
        # Load structure constants
        structures = load_structure_constants(structure_file)
        
        # Open ROOT file
        f = ROOT.TFile.Open(root_file)
        if not f or f.IsZombie():
            print("Error opening {0}".format(root_file))
            continue
        
        tree = f.Get("AnalysisTree")
        if not tree:
            print("AnalysisTree not found in {0}".format(root_file))
            f.Close()
            continue
        
        # Fill SM histograms
        print("Filling SM histograms...")
        for i in range(min(tree.GetEntries(), len(structures))):
            tree.GetEntry(i)
            
            # Get variable values
            for var in variables:
                if hasattr(tree, var):
                    value = getattr(tree, var)
                    histograms["{0}_SM".format(var)].Fill(value)
        
        f.Close()
    
    # Normalize SM histograms
    for var in variables:
        if histograms["{0}_SM".format(var)].Integral() > 0:
            histograms["{0}_SM".format(var)].Scale(1.0 / histograms["{0}_SM".format(var)].Integral())
        histograms["{0}_SM".format(var)].Write()
    
    # SET each Wilson coefficient
    if wc_values is None:
        # set each Wilson coefficient one at a time with value 10.0
        for wc_index, wc_name in WC_NAMES.items():
            print("Processing {0} (index {1})...".format(wc_name, wc_index))
            
            # Set up WC values (all 0 except the one we're looking at)
            wc_vals = np.zeros(16)
            wc_vals[wc_index] = 10.0
            
            process_single_wc(root_files, structure_files, variables, wc_index, wc_name, wc_vals, histograms, output_dir, out_f)
    else:
        # Process custom WC values
        wc_vals = np.zeros(16)
        wc_name = "custom"
        for name, value in wc_values.items():
            if name in WC_INDICES:
                wc_vals[WC_INDICES[name]] = value
                if value != 0:
                    wc_name += "_{0}{1}".format(name, value)
        
        process_single_wc(root_files, structure_files, variables, -1, wc_name, wc_vals, histograms, output_dir, out_f)
    
    # Close output file
    out_f.Close()
    print("Histograms saved to {0}".format(output_file))

def process_single_wc(root_files, structure_files, variables, wc_index, wc_name, wc_values, sm_histograms, output_dir, out_f):
    """Process a single Wilson coefficient configuration"""
    # Create EFT histograms
    eft_histograms = {}
    ratio_histograms = {}
    
    for var in variables:
        # Define histogram parameters based on variable
        if var == 'DeltaYreco':
            bins, xmin, xmax = 14, -3, 3
            x_title = "#Delta y_{reco}"
        elif var == 'Delta_phi':
            bins, xmin, xmax = 16, -3.2, 3.2
            x_title = "#Delta#phi"
        elif var == 'Sigma_phi':
            bins, xmin, xmax = 16, -3.2, 3.2
            x_title = "#Sigma#phi"
        else:
            bins, xmin, xmax = 20, -5, 5
            x_title = var
        
        # Create EFT histogram
        eft_histograms[var] = ROOT.TH1F("h_{0}_EFT_{1}".format(var, wc_name), "EFT {0} ({1})".format(x_title, wc_name), bins, xmin, xmax)
    
    # Process each ROOT file and corresponding structure constants
    for i, (root_file, structure_file) in enumerate(zip(root_files, structure_files)):
        # Load structure constants
        structures = load_structure_constants(structure_file)
        
        # Open ROOT file
        f = ROOT.TFile.Open(root_file)
        if not f or f.IsZombie():
            print("Error opening {0}".format(root_file))
            continue
        
        tree = f.Get("AnalysisTree")
        if not tree:
            print("AnalysisTree not found in {0}".format(root_file))
            f.Close()
            continue
        
        # Fill EFT histograms
        for i in range(min(tree.GetEntries(), len(structures))):
            tree.GetEntry(i)
            
            # Calculate EFT weight
            event_struct = structures[i]
            weight = event_weights_lin_quad(event_struct, wc_values)
            
            # Get variable values and fill histograms
            for var in variables:
                if hasattr(tree, var):
                    value = getattr(tree, var)
                    eft_histograms[var].Fill(value, weight)
        
        f.Close()
    
    # Normalize EFT histograms and create ratio histograms
    for var in variables:
        if eft_histograms[var].Integral() > 0:
            eft_histograms[var].Scale(1.0 / eft_histograms[var].Integral())
        
        # Create ratio histogram
        ratio_histograms[var] = eft_histograms[var].Clone("h_ratio_{0}_{1}".format(var, wc_name))
        ratio_histograms[var].SetTitle("EFT/SM Ratio {0} ({1})".format(var, wc_name))
        ratio_histograms[var].Divide(sm_histograms["{0}_SM".format(var)])
        
        # Write histograms to file
        eft_histograms[var].Write()
        ratio_histograms[var].Write()
        
        # Create PDF plots
        create_ratio_plot(sm_histograms["{0}_SM".format(var)], eft_histograms[var], ratio_histograms[var], 
                         var, wc_name, os.path.join(output_dir, "{0}_plots".format(var)))

def create_ratio_plot(h_sm, h_eft, h_ratio, variable, wc_name, output_dir):
    """Create a ratio plot for a single variable and Wilson coefficient"""
    # Set up canvas
    c = ROOT.TCanvas("c_{0}_{1}".format(variable, wc_name), "{0} Ratio Plot".format(variable), 800, 800)
    c.Divide(1, 2)
    
    # Upper pad for distributions
    pad1 = c.cd(1)
    pad1.SetPad(0.0, 0.3, 1.0, 1.0)
    pad1.SetBottomMargin(0.02)
    pad1.SetLeftMargin(0.15)
    pad1.SetRightMargin(0.05)
    
    # Set histogram styles
    h_sm.SetLineColor(ROOT.kBlack)
    h_sm.SetLineWidth(2)
    h_sm.SetMarkerColor(ROOT.kBlack)
    h_sm.SetMarkerStyle(20)
    h_sm.SetMarkerSize(1.0)
    
    h_eft.SetLineColor(ROOT.kRed)
    h_eft.SetLineWidth(2)
    h_eft.SetMarkerColor(ROOT.kRed)
    h_eft.SetMarkerStyle(21)
    h_eft.SetMarkerSize(1.0)
    
    # Get x-axis title
    if variable == 'DeltaYreco':
        x_title = "#Delta y_{reco}"
    elif variable == 'Delta_phi':
        x_title = "#Delta#phi"
    elif variable == 'Sigma_phi':
        x_title = "#Sigma#phi"
    else:
        x_title = variable
    
    # Draw distributions
    h_sm.GetXaxis().SetLabelSize(0)
    h_sm.GetYaxis().SetTitle("Normalized")
    h_sm.GetYaxis().SetTitleOffset(1.5)
    h_sm.GetYaxis().SetTitleSize(0.05)
    h_sm.GetYaxis().SetLabelSize(0.05)
    h_sm.SetMaximum(max(h_sm.GetMaximum(), h_eft.GetMaximum()) * 1.2)
    
    # Draw with error bars
    h_sm.Draw("E")  # Draw with error bars
    h_eft.Draw("E SAME")  # Draw with error bars
    
    # Create legend
    leg = ROOT.TLegend(0.65, 0.65, 0.90, 0.85)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    leg.AddEntry(h_sm, "SM", "lep")  # Changed to lep to show line, error, point
    leg.AddEntry(h_eft, "EFT ({0})".format(wc_name), "lep") 
    leg.Draw()
    
    # Add CMS text
    cms_text = ROOT.TLatex()
    cms_text.SetNDC()
    cms_text.SetTextSize(0.05)
    cms_text.DrawLatex(0.20, 0.92, "#bf{CMS} #it{Simulation}")
    
    # Lower pad for ratio
    pad2 = c.cd(2)
    pad2.SetPad(0.0, 0.0, 1.0, 0.3)
    pad2.SetTopMargin(0.02)
    pad2.SetBottomMargin(0.3)
    pad2.SetLeftMargin(0.15)
    pad2.SetRightMargin(0.05)
    pad2.SetGridy()
    
    # Set ratio histogram style
    h_ratio.SetLineColor(ROOT.kRed)
    h_ratio.SetLineWidth(2)
    h_ratio.SetMarkerColor(ROOT.kRed)
    h_ratio.SetMarkerStyle(21)
    h_ratio.SetMarkerSize(1.0)
    
    # Keep error bars for ratio

    
    # Draw ratio with error bars
    h_ratio.GetXaxis().SetTitle(x_title)
    h_ratio.GetXaxis().SetTitleSize(0.12)
    h_ratio.GetXaxis().SetLabelSize(0.12)
    h_ratio.GetXaxis().SetTitleOffset(1.0)
    
    h_ratio.GetYaxis().SetTitle("EFT/SM")
    h_ratio.GetYaxis().SetTitleSize(0.12)
    h_ratio.GetYaxis().SetLabelSize(0.12)
    h_ratio.GetYaxis().SetTitleOffset(0.5)
    h_ratio.GetYaxis().SetRangeUser(0.8, 1.2)
    h_ratio.GetYaxis().SetNdivisions(505)
    
    h_ratio.Draw("E")  # Draw with error bars
    
    # Draw reference line at y=1
    line = ROOT.TLine(h_ratio.GetXaxis().GetXmin(), 1, h_ratio.GetXaxis().GetXmax(), 1)
    line.SetLineStyle(2)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)
    line.Draw("same")
    
    # Save the plot
    c.SaveAs(os.path.join(output_dir, "{0}_{1}_ratio.pdf".format(variable, wc_name)))
    c.SaveAs(os.path.join(output_dir, "{0}_{1}_ratio.png".format(variable, wc_name)))

def create_combined_ratio_plot(output_dir, variable):
    """Create a combined ratio plot for all Wilson coefficients for a single variable"""
    # Dictionary of Wilson coefficients and their indices
    WC_NAMES = {
        0: "ctGRe", 1: "ctGIm", 2: "cQj18", 3: "cQj38",
        4: "cQj11", 5: "cQj31", 6: "ctu8", 7: "ctd8",
        8: "ctj8", 9: "cQu8", 10: "cQd8", 11: "ctu1",
        12: "ctd1", 13: "ctj1", 14: "cQu1", 15: "cQd1"
    }
    
    # Open the combined histograms file
    f = ROOT.TFile(os.path.join(output_dir, "combined_histograms.root"))
    if not f or f.IsZombie():
        print("Error opening combined histograms file")
        return
    
    # Get x-axis title
    if variable == 'DeltaYreco':
        x_title = "#Delta y_{reco}"
        x_min, x_max = -3, 3
    elif variable == 'Delta_phi':
        x_title = "#Delta#phi"
        x_min, x_max = -3.2, 3.2
    elif variable == 'Sigma_phi':
        x_title = "#Sigma#phi"
        x_min, x_max = -3.2, 3.2
    else:
        x_title = variable
        x_min, x_max = -5, 5
    
    # Create canvas
    c = ROOT.TCanvas("c_combined_{0}".format(variable), "Combined {0} Ratio".format(variable), 800, 600)
    c.SetLeftMargin(0.15)
    
    # Create dummy histogram for axes
    h_dummy = ROOT.TH1F("h_dummy_{0}".format(variable), "", 20, x_min, x_max)
    h_dummy.SetTitle("")
    h_dummy.GetXaxis().SetTitle(x_title)
    h_dummy.GetYaxis().SetTitle("EFT/SM (normalized)")
    h_dummy.GetYaxis().SetTitleOffset(1.5)
    h_dummy.GetYaxis().SetRangeUser(0, 2)
    h_dummy.SetStats(0)
    h_dummy.Draw()
    
    # Create legend
    leg = ROOT.TLegend(0.82, 0.15, 0.95, 0.85)
    leg.SetBorderSize(0)
    leg.SetFillStyle(0)
    
    # Define colors
    colors = [
        ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kMagenta+1,
        ROOT.kCyan+2, ROOT.kOrange+1, ROOT.kViolet-1, ROOT.kSpring+10,
        ROOT.kTeal+1, ROOT.kYellow+2, ROOT.kBlue+2, ROOT.kRed+2,
        ROOT.kGreen+3, ROOT.kViolet+2, ROOT.kCyan+3, ROOT.kOrange+2
    ]
    
    # Draw ratio histograms
    for wc_index, wc_name in WC_NAMES.items():
        h_ratio = f.Get("h_ratio_{0}_{1}".format(variable, wc_name))
        if not h_ratio:
            continue
            
        # Set histogram style
        h_ratio.SetLineColor(colors[wc_index])
        h_ratio.SetLineWidth(2)
        h_ratio.SetMarkerColor(colors[wc_index])
        h_ratio.SetMarkerStyle(20)
        h_ratio.SetMarkerSize(1.0)
        
        # Set all bin errors to zero for combined plots
        for i in range(1, h_ratio.GetNbinsX() + 1):
            h_ratio.SetBinError(i, 0)
        
        # Draw histogram without error bars for combined plots
        h_ratio.Draw("HIST SAME")
        h_ratio.Draw("P SAME")
        
        # Add to legend
        leg.AddEntry(h_ratio, wc_name, "lp")
    
    # Draw reference line at y=1
    line = ROOT.TLine(x_min, 1, x_max, 1)
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
    
    # Save the plot
    var_dir = os.path.join(output_dir, "{0}_plots".format(variable))
    if not os.path.exists(var_dir):
        os.makedirs(var_dir)
    
    c.SaveAs(os.path.join(var_dir, "combined_{0}_ratio.pdf".format(variable)))
    c.SaveAs(os.path.join(var_dir, "combined_{0}_ratio.png".format(variable)))
    
    # Close the file
    f.Close()

# Dictionary of Wilson coefficient indices
WC_INDICES = {
    "ctGRe": 0, "ctGIm": 1, "cQj18": 2, "cQj38": 3,
    "cQj11": 4, "cQj31": 5, "ctu8": 6, "ctd8": 7,
    "ctj8": 8, "cQu8": 9, "cQd8": 10, "ctu1": 11,
    "ctd1": 12, "ctj1": 13, "cQu1": 14, "cQd1": 15
}

def main():
    parser = argparse.ArgumentParser(description='Process all ROOT files in a directory for EFT structure constants and plots')
    parser.add_argument('--input-dir', type=str, default='/data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_deltaPhi_sigmaPhi_ttree',
                        help='Directory containing ROOT files to process')
    parser.add_argument('--output-dir', type=str, default='results',
                        help='Directory to store output files')
    parser.add_argument('--calc-only', action='store_true',
                        help='Only calculate structure constants, skip plotting')
    parser.add_argument('--plot-only', action='store_true',
                        help='Only create plots, skip structure constant calculation')
    parser.add_argument('--combined-only', action='store_true',
                        help='Only create combined ratio plots, skip individual plots')
    parser.add_argument('--variables', type=str, nargs='+', default=['DeltaYreco', 'Delta_phi', 'Sigma_phi'],
                        help='Variables to plot (default: DeltaYreco Delta_phi Sigma_phi)')
    parser.add_argument('--custom-wc', action='store_true',
                        help='Use custom Wilson coefficient values defined in the script')
    parser.add_argument('--merge-plots', action='store_true',
                        help='Create merged plots from all files')
    parser.add_argument('--file-pattern', type=str, default='*.root',
                        help='Pattern to match ROOT files (default: *.root)')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # Find all ROOT files in the input directory matching the pattern
    root_files = glob.glob(os.path.join(args.input_dir, args.file_pattern))
    
    if not root_files:
        print("No ROOT files found in {} matching pattern {}".format(args.input_dir, args.file_pattern))
        return
    
    print("Found {} ROOT files to process".format(len(root_files)))
    
    # Lists to store structure constants and file paths for merging
    all_structure_files = []
    all_root_files = []
    
    # Process each ROOT file
    for i, root_file in enumerate(root_files):
        file_basename = os.path.basename(root_file)
        sample_name = file_basename.replace("uhh2.AnalysisModuleRunner.MC.", "").replace(".root", "")
        
        # Create sample-specific output directory
        sample_output_dir = os.path.join(args.output_dir, sample_name)
        if not os.path.exists(sample_output_dir):
            os.makedirs(sample_output_dir)
        
        print("\nProcessing file {}/{}: {}".format(i+1, len(root_files), file_basename))
        
        # Calculate structure constants if not in plot-only mode
        if not args.plot_only:
            structure_const_file = os.path.join(sample_output_dir, "structure_constants.npy")
            
            print("Calculating structure constants for {}...".format(file_basename))
            calc_cmd = [
                "python", "calc_structure_constants.py",
                root_file,
                structure_const_file
            ]
            
            try:
                subprocess.check_call(calc_cmd)
                print("Structure constants saved to {}".format(structure_const_file))
            except subprocess.CalledProcessError as e:
                print("Error calculating structure constants for {}: {}".format(file_basename, e))
                continue
        else:
            # If in plot-only mode, check if structure constants file exists
            structure_const_file = os.path.join(sample_output_dir, "structure_constants.npy")
            if not os.path.exists(structure_const_file):
                print("Structure constants file not found for {}. Run without --plot-only first.".format(sample_name))
                continue
        
        # Add to lists for merged plots
        all_structure_files.append(structure_const_file)
        all_root_files.append(root_file)
    
    # Create combined plots if requested
    if args.merge_plots and not args.calc_only:
        print("\nCreating combined plots from all files...")
        
        # Define custom Wilson coefficient values if requested
        wc_values = None
        if args.custom_wc:
            wc_values = {
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
                "cQd1": 0.0,
            }
        
        # Create histograms
        create_histograms(all_root_files, all_structure_files, args.output_dir, args.variables, wc_values)
        
        # Create combined ratio plots
        for var in args.variables:
            create_combined_ratio_plot(args.output_dir, var)
    
    print("\nAll files processed successfully!")

if __name__ == "__main__":
    main() 