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

void Combined() {
    
    TH2F* Matrix_Combined = new TH2F("Matrix_Combined", "Matrix_Combined", 10, -2.5, 22.5, 10 , -2.5,22.5);

    std::vector<std::string> inputFiles = {"0_250.root", "250_500.root", "500_750.root", "750_900.root", "900Inf.root"};
    std::vector<std::string> matrixNames = {"0 < Mtt  <250", "250 < Mtt  <500", "500< Mtt <750", "750< Mtt <900", "900 < Mtt"};


    for (int i = 0; i < 5; ++i) {
        TFile* inFile = new TFile(inputFiles[i].c_str(), "READ");
        TH2F* Matrix_i = (TH2F*)inFile->Get(matrixNames[i].c_str());
        
        for (int x_bin = 0; x_bin < 2; ++x_bin) {
            for (int y_bin = 0; y_bin < 2; ++y_bin) {
                double bin_content = Matrix_i->GetBinContent(x_bin + 1, y_bin + 1);
                Matrix_Combined->SetBinContent(2*i + x_bin + 1, 2*i + y_bin + 1, bin_content);
            }
        }
        inFile->Close();
    }

    TFile* outFile = new TFile("CombinedMatrix.root", "RECREATE");

    Matrix_Combined->GetXaxis()->SetTitle("#Delta |Y_{rec}|");
    Matrix_Combined->GetYaxis()->SetTitle("#Delta |Y_{gen}|");
    Matrix_Combined->Write("Matrix_Combined");

    TCanvas *c1 = new TCanvas("c1", "Canvas", 800, 600);
    gStyle->SetPalette(1);
    gStyle->SetOptStat(0);
    Matrix_Combined->Draw("COLZ");
    c1->SaveAs("CombinedMatrix.png");


    outFile->Close();

}