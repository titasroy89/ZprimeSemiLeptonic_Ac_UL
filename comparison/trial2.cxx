#include <TFile.h>
#include <TH1.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <iostream>

void trial2()
{

// 	TFile file("General.root","read");
// 	TCanvas *c1 = (TCanvas*)file.Get("OSU1000_10");
// 	TGraphAsymmErrors *ae = (TGraphAsymmErrors*)c1->GetPrimitive("OSU1000_10");
// 	TH1F *h = (TH1F*)ae->GetHistogram();
// 	TCanvas c2;
//    h->Draw();

//    TFile outputFile("Output.root", "recreate"); // Create the output ROOT file

//    TFile f("General.root", "read");

//    TCanvas *c1 = (TCanvas*)f.Get("OSU1000_10");
//    TGraphAsymmErrors *ae = (TGraphAsymmErrors*)c1->GetPrimitive("OSU1000_10");

//    TCanvas *c2 = (TCanvas*)f.Get("UIC1000_10");
//    TH1D *h1 = nullptr;

//    TList* l = c2->GetListOfPrimitives();
//    TIter next(l);
//    TObject *obj;
//    while ((obj = next())) {
//       if (obj->InheritsFrom(TH1D::Class())) {
//          h1 = (TH1D*)obj;
//          break; // Exit the loop once a TH1D object is found
//       }
//    }

//    if (h1) {
//       TCanvas c3;
//       h1->Draw();
//       ae->Draw("L");
// 	  h1 ->Write("OSU1000_10_2");
// 	  ae->Write("UIC1000_10_2");
//    }

const char* h_1="OSU1200_13";
const char* h_2="UIC1200_13";
// const char* h_3="Cor800_8";

const char* n_1="OSU 1200e";
const char* n_2="UIC 1200e";
// const char* n_3="Cornell 800e";

TFile *file = TFile::Open("General_Occ.root");
TCanvas *c1 = (TCanvas*)file->Get(h_1);
TCanvas *c2 = (TCanvas*)file->Get(h_2);
// TCanvas *c3 = (TCanvas*)file->Get(h_3);

TCanvas *cnew = new TCanvas("cnew", "cnew", 800, 600);
bool first = true;

// TCanvas* canvases[3] = {c1, c2, c3};
TCanvas* canvases[2] = {c1, c2};
int color1 = kRed;
int color2 = kBlue;
// int color3 = TColor::GetColor("#006400");  // Dark green
// int color3 = kGreen; 
// int colors[3] = {color1, color2, color3};  // Colors for the histograms
int colors[2] = {color1, color2};  // Colors for the histograms


// const char* names[3] = {n_1, n_2,n_3};

const char* names[2] = {n_1, n_2};


// Create a legend
TLegend *legend = new TLegend(0.7,0.7,0.9,0.9);

for (int i = 0; i < 2; i++) {
  TCanvas *c = canvases[i];
  TIter next(c->GetListOfPrimitives());
  TObject *obj;

  while ((obj = next())) {
    if (obj->InheritsFrom(TH1F::Class())) {
      TH1F *h = (TH1F*)obj;

      // Set the line color
      h->SetLineColor(colors[i]);
	  h->SetLineWidth(2);

      if (first) {
        h->Draw();
        first = false;
      } else {
        h->Draw("SAME");
      }

      // Add the histogram to the legend
      legend->AddEntry(h, names[i], "l");
    }
  }
}

// Draw the legend
legend->Draw();

cnew->Update();
cnew->SaveAs("trial.pdf");

}