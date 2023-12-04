#include <TFile.h>
#include <TH2F.h>
#include <TH1D.h>
#include <TCanvas.h>
#include <TPaveText.h>
#include <iostream>


void projectOnY() {
    TFile* file = new TFile("500_750.root", "READ");
    if (!file->IsOpen()) {
        std::cerr << "Error opening file." << std::endl;
        return;
    }
    
    TH2F* h2D = (TH2F*) file->Get("500< Mtt <750");
    if (!h2D) {
        std::cerr << "2D histogram not found." << std::endl;
        file->Close();
        return;
    }

    TH1D* hX1 = h2D->ProjectionX("#Delta |Y_{gen}| < 0", 1, 1);  
    TH1D* hX2 = h2D->ProjectionX("#Delta |Y_{gen}| > 0", 2, 2);  

    if (!hX1 || !hX2) {
        std::cerr << "Error projecting onto Y-axis." << std::endl;
        file->Close();
        return;
    }

    hX1->GetXaxis()->SetTitle("#Delta |Y_{rec}|");
    hX2->GetXaxis()->SetTitle("#Delta |Y_{rec}|");


    TPaveText* label1 = new TPaveText(0.65, 0.8, 0.7, 0.85, "NDC"); // NDC sets coordinates to be relative to pad dimensions
    label1->AddText("#Delta |Y_{gen}| < 0");
    label1->SetTextSize(0.04);
    label1->SetFillColor(0); // transparent background

    TPaveText* label2 = new TPaveText(0.65, 0.8, 0.7, 0.85, "NDC");
    label2->AddText("#Delta |Y_{gen}| > 0");
    label2->SetTextSize(0.04);
    label2->SetFillColor(0);

    // Print the projections
    std::cout << "Projection for first x-bin: " << hX1->GetBinContent(1) << std::endl;
    std::cout << "Projection for second x-bin: " << hX2->GetBinContent(1) << std::endl;

    TCanvas* c1 = new TCanvas("dY_gen<0", "dY_gen<0", 800, 600);
    hX1->Draw();
    label1->Draw("same");
    c1->Modified();
    c1->Update();
    c1->SaveAs("projectionX1.png");

    TCanvas* c2 = new TCanvas("DY_gen>0", "DY_gen>0", 800, 600);
    hX2->Draw();
    label2->Draw("same");
    c2->Modified();
    c2->Update();
    c2->SaveAs("projectionX2.png");

    // Clean up
    file->Close();
}

int main() {
    projectOnY();
    return 0;
}
