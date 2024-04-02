void plotLikelihoodScan(const char* fileName) {
    TFile* file = TFile::Open(fileName);
    TTree* tree = (TTree*)file->Get("limit");

    float deltaNLL, Ac;
    tree->SetBranchAddress("deltaNLL", &deltaNLL);
    tree->SetBranchAddress("Ac", &Ac);

    int n = tree->GetEntries();
    TGraph* graph = new TGraph(n);

    for (int i = 0; i < n; ++i) {
        tree->GetEntry(i);
        graph->SetPoint(i, Ac, 2*deltaNLL);
    }

    graph->SetTitle("Likelihood scan for Ac;Ac;2#DeltaNLL");
    graph->SetLineColor(kBlue);
    graph->SetLineWidth(2);
    graph->Draw("AL");

    // Draw the 1 sigma and 2 sigma lines
    TLine* line1 = new TLine(graph->GetXaxis()->GetXmin(), 1, graph->GetXaxis()->GetXmax(), 1);
    line1->SetLineColor(kRed);
    line1->SetLineStyle(2);
    line1->Draw("same");

    TLine* line2 = new TLine(graph->GetXaxis()->GetXmin(), 4, graph->GetXaxis()->GetXmax(), 4);
    line2->SetLineColor(kRed);
    line2->SetLineStyle(2);
    line2->Draw("same");
}

// root                                                                                   
// root [0] .L plotLikelihoodScan.C 
// root [1] plotLikelihoodScan("higgsCombine_paramFit_Test_TTbar_norm.MultiDimFit.mH125.root")



// root plotLikelihoodScan.C("../higgsCombine_paramFit_Test_TTbar_norm.MultiDimFit.mH125.root")

// void plotLikelihoodScan(const char* filename) {
//     TFile *file = TFile::Open(filename);
//     TTree *tree = (TTree*)file->Get("limit");

//     float deltaNLL, Ac;

//     tree->SetBranchAddress("deltaNLL", &deltaNLL);
//     tree->SetBranchAddress("Ac", &Ac);

//     // Create a graph for the likelihood scan
//     TGraph *graph = new TGraph();
//     int n = tree->GetEntries();
//     for (int i = 0; i < n; i++) {
//         tree->GetEntry(i);
//         graph->SetPoint(i, Ac, 2.0 * deltaNLL);  // 2*deltaNLL for 1 sigma confidence level
//     }

//     // Plotting
//     TCanvas *canvas = new TCanvas("canvas", "", 800, 600);
//     graph->SetTitle(";Ac;2#DeltaNLL");
//     graph->SetLineColor(kBlue);
//     graph->SetLineWidth(2);
//     graph->Draw("AL");

//     // Draw the line at 1 for 1 sigma
//     TLine *line = new TLine(Ac, 1, Ac, 1);
//     line->SetLineColor(kRed);
//     line->SetLineStyle(2);
//     line->Draw("same");

//     canvas->SaveAs("LikelihoodScan.png");
//     delete canvas;
// }
