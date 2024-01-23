from ROOT import *
import os
import sys
from optparse import OptionParser

def getEnvelope(inputDir, v_samples, v_variations, combine_file, deltaYDir):
    for sample in v_samples:
        inFile = TFile.Open(inputDir + "muon/workdir_AnalysisDNN_UL18_muon_sys_all/nominal/" + sample + ".root", "READ")
        if not inFile:
            print("Input file for {} not found.".format(sample))
            continue

        h_nominal = inFile.Get("DeltaY_reco_SystVariations_750_1000_muon/DeltaY")
        if not h_nominal:
            print("Nominal histogram for {} not found.".format(sample))
            continue

        v_variation_norms = []
        for variation in v_variations:
            variation_hist_name = "DeltaY_reco_SystVariations_750_1000_muon/DeltaY_murmuf_" + variation
            variation_hist = inFile.Get(variation_hist_name)
            if not variation_hist:
                print "Variation histogram '%s' for %s not found." % (variation_hist_name, sample)
                continue

            norm = variation_hist.GetBinContent(1) / h_nominal.GetBinContent(1)
            v_variation_norms.append(norm)

        deltaYDir.cd()
        h_scale_up = h_nominal.Clone(sample + "_murmufUp")
        h_scale_down = h_nominal.Clone(sample + "_murmufDown")

        for bin_idx in range(1, h_nominal.GetNbinsX() + 1):
            scale_max = 0.
            scale_min = 10000000000.
            for b, variation in enumerate(v_variations):
                vars_hist_name = "DeltaY_reco_SystVariations_750_1000_muon/DeltaY_murmuf_" + variation
                bin_content = inFile.Get(vars_hist_name).GetBinContent(bin_idx) / v_variation_norms[b]
                scale_max = max(scale_max, bin_content)
                scale_min = min(scale_min, bin_content)

            h_scale_up.SetBinContent(bin_idx, scale_max)
            h_scale_down.SetBinContent(bin_idx, scale_min)

        combine_file.cd()  # Switch to output file before writing
        h_scale_up.Write()
        h_scale_down.Write()

        inFile.Close()

# Rest of your script ...

combine_file = TFile('dY_%s_%s.root' % (finalState, Mttbar), 'RECREATE')
deltaYDir = combine_file.mkdir("DeltaY")
deltaYDir.cd()

# Process each sample and write to deltaYDir in combine_file
# ...

v_samples = ["TTbar", "WJets", "ST", "QCD", "DY", "Diboson"]
v_variations = ["upup", "upnone", "noneup", "nonedown", "downnone", "downdown"]

getEnvelope(inputDir, v_samples, v_variations, combine_file, deltaYDir)

combine_file.Close()
