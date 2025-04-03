import ROOT

ROOT.gROOT.SetBatch(True)

file1 = ROOT.TFile.Open('/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFTvsUL/output_EFT/Preselection/workdir_EFT_madgraph_HT800/uhh2.AnalysisModuleRunner.MC.EFT_sample_UL18_0.root', 'READ')
file2 = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFTvsUL/output_UL/Preselection/workdir_Preselection_UL18_powheg_HT800/TTbar.root", 'READ')


folder1 = file1.Get("MET_General")
folder2 = file2.Get("MET_General")

histograms = {
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

for histogram_name, hist_def in (histograms).items():
    hist1 = folder1.Get(histogram_name)
    hist2 = folder2.Get(histogram_name)
    
    c = ROOT.TCanvas("c", "Overlay Histograms: " + histogram_name, 800, 600)

    if hist1 and hist2:
        if hist1.Integral() > 0:
            hist1.Scale(1.0 / hist1.Integral())
        
        if hist2.Integral() > 0:
            hist2.Scale(1.0 / hist2.Integral())
            
        max_y_value = max(hist1.GetMaximum(), hist2.GetMaximum())
        
        hist1.SetLineColor(2)
        hist2.SetLineColor(4)  
        
        hist1.SetMaximum(max_y_value * 1.2)
        
        hist1.Draw('HIST')
        hist2.Draw("HISTSAME")

        legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
        legend.AddEntry(hist1, "Madgraph EFT")
        legend.AddEntry(hist2, "Powheg")
        legend.Draw()

        c.Update()

        c.SaveAs("overlay_" + histogram_name + ".png")
    
    else:
        print("Histogram not found:", histogram_name)
        

file1.Close()
file2.Close()
