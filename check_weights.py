import ROOT
import numpy as np

def inspect_geninfo(geninfo):
    """Inspect the GenInfo object in detail"""
    print("\nInspecting GenInfo object:")
    
    # Try to access common attributes
    try:
        print("\nAvailable methods/attributes:")
        for attr in dir(geninfo):
            if not attr.startswith('_'):  # Skip internal attributes
                print("- %s" % attr)
                
        # Try to access specific weight-related attributes
        if hasattr(geninfo, 'weights'):
            weights = geninfo.weights()
            print("\nWeights vector size: %d" % weights.size())
            print("First 5 weights:")
            for i in range(min(5, weights.size())):
                print("  [%d]: %s" % (i, weights[i]))
                
        if hasattr(geninfo, 'weight_EFT'):
            weight_eft = geninfo.weight_EFT()
            print("\nEFT weight: %s" % weight_eft)
            
        if hasattr(geninfo, 'binningValues'):
            binning = geninfo.binningValues()
            print("\nBinning values size: %d" % binning.size())
            print("First 5 binning values:")
            for i in range(min(5, binning.size())):
                print("  [%d]: %s" % (i, binning[i]))
            
    except Exception as e:
        print("Error inspecting GenInfo: %s" % e)

def inspect_root_file(filename):
    print("Opening file:", filename)
    
    f = ROOT.TFile.Open(filename)
    if not f or f.IsZombie():
        print("Error: cannot open file %s" % filename)
        return
    
    tree = f.Get("AnalysisTree")
    if not tree:
        print("Error: cannot find AnalysisTree")
        return
    
    # Get first entry to inspect
    tree.GetEntry(0)
    
    # Get GenInfo object
    geninfo = getattr(tree, 'genInfo')
    if geninfo:
        inspect_geninfo(geninfo)
        
        # Try to get weights for first few events
        print("\nChecking weights for first 5 events:")
        for i in range(min(5, tree.GetEntries())):
            tree.GetEntry(i)
            geninfo = getattr(tree, 'genInfo')
            print("\nEvent %d:" % i)
            try:
                if hasattr(geninfo, 'weights'):
                    weights = geninfo.weights()
                    print("Number of weights: %d" % weights.size())
                    if weights.size() > 0:
                        print("First weight: %s" % weights[0])
                        print("Last weight: %s" % weights[weights.size()-1])
            except Exception as e:
                print("Error accessing weights: %s" % e)
    
    print("\nTotal events in tree: %d" % tree.GetEntries())
    f.Close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python check_weights.py <root_file>")
        sys.exit(1)
    
    try:
        inspect_root_file(sys.argv[1])
    except Exception as e:
        print("Error during execution: %s" % e) 