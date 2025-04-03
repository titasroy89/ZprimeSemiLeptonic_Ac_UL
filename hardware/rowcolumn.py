import ROOT

file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/hardware/Run000020_PixelAlive.root")

directory = file.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0")

if not directory:
    print("Directory not found!")
    exit()

canvas = directory.Get("Chip_12/D_B(0)_O(0)_H(0)_PixelAlive_Chip(12)")
if not canvas:
    print("Canvas not found!")
    exit()

hist = None
for primitive in canvas.GetListOfPrimitives():
    if isinstance(primitive, ROOT.TH2):
        hist = primitive
        break

if not hist:
    print("Histogram not found in canvas!")
    exit()

n_bins_x = hist.GetNbinsX()
n_bins_y = hist.GetNbinsY()

print("Number of bins in x: {n_bins_x}".format(n_bins_x=n_bins_x))
print("Number of bins in y: {n_bins_y}".format(n_bins_y=n_bins_y))

for x_bin in range(1, n_bins_x + 1):
    for y_bin in range(1, n_bins_y + 1):
        bin_content = hist.GetBinContent(x_bin, y_bin)
        print("Bin (x, y): ({x_bin}, {y_bin}) -> Content: {bin_content}".format(x_bin=x_bin, y_bin=y_bin, bin_content=bin_content))

file.Close()
