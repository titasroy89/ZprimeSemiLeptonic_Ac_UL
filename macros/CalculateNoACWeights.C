#include <iostream>
#include <vector>
#include <string>
#include <glob.h>
#include <memory>

#include "TFile.h"
#include "TTree.h"
#include "TH1D.h"
#include "TString.h"
#include "TChain.h"

// Run this macro once to generate the NoAC_Weights_GEN.root file.
// Usage: root -l -b -q CalculateNoACWeights.C

void CalculateNoACWeights() {
    // ---------------- CONFIGURATION ----------------
    // Input path (from your XML)
    string input_pattern = "/data/dust/user/titasroy/Files_fromBeren/workdir_Preselection_UL17_templatemethod/uhh2.AnalysisModuleRunner.MC.TTToSemiLeptonic_UL17_*.root";
    
    // Output file name
    string output_file = "NoAC_Weights_GEN.root";
    
    // Mtt binning (must match your C++ code)
    std::vector<double> mtt_edges = {0.0, 350.0, 500.0, 750.0, 1000.0, 1500.0, 10000.0};
    // -----------------------------------------------

    cout << "--- Starting NoAC Weight Pre-calculation ---" << endl;
    cout << "Input pattern: " << input_pattern << endl;

    // Glob files
    glob_t gl;
    glob(input_pattern.c_str(), 0, nullptr, &gl);
    vector<string> files;
    for(size_t i=0; i<gl.gl_pathc; ++i) files.push_back(gl.gl_pathv[i]);
    globfree(&gl);

    if(files.empty()) {
        cerr << "ERROR: No files found matching pattern!" << endl;
        return;
    }
    cout << "Found " << files.size() << " files." << endl;

    // Create Chain to handle multiple files easier
    TChain* chain = new TChain("AnalysisTree");
    for(const auto& f : files) {
        chain->Add(f.c_str());
    }

    // Create Output Histograms
    // 1. Inclusive
    TH1D* h_inclusive = new TH1D("Hgen_sum_from_tree", "GEN histogram inclusive", 300, -1.0, 1.0);
    h_inclusive->Sumw2();

    // 2. Mtt-binned
    int n_mtt = mtt_edges.size() - 1;
    vector<TH1D*> h_mtt(n_mtt);
    for(int i=0; i<n_mtt; ++i) {
        TString name = TString::Format("Hgen_sum_from_tree_mttbin%d", i);
        h_mtt[i] = new TH1D(name, TString::Format("GEN histogram mtt bin %d", i), 300, -1.0, 1.0);
        h_mtt[i]->Sumw2();
    }

    // Processing
    // We use TTree::Draw for efficiency, but on a Chain it might still be slow if not careful.
    // For large datasets, it's often faster to disable unneeded branches, but Draw handles that.
    
    cout << "Drawing Inclusive Histogram..." << endl;
    // Check if weight branch exists
    bool has_weight = chain->GetBranch("weight");
    TString base_sel = "(xi_gen > -1.1 && xi_gen < 1.1)"; // Basic sanity cut
    TString weight_expr = has_weight ? (base_sel + " * weight") : base_sel;

    // Inclusive
    chain->Draw("xi_gen >> Hgen_sum_from_tree", weight_expr, "goff");
    cout << "  Entries: " << h_inclusive->GetEntries() << endl;

    // Mtt bins
    for(int i=0; i<n_mtt; ++i) {
        cout << "Drawing Mtt Bin " << i << " (" << mtt_edges[i] << " to " << mtt_edges[i+1] << ")..." << endl;
        TString bin_sel = TString::Format("(%s && mtt_gen >= %f && mtt_gen < %f)", base_sel.Data(), mtt_edges[i], mtt_edges[i+1]);
        TString bin_weight_expr = has_weight ? (bin_sel + " * weight") : bin_sel;
        
        chain->Draw(TString::Format("xi_gen >> Hgen_sum_from_tree_mttbin%d", i), bin_weight_expr, "goff");
        cout << "  Entries: " << h_mtt[i]->GetEntries() << endl;
    }

    // Save to file
    cout << "Saving to " << output_file << "..." << endl;
    TFile* out = TFile::Open(output_file.c_str(), "RECREATE");
    h_inclusive->Write();
    for(auto h : h_mtt) h->Write();
    out->Close();

    cout << "Done! Copy " << output_file << " to a location accessible by your jobs and update your XML." << endl;
}

