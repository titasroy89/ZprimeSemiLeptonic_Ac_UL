import ROOT
from math import sqrt, pow

input_files = {
    "dY_UL18_muon_750_1000_TTbar.root": "TTbar", 
    "dY_UL18_muon_750_1000_WJets.root": "WJets",
    "dY_UL18_muon_750_1000_ST.root": "ST",
    "dY_UL18_muon_750_1000_Diboson.root": "Diboson",
    "dY_UL18_muon_750_1000_DY.root": "DY",
    "dY_UL18_muon_750_1000_QCD.root": "QCD",
}

input_base_dir = "./"

for filename, sample in input_files.items():
    file_path = input_base_dir + filename
    
    f = ROOT.TFile.Open(file_path, "UPDATE")
    
    # Different samples in the TTbar file
    if sample == "TTbar":
        ttbar_samples = ["TTbar1", "TTbar2"] 
        for ttbar_sample in ttbar_samples:
            h_nominal_path = "{}".format(ttbar_sample)
            h_nominal = f.Get(h_nominal_path)
            
            h_nominal_new = h_nominal.Clone(sample)  # New name for the nominal histogram
            h_pdfUp = h_nominal.Clone(sample + "_pdfUp")  # Name for the pdfUp histogram
            h_pdfDown = h_nominal.Clone(sample + "_pdfDown")
            
            for hist in [h_nominal_new, h_pdfUp, h_pdfDown]:
                if hist:
                    hist.Write("", ROOT.TObject.kOverwrite)
    else:
        h_nominal_path = "{}".format(sample)
        h_nominal = f.Get(h_nominal_path)
    
        h_nominal_new = h_nominal.Clone(sample)  # New name for the nominal histogram
        h_pdfUp = h_nominal.Clone(sample + "_pdfUp")  # Name for the pdfUp histogram
        h_pdfDown = h_nominal.Clone(sample + "_pdfDown")

        if sample != "Diboson":  # If not Diboson, calculate PDF uncertainties
            h_nominal_sum_weights = f.Get("Middle_General/sum_event_weights")
            v_pdf_norm = []

            # Retrieve the PDF histograms
            v_pdf = []  
            for i in range(1, 101):  
                h_pdf = f.Get("Middle_General/sum_event_weights_PDF_" + str(i))
                norm_scale_pdf = h_pdf.GetBinContent(1) / h_nominal_sum_weights.GetBinContent(1)
                v_pdf_norm.append(norm_scale_pdf)
                v_pdf.append(h_pdf) 

            n_hists = len(v_pdf) // 100  
            for i in range(n_hists):
                # Use the existing h_pdfUp and h_pdfDown instead of cloning again
                for j in range(1, h_pdfUp.GetNbinsX() + 1):  # loop over bins; +1 because the range is exclusive
                    nominal_bin_content = h_nominal.GetBinContent(j)
                    sum_bins = 0.

                    for k in range(100):  # loop over PDF variations
                        h_pdf_variation = v_pdf[k * n_hists + i]
                        if j == 1:  # scale only once and not again for each bin!
                            h_pdf_variation.Scale(1. / v_pdf_norm[k])
                        bin_content = h_pdf_variation.GetBinContent(j)
                        sum_bins += pow(bin_content - nominal_bin_content, 2)

                    rms = sqrt(sum_bins / 100)
                    h_pdfUp.SetBinContent(j, nominal_bin_content + rms)
                    h_pdfDown.SetBinContent(j, nominal_bin_content - rms)

    # Write histograms to the file
    for hist in [h_nominal_new, h_pdfUp, h_pdfDown]:
        if hist:
            hist.Write("", ROOT.TObject.kOverwrite)
            
    f.Close()
