from ROOT import *
import os
import sys
import math
from optparse import OptionParser
      

parser = OptionParser()
parser.add_option("-y", "--year", dest="year", help="Specify the year (UL18, UL17, preUL16, postUL16)", type='str')
parser.add_option("-l", "--lepton_flavor", dest="lepton_flavor", help="Specify the lepton flavor (electron, muon)", type='str')

(options, args) = parser.parse_args()

year = options.year if options.year else "UL18"  # default value if not specified
lepton_flavor = options.lepton_flavor if options.lepton_flavor else "muon"  # default value if not specified


# finalState = options.channel

inputDir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/{}/".format(year)
combine_file_name = 'Mtt_{}_{}_CR2.root'.format(year, lepton_flavor)
combine_file = TFile(combine_file_name, 'RECREATE')
stackList = {"TTToSemiLeptonic", "TTToOthers", "WJets", "DY", "ST", "Diboson", "QCD", "DATA"}


############ 
# ----------------- other systematics except PDF, JER/JEC, murmuf ----------------
############ 


systematic_name_mapping = {
    "mu_reco": "muonReco",
    "pu": "pu",
    "prefiring": "prefiringWeight",
    "mu_id": "muonID",
    "mu_iso": "muonIso",
    "mu_trigger": "muonTrigger",
    "ele_id" : "electronID", 
    "ele_trigger": "electronTrigger",
    "ele_reco": "electronReco",
    "isr": "isr", 
    "fsr": "fsr", 
    "btag_cferr1": "btagCferr1", 
    "btag_cferr2": "btagCferr2", 
    "btag_hf": "btagHf",  
    "btag_hfstats1": "btagHfstats1",
    "btag_hfstats2": "btagHfstats2", 
    "btag_lf": "btagLf", 
    "btag_lfstats1": "btagLfstats1",
    "btag_lfstats2": "btagLfstats2", 
    "ttag_corr": "ttagCorr", 
    "ttag_uncorr": "ttagUncorr", 
    "tmistag": "tmistag"  
    
}

# reads nominal histograms and computes projections for the "TTbar" sample. 
# for other samples, it reads nominal histograms and writes them to the output file. 
# It also processes and writes systematic variations, using systematic_name_mapping

print(" ----------------- all systematics except PDF, JER/JEC, murmuf ----------------")
for sample in stackList:
    inFile = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}_Syst_rebin_v2/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sample), "READ")
    if not inFile:
        print("Input file for {} not found.".format(sample))
        continue
    
    combine_file.cd()

    
    if sample == "DATA":
        print("Processing sample for other sys: ", sample)
        data_obs = inFile.Get("DNN_output2_General/M_Zprime_all").Clone("M_Zprime_DATA")
        data_obs.Rebin(2)
        data_obs.Write("M_Zprime_DATA")
    
    else:
        print("Processing sample for other sys: ", sample)
        
        h_nominal = inFile.Get("DeltaY_SystVariations_DNN_output2/M_Zprime").Clone("M_Zprime_" + sample)
        h_nominal.Rebin(2)
        h_nominal.Write("M_Zprime_" + sample)
        
        
        for sys, new_sys_name in systematic_name_mapping.items():
            print sys
            
            for variation in ["up", "down"]:
                sys_hist_name = "M_Zprime_{}_{}".format(sys, variation)
                sys_hist = inFile.Get("DeltaY_SystVariations_DNN_output2/" + sys_hist_name)
                if sys_hist:
                    sys_hist.Rebin(2)
                    output_hist_name = "M_Zprime_{}_{}{}".format(sample, sys, variation.capitalize())
                    sys_hist.Clone(output_hist_name).Write()
            
         
    inFile.Close()

# processes each sample in v_samples to create envelope histograms for each variation in v_variations. 
# histograms are normalized based on the first bin content and written to the DeltaY directory in the output ROOT file

# calculates normalization factors, and then computes the maximum and minimum variations for each bin. The resulting histograms are named sample_murmufUp and sample_murmufDown

############ 
# ----------------- murmuf ----------------

