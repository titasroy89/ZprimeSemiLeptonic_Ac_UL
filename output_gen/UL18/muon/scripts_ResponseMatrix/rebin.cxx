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

void rebin() {

    // Create a chain of trees
    TChain *chain = new TChain("AnalysisTree");

    // Add the trees from the two files to the chain
    chain->Add("semi1.root");
    chain->Add("other.root");

    // Create the histogram
    TH1F *h1 = new TH1F("h1", "DeltaR hadronic", 20, -0.5, 0.5);
    TH1F *h2 = new TH1F("h2", "DeltaR leptonic", 20, -0.5, 0.5);

    // Fill the histogram with data from the chain
    chain->Draw("DeltaR_hadronic_genparticle>>h1", "", "goff");
    chain->Draw("DeltaR_leptonic_genparticle>>h2", "", "goff");

    // Write the histogram to the output file
    TFile *outputFile = new TFile("output.root", "RECREATE");
    h1->Write();
    h2->Write();
    outputFile->Close();

   
}

