//  importing libraries

#include <algorithm>
#include <iterator>
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

void Matrix_0_250() {

    // std::vector<std::string> inputFiles = {"Semileptonic.root", "DYJets.root", "WJets.root", "ST.root", "QCD.root", "OtherTT.root", "Diboson.root"};
    std::vector<std::string> inputFiles = {"Semileptonic.root", "Other.root"};

    std::map<std::string, std::string> histNames = {
        {"DY_N_N_Mass_0_250_reco_muon_General/DeltaY_reco", "h_DeltaY_N_N"}, 
        {"DY_N_P_Mass_0_250_reco_muon_General/DeltaY_reco", "h_DeltaY_N_P"}, 
        {"DY_P_N_Mass_0_250_reco_muon_General/DeltaY_reco", "h_DeltaY_P_N"}, 
        {"DY_P_P_Mass_0_250_reco_muon_General/DeltaY_reco", "h_DeltaY_P_P"}
        };

    TH2D* Matrix = new TH2D("0 < Mtt  <250", "0 < Mtt  <250", 2, -2.5, 2.5, 2, -2.5,2.5);
    Matrix->GetXaxis()->SetTitle("#Delta |Y_{rec}|");
    Matrix->GetYaxis()->SetTitle("#Delta |Y_{gen}|");


    TFile* outFile = new TFile("0_250.root", "RECREATE");

    std::map<std::string, TH1F*> outHists;

    for (const auto& inputFileName : inputFiles) {
        TFile* inFile = new TFile(inputFileName.c_str(), "READ");
        for (const auto& pair : histNames){
            TH1F *h = (TH1F*)inFile->Get(pair.first.c_str());
            TH1F *h_out;
            if (outFile->Get(pair.second.c_str())) {
                h_out = (TH1F*)outFile->Get(pair.second.c_str());
                h_out->Add(h);
                outFile->cd();
                h_out->Write(pair.second.c_str(), TObject::kOverwrite);
            } else {
                outFile->cd();
                h->Write(pair.second.c_str());
            }
        }
        inFile->Close();
    }
    outFile->cd(); 
    for (const auto& pair : outHists){
        pair.second->Write();
    }
    outFile->Close();

    TFile* openOutFile = new TFile("0_250.root", "READ");
    TH1F *h_DeltaY_N_N = (TH1F*)openOutFile->Get("h_DeltaY_N_N");
    TH1F *h_DeltaY_N_P = (TH1F*)openOutFile->Get("h_DeltaY_N_P");
    TH1F *h_DeltaY_P_N = (TH1F*)openOutFile->Get("h_DeltaY_P_N");
    TH1F *h_DeltaY_P_P = (TH1F*)openOutFile->Get("h_DeltaY_P_P");

    // Define x range
    double xLow_1 = -2.5, xHigh_1 = 2.5;
    double xLow_2 = 0, xHigh_2 = 0;

    // Convert x range to bin numbers
    int binLow_1 = h_DeltaY_N_N->FindBin(xLow_1);
    int binHigh_1 = h_DeltaY_N_N->FindBin(xHigh_2);

    int binLow_2 = h_DeltaY_N_P->FindBin(xLow_1);
    int binHigh_2 = h_DeltaY_N_P->FindBin(xHigh_1);

    int binLow_3 = h_DeltaY_P_P->FindBin(xLow_2);
    int binHigh_3 = h_DeltaY_P_P->FindBin(xHigh_1);

    

    double integral_NN = h_DeltaY_N_N->Integral(binLow_1, binHigh_1);
    double integral_NP = h_DeltaY_N_P->Integral(binLow_3, binHigh_3);
    double integral_PN = h_DeltaY_P_N->Integral(binLow_1, binHigh_1);
    double integral_PP = h_DeltaY_P_P->Integral(binLow_3, binHigh_3);

    // double integral [2][2] = {
    //     {h_DeltaY_N_N->Integral(),h_DeltaY_P_N->Integral()},
    //     {h_DeltaY_N_P->Integral(),h_DeltaY_P_P->Integral()}
    //     };


    double integral [2][2] = {
        {integral_NN,integral_NP},
        {integral_PN,integral_PP}
        };

    for(int i=0; i<2; i++){
        for(int j=0; j<2; j++){
            Matrix->SetBinContent(i+1,j+1,integral[i][j]);
        }
    }

    TFile* outFileWrite = new TFile("0_250.root", "UPDATE");
    outFileWrite->cd();  
    Matrix->Write();
    outFileWrite->Close();

    std::cout << "DeltaY_gen < 0, DeltaY_reco < 0 " << " : "<< integral[0][0] << std::endl;
    std::cout << "DeltaY_gen < 0, DeltaY_reco > 0 " << " : "<< integral[0][1] << std::endl;
    std::cout << "DeltaY_gen > 0, DeltaY_reco < 0 " << " : "<< integral[1][0] << std::endl;
    std::cout << "DeltaY_gen > 0, DeltaY_reco > 0 " << " : "<< integral[1][1] << std::endl;

    openOutFile->Close();

    

    // TCanvas *c1 = new TCanvas("c1", "Canvas", 800, 600);
    // Matrix->Draw("colz");
    // c1->SaveAs("0_250.png");

}
