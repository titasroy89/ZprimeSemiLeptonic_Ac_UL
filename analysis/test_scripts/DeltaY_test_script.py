#! /usr/bin/env python
from ROOT import *
import ROOT
import sys
import numpy

# As an input, Higgs Combine takes a txt based file containing the observed and expected yields.


# list of DeltaY ROOT files 
input_files = ["DeltaY_UL18_muon.root" ]

# Output ROOT file
output_file = ROOT.TFile("DeltaY_UL18_muon.root", "RECREATE")
output_file.cd()

for input_file in input_files:
    # Opening root file
    infile = ROOT.TFile(input_file)
    # Getting DeltaY histogram from the file
    hist = infile.Get("px1")
    if hist:
        # The Clone() method creates a copy of the histogram. One can save multiple histograms with the same name from different input files in the same output file.
        # Clone the histogram and give it a different name
        hist_clone = hist.Clone("px1")
        # Writing the histogram to the output file
        hist_clone.Write()
    infile.Close()

# Close the output file
output_file.Close()




