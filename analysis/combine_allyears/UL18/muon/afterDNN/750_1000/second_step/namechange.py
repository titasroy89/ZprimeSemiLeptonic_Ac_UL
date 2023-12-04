import ROOT

f = ROOT.TFile("dY_UL18_muon_750_900.root", "UPDATE")
# f.ls()
hist_names = ["TTbar_1", "TTbar_2", "DY", "Diboson", "WJets", "QCD", "ST"]
new_names = [name + "_nominal" for name in hist_names]

for old_name, new_name in zip(hist_names, new_names):
    hist = f.Get(old_name)
    if not hist:
        print("Failed to retrieve histogram:", old_name)
        continue
    cloned_hist = hist.Clone(new_name)
    cloned_hist.SetDirectory(0)  # This detaches the histogram from the file/directory
    cloned_hist.Write()

f.Close()
