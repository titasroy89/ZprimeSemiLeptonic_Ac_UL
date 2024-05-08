from ROOT import *
import os
import sys
import math
from optparse import OptionParser
from ROOT import TH1D
import math
      

parser = OptionParser()
parser.add_option("-y", "--year", dest="year", help="Specify the year (UL18, UL17, preUL16, postUL16)", type='str')
parser.add_option("-m", "--mass_range", dest="mass_range", help="Specify the mass range (0_500, 500_750, 750-1000, 1000-1500, 1500Inf)", type='str')
parser.add_option("-l", "--lepton_flavor", dest="lepton_flavor", help="Specify the lepton flavor (electron, muon)", type='str')

(options, args) = parser.parse_args()

year = options.year if options.year else "UL18"  # default value if not specified
mass_range = options.mass_range if options.mass_range else "1000_1500"  # default value if not specified
lepton_flavor = options.lepton_flavor if options.lepton_flavor else "muon"  # default value if not specified


# finalState = options.channel

inputDir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/{}/".format(year)
combine_file_name = 'dY_{}_{}_{}_SR.root'.format(year, lepton_flavor, mass_range)
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
    inFile = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}_latest_dY/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sample), "READ")
    if not inFile:
        print("Input file for {} not found.".format(sample))
        continue
    
    combine_file.cd()

    
    if sample == "DATA":
        # print("in data loop, sample: ", sample)
        print("Processing sample for other sys: ", sample)
        data_obs = inFile.Get("DeltaY_reco_{}_{}_data_General/DeltaY_reco".format(mass_range, lepton_flavor)).Clone("data_obs")
        data_obs.Write("data_obs")
        
    elif sample == "TTbar":
        print("Processing sample for other sys: ", sample)
        path_nom = "DeltaY_reco_SystVariations_ttbar_{}_{}_SR/DeltaY_tt".format(mass_range, lepton_flavor)
                
        # Retrieving the response matrix directly
        Matrix = inFile.Get(path_nom)
        if not Matrix:
            print("Response matrix not found for TTbar.")
            continue
        
        ProjX_1 = Matrix.ProjectionX("TTbar_1", 1, 1)
        ProjX_2 = Matrix.ProjectionX("TTbar_2", 2, 2)

        ProjX_1.GetXaxis().SetTitle("#Delta_Y_{reco}")
        ProjX_2.GetXaxis().SetTitle("#Delta_Y_{reco}")

        nominal_projections = [ProjX_1, ProjX_2]
        
        Matrix.Write()
        ProjX_1.Write("TTbar_1")
        ProjX_2.Write("TTbar_2")
        
        
        for sys, new_sys_name in systematic_name_mapping.items():
            print sys
            for variation in ["up", "down"]:
                
                # Retrieve matrices for systematic variations
                matrix_path = "DeltaY_reco_SystVariations_ttbar_{}_{}_SR/DeltaY_{}_{}_tt".format(mass_range, lepton_flavor, sys,variation)
                Matrix_var = inFile.Get(matrix_path)
                if not Matrix_var:
                    print("Response matrix for systematic {} variation {} not found.").format(sys, variation)
                    continue
                

                ProjX_1 = Matrix.ProjectionX("TTbar_1_{}_{}".format(new_sys_name, variation), 1, 1)
                ProjX_2 = Matrix.ProjectionX("TTbar_2_{}_{}".format(new_sys_name, variation), 2, 2)

                ProjX_1.GetXaxis().SetTitle("#Delta_Y_{reco}")
                ProjX_2.GetXaxis().SetTitle("#Delta_Y_{reco}")

                output_hist_1 = "TTbar_1_{}{}".format(new_sys_name, variation.capitalize())
                output_hist_2 = "TTbar_2_{}{}".format(new_sys_name, variation.capitalize())

                ProjX_1.Write(output_hist_1)
                ProjX_2.Write(output_hist_2)

    else:
        print("Processing sample for other sys: ", sample)
        
        h_nominal = inFile.Get("DeltaY_reco_SystVariations_{}_{}_SR/DeltaY".format(mass_range, lepton_flavor)).Clone(sample)
        h_nominal.Write(sample)
        
        
        for sys, new_sys_name in systematic_name_mapping.items():
            print sys
            
            for variation in ["up", "down"]:
                sys_hist_name = "DeltaY_{}_{}".format(sys, variation)
                sys_hist = inFile.Get("DeltaY_reco_SystVariations_{}_{}_SR/".format(mass_range, lepton_flavor) + sys_hist_name)
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

