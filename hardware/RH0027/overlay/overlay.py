import ROOT

main_file_path = "SCurve_FB.root"
compare_files = [
    "SCurve_RB_5.root",
    "SCurve_RB_10.root",
    "SCurve_RB_20.root",
    "SCurve_RB_30.root",
    "SCurve_RB_50.root",
    "SCurve_RB_80.root"
]

# Scan_n = 'Threshold1D'
Scan_n = 'Noise1D'
H_ID='0'
C_ID='13'

main_file = ROOT.TFile.Open(main_file_path)
compare_files = [ROOT.TFile.Open(file) for file in compare_files]

# Function to extract histogram from canvas
def get_hist_from_canvas(canvas):
    if isinstance(canvas, ROOT.TCanvas):
        prims = canvas.GetListOfPrimitives()
        for obj in prims:
            if isinstance(obj, ROOT.TH1):  # Check if the object is a histogram
                return obj
    return None
main_canvas = main_file.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_"+str(int(C_ID))+"/D_B(0)_O(0)_H(0)_"+Scan_n+"_Chip("+str(int(C_ID))+")")  
compare_canvases = [
    file.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_"+str(int(C_ID))+"/D_B(0)_O(0)_H(0)_"+Scan_n+"_Chip("+str(int(C_ID))+")")
    for file in compare_files
]

# Extract histograms from the canvases
main_hist = get_hist_from_canvas(main_canvas)
compare_hists = [get_hist_from_canvas(canvas) for canvas in compare_canvases]

# print(f"Main Histogram: {main_hist}, Type: {type(main_hist)}")
# for i, hist in enumerate(compare_hists):
#     print(f"Compare Histogram {i+1}: {hist}, Type: {type(hist)}")

if not main_hist:
    raise ValueError("Main histogram not found or not valid. Check the path or file.")
for i, hist in enumerate(compare_hists):
    if not hist:
        raise ValueError(f"Comparison histogram {i+1} not found or not valid. Check the path or file.")

canvas = ROOT.TCanvas("canvas", "Threshold Distribution", 800, 600)

# main_hist.GetXaxis().SetRangeUser(400, 900)  
# main_hist.GetYaxis().SetRangeUser(0, 12000)

main_hist.GetXaxis().SetRangeUser(0, 60)  
main_hist.GetYaxis().SetRangeUser(0, 35000)

main_hist.SetLineColor(ROOT.kBlack)  # Set color for the main histogram
main_hist.SetLineWidth(2)            # Set line width for the main histogram
main_hist.Draw("HIST")               # Draw the main histogram

# Set drawing options and overlay the compare histograms
colors = [ROOT.kRed, ROOT.kBlue, ROOT.kGreen, ROOT.kMagenta, ROOT.kCyan, ROOT.kOrange]

for i, hist in enumerate(compare_hists):
    hist.SetLineColor(colors[i])  
    hist.SetLineWidth(2)          
    hist.Draw("HIST SAME")       


legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)  

if isinstance(main_hist, ROOT.TH1): 
    legend.AddEntry(main_hist, "Forward Bias +0.3V", "l")
else:
    print("Error: Main histogram is not valid for legend entry.")

reverse_bias_labels = ["Reverse Bias -5V", "Reverse Bias -10V", "Reverse Bias -20V", 
                       "Reverse Bias -30V", "Reverse Bias -50V", "Reverse Bias -80V"]

for i, hist in enumerate(compare_hists):
    if isinstance(hist, ROOT.TH1):
        legend.AddEntry(hist, reverse_bias_labels[i], "l")
    else:
        print(f"Error: Compare histogram {i+1} is not valid for legend entry.")

legend.Draw()

# main_hist.GetXaxis().SetTitle("X-axis Title") 
# main_hist.GetYaxis().SetTitle("Y-axis Title")  

canvas.Update()

canvas.SaveAs("overlay_plot_noise_13.pdf") 

# input("Press Enter to exit...")
