import ROOT

# Open the ROOT file and access the TTree
file = ROOT.TFile.Open("TTbar_all.root")

dirs = ["Gen_N_General", "Ele_gen_N_900Inf_General","Ele_N_Pt_900Inf_General", "Ele_N_Pt_Eta_900Inf_General", "Ele_N_JetPt_900Inf_General", "Ele_N_JetPt_Eta_900Inf_General"]


# Create histograms for each branch
hist1 = ROOT.TH1F("hist1", "DeltaY_N_gen_ele", 1, -2, 2)
hist2 = ROOT.TH1F("hist2", "DeltaY_N_gen_ele_mass", 1, -2, 2)
hist3 = ROOT.TH1F("hist2", "DeltaY_N_gen_ele_pt", 1, -2, 2)
hist4 = ROOT.TH1F("hist3", "DeltaY_N_gen_ele_pt_eta", 1, -2, 2)
hist5 = ROOT.TH1F("hist4", "DeltaY_N_gen_ele_jetpt", 1, -2, 2)
hist6 = ROOT.TH1F("hist5", "DeltaY_N_gen_ele_jetpteta", 1, -2, 2)

hists = [hist1, hist2, hist3, hist4, hist5, hist6]

# Iterate over specified directories
for i, dir_name in enumerate(dirs):
    # Get the directory
    dir = file.Get(dir_name)

    if dir == None or not dir.InheritsFrom('TDirectory'):
        print("Directory {0} does not exist or is not a TDirectory".format(dir_name))
        continue
    
    # Get the histogram from the directory
    hist = dir.Get("DeltaY_N_ele")

    # Fill the corresponding histogram
    for j, bin in enumerate(range(1, hist.GetNbinsX()+1)):
        hists[i].Fill(hist.GetBinCenter(bin), hist.GetBinContent(bin))

        if j % 10000 == 0 and j > 0: 
            print("Processing bin {0} in directory {1}".format(j, dir_name))

    print("Processed directory {0}".format(dir_name))

print("UL18 Electron -> Number of events without cuts: {}".format(hist1.Integral()))
print("UL18 Electron -> Number of events with 900Inf mass cut: {}".format(hist2.Integral()))
print("UL18 Electron -> Number of events with lepton_pt cut: {}".format(hist3.Integral()))
print("UL18 Electron -> Number of events with lepton_pt & eta cut : {}".format(hist4.Integral()))
print("UL18 Electron -> Number of events with lepton_pt eta & jet pt cut : {}".format(hist5.Integral()))
print("UL18 Electron -> Number of events with lepton_pt eta & jet pt eta cut : {}".format(hist6.Integral()))

        
# Create a new histogram with 3 bins
cutflow = ROOT.TH1F("cutflow", "UL18 Ele DeltaY < 0, 900<Mtt", 6, 0, 6)
cutflow.GetXaxis().SetBinLabel(1, "All")
cutflow.GetXaxis().SetBinLabel(2, "Mass Cut")
cutflow.GetXaxis().SetBinLabel(3, "Lepton Pt")
cutflow.GetXaxis().SetBinLabel(4, "Lepton Pt&Eta")
cutflow.GetXaxis().SetBinLabel(5, "Lepton Pt&Eta and Jet Pt")
cutflow.GetXaxis().SetBinLabel(6, "Lepton Pt&Eta and Jet Pt&Eta")


# Fill the new histogram with the integral of each branch histogram
cutflow.SetBinContent(1, hist1.Integral())
cutflow.SetBinContent(2, hist2.Integral())
cutflow.SetBinContent(3, hist3.Integral())
cutflow.SetBinContent(4, hist4.Integral())
cutflow.SetBinContent(5, hist5.Integral())
cutflow.SetBinContent(6, hist6.Integral())

# Draw the new histogram
canvas = ROOT.TCanvas("canvas", "UL18 Ele DeltaY < 0, 900<Mtt", 800, 600)
cutflow.Draw()

canvas.Draw()
canvas.SaveAs("DeltaY_N_gen_ele_900Inf.png")