def calculate_envelope(projection, nominal_projection, norm, up_name, down_name):
    hist_scale_up = nominal_projection.Clone(up_name)
    hist_scale_down = nominal_projection.Clone(down_name)
    
    for bin_idx in range(1, nominal_projection.GetNbinsX() + 1):
        scaled_val = projection.GetBinContent(bin_idx) / norm
        max_val = max(nominal_projection.GetBinContent(bin_idx), scaled_val)
        min_val = min(nominal_projection.GetBinContent(bin_idx), scaled_val)
        hist_scale_up.SetBinContent(bin_idx, max_val)
        hist_scale_down.SetBinContent(bin_idx, min_val)

    return hist_scale_up, hist_scale_down

def getEnvelope(inputDir, v_samples, v_variations, combine_file):
    
    print(" ----------------- murmuf processing ----------------")

    
    for sample in v_samples:
        inFile = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}_latest_dY/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sample), "READ")       
        if not inFile:
            print("Input file for {} not found.".format(sample))
            continue
        combine_file.cd()
        
        
        if sample == "TTbar":
        
            print("Processing sample for murmuf: ", sample)
            
            # path = "DeltaY_reco_SystVariations_ttbar_{}_{}_SR/DeltaY_tt".format(mass_range, lepton_flavor)
            # nominal_matrix = inFile.Get(path)
            
            # # nominal_matrix = inFile.Get("DeltaY_reco_SystVariations_ttbar_{}_{}_SR/DeltaY_tt").format(mass_range, lepton_flavor)
            # if not nominal_matrix:
            #     print("Nominal matrix not found for TTbar.")
            #     continue
            # proj1_nominal = nominal_matrix.ProjectionX("TTbar_1", 1, 1)
            # proj2_nominal = nominal_matrix.ProjectionX("TTbar_2", 2, 2)

        
            for variation in v_variations:
                path_var = "DeltaY_reco_SystVariations_ttbar_{}_{}_SR/DeltaY_murmuf_{}_tt".format(mass_range, lepton_flavor, variation)
                matrix_var = inFile.Get(path_var)
                # matrix_var = inFile.Get("DeltaY_reco_SystVariations_ttbar_{}_{}_SR/DeltaY_murmuf_{}_tt").format(mass_range, lepton_flavor, variation)
               
                if not matrix_var:
                    print("Missing matrix for variation: {}").format(variation)
                    continue
                
                proj1_var = matrix_var.ProjectionX("TTbar_1_murmuf_{}".format(variation), 1, 1)
                proj2_var = matrix_var.ProjectionX("TTbar_2_murmuf_{}".format(variation), 2, 2)
                
                # Create up and down histograms by applying symmetric manipulation
                proj1_up_name = "TTbar_1_{}Up".format(variation)
                proj1_down_name = "TTbar_1_{}Down".format(variation)
                proj2_up_name = "TTbar_2_{}Up".format(variation)
                proj2_down_name = "TTbar_2_{}Down".format(variation)
                
                pdf_proj1_up = ProjX_1.Clone(proj1_up_name)
                pdf_proj2_up = ProjX_2.Clone(proj1_down_name)
                pdf_proj1_down = ProjX_1.Clone(proj2_up_name)
                pdf_proj2_down = ProjX_2.Clone(proj2_down_name)


                for bin_idx in range(1, ProjX_1.GetNbinsX() + 1):
                    
                    scaling_factor_1 = proj1_var.GetBinContent(bin_idx) / ProjX_1.GetBinContent(bin_idx) if ProjX_1.GetBinContent(bin_idx) != 0 else 1
                    scaling_factor_2 = proj2_var.GetBinContent(bin_idx) / ProjX_2.GetBinContent(bin_idx) if ProjX_2.GetBinContent(bin_idx) != 0 else 1
                
                    pdf_proj1_up.SetBinContent(bin_idx, ProjX_1.GetBinContent(bin_idx) * (1 + abs(1 - scaling_factor_1)))
                    pdf_proj1_down.SetBinContent(bin_idx, ProjX_1.GetBinContent(bin_idx) * (1 - abs(1 - scaling_factor_1)))
                    pdf_proj2_up.SetBinContent(bin_idx, ProjX_2.GetBinContent(bin_idx) * (1 + abs(1 - scaling_factor_2)))
                    pdf_proj2_down.SetBinContent(bin_idx, ProjX_2.GetBinContent(bin_idx) * (1 - abs(1 - scaling_factor_2)))

                pdf_proj1_up.Write()
                pdf_proj2_up.Write()
                pdf_proj1_down.Write()
                pdf_proj2_down.Write()
            
        else:
            print("Processing sample for murmuf: ", sample)
            
            # pdf_nominal_path = "DeltaY_reco_SystVariations_{}_{}_SR/DeltaY".format(mass_range, lepton_flavor)
        
            # h_nominal = inFile.Get(pdf_nominal_path)
            # if not h_nominal:
            #     print("Nominal histogram for {} not found.".format(sample))
            #     continue

            for variation in v_variations:
                variation_hist = inFile.Get("DeltaY_reco_SystVariations_{}_{}_SR/DeltaY_murmuf_{}".format(mass_range, lepton_flavor, variation))
                
                if not variation_hist:
                    print("Histogram for variation '{}' not found in {}").format(variation, sample)
                    continue
                
                variation_hist_up_name = "{}_{}Up".format(sample, variation)
                variation_hist_down_name = "{}_{}Down".format(sample, variation)
                variation_hist_up = h_nominal.Clone(variation_hist_up_name)
                variation_hist_down = h_nominal.Clone(variation_hist_down_name)

                for bin_idx in range(1, h_nominal.GetNbinsX() + 1):
                    scaling_factor = variation_hist.GetBinContent(bin_idx) / h_nominal.GetBinContent(bin_idx) if h_nominal.GetBinContent(bin_idx) != 0 else 1
                    variation_hist_up.SetBinContent(bin_idx, h_nominal.GetBinContent(bin_idx) * (1 + abs(1 - scaling_factor)))
                    variation_hist_down.SetBinContent(bin_idx, h_nominal.GetBinContent(bin_idx) * (1 - abs(1 - scaling_factor)))

                variation_hist_up.Write()
                variation_hist_down.Write()


        inFile.Close()


