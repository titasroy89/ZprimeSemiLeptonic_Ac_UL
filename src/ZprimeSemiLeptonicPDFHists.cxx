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
      const auto& genparticles = event.genparticles;
      ZprimeCandidate* BestZprimeCandidate = event.get(h_BestZprimeCandidateChi2);

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
      float Mreco = BestZprimeCandidate->Zprime_v4().M();
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