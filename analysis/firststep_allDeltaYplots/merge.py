import ROOT

def combine_root_files(input_files, output_file, tree_name):
    chain = ROOT.TChain(tree_name)

    # Add the input files to the TChain
    for file in input_files:
        chain.Add(file)

    # Create a new output file and create a new TTree with the same branches as the input TTree
    output = ROOT.TFile(output_file, "RECREATE")
    tree = chain.CloneTree(0)  # Clone only the structure, not the data

    # Process events in chunks
    num_entries = chain.GetEntries()
    for i in range(num_entries):
        chain.GetEntry(i)  # Get the current event
        tree.Fill()  # Fill the output tree with the current event

    # Write and close the output file
    tree.Write()
    output.Close()

if __name__ == "__main__":
    input_files = [
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar1.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar2.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar3.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar4.root"
        
    ]
    output_file = "uhh2.AnalysisModuleRunner.TTbar.root"
    tree_name = "AnalysisTree"  # Replace with the name of the TTree you want to combine

    combine_root_files(input_files, output_file, tree_name)
