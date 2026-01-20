#!/usr/bin/env python2
import ROOT
import glob
import math
import argparse
import os

# Setup
ROOT.gROOT.SetBatch(True)
ROOT.TH1.SetDefaultSumw2()

def get_noac_suffix(fv):
    # Matches C++ get_noac_suffix logic
    if abs(fv) < 0.01: return "noac0"
    if fv < 0: return "noacm" + str(int(abs(fv)))
    return "noac" + str(int(fv))

def mirror_hist(h_in):
    h_mir = h_in.Clone(h_in.GetName() + "_mirrored")
    h_mir.Reset()
    nb = h_in.GetNbinsX()
    for i in range(1, nb + 1):
        xc = h_in.GetXaxis().GetBinCenter(i)
        # Find bin for -xc
        j = h_in.FindBin(-xc)
        # Handle edge cases (though symmetric binning [-1,1] should be fine)
        if j < 1: j = 1
        if j > nb: j = nb
        
        h_mir.SetBinContent(i, h_in.GetBinContent(j))
        h_mir.SetBinError(i, h_in.GetBinError(j))
    return h_mir

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', required=True, help='Input ROOT file pattern (glob)')
    parser.add_argument('--output', '-o', required=True, help='Output ROOT file')
    parser.add_argument('--tree', default='AnalysisTree', help='Tree name')
    args = parser.parse_args()

    # Get list of files
    files = glob.glob(args.input)
    if not files:
        print "No files found matching", args.input
        return

    print "Found", len(files), "files."

    # Define bins
    # 6 bins: [-1, -0.6, -0.2, 0.2, 0.6, 1] ? Or uniform?
    # C++ uses uniform 6 bins in [-1, 1].
    # We want 18 bins uniform [-1, 1].
    
    nbins = 18
    xmin = -1.0
    xmax = 1.0
    
    # Histogram for inclusive xi (S+A)
    # Use a chain to read many files
    chain = ROOT.TChain(args.tree)
    for f in files:
        chain.Add(f)
        
    print "Total entries:", chain.GetEntries()

    # DEBUG: Print branches to debug missing xi_gen
    print "Available branches:"
    branches = chain.GetListOfBranches()
    for i in range(branches.GetEntries()):
        print "  ", branches.At(i).GetName()
    
    if not branches.FindObject("xi_gen"):
        print "ERROR: Branch 'xi_gen' not found in tree!"
        return

    # Define mtt bins (matching C++ noac_mtt_edges)
    mtt_edges = [0.0, 350.0, 500.0, 750.0, 1000.0, 1500.0, 10000.0]
    
    # Check branches
    l = chain.GetListOfBranches()
    has_weight = l.FindObject("weight")
    has_mtt = l.FindObject("mtt_gen")
    
    if not has_mtt:
        print "Error: mtt_gen branch not found in tree!"
        return

    f_out = ROOT.TFile(args.output, "RECREATE")
    
    # Loop over mtt bins
    for ib in range(len(mtt_edges)-1):
        low = mtt_edges[ib]
        high = mtt_edges[ib+1]
        bin_suffix = "_mtt%d" % ib
        print "Processing mtt bin %d: [%.0f, %.0f]" % (ib, low, high)
        
        h_incl = ROOT.TH1D("h_incl" + bin_suffix, "Inclusive GEN xi mtt%d" % ib, nbins, xmin, xmax)
        
        # Selection
        sel = "(xi_gen > -1.0001 && xi_gen < 1.0001) && (mtt_gen >= %f && mtt_gen < %f)" % (low, high)
        if has_weight:
            sel += " * weight"
            
        chain.Draw("xi_gen >> h_incl" + bin_suffix, sel, "goff")
        
        # Decompose
        h_mir = mirror_hist(h_incl)
        h_S = h_incl.Clone("h_S" + bin_suffix)
        h_A = h_incl.Clone("h_A" + bin_suffix)
        h_S.Reset(); h_A.Reset()
        h_S.Add(h_incl, h_mir, 0.5, 0.5)
        h_A.Add(h_incl, h_mir, 0.5, -0.5)
        
        h_S.Write()
        h_A.Write()
        h_incl.Write()
        
        # Build templates
        for fv in f_values:
            suffix = get_noac_suffix(fv)
            # Naming: match what analysis code might expect or clear identification
            # Standard analysis might expect just "DeltaY_xi_gen_18_noacX" if files are split by mtt bin
            # But here we put all in one file. Let's append bin suffix.
            hname = "DeltaY_xi_gen_18_" + suffix + bin_suffix
            
            h_f = h_S.Clone(hname)
            h_f.Add(h_A, 1.0 - fv)
            h_f.Write()

        # --- Plotting ---
        c = ROOT.TCanvas("c_mtt%d" % ib, "Templates mtt%d" % ib, 800, 600)
        # Get f=0, f=1, f=-1, f=4, f=-4 for comparison
        h0 = f_out.Get("DeltaY_xi_gen_18_noac0" + bin_suffix)
        h1 = f_out.Get("DeltaY_xi_gen_18_noac1" + bin_suffix)
        hm1 = f_out.Get("DeltaY_xi_gen_18_noacm1" + bin_suffix)
        h4 = f_out.Get("DeltaY_xi_gen_18_noac4" + bin_suffix)
        hm4 = f_out.Get("DeltaY_xi_gen_18_noacm4" + bin_suffix)
        
        if h0 and h1 and hm1 and h4 and hm4:
            h0.SetLineColor(ROOT.kBlack); h0.SetLineWidth(2)
            h1.SetLineColor(ROOT.kRed); h1.SetLineWidth(2)
            hm1.SetLineColor(ROOT.kBlue); hm1.SetLineWidth(2)
            h4.SetLineColor(ROOT.kMagenta); h4.SetLineWidth(2); h4.SetLineStyle(2)
            hm4.SetLineColor(ROOT.kGreen+2); hm4.SetLineWidth(2); hm4.SetLineStyle(2)
            
            # Normalize to 1 for shape comparison
            for h in [h0, h1, hm1, h4, hm4]:
                if h.Integral() > 0: h.Scale(1./h.Integral())
            
            h0.SetStats(0)
            h0.SetTitle("GEN Templates Mtt Bin %d;GEN #xi;Normalized Events" % ib)
            max_y = max([h.GetMaximum() for h in [h0, h1, hm1, h4, hm4]])
            h0.GetYaxis().SetRangeUser(0, max_y * 1.2)
            
            h0.Draw("HIST")
            h1.Draw("HIST SAME")
            hm1.Draw("HIST SAME")
            h4.Draw("HIST SAME")
            hm4.Draw("HIST SAME")
            
            leg = ROOT.TLegend(0.7, 0.6, 0.9, 0.9)
            leg.AddEntry(h0, "f=0 (SM)", "l")
            leg.AddEntry(h1, "f=1.0", "l")
            leg.AddEntry(hm1, "f=-1.0", "l")
            leg.AddEntry(h4, "f=4.0", "l")
            leg.AddEntry(hm4, "f=-4.0", "l")
            leg.Draw()
            
            out_png = args.output.replace(".root", "") + "_mtt%d.png" % ib
            c.SaveAs(out_png)

    f_out.Close()
    print "Done. Output written to", args.output

if __name__ == "__main__":
    main()

