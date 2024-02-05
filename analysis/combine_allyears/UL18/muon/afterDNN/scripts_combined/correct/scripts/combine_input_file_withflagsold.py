from ROOT import *
import os
import sys
from optparse import OptionParser
      

parser = OptionParser()
parser.add_option("-y", "--year", dest="year", help="Specify the year (UL18, UL17, preUL16, postUL16)", type='str')
parser.add_option("-m", "--mass_range", dest="mass_range", help="Specify the mass range (0_500, 500_750, 750-1000, 1000-1500, 1500Inf)", type='str')
parser.add_option("-l", "--lepton_flavor", dest="lepton_flavor", help="Specify the lepton flavor (electron, muon)", type='str')

(options, args) = parser.parse_args()

year = options.year if options.year else "UL18"  # default value if not specified
mass_range = options.mass_range if options.mass_range else "750_1000"  # default value if not specified
lepton_flavor = options.lepton_flavor if options.lepton_flavor else "muon"  # default value if not specified


# finalState = options.channel

inputDir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/{}/".format(year)
combine_file_name = 'dY_{}_{}_{}.root'.format(year, lepton_flavor, mass_range)
combine_file = TFile(combine_file_name, 'RECREATE')
stackList = {"TTbar", "WJets", "DY", "ST", "Diboson", "QCD", "DATA"}


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
    inFile = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sample), "READ")
    if not inFile:
        print("Input file for {} not found.".format(sample))
        continue
    
    combine_file.cd()

    
    if sample == "DATA":
        print("Processing sample for other sys: ", sample)
        data_obs = inFile.Get("DeltaY_reco_{}_{}_data_General/DeltaY_reco".format(mass_range, lepton_flavor)).Clone("data_obs")
        data_obs.Write("data_obs")
        
    elif sample == "TTbar":
        print("Processing sample for other sys: ", sample)
        h_nominal = inFile.Get("DeltaY_reco_SystVariations_{}_{}/DeltaY".format(mass_range, lepton_flavor)).Clone(sample)
        
        h_PP = inFile.Get("DY_P_P_{}_{}_General/DeltaY_reco".format(mass_range, lepton_flavor)).Clone()
        h_PN = inFile.Get("DY_P_N_{}_{}_General/DeltaY_reco".format(mass_range, lepton_flavor)).Clone()
        h_NP = inFile.Get("DY_N_P_{}_{}_General/DeltaY_reco".format(mass_range, lepton_flavor)).Clone()
        h_NN = inFile.Get("DY_N_N_{}_{}_General/DeltaY_reco".format(mass_range, lepton_flavor)).Clone()

        Matrix = TH2D("Matrix","", 2, -2.5, 2.5, 2, -2.5, 2.5)

        Matrix.SetBinContent(1, 1, h_NN.Integral())
        Matrix.SetBinContent(1, 2, h_PN.Integral())
        Matrix.SetBinContent(2, 1, h_NP.Integral())
        Matrix.SetBinContent(2, 2, h_PP.Integral())

        ProjX_1 = Matrix.ProjectionX("px1", 1, 1)
        ProjX_2 = Matrix.ProjectionX("px2", 2, 2)

        ProjX_1.GetXaxis().SetTitle("#Delta_Y_{reco}")
        ProjX_2.GetXaxis().SetTitle("#Delta_Y_{reco}")

        nominal_projections = [ProjX_1, ProjX_2]
        
        Matrix.Write()
        ProjX_1.Write("TTbar_1")
        ProjX_2.Write("TTbar_2")
        
        
        for sys, new_sys_name in systematic_name_mapping.items():
            print sys
            for variation in ["up", "down"]:
                h_PP = inFile.Get("DeltaY_reco_SystVariations_P_P_{}_{}/DeltaY_{}_{}".format(mass_range, lepton_flavor, sys, variation))
                h_PN = inFile.Get("DeltaY_reco_SystVariations_P_N_{}_{}/DeltaY_{}_{}".format(mass_range, lepton_flavor, sys, variation))
                h_NP = inFile.Get("DeltaY_reco_SystVariations_N_P_{}_{}/DeltaY_{}_{}".format(mass_range, lepton_flavor, sys, variation))
                h_NN = inFile.Get("DeltaY_reco_SystVariations_N_N_{}_{}/DeltaY_{}_{}".format(mass_range, lepton_flavor, sys, variation))

                # if not h_PP or not h_PN or not h_NP or not h_NN:
                #     print("Could not find one or more histograms for systematic '{}' variation '{}'".format(sys, variation))
                #     continue
                
                Matrix = TH2D("Matrix_{}_{}".format(sys, variation), "", 2, -2.5, 2.5, 2, -2.5, 2.5)
                Matrix.SetBinContent(1, 1, h_NN.Integral())
                Matrix.SetBinContent(1, 2, h_PN.Integral())
                Matrix.SetBinContent(2, 1, h_NP.Integral())
                Matrix.SetBinContent(2, 2, h_PP.Integral())

                ProjX_1 = Matrix.ProjectionX("px1_{}_{}".format(sys, variation), 1, 1)
                ProjX_2 = Matrix.ProjectionX("px2_{}_{}".format(sys, variation), 2, 2)

                ProjX_1.GetXaxis().SetTitle("#Delta_Y_{reco}")
                ProjX_2.GetXaxis().SetTitle("#Delta_Y_{reco}")

                output_hist_1 = "TTbar_1_{}{}".format(new_sys_name, variation.capitalize())
                output_hist_2 = "TTbar_2_{}{}".format(new_sys_name, variation.capitalize())

                ProjX_1.Write(output_hist_1)
                ProjX_2.Write(output_hist_2)

    else:
        print("Processing sample for other sys: ", sample)
        
        h_nominal = inFile.Get("DeltaY_reco_SystVariations_{}_{}/DeltaY".format(mass_range, lepton_flavor)).Clone(sample)
        h_nominal.Write(sample)
        
        
        for sys, new_sys_name in systematic_name_mapping.items():
            print sys
            
            for variation in ["up", "down"]:
                sys_hist_name = "DeltaY_{}_{}".format(sys, variation)
                sys_hist = inFile.Get("DeltaY_reco_SystVariations_{}_{}/".format(mass_range, lepton_flavor) + sys_hist_name)
                if sys_hist:
                    output_hist_name = "{}_{}{}".format(sample, new_sys_name, variation.capitalize())
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

