import ROOT
import os

ROOT.gROOT.SetBatch(True)

def variations(root_file, variable_name, systematic, nominal_folder, syst_folder, output_dir):
    file = ROOT.TFile(root_file, "READ")
    
    up_name = f"{variable_name}_{systematic}_up"
    down_name = f"{variable_name}_{systematic}_down"
    
    h_nominal = file.Get(f"{nominal_folder}/{variable_name}")
    h_up = file.Get(f"{syst_folder}/{up_name}")
    h_down = file.Get(f"{syst_folder}/{down_name}")
    
    if not h_nominal or not h_up or not h_down:
        print(f"Error: Histogram for {systematic} not found in file!")
        return
    
    canvas_title = f"{systematic.capitalize()} Variations"
    c = ROOT.TCanvas("c", canvas_title, 800, 600)
    
    h_nominal.SetLineColor(ROOT.kBlack)  
    h_up.SetLineColor(ROOT.kRed)         
    h_down.SetLineColor(ROOT.kBlue)      
    
    h_nominal.SetTitle(f"{systematic.capitalize()} Variations")
    h_nominal.GetXaxis().SetTitle(f"{systematic.capitalize()} Systematic")
    h_nominal.GetYaxis().SetTitle("Entries")
    
    h_nominal.Draw("hist")  
    h_up.Draw("hist same") 
    h_down.Draw("hist same") 
    
    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.AddEntry(h_nominal, "Nominal", "l")
    legend.AddEntry(h_up, "Up Variation", "l")
    legend.AddEntry(h_down, "Down Variation", "l")
    legend.Draw()
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, f"{systematic}_variations.png")
    c.SaveAs(output_file)
    
    file.Close()

systematics = [
    "pu", "prefiring", "mu_id_stat", "mu_id_syst", "mu_iso_stat", "mu_iso_syst",
    "mu_trigger_stat", "mu_trigger_syst", "ele_id", "ele_trigger", "ele_reco",
    "murmuf_upup", "murmuf_upnone", "murmuf_noneup", "murmuf_nonedown",
    "murmuf_downnone", "murmuf_downdown", "isr", "fsr", "btag_cferr1", "btag_cferr2", 
    "btag_hf", "btag_hfstats1", "btag_hfstats2", "btag_lf", "btag_lfstats1", 
    "btag_lfstats2", "ttag_corr", "ttag_uncorr", "tmistag"
]

root_file = "Others.root"  
variable_name = "Sigma_phi_2"

mass_regions = ["0_500", "500_750", "750_1000", "1000_1500", "1500Inf"]

for mass_region in mass_regions:
    nominal_folder = f"DeltaY_reco_{mass_region}_SR_General"
    syst_folder = f"DeltaY_reco_SystVariations_{mass_region}_SR"
    output_dir = mass_region  # Save outputs in directories named after mass regions
    for syst in systematics:
        variations(root_file, variable_name, syst, nominal_folder, syst_folder, output_dir)
