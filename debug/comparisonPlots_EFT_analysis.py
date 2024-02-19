import ROOT

ROOT.gROOT.SetBatch(True)

file = ROOT.TFile.Open('/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFTvsUL/output_DNN/UL18/muon/workdir_Analysis_muon_madgraphEFT/uhh2.AnalysisModuleRunner.MC.EFT_sample_UL18_0.root', 'READ')
# file = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFTvsUL/output_UL/UL18/muon/workdir_Analysis_muon_powheg/TTbar.root", 'READ')

met_directory = file.Get("TTbarCandidate_General")

if met_directory:
    print("TTbarCandidate directory is found")
else:
    print("TTbarCandidate directory is not found")

hist_names = {
    "N_jets":          ("N_jets", "N_{jets}", 21, -0.5, 20.5),
    "pt_jet1":         ("pt_jet1", "p_{T}^{jet 1} [GeV]", 50, 0, 1500),
    "pt_jet2":         ("pt_jet2", "p_{T}^{jet 2} [GeV]", 50, 0, 1500),
    "eta_jet1":        ("eta_jet1", "#eta^{jet 1}", 50, -2.5, 2.5),
    "eta_jet2":        ("eta_jet2", "#eta^{jet 2}", 50, -2.5, 2.5),
    "pt_mu":           ("pt_mu", "p_{T}^{#mu} [GeV]", 50, 0, 1500),
    "eta_mu":          ("eta_mu", "#eta^{#mu}", 50, -2.5, 2.5),
    "pt_ele":          ("pt_ele", "p_{T}^{e} [GeV]", 50, 0, 1500),
    "eta_ele":         ("eta_ele", "#eta^{e}", 50, -2.5, 2.5),
    "pt_AK8Puppijet":  ("pt_AK8Puppijet", "p_{T}^{AK8Puppi jets} [GeV]", 50, 0, 1500),
    "toplep_pt":       ("toplep_pt", "p_{T}^{t,lep} [GeV]", 70, 0, 7000),
    "toplep_eta":      ("toplep_eta", "#eta^{t,lep}", 60, -3.0, 3.0),
    "tophad_pt":       ("tophad_pt", "p_{T}^{t,had} [GeV]", 70, 0, 7000),
    "tophad_eta":      ("tophad_eta", "#eta^{t,had}", 60, -3.0, 3.0),
    "MET":             ("MET", "missing E_{T} [GeV]", 50, 0, 7000),
    "topgen_pt":       ("topgen_pt", "p_{T}^{top} [GeV] in gen",70, 0, 7000),
    "topgen_eta":      ("antitopgen_eta", "#eta^{top} in gen",60, -3.0, 3.0),
    "antitopgen_pt":   ("topgen_pt", "p_{antiT}^{top} [GeV] in gen",70, 0, 7000),
    "antitopgen_eta":  ("antitopgen_eta", "#eta^{antiT}",60, -3.0, 3.0),
    "leptongen_pt":    ("leptongen_pt", "p_{T}^{lepton} [GeV] in gen",70, 0, 7000),
    "leptongen_eta":   ("leptongen_eta", "#eta^{lepton} in gen",60, -3.0, 3.0),
    "muongen_pt":      ("muongen_pt", "p_{T}^{muon} [GeV] in gen",70, 0, 7000),
    "muongen_eta":     ("muongen_eta", "#eta^{muon} in gen"      ,60, -3.0, 3.0),
    "electrongen_pt":  ("electrongen_pt", "p_{T}^{electron} [GeV] in gen",70, 0, 7000),
    "electrongen_eta": ("electrongen_eta", "#eta^{electron} in gen",60, -3.0, 3.0),
    "bquarkgen_pt":    ("bquarkgen_pt", "p_{bquark} [GeV] in gen",70, 0, 7000),
    "bquarkgen_eta":   ("bquarkgen_eta", "#eta^{bquark} in gen",60, -3.0, 3.0),
    "ditop_mass":      ("ditop_mass", "m_{t#bar{t}} [GeV]", 70, 0, 7000),
    "pt_AK8PuppiTaggedjet":("pt_AK8PuppiTaggedjet", "p_{T}^{AK8Puppi Tagged jets} [GeV]", 45, 0, 900),
    "N_mu":            ("N_mu", "N^{#mu}", 11, -0.5, 10.5),
    "N_ele":           ("N_ele", "N^{e}", 11, -0.5, 10.5),


}


for hist_name, hist_def in (hist_names).items():
    hist = met_directory.Get(hist_name)
    
    if not hist:
        print(hist_name, "is not found")
    
    if hist:
        print("working on:", hist_name)
        if hist.Integral() > 0:
            hist.Scale(1.0 / hist.Integral())

        hist.GetXaxis().SetTitle(hist_def[1])  # Set the X-axis title
        hist.GetXaxis().SetRangeUser(hist_def[3], hist_def[4])  # Set the X-axis range
        
        canvas = ROOT.TCanvas('canvas_' + hist_name, hist_name, 800, 600)
        hist.Draw('HIST')
    
        canvas.SaveAs(hist_name + 'madgraph.pdf')

file.Close()