# 1) Retrieve histograms from the input file: nominal, upup, upnone
# 2) Calculate normalization scales for each variation by dividing the first bin content of each variation histogram by the first bin content of the nominal histogram.
# 3) Apply these normalization scales to the corresponding histograms from a vector of murmuf variations (like v_murmuf_upup, v_murmuf_upnone, etc.).
# 4) For each set of variation histograms, find the maximum and minimum values in each bin among all variations, create two new histograms: hist_scaleUp and hist_scaleDown.
# 5) Name these histograms depending on the specific convention
############ 

def getEnvelope(inputDir, v_samples, v_variations, combine_file):
    
    print(" ----------------- murmuf processing ----------------")
    
    for sample in v_samples:
        inFile = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}_Syst_rebin_v2/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sample), "READ")       
        if not inFile:
            print("Input file for {} not found.".format(sample))
            continue
        combine_file.cd()

        print("Processing sample for murmuf: ", sample)
    
        h_nominal = inFile.Get("DeltaY_SystVariations_DNN_output2/M_Zprime")
        h_nominal.Rebin(2)
        scales = {}
        if not h_nominal:
            print("Nominal histogram for {} not found.".format(sample))
            continue

        for variation in v_variations:
            variation_hist = inFile.Get("DeltaY_SystVariations_DNN_output2/M_Zprime_murmuf_{}".format(variation))
            
            if variation_hist: 
                variation_hist.Rebin(2)
                if h_nominal.GetBinContent(1) != 0:
                    scales[variation] = variation_hist.GetBinContent(1) / h_nominal.GetBinContent(1)
            else:
                print("Histogram for variation '{}' not found in {}".format(variation, sample))

        hist_scaleUp = h_nominal.Clone("M_Zprime_" + sample + "_murmufUp")
        hist_scaleDown = h_nominal.Clone("M_Zprime_" + sample + "_murmufDown")

        # apply scales and find max/min for each bin
        for bin_idx in range(1, h_nominal.GetNbinsX() + 1):
            max_val = h_nominal.GetBinContent(bin_idx)
            min_val = h_nominal.GetBinContent(bin_idx)
            for var, scale in scales.items():
                var_hist = inFile.Get("DeltaY_SystVariations_DNN_output2/M_Zprime_murmuf_{}".format(var))
                if var_hist:
                    scaled_val = var_hist.GetBinContent(bin_idx) / scale
                    max_val = max(max_val, scaled_val)
                    min_val = min(min_val, scaled_val)

            hist_scaleUp.SetBinContent(bin_idx, max_val)
            hist_scaleDown.SetBinContent(bin_idx, min_val)
        
        combine_file.cd()
        hist_scaleUp.Write()
        hist_scaleDown.Write()

        inFile.Close()



############ 
# ----------------- PDFs (100) ----------------
############ 


