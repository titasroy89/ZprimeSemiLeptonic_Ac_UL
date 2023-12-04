import ROOT

# canvas = ROOT.TCanvas("canvas", "OSU & UIC")

file1 = ROOT.TFile.Open("UIC_RH15/1200_Threqu_UIC.root")
file2 = ROOT.TFile.Open("OSU_RH15/1200_Threqu_OSU.root")

file4 = ROOT.TFile.Open("UIC_RH15/1000_Threqu_UIC.root")
file5 = ROOT.TFile.Open("OSU_RH15/1000_Threqu_OSU.root")

file7 = ROOT.TFile.Open("UIC_RH15/800_Threqu_UIC.root")
file8 = ROOT.TFile.Open("OSU_RH15/800_Threqu_OSU.root")

file9 = ROOT.TFile.Open("UIC_RH15/1200_Threqu_UIC.root")
file10 = ROOT.TFile.Open("OSU_RH15/1200_Threqu_OSU.root")

file11 = ROOT.TFile.Open("UIC_RH15/1000_Threqu_UIC.root")
file12 = ROOT.TFile.Open("OSU_RH15/1000_Threqu_OSU.root")

file13 = ROOT.TFile.Open("UIC_RH15/800_Threqu_UIC.root")
file14 = ROOT.TFile.Open("OSU_RH15/800_Threqu_OSU.root")

    
hist1 = file1.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")
hist2 = file2.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")
# hist3 = file3.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")

hist4 = file4.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")
hist5 = file5.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")
# hist6 = file6.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")

hist7 = file7.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")
hist8 = file8.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")
# hist9 = file9.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")

hist9 = file1.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
hist10 = file2.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
# hist3 = file3.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")

hist11 = file4.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
hist12 = file5.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
# hist6 = file6.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_13/D_B(0)_O(0)_H(0)_Occ1D_Chip(13)")

hist13 = file7.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
hist14 = file8.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")


file1.Close()
file2.Close()
# file3.Close()

file4.Close()
file5.Close()
# file6.Close()

file7.Close()
file8.Close()

file9.Close()
file10.Close()

file11.Close()
file12.Close()

file13.Close()
file14.Close()

output_file = ROOT.TFile.Open("General_Occ.root", "RECREATE")
output_file.cd()

hist1.Write("UIC1200_13")
hist2.Write("OSU1200_13")
# hist3.Write("Cor1200_12")

hist4.Write("UIC1000_13")
hist5.Write("OSU1000_13")
# hist6.Write("Cor1000_12")

hist7.Write("UIC800_13")
hist8.Write("OSU800_13")

hist9.Write("UIC1200_12")
hist10.Write("OSU1200_12")

hist11.Write("UIC1000_12")
hist12.Write("OSU1000_12")

hist13.Write("UIC800_12")
hist14.Write("OSU800_12")


output_file.Close()

