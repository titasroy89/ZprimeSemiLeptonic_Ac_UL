#pragma once

#include "UHH2/core/include/Hists.h"
#include "UHH2/core/include/Event.h"
#include "UHH2/ZprimeSemiLeptonic/include/ZprimeCandidate.h"

class ZprimeSemiLeptonicEFTHists: public uhh2::Hists {
public:
    ZprimeSemiLeptonicEFTHists(uhh2::Context & ctx, const std::string & dirname);
    virtual void fill(const uhh2::Event & ev) override;
    virtual ~ZprimeSemiLeptonicEFTHists();

private:
    bool is_mc;
    bool debug;
    int n_weights;  // Number of EFT weights
    int weight_start_index;  // Starting index for EFT weights in systweights
    std::vector<std::string> hist_names;  // Dynamic size for weights
    
    // Event handles
    uhh2::Event::Handle<ZprimeCandidate*> h_BestZprimeCandidateChi2;
    uhh2::Event::Handle<bool> h_is_zprime_reconstructed_chi2;

    // Helper functions
    void init_weights(uhh2::Context & ctx);
    double get_nominal_weight(const uhh2::Event & event) const;
}; 