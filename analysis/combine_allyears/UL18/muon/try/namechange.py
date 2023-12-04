import ROOT

f = ROOT.TFile("DeltaY.root", "UPDATE")
# f.ls()
hist_names = ["Ttbar_1_nominal", "Ttbar_2_nominal", "dy_nominal", "wjets_nominal", "qcd_nominal", "singletop_nominal"]
new_names = [name.replace('_nominal', '') for name in hist_names]

for old_name, new_name in zip(hist_names, new_names):
    hist = f.Get(old_name)
    if not hist:
        print("Failed to retrieve histogram:", old_name)
        continue
    cloned_hist = hist.Clone(new_name)
    cloned_hist.SetDirectory(0)  # This detaches the histogram from the file/directory
    cloned_hist.Write()

f.Close()
