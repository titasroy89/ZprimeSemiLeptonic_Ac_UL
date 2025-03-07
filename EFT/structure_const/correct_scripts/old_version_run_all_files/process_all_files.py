#!/usr/bin/env python
"""
Script to process all ROOT files with their corresponding structure constants files.
This script will:
1. Find all ROOT files and match them with their structure constants files
2. Run the plotting scripts for each pair
3. Combine the histograms using hadd

Usage:
    python process_all_files.py <root_files_dir> <structure_constants_dir> [--custom-wc] [--delta-phi-only] [--sigma-phi-only] [--delta-y-only]
"""

import os
import sys
import glob
import subprocess
import argparse
import shutil

def find_matching_files(root_dir, npy_dir):
    """Find ROOT files and their matching structure constants files."""
    root_files = glob.glob(os.path.join(root_dir, "*.root"))
    matches = []
    
    for root_file in root_files:
        basename = os.path.basename(root_file)
        filename_without_ext = os.path.splitext(basename)[0]
        
        # Look for matching structure constants file
        npy_file = os.path.join(npy_dir, "%s_structure_constants.npy" % filename_without_ext)
        
        if os.path.exists(npy_file):
            matches.append((root_file, npy_file))
        else:
            print("Warning: No matching structure constants file found for %s" % root_file)
    
    return matches

def run_plotting_scripts(file_pairs, output_dir, args):
    """Run the plotting scripts for each file pair."""
    # Create output directories for ROOT files
    root_output_dir = os.path.join(output_dir, "root_files")
    if not os.path.exists(root_output_dir):
        os.makedirs(root_output_dir)
    
    # Process each file pair
    for i, (root_file, npy_file) in enumerate(file_pairs):
        print("\nProcessing file pair %d/%d:" % (i+1, len(file_pairs)))
        print("  ROOT file: %s" % root_file)
        print("  NPY file: %s" % npy_file)
        
        basename = os.path.basename(root_file)
        filename_without_ext = os.path.splitext(basename)[0]
        
        # Create separate directories for PDF plots for this file
        file_plots_dir = os.path.join(output_dir, "plots", filename_without_ext)
        if not os.path.exists(file_plots_dir):
            os.makedirs(file_plots_dir)
        
        # Create a single output ROOT file for all plots
        combined_output = os.path.join(root_output_dir, "%s_all_plots.root" % filename_without_ext)
        
        # Run deltaY script if not disabled
        if not args.delta_phi_only and not args.sigma_phi_only:
            # Create directory for deltaY plots
            deltaY_plots_dir = os.path.join(file_plots_dir, "deltaY_plots")
            if not os.path.exists(deltaY_plots_dir):
                os.makedirs(deltaY_plots_dir)
            
            # Run the script with the output directory parameter
            cmd = ["python", "plot_deltaY_shape.py", npy_file, root_file, 
                   "--output-root", combined_output,
                   "--output-dir", deltaY_plots_dir]
            
            if args.custom_wc:
                cmd.append("--custom-wc")
            
            print("  Running: %s" % " ".join(cmd))
            subprocess.call(cmd)
            print("  DeltaY plots saved to: %s" % deltaY_plots_dir)
        
        # Run deltaPhi_sigmaPhi script if not disabled
        if not args.delta_y_only:
            # For Delta Phi
            if not args.sigma_phi_only:
                # Create directory for deltaPhi plots
                deltaPhi_plots_dir = os.path.join(file_plots_dir, "delta_phi_plots")
                if not os.path.exists(deltaPhi_plots_dir):
                    os.makedirs(deltaPhi_plots_dir)
                
                # Run the script with the output directory parameter
                cmd = ["python", "plot_deltaPhi_sigmaPhi.py", npy_file, root_file, 
                       "--output-root", combined_output,
                       "--output-dir", deltaPhi_plots_dir,
                       "--delta-phi-only"]
                
                if args.custom_wc:
                    cmd.append("--custom-wc")
                
                print("  Running: %s" % " ".join(cmd))
                subprocess.call(cmd)
                print("  DeltaPhi plots saved to: %s" % deltaPhi_plots_dir)
            
            # For Sigma Phi
            if not args.delta_phi_only:
                # Create directory for sigmaPhi plots
                sigmaPhi_plots_dir = os.path.join(file_plots_dir, "sigma_phi_plots")
                if not os.path.exists(sigmaPhi_plots_dir):
                    os.makedirs(sigmaPhi_plots_dir)
                
                # Run the script with the output directory parameter
                cmd = ["python", "plot_deltaPhi_sigmaPhi.py", npy_file, root_file, 
                       "--output-root", combined_output,
                       "--output-dir", sigmaPhi_plots_dir,
                       "--sigma-phi-only"]
                
                if args.custom_wc:
                    cmd.append("--custom-wc")
                
                print("  Running: %s" % " ".join(cmd))
                subprocess.call(cmd)
                print("  SigmaPhi plots saved to: %s" % sigmaPhi_plots_dir)
        
        print("  All plots for %s saved in: %s" % (filename_without_ext, file_plots_dir))
        print("  All histograms saved to ROOT file: %s" % combined_output)

def combine_histograms(output_dir):
    """Combine histograms using hadd."""
    # Combine all ROOT files
    root_files_dir = os.path.join(output_dir, "root_files")
    root_files = glob.glob(os.path.join(root_files_dir, "*.root"))
    if root_files:
        combined_output = os.path.join(output_dir, "combined_all_plots.root")
        cmd = ["hadd", "-f", combined_output] + root_files
        print("\nCombining all histograms:")
        print("  Running: %s" % " ".join(cmd))
        subprocess.call(cmd)

def main():
    parser = argparse.ArgumentParser(description="Process all ROOT files with their corresponding structure constants files")
    parser.add_argument("root_dir", help="Directory containing ROOT files")
    parser.add_argument("npy_dir", help="Directory containing structure constants files")
    parser.add_argument("--custom-wc", action="store_true", help="Use custom Wilson coefficient values")
    parser.add_argument("--delta-phi-only", action="store_true", help="Only process Delta Phi")
    parser.add_argument("--sigma-phi-only", action="store_true", help="Only process Sigma Phi")
    parser.add_argument("--delta-y-only", action="store_true", help="Only process Delta Y")
    parser.add_argument("--output-dir", default="combined_output", help="Output directory for combined histograms")
    
    args = parser.parse_args()
    
    # Create output directory
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    # Create plots directory
    plots_dir = os.path.join(args.output_dir, "plots")
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
    
    # Find matching files
    file_pairs = find_matching_files(args.root_dir, args.npy_dir)
    print("Found %d matching file pairs" % len(file_pairs))
    
    if not file_pairs:
        print("No matching file pairs found. Exiting.")
        sys.exit(1)
    
    # Run plotting scripts
    run_plotting_scripts(file_pairs, args.output_dir, args)
    
    # Combine histograms
    combine_histograms(args.output_dir)
    
    print("\nAll processing complete!")
    print("Combined histograms saved in: %s" % args.output_dir)
    print("Individual PDF plots saved in: %s/plots/<filename>/" % args.output_dir)

if __name__ == "__main__":
    main() 