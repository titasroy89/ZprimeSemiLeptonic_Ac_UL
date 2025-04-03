import ROOT

file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/hardware/Run000020_PixelAlive.root", "READ")
canvas = file.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_PixelAlive_Chip(12)")

# pixelalive_plot = file.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_PixelAlive_Chip(12)")

# if not pixelalive_plot:
#     raise Exception("PixelAlive plot not found in the ROOT file.")

# n_bins_x = pixelalive_plot.GetNbinsX()
# n_bins_y = pixelalive_plot.GetNbinsY()

# total_occupancy = 0
# total_bins = 0

# for x in range(1, n_bins_x + 1):
#     for y in range(1, n_bins_y + 1):
#         bin_content = pixelalive_plot.GetBinContent(x, y)
#         total_occupancy += bin_content
#         total_bins += 1

# average_occupancy = total_occupancy / total_bins

# print("Average Occupancy: {}".format(average_occupancy))

# file.Close()


###### Canvas 

# if not canvas:
#     raise Exception("PixelAlive canvas not found in the ROOT file.")

# histogram = None
# primitives = canvas.GetListOfPrimitives()
# for primitive in primitives:
#     if isinstance(primitive, ROOT.TH2):
#         histogram = primitive
#         break

# if not histogram:
#     raise Exception("No TH2 histogram found in the PixelAlive canvas.")

# n_bins_x = histogram.GetNbinsX()
# n_bins_y = histogram.GetNbinsY()

# total_occupancy = 0
# total_bins = 0

# for x in range(1, n_bins_x + 1):
#     for y in range(1, n_bins_y + 1):
#         bin_content = histogram.GetBinContent(x, y)
#         total_occupancy += bin_content
#         total_bins += 1
# print ("total_occupancy: ", total_occupancy, "-- total_bins: ", total_bins)
# average_occupancy = total_occupancy / total_bins

# print("Average Occupancy: {average_occupancy}".format(average_occupancy=average_occupancy))

# file.Close()

# number_of_triggers = 1.0e6
# bx_per_trigger = 10

# total_hits = average_occupancy * number_of_triggers * bx_per_trigger

# print("Total Hits: {total_hits}".format(total_hits=total_hits))


### Total number of hits per pixel

number_of_events = 1e7  # Number of events
triggers_per_event = 10   # Triggers per event
total_number_of_triggers = number_of_events * triggers_per_event  # Total number of triggers

histogram = None
primitives = canvas.GetListOfPrimitives()
for primitive in primitives:
    if isinstance(primitive, ROOT.TH2):
        histogram = primitive
        break

if not histogram:
    raise Exception("No TH2 histogram found in the PixelAlive canvas.")

hits_per_pixel_hist = ROOT.TH1F("hits_per_pixel", "Number of Hits per Pixel -1e7 Events, 1000e", 100, 0, 15000)

n_bins_x = histogram.GetNbinsX()
n_bins_y = histogram.GetNbinsY()

for x in range(1, n_bins_x + 1):
    for y in range(1, n_bins_y + 1):
        occupancy = histogram.GetBinContent(x, y)
        number_of_hits_per_pixel = occupancy * total_number_of_triggers
        hits_per_pixel_hist.Fill(number_of_hits_per_pixel)

canvas_new = ROOT.TCanvas("canvas_new", "Hits per Pixel", 800, 600)
hits_per_pixel_hist.GetXaxis().SetTitle("Number of total Hits/pixel")
hits_per_pixel_hist.GetYaxis().SetTitle("Entries")
hits_per_pixel_hist.Draw()

canvas_new.SaveAs("hits_per_pixel_Run20.png")

file.Close()

