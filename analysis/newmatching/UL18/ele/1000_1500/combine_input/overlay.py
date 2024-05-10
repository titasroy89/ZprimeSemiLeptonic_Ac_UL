import ROOT

ROOT.gROOT.SetBatch(True)

file = ROOT.TFile("dY_UL18_muon_0_500.root", "READ")

hist1 = file.Get("CR2/TTbar_1_murmufUp")
hist2 = file.Get("CR2/TTbar_1_murmufDown")
hist3 = file.Get("CR2/TTbar_1")


hist1.SetLineColor(ROOT.kBlue)
hist1.SetLineWidth(2)
hist2.SetLineColor(ROOT.kRed)
hist2.SetLineWidth(2)
hist3.SetLineColor(ROOT.kOrange)
hist3.SetLineWidth(2)

canvas = ROOT.TCanvas("canvas", "Overlayed Histograms", 800, 600)

hist1.Draw("HIST")
hist2.Draw("HIST SAME")
hist3.Draw("HIST SAME")

legend = ROOT.TLegend(0.7, 0.8, 0.9, 0.9)
legend.AddEntry(hist1, "CR2_TTbar_1_murmufUp", "l")
legend.AddEntry(hist2, "CR2_TTbar_1_murmufDown", "l")
legend.AddEntry(hist3, "CR2_TTbar_1", "l")
legend.Draw()

canvas.Update()

canvas.SaveAs("CR2_TTbar_1.png")

file.Close()
