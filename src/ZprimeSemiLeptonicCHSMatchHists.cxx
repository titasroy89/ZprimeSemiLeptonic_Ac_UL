#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicCHSMatchHists.h"
#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicModules.h"
#include "UHH2/core/include/Event.h"
#include <UHH2/core/include/Utils.h>
#include <UHH2/common/include/Utils.h>
#include "UHH2/common/include/JetIds.h"
#include <math.h>

#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/TTbarReconstruction.h>
#include <UHH2/common/include/ReconstructionHypothesisDiscriminators.h>

#include "TH1F.h"
#include "TH2D.h"
#include <iostream>

using namespace std;
using namespace uhh2;

ZprimeSemiLeptonicCHSMatchHists::ZprimeSemiLeptonicCHSMatchHists(uhh2::Context& ctx, const std::string& dirname):
Hists(ctx, dirname) {

  is_mc = ctx.get("dataset_type") == "MC";
  h_CHSjets_matched = ctx.get_handle<std::vector<Jet>>("CHS_matched");
  init();
}

void ZprimeSemiLeptonicCHSMatchHists::init(){

  // jets
  N_jets            = book<TH1F>("N_jets", "N_{jets}", 21, -0.5, 20.5);
  pt_jet            = book<TH1F>("pt_jet", "p_{T}^{jets} [GeV]", 50, 0, 1500);
  pt_jet1           = book<TH1F>("pt_jet1", "p_{T}^{jet 1} [GeV]",  50, 0, 1500);
  pt_jet2           = book<TH1F>("pt_jet2", "p_{T}^{jet 2} [GeV]", 50, 0, 1500);
  pt_jet3           = book<TH1F>("pt_jet3", "p_{T}^{jet 3} [GeV]", 50, 0, 1500);
  eta_jet           = book<TH1F>("eta_jet", "#eta^{jets}", 50, -2.5, 2.5);
  eta_jet1          = book<TH1F>("eta_jet1", "#eta^{jet 1}", 50, -2.5, 2.5);
  eta_jet2          = book<TH1F>("eta_jet2", "#eta^{jet 2}", 50, -2.5, 2.5);
  eta_jet3          = book<TH1F>("eta_jet3", "#eta^{jet 3}", 50, -2.5, 2.5);
  phi_jet           = book<TH1F>("phi_jet", "#phi^{jets}", 35, -3.5, 3.5);
  phi_jet1          = book<TH1F>("phi_jet1", "#phi^{jet 1}", 35, -3.5, 3.5);
  phi_jet2          = book<TH1F>("phi_jet2", "#phi^{jet 2}", 35, -3.5, 3.5);
  phi_jet3          = book<TH1F>("phi_jet3", "#phi^{jet 3}", 35, -3.5, 3.5);
  m_jet             = book<TH1F>("m_jet", "m^{jets}", 50, 0, 500);
  m_jet1            = book<TH1F>("m_jet1", "m^{jet 1}", 50, 0, 500);
  m_jet2            = book<TH1F>("m_jet2", "m^{jet 2}", 50, 0, 500);
  m_jet3            = book<TH1F>("m_jet3", "m^{jet 3}", 50, 0, 500);
  bscore_jet        = book<TH1F>("bscore_jet",  "bscore^{jets}", 20, 0, 1);
  bscore_jet1       = book<TH1F>("bscore_jet1", "bscore^{jet 1}", 20, 0, 1);
  bscore_jet2       = book<TH1F>("bscore_jet2", "bscore^{jet 2}", 20, 0, 1);
  bscore_jet3       = book<TH1F>("bscore_jet3", "bscore^{jet 3}", 20, 0, 1);
  N_bJets_loose     = book<TH1F>("N_bJets_loose", "N_{jets}^{bscore loose}", 11, -0.5, 10.5);
  N_bJets_med       = book<TH1F>("N_bJets_med",   "N_{jets}^{bscore medium}", 11, -0.5, 10.5);
  N_bJets_tight     = book<TH1F>("N_bJets_tight", "N_{jets}^{bscore tight}", 11, -0.5, 10.5);

  // CHS matched jets
  CHS_matched_N_jets            = book<TH1F>("CHS_matched_N_jets", "CHS matched N_{jets}", 21, -0.5, 20.5);
  CHS_matched_pt_jet            = book<TH1F>("CHS_matched_pt_jet", "CHS matched p_{T}^{jets} [GeV]",  50, 0, 1500);
  CHS_matched_pt_jet1           = book<TH1F>("CHS_matched_pt_jet1", "CHS matched p_{T}^{jet 1} [GeV]",  50, 0, 1500);
  CHS_matched_pt_jet2           = book<TH1F>("CHS_matched_pt_jet2", "CHS matched p_{T}^{jet 2} [GeV]", 50, 0, 1500);
  CHS_matched_pt_jet3           = book<TH1F>("CHS_matched_pt_jet3", "CHS matched p_{T}^{jet 3} [GeV]", 50, 0, 1500);
  CHS_matched_eta_jet           = book<TH1F>("CHS_matched_eta_jet", "CHS matched #eta^{jets}", 50, -2.5, 2.5);
  CHS_matched_eta_jet1          = book<TH1F>("CHS_matched_eta_jet1", "CHS matched #eta^{jet 1}", 50, -2.5, 2.5);
  CHS_matched_eta_jet2          = book<TH1F>("CHS_matched_eta_jet2", "CHS matched #eta^{jet 2}", 50, -2.5, 2.5);
  CHS_matched_eta_jet3          = book<TH1F>("CHS_matched_eta_jet3", "CHS matched #eta^{jet 3}", 50, -2.5, 2.5);
  CHS_matched_phi_jet           = book<TH1F>("CHS_matched_phi_jet", "CHS matched #phi^{jets}", 35, -3.5, 3.5);
  CHS_matched_phi_jet1          = book<TH1F>("CHS_matched_phi_jet1", "CHS matched #phi^{jet 1}", 35, -3.5, 3.5);
  CHS_matched_phi_jet2          = book<TH1F>("CHS_matched_phi_jet2", "CHS matched #phi^{jet 2}", 35, -3.5, 3.5);
  CHS_matched_phi_jet3          = book<TH1F>("CHS_matched_phi_jet3", "CHS matched #phi^{jet 3}", 35, -3.5, 3.5);
  CHS_matched_m_jet             = book<TH1F>("CHS_matched_m_jet", "CHS matched m^{jets}", 50, 0, 500);
  CHS_matched_m_jet1            = book<TH1F>("CHS_matched_m_jet1", "CHS matched m^{jet 1}", 50, 0, 500);
  CHS_matched_m_jet2            = book<TH1F>("CHS_matched_m_jet2", "CHS matched m^{jet 2}", 50, 0, 500);
  CHS_matched_m_jet3            = book<TH1F>("CHS_matched_m_jet3", "CHS matched m^{jet 3}", 50, 0, 500);
  CHS_matched_bscore_jet        = book<TH1F>("CHS_matched_bscore_jet",  "CHS matched bscore^{jets}", 20, 0, 1);
  CHS_matched_bscore_jet1       = book<TH1F>("CHS_matched_bscore_jet1", "CHS matched bscore^{jet 1}", 20, 0, 1);
  CHS_matched_bscore_jet2       = book<TH1F>("CHS_matched_bscore_jet2", "CHS matched bscore^{jet 2}", 20, 0, 1);
  CHS_matched_bscore_jet3       = book<TH1F>("CHS_matched_bscore_jet3", "CHS matched bscore^{jet 3}", 20, 0, 1);
  CHS_matched_N_bJets_loose     = book<TH1F>("CHS_matched_N_bJets_loose", "CHS matched N_{jets}^{bscore loose}", 11, -0.5, 10.5);
  CHS_matched_N_bJets_med       = book<TH1F>("CHS_matched_N_bJets_med",   "CHS matched N_{jets}^{bscore medium}", 11, -0.5, 10.5);
  CHS_matched_N_bJets_tight     = book<TH1F>("CHS_matched_N_bJets_tight", "CHS matched N_{jets}^{bscore tight}", 11, -0.5, 10.5);
  CHS_matched_N_Jets_LepVeto    = book<TH1F>("CHS_matched_N_Jets_LepVeto", "CHS matched N_{jets}^{Tight Lep Veto}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_Tight      = book<TH1F>("CHS_matched_N_Jets_Tight", "CHS matched N_{jets}^{Tight}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_NotTight   = book<TH1F>("CHS_matched_N_Jets_NotTight", "CHS matched N_{jets}^{Not Tight}", 21, -0.5, 20.5);

  CHS_matched_N_Jets_LepVeto_all    = book<TH1F>("CHS_matched_N_Jets_LepVeto_all", "CHS matched N_{jets}^{Tight Lep Veto}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_Tight_all      = book<TH1F>("CHS_matched_N_Jets_Tight_all", "CHS matched N_{jets}^{Tight}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_NotTight_all   = book<TH1F>("CHS_matched_N_Jets_NotTight_all", "CHS matched N_{jets}^{Not Tight}", 21, -0.5, 20.5);

  CHS_matched_N_Jets_LepVeto_1  = book<TH1F>("CHS_matched_N_Jets_LepVeto_1", "CHS matched N_{jets}^{Tight Lep Veto}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_Tight_1    = book<TH1F>("CHS_matched_N_Jets_Tight_1", "CHS matched N_{jets}^{Tight}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_NotTight_1 = book<TH1F>("CHS_matched_N_Jets_NotTight_1", "CHS matched N_{jets}^{Not Tight}", 21, -0.5, 20.5);

  CHS_matched_N_Jets_LepVeto_2  = book<TH1F>("CHS_matched_N_Jets_LepVeto_2", "CHS matched N_{jets}^{Tight Lep Veto}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_Tight_2    = book<TH1F>("CHS_matched_N_Jets_Tight_2", "CHS matched N_{jets}^{Tight}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_NotTight_2 = book<TH1F>("CHS_matched_N_Jets_NotTight_2", "CHS matched N_{jets}^{Not Tight}", 21, -0.5, 20.5);

  CHS_matched_N_Jets_LepVeto_3  = book<TH1F>("CHS_matched_N_Jets_LepVeto_3", "CHS matched N_{jets}^{Tight Lep Veto}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_Tight_3    = book<TH1F>("CHS_matched_N_Jets_Tight_3", "CHS matched N_{jets}^{Tight}", 21, -0.5, 20.5);
  CHS_matched_N_Jets_NotTight_3 = book<TH1F>("CHS_matched_N_Jets_NotTight_3", "CHS matched N_{jets}^{Not Tight}", 21, -0.5, 20.5);

  //deltaR
  CHS_matched_deltaRmin_CHS_Puppi  = book<TH1F>("CHS_matched_deltaRmin_CHS_Puppi", "#DeltaR_{min}(CHS jet, Puppi jet)", 120, 0., 3.0);
  diff_pt                       = book<TH1F>("diff_pt", "#Delta p_{T}(CHS jet, Puppi jet) GeV", 40, -200, 200.);
  diff_eta                      = book<TH1F>("diff_eta", "#Delta #eta(CHS jet, Puppi jet) GeV", 50, -2.5, 2.5);
  ratio_chs_pt                  = book<TH1F>("ratio_chs_pt", "(CHS p_{T}-Puppi p_{T})/CHS p_{T}", 800, -100, 100.);
  ratio_puppi_pt                = book<TH1F>("ratio_puppi_pt", "(CHS p_{T}-Puppi p_{T})/Puppi p_{T}", 800, -100, 100.);
  ratio_chs_eta                 = book<TH1F>("ratio_chs_eta", "(CHS #eta-Puppi #eta)/CHS #eta", 100, -2.5, 2.5);
  ratio_puppi_eta               = book<TH1F>("ratio_puppi_eta", "(CHS #eta-Puppi #eta)/Puppi #eta", 100, -2.5, 2.5);
  ratio_chs_puppi_pt            = book<TH1F>("ratio_chs_puppi_pt", "CHS p_{T}/Puppi p_{T}", 800, -100, 100.);
  ratio_chs_puppi_eta           = book<TH1F>("ratio_puppi_eta", "CHS #eta/Puppi #eta", 100, -2.5, 2.5);

  
  diff_pt_bin1                  = book<TH1F>("diff_pt_bin1", "#Delta p_{T}(CHS jet, Puppi jet) GeV",  40, -200, 200.);
  diff_eta_bin1                 = book<TH1F>("diff_eta_bin1", "#Delta #eta(CHS jet, Puppi jet) GeV", 50, -2.5, 2.5);
  ratio_chs_pt_bin1             = book<TH1F>("ratio_chs_pt_bin1", "(CHS p_{T}-Puppi p_{T})/CHS p_{T}", 400, -100, 100.);
  ratio_puppi_pt_bin1           = book<TH1F>("ratio_puppi_pt_bin1", "(CHS p_{T}-Puppi p_{T})/Puppi p_{T}", 400, -100, 100.);
  ratio_chs_eta_bin1            = book<TH1F>("ratio_chs_eta_bin1", "#CHS #eta-Puppi #eta)/CHS #eta", 100, -2.5, 2.5);
  ratio_puppi_eta_bin1          = book<TH1F>("ratio_puppi_eta_bin1", "(CHS #eta-Puppi #eta)/Puppi #eta", 100, -2.5, 2.5);
  ratio_chs_puppi_pt_bin1       = book<TH1F>("ratio_chs_puppi_pt_bin1", "CHS p_{T}/Puppi p_{T}", 800, -100, 100.);
  ratio_chs_puppi_eta_bin1      = book<TH1F>("ratio_chs_puppi_eta_bin1", "CHS #eta/Puppi #eta", 100, -2.5, 2.5);
 
  diff_pt_bin2                  = book<TH1F>("diff_pt_bin2", "#Delta p_{T}(CHS jet, Puppi jet) GeV",  40, -200, 200.);
  diff_eta_bin2                 = book<TH1F>("diff_eta_bin2", "#Delta #eta(CHS jet, Puppi jet) GeV", 50, -2.5, 2.5);
  ratio_chs_pt_bin2             = book<TH1F>("ratio_chs_pt_bin2", "(CHS p_{T}-Puppi p_{T})/CHS p_{T}", 400, -100, 100.);
  ratio_puppi_pt_bin2           = book<TH1F>("ratio_puppi_pt_bin2", "(CHS p_{T}-Puppi p_{T})/Puppi p_{T}", 400, -100, 100.);
  ratio_chs_eta_bin2            = book<TH1F>("ratio_chs_eta_bin2", "#CHS #eta-Puppi #eta)/CHS #eta", 100, -2.5, 2.5);
  ratio_puppi_eta_bin2          = book<TH1F>("ratio_puppi_eta_bin2", "(CHS #eta-Puppi #eta)/Puppi #eta", 100, -2.5, 2.5);
  ratio_chs_puppi_pt_bin2       = book<TH1F>("ratio_chs_puppi_pt_bin2", "CHS p_{T}/Puppi p_{T}", 800, -100, 100.);
  ratio_chs_puppi_eta_bin2      = book<TH1F>("ratio_chs_puppi_eta_bin2", "CHS #eta/Puppi #eta", 100, -2.5, 2.5);
  
  diff_pt_bin3                  = book<TH1F>("diff_pt_bin3", "#Delta p_{T}(CHS jet, Puppi jet) GeV",  40, -200, 200.);
  diff_eta_bin3                 = book<TH1F>("diff_eta_bin3", "#Delta #eta(CHS jet, Puppi jet) GeV", 50, -2.5, 2.5);
  ratio_chs_pt_bin3             = book<TH1F>("ratio_chs_pt_bin3", "(CHS p_{T}-Puppi p_{T})/CHS p_{T}", 400, -100, 100.);
  ratio_puppi_pt_bin3           = book<TH1F>("ratio_puppi_pt_bin3", "(CHS p_{T}-Puppi p_{T})/Puppi p_{T}", 400, -100, 100.);
  ratio_chs_eta_bin3            = book<TH1F>("ratio_chs_eta_bin3", "#CHS #eta-Puppi #eta)/CHS #eta", 100, -2.5, 2.5);
  ratio_puppi_eta_bin3          = book<TH1F>("ratio_puppi_eta_bin3", "(CHS #eta-Puppi #eta)/Puppi #eta", 100, -2.5, 2.5);
  ratio_chs_puppi_pt_bin3       = book<TH1F>("ratio_chs_puppi_pt_bin3", "CHS p_{T}/Puppi p_{T}", 800, -100, 100.);
  ratio_chs_puppi_eta_bin3      = book<TH1F>("ratio_chs_puppi_eta_bin3", "CHS #eta/Puppi #eta", 100, -2.5, 2.5);


  eta_vs_pt     = book<TH2F>("eta_vs_pt", "#Delta(p_{T}) vs. #Delta(#eta); #Delta(#eta); #Delta(p_{T})", 50, -2.5, 2.5, 40, -200, 200.);


}


void ZprimeSemiLeptonicCHSMatchHists::fill(const Event & event){

  double weight = event.weight;

  /*
  █      ██ ███████ ████████ ███████
  █      ██ ██         ██    ██
  █      ██ █████      ██    ███████
  █ ██   ██ ██         ██         ██
  █  █████  ███████    ██    ███████
  */

  vector<Jet>* jets = event.jets;
  int Njets = jets->size();
  N_jets->Fill(Njets, weight);

  for(unsigned int i=0; i<jets->size(); i++){
    pt_jet->Fill(jets->at(i).pt(),weight);
    eta_jet->Fill(jets->at(i).eta(),weight);
    phi_jet->Fill(jets->at(i).phi(),weight);
    m_jet->Fill(jets->at(i).v4().M(),weight);
    // bscore_jet->Fill(jets->at(i).btag_DeepJet(), weight);
    if(i==0){
      pt_jet1->Fill(jets->at(i).pt(),weight);
      eta_jet1->Fill(jets->at(i).eta(),weight);
      phi_jet1->Fill(jets->at(i).phi(),weight);
      m_jet1->Fill(jets->at(i).v4().M(),weight);
      // bscore_jet1->Fill(jets->at(i).btag_DeepJet(), weight);
    }
    else if(i==1){
      pt_jet2->Fill(jets->at(i).pt(),weight);
      eta_jet2->Fill(jets->at(i).eta(),weight);
      phi_jet2->Fill(jets->at(i).phi(),weight);
      m_jet2->Fill(jets->at(i).v4().M(),weight);
      // bscore_jet2->Fill(jets->at(i).btag_DeepJet(), weight);
    }
    else if(i==2){
      pt_jet3->Fill(jets->at(i).pt(),weight);
      eta_jet3->Fill(jets->at(i).eta(),weight);
      phi_jet3->Fill(jets->at(i).phi(),weight);
      m_jet3->Fill(jets->at(i).v4().M(),weight);
      // bscore_jet3->Fill(jets->at(i).btag_DeepJet(), weight);
    }
  }

  int Nbjets_loose = 0, Nbjets_medium = 0, Nbjets_tight = 0;
  DeepJetBTag Btag_loose  = DeepJetBTag(DeepJetBTag::WP_LOOSE);
  DeepJetBTag Btag_medium = DeepJetBTag(DeepJetBTag::WP_MEDIUM);
  DeepJetBTag Btag_tight  = DeepJetBTag(DeepJetBTag::WP_TIGHT);

  for (unsigned int i =0; i<jets->size(); i++) {
    if(Btag_loose(jets->at(i),event))  Nbjets_loose++;
    if(Btag_medium(jets->at(i),event)) Nbjets_medium++;
    if(Btag_tight(jets->at(i),event))  Nbjets_tight++;
  }

  N_bJets_loose->Fill(Nbjets_loose,weight);
  N_bJets_med->Fill(Nbjets_medium,weight);
  N_bJets_tight->Fill(Nbjets_tight,weight);


  /*
  █  ██████ ██   ██ ███████      ██ ███████ ████████ ███████
  █ ██      ██   ██ ██           ██ ██         ██    ██
  █ ██      ███████ ███████      ██ █████      ██    ███████
  █ ██      ██   ██      ██ ██   ██ ██         ██         ██
  █  ██████ ██   ██ ███████  █████  ███████    ██    ███████
  */

  //// Matched to Puppi jets
  const JetPFID jetID_CHS(JetPFID::WP_TIGHT_CHS);
  vector<Jet> AK4CHSjets_matched = event.get(h_CHSjets_matched);
  int CHS_matched_Njets = AK4CHSjets_matched.size();
  CHS_matched_N_jets->Fill(CHS_matched_Njets, weight);
  // cout << "does it pass Jet ID Tight?: "

  for(unsigned int i=0; i<AK4CHSjets_matched.size(); i++){
    CHS_matched_pt_jet->Fill(AK4CHSjets_matched.at(i).pt(),weight);
    CHS_matched_eta_jet->Fill(AK4CHSjets_matched.at(i).eta(),weight);
    CHS_matched_phi_jet->Fill(AK4CHSjets_matched.at(i).phi(),weight);
    CHS_matched_m_jet->Fill(AK4CHSjets_matched.at(i).v4().M(),weight);
    // CHS_matched_bscore_jet->Fill(AK4CHSjets_matched.at(i).btag_DeepJet(), weight);
    if(i==0){
      CHS_matched_pt_jet1->Fill(AK4CHSjets_matched.at(i).pt(),weight);
      CHS_matched_eta_jet1->Fill(AK4CHSjets_matched.at(i).eta(),weight);
      CHS_matched_phi_jet1->Fill(AK4CHSjets_matched.at(i).phi(),weight);
      CHS_matched_m_jet1->Fill(AK4CHSjets_matched.at(i).v4().M(),weight);
      // CHS_matched_bscore_jet1->Fill(AK4CHSjets_matched.at(i).btag_DeepJet(), weight);
    }
    else if(i==1){
      CHS_matched_pt_jet2->Fill(AK4CHSjets_matched.at(i).pt(),weight);
      CHS_matched_eta_jet2->Fill(AK4CHSjets_matched.at(i).eta(),weight);
      CHS_matched_phi_jet2->Fill(AK4CHSjets_matched.at(i).phi(),weight);
      CHS_matched_m_jet2->Fill(AK4CHSjets_matched.at(i).v4().M(),weight);
      // CHS_matched_bscore_jet2->Fill(AK4CHSjets_matched.at(i).btag_DeepJet(), weight);
    }
    else if(i==2){
      CHS_matched_pt_jet3->Fill(AK4CHSjets_matched.at(i).pt(),weight);
      CHS_matched_eta_jet3->Fill(AK4CHSjets_matched.at(i).eta(),weight);
      CHS_matched_phi_jet3->Fill(AK4CHSjets_matched.at(i).phi(),weight);
      CHS_matched_m_jet3->Fill(AK4CHSjets_matched.at(i).v4().M(),weight);
      // CHS_matched_bscore_jet3->Fill(AK4CHSjets_matched.at(i).btag_DeepJet(), weight);
    }
  }

  int CHS_matched_Nbjets_loose = 0, CHS_matched_Nbjets_medium = 0, CHS_matched_Nbjets_tight = 0;
  DeepJetBTag CHS_matched_Btag_loose  = DeepJetBTag(DeepJetBTag::WP_LOOSE);
  DeepJetBTag CHS_matched_Btag_medium = DeepJetBTag(DeepJetBTag::WP_MEDIUM);
  DeepJetBTag CHS_matched_Btag_tight  = DeepJetBTag(DeepJetBTag::WP_TIGHT);

  for (unsigned int i =0; i<AK4CHSjets_matched.size(); i++) {
    if(CHS_matched_Btag_loose(AK4CHSjets_matched.at(i),event))  CHS_matched_Nbjets_loose++;
    if(CHS_matched_Btag_medium(AK4CHSjets_matched.at(i),event)) CHS_matched_Nbjets_medium++;
    if(CHS_matched_Btag_tight(AK4CHSjets_matched.at(i),event))  CHS_matched_Nbjets_tight++;
  }

  CHS_matched_N_bJets_loose->Fill(CHS_matched_Nbjets_loose,weight);
  CHS_matched_N_bJets_med->Fill(CHS_matched_Nbjets_medium,weight);
  CHS_matched_N_bJets_tight->Fill(CHS_matched_Nbjets_tight,weight);




  // Check CHS ID working point
  int CHS_matched_jets_tightlepveto = 0, CHS_matched_jets_tight = 0, CHS_matched_jets_nottight = 0;
  JetPFID CHS_matched_LepVetoTight = JetPFID(JetPFID::WP_TIGHT_LEPVETO_CHS);
  JetPFID CHS_matched_Tight  = JetPFID(JetPFID::WP_TIGHT_CHS);

  for (unsigned int i =0; i<AK4CHSjets_matched.size(); i++) {
    if(CHS_matched_Tight(AK4CHSjets_matched.at(i),event))  CHS_matched_jets_tight++;
    if(!CHS_matched_Tight(AK4CHSjets_matched.at(i),event)) CHS_matched_jets_nottight++;
    
    if(CHS_matched_LepVetoTight(AK4CHSjets_matched.at(i),event))  CHS_matched_jets_tightlepveto++;
  }

  CHS_matched_N_Jets_LepVeto->Fill(CHS_matched_jets_tightlepveto,weight);
  CHS_matched_N_Jets_Tight->Fill(CHS_matched_jets_tight,weight);
  CHS_matched_N_Jets_NotTight->Fill(CHS_matched_jets_nottight,weight);

  



  // vector<Jet>* jets = event.jets;
  // vector<Jet> AK4CHSjets_matched = event.get(h_CHSjets_matched);

  ///calculate deltaR between CHS and Puppi Jet
  for(unsigned int i=0; i<jets->size(); i++){
    // cout << "event.run:"<<event.run <<endl;
    // cout<<"puppi jets size: "<<jets->size()<<endl;
    double dRmin_CHS_Puppi = 99999;
    double pt_chs=0;
    double eta_chs=0;
    if (jets->size()!=AK4CHSjets_matched.size()){
    cout << "Puppi size and CHS NOT eqaul"<<endl;
    }
    int CHS_matched_jets_tightlepveto_all = 0, CHS_matched_jets_tight_all = 0, CHS_matched_jets_nottight_all = 0;
    for(unsigned int j=0; j<AK4CHSjets_matched.size(); j++){
      
      double dR=deltaR(AK4CHSjets_matched.at(j),jets->at(i));
      double pt_match=AK4CHSjets_matched.at(j).pt();
      double eta_match=AK4CHSjets_matched.at(j).eta();

      if(dR < dRmin_CHS_Puppi){
        dRmin_CHS_Puppi = dR;
        pt_chs=pt_match;
        eta_chs=eta_match;
        if(CHS_matched_Tight(AK4CHSjets_matched.at(i),event))  CHS_matched_jets_tight_all++;
        if(!CHS_matched_Tight(AK4CHSjets_matched.at(i),event))  CHS_matched_jets_nottight_all++;
        if(CHS_matched_LepVetoTight(AK4CHSjets_matched.at(i),event))  CHS_matched_jets_tightlepveto_all++;

      }
    }
    CHS_matched_N_Jets_LepVeto_all->Fill(CHS_matched_jets_tightlepveto_all,weight);
    CHS_matched_N_Jets_Tight_all->Fill(CHS_matched_jets_tight_all,weight);
    CHS_matched_N_Jets_NotTight_all->Fill(CHS_matched_jets_nottight_all,weight);
    


    // cout << " matched to CHS pt: "<<pt_chs<<endl;
    diff_pt->Fill(pt_chs-jets->at(i).pt(),weight);
    diff_eta->Fill(eta_chs-jets->at(i).eta(),weight);
    ratio_chs_pt->Fill((pt_chs-jets->at(i).pt())/pt_chs,weight);
    ratio_puppi_pt->Fill((pt_chs-jets->at(i).pt())/jets->at(i).pt(),weight);
    ratio_chs_puppi_pt->Fill((pt_chs/jets->at(i).pt()),weight);
    ratio_chs_puppi_eta->Fill((eta_chs/jets->at(i).eta()),weight);

    // cout<<"about to fill all eta"<<endl;
    ratio_chs_eta->Fill((eta_chs-jets->at(i).eta())/eta_chs,weight);
    // cout<<"filled all eta"<<endl;
    ratio_puppi_eta->Fill((eta_chs-jets->at(i).eta())/jets->at(i).eta(),weight);

    if (jets->at(i).pt()>0 and jets->at(i).pt()<50.){
        diff_pt_bin1->Fill(pt_chs-jets->at(i).pt(),weight);
        diff_eta_bin1->Fill(eta_chs-jets->at(i).eta(),weight);
        ratio_chs_pt_bin1->Fill((pt_chs-jets->at(i).pt())/pt_chs,weight);
        ratio_puppi_pt_bin1->Fill((pt_chs-jets->at(i).pt())/jets->at(i).pt(),weight);
        ratio_chs_eta_bin1->Fill((eta_chs-jets->at(i).eta())/eta_chs,weight);
        ratio_puppi_eta_bin1->Fill((eta_chs-jets->at(i).eta())/jets->at(i).eta(),weight);
        ratio_chs_puppi_pt_bin1->Fill((pt_chs/jets->at(i).pt()),weight);
        ratio_chs_puppi_eta_bin1->Fill((eta_chs/jets->at(i).eta()),weight);
        CHS_matched_N_Jets_LepVeto_1->Fill(CHS_matched_jets_tightlepveto_all,weight);
        CHS_matched_N_Jets_Tight_1->Fill(CHS_matched_jets_tight_all,weight);
        CHS_matched_N_Jets_NotTight_1->Fill(CHS_matched_jets_nottight_all,weight);


      }
    if (jets->at(i).pt()>50 and jets->at(i).pt()<100.){
        diff_pt_bin2->Fill(pt_chs-jets->at(i).pt(),weight);
        diff_eta_bin2->Fill(eta_chs-jets->at(i).eta(),weight);
        ratio_chs_pt_bin2->Fill((pt_chs-jets->at(i).pt())/pt_chs,weight);
        ratio_puppi_pt_bin2->Fill((pt_chs-jets->at(i).pt())/jets->at(i).pt(),weight);
        ratio_chs_eta_bin2->Fill((eta_chs-jets->at(i).eta())/eta_chs,weight);
        ratio_puppi_eta_bin2->Fill((eta_chs-jets->at(i).eta())/jets->at(i).eta(),weight);
        ratio_chs_puppi_pt_bin2->Fill((pt_chs/jets->at(i).pt()),weight);
        ratio_chs_puppi_eta_bin2->Fill((eta_chs/jets->at(i).eta()),weight);
        CHS_matched_N_Jets_LepVeto_2->Fill(CHS_matched_jets_tightlepveto_all,weight);
        CHS_matched_N_Jets_Tight_2->Fill(CHS_matched_jets_tight_all,weight);
        CHS_matched_N_Jets_NotTight_2->Fill(CHS_matched_jets_nottight_all,weight);


    }
    if (jets->at(i).pt()>100){
       
        // if ((pt_chs-jets->at(i).pt())<-20){
        // // cout << "event.run:"<<event.run <<endl;
        // // // cout << event.run <<endl;
        // // cout <<" puppi pt: "<<jets->at(i).pt()<<endl;
        // // cout <<" chs pt: "<<pt_chs<<endl;
        // // cout <<" diff: "<<pt_chs-jets->at(i).pt()<<endl;
        // }
        diff_pt_bin3->Fill(pt_chs-jets->at(i).pt(),weight);
        ratio_chs_pt_bin3->Fill((pt_chs-jets->at(i).pt())/pt_chs,weight);
        ratio_puppi_pt_bin3->Fill((pt_chs-jets->at(i).pt())/jets->at(i).pt(),weight);
        diff_eta_bin3->Fill(eta_chs-jets->at(i).eta());
        ratio_chs_eta_bin3->Fill((eta_chs-jets->at(i).eta())/eta_chs,weight);
        // cout<<"about to fill eta"<<endl;
        ratio_puppi_eta_bin3->Fill((eta_chs-jets->at(i).eta())/jets->at(i).eta(),weight);
        ratio_chs_puppi_pt_bin3->Fill((pt_chs/jets->at(i).pt()),weight);
        ratio_chs_puppi_eta_bin3->Fill((eta_chs/jets->at(i).eta()),weight);
        CHS_matched_N_Jets_LepVeto_3->Fill(CHS_matched_jets_tightlepveto_all,weight);
        CHS_matched_N_Jets_Tight_3->Fill(CHS_matched_jets_tight_all,weight);
        CHS_matched_N_Jets_NotTight_3->Fill(CHS_matched_jets_nottight_all,weight);


        // cout<<"filled eta"<<endl;


    }

    CHS_matched_deltaRmin_CHS_Puppi->Fill(dRmin_CHS_Puppi,weight);
  }


} //Method



ZprimeSemiLeptonicCHSMatchHists::~ZprimeSemiLeptonicCHSMatchHists(){}
