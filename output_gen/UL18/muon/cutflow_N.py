import ROOT

# Open the ROOT file and access the TTree
file = ROOT.TFile.Open("Semi.root")
tree = file.Get("AnalysisTree")

# Create histograms for each branch
hist1 = ROOT.TH1F("hist1", "DeltaY_N_gen_muon", 1, -2, 2)
hist2 = ROOT.TH1F("hist2", "DeltaY_N_gen_pt_muon", 1, -2, 2)
hist3 = ROOT.TH1F("hist3", "DeltaY_N_gen_eta_muon", 1, -2, 2)
hist4 = ROOT.TH1F("hist4", "DeltaY_N_gen_jet_pt_muon", 1, -2, 2)
hist5 = ROOT.TH1F("hist5", "DeltaY_N_gen_jet_eta_muon", 1, -2, 2)



# Fill the histograms
for i, event in enumerate(tree):
    # Load the current tree entry
    hist1.Fill(event.DeltaY_N_gen_muon)
    hist2.Fill(event.DeltaY_N_gen_pt_muon)
    hist3.Fill(event.DeltaY_N_gen_eta_muon)
    hist4.Fill(event.DeltaY_N_gen_jet_pt_muon)
    hist5.Fill(event.DeltaY_N_gen_jet_eta_muon)
    # hist1.Fill(event.DeltaY_N_gen_muon)
    # hist4.Fill(event.DeltaY_N_gen_jet_pt_muon)
    # hist5.Fill(event.DeltaY_N_gen_jet_eta_muon)
    # hist2.Fill(event.DeltaY_N_gen_pt_muon)
    # hist3.Fill(event.DeltaY_N_gen_eta_muon)
    

        
    if i % 10000 == 0 and i > 0: 
        print("Processing entry {}/{}".format(i, tree.GetEntries()))

print("UL18 muon -> Number of events without cuts: {}".format(hist1.Integral()))
print("UL18 muon -> Number of events with lepton_pt cut: {}".format(hist2.Integral()))
print("UL18 muon -> Number of events with lepton_pt & eta cut : {}".format(hist3.Integral()))
print("UL18 muon -> Number of events with lepton_pt eta & jet pt cut : {}".format(hist4.Integral()))
print("UL18 muon -> Number of events with lepton_pt eta & jet pt eta cut : {}".format(hist5.Integral()))

# print("UL18 muon -> Number of events without cuts: {}".format(hist1.Integral()))
# print("UL18 muon -> Number of events with lepton_pt eta & jet pt cut : {}".format(hist4.Integral()))
# print("UL18 muon -> Number of events with lepton_pt eta & jet pt eta cut : {}".format(hist5.Integral()))
# print("UL18 muon -> Number of events with lepton_pt cut: {}".format(hist2.Integral()))
# print("UL18 muon -> Number of events with lepton_pt & eta cut : {}".format(hist3.Integral()))

        
# Create a new histogram with 3 bins
cutflow = ROOT.TH1F("cutflow", "UL18 muon DeltaY < 0", 5, 0, 5)
cutflow.GetXaxis().SetBinLabel(1, "All")
cutflow.GetXaxis().SetBinLabel(2, "Lepton Pt")
cutflow.GetXaxis().SetBinLabel(3, "Lepton Pt&Eta")
cutflow.GetXaxis().SetBinLabel(4, "Lepton Pt&Eta and Jet Pt")
cutflow.GetXaxis().SetBinLabel(5, "Lepton Pt&Eta and Jet Pt&Eta")

# cutflow.GetXaxis().SetBinLabel(1, "All")
# cutflow.GetXaxis().SetBinLabel(4, "Jet Pt")
# cutflow.GetXaxis().SetBinLabel(5, "Jet Pt&Eta")
# cutflow.GetXaxis().SetBinLabel(2, "Lepton Pt")
# cutflow.GetXaxis().SetBinLabel(3, "Lepton Pt&Eta")


# Fill the new histogram with the integral of each branch histogram
cutflow.SetBinContent(1, hist1.Integral())
cutflow.SetBinContent(2, hist2.Integral())
cutflow.SetBinContent(3, hist3.Integral())
cutflow.SetBinContent(4, hist4.Integral())
cutflow.SetBinContent(5, hist5.Integral())

# cutflow.SetBinContent(1, hist1.Integral())
# cutflow.SetBinContent(4, hist4.Integral())
# cutflow.SetBinContent(5, hist5.Integral())
# cutflow.SetBinContent(2, hist2.Integral())
# cutflow.SetBinContent(3, hist3.Integral())



# Draw the new histogram
canvas = ROOT.TCanvas("canvas", "UL18 muon DeltaY < 0", 800, 600)
cutflow.Draw()

canvas.Draw()
canvas.SaveAs("DeltaY_N_gen_muon_prese_thistime.png")



