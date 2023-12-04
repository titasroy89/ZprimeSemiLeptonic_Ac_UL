import ROOT
import os

ROOT.gROOT.SetBatch(True)
ROOT.ROOT.EnableImplicitMT()

chain = ROOT.TChain("AnalysisTree")
chain.Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_gen_validation/UL18/workdir_UL18_preselection_genvalidation/*.root")

df = ROOT.RDataFrame(chain)

canvas = ROOT.TCanvas("c1", "Canvas", 800, 600)

variables = {
    "lepton_pt": {"bins": (1000, 0, 1000), "title": "Lepton pT Distribution"},
    "lepton_eta": {"bins": (100, -5, 5), "title": "Lepton Eta Distribution"},
    "lepton_phi": {"bins": (100, -ROOT.TMath.Pi(), ROOT.TMath.Pi()), "title": "Lepton Azimuthal Angle Distribution"},
    "topMultiplicity": {"bins": (4, 0, 4),  "title": "Top Multiplicity Distribution" },
    "MET":  {"bins": (100, 0, 200),  "title": "MET Distribution"},
    "angle_top_antitop":  {"bins": (50, 0, ROOT.TMath.Pi()),  "title": "Angle between top and antitop" },
    "ttbar_mass": {"bins": (1000, 0, 7000),  "title": "Invariant Mass Distribution" },
    "ele_pt":  {"bins": (1000, 0, 200),  "title": "Electron pT Distribution" },
    "muon_pt":  {"bins": (1000, 0, 200),  "title": "Muon pT Distribution" },
    "bquark_pt": {"bins": (1000, 0, 1000), "title": "b-quark pT Distribution" },
    "bquark_eta": {"bins": (100, -5, 5), "title": "b-quark Eta Distribution" },
    "tops_pt":  {"bins": (100, 0, 3000), "title": "Top Quark pT Distribution, abs(pdgId)=6" },
    "top_pt":  {"bins": (100, 0, 3000),  "title":"Top Quark pT Distribution, pdgId=6"},
    "antitop_pt":  {"bins": (100, 0, 3000),  "title": "Anti-Top Quark pT Distribution" },
    "motherPdgId": {"bins": (27, -6, 22),  "title": "PDG ID of Top's Mother"},
    "leptonFlavor": {"bins": (5, -2, 3), "title": "Lepton Flavor Distribution"}
}

logY_variables = ["MET", "ttbar_mass", "topMultiplicity", "motherPdgId", "lepton_pt", "electron_pt","muon_pt", "bquark_pt", "tops_pt", "top_pt", "antitop_pt"] 
    
for var, settings in variables.items():
    hist_name = "hist_" + var
    hist_title = settings["title"] + "; Value; Events"
    bins = settings["bins"]

    hist = df.Histo1D((hist_name, hist_title, bins[0], bins[1], bins[2]), var)

    if var in logY_variables:
        canvas.SetLogy(1)  
    else:
        canvas.SetLogy(0) 
        
    hist.Draw()
    canvas.SaveAs("{}.png".format(var))
    
    
    