def processPDF(inputDir, v_samples, combine_file):
    print(" ----------------- PDFs processing ----------------")
    
    
    for sample in v_samples:
        inFile = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}_Syst_rebin_v2/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sample), "READ")
        if not inFile:
            print("Input file for {} not found.".format(sample))
            continue
        combine_file.cd()

        print("Processing PDF: ", sample)
        nominal_hist_name = "DeltaY_SystVariations_DNN_output2/M_Zprime" if sample == "Diboson" else "DeltaY_SystVariations_DNN_output2/M_Zprime"
        nominal = inFile.Get(nominal_hist_name)
        if not nominal:
            print("Nominal histogram for {} not found.".format(sample))
            continue

        nominal.Rebin(2)
        # nominal.GetXaxis().SetRangeUser(0, 5000)

        if sample == "Diboson":
            hist_pdfUp = nominal.Clone("M_Zprime_Diboson_pdfUp")
            hist_pdfDown = nominal.Clone("M_Zprime_Diboson_pdfDown")
            
            hist_pdfUp.Write()
            hist_pdfDown.Write()


        else:
            
            hist_pdfUp = TH1F("M_Zprime_{}_pdfUp".format(sample), "{} pdf up variation".format(sample), nominal.GetNbinsX(), nominal.GetXaxis().GetXmin(), nominal.GetXaxis().GetXmax())
            hist_pdfDown = TH1F("M_Zprime_{}_pdfDown".format(sample), "{} pdf down variation".format(sample), nominal.GetNbinsX(), nominal.GetXaxis().GetXmin(), nominal.GetXaxis().GetXmax())
            
            sum_bins = [0.] * (nominal.GetNbinsX() + 1)  # Initialize sum of deviations squared for each bin
            
            for i in range(1, 101):
                pdf_hist = inFile.Get("Zprime_PDFVariations_DNN_output2/M_Zprime_PDF_{}".format(i))
                if pdf_hist:
                    pdf_hist.Rebin(2)
                    if nominal.GetBinContent(1) != 0:
                        scale = pdf_hist.GetBinContent(1) / nominal.GetBinContent(1)
                        pdf_hist.Scale(1. / scale)

                    for bin_idx in range(1, nominal.GetNbinsX() + 1):
                        deviation = pdf_hist.GetBinContent(bin_idx) - nominal.GetBinContent(bin_idx)
                        sum_bins[bin_idx] += deviation ** 2

            for bin_idx in range(1, nominal.GetNbinsX() + 1):
                rms = math.sqrt(sum_bins[bin_idx] / 100)
                hist_pdfUp.SetBinContent(bin_idx, nominal.GetBinContent(bin_idx) + rms)
                hist_pdfDown.SetBinContent(bin_idx, nominal.GetBinContent(bin_idx) - rms)

            hist_pdfUp.Write()
            hist_pdfDown.Write()

        inFile.Close()
            
            
# Diboson Sample:
# For Diboson, I am cloning the nominal histogram for each of the 100 PDF variations and naming them Up or Down variation. So, this sample is without specific PDF variations.

# TTbar Sample:
# I am creating a matrix from four quadrants, calculating the projection for each, and then applying each of the 100 PDF variations.
# For each PDF variation, I create a matrix, calculate its projections, and then calculate the deviation from the nominal projection for both projections (TTbar_1 and TTbar_2).

# Other Samples:
# For samples other than Diboson and TTbar, I am looping through each of the 100 PDF variations and calculate the Up and Down variations based on the deviation from the nominal histogram.

############ 
# ----------------- JER/JEC ----------------
############ 


def processJERJEC(inputDir, v_samples, combine_file, sys_variations):
    print(" ----------------- JER/JEC processing ----------------")

    for sys_variation in sys_variations: 
        print(" --- passed to another JER/JEC variation ---")
        for sample in v_samples:
            sys_file = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}_{}_Syst/{}.root".format(lepton_flavor, year, lepton_flavor, sys_variation, sample), "READ")
            if not sys_file:
                print("Input file for {} variation {} not found.".format(sample, sys_variation))
                continue
            
            combine_file.cd()

            print("Processing {} for {} ".format(sample, sys_variation))
            hist_name = "DNN_output2_General/M_Zprime"
            jer_jec_hist = sys_file.Get(hist_name)
            
            if jer_jec_hist:
                
                new_hist_name = "M_Zprime_{}_{}".format(sample, sys_variation.split('_')[0].lower() + sys_variation.split('_')[1].capitalize())
                jer_jec_hist_cloned = jer_jec_hist.Clone(new_hist_name)
                jer_jec_hist_cloned.Rebin(2)
                # jer_jec_hist_cloned.GetXaxis().SetRangeUser(0, 5000)
                jer_jec_hist_cloned.Write()
            
            else:
                print("Missing histogram for {}: {}".format(sample, hist_name))
                
            sys_file.Close()



sys_variations = ["JEC_up", "JEC_down", "JER_up", "JER_down"]

v_samples = ["TTToSemiLeptonic", "TTToOthers", "WJets", "ST", "QCD", "DY", "Diboson"]
v_variations = ["upup", "upnone", "noneup", "nonedown", "downnone", "downdown"]

getEnvelope(inputDir, v_samples, v_variations, combine_file)

processPDF(inputDir, v_samples, combine_file)

processJERJEC(inputDir, v_samples, combine_file, sys_variations)

combine_file.Close()