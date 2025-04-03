#!/usr/bin/env python2
import ROOT
ROOT.gROOT.SetBatch(True)
def main():
    #-------------------------------------------------------------------
    # 1) List of ROOT files
    #-------------------------------------------------------------------
    files = [
        # "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_700_900_1.root",
        # "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_700_900_2.root",
        # "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_700_900_3.root",
        # "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_700_900_4.root"
        
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_900_Inf_1.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_900_Inf_2.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_900_Inf_3.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_900_Inf_4.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_900_Inf_5.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_EFT/Preselection/EFT_Mtt_900_Inf_6.root"


    ]


    #-------------------------------------------------------------------
    # 2) Dictionary to store combined yields from all files:
    #    raw_cutflow[folder_name] = yield
    #-------------------------------------------------------------------
    raw_cutflow = {}

    #-------------------------------------------------------------------
    # 3) Loop over each ROOT file and accumulate yields
    #-------------------------------------------------------------------
    for fpath in files:
        print("Opening file: {}".format(fpath))
        f = ROOT.TFile.Open(fpath)
        if not f or f.IsZombie():
            print("  ERROR: Could not open file {}".format(fpath))
            continue

        # Get list of top-level keys (directories, histograms, etc.)
        keys = f.GetListOfKeys()
        for key in keys:
            obj = key.ReadObj()
            # Only process directories
            if not obj.InheritsFrom("TDirectory"):
                continue

            cut_name = obj.GetName()  # e.g. "CommonModules", "Lepton1", etc.

            f.cd(cut_name)
            hist = ROOT.gDirectory.Get("N_jets")
            if not hist:
                print("  WARNING: 'N_jets' not found in directory '{}', file '{}'"
                      .format(cut_name, fpath))
                continue
            num_events = hist.GetEntries()

            # Accumulate yield
            raw_cutflow[cut_name] = raw_cutflow.get(cut_name, 0.0) + num_events

        f.Close()

    #-------------------------------------------------------------------
    # 4) cutflow order
    #
    #-------------------------------------------------------------------

    # (label_for_printing, [list_of_folder_names_in_precedence_order])
    final_cutflow_order = [
        ("Input",              ["Input_General"]),
        ("CommonModules",      ["CommonModules_General"]),
        ("> 1 Lepton",   ["Lepton1_General"]),      
        ("JetID+Cleaners",     ["TopjetCleaner_General"]),
        ("> 1 Jet",      ["Jet1_General"]),
        ("> 2 Jets",     ["Jet2_General"]),
        ("MET",                ["MET_General"])
    ]

    #-------------------------------------------------------------------
    # 5) final cutflow
    #-------------------------------------------------------------------
    cutflow_final = []
    for (pretty_label, folders) in final_cutflow_order:
        yield_val = None
        for fname in folders:
            if fname in raw_cutflow:
                yield_val = raw_cutflow[fname]
                break
        if yield_val is None:
            # None of the folders were found
            yield_val = 0.0
        cutflow_final.append((pretty_label, yield_val))

    #-------------------------------------------------------------------
    # 6) Print a text-based table
    #-------------------------------------------------------------------
    print("\n=== Cutflow (Summed Across All Files) ===")
    print("{:25}  {:>15}".format("Cut Name", "Yield"))
    print("-" * 42)
    for label, yval in cutflow_final:
        print("{:25}  {:15.2f}".format(label, yval))

    #-------------------------------------------------------------------
    # 7) Create a single histogram for these final steps
    #-------------------------------------------------------------------
    n_cuts = len(cutflow_final)
    cutflow_hist = ROOT.TH1F("CutFlow", "CutFlow Mtt 900-Inf", n_cuts, 0, n_cuts)
    cutflow_hist.SetStats(False)
    cutflow_hist.GetYaxis().SetTitle("Number of Events")
    cutflow_hist.GetXaxis().SetTitle("Cut Step")

    for i, (label, yval) in enumerate(cutflow_final):
        bin_index = i + 1
        cutflow_hist.GetXaxis().SetBinLabel(bin_index, label)
        cutflow_hist.SetBinContent(bin_index, yval)

    c = ROOT.TCanvas("c", "CutFlowCanvas", 800, 600)
    cutflow_hist.Draw("HIST TEXT0")
    c.Update()
    c.SaveAs("cutflow_900Inf.pdf")

    print("\nCutflow histogram saved as 'cutflow_custom.pdf'.")

if __name__ == "__main__":
    main()
