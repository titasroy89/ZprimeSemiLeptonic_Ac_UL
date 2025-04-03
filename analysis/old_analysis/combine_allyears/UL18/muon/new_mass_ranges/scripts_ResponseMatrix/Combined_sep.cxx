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
    std::vector<std::string> inputFiles = {"0_250.root", "250_500.root", "500_750.root", "750_900.root", "900Inf.root"};
    std::vector<std::string> matrixNames = {"0 < Mtt  <250", "250 < Mtt  <500", "500< Mtt <750", "750< Mtt <900", "900 < Mtt"};

    std::vector<TH2F*> Matrices;
    TFile *files[5];

    for (int i = 0; i < 5; ++i) {
        files[i] = new TFile(inputFiles[i].c_str(), "READ");
        TH2F* Matrix_i = (TH2F*)files[i]->Get(matrixNames[i].c_str());

        // Set title and labels
        Matrix_i->SetTitle(matrixNames[i].c_str());
        Matrix_i->GetXaxis()->SetTitle("#Delta |Y_{rec}|");
        Matrix_i->GetYaxis()->SetTitle("#Delta |Y_{gen}|");

        Matrices.push_back(Matrix_i);
    }

    TCanvas *canvas = new TCanvas("canvas", "Canvas", 800, 1000);
    canvas->Divide(1,5);

    for (int i = 0; i < 5; i++) {
        canvas->cd(i+1);
        // Draw the histogram
        Matrices[i]->Draw("colz");
        // Set the range for the x and y axis
        Matrices[i]->GetXaxis()->SetRangeUser(-2.5, 2.5);
        Matrices[i]->GetYaxis()->SetRangeUser(-2.5, 2.5);
    }

    // Save the canvas as a PNG file
    canvas->SaveAs("Combined_Matrix_sep.png");

}