def getEnvelope(inputDir, v_samples, v_variations, combine_file, nominal_projections):
    
    print(" ----------------- murmuf processing ----------------")
    
    for sample in v_samples:
        inFile = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sample), "READ")       
        if not inFile:
            print("Input file for {} not found.".format(sample))
            continue
        combine_file.cd()
        
        
        if sample == "TTbar":
            print("Processing sample for murmuf: ", sample)
        
            for variation in v_variations:
                
                Matrix = TH2D("Matrix_murmuf_{}".format(variation), "", 2, -2.5, 2.5, 2, -2.5, 2.5)
                for quadrant in ["P_P", "P_N", "N_P", "N_N"]:
                    hist_name = "DeltaY_reco_SystVariations_{}_{}_{}/DeltaY_murmuf_{}".format(quadrant, mass_range, lepton_flavor, variation)
                    h_var = inFile.Get(hist_name)
                    if not h_var:
                        print("Missing histogram for variation: {}".format(hist_name))
                        continue
                    Matrix.SetBinContent(1 if "N" in quadrant else 2, 1 if quadrant.endswith("N") else 2, h_var.Integral())

                projection_1 = Matrix.ProjectionX("px1_murmuf_{}".format(variation), 1, 1)
                projection_2 = Matrix.ProjectionX("px2_murmuf_{}".format(variation), 2, 2)

                norm_1 = projection_1.GetBinContent(1) / nominal_projections[0].GetBinContent(1)
                norm_2 = projection_2.GetBinContent(1) / nominal_projections[1].GetBinContent(1)

            hist_scaleUp_1 = nominal_projections[0].Clone("TTbar_1_murmufUp")
            hist_scaleDown_1 = nominal_projections[0].Clone("TTbar_1_murmufDown")
            
            hist_scaleUp_2 = nominal_projections[1].Clone("TTbar_2_murmufUp")
            hist_scaleDown_2 = nominal_projections[1].Clone("TTbar_2_murmufDown")

            for bin_idx in range(1, nominal_projections[0].GetNbinsX() + 1):
                max_val = min_val = nominal_projections[0].GetBinContent(bin_idx)
                scaled_val_1 = projection_1.GetBinContent(bin_idx) / norm_1
                max_val = max(max_val, scaled_val_1)
                min_val = min(min_val, scaled_val_1)
                hist_scaleUp_1.SetBinContent(bin_idx, max_val)
                hist_scaleDown_1.SetBinContent(bin_idx, min_val)

            for bin_idx in range(1, nominal_projections[1].GetNbinsX() + 1):
                max_val = min_val = nominal_projections[1].GetBinContent(bin_idx)
                scaled_val_2 = projection_2.GetBinContent(bin_idx) / norm_2
                max_val = max(max_val, scaled_val_2)
                min_val = min(min_val, scaled_val_2)
                hist_scaleUp_2.SetBinContent(bin_idx, max_val)
                hist_scaleDown_2.SetBinContent(bin_idx, min_val)

            combine_file.cd()
            hist_scaleUp_1.Write()
            hist_scaleDown_1.Write()
            hist_scaleUp_2.Write()
            hist_scaleDown_2.Write()

            
        else:
            print("Processing sample for murmuf: ", sample)
        
            h_nominal = inFile.Get("DeltaY_reco_SystVariations_{}_{}/DeltaY".format(mass_range, lepton_flavor))
            scales = {}
            if not h_nominal:
                print("Nominal histogram for {} not found.".format(sample))
                continue

            for variation in v_variations:
                variation_hist = inFile.Get("DeltaY_reco_SystVariations_{}_{}/DeltaY_murmuf_{}".format(mass_range, lepton_flavor, variation))
                
                if variation_hist:
                    scales[variation] = variation_hist.GetBinContent(1) / h_nominal.GetBinContent(1)
                else:
                    print("Histogram for variation '{}' not found in {}".format(var, sample))

            hist_scaleUp = h_nominal.Clone(sample + "_murmufUp")
            hist_scaleDown = h_nominal.Clone(sample + "_murmufDown")

            # apply scales and find max/min for each bin
            for bin_idx in range(1, h_nominal.GetNbinsX() + 1):
                max_val = h_nominal.GetBinContent(bin_idx)
                min_val = h_nominal.GetBinContent(bin_idx)
                for var, scale in scales.items():
                    var_hist = inFile.Get("DeltaY_reco_SystVariations_{}_{}/DeltaY_murmuf_{}".format(mass_range, lepton_flavor, var))
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
        inFile = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sample), "READ")
        if not inFile:
            print("Input file for {} not found.".format(sample))
            continue
        combine_file.cd()

        if sample == "Diboson":
            for i in range(1, 101):
                nominal_hist_name = "DeltaY_reco_{}_{}_General/DeltaY_reco".format(mass_range, lepton_flavor)
                nominal = inFile.Get(nominal_hist_name) 
                if not nominal:
                    print("Nominal histogram for Diboson not found.")
                    continue
                
                hist_pdfUp = nominal.Clone("Diboson_PDF_{}Up".format(i))
                hist_pdfDown = nominal.Clone("Diboson_PDF_{}Down".format(i))
                hist_pdfUp.Write()
                hist_pdfDown.Write()


        if sample == "TTbar":
            print("Processing TTbar for PDF: ", sample)
            
            Matrix_nominal = TH2D("Matrix_nominal", "", 2, -2.5, 2.5, 2, -2.5, 2.5)
            for quadrant in ["P_P", "P_N", "N_P", "N_N"]:
                hist_name = "DY_{}_{}_{}_General/DeltaY_reco".format(quadrant, mass_range, lepton_flavor)
                h_var = inFile.Get(hist_name)
                if not h_var:
                    print("Missing histogram for quadrant: {}".format(quadrant))
                    continue
                Matrix_nominal.SetBinContent(1 if "N" in quadrant else 2, 1 if quadrant.endswith("N") else 2, h_var.Integral())

            projection_1 = Matrix_nominal.ProjectionX("px_1", 1, 1)
            projection_2 = Matrix_nominal.ProjectionX("px_2", 2, 2)

            
            for i in range(1, 101):  
                Matrix = TH2D("Matrix_PDF_{}".format(i), "", 2, -2.5, 2.5, 2, -2.5, 2.5)
                for quadrant in ["P_P", "P_N", "N_P", "N_N"]:
                    hist_name = "DeltaY_reco_PDFVariations_{}_{}_{}/DeltaY_PDF_{}".format(quadrant, mass_range, lepton_flavor, i)
                    h_var = inFile.Get(hist_name)
                    if h_var:
                        Matrix.SetBinContent(1 if "N" in quadrant else 2, 1 if quadrant.endswith("N") else 2, h_var.Integral())
                    else:
                        print("Missing histogram for PDF variation: {}".format(hist_name))
                        continue

                ProjX_1 = Matrix.ProjectionX("px1_PDF_{}".format(i), 1, 1)
                ProjX_2 = Matrix.ProjectionX("px2_PDF_{}".format(i), 2, 2)
                
                hist_1_pdfUp = ProjX_1.Clone("TTbar_1_PDF_{}Up".format(i))
                hist_1_pdfDown = ProjX_1.Clone("TTbar_1_PDF_{}Down".format(i))
                
                hist_2_pdfUp = ProjX_2.Clone("TTbar_2_PDF_{}Up".format(i))
                hist_2_pdfDown = ProjX_2.Clone("TTbar_2_PDF_{}Down".format(i))

                
                for bin_idx in range(1, ProjX_1.GetNbinsX() + 1):
                    nominal_bin_content_1 = projection_1.GetBinContent(bin_idx)
                    bin_content_1 = ProjX_1.GetBinContent(bin_idx)
                    deviation_1 = bin_content_1 - nominal_bin_content_1
                    hist_1_pdfUp.SetBinContent(bin_idx, nominal_bin_content_1 + deviation_1)
                    hist_1_pdfDown.SetBinContent(bin_idx, nominal_bin_content_1 - deviation_1)

                for bin_idx in range(1, ProjX_2.GetNbinsX() + 1):
                    nominal_bin_content_2 = projection_2.GetBinContent(bin_idx)
                    bin_content_2 = ProjX_2.GetBinContent(bin_idx)
                    deviation_2 = bin_content_2 - nominal_bin_content_2
                    hist_2_pdfUp.SetBinContent(bin_idx, nominal_bin_content_2 + deviation_2)
                    hist_2_pdfDown.SetBinContent(bin_idx, nominal_bin_content_2 - deviation_2)

                hist_1_pdfUp.Write()
                hist_1_pdfDown.Write()
                
                hist_2_pdfUp.Write()
                hist_2_pdfDown.Write()
                    
                
        
        else:
            
            nominal = inFile.Get("DeltaY_reco_{}_{}_General/DeltaY_reco".format(mass_range, lepton_flavor))
            if not nominal:
                print("Nominal histogram for {} not found.".format(sample))
                continue

            for i in range(1, 101):
                pdf_hist = inFile.Get("DeltaY_reco_PDFVariations_{}_{}/DeltaY_PDF_{}".format(mass_range, lepton_flavor, i))
                if pdf_hist:
                    hist_pdfUp = pdf_hist.Clone("{}_PDF_{}Up".format(sample, i))
                    hist_pdfDown = pdf_hist.Clone("{}_PDF_{}Down".format(sample, i))
                    
                    for bin_idx in range(1, nominal.GetNbinsX() + 1):
                        nominal_bin_content = nominal.GetBinContent(bin_idx)
                        bin_content = pdf_hist.GetBinContent(bin_idx)
                        deviation = bin_content - nominal_bin_content

                        hist_pdfUp.SetBinContent(bin_idx, nominal_bin_content + deviation)
                        hist_pdfDown.SetBinContent(bin_idx, nominal_bin_content - deviation)

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
            sys_file = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}_{}/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sys_variation, sample), "READ")
            if not sys_file:
                print("Input file for {} variation {} not found.".format(sample, sys_variation))
                continue
            
            combine_file.cd()

            if sample == "TTbar":
                print("Processing TTbar for {} ".format(sys_variation))
                
                Matrix = TH2D("Matrix_{}".format(sys_variation), "", 2, -2.5, 2.5, 2, -2.5, 2.5)
                
                for quadrant in ["P_P", "P_N", "N_P", "N_N"]:
                    hist_name = "DY_{}_{}_{}_General/DeltaY_reco".format(quadrant, mass_range, lepton_flavor)
                    h_var = sys_file.Get(hist_name)
                    if h_var:
                        Matrix.SetBinContent(1 if "N" in quadrant else 2, 1 if quadrant.endswith("N") else 2, h_var.Integral())
                    else:
                        print("Missing histogram for {}: {}".format(sys_variation, hist_name))

                ProjX_1 = Matrix.ProjectionX("px1_{}".format(sys_variation), 1, 1)
                ProjX_2 = Matrix.ProjectionX("px2_{}".format(sys_variation), 2, 2)

                output_name_1 = "TTbar_1_{}".format(sys_variation.split('_')[0].lower() + sys_variation.split('_')[1].capitalize())
                output_name_2 = "TTbar_2_{}".format(sys_variation.split('_')[0].lower() + sys_variation.split('_')[1].capitalize())


                ProjX_1.Write(output_name_1)
                ProjX_2.Write(output_name_2)
                
            else:
                print("Processing {} for {} ".format(sample, sys_variation))
                hist_name = "DeltaY_reco_{}_{}_General/DeltaY_reco".format(mass_range, lepton_flavor)
                jer_jec_hist = sys_file.Get(hist_name)
                if jer_jec_hist:
                    jer_jec_hist.Clone("{}_{}".format(sample, sys_variation.split('_')[0].lower() + sys_variation.split('_')[1].capitalize())).Write()
                
                else:
                    print("Missing histogram for {}: {}".format(sample, hist_name))
            sys_file.Close()



sys_variations = ["JEC_up", "JEC_down", "JER_up", "JER_down"]

v_samples = ["TTbar", "WJets", "ST", "QCD", "DY", "Diboson"]
v_variations = ["upup", "upnone", "noneup", "nonedown", "downnone", "downdown"]

getEnvelope(inputDir, v_samples, v_variations, combine_file, nominal_projections)

processPDF(inputDir, v_samples, combine_file)

processJERJEC(inputDir, v_samples, combine_file, sys_variations)

combine_file.Close()



#  For TTbar samples, the nominal histograms are not directly in the input file. The projection histograms I making in the script will be my 2 nominal histograms (TTbar_1 and TTbar_2). I want to save these histograms in the output file as nominal histograms. Additionally, I would like to apply the w