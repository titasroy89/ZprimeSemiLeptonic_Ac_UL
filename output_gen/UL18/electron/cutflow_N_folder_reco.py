import ROOT

# Open the ROOT file and access the TTree
file = ROOT.TFile.Open("Semileptonic_folder_reco.root")

dirs = ["DeltaY_reco_N_electron_General", "Ele1_Tot_General", "TriggerEle_General", "TwoDCut_Ele_General", "Jet1_General", "MET_General", "Btags1_General", "Chi2_General" ]


# Create histograms for each branch
hist1 = ROOT.TH1F("hist1", "DeltaY_N_gen_electron", 1, -2, 2)
hist2 = ROOT.TH1F("hist2", "DeltaY_N_gen_electron_pteta", 1, -2, 2)
hist3 = ROOT.TH1F("hist3", "DeltaY_N_gen_electron_trigger", 1, -2, 2)
hist4 = ROOT.TH1F("hist4", "DeltaY_N_gen_electron_twod", 1, -2, 2)
hist5 = ROOT.TH1F("hist5", "DeltaY_N_gen_electron_jetpteta", 1, -2, 2)
hist6 = ROOT.TH1F("hist6", "DeltaY_N_gen_electron_met", 1, -2, 2)
hist7 = ROOT.TH1F("hist7", "DeltaY_N_gen_electron_btag", 1, -2, 2)
hist8 = ROOT.TH1F("hist8", "DeltaY_N_gen_electron_chi2", 1, -2, 2)

hists = [hist1, hist2, hist3, hist4, hist5, hist6, hist7, hist8]

# Iterate over specified directories
for i, dir_name in enumerate(dirs):
    # Get the directory
    dir = file.Get(dir_name)

    # Get the histogram from the directory
    hist = dir.Get("DeltaY_N_ele")

    # Fill the corresponding histogram
    for j, bin in enumerate(range(1, hist.GetNbinsX()+1)):
        hists[i].Fill(hist.GetBinCenter(bin), hist.GetBinContent(bin))

        if j % 10000 == 0 and j > 0: 
            print("Processing bin {0} in directory {1}".format(j, dir_name))

    print("Processed directory {0}".format(dir_name))

print("UL18 electron -> Number of events without cuts: {}".format(hist1.Integral()))
print("UL18 electron -> Number of events with lepton pt & eta cut: {}".format(hist2.Integral()))
print("UL18 electron -> Number of events with electron trigger : {}".format(hist3.Integral()))
print("UL18 electron -> Number of events with 2D cut : {}".format(hist4.Integral()))
print("UL18 electron -> Number of events with jet pt & eta cut : {}".format(hist5.Integral()))
print("UL18 electron -> Number of events with met cut : {}".format(hist6.Integral()))
print("UL18 electron -> Number of events with btag : {}".format(hist7.Integral()))
print("UL18 electron -> Number of events with chi2 cut : {}".format(hist8.Integral()))

        
# Create a new histogram with 3 bins
cutflow = ROOT.TH1F("cutflow", "UL18 electron DeltaY < 0", 8, 0, 8)
cutflow.GetXaxis().SetBinLabel(1, "All")
cutflow.GetXaxis().SetBinLabel(2, "Lepton Pt&Eta")
cutflow.GetXaxis().SetBinLabel(3, "electron Trigger")
cutflow.GetXaxis().SetBinLabel(4, "2D")
cutflow.GetXaxis().SetBinLabel(5, "Jet Pt&Eta")
cutflow.GetXaxis().SetBinLabel(6, "MET")
cutflow.GetXaxis().SetBinLabel(7, "Btag")
cutflow.GetXaxis().SetBinLabel(8, "Chi2")


# Fill the new histogram with the integral of each branch histogram
cutflow.SetBinContent(1, hist1.Integral())
cutflow.SetBinContent(2, hist2.Integral())
cutflow.SetBinContent(3, hist3.Integral())
cutflow.SetBinContent(4, hist4.Integral())
cutflow.SetBinContent(5, hist5.Integral())
cutflow.SetBinContent(6, hist6.Integral())
cutflow.SetBinContent(7, hist7.Integral())
cutflow.SetBinContent(8, hist8.Integral())

# Draw the new histogram
canvas = ROOT.TCanvas("canvas", "UL18 electron DeltaY < 0", 800, 600)
cutflow.Draw()

canvas.Draw()
canvas.SaveAs("DeltaY_N_electron_reco.png")



