import ROOT
import os
import math


ROOT.gROOT.SetBatch(True)

def variations(root_file, variable_name, systematic, nominal_folder, syst_folder, output_dir, use_suffixes=True):
    file = ROOT.TFile(root_file, "READ")
    
    if use_suffixes:
        up_name = "{variable_name}_{systematic}_up".format(variable_name=variable_name, systematic=systematic)
        down_name = "{variable_name}_{systematic}_down".format(variable_name=variable_name, systematic=systematic)
    else:
        # For custom naming, such as PDF systematic
        up_name = "{variable_name}_{systematic}_up".format(variable_name=variable_name, systematic=systematic)
        down_name = "{variable_name}_{systematic}_down".format(variable_name=variable_name, systematic=systematic)
    
    # Adjust folder paths if necessary
    if nominal_folder == ".":
        nominal_hist_path = "{variable_name}".format(variable_name=variable_name)
    else:
        nominal_hist_path = "{nominal_folder}/{variable_name}".format(nominal_folder=nominal_folder, variable_name=variable_name)
    
    if syst_folder == ".":
        up_hist_path = "{up_name}".format(up_name=up_name)
        down_hist_path = "{down_name}".format(down_name=down_name)
    else:
        up_hist_path = "{syst_folder}/{up_name}".format(syst_folder=syst_folder, up_name=up_name)
        down_hist_path = "{syst_folder}/{down_name}".format(syst_folder=syst_folder, down_name=down_name)
    
    h_nominal = file.Get(nominal_hist_path)
    h_up = file.Get(up_hist_path)
    h_down = file.Get(down_hist_path)
    
    if not h_nominal:
        print "Error: Nominal histogram '{}' not found in file '{}'.".format(nominal_hist_path, root_file)
        return
    if not h_up:
        print "Error: Up variation histogram '{}' not found in file '{}'.".format(up_hist_path, root_file)
        return
    if not h_down:
        print "Error: Down variation histogram '{}' not found in file '{}'.".format(down_hist_path, root_file)
        return
    
    # Calculate the maximum value among the histograms
    max_vals = [h_nominal.GetMaximum(), h_up.GetMaximum(), h_down.GetMaximum()]
    max_hist = max(max_vals)
    
    # Set the y-axis range
    h_nominal.SetMinimum(0)
    h_nominal.SetMaximum(max_hist * 1.1)
    
    canvas_title = "{} Variations".format(systematic.capitalize())
    c = ROOT.TCanvas("c", canvas_title, 800, 600)
    
    h_nominal.SetLineColor(ROOT.kBlack)
    h_up.SetLineColor(ROOT.kRed)
    h_down.SetLineColor(ROOT.kBlue)
    
    h_nominal.SetTitle(canvas_title)
    h_nominal.GetXaxis().SetTitle(variable_name)
    h_nominal.GetYaxis().SetTitle("Entries")
    
    h_nominal.Draw("hist")
    h_up.Draw("hist same")
    h_down.Draw("hist same")
    
    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.AddEntry(h_nominal, "Nominal", "l")
    legend.AddEntry(h_up, "Up Variation", "l")
    legend.AddEntry(h_down, "Down Variation", "l")
    legend.Draw()
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    output_file = os.path.join(output_dir, "{}_variations.png".format(systematic))
    c.SaveAs(output_file)
    
    file.Close()


