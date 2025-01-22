import ROOT

ROOT.gROOT.SetBatch(True)


root_file = "/nfs/dust/cms/user/titasroy/Ac_UL_ntuples/2018/muon/workdir_AnalysisDNN_2018_muon/NOMINAL/uhh2.AnalysisModuleRunner.MC.ST.root"  
variable_name = "DeltaY_reco_d1"
nominal_folder = "DeltaY_reco_500_750_SR_General" 
syst_folder = "DeltaY_reco_SystVariations_500_750_SR" 

def draw_histogram_with_variations(root_file, variable_name, systematic, nominal_folder, syst_folder):
    file = ROOT.TFile(root_file, "READ")
    print(variable_name, syst)
    up_name = "%s_%s_up"%(variable_name,syst)
    down_name = "%s_%s_down"%(variable_name,syst)
    
    h_nominal = file.Get("%s/%s"%(nominal_folder,variable_name))
    h_up = file.Get("%s/%s"%(syst_folder,up_name))
    h_down = file.Get("%s/%s"%(syst_folder,down_name))
    
    if not h_nominal or not h_up or not h_down:
        print("Error: Histogram for %s not found in file!"%(syst))
        return
    
    canvas_title = "%s Variations"%(syst)
    c = ROOT.TCanvas("c", canvas_title, 800, 600)
    
    h_nominal.SetLineColor(ROOT.kBlack)  
    h_up.SetLineColor(ROOT.kRed)         
    h_down.SetLineColor(ROOT.kBlue)      
    
    h_nominal.SetTitle("%s Variations"%(syst))
    h_nominal.GetXaxis().SetTitle("%s"%(syst))
    h_nominal.GetYaxis().SetTitle("Entries")
    h_up.Draw("hist")
    h_nominal.Draw("hist,same")  
    # h_up.Draw("hist same") 
    h_down.Draw("hist same") 
    
    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.AddEntry(h_nominal, "Nominal", "l")
    legend.AddEntry(h_up, "Up Variation", "l")
    legend.AddEntry(h_down, "Down Variation", "l")
    legend.Draw()
    c.SetLogy(1)
    output_file = "syst_plots/%s_variations_ST_%s.png"%(syst,variable_name)
    c.SaveAs(output_file)
    
    file.Close()

systematics = [
    "pu", "prefiring", "mu_id_stat", "mu_id_syst", "mu_iso_stat", "mu_iso_syst",
    "mu_trigger_stat", "mu_trigger_syst", "ele_id", "ele_trigger", "ele_reco",
    "murmuf_upup", "murmuf_upnone", "murmuf_noneup", "murmuf_nonedown",
    "murmuf_downnone", "murmuf_downdown", "isr", "fsr", "btag_cferr1", "btag_cferr2", 
    "btag_hf", "btag_hfstats1", "btag_hfstats2", "btag_lf", "btag_lfstats1", 
    "btag_lfstats2", "ttag_corr", "ttag_uncorr", "tmistag", "isr", "fsr"
]


for syst in systematics:
    draw_histogram_with_variations(root_file, variable_name, syst, nominal_folder, syst_folder)
