#!/usr/bin/env python2

import ROOT
import sys

def list_branches(input_file):
    file = ROOT.TFile.Open(input_file)
    if not file or file.IsZombie():
        print("Error: Could not open the ROOT file:", input_file)
        return
    tree = file.Get("AnalysisTree")
    if not tree:
        print("Error: TTree 'AnalysisTree' not found in file:", input_file)
        return
    print("\nListing branches for file:", input_file)
    for branch in tree.GetListOfBranches():
        print(branch.GetName(), "-", branch.GetTitle())
    file.Close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python list_branches.py <ROOT_file1> [<ROOT_file2> ...]")
        sys.exit(1)
    # for root_file in sys.argv[1:]:
        list_branches("Ntuple_1211.root")
