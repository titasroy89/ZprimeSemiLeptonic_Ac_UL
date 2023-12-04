import ROOT
from ROOT import TCanvas, TFile, gStyle

file = TFile ("dY_UL18_muon_750_900.root")

canvas = TCanvas("c", "c", 800, 600)

weight_pu = file.Get("TTbar_1")
weight_pu_up = file.Get("TTbar_1_muonTriggerUp")
weight_pu_down = file.Get("TTbar_1_muonTriggerDown")

# weight_pu = ROOT.TH1F("weight_pu", "", weight_pu_orig.GetNbinsX(), weight_pu_orig.GetXaxis().GetXmin(), weight_pu_orig.GetXaxis().GetXmax())
# weight_pu_up = ROOT.TH1F("weight_pu_up", "", weight_pu_up_orig.GetNbinsX(), weight_pu_up_orig.GetXaxis().GetXmin(), weight_pu_up_orig.GetXaxis().GetXmax())
# weight_pu_down = ROOT.TH1F("weight_pu_down", "", weight_pu_down_orig.GetNbinsX(), weight_pu_down_orig.GetXaxis().GetXmin(), weight_pu_down_orig.GetXaxis().GetXmax())

# # Copy the bin content but not the errors
# for bin in range(1, weight_pu.GetNbinsX()+1):
#     weight_pu.SetBinContent(bin, weight_pu_orig.GetBinContent(bin))
#     weight_pu_up.SetBinContent(bin, weight_pu_up_orig.GetBinContent(bin))
#     weight_pu_down.SetBinContent(bin, weight_pu_down_orig.GetBinContent(bin))
    
weight_pu.SetLineColor(1)  # Black
weight_pu_up.SetLineColor(2)  # Red
weight_pu_down.SetLineColor(4)  # Blue
weight_pu.Draw()
weight_pu_up.Draw("SAME")
weight_pu_down.Draw("SAME")

# weight_pu.GetXaxis().SetTitle("")
# weight_pu.GetYaxis().SetTitle("Y-axis")

legend = ROOT.TLegend(0.7,0.7,0.9,0.9)
legend.AddEntry(weight_pu,"nominal","l")
legend.AddEntry(weight_pu_up,"up","l")
legend.AddEntry(weight_pu_down,"down","l")
legend.Draw()

canvas.SaveAs("muonreco2.png")
