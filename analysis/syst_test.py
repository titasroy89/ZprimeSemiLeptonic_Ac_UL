import ROOT

# Open the ROOT file containing the nominal histogram
file = ROOT.TFile("DeltaY_UL18_muon_750_900_sys.root", "UPDATE")

# Get the nominal histogram from the file
nominal_hist = file.Get("TTbar_1")

# Define the size of the uncertainty to apply (e.g. 10%)
uncertainty_size = 0.1

# Define the names for the up and down variations
up_name = "TTbar_1_up"
down_name = "TTbar_1_down"

# Create histograms for the up and down variations
up_hist = nominal_hist.Clone(up_name)
down_hist = nominal_hist.Clone(down_name)

# Loop over each bin in the nominal histogram and apply the variation
for i in range(1, nominal_hist.GetNbinsX() + 1):
    nominal_bin_content = nominal_hist.GetBinContent(i)
    up_bin_content = nominal_bin_content * (1.0 + uncertainty_size)
    down_bin_content = nominal_bin_content * (1.0 - uncertainty_size)
    up_hist.SetBinContent(i, up_bin_content)
    down_hist.SetBinContent(i, down_bin_content)

# Write the new histograms to the file
up_hist.Write()
down_hist.Write()

# Close the ROOT file
file.Close()