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

// void rebin() {

// TFile *inputFile = new TFile("ttbar.root");
// TTree *tree = (TTree*)inputFile->Get("AnalysisTree");

// TH1F *h = new TH1F("h", "DeltaR", 20, -0.5, 0.5);

// // Fill the histogram with data from the TTree.
// tree->Draw("DeltaR_jet_genparticle>>h");

// TFile *outputFile = new TFile("output.root", "RECREATE");
// h->Write();
// outputFile->Close();

// // Don't forget to close the input file as well.
// inputFile->Close();
// }

void noreco() {

    // Create a chain of trees
    TChain *chain = new TChain("AnalysisTree");

    // Add the trees from the two files to the chain
    chain->Add("semi1.root");
    chain->Add("other.root");

    // Create the histogram
    TH1F *h1 = new TH1F("h1", "not_reconstructed", 20,0,1000 );
    TH1F *h2 = new TH1F("h2", "not_reconstructed 0 < mtt < 250", 20,0,1000);
    TH1F *h3 = new TH1F("h3", "not_reconstructed 250 < mtt < 500", 20,0,1000);
    TH1F *h4 = new TH1F("h4", "not_reconstructed 500 < mtt < 750",20,0,1000);
    TH1F *h5 = new TH1F("h5", "not_reconstructed 750 < mtt < 900", 20, 0,1000);
    TH1F *h6 = new TH1F("h6", "not_reconstructed 900 < mtt", 20, 0,1000);


    // Fill the histogram with data from the chain
    chain->Draw("not_reconstructed>>h1", "", "goff");
    chain->Draw("not_reconstructed_0_250>>h2", "", "goff");
    chain->Draw("not_reconstructed_250_500>>h3", "", "goff");
    chain->Draw("not_reconstructed_500_750>>h4", "", "goff");
    chain->Draw("not_reconstructed_750_900>>h5", "", "goff");
    chain->Draw("not_reconstructed_900Inf>>h6", "", "goff");

    // Write the histogram to the output file
    TFile *outputFile = new TFile("output_notreco2.root", "RECREATE");
    cout << "not_reconstructed" << h1->Integral()<<endl;
    cout << "not_reconstructed_0_250" << h2->Integral()<<endl;
    cout << "not_reconstructed_250_500" << h3->Integral()<<endl;
    cout << "not_reconstructed_500_750" << h4->Integral()<<endl;
    cout << "not_reconstructed_750_900" << h5->Integral()<<endl;
    cout << "not_reconstructed_900Inf" << h6->Integral()<<endl;

    h1->Write();
    h2->Write();
    h3->Write();
    h4->Write();
    h5->Write();
    h6->Write();
    
    outputFile->Close();

   
}

