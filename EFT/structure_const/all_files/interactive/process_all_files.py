"""
Script to process all ROOT files with their corresponding structure constants files.
This script will:
1. Find all ROOT files and match them with their structure constants files
2. Run the plotting scripts for each pair
3. Combine the histograms using hadd

Usage:
    python process_all_files.py <root_files_dir> <structure_constants_dir> [--custom-wc] [--delta-phi-only] [--sigma-phi-only] [--delta-y-only]
    /data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_deltaPhi_sigmaPhi_ttree
    /data/dust/group/cms/zprime-uhh/Analysis_EFT_UL17/muon/workdir_Analysis_EFT_UL17_muon_semilepton_deltayreco_deltaPhi_sigmaPhi_ttree/ ../../correct_scripts/structure_constants_all_files_2017/
"""

import multiprocessing
from functools import partial
import glob
import os
import sys
import subprocess
import argparse

# global counter for tracking progress
counter = None

def find_matching_files(root_dir, npy_dir):
    #Find matching ROOT and NPY files.

    # Get all ROOT files
    root_files = glob.glob(os.path.join(root_dir, "*.root"))
    
    # Get all NPY files
    npy_files = glob.glob(os.path.join(npy_dir, "*.npy"))
    
    # Find matching pairs
    file_pairs = []
    for root_file in root_files:
        root_basename = os.path.basename(root_file)
        root_filename = os.path.splitext(root_basename)[0]
        
        # Expected NPY filename pattern
        expected_npy_filename = root_filename + "_structure_constants.npy"
        
        # Look for matching NPY file
        for npy_file in npy_files:
            npy_basename = os.path.basename(npy_file)
            if npy_basename == expected_npy_filename:
                file_pairs.append((root_file, npy_file))
                print("Matched: {} with {}".format(root_basename, npy_basename))
                break
    
    return file_pairs

def process_file_pair(file_pair, output_dir, args):
    #Process a single file pair.
    global counter
    root_file, npy_file = file_pair
    
    # Update counter and get current value
    with counter.get_lock():
        counter.value += 1
        current = counter.value
    
    total_files = args.total_files
    print("\nProcessing file pair [{}/{}]:".format(current, total_files))
    print("  ROOT file: %s" % root_file)
    print("  NPY file: %s" % npy_file)
    
    basename = os.path.basename(root_file)
    filename_without_ext = os.path.splitext(basename)[0]
    
    # Create separate directories for PDF plots for this file
    file_plots_dir = os.path.join(output_dir, "plots", filename_without_ext)
    if not os.path.exists(file_plots_dir):
        os.makedirs(file_plots_dir)
    
    # Create a single output ROOT file for all plots
    root_output_dir = os.path.join(output_dir, "root_files")
    if not os.path.exists(root_output_dir):
        os.makedirs(root_output_dir)
        
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
            
        if args.fast_mode:
            cmd.append("--fast-mode")
        
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
                
            if args.fast_mode:
                cmd.append("--fast-mode")
            
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
                
            if args.fast_mode:
                cmd.append("--fast-mode")
            
            print("  Running: %s" % " ".join(cmd))
            subprocess.call(cmd)
            print("  SigmaPhi plots saved to: %s" % sigmaPhi_plots_dir)
    
    print("  All plots for %s saved in: %s" % (filename_without_ext, file_plots_dir))
    print("  All histograms saved to ROOT file: %s" % combined_output)
    
    return combined_output

def run_plotting_scripts(file_pairs, output_dir, args):
    #Run plotting scripts for all file pairs.
    global counter
    
    # Initialize counter as a shared variable
    counter = multiprocessing.Value('i', 0)
    
    # Store total files count in args for access in process_file_pair
    args.total_files = len(file_pairs)
    
    # Create output directory for ROOT files
    root_output_dir = os.path.join(output_dir, "root_files")
    if not os.path.exists(root_output_dir):
        os.makedirs(root_output_dir)
    
    # Determine number of processes to use
    num_processes = args.num_processes
    if num_processes <= 0:
        # Use 75% of available cores by default
        num_processes = max(1, int(multiprocessing.cpu_count() * 0.75))
    
    print("Processing {} file pairs using {} processes...".format(len(file_pairs), num_processes))
    
    # Create a partial function with fixed arguments
    process_func = partial(process_file_pair, output_dir=output_dir, args=args)
    
    # Process files in parallel
    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.map(process_func, file_pairs)
    pool.close()
    pool.join()
    
    return results

def combine_histograms(output_dir):
    #Combine histograms using hadd. Not using this currently.

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
    parser.add_argument("--num-processes", type=int, help="Number of parallel processes to use")
    parser.add_argument("--skip-combine", action="store_true", default=True, help="Skip combining histograms at the end")
    parser.add_argument("--do-combine", action="store_false", dest="skip_combine", help="Combine histograms at the end")
    parser.add_argument("--fast-mode", action="store_true", help="Run in fast mode with reduced set of Wilson coefficients")
    
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
    if not args.skip_combine:
        combine_histograms(args.output_dir)
    
    print("\nAll processing complete!")
    print("Combined histograms saved in: %s" % args.output_dir)
    print("Individual PDF plots saved in: %s/plots/<filename>/" % args.output_dir)

if __name__ == "__main__":
    main() 