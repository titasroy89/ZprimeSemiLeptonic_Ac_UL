import ROOT

output_file = ROOT.TFile.Open("mttbar_multiprocess_0_700.root")

hist_lastcopy = output_file.Get("hist_mttbar_lastcopy")
hist_reconstructed = output_file.Get("hist_mttbar_reconstructed")

canvas = ROOT.TCanvas("canvas", "Invariant Mass Comparison", 800, 600)

hist_lastcopy.SetLineColor(ROOT.kBlue)
hist_reconstructed.SetLineColor(ROOT.kRed)

hist_lastcopy.Draw("HIST")
hist_reconstructed.Draw("HIST SAME")

legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(hist_lastcopy, "Last Copy Method", "l")
legend.AddEntry(hist_reconstructed, "Reconstructed Method", "l")
legend.Draw()

canvas.SaveAs("mttbar_comparison.png")

output_file.Close()
