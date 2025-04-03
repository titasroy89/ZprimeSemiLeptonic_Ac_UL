import ROOT

ROOT.gROOT.SetBatch(True)

# file = ROOT.TFile.Open('/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFTvsUL/output_EFT/Preselection/workdir_EFT_madgraph_HT800/uhh2.AnalysisModuleRunner.MC.EFT_sample_UL18_0.root', 'READ')
file = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFTvsUL/output_UL/Preselection/workdir_Preselection_UL18_powheg_HT800/TTbar.root", 'READ')
met_directory = file.Get("MET_General")

if met_directory:
    print("met directory is found")
else:
    print("met directory is not found")

hist_names = {
    "N_jets":          ("N_jets", "N_{jets}", 21, -0.5, 20.5),
    "pt_jet1":         ("pt_jet1", "p_{T}^{jet 1} [GeV]", 50, 0, 2000),
    "pt_jet2":         ("pt_jet2", "p_{T}^{jet 2} [GeV]", 50, 0, 2000),
    "eta_jet1":        ("eta_jet1", "#eta^{jet 1}", 50, -2.5, 2.5),
    "eta_jet2":        ("eta_jet2", "#eta^{jet 2}", 50, -2.5, 2.5),
    "pt_mu":           ("pt_mu", "p_{T}^{#mu} [GeV]", 50, 0, 2000),
    "eta_mu":          ("eta_mu", "#eta^{#mu}", 50, -2.5, 2.5),
    "pt_ele":          ("pt_ele", "p_{T}^{e} [GeV]", 50, 0, 2000),
    "eta_ele":         ("eta_ele", "#eta^{e}", 50, -2.5, 2.5),
    "MET":             ("MET", "missing E_{T} [GeV]", 50, 0, 3000),
    "topgen_pt":       ("topgen_pt", "p_{T}^{top} [GeV] in gen",70, 0, 3000),
    "topgen_eta":      ("topgen_eta", "#eta^{top} in gen",60, -2.5, 2.5),
    "antitopgen_pt":   ("antitopgen_pt", "p_{antiT}^{top} [GeV] in gen",70, 0, 3000),
    "antitopgen_eta":  ("antitopgen_eta", "#eta^{antiT}",60, -2.5, 2.5),
    "leptongen_pt":    ("leptongen_pt", "p_{T}^{lepton} [GeV] in gen",70, 0, 3000),
    "leptongen_eta":   ("leptongen_eta", "#eta^{lepton} in gen",60, -2.5, 2.5),
    "muongen_pt":      ("muongen_pt", "p_{T}^{muon} [GeV] in gen",70, 0, 3000),
    "muongen_eta":     ("muongen_eta", "#eta^{muon} in gen"      ,60, -2.5, 2.5),
    "electrongen_pt":  ("electrongen_pt", "p_{T}^{electron} [GeV] in gen",70, 0, 3000),
    "electrongen_eta": ("electrongen_eta", "#eta^{electron} in gen",60, -2.5, 2.5),
    "bquarkgen_pt":    ("bquarkgen_pt", "p_{bquark} [GeV] in gen",70, 0, 3000),
    "bquarkgen_eta":   ("bquarkgen_eta", "#eta^{bquark} in gen",60, -2.5, 2.5),
    "mttbar":          ("mttbar", "m_{t#bar{t}} [GeV]", 100, 0, 7000),
    "N_mu":            ("N_mu", "N^{#mu}", 11, -0.5, 10.5),
    "N_ele":           ("N_ele", "N^{e}", 11, -0.5, 10.5),
    "leadingJetPtHist": ("leadingJetPtHist", "p_{leading jet} [GeV] in gen",1000, 0, 3000),
    "genHT_dist":       ("genHT_dist", "HT_{sum of gen jet pt} [GeV]",1000, 0, 3000)


}


for hist_name, hist_def in (hist_names).items():
    hist = met_directory.Get(hist_name)
    
    if not hist:
        print(hist_name, "is not found")
    
    if hist:
        print("working on:", hist_name)
        if hist.Integral() > 0:
            hist.Scale(1.0 / hist.Integral())
        
        canvas = ROOT.TCanvas('canvas_' + hist_name, hist_name, 800, 600)
        hist.Draw('HIST')
    
        canvas.SaveAs(hist_name + 'powheg.pdf')

file.Close()

