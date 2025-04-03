#!/usr/bin/env python
from __future__ import division, print_function

import os
import sys
import glob
import argparse
import subprocess

def create_condor_submit_file(root_file, output_dir, calc_only=False, plot_only=False, custom_wc=False, variables=None):
    """Create a condor submit file for a single ROOT file"""
    file_basename = os.path.basename(root_file)
    sample_name = file_basename.replace("uhh2.AnalysisModuleRunner.MC.", "").replace(".root", "")
    
    # Create sample-specific output directory
    sample_output_dir = os.path.join(os.path.abspath(output_dir), sample_name)
    if not os.path.exists(sample_output_dir):
        os.makedirs(sample_output_dir)
    
    # Create condor submit file
    submit_file = os.path.join(sample_output_dir, "condor_job.submit")
    
    # Create shell script to run the job
    shell_script = os.path.join(sample_output_dir, "run_job.sh")
    
    # Get absolute path to the current directory and script
    current_dir = os.path.abspath(os.path.dirname(__file__))
    script_path = os.path.join(current_dir, "process_all_samples.py")
    
    # Build command with absolute path to the script
    cmd = "python {0} --input-dir {1} --output-dir {2}".format(
        script_path,
        os.path.dirname(root_file),
        sample_output_dir
    )
    
    # Add specific file pattern to only process this file
    file_pattern = os.path.basename(root_file)
    cmd += " --file-pattern '{0}'".format(file_pattern)
    
    if calc_only:
        cmd += " --calc-only"
    if plot_only:
        cmd += " --plot-only"
    if custom_wc:
        cmd += " --custom-wc"
    if variables:
        cmd += " --variables {0}".format(" ".join(variables))
    
    # Write shell script
    with open(shell_script, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Setup CMSSW environment\n")
        f.write("source /cvmfs/cms.cern.ch/cmsset_default.sh\n")
        f.write("cd /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src\n")
        f.write("eval `scramv1 runtime -sh`\n")
        f.write("cd {0}\n".format(current_dir))
        f.write("echo 'Running: {0}'\n".format(cmd))
        f.write("{0}\n".format(cmd))
    
    # Make shell script executable
    os.chmod(shell_script, 0o755)
    
    # Write condor submit file
    with open(submit_file, 'w') as f:
        f.write("universe = vanilla\n")
        f.write("executable = {0}\n".format(shell_script))
        f.write("output = {0}/condor.out\n".format(sample_output_dir))
        f.write("error = {0}/condor.err\n".format(sample_output_dir))
        f.write("log = {0}/condor.log\n".format(sample_output_dir))
        f.write("request_memory = 4000\n")  # Request 4GB of memory
        f.write("request_cpus = 1\n")
        f.write("queue\n")
    
    return submit_file

def main():
    parser = argparse.ArgumentParser(description='Prepare batch jobs to process ROOT files')
    parser.add_argument('--input-dir', type=str, required=True,
                        help='Directory containing ROOT files to process')
    parser.add_argument('--output-dir', type=str, default='results',
                        help='Directory to store output files')
    parser.add_argument('--calc-only', action='store_true',
                        help='Only calculate structure constants, skip plotting')
    parser.add_argument('--plot-only', action='store_true',
                        help='Only create plots, skip structure constant calculation')
    parser.add_argument('--variables', type=str, nargs='+', default=['DeltaYreco', 'Delta_phi', 'Sigma_phi'],
                        help='Variables to plot (default: DeltaYreco Delta_phi Sigma_phi)')
    parser.add_argument('--custom-wc', action='store_true',
                        help='Use custom Wilson coefficient values defined in the script')
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
        sys.exit(1)
    
    print("Found {} ROOT files to process".format(len(root_files)))
    
    # Create a directory for all submit files
    submit_dir = os.path.join(os.getcwd(), "condor_submit_files")
    if not os.path.exists(submit_dir):
        os.makedirs(submit_dir)
    
    # Create a master submit file that includes all individual submit files
    master_submit_file = os.path.join(submit_dir, "submit_all.sh")
    with open(master_submit_file, "w") as master_file:
        master_file.write("#!/bin/bash\n\n")
        master_file.write("# This script submits all condor jobs\n\n")
        master_file.write("# Load condor environment if needed\n")
        master_file.write("# Uncomment the line below if you need to load the condor module\n")
        master_file.write("# module load condor\n\n")
        
        # Create merge script
        merge_script_path = os.path.join(os.getcwd(), "merge_results.sh")
        with open(merge_script_path, "w") as merge_script:
            merge_script.write("#!/bin/bash\n\n")
            merge_script.write("# This script merges the results from all batch jobs\n\n")
            
            # Setup CMSSW environment
            merge_script.write("# Setup CMSSW environment\n")
            merge_script.write("source /cvmfs/cms.cern.ch/cmsset_default.sh\n")
            merge_script.write("cd /data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src\n")
            merge_script.write("eval `scramv1 runtime -sh`\n")
            merge_script.write("cd {}\n\n".format(os.path.abspath(os.path.dirname(__file__))))
            
            # Add commands to merge structure constants
            if not args.plot_only:
                merge_script.write("# Merge structure constants\n")
                merge_script.write("python {} --input-dir {} --output-dir {} --plot-only --merge-plots".format(
                    os.path.join(os.path.abspath(os.path.dirname(__file__)), "process_all_samples.py"),
                    args.input_dir, 
                    os.path.abspath(args.output_dir)))
                if args.custom_wc:
                    merge_script.write(" --custom-wc")
                if args.variables:
                    merge_script.write(" --variables {}".format(" ".join(args.variables)))
                if args.file_pattern != "*.root":
                    merge_script.write(" --file-pattern '{}'".format(args.file_pattern))
                merge_script.write("\n\n")
            
            merge_script.write("echo 'All results merged successfully!'\n")
        
        # Make merge script executable
        os.chmod(merge_script_path, os.stat(merge_script_path).st_mode | 0o111)
        
        print("Created merge script: {}".format(merge_script_path))
        
        # Create a script to check job status
        check_script_path = os.path.join(os.getcwd(), "check_jobs.sh")
        with open(check_script_path, "w") as check_script:
            check_script.write("#!/bin/bash\n\n")
            check_script.write("# This script checks the status of all condor jobs\n\n")
            check_script.write("condor_q | grep $(whoami)\n")
        
        # Make check script executable
        os.chmod(check_script_path, os.stat(check_script_path).st_mode | 0o111)
        
        # Process each ROOT file
        submit_files = []
        for i, root_file in enumerate(root_files):
            submit_file = create_condor_submit_file(
                root_file, 
                args.output_dir, 
                calc_only=args.calc_only, 
                plot_only=args.plot_only, 
                custom_wc=args.custom_wc,
                variables=args.variables
            )
            submit_files.append(submit_file)
            
            # Add to master submit file
            master_file.write("echo 'Submitting job for {}'\n".format(os.path.basename(root_file)))
            master_file.write("condor_submit {}\n".format(submit_file))
        
        master_file.write("\necho 'All jobs submitted. Run {} after completion to merge results.'\n".format(merge_script_path))
    
    # Make master submit file executable
    os.chmod(master_submit_file, 0o755)
    
    print("\nAll submit files created successfully!")
    print("To submit all jobs, run: {}".format(master_submit_file))
    print("To check job status, run: {}".format(check_script_path))
    print("After all jobs complete, run: {}".format(merge_script_path))
    print("\nIf condor_submit is not in your PATH, you may need to load the condor module first:")
    print("module load condor")

if __name__ == "__main__":
    main() 