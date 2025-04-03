#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
from collect_EFT_reweight import WC_NAMES

def main():
    if len(sys.argv) != 2:
        print "Usage: python inspect_structure_constants.py <structure_constants.npy>"
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Load the structure constants
    structures = np.load(input_file)
    
    # Print basic information
    print "\nStructure Constants File Information:"
    print "------------------------------------"
    print "Array shape:", structures.shape
    print "Data type:", structures.dtype
    print "Number of events:", structures.shape[0]
    print "Number of coefficients per event:", structures.shape[1]
    
    # Print structure of coefficients for first event
    print "\nFirst event coefficients breakdown:"
    print "--------------------------------"
    
    # Constant term (1) - position 0
    print "Constant term (SM point):", structures[0,0]
    
    # Linear terms (16) - positions 1-16
    print "\nLinear terms (first 5 WCs):"
    for i in range(5):
        print "%-6s: %g" % (WC_NAMES[i], structures[0,1+i])
    
    print "\nQuadratic terms:"
    # Diagonal quadratic terms (16) - positions 17-32
    print "\n  Squared terms (first 5 WCs):"
    for i in range(5):
        print "  %-6s²: %g" % (WC_NAMES[i], structures[0,17+i])
    
    # Off-diagonal quadratic terms (120) - positions 33-152
    print "\n  Mixed terms (first 5 pairs):"
    pairs = [(0,1), (0,2), (0,3), (0,4), (0,5)]  # First 5 pairs
    for idx, (i,j) in enumerate(pairs):
        print "  %-6s × %-6s: %g" % (WC_NAMES[i], WC_NAMES[j], structures[0,33+idx])
    
    print "\nStructure of the EFT weight polynomial:"
    print "w = c₀ + Σᵢ(cᵢWCᵢ) + Σᵢⱼ(dᵢⱼWCᵢWCⱼ)"
    print "where:"
    print "- c₀ is the constant term (SM)"
    print "- cᵢ are the linear coefficients"
    print "- dᵢⱼ are the quadratic coefficients (including both squared and mixed terms)"
    print "  * For i=j: dᵢᵢWCᵢ² (squared terms)"
    print "  * For i≠j: dᵢⱼWCᵢWCⱼ (mixed terms)"

if __name__ == "__main__":
    main() 