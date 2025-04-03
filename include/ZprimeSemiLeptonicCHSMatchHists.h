#pragma once

#include "UHH2/core/include/Hists.h"
#include "UHH2/core/include/Event.h"
#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicModules.h"

#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/TTbarReconstruction.h>
#include <UHH2/common/include/ReconstructionHypothesisDiscriminators.h>


class ZprimeSemiLeptonicCHSMatchHists: public uhh2::Hists {
public:
  explicit ZprimeSemiLeptonicCHSMatchHists(uhh2::Context&, const std::string&);
  virtual void fill(const uhh2::Event&) override;

protected:
  void init();
  bool is_mc;

TH1F *N_jets, *pt_jet, *pt_jet1, *pt_jet2, *pt_jet3, *eta_jet, *eta_jet1, *eta_jet2, *eta_jet3, *phi_jet, *phi_jet1, *phi_jet2, *phi_jet3, *m_jet, *m_jet1, *m_jet2, *m_jet3, *bscore_jet, *bscore_jet1, *bscore_jet2, *bscore_jet3, *N_bJets_loose, *N_bJets_med, *N_bJets_tight;
TH2F *eta_vs_pt;
TH1F *CHS_bjet_pt, *CHS_bjet_pt_low, *Puppi_bjet_pt, *Puppi_bjet_pt_low;
TH1F *CHS_bjet1_pt, *CHS_bjet2_pt, *Puppi_bjet1_pt, *Puppi_bjet2_pt;
TH1F *diff_bjet1_pt, *diff_bjet2_pt;
TH1F *diff_bjet_pt, *diff_bjet_pt_low, * ratio_diff_bjet_pt;

TH1F *diff_pt_btag, *diff_pt_btag_1, *diff_pt_btag_2, *diff_pt_btag_3;
TH1F *CHS_matched_N_Jets_NotTight,*CHS_matched_N_Jets_NotTight_all, *CHS_matched_N_Jets_NotTight_1, *CHS_matched_N_Jets_NotTight_2, *CHS_matched_N_Jets_NotTight_3;
TH1F *CHS_matched_N_Jets_LepVeto, *CHS_matched_N_Jets_Tight, *CHS_matched_N_Jets_LepVeto_all, *CHS_matched_N_Jets_Tight_all, *CHS_matched_N_Jets_LepVeto_1, *CHS_matched_N_Jets_Tight_1,*CHS_matched_N_Jets_LepVeto_2, *CHS_matched_N_Jets_Tight_2, *CHS_matched_N_Jets_LepVeto_3, *CHS_matched_N_Jets_Tight_3; 
TH1F *CHS_matched_N_jets, *CHS_matched_pt_jet, *CHS_matched_pt_jet1, *CHS_matched_pt_jet2, *CHS_matched_pt_jet3, *CHS_matched_eta_jet, *CHS_matched_eta_jet1, *CHS_matched_eta_jet2, *CHS_matched_eta_jet3, *CHS_matched_phi_jet, *CHS_matched_phi_jet1, *CHS_matched_phi_jet2, *CHS_matched_phi_jet3, *CHS_matched_m_jet, *CHS_matched_m_jet1, *CHS_matched_m_jet2, *CHS_matched_m_jet3, *CHS_matched_bscore_jet, *CHS_matched_bscore_jet1, *CHS_matched_bscore_jet2, *CHS_matched_bscore_jet3, *CHS_matched_N_bJets_loose, *CHS_matched_N_bJets_med, *CHS_matched_N_bJets_tight, *CHS_matched_deltaRmin_CHS_Puppi, *diff_pt, *diff_eta, *diff_pt_bin1, *diff_eta_bin1, *diff_pt_bin2, *diff_eta_bin2, *diff_pt_bin3, *diff_eta_bin3;
TH1F *ratio_chs_pt, *ratio_chs_pt_bin1, *ratio_chs_pt_bin2, *ratio_chs_pt_bin3, *ratio_puppi_pt, *ratio_puppi_pt_bin1, *ratio_puppi_pt_bin2, *ratio_puppi_pt_bin3;
TH1F *ratio_chs_eta, *ratio_chs_eta_bin1, *ratio_chs_eta_bin2, *ratio_chs_eta_bin3, *ratio_puppi_eta, *ratio_puppi_eta_bin1, *ratio_puppi_eta_bin2, *ratio_puppi_eta_bin3;
TH1F *ratio_chs_puppi_pt_bin3, *ratio_chs_puppi_pt_bin2, *ratio_chs_puppi_pt_bin1, *ratio_chs_puppi_pt;
TH1F *ratio_chs_puppi_eta_bin3, *ratio_chs_puppi_eta_bin2, *ratio_chs_puppi_eta_bin1, *ratio_chs_puppi_eta;

uhh2::Event::Handle< std::vector<Jet> > h_CHSjets_matched;
  virtual ~ZprimeSemiLeptonicCHSMatchHists();
};
