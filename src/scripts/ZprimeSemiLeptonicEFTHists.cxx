#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicEFTHists.h"
#include "UHH2/core/include/Event.h"
#include <UHH2/core/include/Utils.h>
#include <UHH2/common/include/Utils.h>
#include <math.h>
#include <sstream>

using namespace std;
using namespace uhh2;

ZprimeSemiLeptonicEFTHists::ZprimeSemiLeptonicEFTHists(Context & ctx, const string& dirname): 
Hists(ctx, dirname) {
    is_mc = ctx.get("dataset_type") == "MC";
    debug = false;
    
    // Get handles
    h_BestZprimeCandidateChi2 = ctx.get_handle<ZprimeCandidate*>("ZprimeCandidateBestChi2");
    h_is_zprime_reconstructed_chi2 = ctx.get_handle<bool>("is_zprime_reconstructed_chi2");

    // Initialize weights
    init_weights(ctx);

    // Book histograms for each EFT weight
    for(int i=0; i < n_weights; i++) {
        std::stringstream ss_name;
        ss_name << "EFT_weight_" << i;
        hist_names.push_back(ss_name.str());
        
        // Book weight distribution histogram
        book<TH1F>(hist_names[i].c_str(), 
                   ("EFT weight " + to_string(i)).c_str(), 
                   100, -10, 10);

        // Book weight vs mass histogram
        book<TH2F>((hist_names[i] + "_vs_mass").c_str(),
                   ("EFT weight " + to_string(i) + " vs m_{t#bar{t}}").c_str(),
                   100, 0, 5000,  // mass bins
                   100, -10, 10); // weight bins
    }

    // Book summary histograms
    book<TH1F>("n_weights", "Number of EFT weights", 1, 0, 1);
    book<TH1F>("weight_start_index", "Start index of EFT weights", 1, 0, 1);
}

void ZprimeSemiLeptonicEFTHists::init_weights(Context & ctx) {
    // Set number of weights and starting index based on dataset
    if(ctx.get("dataset_version").find("EFT") != string::npos) {
        n_weights = 1677;  // Update this based on your actual number of weights
        weight_start_index = 9;  // Update this based on your weight structure
    } else {
        n_weights = 0;
        weight_start_index = 0;
    }
}

double ZprimeSemiLeptonicEFTHists::get_nominal_weight(const Event & event) const {
    if(!event.genInfo) return 1.0;
    return event.genInfo->weights().size() > 0 ? event.genInfo->weights().at(0) : 1.0;
}

void ZprimeSemiLeptonicEFTHists::fill(const Event & event) {
    if(!is_mc || n_weights == 0) return;

    double weight = event.weight;
    double nominal_weight = get_nominal_weight(event);
    
    // Fill summary histograms
    hist("n_weights")->Fill(0.5, n_weights);
    hist("weight_start_index")->Fill(0.5, weight_start_index);

    bool is_zprime_reconstructed = event.get(h_is_zprime_reconstructed_chi2);
    if(!is_zprime_reconstructed) return;

    ZprimeCandidate* cand = event.get(h_BestZprimeCandidateChi2);
    double mttbar = cand ? cand->Zprime_v4().M() : -1;
    
    // Access EFT weights from genInfo
    if(event.genInfo && event.genInfo->systweights().size() > (unsigned int)(weight_start_index + n_weights)) {
        for(int i=0; i < n_weights; i++) {
            double eft_weight = event.genInfo->systweights().at(i + weight_start_index);
            double weight_ratio = eft_weight / nominal_weight;
            
            // Fill weight distribution
            hist(hist_names[i])->Fill(weight_ratio, weight);
            
            // Fill weight vs mass correlation if mass is valid
            if(mttbar > 0) {
                TH2F* h2 = dynamic_cast<TH2F*>(hist(hist_names[i] + "_vs_mass"));
                if(h2) h2->Fill(mttbar, weight_ratio, weight);
            }
        }
    }
}

ZprimeSemiLeptonicEFTHists::~ZprimeSemiLeptonicEFTHists(){} 