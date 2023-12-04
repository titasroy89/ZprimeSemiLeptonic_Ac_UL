#include "TH2.h"
#include "TFile.h"

int migration() {
    TFile *file = TFile::Open("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/combine_allyears/UL18/muon/new_mass_ranges/1000_1500/first_step_scripts/dY_UL18_muon_1000_1500_TTbar.root");
    if (file == nullptr) {
        return 1;
    }

    TH2F *h2 = (TH2F*)file->Get("Matrix");

    double bin_11 = h2->GetBinContent(1, 1);
    double bin_22 = h2->GetBinContent(2, 2);
    double bin_12 = h2->GetBinContent(1, 2);
    double bin_21 = h2->GetBinContent(2, 1);

    double bin_11_err = h2->GetBinError(1, 1);
    double bin_22_err = h2->GetBinError(2, 2);
    double bin_12_err = h2->GetBinError(1, 2);
    double bin_21_err = h2->GetBinError(2, 1);


    std::cout << "Number of events in bin (1,1): " << bin_11 << " +- " << bin_11_err << std::endl;
    std::cout << "Number of events in bin (2,2): " << bin_22 << " +- " << bin_22_err << std::endl;
    std::cout << "Number of events in bin (1,2): " << bin_12 << " +- " << bin_12_err << std::endl;
    std::cout << "Number of events in bin (2,1): " << bin_21 << " +- " << bin_21_err << std::endl;


    double ratio_11_22 = bin_11 / bin_22; 
    double ratio_12_21 = bin_12 / bin_21; 

    // Calculate the uncertainties for the ratios using error propagation
    double ratio_11_22_err = ratio_11_22 * sqrt(pow(bin_11_err / bin_11, 2) + pow(bin_22_err / bin_22, 2));
    double ratio_12_21_err = ratio_12_21 * sqrt(pow(bin_12_err / bin_12, 2) + pow(bin_21_err / bin_21, 2));

    // Print the ratios wmith uncertainties
    std::cout << "Ratio of events (1,1)/(2,2): " << ratio_11_22 << " +- " << ratio_11_22_err << std::endl;
    std::cout << "Ratio of events (1,2)/(2,1): " << ratio_12_21 << " +- " << ratio_12_21_err << std::endl;




    file->Close();

    return 0;
}

