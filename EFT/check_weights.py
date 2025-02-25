#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ROOT
import numpy as np

def inspect_eft_weights(filename):
    f = ROOT.TFile.Open(filename)
    if not f or f.IsZombie():
        print "Error: cannot open file %s" % filename
        return
    
    tree = f.Get("AnalysisTree")
    if not tree:
        print "Error: cannot find AnalysisTree"
        return

    n_entries = tree.GetEntries()
    print "\nTotal number of events in tree: %d" % n_entries

    # Get first event to examine weight structure
    tree.GetEntry(0)
    
    # Get number of weights
    n_weights = tree.n_eft_weights
    print "\nNumber of EFT weights: %d" % n_weights
    
    # Print reference point weight
    ref_weight = tree.ref_point_weight
    print "\nReference point weight: %f" % ref_weight
    
    # Print first few weights
    print "\nFirst 10 EFT weights:"
    for i in range(min(10, n_weights)):
        weight_value = getattr(tree, "eft_weight_%d" % i)
        print "Weight[%d] = %f" % (i, weight_value)
    
    # Check weight from different events
    print "\nChecking weight consistency across first 5 events:"
    ref_weights = []
    for i in range(min(5, n_entries)):
        tree.GetEntry(i)
        ref_weights.append(tree.ref_point_weight)
    
    print "Reference weights:", ref_weights
    if len(set(ref_weights)) == 1:
        print "[OK] Reference weights are consistent across events"
    else:
        print "[!] Reference weights vary across events"

    # Print specific weight index
    def print_weight_stats(weight_idx):
        print "\nStatistics for weight index %d:" % weight_idx
        values = []
        for i in range(n_entries):
            tree.GetEntry(i)
            values.append(getattr(tree, "eft_weight_%d" % weight_idx))
        values = np.array(values)
        print "  Mean: %f" % np.mean(values)
        print "  Std:  %f" % np.std(values)
        print "  Min:  %f" % np.min(values)
        print "  Max:  %f" % np.max(values)
    
    # Print stats for reference point and first EFT weight
    print_weight_stats(0)
    print_weight_stats(1)
    
    f.Close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "Usage: python check_weights.py <root_file>"
        sys.exit(1)
    
    inspect_eft_weights(sys.argv[1])

    # /data/dust/group/cms/zprime-uhh/Preselection_EFT_UL17/workdir_Preselection_EFT_UL17_semilepton_0_700/uhh2.AnalysisModuleRunner.MC.MC_EFT_Mttbar_0-700_UL17_1.root