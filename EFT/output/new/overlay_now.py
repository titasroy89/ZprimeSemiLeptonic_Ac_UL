import ROOT

def overlay_histograms_normalized():
    file1 = ROOT.TFile.Open("mttbar_multiprocess_0_700_1_new.root")
    file2 = ROOT.TFile.Open("mttbar_multiprocess_700_900.root")
    file3 = ROOT.TFile.Open("mttbar_multiprocess_900Inf.root")
# hist_mttbar_reconstructed
# hist_mttbar_total
    hist1 = file1.Get("hist_njets_total")
    hist2 = file2.Get("hist_njets_total")
    hist3 = file3.Get("hist_njets_total")

    print("Integral before scaling (hist1):", hist1.Integral("width"))
    print("Integral before scaling (hist2):", hist2.Integral("width"))
    print("Integral before scaling (hist3):", hist3.Integral("width"))

    integral1 = hist1.Integral("width")
    if integral1 != 0:
        hist1.Scale(1.0 / integral1)
    else:
        print("Histogram1 has zero integral, cannot normalize.")

    integral2 = hist2.Integral("width")
    if integral2 != 0:
        hist2.Scale(1.0 / integral2)
    else:
        print("Histogram2 has zero integral, cannot normalize.")

    integral3 = hist3.Integral("width")
    if integral3 != 0:
        hist3.Scale(1.0 / integral3)
    else:
        print("Histogram3 has zero integral, cannot normalize.")


    print("Integral after scaling (hist1):", hist1.Integral("width"))
    print("Integral after scaling (hist2):", hist2.Integral("width"))
    print("Integral after scaling (hist3):", hist3.Integral("width"))

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

    c1.SaveAs("hist_mttbar_total_all.png")

    file1.Close()
    file2.Close()
    file3.Close()

if __name__ == "__main__":
    overlay_histograms_normalized()

