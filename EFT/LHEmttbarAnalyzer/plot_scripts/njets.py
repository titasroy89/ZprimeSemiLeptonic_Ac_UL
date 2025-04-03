#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ROOT
from array import array
import sys

def plot_numJets():
    ROOT.gStyle.SetOptStat(0)  
    ROOT.gROOT.SetBatch(True)

    # **Define Cross-Section Values (in pb)**
    sigma1 = 1.842e+02  # 184.2 pb for 0-700 GeV
    sigma2 = 2.484e+01  # 24.84 pb for 700-900 GeV
    sigma3 = 4.525e+01  # 45.25 pb for 900-Inf GeV

    # **Define Integrated Luminosity (in pb^{-1})**
    lumi = 41800  # 41.8 fb^{-1} = 41800 pb^{-1}

    file1_path = "0_700_root/lhe_0_700.root"
    file2_path = "700_900_root/lhe_700_900.root"
    file3_path = "900_Inf_root/lhe_900Inf.root"

    file1 = ROOT.TFile.Open(file1_path)
    file2 = ROOT.TFile.Open(file2_path)
    file3 = ROOT.TFile.Open(file3_path)

    if not file1 or file1.IsZombie():
        print "Error: Cannot open file:", file1_path
        sys.exit(1)
    if not file2 or file2.IsZombie():
        print "Error: Cannot open file:", file2_path
        sys.exit(1)
    if not file3 or file3.IsZombie():
        print "Error: Cannot open file:", file3_path
        sys.exit(1)

    hist_name = "LHEMttbarAnalyzer/numJets"

    hist1 = file1.Get(hist_name)
    if not hist1:
        print "Error: Cannot find histogram '{}' in file {}".format(hist_name, file1_path)
        sys.exit(1)
    hist1 = hist1.Clone("hist1")

    hist2 = file2.Get(hist_name)
    if not hist2:
        print "Error: Cannot find histogram '{}' in file {}".format(hist_name, file2_path)
        sys.exit(1)
    hist2 = hist2.Clone("hist2")

    hist3 = file3.Get(hist_name)
    if not hist3:
        print "Error: Cannot find histogram '{}' in file {}".format(hist_name, file3_path)
        sys.exit(1)
    hist3 = hist3.Clone("hist3")

    N_gen1 = hist1.GetSumOfWeights()
    N_gen2 = hist2.GetSumOfWeights()
    N_gen3 = hist3.GetSumOfWeights()

    if N_gen1 == 0 or N_gen2 == 0 or N_gen3 == 0:
        print "Error: One of the histograms has zero generated events. Cannot scale."
        sys.exit(1)

    scaling_factor1 = (sigma1 * lumi) / N_gen1
    scaling_factor2 = (sigma2 * lumi) / N_gen2
    scaling_factor3 = (sigma3 * lumi) / N_gen3

    print "Scaling Factors:"
    print "hist1 (0-700 GeV):", scaling_factor1
    print "hist2 (700-900 GeV):", scaling_factor2
    print "hist3 (900-Inf GeV):", scaling_factor3

    # **Scale Histograms by (σ × L) / N_gen**
    hist1.Scale(scaling_factor1)
    hist2.Scale(scaling_factor2)
    hist3.Scale(scaling_factor3)

    normalize = True  

    if normalize:
        if hist1.Integral() != 0:
            hist1.Scale(1.0 / hist1.Integral())
            print "Integral of hist1 after normalization:", hist1.Integral()
        else:
            print "Warning: hist1 has zero integral, cannot normalize."

        if hist2.Integral() != 0:
            hist2.Scale(1.0 / hist2.Integral())
            print "Integral of hist2 after normalization:", hist2.Integral()
        else:
            print "Warning: hist2 has zero integral, cannot normalize."

        if hist3.Integral() != 0:
            hist3.Scale(1.0 / hist3.Integral())
            print "Integral of hist3 after normalization:", hist3.Integral()
        else:
            print "Warning: hist3 has zero integral, cannot normalize."

    hist1.SetLineColor(ROOT.kRed)
    hist2.SetLineColor(ROOT.kGreen+2)
    hist3.SetLineColor(ROOT.kBlue)
      # Distinct color for combined histogram

    hist1.SetLineWidth(2)
    hist2.SetLineWidth(2)
    hist3.SetLineWidth(2)

    hist_combined = hist1.Clone("hist_combined")
    hist_combined.SetLineColor(ROOT.kBlue+2)  # Distinct color for combined histogram
    hist_combined.SetLineWidth(2)  # Thicker line for combined histogram
    # hist_combined.SetLineStyle(1)  # Solid line


    hist_combined.Add(hist2)
    hist_combined.Add(hist3)

    if normalize:
        if hist_combined.Integral() != 0:
            hist_combined.Scale(1.0 / hist_combined.Integral())
            # print "Integral of hist_combined after normalization:", hist_combined.Integral()
        else:
            print "Warning: hist_combined has zero integral, cannot normalize."

    c1 = ROOT.TCanvas("c1", "numJets Distribution", 800, 600)
    c1.SetGrid()

    hist1.GetXaxis().SetTitle("Number of Jets")
    if normalize:
        hist1.GetYaxis().SetTitle("Normalized Events")
    else:
        hist1.GetYaxis().SetTitle("Events")

    # hist1.Draw("HIST")
    # hist2.Draw("HIST SAME")
    # hist3.Draw("HIST SAME")
    hist_combined.Draw("HIST SAME") 

    legend = ROOT.TLegend(0.65, 0.75, 0.88, 0.88)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.AddEntry(hist1, "Mttbar (0-700 GeV)", "l")
    legend.AddEntry(hist2, "Mttbar (700-900 GeV)", "l")
    legend.AddEntry(hist3, "Mttbar (900-Inf GeV)", "l")
    # legend.Draw()

    max_y = max(hist1.GetMaximum(), hist2.GetMaximum(), hist3.GetMaximum())
    hist1.SetMaximum(max_y * 1.2)

    output_image = "numJets_comb_weighted_normalized.png"
    c1.SaveAs(output_image)
    print "Plot saved as:", output_image

    file1.Close()
    file2.Close()
    file3.Close()

if __name__ == "__main__":
    plot_numJets()