############ 
# ----------------- PDFs (100) ----------------
############ 

# Function to calculate and write RMS based histograms
def calculate_and_write_rms_histograms(projections, nominal_projection, hist_name):
    
    pdf_up_name = "{}_pdfUp".format(hist_name)
    pdf_down_name = "{}_pdfDown".format(hist_name)
    
    hist_pdf_up = TH1D(pdf_up_name, "", nominal_projection.GetNbinsX(), nominal_projection.GetXaxis().GetXmin(), nominal_projection.GetXaxis().GetXmax())
    hist_pdf_down = TH1D(pdf_down_name, "", nominal_projection.GetNbinsX(), nominal_projection.GetXaxis().GetXmin(), nominal_projection.GetXaxis().GetXmax())

    for bin_idx in range(1, nominal_projection.GetNbinsX() + 1):
        nominal_val = nominal_projection.GetBinContent(bin_idx)
        values = projections.GetBinContent(bin_idx)
        rms = math.sqrt(sum((x - nominal_val) ** 2 for x in values) / len(values))
        
        hist_pdf_up.SetBinContent(bin_idx, nominal_val + rms)
        hist_pdf_down.SetBinContent(bin_idx, nominal_val - rms)

    combine_file.cd()
    hist_pdf_up.Write()
    hist_pdf_down.Write()


