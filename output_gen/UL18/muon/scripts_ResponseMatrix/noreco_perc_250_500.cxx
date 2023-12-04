#include <algorithm>
#include <iterator>
#include <iostream>
#include <TFile.h>
#include <TROOT.h>
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLatex.h>
#include "TCanvas.h"
#include "RooPlot.h"
#include "TTree.h"
#include "TH1D.h"
#include "TH1D.h"
#include "THStack.h"
#include "TRandom.h"
#include "TUnfoldDensity.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TFrame.h"
#include "TPaveLabel.h"
#include "TPad.h"
#include "TLegend.h"
#include "TRandom3.h"
#include "TFile.h"
#include "TMath.h"

using namespace RooFit ;

void noreco_perc_250_500() {

    TFile *file1 = TFile::Open("semi.root");
    TFile *file2 = TFile::Open("other.root");

    const char* folderNames[] = {
        "DY_Match_N_N_250_500_muon_General", "DY_Match_N_P_250_500_muon_General",
        "DY_Match_P_N_250_500_muon_General", "DY_Match_P_P_250_500_muon_General",
        "DY_Mass_250_500_NOT_reco_muon_General"
    };

    const char* histName = "DeltaY_reco";
    
    TH1D* combinedHists[5];

    for (int i = 0; i < 5; ++i) {
        TDirectory* dir1 = (TDirectory*)file1->Get(folderNames[i]);
        TDirectory* dir2 = (TDirectory*)file2->Get(folderNames[i]);
        TH1D *hist1 = (TH1D*)dir1->Get(histName);
        TH1D *hist2 = (TH1D*)dir2->Get(histName);

        TString combinedHistName = TString::Format("combined_%s", folderNames[i]);
        combinedHists[i] = (TH1D*)hist1->Clone(combinedHistName);
        combinedHists[i]->Add(hist2);
    }


    double totalN = combinedHists[0]->Integral() + combinedHists[1]->Integral();
    double totalP = combinedHists[2]->Integral() + combinedHists[3]->Integral();

    std::cout << "========= " << std::endl;
    std::cout << "250_500 " << std::endl;
    std::cout << "========= " << std::endl; 

    std::cout << "Percentage of gen bin N correctly matched in reco bin N: " 
              << (combinedHists[0]->Integral() / totalN) * 100 << "%" << std::endl;

    std::cout << "Number of gen bin N correctly matched in reco bin N: " 
              << (combinedHists[0]->Integral()) << std::endl;
    
    std::cout << "Percentage of gen bin N incorrectly matched in reco bin P: " 
              << (combinedHists[1]->Integral() / totalN) * 100 << "%" << std::endl;

    std::cout << "Number of gen bin N incorrectly matched in reco bin P: " 
              << (combinedHists[1]->Integral() ) << std::endl;
              
    std::cout << "Percentage of gen bin P correctly matched in reco bin P: " 
              << (combinedHists[3]->Integral() / totalP) * 100 << "%" << std::endl;

    std::cout << "Number of gen bin P correctly matched in reco bin P: " 
              << (combinedHists[3]->Integral() ) << std::endl;


    std::cout << "Percentage of gen bin P incorrectly matched in reco bin N: " 
              << (combinedHists[2]->Integral() / totalP) * 100 << "%" << std::endl;

    std::cout << "Number of gen bin P incorrectly matched in reco bin N: " 
              << (combinedHists[2]->Integral()) << std::endl;



    double unmatchedPercentage = (combinedHists[4]->Integral() / (totalN + totalP)) * 100;
    std::cout << "Number of unmatched gen particles: " << combinedHists[4]->Integral() << std::endl;
    std::cout << "Percentage of unmatched gen particles: " << unmatchedPercentage << "%" << std::endl;

    // Cleanup
    file1->Close();
    file2->Close();
    for (int i = 0; i < 5; ++i) {
        delete combinedHists[i];
    }

}
