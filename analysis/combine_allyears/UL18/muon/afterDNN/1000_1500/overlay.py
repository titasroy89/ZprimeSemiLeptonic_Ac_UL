import ROOT

ROOT.gROOT.SetBatch(True)

file = ROOT.TFile("dY_UL18_muon_1000_1500.root", "READ")

hist1 = file.Get("WJets")
hist2 = file.Get("WJets_pdfUp")
hist3 = file.Get("WJets_pdfDown")

canvas = ROOT.TCanvas("canvas", "Overlay Histograms", 800, 600)

hist1.SetLineColor(ROOT.kRed)
hist2.SetLineColor(ROOT.kBlue)
hist3.SetLineColor(ROOT.kGreen)

hist1.Draw("HIST")
hist2.Draw("HISTSAME")
hist3.Draw("HISTSAME")

legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(hist1, "Nominal", "f")
legend.AddEntry(hist2, "PDF Up", "f")
legend.AddEntry(hist3, "PDF Down", "f")
legend.Draw()

canvas.Draw()
canvas.SaveAs("overlay_histograms.pdf")

file.Close()
