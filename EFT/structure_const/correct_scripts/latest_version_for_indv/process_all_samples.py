#!/usr/bin/env python

import os
import sys
import glob
import subprocess
import argparse

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
    parser.add_argument('--delta-phi-only', action='store_true',
                        help='Only create Delta_phi plots')
    parser.add_argument('--sigma-phi-only', action='store_true',
                        help='Only create Sigma_phi plots')
    parser.add_argument('--merge-plots', action='store_true',
                        help='Create merged plots from all files')
    parser.add_argument('--save-root', action='store_true', default=True,
                        help='Save histograms in ROOT format for use with hadd')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # Find all ROOT files in the input directory
    root_files = glob.glob(os.path.join(args.input_dir, "*.root"))
    
    if not root_files:
        print("No ROOT files found in {}".format(args.input_dir))
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
        
        # Create individual plots if not in calc-only mode and not merging
        if not args.calc_only:
            print("Creating histograms for {}...".format(file_basename))
            
            # Create a script to generate histograms and save them in ROOT format
            hist_script_path = os.path.join(sample_output_dir, "create_histograms.py")
            with open(hist_script_path, 'w') as f:
                f.write("""#!/usr/bin/env python
import numpy as np
import sys
import os
import ROOT

# Input files
structure_file = "{structure_file}"
root_file = "{root_file}"

# Output directory
output_dir = "{output_dir}"

# Load structure constants
print("Loading structure constants from {}...".format(structure_file))
try:
    structures = np.load(structure_file)
    print("Loaded {} events".format(len(structures)))
except Exception as e:
    print("Error loading structure constants: {}".format(e))
    sys.exit(1)

# Dictionary of Wilson coefficients and their indices
WC_NAMES = {{
    0: "ctGRe", 1: "ctGIm", 2: "cQj18", 3: "cQj38",
    4: "cQj11", 5: "cQj31", 6: "ctu8", 7: "ctd8",
    8: "ctj8", 9: "cQu8", 10: "cQd8", 11: "ctu1",
    12: "ctd1", 13: "ctj1", 14: "cQu1", 15: "cQd1"
}}

# Set ROOT to batch mode
ROOT.gROOT.SetBatch(True)

# Open input ROOT file
f = ROOT.TFile.Open(root_file)
if not f or f.IsZombie():
    print("Error opening {}".format(root_file))
    sys.exit(1)

tree = f.Get("AnalysisTree")
if not tree:
    print("AnalysisTree not found in {}".format(root_file))
    f.Close()
    sys.exit(1)

# Create output ROOT file
output_file = os.path.join(output_dir, "histograms.root")
out_f = ROOT.TFile(output_file, "RECREATE")

# Create histograms for Delta_phi and Sigma_phi
h_delta_phi_SM = ROOT.TH1F("h_delta_phi_SM", "SM #Delta#phi", 16, -3.2, 3.2)
h_sigma_phi_SM = ROOT.TH1F("h_sigma_phi_SM", "SM #Sigma#phi", 16, -3.2, 3.2)

# Fill SM histograms
print("Filling SM histograms...")
for i in range(tree.GetEntries()):
    tree.GetEntry(i)
    
    # Get Delta_phi and Sigma_phi values
    delta_phi = tree.Delta_phi
    sigma_phi = tree.Sigma_phi
    
    # Fill histograms
    h_delta_phi_SM.Fill(delta_phi)
    h_sigma_phi_SM.Fill(sigma_phi)

# Normalize SM histograms
if h_delta_phi_SM.Integral() > 0:
    h_delta_phi_SM.Scale(1.0 / h_delta_phi_SM.Integral())
if h_sigma_phi_SM.Integral() > 0:
    h_sigma_phi_SM.Scale(1.0 / h_sigma_phi_SM.Integral())

# Write SM histograms to file
h_delta_phi_SM.Write()
h_sigma_phi_SM.Write()

# Process each Wilson coefficient
for wc_index, wc_name in WC_NAMES.items():
    print("Processing {} (index {})...".format(wc_name, wc_index))
    
    # Set up WC values (all 0 except the one we're looking at)
    wc_values = np.zeros(16)
    wc_values[wc_index] = 10.0  # Set to 10 by default
    
    # Create EFT histograms
    h_delta_phi_EFT = ROOT.TH1F("h_delta_phi_EFT_{}".format(wc_name), 
                               "EFT #Delta#phi ({})".format(wc_name), 16, -3.2, 3.2)
    h_sigma_phi_EFT = ROOT.TH1F("h_sigma_phi_EFT_{}".format(wc_name), 
                               "EFT #Sigma#phi ({})".format(wc_name), 16, -3.2, 3.2)
    
    # Loop through events
    for i in range(min(tree.GetEntries(), len(structures))):
        tree.GetEntry(i)
        
        # Get Delta_phi and Sigma_phi values
        delta_phi = tree.Delta_phi
        sigma_phi = tree.Sigma_phi
        
        # Calculate EFT weight
        event_struct = structures[i]
        
        # Linear and quadratic terms
        lin_term = 0.0
        quad_term = 0.0
        
        # Linear term: sum of c_i * w_i
        for j in range(16):
            lin_term += wc_values[j] * event_struct[j+1]
        
        # Quadratic term: sum of c_i * c_j * w_ij
        idx = 17  # Start after the linear terms
        for j in range(16):
            for k in range(j, 16):  # Upper triangular matrix
                quad_term += wc_values[j] * wc_values[k] * event_struct[idx]
                idx += 1
        
        # Total weight
        weight = event_struct[0] + lin_term + quad_term
        
        # Fill histograms
        h_delta_phi_EFT.Fill(delta_phi, weight)
        h_sigma_phi_EFT.Fill(sigma_phi, weight)
    
    # Normalize EFT histograms
    if h_delta_phi_EFT.Integral() > 0:
        h_delta_phi_EFT.Scale(1.0 / h_delta_phi_EFT.Integral())
    if h_sigma_phi_EFT.Integral() > 0:
        h_sigma_phi_EFT.Scale(1.0 / h_sigma_phi_EFT.Integral())
    
    # Create ratio histograms
    h_ratio_delta_phi = h_delta_phi_EFT.Clone("h_ratio_delta_phi_{}".format(wc_name))
    h_ratio_delta_phi.SetTitle("EFT/SM Ratio #Delta#phi ({})".format(wc_name))
    h_ratio_delta_phi.Divide(h_delta_phi_SM)
    
    h_ratio_sigma_phi = h_sigma_phi_EFT.Clone("h_ratio_sigma_phi_{}".format(wc_name))
    h_ratio_sigma_phi.SetTitle("EFT/SM Ratio #Sigma#phi ({})".format(wc_name))
    h_ratio_sigma_phi.Divide(h_sigma_phi_SM)
    
    # Write histograms to file
    h_delta_phi_EFT.Write()
    h_sigma_phi_EFT.Write()
    h_ratio_delta_phi.Write()
    h_ratio_sigma_phi.Write()

# Close files
out_f.Close()
f.Close()

print("Histograms saved to {}".format(output_file))

# Create PDF plots if requested
create_delta_phi = {create_delta_phi}
create_sigma_phi = {create_sigma_phi}
combined_only = {combined_only}

if create_delta_phi or create_sigma_phi:
    # Create directories for plots
    if create_delta_phi:
        delta_phi_dir = os.path.join(output_dir, "delta_phi_plots")
        if not os.path.exists(delta_phi_dir):
            os.makedirs(delta_phi_dir)
    
    if create_sigma_phi:
        sigma_phi_dir = os.path.join(output_dir, "sigma_phi_plots")
        if not os.path.exists(sigma_phi_dir):
            os.makedirs(sigma_phi_dir)
    
    # Open the output ROOT file to read histograms
    f = ROOT.TFile(output_file)
    
    # Create combined ratio plots
    if create_delta_phi:
        print("Creating combined ratio plot for Delta_phi...")
        c_delta_phi = ROOT.TCanvas("c_delta_phi", "Combined #Delta#phi Ratio", 800, 600)
        c_delta_phi.SetLeftMargin(0.15)
        
        # Create dummy histogram for axes
        h_dummy_delta_phi = ROOT.TH1F("h_dummy_delta_phi", "", 16, -3.2, 3.2)
        h_dummy_delta_phi.SetTitle("")
        h_dummy_delta_phi.GetXaxis().SetTitle("#Delta#phi")
        h_dummy_delta_phi.GetYaxis().SetTitle("EFT/SM (normalized)")
        h_dummy_delta_phi.GetYaxis().SetTitleOffset(1.5)
        h_dummy_delta_phi.GetYaxis().SetRangeUser(0.8, 1.2)
        h_dummy_delta_phi.SetStats(0)
        h_dummy_delta_phi.Draw()
        
        # Create legend
        leg_delta_phi = ROOT.TLegend(0.82, 0.15, 0.95, 0.85)
        leg_delta_phi.SetBorderSize(0)
        leg_delta_phi.SetFillStyle(0)
        
        # Define colors
        colors = [
            ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kMagenta+1,
            ROOT.kCyan+2, ROOT.kOrange+1, ROOT.kViolet-1, ROOT.kSpring+10,
            ROOT.kTeal+1, ROOT.kYellow+2, ROOT.kBlue+2, ROOT.kRed+2,
            ROOT.kGreen+3, ROOT.kViolet+2, ROOT.kCyan+3, ROOT.kOrange+2
        ]
        
        # Draw ratio histograms
        for wc_index, wc_name in WC_NAMES.items():
            h_ratio = f.Get("h_ratio_delta_phi_{}".format(wc_name))
            if not h_ratio:
                continue
                
            # Set histogram style
            h_ratio.SetLineColor(colors[wc_index])
            h_ratio.SetLineWidth(2)
            h_ratio.SetMarkerColor(colors[wc_index])
            h_ratio.SetMarkerStyle(20)
            h_ratio.SetMarkerSize(1.0)
            
            # Set all bin errors to zero
            for i in range(1, h_ratio.GetNbinsX() + 1):
                h_ratio.SetBinError(i, 0)
            
            # Draw histogram
            h_ratio.Draw("HIST SAME")
            h_ratio.Draw("P SAME")
            
            # Add to legend
            leg_delta_phi.AddEntry(h_ratio, wc_name, "lp")
        
        # Draw reference line at y=1
        line_delta_phi = ROOT.TLine(-3.2, 1, 3.2, 1)
        line_delta_phi.SetLineStyle(2)
        line_delta_phi.SetLineColor(ROOT.kBlack)
        line_delta_phi.SetLineWidth(2)
        line_delta_phi.Draw("same")
        
        # Draw the legend
        leg_delta_phi.Draw()
        
        # Add CMS text
        cms_text_delta_phi = ROOT.TLatex()
        cms_text_delta_phi.SetNDC()
        cms_text_delta_phi.SetTextSize(0.05)
        cms_text_delta_phi.DrawLatex(0.20, 0.92, "#bf{{CMS}} #it{{Simulation}}")
        
        # Save the plot
        c_delta_phi.SaveAs(os.path.join(delta_phi_dir, "combined_delta_phi_ratio.pdf"))
        c_delta_phi.SaveAs(os.path.join(delta_phi_dir, "combined_delta_phi_ratio.png"))
    
    if create_sigma_phi:
        print("Creating combined ratio plot for Sigma_phi...")
        c_sigma_phi = ROOT.TCanvas("c_sigma_phi", "Combined #Sigma#phi Ratio", 800, 600)
        c_sigma_phi.SetLeftMargin(0.15)
        
        # Create dummy histogram for axes
        h_dummy_sigma_phi = ROOT.TH1F("h_dummy_sigma_phi", "", 16, -3.2, 3.2)
        h_dummy_sigma_phi.SetTitle("")
        h_dummy_sigma_phi.GetXaxis().SetTitle("#Sigma#phi")
        h_dummy_sigma_phi.GetYaxis().SetTitle("EFT/SM (normalized)")
        h_dummy_sigma_phi.GetYaxis().SetTitleOffset(1.5)
        h_dummy_sigma_phi.GetYaxis().SetRangeUser(0.8, 1.2)
        h_dummy_sigma_phi.SetStats(0)
        h_dummy_sigma_phi.Draw()
        
        # Create legend
        leg_sigma_phi = ROOT.TLegend(0.82, 0.15, 0.95, 0.85)
        leg_sigma_phi.SetBorderSize(0)
        leg_sigma_phi.SetFillStyle(0)
        
        # Draw ratio histograms
        for wc_index, wc_name in WC_NAMES.items():
            h_ratio = f.Get("h_ratio_sigma_phi_{}".format(wc_name))
            if not h_ratio:
                continue
                
            # Set histogram style
            h_ratio.SetLineColor(colors[wc_index])
            h_ratio.SetLineWidth(2)
            h_ratio.SetMarkerColor(colors[wc_index])
            h_ratio.SetMarkerStyle(20)
            h_ratio.SetMarkerSize(1.0)
            
            # Set all bin errors to zero
            for i in range(1, h_ratio.GetNbinsX() + 1):
                h_ratio.SetBinError(i, 0)
            
            # Draw histogram
            h_ratio.Draw("HIST SAME")
            h_ratio.Draw("P SAME")
            
            # Add to legend
            leg_sigma_phi.AddEntry(h_ratio, wc_name, "lp")
        
        # Draw reference line at y=1
        line_sigma_phi = ROOT.TLine(-3.2, 1, 3.2, 1)
        line_sigma_phi.SetLineStyle(2)
        line_sigma_phi.SetLineColor(ROOT.kBlack)
        line_sigma_phi.SetLineWidth(2)
        line_sigma_phi.Draw("same")
        
        # Draw the legend
        leg_sigma_phi.Draw()
        
        # Add CMS text
        cms_text_sigma_phi = ROOT.TLatex()
        cms_text_sigma_phi.SetNDC()
        cms_text_sigma_phi.SetTextSize(0.05)
        cms_text_sigma_phi.DrawLatex(0.20, 0.92, "#bf{{CMS}} #it{{Simulation}}")
        
        # Save the plot
        c_sigma_phi.SaveAs(os.path.join(sigma_phi_dir, "combined_sigma_phi_ratio.pdf"))
        c_sigma_phi.SaveAs(os.path.join(sigma_phi_dir, "combined_sigma_phi_ratio.png"))
    
    # Close the file
    f.Close()

print("Done!")
""".format(
                    structure_file=structure_const_file,
                    root_file=root_file,
                    output_dir=sample_output_dir,
                    create_delta_phi="True" if not args.sigma_phi_only else "False",
                    create_sigma_phi="True" if not args.delta_phi_only else "False",
                    combined_only="True" if args.combined_only else "False"
                ))
            
            # Make the script executable
            os.chmod(hist_script_path, 0o755)
            
            # Run the histogram creation script
            try:
                print("Running histogram creation script...")
                subprocess.check_call(["python", hist_script_path])
                print("Histograms saved to {}".format(os.path.join(sample_output_dir, "histograms.root")))
            except subprocess.CalledProcessError as e:
                print("Error creating histograms: {}".format(e))
                continue
    
    # Create instructions for using hadd
    if len(all_root_files) > 0 and args.save_root:
        hadd_instructions = os.path.join(args.output_dir, "hadd_instructions.txt")
        with open(hadd_instructions, 'w') as f:
            f.write("""# Instructions for combining histogram ROOT files using hadd

# To combine all histogram files into one:
hadd {output_dir}/combined_histograms.root {sample_dirs}

# After combining, you can use ROOT to create plots from the combined file.
# Example ROOT macro to create combined plots:
/*
void create_combined_plots() {{
    TFile *f = TFile::Open("{output_dir}/combined_histograms.root");
    
    // Create Delta_phi combined ratio plot
    TCanvas *c1 = new TCanvas("c1", "Combined #Delta#phi Ratio", 800, 600);
    c1->SetLeftMargin(0.15);
    
    // Create dummy histogram for axes
    TH1F *h_dummy = new TH1F("h_dummy", "", 16, -3.2, 3.2);
    h_dummy->SetTitle("");
    h_dummy->GetXaxis()->SetTitle("#Delta#phi");
    h_dummy->GetYaxis()->SetTitle("EFT/SM (normalized)");
    h_dummy->GetYaxis()->SetTitleOffset(1.5);
    h_dummy->GetYaxis()->SetRangeUser(0.8, 1.2);
    h_dummy->SetStats(0);
    h_dummy->Draw();
    
    // Create legend
    TLegend *leg = new TLegend(0.82, 0.15, 0.95, 0.85);
    leg->SetBorderSize(0);
    leg->SetFillStyle(0);
    
    // Define colors
    int colors[16] = {{
        kRed, kBlue, kGreen+2, kMagenta+1,
        kCyan+2, kOrange+1, kViolet-1, kSpring+10,
        kTeal+1, kYellow+2, kBlue+2, kRed+2,
        kGreen+3, kViolet+2, kCyan+3, kOrange+2
    }};
    
    // Dictionary of Wilson coefficients
    const char* wc_names[16] = {{
        "ctGRe", "ctGIm", "cQj18", "cQj38",
        "cQj11", "cQj31", "ctu8", "ctd8",
        "ctj8", "cQu8", "cQd8", "ctu1",
        "ctd1", "ctj1", "cQu1", "cQd1"
    }};
    
    // Draw ratio histograms
    for (int i = 0; i < 16; i++) {{
        TString histname = TString::Format("h_ratio_delta_phi_%s", wc_names[i]);
        TH1F *h_ratio = (TH1F*)f->Get(histname);
        if (!h_ratio) continue;
        
        // Set histogram style
        h_ratio->SetLineColor(colors[i]);
        h_ratio->SetLineWidth(2);
        h_ratio->SetMarkerColor(colors[i]);
        h_ratio->SetMarkerStyle(20);
        h_ratio->SetMarkerSize(1.0);
        
        // Set all bin errors to zero
        for (int j = 1; j <= h_ratio->GetNbinsX(); j++) {{
            h_ratio->SetBinError(j, 0);
        }}
        
        // Draw histogram
        h_ratio->Draw("HIST SAME");
        h_ratio->Draw("P SAME");
        
        // Add to legend
        leg->AddEntry(h_ratio, wc_names[i], "lp");
    }}
    
    // Draw reference line at y=1
    TLine *line = new TLine(-3.2, 1, 3.2, 1);
    line->SetLineStyle(2);
    line->SetLineColor(kBlack);
    line->SetLineWidth(2);
    line->Draw("same");
    
    // Draw the legend
    leg->Draw();
    
    // Add CMS text
    TLatex *cms_text = new TLatex();
    cms_text->SetNDC();
    cms_text->SetTextSize(0.05);
    cms_text->DrawLatex(0.20, 0.92, "#bf{{CMS}} #it{{Simulation}}");
    
    // Save the plot
    c1->SaveAs("{output_dir}/combined_delta_phi_ratio.pdf");
    c1->SaveAs("{output_dir}/combined_delta_phi_ratio.png");
    
    // Create Sigma_phi combined ratio plot (similar to Delta_phi)
    // ... (code similar to above)
}}
*/
""".format(
                output_dir=args.output_dir,
                sample_dirs=" ".join([os.path.join(args.output_dir, os.path.basename(f).replace("uhh2.AnalysisModuleRunner.MC.", "").replace(".root", ""), "histograms.root") for f in all_root_files])
            ))
        
        print("\nInstructions for combining histogram files with hadd saved to {}".format(hadd_instructions))
    
    print("\nAll files processed successfully!")

if __name__ == "__main__":
    main() 