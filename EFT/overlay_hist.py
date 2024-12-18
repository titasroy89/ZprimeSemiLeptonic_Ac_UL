import ROOT

def overlay_histograms():
    file1 = ROOT.TFile.Open("samples/0_700/mttbar_multiprocess_0_700.root")
    if not file1 or file1.IsZombie():
        print("Error opening file0_700.root")
        return

    file2 = ROOT.TFile.Open("samples/700_900/mttbar_multiprocess_700_900.root")
    if not file2 or file2.IsZombie():
        print("Error opening file700_900.root")
        return

    hist1 = file1.Get("hist_mttbar_reconstructed")
    hist2 = file2.Get("hist_mttbar_reconstructed")

    if not hist1 or not hist2:
        print("Error retrieving histograms")
        return

    hist1.SetLineColor(ROOT.kBlue)
    hist1.SetLineWidth(2)
    hist2.SetLineColor(ROOT.kRed)
    hist2.SetLineWidth(2)

    c1 = ROOT.TCanvas("c1", "Reference Point Weight", 800, 600)
    c1.SetGrid()

    hist1.Draw("HIST")
    hist2.Draw("HIST SAME")

    legend = ROOT.TLegend(0.7,0.7,0.9,0.9)
    legend.AddEntry(hist1, "Mtt 0-700", "l")
    legend.AddEntry(hist2, "Mtt 700-900", "l")
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()

    hist1.GetXaxis().SetTitle("Mtt [GeV] (gen particles)")
    hist1.GetYaxis().SetTitle("Events")
    hist1.SetTitle("Reference Point Weight")

    max1 = hist1.GetMaximum()
    max2 = hist2.GetMaximum()
    ymax = max(max1, max2) * 1.2  
    hist1.SetMaximum(ymax)

    c1.SaveAs("Mtt_overlay.png")


if __name__ == "__main__":
    overlay_histograms()
