#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import ROOT
import sys
from collect_EFT_reweight import WC_NAMES

# Predefined WC points
WC_POINTS = {
    'sm': [0.0] * 16,
    'ctGRe_p1': [10.0] + [0.0] * 15,  # ctGRe = 1
    'ctGRe_p2': [2.0] + [0.0] * 15,  # ctGRe = 2
    'ctGIm_p1': [0.0, 1.0] + [0.0] * 14,  # ctGIm = 1
    'ctGRe_ctGIm_p1': [1.0, 1.0] + [0.0] * 14,  # ctGRe = 1, ctGIm = 1
    'all_p1': [1.0] * 16,  # all WCs = 1
    'all_p0p1': [0.1] * 16,  # all WCs = 0.1
}

def print_available_points():
    """Print all available predefined points"""
    print "\nAvailable predefined points:"
    print "-" * 50
    for name, values in sorted(WC_POINTS.items()):
        print "%-15s:" % name,
        nonzero = [(WC_NAMES[i], v) for i, v in enumerate(values) if abs(v) > 1e-10]
        if nonzero:
            print ", ".join("%s=%.1f" % (wc, val) for wc, val in nonzero)
        else:
            print "all WCs = 0 (SM)"
    print "-" * 50

def calculate_event_weight(mg_weights, wc_values):
    """Calculate weight for a single event given its MG weights and desired WC values"""
    # Constants
    num_WCs = 16
    
    # 1. Constant term (SM point)
    c0 = mg_weights[201]  # weight 201
    
    # 2. Linear terms (16 terms)
    linear_terms = np.zeros(16)
    for i in range(16):
        linear_terms[i] = mg_weights[203 + i]  # weights 203-218
    
    # 3. Quadratic terms
    # a) Diagonal terms (WC²) - 16 terms
    diag_quad_indices = [18, 34, 49, 63, 76, 88, 99, 109, 118, 126, 134, 139, 144, 148, 151, 153]
    quad_diag = np.zeros(16)
    for i in range(16):
        quad_diag[i] = mg_weights[201 + diag_quad_indices[i]]
    
    # b) Mixed terms (WCi×WCj) - 120 terms
    mixed_terms = np.zeros(120)
    idx = 0
    for i in range(num_WCs):
        for j in range(i+1, num_WCs):
            if i == 0:  # ctGRe pairs
                mixed_terms[idx] = mg_weights[201 + 19+j-1]
            else:
                offset = diag_quad_indices[i]
                mixed_terms[idx] = mg_weights[201 + offset+j-i]
            idx += 1
    
    # Calculate final weight
    weight = c0
    
    # Add linear terms
    weight += np.sum(linear_terms * wc_values)
    
    # Add diagonal quadratic terms
    weight += np.sum(quad_diag * np.square(wc_values))
    
    # Add mixed terms
    idx = 0
    for i in range(num_WCs):
        for j in range(i+1, num_WCs):
            weight += mixed_terms[idx] * wc_values[i] * wc_values[j]
            idx += 1
    
    return weight

def process_events(root_filename, wc_values):
    """Process events and calculate weights"""
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
    
    # Process events
    weights = np.zeros(nentries)
    for ientry in range(nentries):
        if ientry % 100000 == 0:
            print "Processing event %d / %d" % (ientry, nentries)
        
        t.GetEntry(ientry)
        syst = t.genInfo.systweights()
        weights[ientry] = calculate_event_weight(syst, wc_values)
    
    f.Close()
    
    # Print summary statistics
    print "\nResults:"
    print "  Mean weight: %.6f" % np.mean(weights)
    print "  Std  weight: %.6f" % np.std(weights)
    print "  Min  weight: %.6f" % np.min(weights)
    print "  Max  weight: %.6f" % np.max(weights)
    
    return weights

def main():
    if len(sys.argv) != 3:
        print "Usage: python reweight_events.py <input.root> <point_name>"
        print "Example: python reweight_events.py input.root sm"
        print "Example: python reweight_events.py input.root ctGRe_p1"
        print_available_points()
        sys.exit(1)
    
    root_filename = sys.argv[1]
    point_name = sys.argv[2]
    
    # Get WC values from predefined points
    if point_name not in WC_POINTS:
        print "Error: Unknown point '%s'" % point_name
        print_available_points()
        sys.exit(1)
    
    wc_values = WC_POINTS[point_name]
    
    # Process events and calculate weights
    weights = process_events(root_filename, wc_values)

if __name__ == "__main__":
    main() 