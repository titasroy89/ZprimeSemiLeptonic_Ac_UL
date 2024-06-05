import ROOT

file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL17/Preselection/workdir_Preselection_UL17_chargecheck/nominal/TTbar.root")
# file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL17/muon/workdir_AnalysisDNN_UL17_muon_chargecheck/nominal/TTbar.root")


# hist_ttbar = file.Get("NNInputsBeforeReweight_General/N_lep_charge") 
# hist_ttbar = file.Get("AfterChi2_General/N_lep_charge")
# hist_ttbar = file.Get("Weights_Init_General/N_ele_charge") 
hist_ttbar = file.Get("MET_General/N_ele_charge") 

def get_counts_and_uncertainties(hist):
    n_bins = hist.GetNbinsX()
    counts = []
    uncertainties = []
    for i in range(1, n_bins + 1):
        count = hist.GetBinContent(i)
        uncertainty = hist.GetBinError(i)
        counts.append(count)
        uncertainties.append(uncertainty)
    return counts, uncertainties

counts_ttbar, uncertainties_ttbar = get_counts_and_uncertainties(hist_ttbar)

for i in range(len(counts_ttbar)):
    print("Bin {}: Count = {}, Uncertainty = {}").format(i, counts_ttbar[i], uncertainties_ttbar[i])
    # print("Bin {}: Count = {:.4e}, Uncertainty = {:.4e}".format(i + 1, counts_ttbar[i], uncertainties_ttbar[i]))


file.Close()
