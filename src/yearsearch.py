import ROOT

file = ROOT.TFile("/pnfs/desy.de/cms/tier2/store/group/uhh/uhh2ntuples/RunII_106X_v2/UL17/TTtoLNu2Q-1Jets-smeft_MTT-900toInf_TuneCP5_13TeV_madgraphMLM-pythia8/crab_TTtoLNu2Q-1Jets-smeft_MTT-900toInf_CP5_madgraphMLM-pythia8_Summer20UL17_v2/241105_230722/0000/Ntuple_100.root")
tree = file.Get("AnalysisTree")  
# tree.Print()

years = set()
for event in tree:
    years.add(event.year)
    print(event.year)
print("Years in the ntuple:", years)
