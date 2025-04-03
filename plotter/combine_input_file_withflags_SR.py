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

# inputDir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/{}/".format(year)
inputDir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_latest_dY/nominal/"
combine_file_name = 'Mtt_{}_{}_CR2_dY.root'.format(year, lepton_flavor)
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
    inFile = TFile.Open(inputDir + "{}.root".format(sample), "READ")
    if not inFile:
        print("Input file for {} not found.".format(sample))
        continue
    
    combine_file.cd()

    
    if sample == "DATA":
        print("Processing sample for other sys: ", sample)
        data_obs = inFile.Get("DNN_output2_General/DeltaY_reco").Clone("DeltaY_DATA")
        data_obs.Rebin(2)
        data_obs.Write("DeltaY_DATA")
    
    elif sample == "TTToSemiLeptonic" or sample == "TTToOthers":
        print("Processing sample for other sys: ", sample)
        path_nom = "DeltaY_reco_SystVariations_ttbar_{}_CR2/DeltaY_tt".format(lepton_flavor)
                
        # Retrieving the response matrix directly
        Matrix = inFile.Get(path_nom)
        if not Matrix:
            print("Response matrix not found for TTbar.")
            continue
        
        ProjX_1 = Matrix.ProjectionX("TTbar_1", 1, 1)
        ProjX_2 = Matrix.ProjectionX("TTbar_2", 2, 2)

        # ProjX_1.GetXaxis().SetTitle("#Delta_Y_{reco}")
        # ProjX_2.GetXaxis().SetTitle("#Delta_Y_{reco}")

        nominal_projections = [ProjX_1, ProjX_2]
        
        Matrix.Write()
    
        ProjX_1.Add(ProjX_2)
        ProjX_1.Write("DeltaY_" + sample)
        print(ProjX_1.GetEntries())
        
        
        for sys, new_sys_name in systematic_name_mapping.items():
            print sys
            for variation in ["up", "down"]:
                
                # Retrieve matrices for systematic variations
                matrix_path = "DeltaY_reco_SystVariations_ttbar_{}_CR2/DeltaY_{}_{}_tt".format(lepton_flavor, sys,variation)
                Matrix_var = inFile.Get(matrix_path)
                if not Matrix_var:
                    print("Response matrix for systematic {} variation {} not found.").format(sys, variation)
                    continue
                
                output_hist_1 = "DeltaY_{}_{}_1".format(sys, variation)
                output_hist_2 = "DeltaY_{}_{}_2".format(sys, variation)
                
                ProjX_1 = Matrix.ProjectionX(output_hist_1, 1, 1)
                ProjX_2 = Matrix.ProjectionX(output_hist_2, 2, 2)
                
                if not ProjX_1:
                    print("issue in projx1 ")

                output_hist_name = "DeltaY_{}_{}{}".format(sample, sys, variation.capitalize())
                
                ProjX_1.Add(ProjX_2)
                ProjX_1.Write(output_hist_name)
     
    
    else:
        print("Processing sample for other sys: ", sample)
        
        h_nominal = inFile.Get("DeltaY_SystVariations_DNN_output2/DeltaY").Clone("DeltaY_" + sample)
        h_nominal.Rebin(2)
        h_nominal.Write("DeltaY_" + sample)
        print(h_nominal.GetEntries())
        
        
        for sys, new_sys_name in systematic_name_mapping.items():
            print sys
            
            for variation in ["up", "down"]:
                sys_hist_name = "DeltaY_{}_{}".format(sys, variation)
                sys_hist = inFile.Get("DeltaY_SystVariations_DNN_output2/" + sys_hist_name)
                if sys_hist:
                    sys_hist.Rebin(2)
                    output_hist_name = "DeltaY_{}_{}{}".format(sample, sys, variation.capitalize())
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
        inFile = TFile.Open(inputDir + "{}.root".format(sample), "READ")       
        if not inFile:
            print("Input file for {} not found.".format(sample))
            continue
        combine_file.cd()

        print("Processing sample for murmuf: ", sample)
        
        if sample == "TTToSemiLeptonic" or sample == "TTToOthers":
            
            print("Processing sample for murmuf: ", sample)
            
            scaled_histograms_up = {}
            scaled_histograms_down = {}
            
            hist_scaleUp_1 = ProjX_1.Clone("TTbar_1_murmufUp")
            hist_scaleDown_1 = ProjX_1.Clone("TTbar_1_murmufDown")
            hist_scaleUp_2 = ProjX_2.Clone("TTbar_2_murmufUp")
            hist_scaleDown_2 = ProjX_2.Clone("TTbar_2_murmufDown")
        
            for variation in v_variations:
                path_var = "DeltaY_reco_SystVariations_ttbar_{}_CR2/DeltaY_murmuf_{}_tt".format(lepton_flavor, variation)
                matrix_var = inFile.Get(path_var)
               
                if not matrix_var:
                    print("Missing matrix for variation: {}".format(variation))
                
                projection_1 = matrix_var.ProjectionX("DeltaY_" + sample + "_murmufUp", 1, 1)
                projection_2 = matrix_var.ProjectionX("DeltaY_" + sample + "_murmufUp", 2, 2)
                
                # print(ProjX_1)

            
                norm_1 = projection_1.GetBinContent(1) / ProjX_1.GetBinContent(1)
                norm_2 = projection_2.GetBinContent(1) / ProjX_2.GetBinContent(1)
                
                scaled_histograms_up[variation + "_1"] = projection_1.Clone(variation + "_proj1_scaled")
                scaled_histograms_down[variation + "_2"] = projection_2.Clone(variation + "_proj2_scaled")
                scaled_histograms_up[variation + "_1"].Scale(1 / norm_1)
                scaled_histograms_down[variation + "_2"].Scale(1 / norm_2)


            for bin_idx in range(1, ProjX_1.GetNbinsX() + 1):
                max_val_1 = min_val_1 = hist_scaleUp_1.GetBinContent(bin_idx)
                max_val_2 = min_val_2 = hist_scaleUp_2.GetBinContent(bin_idx)

                for key in scaled_histograms_up.keys():
                    max_val_1 = max(max_val_1, scaled_histograms_up[key].GetBinContent(bin_idx))
                    min_val_1 = min(min_val_1, scaled_histograms_up[key].GetBinContent(bin_idx))

                for key in scaled_histograms_down.keys():
                    max_val_2 = max(max_val_2, scaled_histograms_down[key].GetBinContent(bin_idx))
                    min_val_2 = min(min_val_2, scaled_histograms_down[key].GetBinContent(bin_idx))

                hist_scaleUp_1.SetBinContent(bin_idx, max_val_1)
                hist_scaleDown_1.SetBinContent(bin_idx, min_val_1)
                hist_scaleUp_2.SetBinContent(bin_idx, max_val_2)
                hist_scaleDown_2.SetBinContent(bin_idx, min_val_2)

            hist_scaleUp_1.Add(hist_scaleUp_2)
            hist_scaleUp_1.Write("DeltaY_" + sample + "_murmufUp")
            
            hist_scaleDown_1.Add(hist_scaleDown_2)
            hist_scaleDown_1.Write("DeltaY_" + sample + "_murmufDown")

    
    
        else:
            h_nominal = inFile.Get("DeltaY_SystVariations_DNN_output2/DeltaY")
            h_nominal.Rebin(2)
            scales = {}
            if not h_nominal:
                print("Nominal histogram for {} not found.".format(sample))
                continue

            for variation in v_variations:
                variation_hist = inFile.Get("DeltaY_SystVariations_DNN_output2/DeltaY_murmuf_{}".format(variation))
                
                if variation_hist: 
                    variation_hist.Rebin(2)
                    if h_nominal.GetBinContent(1) != 0:
                        scales[variation] = variation_hist.GetBinContent(1) / h_nominal.GetBinContent(1)
                else:
                    print("Histogram for variation '{}' not found in {}".format(variation, sample))

            hist_scaleUp = h_nominal.Clone("DeltaY_" + sample + "_murmufUp")
            hist_scaleDown = h_nominal.Clone("DeltaY_" + sample + "_murmufDown")

            # apply scales and find max/min for each bin
            for bin_idx in range(1, h_nominal.GetNbinsX() + 1):
                max_val = h_nominal.GetBinContent(bin_idx)
                min_val = h_nominal.GetBinContent(bin_idx)
                for var, scale in scales.items():
                    var_hist = inFile.Get("DeltaY_SystVariations_DNN_output2/DeltaY_murmuf_{}".format(var))
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
        inFile = TFile.Open(inputDir + "{}.root".format(sample), "READ")
        if not inFile:
            print("Input file for {} not found.".format(sample))
            continue
        combine_file.cd()

        print("Processing PDF: ", sample)
        nominal_hist_name = "DeltaY_SystVariations_DNN_output2/DeltaY" 
        # if sample == "Diboson" else "DeltaY_SystVariations_DNN_output2/DeltaY"
        nominal = inFile.Get(nominal_hist_name)
        if not nominal:
            print("Nominal histogram for {} not found.".format(sample))
            continue

        nominal.Rebin(2)
        # nominal.GetXaxis().SetRangeUser(0, 5000)

        if sample == "Diboson":
            hist_pdfUp = nominal.Clone("DeltaY_Diboson_pdfUp")
            hist_pdfDown = nominal.Clone("DeltaY_Diboson_pdfDown")
            
            hist_pdfUp.Write()
            hist_pdfDown.Write()
        
        elif sample == "TTToSemiLeptonic" or sample == "TTToOthers":
            print("Processing TTbar for PDF: ", sample)
            
            
            # Process PDF variations
            pdf_projections_1 = []
            pdf_projections_2 = []
            
            for i in range(1, 101):  
                weight_matrix_path = "DeltaY_reco_PDFVariations_ttbar_{}_CR2/DeltaY_PDF_RM_{}".format(lepton_flavor, i)
                weight_matrix = inFile.Get(weight_matrix_path)
                if not weight_matrix:
                    print("PDF weight matrix {} not found.").format(i)
                    continue
                
        
                pdf_projections_1.append(weight_matrix.ProjectionX("px1_pdf_{}".format(i), 1, 1))
                pdf_projections_2.append(weight_matrix.ProjectionX("px2_pdf_{}".format(i), 2, 2))
                
                
                # Step 2: normalization & rms calculation
            norm_scales_1 = []
            norm_scales_2 = []
                
            for i in range(100):
                norm_scale_1 = pdf_projections_1[i].GetBinContent(1) / ProjX_1.GetBinContent(1)
                norm_scales_1.append(norm_scale_1)
                pdf_projections_1[i].Scale(1. / norm_scale_1)
                
                norm_scale_2 = pdf_projections_2[i].GetBinContent(1) / ProjX_2.GetBinContent(1)
                norm_scales_2.append(norm_scale_2)
                pdf_projections_2[i].Scale(1. / norm_scale_2)
                
            hist_pdfUp_1 = TH1D("DeltaY_{}_pdfUp".format(sample), "", ProjX_1.GetNbinsX(), ProjX_1.GetXaxis().GetXmin(), ProjX_1.GetXaxis().GetXmax())
            hist_pdfDown_1 = TH1D("DeltaY_{}_pdfDown".format(sample), "", ProjX_1.GetNbinsX(), ProjX_1.GetXaxis().GetXmin(), ProjX_1.GetXaxis().GetXmax())
            hist_pdfUp_2 = TH1D("DeltaY_{}_pdfUp".format(sample), "", ProjX_2.GetNbinsX(), ProjX_2.GetXaxis().GetXmin(), ProjX_2.GetXaxis().GetXmax())
            hist_pdfDown_2 = TH1D("DeltaY_{}_pdfDown".format(sample), "", ProjX_2.GetNbinsX(), ProjX_2.GetXaxis().GetXmin(), ProjX_2.GetXaxis().GetXmax())


            for bin_idx in range(1, ProjX_1.GetNbinsX() + 1):
                sum_bins_1 = 0.
                for i in range(100):
                    bin_content_1_pdf = pdf_projections_1[i].GetBinContent(bin_idx)
                    sum_bins_1 += (bin_content_1_pdf - ProjX_1.GetBinContent(bin_idx)) ** 2
                rms_1 = math.sqrt(sum_bins_1 / 100)
                
        
                value_up_1 = ProjX_1.GetBinContent(bin_idx) + rms_1
                value_down_1 = ProjX_1.GetBinContent(bin_idx) - rms_1
                
                hist_pdfUp_1.SetBinContent(bin_idx, value_up_1 )
                hist_pdfDown_1.SetBinContent(bin_idx, value_down_1)
            
            for bin_idx in range(1, ProjX_1.GetNbinsX() + 1):
                sum_bins_2 = 0.
                for i in range(100):
                    bin_content_2_pdf = pdf_projections_2[i].GetBinContent(bin_idx)
                    sum_bins_2 += (bin_content_2_pdf - ProjX_2.GetBinContent(bin_idx)) ** 2
                
                rms_2 = math.sqrt(sum_bins_2 / 100)
                
                value_up_2 = ProjX_2.GetBinContent(bin_idx) + rms_2
                value_down_2 = ProjX_2.GetBinContent(bin_idx) - rms_2
                
                hist_pdfUp_2.SetBinContent(bin_idx, value_up_2)
                hist_pdfDown_2.SetBinContent(bin_idx, value_down_2)
            
            hist_pdfUp_1.Add(hist_pdfUp_2) 
            hist_pdfUp_1.Write("DeltaY_{}_pdfUp".format(sample))
            hist_pdfDown_1.Add(hist_pdfDown_2)
            hist_pdfDown_1.Write("DeltaY_{}_pdfDown".format(sample))


        else:
            
            hist_pdfUp = TH1F("DeltaY_{}_pdfUp".format(sample), "{} pdf up variation".format(sample), nominal.GetNbinsX(), nominal.GetXaxis().GetXmin(), nominal.GetXaxis().GetXmax())
            hist_pdfDown = TH1F("DeltaY_{}_pdfDown".format(sample), "{} pdf down variation".format(sample), nominal.GetNbinsX(), nominal.GetXaxis().GetXmin(), nominal.GetXaxis().GetXmax())
            
            sum_bins = [0.] * (nominal.GetNbinsX() + 1)  # Initialize sum of deviations squared for each bin
            
            for i in range(1, 101):
                pdf_hist = inFile.Get("Zprime_PDFVariations_DNN_output2/DeltaY_PDF_{}".format(i))
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
            hist_name = "DeltaY_SystVariations_DNN_output2/DeltaY"
            jer_jec_hist = sys_file.Get(hist_name)
            
            if jer_jec_hist:
                
                new_hist_name = "DeltaY_{}_{}".format(sample, sys_variation.split('_')[0].lower() + sys_variation.split('_')[1].capitalize())
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

# processJERJEC(inputDir, v_samples, combine_file, sys_variations)

combine_file.Close()