import ROOT

# canvas = ROOT.TCanvas("canvas", "OSU & UIC")

file1 = ROOT.TFile.Open("OSU_1200_Threqu.root")
file2 = ROOT.TFile.Open("UIC_1200_Threqu.root")
# file3 = ROOT.TFile.Open("Cor_1200_Threqu.root")

file4 = ROOT.TFile.Open("OSU_1000_Threqu.root")
file5 = ROOT.TFile.Open("UIC_1000_Threqu.root")
file6 = ROOT.TFile.Open("Cor_1000_Threqu.root")

file7 = ROOT.TFile.Open("OSU_800_Threqu.root")
file8 = ROOT.TFile.Open("UIC_800_Threqu.root")
file9 = ROOT.TFile.Open("Cornell_800_Threqu.root")


    
hist1 = file1.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
hist2 = file2.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
# hist3 = file3.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")

hist4 = file4.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
hist5 = file5.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
hist6 = file6.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")

hist7 = file7.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
hist8 = file8.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")
hist9 = file9.Get("Detector/Board_0/OpticalGroup_0/Hybrid_0/Chip_12/D_B(0)_O(0)_H(0)_Occ1D_Chip(12)")


file1.Close()
file2.Close()
# file3.Close()

file4.Close()
file5.Close()
file6.Close()

file7.Close()
file8.Close()
file9.Close()

output_file = ROOT.TFile.Open("General3.root", "RECREATE")
output_file.cd()

hist1.Write("OSU1200_12")
hist2.Write("UIC1200_12")
# hist3.Write("Cor1200_12")

hist4.Write("OSU1000_12")
hist5.Write("UIC1000_12")
hist6.Write("Cor1000_12")

hist7.Write("OSU800_12")
hist8.Write("UIC800_12")
hist9.Write("Cor800_12")

output_file.Close()

