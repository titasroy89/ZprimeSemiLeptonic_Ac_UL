#pragma once

#include "UHH2/core/include/Hists.h"
#include "UHH2/core/include/Event.h"
#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicModules.h"

#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/TTbarReconstruction.h>
#include <UHH2/common/include/ReconstructionHypothesisDiscriminators.h>



#include <TLorentzVector.h>
#include "TH1F.h"
#include <string>
#include <math.h>
#include <sstream>
#include <iostream>

namespace uhh2 {

  class ZprimeSemiLeptonicPDFHists: public uhh2::Hists {
  public:
    explicit ZprimeSemiLeptonicPDFHists(uhh2::Context&, const std::string&);
    virtual void fill(const uhh2::Event&) override;
    std::string hist_names[100];
    std::string hist_names_tt[100];
    std::string hist_names_dy_d1[100];
    std::string hist_names_dy_d2[100];
    std::string hist_names_sigma_1[100];
    std::string hist_names_sigma_2[100];
    

  protected:
    bool is_mc;
    bool is_dy;
    bool is_tt;
    bool is_wjets;
    bool is_qcd_HTbinned;
    bool is_alps;
    bool is_azh;
    bool is_htott_scalar;
    bool is_htott_pseudo;
    bool is_zprimetott;
    bool isMuon;
    bool isElectron;
    bool debug;
    bool ishotvr, isdeepAK8;
  
    uhh2::Event::Handle< std::vector<TopJet> > h_AK8TopTags;
    uhh2::Event::Handle< std::vector<Jet> > h_CHSjets_matched;
    uhh2::Event::Handle<bool> h_is_zprime_reconstructed_chi2;
    uhh2::Event::Handle<ZprimeCandidate*> h_BestZprimeCandidateChi2;
    uhh2::Event::Handle<std::vector<ReconstructionHypothesis>> h_ttbar_hyps;
    virtual ~ZprimeSemiLeptonicPDFHists();
  };
}