def processPDF(inputDir, v_samples, combine_file):
    print(" ----------------- PDFs processing ----------------")
    
    
    for sample in v_samples:
        inFile = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}_latest_dY/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sample), "READ")
        if not inFile:
            print("Input file for {} not found.".format(sample))
            continue
        combine_file.cd()

        if sample == "Diboson":
                nominal_hist_name = "DeltaY_reco_{}_{}_SR_General/DeltaY_reco".format(mass_range, lepton_flavor)
                nominal = inFile.Get(nominal_hist_name) 
                if not nominal:
                    print("Nominal histogram for Diboson not found.")
                    continue
                
                hist_pdfUp = nominal.Clone("Diboson_pdfUp")
                hist_pdfDown = nominal.Clone("Diboson_pdfDown")
                hist_pdfUp.Write()
                hist_pdfDown.Write()


        elif sample == "TTbar":
            print("Processing TTbar for PDF: ", sample)
            
            # Step 1: Retrieve the nominal matrix and create projections
            
            # nom_mat_path = "DY_ttbar_{}_{}_SR_General/response_matrix".format(mass_range, lepton_flavor)
            # nominal_matrix = inFile.Get(nom_mat_path)
            # if not nominal_matrix:
            #     print("Nominal matrix not found for TTbar.")
            # else:
            # proj1_nominal = nominal_matrix.ProjectionX("px1_nominal", 1, 1)
            # proj2_nominal = nominal_matrix.ProjectionX("px2_nominal", 2, 2)
            
            # print("proj1_nominal 1: ", proj1_nominal.GetBinContent(1)) 
            # print("proj1_nominal 2: ", proj1_nominal.GetBinContent(2)) 
            
            # print("proj2_nominal 1: ", proj2_nominal.GetBinContent(1)) 
            # print("proj2_nominal 2: ", proj2_nominal.GetBinContent(2)) 
            
            # Process PDF variations
            pdf_projections_1 = []
            pdf_projections_2 = []
            
            for i in range(1, 101):  
                weight_matrix_path = "DeltaY_reco_PDFVariations_ttbar_{}_{}_SR/DeltaY_PDF_RM_{}".format(mass_range, lepton_flavor, i)
                weight_matrix = inFile.Get(weight_matrix_path)
                if not weight_matrix:
                    print("PDF weight matrix {} not found.").format(i)
                    continue
                
                # Projections for the PDF weight
                
                # weight_proj1 = weight_matrix.ProjectionX("weight_TTbar_1_pdf_{}".format(i), 1, 1)
                # weight_proj2 = weight_matrix.ProjectionX("weight_TTbar_2_pdf_{}".format(i), 2, 2)
                
                # pdf_projections_1.append(weight_proj1)
                # pdf_projections_2.append(weight_proj2)
                
                pdf_projections_1.append(weight_matrix.ProjectionX("px1_pdf_{}".format(i), 1, 1))
                pdf_projections_2.append(weight_matrix.ProjectionX("px2_pdf_{}".format(i), 2, 2))
                
                # Create histograms for up and down variations by applying the weight symmetrically
                pdf_proj1_up = ProjX_1.Clone("TTbar_1_pdf_{}_up".format(i))
                pdf_proj2_up = ProjX_2.Clone("TTbar_2_pdf_{}_up".format(i))
                pdf_proj1_down = ProjX_1.Clone("TTbar_1_pdf_{}_down".format(i))
                pdf_proj2_down = ProjX_2.Clone("TTbar_2_pdf_{}_down".format(i))
                
                
                # Calculate RMS and write histograms for both projections
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
                
            hist_pdfUp_1 = TH1D("TTbar_1_pdfUp", "", ProjX_1.GetNbinsX(), ProjX_1.GetXaxis().GetXmin(), ProjX_1.GetXaxis().GetXmax())
            hist_pdfDown_1 = TH1D("TTbar_1_pdfDown", "", ProjX_1.GetNbinsX(), ProjX_1.GetXaxis().GetXmin(), ProjX_1.GetXaxis().GetXmax())
            hist_pdfUp_2 = TH1D("TTbar_2_pdfUp", "", ProjX_2.GetNbinsX(), ProjX_2.GetXaxis().GetXmin(), ProjX_2.GetXaxis().GetXmax())
            hist_pdfDown_2 = TH1D("TTbar_2_pdfDown", "", ProjX_2.GetNbinsX(), ProjX_2.GetXaxis().GetXmin(), ProjX_2.GetXaxis().GetXmax())


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
            
            hist_pdfUp_1.Write()
            hist_pdfDown_1.Write()
            hist_pdfUp_2.Write()
            hist_pdfDown_2.Write()




                # Apply the weight symmetrically to the nominal projection
                # for bin_idx in range(1, ProjX_1.GetNbinsX() + 1):
                    
                #     hist_name_pdf = hist_temp_{}.format(i)
                #     hist_name_pdf = TH1D("hist_name_pdf", "", ProjX_1.GetNbinsX(), ProjX_1.GetXaxis().GetXmin(), ProjX_1.GetXaxis().GetXmax())
                    
                #     hist_name_pdf.GetMean()+
                    
                #     scaling_factor = weight_proj1.GetBinContent(bin_idx) / ProjX_1.GetBinContent(bin_idx) if ProjX_1.GetBinContent(bin_idx) != 0 else 1
                #     print("Scaling factor: ", scaling_factor)
                #     print("UP: ", (1+ abs(1 - scaling_factor)))
                #     print("DOWN: ", (1- abs(1 - scaling_factor)))
                    
                #     pdf_proj1_up.SetBinContent(bin_idx, ProjX_1.GetBinContent(bin_idx) * (1+ abs(1 - scaling_factor)))
                #     pdf_proj1_down.SetBinContent(bin_idx, ProjX_1.GetBinContent(bin_idx) * (1 - abs(1 - scaling_factor)))

                    
                #     # print("Scaling factor: ", 1+ scaling_factor)
                #     # print("Scaling factor: ", 1- scaling_factor)
                #     # print("pdf_proj1_up: ", pdf_proj1_up)
                #     # print("pdf_proj1_down: ", pdf_proj1_down)
                    
                # for bin_idx in range(1, ProjX_2.GetNbinsX() + 1):
                #     scaling_factor = weight_proj2.GetBinContent(bin_idx) / ProjX_2.GetBinContent(bin_idx) if ProjX_2.GetBinContent(bin_idx) != 0 else 1
                    
                #     pdf_proj2_up.SetBinContent(bin_idx, ProjX_2.GetBinContent(bin_idx) * (1 + scaling_factor))
                #     pdf_proj2_down.SetBinContent(bin_idx, ProjX_2.GetBinContent(bin_idx) * (1 - scaling_factor))

                # combine_file.cd()
                # pdf_proj1_up.Write()
                # pdf_proj2_up.Write()
                # pdf_proj1_down.Write()
                # pdf_proj2_down.Write()   
                    
            
 
        else:
            
            print("Processing PDF: ", sample)
            
            # getting the nominal histogram
            # nominal = inFile.Get("DeltaY_reco_{}_{}_SR_General/DeltaY_reco".format(mass_range, lepton_flavor))
            # if not nominal:
            #     print("Nominal histogram for {} not found.").format(sample)
            
            # Process each individual PDF variation (100)
            
            # for i in range(1, 101): 
            #     pdf_hist = inFile.Get("DeltaY_reco_PDFVariations_{}_{}_SR/DeltaY_PDF_{}".format(mass_range, lepton_flavor, i))
            #     if not pdf_hist:
            #         print("PDF histogram for {} not found.").format(sample)
                
            #     pdf_hist_up = h_nominal.Clone("{}_pdf_{}Up".format(sample, i))
            #     pdf_hist_down = h_nominal.Clone("{}_pdf_{}Down".format(sample, i))
 
                
                # normalization scales for each PDF variation
            v_pdf_norm = []
                
            # getting 100 PDFs histograms
            for i in range(1, 101):
                pdf_hist = inFile.Get("DeltaY_reco_PDFVariations_{}_{}_SR/DeltaY_PDF_{}".format(mass_range, lepton_flavor, i))
                if pdf_hist:
                    norm_scale_pdf = pdf_hist.GetBinContent(1) / h_nominal.GetBinContent(1)
                    v_pdf_norm.append(norm_scale_pdf)
                    pdf_hist.Scale(1. / norm_scale_pdf)
                else:
                    print("PDF histogram for {} not found.").format(sample)

            hist_pdfUp = TH1F("{}_pdfUp".format(sample), "{} pdf up variation".format(sample), h_nominal.GetNbinsX(), h_nominal.GetXaxis().GetXmin(), h_nominal.GetXaxis().GetXmax())
            hist_pdfDown = TH1F("{}_pdfDown".format(sample), "{} pdf down variation".format(sample), h_nominal.GetNbinsX(), h_nominal.GetXaxis().GetXmin(), h_nominal.GetXaxis().GetXmax())

            # Calculate RMS for each bin and update up/down histograms
            for bin_idx in range(1, h_nominal.GetNbinsX() + 1):
                sum_bins = 0.
                for j in range(1, 101):
                    pdf_hist = inFile.Get("DeltaY_reco_PDFVariations_{}_{}_SR/DeltaY_PDF_{}".format(mass_range, lepton_flavor, j))
                    bin_content = pdf_hist.GetBinContent(bin_idx)
                    sum_bins += (bin_content - h_nominal.GetBinContent(bin_idx)) ** 2

                rms = math.sqrt(sum_bins / 100)
                hist_pdfUp.SetBinContent(bin_idx, h_nominal.GetBinContent(bin_idx) + rms)
                hist_pdfDown.SetBinContent(bin_idx, h_nominal.GetBinContent(bin_idx) - rms)

            hist_pdfUp.Write()
            hist_pdfDown.Write()



            # for bin_idx in range(1, h_nominal.GetNbinsX() + 1):
            #     scaling_factor = pdf_hist.GetBinContent(bin_idx) / h_nominal.GetBinContent(bin_idx) if h_nominal.GetBinContent(bin_idx) != 0 else 1
            #     pdf_hist_up.SetBinContent(bin_idx, h_nominal.GetBinContent(bin_idx) * (1 + scaling_factor))
            #     pdf_hist_down.SetBinContent(bin_idx, h_nominal.GetBinContent(bin_idx) * (1 - scaling_factor))
            
            # pdf_hist_up.Write()
            # pdf_hist_down.Write()
                
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
            sys_file = TFile.Open(inputDir + "{}/workdir_AnalysisDNN_{}_{}_{}_latest_dY/nominal/{}.root".format(lepton_flavor, year, lepton_flavor, sys_variation, sample), "READ")
            if not sys_file:
                print("Input file for {} variation {} not found.".format(sample, sys_variation))
                continue
            
            combine_file.cd()

            if sample == "TTbar":
                print("Processing TTbar for {} ".format(sys_variation))
                
                matrix_path_jerjec = "DY_ttbar_{}_{}_SR_General/response_matrix".format(mass_range, lepton_flavor)
                Matrix = sys_file.Get(matrix_path_jerjec)
                if not Matrix:
                    print("Nominal matrix not found for TTbar.")
                else:
                    ProjX_1_jerjec = Matrix.ProjectionX("TTbar_1_{}".format(sys_variation), 1, 1)
                    ProjX_2_jerjec = Matrix.ProjectionX("TTbar_2_{}".format(sys_variation), 2, 2)
                
            
                    output_name_1 = "TTbar_1_{}".format(sys_variation.split('_')[0].lower() + sys_variation.split('_')[1].capitalize())
                    output_name_2 = "TTbar_2_{}".format(sys_variation.split('_')[0].lower() + sys_variation.split('_')[1].capitalize())

                    ProjX_1_jerjec.Write(output_name_1)
                    ProjX_2_jerjec.Write(output_name_2)
                
            else:
                print("Processing {} for {} ".format(sample, sys_variation))
                hist_name = "DeltaY_reco_{}_{}_SR_General/DeltaY_reco".format(mass_range, lepton_flavor)
                jer_jec_hist = sys_file.Get(hist_name)
                if jer_jec_hist:
                    jer_jec_hist.Clone("{}_{}".format(sample, sys_variation.split('_')[0].lower() + sys_variation.split('_')[1].capitalize())).Write()
                
                else:
                    print("Missing histogram for {}: {}".format(sample, hist_name))
            sys_file.Close()



sys_variations = ["JEC_up", "JEC_down", "JER_up", "JER_down"]

v_samples = ["TTbar", "WJets", "ST", "QCD", "DY", "Diboson"]
v_variations = ["upup", "upnone", "noneup", "nonedown", "downnone", "downdown"]

getEnvelope(inputDir, v_samples, v_variations, combine_file)

processPDF(inputDir, v_samples, combine_file)

processJERJEC(inputDir, v_samples, combine_file, sys_variations)

combine_file.Close()



#  For TTbar samples, the nominal histograms are not directly in the input file. The projection histograms I making in the script will be my 2 nominal histograms (TTbar_1 and TTbar_2). I want to save these histograms in the output file as nominal histograms. Additionally, I would like to apply the w