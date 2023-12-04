import ROOT

# file = ROOT.TFile("DeltaY_UL18_muon_750_900_ttbar_test.root", "UPDATE")

# # input file with nominal hists
# nominal_hist = file.Get("TTbar_1")

# # uncertainty percentage
# uncertainty_size = 0.1

# #up and down plot names
# up_name = "TTbar_1_up"
# down_name = "TTbar_1_down"

# up_hist = nominal_hist.Clone(up_name)
# down_hist = nominal_hist.Clone(down_name)

# # Loop over each bin in the nominal histogram and apply uncert
# for i in range(1, nominal_hist.GetNbinsX() + 1):
#     nominal_bin_content = nominal_hist.GetBinContent(i)
#     up_bin_content = nominal_bin_content * (1.0 + uncertainty_size)
#     down_bin_content = nominal_bin_content * (1.0 - uncertainty_size)
#     up_hist.SetBinContent(i, up_bin_content)
#     down_hist.SetBinContent(i, down_bin_content)

# up_hist.Write()
# down_hist.Write()


# file.Close()

input_file = ROOT.TFile.Open("DeltaY_UL18_muon_750_900_ttbar_test.root")

histograms = {}
for i in input_file.GetListOfKeys():
    name = i.GetName()
    if not name.startswith(TTbar_1)
        continue
    histogram = input_file.Get(name)
    histogram[name] = histogram
    
scale_factor{}
for j in input_file.GetListOfKeys():
    name = key.GetName()
    if not name startswith("")
    
