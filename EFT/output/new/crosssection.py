import ROOT

def overlay_histograms_normalized():
    file1 = ROOT.TFile.Open("mttbar_multiprocess_0_700.root")
    file2 = ROOT.TFile.Open("mttbar_multiprocess_700_900.root")
    file3 = ROOT.TFile.Open("mttbar_multiprocess_900Inf.root")
    hist1 = file1.Get("hist_mttbar_reconstructed")
    hist2 = file2.Get("hist_mttbar_total")
    hist3 = file3.Get("hist_mttbar_total")

    # Cross-section values in pb
    sigma1 = 1.842e+02  # 184.2 pb
    sigma2 = 2.484e+01  # 24.84 pb
    sigma3 = 4.525e+01  # 45.25 pb

    # Integrated luminosity in pb^{-1} (2017 data)
    lumi = 41800  # 41.8 fb^{-1} = 41800 pb^{-1}

    # Get the effective number of generated events
    N_gen1 = hist1.GetSumOfWeights()
    N_gen2 = hist2.GetSumOfWeights()
    N_gen3 = hist3.GetSumOfWeights()

    # Calculate scaling factors
    scaling_factor1 = (sigma1 * lumi) / N_gen1
    scaling_factor2 = (sigma2 * lumi) / N_gen2
    scaling_factor3 = (sigma3 * lumi) / N_gen3

    # Scale histograms
    hist1.Scale(scaling_factor1)
    hist2.Scale(scaling_factor2)
    hist3.Scale(scaling_factor3)

    # Print expected events and integrals
    expected_events1 = sigma1 * lumi
    expected_events2 = sigma2 * lumi
    expected_events3 = sigma3 * lumi

    integral1 = hist1.Integral()
    if integral1 != 0:
        hist1.Scale(1.0 / integral1)
    else:
        print("Histogram1 has zero integral, cannot normalize.")

    integral2 = hist2.Integral()
    if integral2 != 0:
        hist2.Scale(1.0 / integral2)
    else:
        print("Histogram2 has zero integral, cannot normalize.")

    integral3 = hist3.Integral()
    if integral3 != 0:
        hist3.Scale(1.0 / integral3)
    else:
        print("Histogram3 has zero integral, cannot normalize.")

    print("Expected events for hist1: {expected_events1}".format(expected_events1=expected_events1))
    print("Expected events for hist2: {expected_events2}".format(expected_events2=expected_events2))
    print("Expected events for hist3: {expected_events3}".format(expected_events3=expected_events3))

    print("Integral after scaling (hist1):", hist1.Integral())
    print("Integral after scaling (hist2):", hist2.Integral())
    print("Integral after scaling (hist3):", hist3.Integral())

    hist1.SetLineColor(ROOT.kBlue)
    hist1.SetLineWidth(2)
    hist2.SetLineColor(ROOT.kOrange)
    hist2.SetLineWidth(2)
    hist3.SetLineColor(ROOT.kRed)
    hist3.SetLineWidth(2)

    hist1.SetStats(0)
    hist2.SetStats(0)
    hist3.SetStats(0)

    c1 = ROOT.TCanvas("c1", "Reference Point Weight", 800, 600)
    c1.SetGrid()

    hist1.Draw("HIST")
    hist2.Draw("HIST SAME")
    hist3.Draw("HIST SAME")

    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.AddEntry(hist1, "Mtt 0-700", "l")
    legend.AddEntry(hist2, "Mtt 700-900", "l")
    legend.AddEntry(hist3, "Mtt 900-Inf", "l")
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()

    hist1.GetXaxis().SetTitle("Mttbar [GeV]")
    hist1.GetYaxis().SetTitle("Normalized Events")
    hist1.SetTitle("Reference Point Weight")

    max_y = max(hist1.GetMaximum(), hist2.GetMaximum(), hist3.GetMaximum())
    hist1.SetMaximum(max_y * 1.2)

    c1.SaveAs("hist_mttbar_normalized_crosssection.png")

    # Close files
    file1.Close()
    file2.Close()
    file3.Close()

if __name__ == "__main__":
    overlay_histograms_normalized()
