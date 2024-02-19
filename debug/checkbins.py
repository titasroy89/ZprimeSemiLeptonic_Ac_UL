import ROOT

def check_entries_below_x(root_file_path, folder_path, histogram_name, x_value):
    f = ROOT.TFile(root_file_path, "READ")

    f.cd(folder_path)
    
    # Retrieve the histogram
    hist = ROOT.gDirectory.Get(histogram_name)
    if not hist:
        print "Histogram %s not found in folder %s" % (histogram_name, folder_path)
        f.Close()
        return

    bin_number = hist.FindBin(x_value)
    

    entries_below_x = hist.Integral(0, bin_number) 
    
    print "Number of entries below %s: %s" % (x_value, entries_below_x)

    f.Close()

# Example usage
root_file_path = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFTvsUL/output_EFT/Preselection/workdir_EFT_preselection_HT800_finalversion/uhh2.AnalysisModuleRunner.MC.EFT_sample_UL18_0.root"  # Change this to your ROOT file path
folder_path = "MET_General"   
histogram_name = "pt_mu"       
x_value = 10                        

# Call the function
check_entries_below_x(root_file_path, folder_path, histogram_name, x_value)
