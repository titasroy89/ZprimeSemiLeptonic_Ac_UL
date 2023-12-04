#include <TFile.h>
#include <TTree.h>
#include <iostream>
#include <vector>

void printSystWeights() {
    std::cout << "Opening file..." << std::endl;

    TFile *file = TFile::Open("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Analysis_UL18_muon_combine/uhh2.AnalysisModuleRunner.MC.TTToSemiLeptonic_UL18_29.root");
    if (!file || file->IsZombie()) {
        std::cerr << "File not found or is corrupted." << std::endl;
        return;
    }

    TTree *tree = (TTree*)file->Get("AnalysisTree");
    if (!tree) {
        std::cerr << "Tree not found." << std::endl;
        return;
    }

    std::vector<float> *systweights = nullptr; // It's safer to initialize with nullptr

    TBranch* br = tree->GetBranch("m_systweights");
    if (!br) {
        std::cerr << "Branch 'm_systweights' does not exist. Exiting." << std::endl;
        return;
    }
    br->SetAddress(&systweights);

    Long64_t nentries = tree->GetEntries();
    std::cout << "Number of entries: " << nentries << std::endl;

    for (Long64_t i = 0; i < nentries; i++)
    {
        tree->GetEntry(i);

        if (!systweights) {
            std::cerr << "Error: systweights pointer is null for entry " << i << ". Skipping." << std::endl;
            continue;
        }

        std::cout << "Entry " << i << " has " << systweights->size() << " weights." << std::endl;

        for (size_t j = 0; j < systweights->size(); j++)
        {
            std::cout << "Weight " << j << ": " << systweights->at(j) << std::endl;
        }
    }

    // Clean up
    if (systweights) {
        delete systweights; // Delete only if it's not a nullptr
    }
    file->Close();
}