def plot_murmuf_variations(root_file, variable_name, murmuf_variations, nominal_folder, syst_folder, output_dir):
    file = ROOT.TFile(root_file, "READ")

    h_nominal = file.Get("{nominal_folder}/{variable_name}".format(nominal_folder=nominal_folder, variable_name=variable_name))
    if not h_nominal:
        print "Error: Nominal histogram '{0}' not found in file '{1}'.".format("{nominal_folder}/{variable_name}".format(nominal_folder=nominal_folder, variable_name=variable_name), root_file)
        return

    h_nominal.SetLineColor(ROOT.kBlack)
    hist_list = [h_nominal]
    max_vals = [h_nominal.GetMaximum()]

    colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen+2, ROOT.kMagenta, ROOT.kOrange, ROOT.kCyan+2]
    for i, systematic in enumerate(murmuf_variations):
        hist_name = "{variable_name}_{systematic}".format(variable_name=variable_name, systematic=systematic)
        h_var = file.Get("{syst_folder}/{hist_name}".format(syst_folder=syst_folder, hist_name=hist_name))
        if not h_var:
            print "Error: Variation histogram '{0}' not found in file '{1}'.".format("{syst_folder}/{hist_name}".format(syst_folder=syst_folder, hist_name=hist_name), root_file)
            continue
        h_var.SetLineColor(colors[i % len(colors)])
        hist_list.append(h_var)
        max_vals.append(h_var.GetMaximum())

    if len(hist_list) == 1:
        print "Warning: No murmuf variation histograms found in file '{0}'.".format(root_file)
        return

    max_hist = max(max_vals)
    h_nominal.SetMinimum(0)
    h_nominal.SetMaximum(max_hist * 1.1)

    canvas_title = "Murmuf Variations"
    c = ROOT.TCanvas("c", canvas_title, 800, 600)
    h_nominal.SetTitle(canvas_title)
    h_nominal.GetXaxis().SetTitle(variable_name)
    h_nominal.GetYaxis().SetTitle("Entries")

    h_nominal.Draw("hist")
    for h_var in hist_list[1:]:
        h_var.Draw("hist same")

    legend = ROOT.TLegend(0.7, 0.6, 0.9, 0.9)
    legend.AddEntry(h_nominal, "Nominal", "l")
    for i, h_var in enumerate(hist_list[1:]):
        legend.AddEntry(h_var, murmuf_variations[i], "l")
    legend.Draw()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "murmuf_variations.png")
    c.SaveAs(output_file)
    file.Close()

def plot_pdf_uncertainty(root_file, variable_name, nominal_folder, pdf_folder, output_dir):
    file = ROOT.TFile(root_file, "READ")

    # Read the nominal histogram
    h_nominal = file.Get("{nominal_folder}/{variable_name}".format(nominal_folder=nominal_folder, variable_name=variable_name))
    if not h_nominal:
        print "Error: Nominal histogram '{0}' not found in file '{1}'.".format("{nominal_folder}/{variable_name}".format(nominal_folder=nominal_folder, variable_name=variable_name), root_file)
        return

    # Clone the nominal histogram to create up and down histograms
    h_pdf_up = h_nominal.Clone("h_pdf_up")
    h_pdf_down = h_nominal.Clone("h_pdf_down")
    h_pdf_up.Reset()
    h_pdf_down.Reset()

    nbins = h_nominal.GetNbinsX()

    # Initialize a list to store the PDF variation histograms
    pdf_variations = []

    # Read and normalize the 100 PDF variation histograms
    for i in range(1, 101):
        hist_name = "{variable_name}_PDF_{index}".format(variable_name=variable_name, index=i)
        h_pdf_var = file.Get("{pdf_folder}/{hist_name}".format(pdf_folder=pdf_folder, hist_name=hist_name))
        if not h_pdf_var:
            print "Warning: PDF variation histogram '{0}' not found in file '{1}'.".format("{pdf_folder}/{hist_name}".format(pdf_folder=pdf_folder, hist_name=hist_name), root_file)
            continue

        # Normalize the PDF variation histogram to the nominal histogram
        norm_factor = h_pdf_var.Integral() / h_nominal.Integral() if h_nominal.Integral() != 0 else 1.0
        h_pdf_var.Scale(1.0 / norm_factor)
        pdf_variations.append(h_pdf_var)

    if len(pdf_variations) == 0:
        print "Warning: No PDF variation histograms found in file '{0}'.".format(root_file)
        return

    # Calculate the RMS of the variations for each bin
    for bin_idx in range(1, nbins + 1):
        nominal_bin_content = h_nominal.GetBinContent(bin_idx)
        sum_squares = 0.0
        n_variations = len(pdf_variations)
        for h_var in pdf_variations:
            var_bin_content = h_var.GetBinContent(bin_idx)
            diff = var_bin_content - nominal_bin_content
            sum_squares += diff ** 2

        rms = math.sqrt(sum_squares / n_variations) if n_variations > 0 else 0.0

        # Set the up and down bin contents
        h_pdf_up.SetBinContent(bin_idx, nominal_bin_content + rms)
        h_pdf_down.SetBinContent(bin_idx, nominal_bin_content - rms)

    # Set up the canvas
    c = ROOT.TCanvas("c_pdf", "PDF Variations", 800, 600)

    # Set line colors
    h_nominal.SetLineColor(ROOT.kBlack)
    h_pdf_up.SetLineColor(ROOT.kRed)
    h_pdf_down.SetLineColor(ROOT.kBlue)

    # Set titles
    h_nominal.SetTitle("PDF Variations")
    h_nominal.GetXaxis().SetTitle(variable_name)
    h_nominal.GetYaxis().SetTitle("Entries")

    # Calculate the maximum y-value among the histograms
    max_vals = [h_nominal.GetMaximum(), h_pdf_up.GetMaximum(), h_pdf_down.GetMaximum()]
    max_hist = max(max_vals)
    h_nominal.SetMinimum(0)
    h_nominal.SetMaximum(max_hist * 1.1)

    # Draw histograms
    h_nominal.Draw("hist")
    h_pdf_up.Draw("hist same")
    h_pdf_down.Draw("hist same")

    # Add legend
    legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    legend.AddEntry(h_nominal, "Nominal", "l")
    legend.AddEntry(h_pdf_up, "PDF Up", "l")
    legend.AddEntry(h_pdf_down, "PDF Down", "l")
    legend.Draw()

    # Handle os.makedirs for Python 2
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "PDF_variations.png")
    c.SaveAs(output_file)

    file.Close()

