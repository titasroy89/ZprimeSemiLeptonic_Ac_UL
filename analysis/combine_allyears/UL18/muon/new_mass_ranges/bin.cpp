#include <iostream>
#include "TFile.h"
#include "TH2.h"

int bin() {
    TFile *file = TFile::Open("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/combine_allyears/UL18/muon/new_mass_ranges/1000_1500/first_step_scripts/dY_UL18_muon_1000_1500_TTbar.root", "READ");
    if (file == nullptr) {
        std::cerr << "File not found. Exiting." << std::endl;
        return 1;
    }

    // Retrieve the histogram
    TH2F *h2 = (TH2F*)file->Get("Matrix");
    if (h2 == nullptr) {
        std::cerr << "Histogram not found in file. Exiting." << std::endl;
        return 1;
    }

    // Get the number of bins along each axis
    int nBinsX = h2->GetNbinsX();
    int nBinsY = h2->GetNbinsY();

    // Check if the histogram is 2x2
    if (nBinsX != 2 || nBinsY != 2) {
        std::cerr << "Histogram is not 2x2. Exiting." << std::endl;
        return 1;
    }

    // Loop over the bins and retrieve the number of events
    std::cout << "Number of events in each bin:" << std::endl;
    for (int i = 1; i <= nBinsX; i++) {
        for (int j = 1; j <= nBinsY; j++) {
            double binContent = h2->GetBinContent(i, j);
            std::cout << "Bin (" << i << ", " << j << "): " << binContent << std::endl;
        }
    }

    // Close the file
    file->Close();

    return 0;
}
