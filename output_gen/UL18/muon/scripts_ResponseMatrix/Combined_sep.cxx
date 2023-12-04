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


void Combined_sep() {



    TH2F* Matrix_Combined = new TH2F("Matrix_Combined", "Matrix_Combined", 15, 0, 15, 15, 0, 15);

    std::vector<std::string> inputFiles = {"0_250.root", "250_500.root", "500_750.root", "750_900.root", "900Inf.root"};
    std::vector<std::string> matrixNames = {"0 < Mtt  <250", "250 < Mtt  <500", "500< Mtt <750", "750< Mtt <900", "900 < Mtt"};

    // Counts of not-filled events for each individual matrix
    std::vector<int> notFilledCounts = {5, 7822927, 7376857, 1358807, 1189290};

    for (int i = 0; i < 5; ++i) {
        TFile* inFile = new TFile(inputFiles[i].c_str(), "READ");
        TH2F* Matrix_i = (TH2F*)inFile->Get(matrixNames[i].c_str());

        for (int x_bin = 0; x_bin < 2; ++x_bin) {
            for (int y_bin = 0; y_bin < 2; ++y_bin) {
                double bin_content = Matrix_i->GetBinContent(x_bin + 1, y_bin + 1);
                Matrix_Combined->SetBinContent(3*i + x_bin + 1, 3*i + y_bin + 1, bin_content);
            }
        }

        // Set the bin for not filled events for this matrix
        Matrix_Combined->SetBinContent(3*i + 3, 3*i + 3, notFilledCounts[i]);

        inFile->Close();
    }

    // Now let's update the labels.
    TAxis* xAxis = Matrix_Combined->GetXaxis();
    TAxis* yAxis = Matrix_Combined->GetYaxis();

    for (int i = 0; i < 5; ++i) {
        xAxis->SetBinLabel(3*i + 1, matrixNames[i].c_str());
        yAxis->SetBinLabel(3*i + 1, matrixNames[i].c_str());

        xAxis->SetBinLabel(3*i + 3, "Not filled");
        yAxis->SetBinLabel(3*i + 3, "Not filled");
    }

    TFile* outFile = new TFile("CombinedMatrix.root", "RECREATE");
    Matrix_Combined->Write("Matrix_Combined");

    TCanvas *c1 = new TCanvas("c1", "Canvas", 800, 600);
    gStyle->SetPalette(1);
    gStyle->SetOptStat(0);
    Matrix_Combined->Draw("COLZ");
    c1->SaveAs("CombinedMatrix.png");

    outFile->Close();
}
