import ROOT
import numpy as np
from array import array

def collect_weights(filename, weight_branch_name):
    """
    Collect EFT weights from ROOT file
    
    Parameters:
    - filename: path to ROOT file
    - weight_branch_name: name of the branch containing weights
    
    Returns:
    - numpy array of shape (n_events, n_weights)
    """
    f = ROOT.TFile.Open(filename)
    if not f or f.IsZombie():
        raise RuntimeError(f"Cannot open file {filename}")
    
    tree = f.Get("Events")
    if not tree:
        raise RuntimeError("Cannot find Events tree")
    
    weights_list = []
    n_entries = tree.GetEntries()
    
    # Progress tracking
    print(f"Processing {n_entries} events...")
    
    for i in range(n_entries):
        if i % 10000 == 0:
            print(f"Processing event {i}/{n_entries}")
            
        tree.GetEntry(i)
        
        # Get weights depending on storage format
        weights = getattr(tree, weight_branch_name)
        
        if isinstance(weights, ROOT.vector('double')):
            # Handle std::vector<double>
            weights = [weights[j] for j in range(weights.size())]
        elif isinstance(weights, ROOT.vector('float')):
            # Handle std::vector<float>
            weights = [weights[j] for j in range(weights.size())]
        elif hasattr(weights, 'size'):
            # Handle other vector types
            weights = [weights[j] for j in range(weights.size())]
        else:
            # Handle scalar weight
            weights = [weights]
            
        weights_list.append(weights)
    
    f.Close()
    
    return np.array(weights_list)

def process_file_and_calculate_constants(filename, weight_branch_name, num_WCs=16):
    """
    Process ROOT file and calculate structure constants
    """
    # Collect weights
    mg_weights = collect_weights(filename, weight_branch_name)
    print(f"Collected weights shape: {mg_weights.shape}")
    
    # Import the structure constant calculation
    from collect_EFT_reweight import obtain_structure_constant
    
    # Calculate structure constants
    structures = obtain_structure_constant(num_WCs, mg_weights)
    print(f"Calculated structure constants for {len(structures)} events")
    
    return structures

# Usage example
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python collect_weights.py <root_file> <weight_branch_name>")
        sys.exit(1)
        
    structures = process_file_and_calculate_constants(sys.argv[1], sys.argv[2]) 