# List of standard systematics (excluding murmuf variations)
systematics = [
    "pu", "prefiring", "mu_id_stat", "mu_id_syst", "mu_iso_stat", "mu_iso_syst",
    "mu_trigger_stat", "mu_trigger_syst", "ele_id", "ele_trigger", "ele_reco",
    "isr", "fsr", "btag_cferr1", "btag_cferr2", 
    "btag_hf", "btag_hfstats1", "btag_hfstats2", "btag_lf", "btag_lfstats1", 
    "btag_lfstats2", "ttag_corr", "ttag_uncorr", "tmistag"
]

# List of murmuf variations
murmuf_variations = [
    "murmuf_upup", "murmuf_upnone", "murmuf_noneup", "murmuf_nonedown",
    "murmuf_downnone", "murmuf_downdown"
]

variable_name = "DeltaY_reco_d2"

mass_regions = ["0_500", "500_750", "750_1000", "1000_1500", "1500Inf"]

root_files = ["TTbar.root", "ST.root", "Others.root"]

root_files_base_path = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/nominal"

for root_file_name in root_files:
    root_file = os.path.join(root_files_base_path, root_file_name)

    if not os.path.isfile(root_file):
        print "Error: ROOT file {0} not found!".format(root_file)
        continue

    for mass_region in mass_regions:
        nominal_folder = "DeltaY_reco_{mass_region}_SR_General".format(mass_region=mass_region)
        syst_folder = "DeltaY_reco_SystVariations_{mass_region}_SR".format(mass_region=mass_region)
        pdf_folder = "DeltaY_reco_PDFVariations_{mass_region}_SR".format(mass_region=mass_region)

        root_file_base = os.path.splitext(root_file_name)[0] 
        output_dir = os.path.join("DeltaY_reco_d2", mass_region, root_file_base)

        for syst in systematics:
            variations(root_file, variable_name, syst, nominal_folder, syst_folder, output_dir, use_suffixes=True)

        plot_pdf_uncertainty(root_file, variable_name, nominal_folder, pdf_folder, output_dir)
