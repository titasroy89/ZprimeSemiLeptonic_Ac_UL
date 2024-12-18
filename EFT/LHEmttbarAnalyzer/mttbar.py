import ROOT
from array import array  
import numpy as np

def overlay_histograms_normalized():
    ROOT.gROOT.SetBatch(True)  # Run in batch mode

    file1 = ROOT.TFile.Open("0_700_root/lhe_0_700.root")
    file2 = ROOT.TFile.Open("700_900_root/lhe_700_900.root")
    file3 = ROOT.TFile.Open("900_Inf_root/lhe_900Inf.root")

    if not file1 or file1.IsZombie():
        print("Error: Cannot open file1.")
        return
    if not file2 or file2.IsZombie():
        print("Error: Cannot open file2.")
        return
    if not file3 or file3.IsZombie():
        print("Error: Cannot open file3.")
        return

    hist1 = file1.Get("LHEMttbarAnalyzer/mttbar").Clone("hist1")
    hist2 = file2.Get("LHEMttbarAnalyzer/mttbar").Clone("hist2")
    hist3 = file3.Get("LHEMttbarAnalyzer/mttbar").Clone("hist3")

    if not hist1:
        print("Error: Cannot find histogram 'mttbar' in file1.")
        return
    if not hist2:
        print("Error: Cannot find histogram 'mttbar' in file2.")
        return
    if not hist3:
        print("Error: Cannot find histogram 'mttbar' in file3.")
        return

    # Cross-section values in pb
    sigma1 = 1.842e+02  # 184.2 pb
    sigma2 = 2.484e+01  # 24.84 pb
    sigma3 = 4.525e+01  # 45.25 pb

    # Integrated luminosity in pb^{-1} (2017 data)
    lumi = 41800  # 41.8 fb^{-1} = 41800 pb^{-1}

    # Get the effective number of generated events
    N_gen1 = hist1.GetSumOfWeights()
    N_gen2 = hist2.GetSumOfWeights()
    N_gen3 = hist3.GetSumOfWeights()

    # print("Integral of hist1 before scaling: {}.Integral()".format(hist1))
    # print("Integral of hist2 before scaling: {}.Integral()".format(hist2))
    # print("Integral of hist3 before scaling: {}.Integral()".format(hist3))

    # Check for zero generated events to prevent division by zero
    if N_gen1 == 0 or N_gen2 == 0 or N_gen3 == 0:
        print("Error: One of the histograms has zero generated events. Cannot scale.")
        return

    scaling_factor1 = (sigma1 * lumi) / N_gen1
    scaling_factor2 = (sigma2 * lumi) / N_gen2
    scaling_factor3 = (sigma3 * lumi) / N_gen3

    print("Scaling factor1: {}".format(scaling_factor1))
    print("Scaling factor2: {}".format(scaling_factor2))
    print("Scaling factor3: {}".format(scaling_factor3))

    hist1.Scale(scaling_factor1)
    hist2.Scale(scaling_factor2)
    hist3.Scale(scaling_factor3)

    # print("Integral of hist1 after scaling: {}.Integral()".format(hist1))
    # print("Integral of hist2 after scaling: {}.Integral()".format(hist2))
    # print("Integral of hist3 after scaling: {}.Integral()".format(hist3))

    normalize = False  # Set to False if you do not want unit area normalization

    if normalize:
        if hist1.Integral() != 0:
            hist1.Scale(1.0 / hist1.Integral())
        else:
            print("Warning: hist1 has zero integral, cannot normalize.")

        if hist2.Integral() != 0:
            hist2.Scale(1.0 / hist2.Integral())
        else:
            print("Warning: hist2 has zero integral, cannot normalize.")

        if hist3.Integral() != 0:
            hist3.Scale(1.0 / hist3.Integral())
        else:
            print("Warning: hist3 has zero integral, cannot normalize.")

    bin_width = 50  # 50 GeV
    mttbar_min = 0
    mttbar_max = 1500
    n_bins = int((mttbar_max - mttbar_min) / bin_width)
    bin_edges = np.linspace(mttbar_min, mttbar_max, n_bins + 1)
    bin_edges_c = array('d', bin_edges)

    hist1_rebinned = hist1.Rebin(n_bins, "hist1_rebinned", bin_edges_c)
    hist2_rebinned = hist2.Rebin(n_bins, "hist2_rebinned", bin_edges_c)
    hist3_rebinned = hist3.Rebin(n_bins, "hist3_rebinned", bin_edges_c)
    
    hist_combined = hist1_rebinned.Clone("hist_combined")
    hist_combined.Add(hist2_rebinned)
    hist_combined.Add(hist3_rebinned)

    hist1_rebinned.SetStats(0)
    hist2_rebinned.SetStats(0)
    hist3_rebinned.SetStats(0)
    hist_combined.SetStats(0)

    #  to normalize the combined histogram to unit area
    integral_combined = hist_combined.Integral()
    if integral_combined != 0:
        hist_combined.Scale(1.0 / integral_combined)
    else:
        print("Combined histogram has zero integral, cannot normalize.")


    hist1_rebinned.SetLineColor(ROOT.kRed)
    hist2_rebinned.SetLineColor(ROOT.kGreen+2)
    hist3_rebinned.SetLineColor(ROOT.kBlue)
    # hist_combined.SetLineColor(ROOT.kOrange+2)

    hist1_rebinned.SetLineWidth(2)
    hist2_rebinned.SetLineWidth(2)
    hist3_rebinned.SetLineWidth(2)
    hist_combined.SetLineWidth(2)

    c1 = ROOT.TCanvas("c1", "Mttbar Distribution", 800, 600)
    c1.SetGrid()

    hist1_rebinned.GetXaxis().SetTitle("Mtt [GeV]")
    hist1_rebinned.GetYaxis().SetTitle("Events")

    # hist1_rebinned.Draw("HIST")
    # hist2_rebinned.Draw("HIST SAME")
    # hist3_rebinned.Draw("HIST SAME")
    hist_combined.Draw("HIST SAME")

    legend = ROOT.TLegend(0.65, 0.75, 0.88, 0.88)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.AddEntry(hist1_rebinned, "Mttbar (0-700 GeV)", "l")
    legend.AddEntry(hist2_rebinned, "Mttbar (700-900 GeV)", "l")
    legend.AddEntry(hist3_rebinned, "Mttbar (900-Inf GeV)", "l")
    # legend.AddEntry(hist_combined, "Total Combined", "l")
    # legend.Draw()

    max_y = max(hist1_rebinned.GetMaximum(), hist2_rebinned.GetMaximum(), hist3_rebinned.GetMaximum())
    hist1_rebinned.SetMaximum(max_y * 1.2)

    c1.SaveAs("mttbar_combined_normalized.png")

    file1.Close()
    file2.Close()
    file3.Close()

if __name__ == "__main__":
    overlay_histograms_normalized()
