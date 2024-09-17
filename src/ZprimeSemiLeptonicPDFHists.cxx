#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicPDFHists.h"
#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicModules.h"
#include "UHH2/core/include/Event.h"
#include <UHH2/core/include/Utils.h>
#include "UHH2/common/include/Utils.h"
#include "UHH2/common/include/JetIds.h"
#include <math.h>
#include <sstream>

#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/TTbarReconstruction.h>
#include <UHH2/common/include/ReconstructionHypothesisDiscriminators.h>

#include <UHH2/core/include/LorentzVector.h>
#include "TH1F.h"
#include "TH2F.h"
#include <iostream>

using namespace std;
using namespace uhh2;

ZprimeSemiLeptonicPDFHists::ZprimeSemiLeptonicPDFHists(uhh2::Context & ctx, const std::string& dirname): 
Hists(ctx, dirname){
 
  is_mc = ctx.get("dataset_type") == "MC";
  is_dy = ctx.get("dataset_version").find("DYJets") == 0;
  is_tt = ctx.get("dataset_version").find("TTTo") == 0;
  is_wjets = ctx.get("dataset_version").find("WJets") == 0;
  is_qcd_HTbinned = ctx.get("dataset_version").find("QCD_HT") == 0;
  is_alps = ctx.get("dataset_version").find("ALP") == 0;
  is_azh = ctx.get("dataset_version").find("AZH") == 0;
  is_htott_scalar = ctx.get("dataset_version").find("HscalarToTTTo") == 0;
  is_htott_pseudo = ctx.get("dataset_version").find("HpseudoToTTTo") == 0;
  is_zprimetott = ctx.get("dataset_version").find("ZPrimeToTT_") == 0;
  h_BestZprimeCandidateChi2 = ctx.get_handle<ZprimeCandidate*>("ZprimeCandidateBestChi2");
  h_is_zprime_reconstructed_chi2 = ctx.get_handle<bool>("is_zprime_reconstructed_chi2");
  ishotvr = (ctx.get("is_hotvr") == "true");
  isdeepAK8 = (ctx.get("is_deepAK8") == "true");
 

  isMuon = false; isElectron = false;
  if(ctx.get("channel") == "muon") isMuon = true;
  if(ctx.get("channel") == "electron") isElectron = true;
  if(isdeepAK8){
    h_AK8TopTags = ctx.get_handle<std::vector<TopJet>>("DeepAK8TopTags");
  }else if(ishotvr){
    h_AK8TopTags = ctx.get_handle<std::vector<TopJet>>("HOTVRTopTags");
  }
  h_CHSjets_matched = ctx.get_handle<std::vector<Jet>>("CHS_matched");

  for(int i=0; i<100; i++){
    std::stringstream ss_name;
    std::stringstream ss_name_tt;
    std::stringstream ss_name_dy_d1;
    std::stringstream ss_name_dy_d2;
    std::stringstream ss_name_sigma_1;
    std::stringstream ss_name_sigma_2;



    ss_name << "DeltaY_PDF_" << i+1;
    ss_name_tt << "DeltaY_PDF_RM_" << i+1;
    ss_name_dy_d1 << "DeltaY_reco_d1_PDF_" << i+1;
    ss_name_dy_d2 << "DeltaY_reco_d2_PDF_" << i+1;
    ss_name_sigma_1 << "Sigma_phi_1_PDF_" << i+1;
    ss_name_sigma_2 << "Sigma_phi_2_PDF_" << i+1;




    stringstream ss_title;
    stringstream ss_title_tt;
    stringstream ss_title_dy_d1;
    stringstream ss_title_dy_d2;
    stringstream ss_title_sigma_1;
    stringstream ss_title_sigma_2;


    ss_title << "#DeltaY_{t#bar{t}} for PDF No. "  << i+1 << " out of 100" ;
    ss_title_tt << "#DeltaY_{t#bar{t}} RM for PDF No. "  << i+1 << " out of 100" ;

    ss_title_dy_d1 <<"#DeltaY_{t#bar{t}} for #Delta #phi >0 for PDF No. "<< i+1 << " out of 100" ;
    ss_title_dy_d2 <<"#DeltaY_{t#bar{t}} for #Delta #phi <0 for PDF No. "<< i+1 << " out of 100" ;

    ss_title_sigma_1 <<"#Sigma #phi for #DeltaY >0 for PDF No. "<< i+1 << " out of 100" ;
    ss_title_sigma_2 <<"#Sigma #phi for #DeltaY <0 for PDF No. "<< i+1 << " out of 100" ;

    std::string s_name = ss_name.str();
    std::string s_name_dy_d1 = ss_name_dy_d1.str();
    std::string s_title_dy_d1 = ss_title_dy_d1.str();
    std::string s_name_dy_d2 = ss_name_dy_d2.str();
    std::string s_title_dy_d2 = ss_title_dy_d2.str();
    std::string s_name_sigma_1 = ss_name_sigma_1.str();
    std::string s_title_sigma_1 = ss_title_sigma_1.str();
    std::string s_name_sigma_2 = ss_name_sigma_2.str();
    std::string s_title_sigma_2 = ss_title_sigma_2.str();

    std::string s_name_tt = ss_name_tt.str();
    std::string s_title = ss_title.str();
    std::string s_title_tt = ss_title_tt.str();
    const char* char_name = s_name.c_str();
    const char* char_name_dy_d1 = s_name_dy_d1.c_str();
    const char* char_name_dy_d2 = s_name_dy_d2.c_str();
    const char* char_name_sigma_1 = s_name_sigma_1.c_str();
    const char* char_name_sigma_2 = s_name_sigma_2.c_str();
    const char* char_name_tt = s_name_tt.c_str();
    const char* char_title = s_title.c_str();
    const char* char_title_tt = s_title_tt.c_str();
    const char* char_title_dy_d1 = s_title_dy_d1.c_str();
    const char* char_title_dy_d2 = s_title_dy_d2.c_str();
    const char* char_title_sigma_1 = s_title_sigma_1.c_str();
    const char* char_title_sigma_2 = s_title_sigma_2.c_str();


 
    hist_names[i] = s_name;
    hist_names_tt[i] = s_name_tt;
    hist_names_dy_d1[i] = s_name_dy_d1;
    hist_names_dy_d2[i] = s_name_dy_d2;
    hist_names_sigma_1[i] = s_name_sigma_1;
    hist_names_sigma_2[i] = s_name_sigma_2;

    book<TH1F>(char_name_dy_d1, char_title_dy_d1,  2, -2.5, 2.5);
    book<TH1F>(char_name_dy_d2, char_title_dy_d2,  2, -2.5, 2.5);
    book<TH1F>(char_name_sigma_1, char_title_sigma_1,  16, -3.2, 3.2);
    book<TH1F>(char_name_sigma_2, char_title_sigma_2,  16, -3.2, 3.2);
    book<TH1F>(char_name, char_title,  2, -2.5, 2.5);
    book<TH2F>(char_name_tt, char_title_tt,  2, -2.5, 2.5, 2, -2.5, 2.5);

  }
}

