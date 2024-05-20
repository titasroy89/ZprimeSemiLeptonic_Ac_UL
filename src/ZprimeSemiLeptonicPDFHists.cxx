#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicPDFHists.h"
#include "UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicModules.h"
#include "UHH2/core/include/Event.h"
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

  isMuon = false; isElectron = false;
  if(ctx.get("channel") == "muon") isMuon = true;
  if(ctx.get("channel") == "electron") isElectron = true;

  for(int i=0; i<100; i++){
    std::stringstream ss_name;
    std::stringstream ss_name_tt;
    ss_name << "DeltaY_PDF_" << i+1;
    ss_name_tt << "DeltaY_PDF_RM_" << i+1;

    stringstream ss_title;
    stringstream ss_title_tt;
    ss_title << "#DeltaY_{t#bar{t}} [GeV] for PDF No. "  << i+1 << " out of 100" ;
    ss_title_tt << "#DeltaY_{t#bar{t}} RM [GeV] for PDF No. "  << i+1 << " out of 100" ;

    std::string s_name = ss_name.str();
    std::string s_name_tt = ss_name_tt.str();
    std::string s_title = ss_title.str();
    std::string s_title_tt = ss_title_tt.str();
    const char* char_name = s_name.c_str();
    const char* char_name_tt = s_name_tt.c_str();
    const char* char_title = s_title.c_str();
    const char* char_title_tt = s_title_tt.c_str();
 
    hist_names[i] = s_name;
    hist_names_tt[i] = s_name_tt;

    book<TH1F>(char_name, char_title,  2, -2.5, 2.5);
    book<TH2F>(char_name_tt, char_title_tt,  2, -2.5, 2.5, 2, -2.5, 2.5);

  }
}

void ZprimeSemiLeptonicPDFHists::fill(const Event & event){

  double weight = event.weight;

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
            // cout << "deltaR: " << deltaR(lep_top, genparticle_p4) << j << endl;
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
        //cout <<"Lepton is positive for PDF"<<endl;
        DeltaY_reco_best = TMath::Abs(0.5*TMath::Log((lep_top.energy() + lep_top.pt()*TMath::SinH(lep_top.eta()))/(lep_top.energy() - lep_top.pt()*TMath::SinH(lep_top.eta())))) - TMath::Abs(0.5*TMath::Log((had_top.energy() + had_top.pt()*TMath::SinH(had_top.eta()))/(had_top.energy() - had_top.pt()*TMath::SinH(had_top.eta()))));
        DeltaY_gen_best = TMath::Abs(0.5*TMath::Log((best_matched_gen_leptop.energy() + best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta()))/(best_matched_gen_leptop.energy() - best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta())))) - TMath::Abs(0.5*TMath::Log((best_matched_gen_hadtop.energy() + best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))/(best_matched_gen_hadtop.energy() - best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))));

        } else {
          //cout <<"Lepton is negative for PDF"<<endl;
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

      // 1) It iterates over 100 PDF weight variations stored in the event.genInfo->systweights()
      // 2) hist(name_tt) retrieves the histogram based on the name generated for each PDF variation.
      // The histogram is initially retrieved as a TH1
      // 3) The histogram is then cast to a TH2F to allow for 2D filling
      // dynamic_cast<TH2F*>(base_hist) converts TH1 pointer into a TH2F. 
      // This is necessary because I need to fill two dimensions (DeltaY_reco_best and DeltaY_gen_best) along with applying the weight


      // int MY_FIRST_INDEX = 9;
      // if(event.genInfo->systweights().size() > (unsigned int) 100 + MY_FIRST_INDEX){
      //   float orig_weight = event.genInfo->originalXWGTUP();
      //   for(int i=0; i<100; i++){
      //     double pdf_weight = event.genInfo->systweights().at(i+MY_FIRST_INDEX);
      //     const char* name_tt = hist_names_tt[i].c_str();
      //     hist(name_tt)->Fill(DeltaY_reco_best, DeltaY_gen_best, weight * pdf_weight / orig_weight);
      //   }
      // }

    }
    else{
      ZprimeCandidate* BestZprimeCandidate = event.get(h_BestZprimeCandidateChi2);
     // float Mreco = BestZprimeCandidate->Zprime_v4().M();
      float deltay=(TMath::Abs(BestZprimeCandidate->top_leptonic_v4().Rapidity()) - TMath::Abs(BestZprimeCandidate->top_hadronic_v4().Rapidity()));
      int MY_FIRST_INDEX = 9;
      if ( is_dy || is_wjets || is_qcd_HTbinned || is_alps || is_azh || is_htott_scalar || is_htott_pseudo || is_zprimetott ) MY_FIRST_INDEX = 47;
      if(event.genInfo->systweights().size() > (unsigned int) 100 + MY_FIRST_INDEX){
        float orig_weight = event.genInfo->originalXWGTUP();
        for(int i=0; i<100; i++){
          double pdf_weight = event.genInfo->systweights().at(i+MY_FIRST_INDEX);
          const char* name = hist_names[i].c_str();
          hist(name)->Fill(deltay,weight * pdf_weight / orig_weight);
        }
      }
    }
  }

  

}

ZprimeSemiLeptonicPDFHists::~ZprimeSemiLeptonicPDFHists(){}