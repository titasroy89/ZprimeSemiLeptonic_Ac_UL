#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicSystematicsHists.h"
#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicModules.h"
#include "UHH2/core/include/Event.h"
#include <UHH2/core/include/Utils.h>
#include <UHH2/common/include/Utils.h>
#include "UHH2/common/include/JetIds.h"
#include <math.h>

#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/TTbarReconstruction.h>
#include <UHH2/common/include/ReconstructionHypothesisDiscriminators.h>

#include <UHH2/core/include/LorentzVector.h>

#include "TH1F.h"
#include "TH2D.h"
#include "TH2F.h"
#include <iostream>
#include <string>

using namespace std;
using namespace uhh2;

ZprimeSemiLeptonicSystematicsHists::ZprimeSemiLeptonicSystematicsHists(uhh2::Context& ctx, const std::string& dirname):
Hists(ctx, dirname) {

  is_mc = ctx.get("dataset_type") == "MC";
  is_Muon = ctx.get("channel") == "muon";
  is_tt = ctx.get("dataset_version").find("TTTo") == 0;

  isMuon = false; isElectron = false;
  if(ctx.get("channel") == "muon") isMuon = true;
  if(ctx.get("channel") == "electron") isElectron = true;

  h_ele_reco           = ctx.get_handle<float>("weight_sfelec_reco");
  h_ele_reco_up        = ctx.get_handle<float>("weight_sfelec_reco_up");
  h_ele_reco_down      = ctx.get_handle<float>("weight_sfelec_reco_down");
  h_ele_id             = ctx.get_handle<float>("weight_sfelec_id");
  h_ele_id_up          = ctx.get_handle<float>("weight_sfelec_id_up");
  h_ele_id_down        = ctx.get_handle<float>("weight_sfelec_id_down");
  h_ele_trigger        = ctx.get_handle<float>("weight_sfelec_trigger");
  h_ele_trigger_up     = ctx.get_handle<float>("weight_sfelec_trigger_up");
  h_ele_trigger_down   = ctx.get_handle<float>("weight_sfelec_trigger_down");
  h_mu_reco            = ctx.get_handle<float>("weight_sfmu_reco");
  h_mu_reco_up         = ctx.get_handle<float>("weight_sfmu_reco_up");
  h_mu_reco_down       = ctx.get_handle<float>("weight_sfmu_reco_down");
  h_mu_iso             = ctx.get_handle<float>("weight_sfmu_iso");
  h_mu_iso_up          = ctx.get_handle<float>("weight_sfmu_iso_up");
  h_mu_iso_down        = ctx.get_handle<float>("weight_sfmu_iso_down");
  h_mu_id              = ctx.get_handle<float>("weight_sfmu_id");
  h_mu_id_up           = ctx.get_handle<float>("weight_sfmu_id_up");
  h_mu_id_down         = ctx.get_handle<float>("weight_sfmu_id_down");
  h_mu_trigger         = ctx.get_handle<float>("weight_sfmu_trigger");
  h_mu_trigger_up      = ctx.get_handle<float>("weight_sfmu_trigger_up");
  h_mu_trigger_down    = ctx.get_handle<float>("weight_sfmu_trigger_down");
  h_pu                 = ctx.get_handle<float>("weight_pu");
  h_pu_up              = ctx.get_handle<float>("weight_pu_up");
  h_pu_down            = ctx.get_handle<float>("weight_pu_down");
  h_prefiring          = ctx.get_handle<float>("prefiringWeight");
  h_prefiring_up       = ctx.get_handle<float>("prefiringWeightUp");
  h_prefiring_down     = ctx.get_handle<float>("prefiringWeightDown");
  h_murmuf_upup        = ctx.get_handle<float>("weight_murmuf_upup");
  h_murmuf_upnone      = ctx.get_handle<float>("weight_murmuf_upnone");
  h_murmuf_noneup      = ctx.get_handle<float>("weight_murmuf_noneup");
  h_murmuf_nonedown    = ctx.get_handle<float>("weight_murmuf_nonedown");
  h_murmuf_downnone    = ctx.get_handle<float>("weight_murmuf_downnone");
  h_murmuf_downdown    = ctx.get_handle<float>("weight_murmuf_downdown");
  h_isr_up             = ctx.get_handle<float>("weight_isr_2_up");
  h_isr_down           = ctx.get_handle<float>("weight_isr_2_down");
  h_fsr_up             = ctx.get_handle<float>("weight_fsr_2_up");
  h_fsr_down           = ctx.get_handle<float>("weight_fsr_2_down");
  h_btag               = ctx.get_handle<float>("weight_btagdisc_central");
  h_btag_cferr1_up     = ctx.get_handle<float>("weight_btagdisc_cferr1_up");
  h_btag_cferr1_down   = ctx.get_handle<float>("weight_btagdisc_cferr1_down");
  h_btag_cferr2_up     = ctx.get_handle<float>("weight_btagdisc_cferr2_up");
  h_btag_cferr2_down   = ctx.get_handle<float>("weight_btagdisc_cferr2_down");
  h_btag_hf_up         = ctx.get_handle<float>("weight_btagdisc_hf_up");
  h_btag_hf_down       = ctx.get_handle<float>("weight_btagdisc_hf_down");
  h_btag_hfstats1_up   = ctx.get_handle<float>("weight_btagdisc_hfstats1_up");
  h_btag_hfstats1_down = ctx.get_handle<float>("weight_btagdisc_hfstats1_down");
  h_btag_hfstats2_up   = ctx.get_handle<float>("weight_btagdisc_hfstats2_up");
  h_btag_hfstats2_down = ctx.get_handle<float>("weight_btagdisc_hfstats2_down");
  h_btag_lf_up         = ctx.get_handle<float>("weight_btagdisc_lf_up");
  h_btag_lf_down       = ctx.get_handle<float>("weight_btagdisc_lf_down");
  h_btag_lfstats1_up   = ctx.get_handle<float>("weight_btagdisc_lfstats1_up");
  h_btag_lfstats1_down = ctx.get_handle<float>("weight_btagdisc_lfstats1_down");
  h_btag_lfstats2_up   = ctx.get_handle<float>("weight_btagdisc_lfstats2_up");
  h_btag_lfstats2_down = ctx.get_handle<float>("weight_btagdisc_lfstats2_down");
  h_ttag               = ctx.get_handle<float>("weight_toptagsf");
  h_ttag_corr_up       = ctx.get_handle<float>("weight_toptagsf_corr_up");
  h_ttag_corr_down     = ctx.get_handle<float>("weight_toptagsf_corr_down");
  h_ttag_uncorr_up     = ctx.get_handle<float>("weight_toptagsf_uncorr_up");
  h_ttag_uncorr_down   = ctx.get_handle<float>("weight_toptagsf_uncorr_down");
  h_tmistag            = ctx.get_handle<float>("weight_topmistagsf");
  h_tmistag_up         = ctx.get_handle<float>("weight_topmistagsf_up");
  h_tmistag_down       = ctx.get_handle<float>("weight_topmistagsf_down");
  // h_toppt              = ctx.get_handle<float>("weight_toppt");
  // h_toppt_up           = ctx.get_handle<float>("weight_toppt_up");
  // h_toppt_down         = ctx.get_handle<float>("weight_toppt_down");


  h_BestZprimeCandidateChi2 = ctx.get_handle<ZprimeCandidate*>("ZprimeCandidateBestChi2");
  h_is_zprime_reconstructed_chi2 = ctx.get_handle<bool>("is_zprime_reconstructed_chi2");
  init();
}

