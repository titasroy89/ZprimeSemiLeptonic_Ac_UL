import ROOT

ROOT.gROOT.SetBatch(True)

def plot_histogram_with_new_xaxis_range(root_file_path, folder_path, histogram_name, new_x_min, new_x_max, output_canvas_name):
    f = ROOT.TFile(root_file_path, "READ")

    f.cd(folder_path)
    
    hist = ROOT.gDirectory.Get(histogram_name)
    if not hist:
        print "Histogram %s not found in folder %s" % (histogram_name, folder_path)
        f.Close()
        return

    canvas = ROOT.TCanvas("canvas", "Canvas for Histogram", 800, 600)

    hist.GetXaxis().SetLimits(new_x_min, new_x_max)
    
    hist.Draw()

    canvas.SaveAs(output_canvas_name)

    f.Close()

root_file_path = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFTvsUL/output_EFT/Preselection/workdir_EFT_preselection_HT800_finalversion/uhh2.AnalysisModuleRunner.MC.EFT_sample_UL18_0.root"  # Change this to your ROOT file path
folder_path = "MET_General"   
histogram_name = "mttbar"       
new_x_min = 0                           
new_x_max = 3000                            
output_canvas_name = "modified_mttbar.png"  

plot_histogram_with_new_xaxis_range(root_file_path, folder_path, histogram_name, new_x_min, new_x_max, output_canvas_name)
