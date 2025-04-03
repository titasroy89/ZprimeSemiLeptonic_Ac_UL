#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import ROOT
import sys
from collect_EFT_reweight import (
    WC_NAMES, 
    obtain_structure_constant,
    calculate_new_weights,
    print_structure_constants
)

def load_weights_from_root(root_filename):
    """Load weights from ROOT file and return as numpy array"""
    f = ROOT.TFile.Open(root_filename)
    if not f or f.IsZombie():
        print "Error: cannot open file", root_filename
        sys.exit(1)
    
    # Get the TTree
    t = f.Get("AnalysisTree")
    if not t:
        print "Error: cannot find TTree 'AnalysisTree'"
        sys.exit(1)
    
    nentries = t.GetEntries()
    print "Found %d events in the tree" % nentries
    
    # Pre-allocate the numpy array for indices 201-354
    mg_weights = np.zeros((nentries, 355), dtype=np.float64)
    
    # Fill weights
    for ientry in range(nentries):
        if ientry % 100000 == 0:
            print "Processing event %d / %d" % (ientry, nentries)
        t.GetEntry(ientry)
        syst = t.genInfo.systweights()
        for j in range(201, 355):  # Only collect weights 201-354
            mg_weights[ientry, j] = syst[j]
    
    f.Close()
    return mg_weights

def calculate_structure_constants(mg_weights):
    """Calculate structure constants for all events"""
    print "\nCalculating structure constants..."
    num_WCs = 16
    structures = obtain_structure_constant(num_WCs, mg_weights)
    print "Obtained structure constants for %d events" % len(structures)
    return structures

def analyze_new_point(structures, wc_values):
    """Analyze weights for a new point in WC space"""
    weights = calculate_new_weights(structures, wc_values)
    
    # Basic statistics
    mean_weight = np.mean(weights)
    std_weight = np.std(weights)
    min_weight = np.min(weights)
    max_weight = np.max(weights)
    
    print "\nWeight statistics for point:"
    for i, val in enumerate(wc_values):
        if abs(val) > 1e-10:  # Only print non-zero WCs
            print "  %s = %.3f" % (WC_NAMES[i], val)
    print "\nResults:"
    print "  Mean weight: %.6f" % mean_weight
    print "  Std  weight: %.6f" % std_weight
    print "  Min  weight: %.6f" % min_weight
    print "  Max  weight: %.6f" % max_weight
    
    return weights

def main():
    if len(sys.argv) != 2:
        print "Usage: python analyze_EFT_weights.py <input.root>"
        sys.exit(1)
    
    root_filename = sys.argv[1]
    
    # 1. Load weights from ROOT file
    print "\nStep 1: Loading weights from ROOT file..."
    mg_weights = load_weights_from_root(root_filename)
    
    # 2. Calculate structure constants
    print "\nStep 2: Calculating structure constants..."
    structures = calculate_structure_constants(mg_weights)
    
    # Save structure constants for later use
    output_file = "structure_constants.npy"
    np.save(output_file, structures)
    print "Saved structure constants to", output_file
    
    # 3. Calculate weights for some example points
    print "\nStep 3: Testing some example points..."
    
    # Example 1: SM point
    print "\nSM point (all WCs = 0):"
    sm_weights = analyze_new_point(structures, [0.0]*16)
    
    # Example 2: ctGRe = 1
    print "\nPoint with ctGRe = 1:"
    wc_test1 = [1.0] + [0.0]*15
    weights1 = analyze_new_point(structures, wc_test1)
    
    # Example 3: ctGRe = 1, ctGIm = 1
    print "\nPoint with ctGRe = 1, ctGIm = 1:"
    wc_test2 = [1.0, 1.0] + [0.0]*14
    weights2 = analyze_new_point(structures, wc_test2)
    
    # Example 4: All WCs = 0.1
    print "\nPoint with all WCs = 0.1:"
    wc_test3 = [0.1]*16
    weights3 = analyze_new_point(structures, wc_test3)
    
    print "\nAnalysis complete! You can now:"
    print "1. Load the saved structure constants from '%s'" % output_file
    print "2. Use them to calculate weights for any WC point"
    print "3. Modify this script to test other WC combinations"

if __name__ == "__main__":
    main() 