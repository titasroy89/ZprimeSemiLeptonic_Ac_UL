import numpy as np
from collect_EFT_reweight import (
    WC_NAMES,
    load_structure_constants,
    calculate_new_weights,
    print_structure_constants
)

def main():
    import sys
    if len(sys.argv) != 2:
        print "Usage: python calculate_EFT_weights.py <structure_constants.npy>"
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Load the structure constants
    structures = load_structure_constants(input_file)
    
    # Print structure constants for first event as a reference
    print_structure_constants(structures[0], 0)
    
    print "\nCalculating weights for each WC = 10 (others = 0):"
    print "%-10s %-15s" % ("WC Name", "First Event Weight")
    print "-" * 30
    
    # For each WC, set it to 10 and others to 0
    num_WCs = 16
    for i in range(num_WCs):
        # Create WC values array with all zeros
        wc_values = [0.0] * num_WCs
        # Set the i-th WC to 10
        wc_values[i] = 10.0
        
        # Calculate weights
        weights = calculate_new_weights(structures, wc_values)
        
        # Print result for first event
        print "%-10s %-15g" % (WC_NAMES[i], weights[0])
    
    # Also print SM point for comparison
    print "\nSM point (all WCs = 0):"
    sm_weights = calculate_new_weights(structures, [0.0] * num_WCs)
    print "Weight for first event: %g" % sm_weights[0]

if __name__ == "__main__":
    main() 