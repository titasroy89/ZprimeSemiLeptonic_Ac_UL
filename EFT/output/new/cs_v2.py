import ROOT
import numpy as np

def overlay_histograms_normalized():
    # Open ROOT files
    file1 = ROOT.TFile.Open("mttbar_multiprocess_0_700.root")
    file2 = ROOT.TFile.Open("mttbar_multiprocess_700_900.root")
    file3 = ROOT.TFile.Open("mttbar_multiprocess_900Inf.root")

    # Get histograms
    hist1 = file1.Get("hist_mttbar_reconstructed")
    hist2 = file2.Get("hist_mttbar_total")
    hist3 = file3.Get("hist_mttbar_total")

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

    # Calculate scaling factors
    scaling_factor1 = (sigma1 * lumi) / N_gen1
    scaling_factor2 = (sigma2 * lumi) / N_gen2
    scaling_factor3 = (sigma3 * lumi) / N_gen3

    # Scale histograms
    hist1.Scale(scaling_factor1)
    hist2.Scale(scaling_factor2)
    hist3.Scale(scaling_factor3)

    # Define bin edges for combined histogram (from 0 to maximum mttbar value)
    bin_width = 50  # 50 GeV bin width
    mttbar_min = 0
    mttbar_max = 1500  # Adjust as needed based on your data
    n_bins = int((mttbar_max - mttbar_min) / bin_width)
    bin_edges = np.linspace(mttbar_min, mttbar_max, n_bins + 1)

    # Create the combined histogram with the desired binning
    hist_combined = ROOT.TH1F("hist_combined", "Mttbar Distribution", n_bins, bin_edges)

    # Rebin individual histograms to match the combined histogram binning
    # Optionally, if histograms already have appropriate binning, this step may be skipped
    hist1_rebinned = hist1.Rebin(n_bins, "hist1_rebinned", bin_edges)
    hist2_rebinned = hist2.Rebin(n_bins, "hist2_rebinned", bin_edges)
    hist3_rebinned = hist3.Rebin(n_bins, "hist3_rebinned", bin_edges)

    # Add the rebinned histograms to the combined histogram
    hist_combined.Add(hist1_rebinned)
    hist_combined.Add(hist2_rebinned)
    hist_combined.Add(hist3_rebinned)

    # Optional: Normalize the combined histogram to unit area
    # Comment this out if you want to keep the absolute event counts
    # integral_combined = hist_combined.Integral()
    # if integral_combined != 0:
    #     hist_combined.Scale(1.0 / integral_combined)
    # else:
    #     print("Combined histogram has zero integral, cannot normalize.")

    # Set histogram styles
    hist_combined.SetLineColor(ROOT.kBlue)
    hist_combined.SetLineWidth(2)
    hist_combined.SetStats(0)

    # Create canvas
    c1 = ROOT.TCanvas("c1", "Mttbar Distribution", 800, 600)
    c1.SetGrid()

    # Draw the combined histogram
    hist_combined.Draw("HIST")

    # Set axis titles
    hist_combined.GetXaxis().SetTitle("Mttbar [GeV]")
    hist_combined.GetYaxis().SetTitle("Events")
    hist_combined.SetTitle("Mttbar")

    # Save the canvas
    c1.SaveAs("hist_mttbar_combined_notnormalized.png")

    # Close files
    file1.Close()
    file2.Close()
    file3.Close()

if __name__ == "__main__":
    overlay_histograms_normalized()