void ZprimeSemiLeptonicPDFHists::fill(const Event & event){

  double weight = event.weight;
  bool debug=false;
  bool is_zprime_reconstructed_chi2 = event.get(h_is_zprime_reconstructed_chi2);
  if(is_zprime_reconstructed_chi2 && is_mc){
    if(is_tt){
      if (debug)cout<<" doing ttbar sample" <<endl;

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
      std::vector<std::pair<double, int>> deltaR_leptonic_values; // ((dR, index), (dR, index), ...)
      std::vector<std::pair<double, int>> deltaR_hadronic_values;

      double deltaR_min_leptonic = 99.0;
      double deltaR_sec_min_leptonic = 99.0;
      int best_gen_for_leptop = -1;
      int sec_best_gen_for_leptop = -1;
      // bool is_leptop_matched = false;

      double deltaR_min_hadronic = 99.0;
      double deltaR_sec_min_hadronic = 99.0;
      int best_gen_for_hadtop = -1;
      int sec_best_gen_for_hadtop = -1;
      // bool is_hadtop_matched = false;

      for(unsigned int j=0; j<genparticles->size(); ++j) {
        if(abs(genparticles->at(j).pdgId()) == 6 ){
          if (genparticles->at(j).index() == 2 || genparticles->at(j).index() == 3){
            LorentzVector genparticle_p4(genparticles->at(j).pt(), genparticles->at(j).eta(), genparticles->at(j).phi(), genparticles->at(j).energy());
            deltaR_leptonic_values.push_back(std::make_pair(deltaR(lep_top, genparticle_p4),genparticles->at(j).index() ));
            deltaR_hadronic_values.push_back(std::make_pair(deltaR(had_top, genparticle_p4), genparticles->at(j).index()));
            // if (debug)cout << "deltaR: " << deltaR(lep_top, genparticle_p4) << j << endl;
          }
        }
      }  
      
      for (const auto& pair_lep : deltaR_leptonic_values) {
        if (pair_lep.first > 0 && pair_lep.first < deltaR_min_leptonic) {
          // deltaR_min_leptonic = pair_lep.first;
          deltaR_sec_min_leptonic = deltaR_min_leptonic;
          deltaR_min_leptonic = pair_lep.first;
          sec_best_gen_for_leptop = best_gen_for_leptop;
          best_gen_for_leptop = pair_lep.second;
          // is_leptop_matched = true;
        }
        else if (pair_lep.first > 0 && pair_lep.first < deltaR_sec_min_leptonic && pair_lep.first != deltaR_min_leptonic && pair_lep.second != best_gen_for_leptop) {
          deltaR_sec_min_leptonic = pair_lep.first;
          sec_best_gen_for_leptop = pair_lep.second;
        }
      }

      // deltaY values calculation starts:

      // matched gen particles
      for (const auto& pair_had : deltaR_hadronic_values) {
        if (pair_had.first > 0 && pair_had.first < deltaR_min_hadronic) {
          // deltaR_min_hadronic = pair_had.first;
          deltaR_sec_min_hadronic = deltaR_min_hadronic;
          deltaR_min_hadronic = pair_had.first;
          sec_best_gen_for_hadtop = best_gen_for_hadtop;
          best_gen_for_hadtop = pair_had.second;
          // is_hadtop_matched = true;
        }
        else if (pair_had.first > 0 && pair_had.first < deltaR_sec_min_hadronic && pair_had.first != deltaR_min_hadronic && pair_had.second != best_gen_for_hadtop) {
          deltaR_sec_min_hadronic = pair_had.first;
          sec_best_gen_for_hadtop = pair_had.second;
        }
      }

      if (best_gen_for_hadtop == best_gen_for_leptop){
        if (deltaR_min_leptonic <= deltaR_min_hadronic){
          best_gen_for_hadtop = sec_best_gen_for_hadtop;
          deltaR_min_hadronic = deltaR_sec_min_hadronic;
        } else {
          best_gen_for_leptop = sec_best_gen_for_leptop;
          deltaR_min_leptonic = deltaR_sec_min_leptonic;
        }
      }

      GenParticle best_matched_gen_leptop;
      GenParticle best_matched_gen_hadtop;

      float_t DeltaY_gen_best = 99.0;
      float_t DeltaY_reco_best = 99.0;
      bool isLeptonPositive = false;

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

      if (deltaR_min_leptonic < 0.4 && deltaR_min_hadronic < 0.4 && best_gen_for_leptop >= 0 && best_gen_for_hadtop >= 0) {
     
        if(static_cast<std::size_t>(best_gen_for_leptop) < genparticles->size()) {
          best_matched_gen_leptop = genparticles->at(best_gen_for_leptop);
        }
        
        if(static_cast<std::size_t>(best_gen_for_hadtop) < genparticles->size()) {
            best_matched_gen_hadtop = genparticles->at(best_gen_for_hadtop);
        }

        if (isLeptonPositive) {
        //if (debug)cout <<"Lepton is positive for PDF"<<endl;
        DeltaY_reco_best = TMath::Abs(0.5*TMath::Log((lep_top.energy() + lep_top.pt()*TMath::SinH(lep_top.eta()))/(lep_top.energy() - lep_top.pt()*TMath::SinH(lep_top.eta())))) - TMath::Abs(0.5*TMath::Log((had_top.energy() + had_top.pt()*TMath::SinH(had_top.eta()))/(had_top.energy() - had_top.pt()*TMath::SinH(had_top.eta()))));
        DeltaY_gen_best = TMath::Abs(0.5*TMath::Log((best_matched_gen_leptop.energy() + best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta()))/(best_matched_gen_leptop.energy() - best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta())))) - TMath::Abs(0.5*TMath::Log((best_matched_gen_hadtop.energy() + best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))/(best_matched_gen_hadtop.energy() - best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))));

        } else {
          //if (debug)cout <<"Lepton is negative for PDF"<<endl;
          DeltaY_reco_best = TMath::Abs(0.5*TMath::Log((had_top.energy() + had_top.pt()*TMath::SinH(had_top.eta()))/(had_top.energy() - had_top.pt()*TMath::SinH(had_top.eta())))) - TMath::Abs(0.5*TMath::Log((lep_top.energy() + lep_top.pt()*TMath::SinH(lep_top.eta()))/(lep_top.energy() - lep_top.pt()*TMath::SinH(lep_top.eta()))));
          DeltaY_gen_best = TMath::Abs(0.5*TMath::Log((best_matched_gen_hadtop.energy() + best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))/(best_matched_gen_hadtop.energy() - best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta())))) - TMath::Abs(0.5*TMath::Log((best_matched_gen_leptop.energy() + best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta()))/(best_matched_gen_leptop.energy() - best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta()))));

        }
      }
      
      
      

      // Fill the histogram

      int MY_FIRST_INDEX = 9;
      if(event.genInfo->systweights().size() > (unsigned int) 100 + MY_FIRST_INDEX){
        float orig_weight = event.genInfo->originalXWGTUP();
        for(int i=0; i<100; i++){
          double pdf_weight = event.genInfo->systweights().at(i + MY_FIRST_INDEX);
          const char* name_tt = hist_names_tt[i].c_str();
          TH1* base_hist = hist(name_tt); // Retrieve histogram using base class method
          TH2F* hist2d = dynamic_cast<TH2F*>(base_hist); // Attempt to cast to TH2F

          if(hist2d) {
              hist2d->Fill(DeltaY_reco_best, DeltaY_gen_best, weight * pdf_weight / orig_weight);
          } else {
              // Handle the error if the histogram is not of type TH2F
              std::cerr << "Histogram casting error for: " << name_tt << std::endl;
          }
        }
      }


    }// loop ending for ttbar only
    //else{
    if (debug)cout << "checking for all MC" << endl;
    ZprimeCandidate* BestZprimeCandidate = event.get(h_BestZprimeCandidateChi2);
    bool is_toptag_reconstruction = BestZprimeCandidate->is_toptag_reconstruction();
    // h_AK8TopTags = ctx.get_handle<std::vector<TopJet>>("DeepAK8TopTags");
    // h_CHSjets_matched = ctx.get_handle<std::vector<Jet>>("CHS_matched");
    if (debug)cout << "about to define vectors" << endl;  
    vector <TopJet> TopTaggedJets = event.get(h_AK8TopTags); 
    if (debug)cout << "define AK8 CHSJets" << endl;   
    vector <Jet> AK4CHSjets_matched = event.get(h_CHSjets_matched);   
    if (debug)cout << "define AK4 CHSJets" << endl;               // AK4Puppijets that have been matched to CHSjets
    vector <float> jets_hadronic_bscores; 
    if (debug)cout << "define float for bscore" << endl;
    // float Mreco = BestZprimeCandidate->Zprime_v4().M();
    
    // bool is_toptag_reconstruction = BestZprimeCandidate->is_toptag_reconstruction();
    // LorentzVector toplep = BestZprimeCandidate->top_leptonic_v4();
    LorentzVector tophad = BestZprimeCandidate->top_hadronic_v4();
    float pt_hadTop_thresh = 150;   
    float pt_hadTop = tophad.pt();
    float bscore_max = -2;
    if(!is_toptag_reconstruction){
        // Loop over resolved hadronic jets to find their bscore via CHS jets
      for(unsigned int i=0; i<BestZprimeCandidate->jets_hadronic().size(); i++){
        double deltaR_min = 99;
        // Match resolved hadronic jets to CHS jets (which have bscores)
        for(unsigned int j=0; j<AK4CHSjets_matched.size(); j++){
          double deltaR_CHS = deltaR(BestZprimeCandidate->jets_hadronic().at(i), AK4CHSjets_matched.at(j));
          if(deltaR_CHS < deltaR_min) deltaR_min = deltaR_CHS;}
        // Build bScore-vector for resolved hadronic jets whose bscore will correspond by index
        for(unsigned int k=0; k<AK4CHSjets_matched.size(); k++){
          if(deltaR(BestZprimeCandidate->jets_hadronic().at(i), AK4CHSjets_matched.at(k)) == deltaR_min) 
          jets_hadronic_bscores.emplace_back(AK4CHSjets_matched.at(k).btag_DeepJet());} // Using DeepJet btag score
      }
      // Loop over bScores-vector to extract highest bscore
      for(unsigned int i=0; i<jets_hadronic_bscores.size(); i++){
        float bscore = jets_hadronic_bscores.at(i);
        if(bscore > bscore_max) bscore_max = bscore;
      }
    
    }
    if(is_toptag_reconstruction){
        // Loop over hadronic top's subjets to extract highest bscore
      for(unsigned int i=0; i < BestZprimeCandidate->tophad_topjet_ptr()->subjets().size(); i++){
        float bscore = BestZprimeCandidate->tophad_topjet_ptr()->subjets().at(i).btag_DeepJet(); // Using DeepJet btag score
        if(bscore > bscore_max) bscore_max = bscore;
      }
    
    }
    if (debug)cout << "about to define boost"<<endl;
    TLorentzVector had_top_b(0, 0, 0, 0);

        // Resolved topology
        if(!is_toptag_reconstruction){ // Define hadronic b-jet as hadronic AK4-jet with highest bscore
          for(unsigned int i=0; i< BestZprimeCandidate->jets_hadronic().size(); i++){
            float bscore = jets_hadronic_bscores.at(i);
            if(bscore == bscore_max) had_top_b.SetPtEtaPhiE(BestZprimeCandidate->jets_hadronic().at(i).pt(), 
                                                            BestZprimeCandidate->jets_hadronic().at(i).eta(), 
                                                            BestZprimeCandidate->jets_hadronic().at(i).phi(), 
                                                            BestZprimeCandidate->jets_hadronic().at(i).energy());
          }
        }
        // Merged topology
        if(is_toptag_reconstruction){ // Define hadronic b-jet as hadronic AK8-subjet with highest bscore
          for(unsigned int j=0; j < BestZprimeCandidate->tophad_topjet_ptr()->subjets().size(); j++){
            float bscore = BestZprimeCandidate->tophad_topjet_ptr()->subjets().at(j).btag_DeepJet();
            if(bscore == bscore_max) had_top_b.SetPtEtaPhiE(BestZprimeCandidate->tophad_topjet_ptr()->subjets().at(j).pt(), 
                                                            BestZprimeCandidate->tophad_topjet_ptr()->subjets().at(j).eta(), 
                                                            BestZprimeCandidate->tophad_topjet_ptr()->subjets().at(j).phi(), 
                                                            BestZprimeCandidate->tophad_topjet_ptr()->subjets().at(j).energy());
          }
        }

      // Lepton 4-vector
        TLorentzVector lep_top_lep(0, 0, 0, 0);
        LorentzVector lep = BestZprimeCandidate->lepton().v4();
        lep_top_lep.SetPtEtaPhiE(lep.pt(), lep.eta(), lep.phi(), lep.E());
        //------------------------------------Define 4vectors of hadronic b-jet and lepton------------------------------------//


        //-------------------------------- Begin boosting top quarks and their decay products --------------------------------//
        // Define 4vectors of top quarks
        TLorentzVector PosTop(0, 0, 0, 0);
        TLorentzVector NegTop(0, 0, 0, 0);

        // POSITIVE LEPTON CONFIGURATION => Positive charged lepton has Positive Top mother
        if(BestZprimeCandidate->lepton().charge() > 0){
          // Define ttbar system
          PosTop.SetPtEtaPhiE(BestZprimeCandidate->top_leptonic_v4().pt(), 
                              BestZprimeCandidate->top_leptonic_v4().eta(), 
                              BestZprimeCandidate->top_leptonic_v4().phi(), 
                              BestZprimeCandidate->top_leptonic_v4().energy());
          NegTop.SetPtEtaPhiE(BestZprimeCandidate->top_hadronic_v4().pt(), 
                              BestZprimeCandidate->top_hadronic_v4().eta(), 
                              BestZprimeCandidate->top_hadronic_v4().phi(), 
                              BestZprimeCandidate->top_hadronic_v4().energy());
        }
        else if (BestZprimeCandidate->lepton().charge() < 0)
        {
        PosTop.SetPtEtaPhiE(BestZprimeCandidate->top_hadronic_v4().pt(), 
                              BestZprimeCandidate->top_hadronic_v4().eta(), 
                              BestZprimeCandidate->top_hadronic_v4().phi(), 
                              BestZprimeCandidate->top_hadronic_v4().energy());
        NegTop.SetPtEtaPhiE(BestZprimeCandidate->top_leptonic_v4().pt(), 
                              BestZprimeCandidate->top_leptonic_v4().eta(), 
                              BestZprimeCandidate->top_leptonic_v4().phi(), 
                              BestZprimeCandidate->top_leptonic_v4().energy());
        }
        
          TLorentzVector ttbar = PosTop + NegTop;
          // Boost into ttbar CoM-Frame <<<-------//
          lep_top_lep.Boost(-ttbar.BoostVector());
          had_top_b.Boost(-ttbar.BoostVector());
          PosTop.Boost(-ttbar.BoostVector());
          NegTop.Boost(-ttbar.BoostVector());

          // Rotate vectors into Helicity Frame <<<------//
          // Rotate about beamline
          lep_top_lep.RotateZ(-1.*PosTop.Phi());
          had_top_b.RotateZ(-1.*PosTop.Phi());
          PosTop.RotateZ(-1.*PosTop.Phi());
          NegTop.RotateZ(-1.*PosTop.Phi());
          // Rotate about y-axis
          lep_top_lep.RotateY(-1.*PosTop.Theta());
          had_top_b.RotateY(-1.*PosTop.Theta());
          PosTop.RotateY(-1.*PosTop.Theta());
          NegTop.RotateY(-1.*PosTop.Theta());

          // Boost into ttbar Rest-Frame <<<--------//
          lep_top_lep.Boost(-PosTop.BoostVector()); // Positive charged lepton has Positive Top mother
          had_top_b.Boost(-NegTop.BoostVector());   // Positive charged lepton means b-jet has Negative Top mother

        //-------------------------------- End boosting top quarks and their decay products --------------------------------//
    
        // Define angular variables as sum and difference of decay products' phi-coordinates
        // sphi and dphi = PosTopDecayProd_phi +- NegTopDecayProd_phi
        if (debug)cout << "done with boost"<<endl;
        float dphi=0.;
        float sphi = lep_top_lep.Phi() + had_top_b.Phi();
        if(BestZprimeCandidate->lepton().charge() > 0){ // lepton is Positive Top's Decay Product
          dphi = lep_top_lep.Phi() - had_top_b.Phi();
        }
        if(BestZprimeCandidate->lepton().charge() < 0)
        {
          dphi = had_top_b.Phi() - lep_top_lep.Phi();
        }
        if (debug)cout << "spin corr vars defined"<<endl;
          // Map back into original domain if necessary
        if(sphi > TMath::Pi()) sphi = sphi - 2*TMath::Pi();
        if(sphi < -TMath::Pi()) sphi = sphi + 2*TMath::Pi();
        if(dphi > TMath::Pi()) dphi = dphi - 2*TMath::Pi();
        if(dphi < -TMath::Pi()) dphi = dphi + 2*TMath::Pi();
        
    
      float deltay=(TMath::Abs(BestZprimeCandidate->top_leptonic_v4().Rapidity()) - TMath::Abs(BestZprimeCandidate->top_hadronic_v4().Rapidity()));
      int MY_FIRST_INDEX = 9;
      if ( is_dy || is_wjets || is_qcd_HTbinned || is_alps || is_azh || is_htott_scalar || is_htott_pseudo || is_zprimetott ) MY_FIRST_INDEX = 47;
      if(event.genInfo->systweights().size() > (unsigned int) 100 + MY_FIRST_INDEX){
        float orig_weight = event.genInfo->originalXWGTUP();
        for(int i=0; i<100; i++){
          double pdf_weight = event.genInfo->systweights().at(i+MY_FIRST_INDEX);
          const char* name = hist_names[i].c_str();
          const char* name_dy_d1 = hist_names_dy_d1[i].c_str();
          const char* name_dy_d2 = hist_names_dy_d2[i].c_str();
          const char* name_sigma_1 = hist_names_sigma_1[i].c_str();
          const char* name_sigma_2 = hist_names_sigma_2[i].c_str();
          if (debug)cout <<" about to fill histos" <<endl;
          if (pt_hadTop > pt_hadTop_thresh && deltay >0){
            hist(name_sigma_1)->Fill(sphi,weight * pdf_weight / orig_weight);
            if (debug)cout <<" done with sigma 1" <<endl;
          }
          if (pt_hadTop > pt_hadTop_thresh && deltay <0){
            hist(name_sigma_2)->Fill(sphi,weight * pdf_weight / orig_weight);
            if (debug)cout <<" done with sigma 2" <<endl;
          }
          if(pt_hadTop < pt_hadTop_thresh && dphi >0){
            hist(name_dy_d1)->Fill(deltay,weight * pdf_weight / orig_weight);
            if (debug)cout <<" done with dy 1" <<endl;
          }
          if(pt_hadTop < pt_hadTop_thresh && dphi < 0){
            hist(name_dy_d2)->Fill(deltay,weight * pdf_weight / orig_weight);
            if (debug)cout <<" done with dy 2" <<endl;
          }
          hist(name)->Fill(deltay,weight * pdf_weight / orig_weight);
          if (debug)cout <<" done with dy" <<endl;
        }
      }
    //} get rid of else for ttbar 
  }

  

}

ZprimeSemiLeptonicPDFHists::~ZprimeSemiLeptonicPDFHists(){}