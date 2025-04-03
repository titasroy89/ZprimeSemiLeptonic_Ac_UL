import ROOT

number_of_events1 = 1.0e7  # number of events for the first histogram
number_of_events2 = 1.0e7  # number of events for the second histogram
triggers_per_event = 10    # bunch crossing per event
total_number_of_triggers1 = number_of_events1 * triggers_per_event  # number of triggers for the first histogram
total_number_of_triggers2 = number_of_events2 * triggers_per_event  # number of triggers for the second histogram

file1 = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/hardware/Run000018_PixelAlive.root", "READ")
canvas1 = file1.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_PixelAlive_Chip(12)")

file2 = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/hardware/Run000020_PixelAlive.root", "READ")
canvas2 = file2.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_PixelAlive_Chip(12)")

def extract_hits_per_pixel(canvas, hist_name, total_number_of_triggers):
    histogram = None
    primitives = canvas.GetListOfPrimitives()
    for primitive in primitives:
        if isinstance(primitive, ROOT.TH2):
            histogram = primitive
            break

    if not histogram:
        raise Exception("No TH2 histogram found in the PixelAlive canvas.")

    hits_per_pixel_hist = ROOT.TH1F(hist_name, "Number of Hits per Pixel", 100, 0, 15000)

    n_bins_x = histogram.GetNbinsX()
    n_bins_y = histogram.GetNbinsY()

    for x in range(1, n_bins_x + 1):
        for y in range(1, n_bins_y + 1):
            occupancy = histogram.GetBinContent(x, y)
            number_of_hits_per_pixel = occupancy * total_number_of_triggers
            hits_per_pixel_hist.Fill(number_of_hits_per_pixel)

    return hits_per_pixel_hist

hits_per_pixel_hist1 = extract_hits_per_pixel(canvas1, "hits_per_pixel1", total_number_of_triggers1)
hits_per_pixel_hist2 = extract_hits_per_pixel(canvas2, "hits_per_pixel2", total_number_of_triggers2)

canvas_new = ROOT.TCanvas("canvas_new", "Hits per Pixel", 800, 600)

hits_per_pixel_hist2.SetLineColor(ROOT.kRed)
hits_per_pixel_hist2.SetLineStyle(1)  # solid line
hits_per_pixel_hist2.SetLineWidth(2)  # thicker line

hits_per_pixel_hist1.SetLineColor(ROOT.kBlue)
hits_per_pixel_hist1.SetLineStyle(2)  # dashed line
hits_per_pixel_hist1.SetLineWidth(2)  # thicker line

hits_per_pixel_hist1.Draw()
hits_per_pixel_hist2.Draw("SAME")

legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend.AddEntry(hits_per_pixel_hist1, "Threshold 2000e ", "l")
legend.AddEntry(hits_per_pixel_hist2, "Threshold 1000e", "l")
legend.Draw()

hits_per_pixel_hist1.GetXaxis().SetTitle("Number of total Hits/pixel")
hits_per_pixel_hist1.GetYaxis().SetTitle("Entries")

canvas_new.SaveAs("hits_per_pixel_overlay_threshold_v2.png")

file1.Close()
file2.Close()
