import ROOT
from array import array

def getEnvelope():
    uhh2_basedir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/combine_allyears/UL18/muon/afterDNN/750_1000/combine_input/"
    file_dir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/"

    v_years = ["UL18"]
    v_channels = ["muon"]
    v_samples = ["TTbar", "WJets", "ST", "QCD", "DY", "Diboson"]
    v_variations = ["upup", "upnone", "noneup", "nonedown", "downnone", "downdown"]
    v_root_directories = ["DeltaY_reco_SystVariations_750_1000_muon"]


    for year in v_years:
        print("year: ", year)

        for channel in v_channels:
            print("channel: ", channel)

            for i, sample in enumerate(v_samples):
                print(sample)

                file_name = file_dir + "muon/workdir_AnalysisDNN_UL18_muon_sys_all/nominal/" + sample + ".root"
                f_in = ROOT.TFile.Open(file_name, "READ")
                v_variation_norms = []

                nominal_hist = f_in.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY")
                if not nominal_hist:
                    print "Nominal histogram for %s not found." % sample
                    continue  # Skip this sample
                
                for variation in v_variations:

                    variation_hist_name = "DeltaY_reco_SystVariations_750_1000_muon/DeltaY_murmuf_" + variation
                    variation_hist = f_in.Get(variation_hist_name)
                    if not variation_hist:
                        print "Variation histogram '%s' for %s not found." % (variation_hist_name, sample)
                        continue  # Skip this variation
                    
                    norm = variation_hist.GetBinContent(1) / nominal_hist.GetBinContent(1)
                    v_variation_norms.append(norm)
                
                f_out = ROOT.TFile(uhh2_basedir + "/" + sample + ".root", "RECREATE")

                for output_root_directory in v_root_directories:
                    h_nominal = f_in.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY")
                    h_scale_up = h_nominal.Clone()
                    h_scale_down = h_nominal.Clone()

                    # Loop over each bin of the histograms
                    for a in range(1, h_nominal.GetNbinsX() + 1):
                        scale_max = 0.
                        scale_min = 10000000000.
                        
                        for b, variation in enumerate(v_variations):
                            vars = "DeltaY_reco_SystVariations_750_1000_muon/DeltaY_murmuf_" + variation
                            bin_content = f_in.Get(vars).GetBinContent(a) / v_variation_norms[b]
                            scale_max = max(scale_max, bin_content)
                            scale_min = min(scale_min, bin_content)

                        h_scale_up.SetBinContent(a, scale_max)
                        h_scale_down.SetBinContent(a, scale_min)


                    f_out.mkdir(output_root_directory)
                    f_out.cd(output_root_directory)
                    h_nominal.SetName("DeltaY")
                    h_scale_up.SetName("MurMufUp")
                    h_scale_down.SetName("MurMufDown")


                    h_scale_up.Write()
                    h_scale_down.Write()

                f_in.Close()
                f_out.Close()

getEnvelope()
