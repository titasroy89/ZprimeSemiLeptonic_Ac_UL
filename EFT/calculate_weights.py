#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import ROOT
import sys
from collect_EFT_rewrite import (
    WC_NAMES,
    obtain_structure_constant,
    calculate_new_weights
)

def process_events(root_filename, wc_values):
    """Process events and calculate weights for given WC values"""
    # Input validation
    if len(wc_values) != 16:
        print "Error: Must provide exactly 16 Wilson coefficients"
        sys.exit(1)
    
    # Print WC configuration
    print "\nCalculating weights for WC configuration:"
    for i, val in enumerate(wc_values):
        if abs(val) > 1e-10:  # Only print non-zero WCs
            print "  %s = %.3f" % (WC_NAMES[i], val)
    
    # Open ROOT file
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
    print "\nProcessing %d events..." % nentries
    
    # Arrays to store results
    all_weights = np.zeros(nentries)
    
    # Process events in chunks for memory efficiency
    chunk_size = 10000
    for chunk_start in range(0, nentries, chunk_size):
        chunk_end = min(chunk_start + chunk_size, nentries)
        chunk_size_actual = chunk_end - chunk_start
        
        # Print progress
        if chunk_start % 100000 == 0:
            print "Processing events %d to %d..." % (chunk_start, chunk_end)
        
        # Get weights for this chunk
        mg_weights_chunk = np.zeros((chunk_size_actual, 355), dtype=np.float64)
        
        # Fill weights for this chunk
        for i, ientry in enumerate(range(chunk_start, chunk_end)):
            t.GetEntry(ientry)
            syst = t.genInfo.systweights()
            for j in range(201, 355):  # Only collect weights 201-354
                mg_weights_chunk[i, j] = syst[j]
        
        # Calculate structure constants for this chunk
        structures_chunk = obtain_structure_constant(16, mg_weights_chunk)
        
        # Calculate new weights for this chunk
        weights_chunk = calculate_new_weights(structures_chunk, wc_values)
        
        # Store results
        all_weights[chunk_start:chunk_end] = weights_chunk
    
    f.Close()
    
    # Print summary statistics
    print "\nResults:"
    print "  Mean weight: %.6f" % np.mean(all_weights)
    print "  Std  weight: %.6f" % np.std(all_weights)
    print "  Min  weight: %.6f" % np.min(all_weights)
    print "  Max  weight: %.6f" % np.max(all_weights)
    
    return all_weights

def main():
    if len(sys.argv) < 3:
        print "Usage: python calculate_weights.py <input.root> <wc1> [wc2 wc3 ...]"
        print "Example for SM point: python calculate_weights.py input.root 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
        print "Example for ctGRe=1: python calculate_weights.py input.root 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
        sys.exit(1)
    
    root_filename = sys.argv[1]
    
    # Parse WC values
    try:
        if len(sys.argv) == 3:
            # If only one value provided, use it for ctGRe and 0 for others
            wc_values = [float(sys.argv[2])] + [0.0]*15
        else:
            # Otherwise expect all 16 values
            wc_values = [float(x) for x in sys.argv[2:18]]  # Only take first 16 values if more provided
            if len(wc_values) < 16:
                wc_values.extend([0.0] * (16 - len(wc_values)))
    except ValueError:
        print "Error: WC values must be numbers"
        sys.exit(1)
    
    # Process events and calculate weights
    weights = process_events(root_filename, wc_values)

if __name__ == "__main__":
    main() 