void ZprimeSemiLeptonicSystematicsHists::init(){

  // Zprime reconstruction
  DeltaY                    = book<TH1F>("DeltaY", "#DeltaY_{t#bar{t}} ",                                       2, -2.5, 2.5);
  DeltaY_mu_reco_up         = book<TH1F>("DeltaY_mu_reco_up",   "#DeltaY_{t#bar{t}} mu_reco_up",                2, -2.5, 2.5);
  DeltaY_mu_reco_down       = book<TH1F>("DeltaY_mu_reco_down", "#DeltaY_{t#bar{t}} mu_reco_down",              2, -2.5, 2.5);
  DeltaY_pu_up              = book<TH1F>("DeltaY_pu_up",   "#DeltaY_{t#bar{t}} pu_up",                          2, -2.5, 2.5);
  DeltaY_pu_down            = book<TH1F>("DeltaY_pu_down", "#DeltaY_{t#bar{t}} pu_down",                        2, -2.5, 2.5);
  DeltaY_prefiring_up       = book<TH1F>("DeltaY_prefiring_up",   "#DeltaY_{t#bar{t}} prefiring_up",            2, -2.5, 2.5);
  DeltaY_prefiring_down     = book<TH1F>("DeltaY_prefiring_down", "#DeltaY_{t#bar{t}} prefiring_down",          2, -2.5, 2.5);
  DeltaY_mu_id_up           = book<TH1F>("DeltaY_mu_id_up",   "#DeltaY_{t#bar{t}} mu_id_up",                    2, -2.5, 2.5);
  DeltaY_mu_id_down         = book<TH1F>("DeltaY_mu_id_down", "#DeltaY_{t#bar{t}} mu_id_down",                  2, -2.5, 2.5);
  DeltaY_mu_iso_up          = book<TH1F>("DeltaY_mu_iso_up",   "#DeltaY_{t#bar{t} mu_iso_up",                   2, -2.5, 2.5);
  DeltaY_mu_iso_down        = book<TH1F>("DeltaY_mu_iso_down", "#DeltaY_{t#bar{t}} mu_iso_down",                2, -2.5, 2.5);
  DeltaY_mu_trigger_up      = book<TH1F>("DeltaY_mu_trigger_up",   "#DeltaY_{t#bar{t}} mu_trigger_up",          2, -2.5, 2.5);
  DeltaY_mu_trigger_down    = book<TH1F>("DeltaY_mu_trigger_down", "#DeltaY_{t#bar{t}} mu_trigger_down",        2, -2.5, 2.5);
  DeltaY_ele_id_up          = book<TH1F>("DeltaY_ele_id_up",   "#DeltaY_{t#bar{t}} ele_id_up",                  2, -2.5, 2.5);
  DeltaY_ele_id_down        = book<TH1F>("DeltaY_ele_id_down", "#DeltaY_{t#bar{t}} ele_id_down",                2, -2.5, 2.5);
  DeltaY_ele_trigger_up     = book<TH1F>("DeltaY_ele_trigger_up",   "#DeltaY_{t#bar{t}} ele_trigger_up",        2, -2.5, 2.5);
  DeltaY_ele_trigger_down   = book<TH1F>("DeltaY_ele_trigger_down", "#DeltaY_{t#bar{t}} ele_trigger_down",      2, -2.5, 2.5);
  DeltaY_ele_reco_up        = book<TH1F>("DeltaY_ele_reco_up",   "#DeltaY_{t#bar{t}} ele_reco_up",              2, -2.5, 2.5);
  DeltaY_ele_reco_down      = book<TH1F>("DeltaY_ele_reco_down", "#DeltaY_{t#bar{t}} ele_reco_down",            2, -2.5, 2.5);
  DeltaY_murmuf_upup        = book<TH1F>("DeltaY_murmuf_upup", "#DeltaY_{t#bar{t}} murmuf_upup",                2, -2.5, 2.5);
  DeltaY_murmuf_upnone      = book<TH1F>("DeltaY_murmuf_upnone", "#DeltaY_{t#bar{t}} murmuf_upnone",            2, -2.5, 2.5);
  DeltaY_murmuf_noneup      = book<TH1F>("DeltaY_murmuf_noneup", "#DeltaY_{t#bar{t}} murmuf_noneup",            2, -2.5, 2.5);
  DeltaY_murmuf_nonedown    = book<TH1F>("DeltaY_murmuf_nonedown", "#DeltaY_{t#bar{t}} murmuf_nonedown",        2, -2.5, 2.5);
  DeltaY_murmuf_downnone    = book<TH1F>("DeltaY_murmuf_downnone", "#DeltaY_{t#bar{t}} murmuf_downnone",        2, -2.5, 2.5);
  DeltaY_murmuf_downdown    = book<TH1F>("DeltaY_murmuf_downdown", "#DeltaY_{t#bar{t}} murmuf_downdown",        2, -2.5, 2.5);
  DeltaY_isr_up             = book<TH1F>("DeltaY_isr_up", "#DeltaY_{t#bar{t}} isr_up",                          2, -2.5, 2.5);
  DeltaY_isr_down           = book<TH1F>("DeltaY_isr_down", "#DeltaY_{t#bar{t}} isr_down",                      2, -2.5, 2.5);
  DeltaY_fsr_up             = book<TH1F>("DeltaY_fsr_up", "#DeltaY_{t#bar{t}} fsr_up",                          2, -2.5, 2.5);
  DeltaY_fsr_down           = book<TH1F>("DeltaY_fsr_down", "#DeltaY_{t#bar{t}} fsr_down",                      2, -2.5, 2.5);
  DeltaY_btag_cferr1_up     = book<TH1F>("DeltaY_btag_cferr1_up", "#DeltaY_{t#bar{t}} btag_cferr1_up",          2, -2.5, 2.5);
  DeltaY_btag_cferr1_down   = book<TH1F>("DeltaY_btag_cferr1_down", "#DeltaY_{t#bar{t}} btag_cferr1_down",      2, -2.5, 2.5);
  DeltaY_btag_cferr2_up     = book<TH1F>("DeltaY_btag_cferr2_up", "#DeltaY_{t#bar{t}} btag_cferr2_up",          2, -2.5, 2.5);
  DeltaY_btag_cferr2_down   = book<TH1F>("DeltaY_btag_cferr2_down", "#DeltaY_{t#bar{t}} btag_cferr2_down",      2, -2.5, 2.5);
  DeltaY_btag_hf_up         = book<TH1F>("DeltaY_btag_hf_up", "#DeltaY_{t#bar{t}} btag_hf_up",                  2, -2.5, 2.5);
  DeltaY_btag_hf_down       = book<TH1F>("DeltaY_btag_hf_down", "#DeltaY_{t#bar{t}} btag_hf_down",              2, -2.5, 2.5);
  DeltaY_btag_hfstats1_up   = book<TH1F>("DeltaY_btag_hfstats1_up", "#DeltaY_{t#bar{t}} btag_hfstats1_up",      2, -2.5, 2.5);
  DeltaY_btag_hfstats1_down = book<TH1F>("DeltaY_btag_hfstats1_down", "#DeltaY_{t#bar{t}} btag_hfstats1_down",  2, -2.5, 2.5);
  DeltaY_btag_hfstats2_up   = book<TH1F>("DeltaY_btag_hfstats2_up", "#DeltaY_{t#bar{t}} btag_hfstats2_up",      2, -2.5, 2.5);
  DeltaY_btag_hfstats2_down = book<TH1F>("DeltaY_btag_hfstats2_down", "#DeltaY_{t#bar{t}} btag_hfstats2_down",  2, -2.5, 2.5);
  DeltaY_btag_lf_up         = book<TH1F>("DeltaY_btag_lf_up", "#DeltaY_{t#bar{t}} btag_lf_up",                  2, -2.5, 2.5);
  DeltaY_btag_lf_down       = book<TH1F>("DeltaY_btag_lf_down", "#DeltaY_{t#bar{t}} btag_lf_down",              2, -2.5, 2.5);
  DeltaY_btag_lfstats1_up   = book<TH1F>("DeltaY_btag_lfstats1_up", "#DeltaY_{t#bar{t}} btag_lfstats1_up",      2, -2.5, 2.5);
  DeltaY_btag_lfstats1_down = book<TH1F>("DeltaY_btag_lfstats1_down", "#DeltaY_{t#bar{t}} btag_lfstats1_down",  2, -2.5, 2.5);
  DeltaY_btag_lfstats2_up   = book<TH1F>("DeltaY_btag_lfstats2_up", "#DeltaY_{t#bar{t}} btag_lfstats2_up",      2, -2.5, 2.5);
  DeltaY_btag_lfstats2_down = book<TH1F>("DeltaY_btag_lfstats2_down", "#DeltaY_{t#bar{t}} btag_lfstats2_down",  2, -2.5, 2.5);
  DeltaY_ttag_corr_up       = book<TH1F>("DeltaY_ttag_corr_up", "#DeltaY_{t#bar{t}} ttag_corr_up",              2, -2.5, 2.5);
  DeltaY_ttag_corr_down     = book<TH1F>("DeltaY_ttag_corr_down", "#DeltaY_{t#bar{t}} ttag_corr_down",          2, -2.5, 2.5);
  DeltaY_ttag_uncorr_up     = book<TH1F>("DeltaY_ttag_uncorr_up", "#DeltaY_{t#bar{t}} ttag_uncorr_up",          2, -2.5, 2.5);
  DeltaY_ttag_uncorr_down   = book<TH1F>("DeltaY_ttag_uncorr_down", "#DeltaY_{t#bar{t}} ttag_counrr_down",      2, -2.5, 2.5);
  DeltaY_tmistag_up         = book<TH1F>("DeltaY_tmistag_up", "#DeltaY_{t#bar{t}} [GeV] tmistag_up",            2, -2.5, 2.5);
  DeltaY_tmistag_down       = book<TH1F>("DeltaY_tmistag_down", "#DeltaY_{t#bar{t}} [GeV] tmistag_down",        2, -2.5, 2.5);
  // DeltaY_toppt_up           = book<TH1F>("DeltaY_toppt_up", "#DeltaY_{t#bar{t}} [GeV] toppt_up",                2, -2.5, 2.5);
  // DeltaY_toppt_down         = book<TH1F>("DeltaY_toppt_down", "#DeltaY_{t#bar{t}} [GeV] toppt_down",            2, -2, 2); 



  // Zprime reconstruction
  DeltaY_tt                    = book<TH2F>("DeltaY_tt", "#DeltaY_{t#bar{t}} ",                                       2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_mu_reco_up_tt         = book<TH2F>("DeltaY_mu_reco_up_tt",   "#DeltaY_{t#bar{t}} mu_reco_up",                2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_mu_reco_down_tt       = book<TH2F>("DeltaY_mu_reco_down_tt", "#DeltaY_{t#bar{t}} mu_reco_down",              2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_pu_up_tt              = book<TH2F>("DeltaY_pu_up_tt",   "#DeltaY_{t#bar{t}} pu_up",                          2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_pu_down_tt            = book<TH2F>("DeltaY_pu_down_tt", "#DeltaY_{t#bar{t}} pu_down",                        2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_prefiring_up_tt       = book<TH2F>("DeltaY_prefiring_up_tt",   "#DeltaY_{t#bar{t}} prefiring_up",            2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_prefiring_down_tt     = book<TH2F>("DeltaY_prefiring_down_tt", "#DeltaY_{t#bar{t}} prefiring_down",          2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_mu_id_up_tt           = book<TH2F>("DeltaY_mu_id_up_tt",   "#DeltaY_{t#bar{t}} mu_id_up",                    2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_mu_id_down_tt         = book<TH2F>("DeltaY_mu_id_down_tt", "#DeltaY_{t#bar{t}} mu_id_down",                  2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_mu_iso_up_tt          = book<TH2F>("DeltaY_mu_iso_up_tt",   "#DeltaY_{t#bar{t} mu_iso_up",                   2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_mu_iso_down_tt        = book<TH2F>("DeltaY_mu_iso_down_tt", "#DeltaY_{t#bar{t}} mu_iso_down",                2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_mu_trigger_up_tt      = book<TH2F>("DeltaY_mu_trigger_up_tt",   "#DeltaY_{t#bar{t}} mu_trigger_up",          2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_mu_trigger_down_tt    = book<TH2F>("DeltaY_mu_trigger_down_tt", "#DeltaY_{t#bar{t}} mu_trigger_down",        2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ele_id_up_tt          = book<TH2F>("DeltaY_ele_id_up_tt",   "#DeltaY_{t#bar{t}} ele_id_up",                  2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ele_id_down_tt        = book<TH2F>("DeltaY_ele_id_down_tt", "#DeltaY_{t#bar{t}} ele_id_down",                2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ele_trigger_up_tt     = book<TH2F>("DeltaY_ele_trigger_up_tt",   "#DeltaY_{t#bar{t}} ele_trigger_up",        2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ele_trigger_down_tt   = book<TH2F>("DeltaY_ele_trigger_down_tt", "#DeltaY_{t#bar{t}} ele_trigger_down",      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ele_reco_up_tt        = book<TH2F>("DeltaY_ele_reco_up_tt",   "#DeltaY_{t#bar{t}} ele_reco_up",              2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ele_reco_down_tt      = book<TH2F>("DeltaY_ele_reco_down_tt", "#DeltaY_{t#bar{t}} ele_reco_down",            2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_murmuf_upup_tt        = book<TH2F>("DeltaY_murmuf_upup_tt", "#DeltaY_{t#bar{t}} murmuf_upup",                2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_murmuf_upnone_tt      = book<TH2F>("DeltaY_murmuf_upnone_tt", "#DeltaY_{t#bar{t}} murmuf_upnone",            2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_murmuf_noneup_tt      = book<TH2F>("DeltaY_murmuf_noneup_tt", "#DeltaY_{t#bar{t}} murmuf_noneup",            2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_murmuf_nonedown_tt    = book<TH2F>("DeltaY_murmuf_nonedown_tt", "#DeltaY_{t#bar{t}} murmuf_nonedown",        2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_murmuf_downnone_tt    = book<TH2F>("DeltaY_murmuf_downnone_tt", "#DeltaY_{t#bar{t}} murmuf_downnone",        2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_murmuf_downdown_tt    = book<TH2F>("DeltaY_murmuf_downdown_tt", "#DeltaY_{t#bar{t}} murmuf_downdown",        2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_isr_up_tt             = book<TH2F>("DeltaY_isr_up_tt", "#DeltaY_{t#bar{t}} isr_up",                          2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_isr_down_tt           = book<TH2F>("DeltaY_isr_down_tt", "#DeltaY_{t#bar{t}} isr_down",                      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_fsr_up_tt             = book<TH2F>("DeltaY_fsr_up_tt", "#DeltaY_{t#bar{t}} fsr_up",                          2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_fsr_down_tt           = book<TH2F>("DeltaY_fsr_down_tt", "#DeltaY_{t#bar{t}} fsr_down",                      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_cferr1_up_tt     = book<TH2F>("DeltaY_btag_cferr1_up_tt", "#DeltaY_{t#bar{t}} btag_cferr1_up",          2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_cferr1_down_tt   = book<TH2F>("DeltaY_btag_cferr1_down_tt", "#DeltaY_{t#bar{t}} btag_cferr1_down",      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_cferr2_up_tt     = book<TH2F>("DeltaY_btag_cferr2_up_tt", "#DeltaY_{t#bar{t}} btag_cferr2_up",          2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_cferr2_down_tt   = book<TH2F>("DeltaY_btag_cferr2_down_tt", "#DeltaY_{t#bar{t}} btag_cferr2_down",      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_hf_up_tt         = book<TH2F>("DeltaY_btag_hf_up_tt", "#DeltaY_{t#bar{t}} btag_hf_up",                  2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_hf_down_tt       = book<TH2F>("DeltaY_btag_hf_down_tt", "#DeltaY_{t#bar{t}} btag_hf_down",              2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_hfstats1_up_tt   = book<TH2F>("DeltaY_btag_hfstats1_up_tt", "#DeltaY_{t#bar{t}} btag_hfstats1_up",      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_hfstats1_down_tt = book<TH2F>("DeltaY_btag_hfstats1_down_tt", "#DeltaY_{t#bar{t}} btag_hfstats1_down",  2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_hfstats2_up_tt   = book<TH2F>("DeltaY_btag_hfstats2_up_tt", "#DeltaY_{t#bar{t}} btag_hfstats2_up",      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_hfstats2_down_tt = book<TH2F>("DeltaY_btag_hfstats2_down_tt", "#DeltaY_{t#bar{t}} btag_hfstats2_down",  2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_lf_up_tt         = book<TH2F>("DeltaY_btag_lf_up_tt", "#DeltaY_{t#bar{t}} btag_lf_up",                  2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_lf_down_tt       = book<TH2F>("DeltaY_btag_lf_down_tt", "#DeltaY_{t#bar{t}} btag_lf_down",              2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_lfstats1_up_tt   = book<TH2F>("DeltaY_btag_lfstats1_up_tt", "#DeltaY_{t#bar{t}} btag_lfstats1_up",      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_lfstats1_down_tt = book<TH2F>("DeltaY_btag_lfstats1_down_tt", "#DeltaY_{t#bar{t}} btag_lfstats1_down",  2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_lfstats2_up_tt   = book<TH2F>("DeltaY_btag_lfstats2_up_tt", "#DeltaY_{t#bar{t}} btag_lfstats2_up",      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_btag_lfstats2_down_tt = book<TH2F>("DeltaY_btag_lfstats2_down_tt", "#DeltaY_{t#bar{t}} btag_lfstats2_down",  2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ttag_corr_up_tt       = book<TH2F>("DeltaY_ttag_corr_up_tt", "#DeltaY_{t#bar{t}} ttag_corr_up",              2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ttag_corr_down_tt     = book<TH2F>("DeltaY_ttag_corr_down_tt", "#DeltaY_{t#bar{t}} ttag_corr_down",          2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ttag_uncorr_up_tt     = book<TH2F>("DeltaY_ttag_uncorr_up_tt", "#DeltaY_{t#bar{t}} ttag_uncorr_up",          2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_ttag_uncorr_down_tt   = book<TH2F>("DeltaY_ttag_uncorr_down_tt", "#DeltaY_{t#bar{t}} ttag_counrr_down",      2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_tmistag_up_tt         = book<TH2F>("DeltaY_tmistag_up_tt", "#DeltaY_{t#bar{t}} [GeV] tmistag_up",            2, -2.5, 2.5, 2, -2.5, 2.5);
  DeltaY_tmistag_down_tt       = book<TH2F>("DeltaY_tmistag_down_tt", "#DeltaY_{t#bar{t}} [GeV] tmistag_down",        2, -2.5, 2.5, 2, -2.5, 2.5);
  // DeltaY_toppt_up           = book<TH1F>("DeltaY_toppt_up", "#DeltaY_{t#bar{t}} [GeV] toppt_up",                2, -2.5, 2.5, 2, -2.5, 2.5);
  // DeltaY_toppt_down         = book<TH1F>("DeltaY_toppt_down", "#DeltaY_{t#bar{t}} [GeV] toppt_down",            2, -2.5, 2.5, 2, -2.5, 2.5); 

}


void ZprimeSemiLeptonicSystematicsHists::fill(const Event & event){

  double weight = event.weight;
  float ele_reco_nominal   = event.get(h_ele_reco);
  float ele_reco_up        = event.get(h_ele_reco_up);
  float ele_reco_down      = event.get(h_ele_reco_down);
  float ele_id_nominal     = event.get(h_ele_id);
  float ele_id_up          = event.get(h_ele_id_up);
  float ele_id_down        = event.get(h_ele_id_down);
  float ele_trigger_nominal= event.get(h_ele_trigger);
  float ele_trigger_up     = event.get(h_ele_trigger_up);
  float ele_trigger_down   = event.get(h_ele_trigger_down);
  float mu_reco_nominal    = event.get(h_mu_reco);
  float mu_reco_up         = event.get(h_mu_reco_up);
  float mu_reco_down       = event.get(h_mu_reco_down);
  float mu_iso_nominal     = event.get(h_mu_iso);
  float mu_iso_up          = event.get(h_mu_iso_up);
  float mu_iso_down        = event.get(h_mu_iso_down);
  float mu_id_nominal      = event.get(h_mu_id);
  float mu_id_up           = event.get(h_mu_id_up);
  float mu_id_down         = event.get(h_mu_id_down);
  float mu_trigger_nominal = event.get(h_mu_trigger);
  float mu_trigger_up      = event.get(h_mu_trigger_up);
  float mu_trigger_down    = event.get(h_mu_trigger_down);
  float pu_nominal         = event.get(h_pu);
  float pu_up              = event.get(h_pu_up);
  float pu_down            = event.get(h_pu_down);
  float prefiring_nominal  = event.get(h_prefiring);
  float prefiring_up       = event.get(h_prefiring_up);
  float prefiring_down     = event.get(h_prefiring_down);
  float murmuf_upup        = event.get(h_murmuf_upup);
  float murmuf_upnone      = event.get(h_murmuf_upnone);
  float murmuf_noneup      = event.get(h_murmuf_noneup);
  float murmuf_nonedown    = event.get(h_murmuf_nonedown);
  float murmuf_downnone    = event.get(h_murmuf_downnone);
  float murmuf_downdown    = event.get(h_murmuf_downdown);
  float isr_up             = event.get(h_isr_up);
  float isr_down           = event.get(h_isr_down);
  float fsr_up             = event.get(h_fsr_up);
  float fsr_down           = event.get(h_fsr_down);
  float btag_nominal       = event.get(h_btag);
  float btag_cferr1_up     = event.get(h_btag_cferr1_up);
  float btag_cferr1_down   = event.get(h_btag_cferr1_down);
  float btag_cferr2_up     = event.get(h_btag_cferr2_up);
  float btag_cferr2_down   = event.get(h_btag_cferr2_down);
  float btag_hf_up         = event.get(h_btag_hf_up);
  float btag_hf_down       = event.get(h_btag_hf_down);
  float btag_hfstats1_up   = event.get(h_btag_hfstats1_up);
  float btag_hfstats1_down = event.get(h_btag_hfstats1_down);
  float btag_hfstats2_up   = event.get(h_btag_hfstats2_up);
  float btag_hfstats2_down = event.get(h_btag_hfstats2_down);
  float btag_lf_up         = event.get(h_btag_lf_up);
  float btag_lf_down       = event.get(h_btag_lf_down);
  float btag_lfstats1_up   = event.get(h_btag_lfstats1_up);
  float btag_lfstats1_down = event.get(h_btag_lfstats1_down);
  float btag_lfstats2_up   = event.get(h_btag_lfstats2_up);
  float btag_lfstats2_down = event.get(h_btag_lfstats2_down);
  float ttag_nominal       = event.get(h_ttag);
  float ttag_corr_up       = event.get(h_ttag_corr_up);
  float ttag_corr_down     = event.get(h_ttag_corr_down);
  float ttag_uncorr_up     = event.get(h_ttag_uncorr_up);
  float ttag_uncorr_down   = event.get(h_ttag_uncorr_down);
  float tmistag_nominal    = event.get(h_tmistag);
  float tmistag_up         = event.get(h_tmistag_up);
  float tmistag_down       = event.get(h_tmistag_down);

  // only up/down variations
  vector<string> names       = {"ele_reco", "ele_id", "ele_trigger", "mu_reco", "mu_iso", "mu_id", "mu_trigger", "pu", "prefiring"};
  vector<float> syst_nominal = {ele_reco_nominal, ele_id_nominal, ele_trigger_nominal, mu_reco_nominal, mu_iso_nominal, mu_id_nominal, mu_trigger_nominal, pu_nominal, prefiring_nominal};
  vector<float> syst_up      = {ele_reco_up, ele_id_up, ele_trigger_up, mu_reco_up, mu_iso_up, mu_id_up, mu_trigger_up, pu_up, prefiring_up};
  vector<float> syst_down    = {ele_reco_down, ele_id_down, ele_trigger_down, mu_reco_down, mu_iso_down, mu_id_down, mu_trigger_down, pu_down, prefiring_down};
  
  vector<TH1F*> hists_up     = {DeltaY_ele_reco_up, DeltaY_ele_id_up, DeltaY_ele_trigger_up, DeltaY_mu_reco_up, DeltaY_mu_iso_up, DeltaY_mu_id_up, DeltaY_mu_trigger_up, DeltaY_pu_up, DeltaY_prefiring_up};
  vector<TH1F*> hists_down   = {DeltaY_ele_reco_down, DeltaY_ele_id_down, DeltaY_ele_trigger_down, DeltaY_mu_reco_down, DeltaY_mu_iso_down, DeltaY_mu_id_down, DeltaY_mu_trigger_down, DeltaY_pu_down, DeltaY_prefiring_down};
  
  vector<TH2F*> hists_up_tt     = {DeltaY_ele_reco_up_tt, DeltaY_ele_id_up_tt, DeltaY_ele_trigger_up_tt, DeltaY_mu_reco_up_tt, DeltaY_mu_iso_up_tt, DeltaY_mu_id_up_tt, DeltaY_mu_trigger_up_tt, DeltaY_pu_up_tt, DeltaY_prefiring_up_tt};
  vector<TH2F*> hists_down_tt   = {DeltaY_ele_reco_down_tt, DeltaY_ele_id_down_tt, DeltaY_ele_trigger_down_tt, DeltaY_mu_reco_down_tt, DeltaY_mu_iso_down_tt, DeltaY_mu_id_down_tt, DeltaY_mu_trigger_down_tt, DeltaY_pu_down_tt, DeltaY_prefiring_down_tt};


  // scale variations need special treatment
  vector<float> syst_scale  = {murmuf_upup, murmuf_upnone, murmuf_noneup, murmuf_nonedown, murmuf_downnone, murmuf_downdown};
  vector<TH1F*> hists_scale = {DeltaY_murmuf_upup, DeltaY_murmuf_upnone, DeltaY_murmuf_noneup, DeltaY_murmuf_nonedown, DeltaY_murmuf_downnone, DeltaY_murmuf_downdown};
  
  vector<TH2F*> hists_scale_tt = {DeltaY_murmuf_upup_tt, DeltaY_murmuf_upnone_tt, DeltaY_murmuf_noneup_tt, DeltaY_murmuf_nonedown_tt, DeltaY_murmuf_downnone_tt, DeltaY_murmuf_downdown_tt};

  // btag variations need special treatment
  vector<float> syst_btag  = {btag_cferr1_up, btag_cferr1_down, btag_cferr2_up, btag_cferr2_down, btag_hf_up, btag_hf_down, btag_hfstats1_up, btag_hfstats1_down, btag_hfstats2_up, btag_hfstats2_down, btag_lf_up, btag_lf_down, btag_lfstats1_up, btag_lfstats1_down, btag_lfstats2_up, btag_lfstats2_down};
  vector<TH1F*> hists_btag  = {DeltaY_btag_cferr1_up, DeltaY_btag_cferr1_down, DeltaY_btag_cferr2_up, DeltaY_btag_cferr2_down, DeltaY_btag_hf_up, DeltaY_btag_hf_down, DeltaY_btag_hfstats1_up, DeltaY_btag_hfstats1_down, DeltaY_btag_hfstats2_up, DeltaY_btag_hfstats2_down, DeltaY_btag_lf_up, DeltaY_btag_lf_down, DeltaY_btag_lfstats1_up, DeltaY_btag_lfstats1_down, DeltaY_btag_lfstats2_up, DeltaY_btag_lfstats2_down};
  
  vector<TH2F*> hists_btag_tt  = {DeltaY_btag_cferr1_up_tt, DeltaY_btag_cferr1_down_tt, DeltaY_btag_cferr2_up_tt, DeltaY_btag_cferr2_down_tt, DeltaY_btag_hf_up_tt, DeltaY_btag_hf_down_tt, DeltaY_btag_hfstats1_up_tt, DeltaY_btag_hfstats1_down_tt, DeltaY_btag_hfstats2_up_tt, DeltaY_btag_hfstats2_down_tt, DeltaY_btag_lf_up_tt, DeltaY_btag_lf_down_tt, DeltaY_btag_lfstats1_up_tt, DeltaY_btag_lfstats1_down_tt, DeltaY_btag_lfstats2_up_tt, DeltaY_btag_lfstats2_down_tt};

  // ttag variations need special treatment
  vector<float> syst_ttag = {ttag_corr_up, ttag_corr_down, ttag_uncorr_up, ttag_uncorr_down};
  vector<TH1F*> hists_ttag = {DeltaY_ttag_corr_up, DeltaY_ttag_corr_down, DeltaY_ttag_uncorr_up, DeltaY_ttag_uncorr_down};
  
  vector<TH2F*> hists_ttag_tt = {DeltaY_ttag_corr_up_tt, DeltaY_ttag_corr_down_tt, DeltaY_ttag_uncorr_up_tt, DeltaY_ttag_uncorr_down_tt};

  // tmistag variations need special treatment
  vector<float> syst_tmistag = {tmistag_up, tmistag_down};
  vector<TH1F*> hists_tmistag = {DeltaY_tmistag_up, DeltaY_tmistag_down};
  
  vector<TH2F*> hists_tmistag_tt = {DeltaY_tmistag_up_tt, DeltaY_tmistag_down_tt};

  // toppt variations need special treatment
  // vector<float> syst_toppt  = {toppt_up, toppt_down};
  // vector<TH1F*> hists_toppt = {DeltaY_toppt_up, DeltaY_toppt_down};
  
  // parton shower variations (ISR, FSR) need special treatment
  vector<float> syst_ps = {isr_up, isr_down, fsr_up, fsr_down};
  vector<TH1F*> hists_ps = {DeltaY_isr_up, DeltaY_isr_down, DeltaY_fsr_up, DeltaY_fsr_down};
  
  vector<TH2F*> hists_ps_tt = {DeltaY_isr_up_tt, DeltaY_isr_down_tt, DeltaY_fsr_up_tt, DeltaY_fsr_down_tt};



  // Zprime reco
  bool is_zprime_reconstructed_chi2 = event.get(h_is_zprime_reconstructed_chi2);
  if(is_zprime_reconstructed_chi2 && is_mc){
    if(is_tt){
      ZprimeCandidate* BestZprimeCandidate = event.get(h_BestZprimeCandidateChi2);
      // float Mreco = BestZprimeCandidate->Zprime_v4().M();
      
      const auto& genparticles = event.genparticles;
      GenParticle top, antitop;
        for(const GenParticle & gp : *genparticles){
            if(gp.pdgId() == 6){
                top = gp;
            }
            else if(gp.pdgId() == -6){
                antitop = gp;
            }
        }
      // The Lorentz vectors represent the 4-momenta (energy, and three spatial momentum components) for the leptonic and hadronic tops from the "BestZprimeCandidate" object
      LorentzVector lep_top = BestZprimeCandidate->top_leptonic_v4();
      LorentzVector had_top = BestZprimeCandidate->top_hadronic_v4();

      // vectors to store the deltaR values for the leptonic and hadronic tops with each gen particle
      // this part initializes vectors to store deltaR values with a default of 99.0 and fills in the actual deltaR values by looping over the gen particles (top)
      std::vector<double> deltaR_leptonic_values(genparticles->size(), 99.0);
      std::vector<double> deltaR_hadronic_values(genparticles->size(), 99.0);

      // deltaR is a measure of separation in the eta-phi space. 
      // The next few sections calculate the deltaR values between the leptonic and hadronic tops and each generator particle
      for(unsigned int j=0; j<genparticles->size(); ++j) {
        if(abs(genparticles->at(j).pdgId()) == 6) {
        LorentzVector genparticle_p4(genparticles->at(j).pt(), genparticles->at(j).eta(), genparticles->at(j).phi(), genparticles->at(j).energy());
        deltaR_leptonic_values[j] = deltaR(lep_top, genparticle_p4);
        deltaR_hadronic_values[j] = deltaR(had_top, genparticle_p4);
        }
      }
      // vectors to store the best gen particle for each top
      // it determines which gen particle is closest in the eta-phi space to the leptonic and hadronic tops
      int best_gen_for_leptop = -1;
      int best_gen_for_hadtop = -1;
      std::vector<int> best_leptop_for_gen(genparticles->size(), -1);
      std::vector<int> best_hadtop_for_gen(genparticles->size(), -1);

      // Find closest gen particle for each top
      // These loops determine whether each gen particle is closer to the leptonic or hadronic top and assigns an index accordingly
      double deltaR_min_leptonic = 99.0;
      bool is_leptop_matched = false;
      for(unsigned int j=0; j<genparticles->size(); ++j) {
        if(abs(genparticles->at(j).pdgId()) == 6) {
          if (deltaR_leptonic_values[j] < deltaR_min_leptonic && deltaR_leptonic_values[j]<0.4) {
              deltaR_min_leptonic = deltaR_leptonic_values[j];
              best_gen_for_leptop = j;
              is_leptop_matched = true;
          }
        }   
      }
      double deltaR_min_hadronic = 99.0;
      bool is_hadtop_matched = false;
      for(unsigned int j=0; j<genparticles->size(); ++j) {
        if(abs(genparticles->at(j).pdgId()) == 6) {
          if (deltaR_hadronic_values[j] < deltaR_min_hadronic && deltaR_hadronic_values[j]<0.4) {
              deltaR_min_hadronic = deltaR_hadronic_values[j];
              best_gen_for_hadtop = j;
              is_hadtop_matched = true;
          }
        }
      }
      for(unsigned int j=0; j<genparticles->size(); ++j) {
        if(abs(genparticles->at(j).pdgId()) == 6) {
          if(deltaR_leptonic_values[j] < deltaR_hadronic_values[j]) {
              best_leptop_for_gen[j] = 0;  // 0 is the index for the single leptonic top
          } else {
              best_hadtop_for_gen[j] = 0;  // 0 is the index for the single hadronic top
          }
        }
      }

      // deltaY values calculation starts:

      // matched gen particles
      GenParticle best_matched_gen_leptop;
      GenParticle best_matched_gen_hadtop;

      bool valid_leptop = true, valid_hadtop = true;

      if (best_gen_for_leptop >= 0 && static_cast<std::size_t>(best_gen_for_leptop) < genparticles->size()) {
          best_matched_gen_leptop = genparticles->at(best_gen_for_leptop);
      } else {
          // std::cerr << "Error: Invalid index for leptonic top gen particle: " << best_gen_for_leptop << std::endl;
          valid_leptop = false;
      }

      if (best_gen_for_hadtop >= 0 && static_cast<std::size_t>(best_gen_for_hadtop) < genparticles->size()) {
          best_matched_gen_hadtop = genparticles->at(best_gen_for_hadtop);
      } else {
          // std::cerr << "Error: Invalid index for hadronic top gen particle: " << best_gen_for_hadtop << std::endl;
          valid_hadtop = false; 
      }

      
      float_t DeltaY_gen_best = 0.0;
      float_t DeltaY_reco_best = 0.0;
      bool isLeptonPositive = false;
      
      // The following if-else block determines whether the lepton is positive or negative

      if(isMuon){
        if (event.muons->at(0).charge() == 1){
          isLeptonPositive = true;
        } else {
          isLeptonPositive = false;
        }
      }

      if(isElectron){
        if (event.electrons->at(0).charge() == 1){
          isLeptonPositive = true;
        } else {
          isLeptonPositive = false;
        }
      }

      // Calculates the delta y (with reco particles) values for the leptonic and hadronic tops depending on the charge of the lepton
      if (isLeptonPositive) {
        DeltaY_reco_best = TMath::Abs(0.5*TMath::Log((lep_top.energy() + lep_top.pt()*TMath::SinH(lep_top.eta()))/(lep_top.energy() - lep_top.pt()*TMath::SinH(lep_top.eta())))) - TMath::Abs(0.5*TMath::Log((had_top.energy() + had_top.pt()*TMath::SinH(had_top.eta()))/(had_top.energy() - had_top.pt()*TMath::SinH(had_top.eta()))));
      } else {
        DeltaY_reco_best = TMath::Abs(0.5*TMath::Log((had_top.energy() + had_top.pt()*TMath::SinH(had_top.eta()))/(had_top.energy() - had_top.pt()*TMath::SinH(had_top.eta())))) - TMath::Abs(0.5*TMath::Log((lep_top.energy() + lep_top.pt()*TMath::SinH(lep_top.eta()))/(lep_top.energy() - lep_top.pt()*TMath::SinH(lep_top.eta()))));
      }

      // Calculates the delta y with matched gen particles
      if(valid_leptop && valid_hadtop) {
        DeltaY_gen_best = TMath::Abs(0.5*TMath::Log((best_matched_gen_leptop.energy() + best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta()))/(best_matched_gen_leptop.energy() - best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta())))) - TMath::Abs(0.5*TMath::Log((best_matched_gen_hadtop.energy() + best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))/(best_matched_gen_hadtop.energy() - best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))));
      }


      // up/down variations
      for(unsigned int i=0; i<names.size(); i++){
        hists_up_tt.at(i)->Fill(DeltaY_reco_best, DeltaY_gen_best, weight * syst_up.at(i)/syst_nominal.at(i));
        hists_down_tt.at(i)->Fill(DeltaY_reco_best, DeltaY_gen_best, weight * syst_down.at(i)/syst_nominal.at(i));
      }
      // scale variations
      for(unsigned int i=0; i<hists_scale.size(); i++){
        hists_scale_tt.at(i)->Fill(DeltaY_reco_best, DeltaY_gen_best, weight * syst_scale.at(i));
      }
      // btag variations
      for(unsigned int i=0; i<hists_btag.size(); i++){
        hists_btag_tt.at(i)->Fill(DeltaY_reco_best, DeltaY_gen_best, weight * syst_btag.at(i)/btag_nominal);
      }
      // ttag variations!
      for(unsigned int i=0; i<hists_ttag.size(); i++){
        hists_ttag_tt.at(i)->Fill(DeltaY_reco_best, DeltaY_gen_best, weight * syst_ttag.at(i)/ttag_nominal);
      }
      // tmistag variations
      for(unsigned int i=0; i<hists_tmistag.size(); i++){
        hists_tmistag_tt.at(i)->Fill(DeltaY_reco_best, DeltaY_gen_best, weight * syst_tmistag.at(i)/tmistag_nominal);
      }
      // ps variations
      for(unsigned int i=0; i<hists_ps.size(); i++){
      hists_ps_tt.at(i)->Fill(DeltaY_reco_best, DeltaY_gen_best, weight * syst_ps.at(i));
      }
    }
   
    
    else{
      ZprimeCandidate* BestZprimeCandidate = event.get(h_BestZprimeCandidateChi2);
      // float Mreco = BestZprimeCandidate->Zprime_v4().M();
      float deltay=(TMath::Abs(BestZprimeCandidate->top_leptonic_v4().Rapidity()) - TMath::Abs(BestZprimeCandidate->top_hadronic_v4().Rapidity()));
      DeltaY->Fill(deltay, weight);

      // up/down variations
      for(unsigned int i=0; i<names.size(); i++){
        hists_up.at(i)->Fill(deltay, weight * syst_up.at(i)/syst_nominal.at(i));
        hists_down.at(i)->Fill(deltay, weight * syst_down.at(i)/syst_nominal.at(i));
      }
      // scale variations
      for(unsigned int i=0; i<hists_scale.size(); i++){
        hists_scale.at(i)->Fill(deltay, weight * syst_scale.at(i));
      }
      // btag variations
      for(unsigned int i=0; i<hists_btag.size(); i++){
        hists_btag.at(i)->Fill(deltay, weight * syst_btag.at(i)/btag_nominal);
      }
      // ttag variations!
      for(unsigned int i=0; i<hists_ttag.size(); i++){
        hists_ttag.at(i)->Fill(deltay, weight * syst_ttag.at(i)/ttag_nominal);
      }
      // tmistag variations
      for(unsigned int i=0; i<hists_tmistag.size(); i++){
        hists_tmistag.at(i)->Fill(deltay, weight * syst_tmistag.at(i)/tmistag_nominal);
      }
      // toppt variations
      // for(unsigned int i=0; i<hists_toppt.size(); i++){
      //   hists_toppt.at(i)->Fill(deltay, weight * syst_toppt.at(i)/toppt_nominal);
      // }
      // ps variations
      for(unsigned int i=0; i<hists_ps.size(); i++){
      hists_ps.at(i)->Fill(deltay, weight * syst_ps.at(i));
      }
    }
  }

} //Method

ZprimeSemiLeptonicSystematicsHists::~ZprimeSemiLeptonicSystematicsHists(){}