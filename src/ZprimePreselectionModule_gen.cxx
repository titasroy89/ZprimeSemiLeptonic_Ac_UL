#include <iostream>
#include <memory>
#include <fstream>
#include <cstdlib>
#include "TVector3.h"
#include "Math/LorentzVector.h"
#include "Math/PtEtaPhiE4D.h"

#include <cmath>

#include <UHH2/core/include/AnalysisModule.h>
#include <UHH2/core/include/Event.h>
#include <UHH2/core/include/Selection.h>
#include "UHH2/common/include/PrintingModules.h"

#include <UHH2/common/include/CleaningModules.h>
#include <UHH2/common/include/NSelections.h>
#include <UHH2/common/include/LumiSelection.h>
#include <UHH2/common/include/TriggerSelection.h>
#include <UHH2/common/include/JetCorrections.h>
#include <UHH2/common/include/JetCorrectionSets.h>
#include <UHH2/common/include/ObjectIdUtils.h>
#include <UHH2/common/include/MuonIds.h>
#include <UHH2/common/include/ElectronIds.h>
#include <UHH2/common/include/JetIds.h>
#include <UHH2/common/include/TopJetIds.h>
#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/Utils.h>
#include <UHH2/common/include/AdditionalSelections.h>
#include "UHH2/common/include/LuminosityHists.h"
#include <UHH2/common/include/MuonHists.h>
#include <UHH2/common/include/ElectronHists.h>
#include <UHH2/common/include/JetHists.h>
#include <UHH2/common/include/EventHists.h>
#include <UHH2/common/include/CommonModules.h>
#include <UHH2/common/include/GenTools_2.h>

#include <UHH2/ZprimeSemiLeptonic/include/ModuleBASE.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicSelections.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicPreselectionHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicGeneratorHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/CHSJetCorrections.h>
#include <UHH2/ZprimeSemiLeptonic/include/TopPuppiJetCorrections.h>
#include "UHH2/HOTVR/include/HOTVRJetCorrectionModule.h"

#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicModules.h>
#include <UHH2/ZprimeSemiLeptonic/include/utils.h>
#include <UHH2/core/include/LorentzVector.h>
#include <UHH2/common/include/ReconstructionHypothesisDiscriminators.h>


using namespace std;
using namespace uhh2;

class ZprimePreselectionModule_gen : public ModuleBASE {

public:
  explicit ZprimePreselectionModule_gen(uhh2::Context&);
  virtual bool process(uhh2::Event&) override;
  void book_histograms(uhh2::Context&, vector<string>);
  void fill_histograms(uhh2::Event&, string);

protected:
  bool debug;

  // Corrections
  std::unique_ptr<CommonModules> common;
  std::unique_ptr<AnalysisModule> hotvrjetCorr;
  std::unique_ptr<TopPuppiJetCorrections> toppuppijetCorr;
  std::unique_ptr<CHSJetCorrections> CHSjetCorr;

  // Cleaners
  std::unique_ptr<JetCleaner>      jet_IDcleaner, jet_cleaner1, jet_cleaner2;
  std::unique_ptr<AnalysisModule>  hotvrjet_cleaner;
  std::unique_ptr<TopJetCleaner>   topjet_puppi_IDcleaner, topjet_puppi_cleaner;

  // Selections
  std::unique_ptr<uhh2::Selection> genflavor_sel;
  std::unique_ptr<uhh2::Selection> jet1_sel;
  std::unique_ptr<uhh2::Selection> jet2_sel;
  std::unique_ptr<uhh2::Selection> met_sel;
  

  Event::Handle<float> h_top_pt;
  Event::Handle<float> h_top_eta;
  Event::Handle<float> h_top_phi; 

  Event::Handle<float> h_antitop_pt;
  Event::Handle<float> h_antitop_eta; 
  Event::Handle<float> h_antitop_phi;  

  Event::Handle<float> h_tops_pt;
  Event::Handle<float> h_tops_eta; 
  Event::Handle<float> h_tops_phi; 

  Event::Handle<float> h_muon_pt; 
  Event::Handle<float> h_muon_eta;
  Event::Handle<float> h_muon_phi;

  Event::Handle<float> h_ele_pt; 
  Event::Handle<float> h_ele_eta;
  Event::Handle<float> h_ele_phi;

  Event::Handle<float> h_lepton_pt; //-beren 
  Event::Handle<float> h_lepton_eta; //-beren
  Event::Handle<float> h_lepton_phi; //-beren

  Event::Handle<float> h_angle_top_antitop; //-beren

  Event::Handle<float> h_bquark_pt; //-beren
  Event::Handle<float> h_bquark_eta; //-beren

  Event::Handle<float> h_ttbar_mass;
  Event::Handle<float> h_MET; //-beren

  Event::Handle<int> h_topMultiplicity; //-beren
  
  Event::Handle<int> h_leptonFlavor; //-beren
  Event::Handle<float> h_motherPdgId; //-beren

  Event::Handle<float> h_nonTopMotherJets; //-beren
  Event::Handle<float> h_jetMultiplicity; //-beren

  uhh2::Event::Handle<std::vector<GenJet>> h_jets;
  Event::Handle<vector<Particle>> h_mygenjets;


  double HT_lep_cut; // HT cut
  std::unique_ptr<uhh2::Selection> htlep_sel; //HT cut



  bool isMC, isHOTVR;
  string Sys_PU;

  std::unique_ptr<Hists> lumihists;
  TString METcollection;

  bool isUL16preVFP, isUL16postVFP, isUL17, isUL18;

  // additional branch with AK4 CHS jets -> for b-tagging
  Event::Handle<vector<Jet>> h_CHSjets;
  // Event::Handle<vector<Particle>> h_mygenjets;


};


void ZprimePreselectionModule_gen::book_histograms(uhh2::Context& ctx, vector<string> tags){
  for(const auto & tag : tags){
    string mytag = tag+"_General";
    book_HFolder(mytag, new ZprimeSemiLeptonicPreselectionHists(ctx,mytag));
  }
}

void ZprimePreselectionModule_gen::fill_histograms(uhh2::Event& event, string tag){
  string mytag = tag+"_General";
  HFolder(mytag)->fill(event);
}



ZprimePreselectionModule_gen::ZprimePreselectionModule_gen(uhh2::Context& ctx){
    
  debug = true;

  for(auto & kv : ctx.get_all()){
    cout << " " << kv.first << " = " << kv.second << endl;
  }

  //// CONFIGURATION
  const TString METcollection = ctx.get("METName");
  isMC    = ctx.get("dataset_type") == "MC";
  isHOTVR = ctx.get("is_HOTVR") == "true";
  Sys_PU  = ctx.get("Sys_PU");

  isUL16preVFP  = (ctx.get("dataset_version").find("UL16preVFP")  != std::string::npos);
  isUL16postVFP = (ctx.get("dataset_version").find("UL16postVFP") != std::string::npos);
  isUL17        = (ctx.get("dataset_version").find("UL17")        != std::string::npos);
  isUL18        = (ctx.get("dataset_version").find("UL18")        != std::string::npos);

  // lepton IDs
  // ElectronId eleID_veto = ElectronID_Fall17_tight_noIso; - eleID_veto tag changed
  ElectronId eleID_veto = ElectronTagID(Electron::mvaEleID_Fall17_noIso_V2_wp90);
  MuonId     muID_veto  = MuonID(Muon::CutBasedIdTight);

  double electron_pt(25.);
  double muon_pt(25.);
  double jet1_pt(30.);
  double jet2_pt(30.);
  double MET(20.);
  HT_lep_cut = 500; // HT cut


  // GEN Flavor selection [W+jets flavor-splitting]
  if(ctx.get("dataset_version").find("WJets") != std::string::npos){

    if     (ctx.get("dataset_version").find("_B") != std::string::npos) genflavor_sel.reset(new GenFlavorSelection("b"));
    else if(ctx.get("dataset_version").find("_C") != std::string::npos) genflavor_sel.reset(new GenFlavorSelection("c"));
    else if(ctx.get("dataset_version").find("_L") != std::string::npos) genflavor_sel.reset(new GenFlavorSelection("l"));

    else genflavor_sel.reset(new uhh2::AndSelection(ctx));
  }
  else genflavor_sel.reset(new uhh2::AndSelection(ctx));


  // Cleaning: Mu, Ele, Jets
  const MuonId muonID_veto(AndId<Muon>(PtEtaCut(muon_pt, 2.4), muID_veto));
  const ElectronId electronID_veto(AndId<Electron>(PtEtaSCCut(electron_pt, 2.5), eleID_veto));
  const JetPFID jetID_CHS(JetPFID::WP_TIGHT_CHS);
  const JetPFID jetID_PUPPI(JetPFID::WP_TIGHT_PUPPI);

  jet_IDcleaner.reset(new JetCleaner(ctx, jetID_PUPPI));
  jet_cleaner1.reset(new JetCleaner(ctx, 15., 3.0));
  jet_cleaner2.reset(new JetCleaner(ctx, 20., 2.5));
  hotvrjet_cleaner.reset(new TopJetCleaner(ctx, PtEtaCut(200., 2.5)));
  topjet_puppi_IDcleaner.reset(new TopJetCleaner(ctx, jetID_PUPPI, "toppuppijets"));
  topjet_puppi_cleaner.reset(new TopJetCleaner(ctx, TopJetId(PtEtaCut(200., 2.5)), "toppuppijets"));

  htlep_sel.reset(new HTlepCut(HT_lep_cut, uhh2::infinity));


  // common modules
  common.reset(new CommonModules());
  common->switch_jetlepcleaner(true);
  // common->disable_pvfilter();
  common->disable_jetpfidfilter();
  common->switch_jetPtSorter(true);
  common->switch_metcorrection(true);
  common->set_muon_id(muonID_veto);
  common->set_electron_id(electronID_veto);
  common->init(ctx, Sys_PU);

  hotvrjetCorr.reset(new HOTVRJetCorrectionModule(ctx));

  toppuppijetCorr.reset(new TopPuppiJetCorrections());
  toppuppijetCorr->init(ctx);

  CHSjetCorr.reset(new CHSJetCorrections());
  CHSjetCorr->init(ctx);

  //// EVENT SELECTION
  jet1_sel.reset(new NJetSelection(1, -1, JetId(PtEtaCut(jet1_pt, 2.5))));
  jet2_sel.reset(new NJetSelection(2, -1, JetId(PtEtaCut(jet2_pt, 2.5))));
  met_sel.reset(new METCut(MET, uhh2::infinity));

  // additional branch with Ak4 CHS jets
  h_CHSjets = ctx.get_handle<vector<Jet>>("jetsAk4CHS");

  h_ttbar_mass = ctx.declare_event_output<float> ("ttbar_mass");

  h_lepton_pt = ctx.declare_event_output<float> ("lepton_pt");
  h_lepton_eta = ctx.declare_event_output<float> ("lepton_eta"); 
  h_lepton_phi = ctx.declare_event_output<float> ("lepton_phi"); 

  h_ele_pt = ctx.declare_event_output<float> ("ele_pt");
  h_ele_eta = ctx.declare_event_output<float> ("ele_eta");
  h_ele_phi = ctx.declare_event_output<float> ("ele_phi");

  h_muon_pt = ctx.declare_event_output<float> ("muon_pt");
  h_muon_eta = ctx.declare_event_output<float> ("muon_eta");
  h_muon_phi = ctx.declare_event_output<float> ("muon_phi");

  h_MET = ctx.declare_event_output<float> ("MET"); 
  h_bquark_pt = ctx.declare_event_output<float> ("bquark_pt"); 
  h_bquark_eta = ctx.declare_event_output<float> ("bquark_eta"); 
  h_angle_top_antitop = ctx.declare_event_output<float> ("angle_top_antitop");
  
  h_motherPdgId = ctx.declare_event_output<float> ("motherPdgId"); 
  h_leptonFlavor = ctx.declare_event_output<int> ("leptonFlavor"); 
  h_topMultiplicity = ctx.declare_event_output<int> ("topMultiplicity"); 
  
  h_nonTopMotherJets = ctx.declare_event_output<float> ("nonTopMotherJets"); 
  h_jetMultiplicity = ctx.declare_event_output<float> ("jetMultiplicity"); 
  // h_jets = ctx.get_handle<std::vector<GenJet>>("jetCollection");

  h_top_pt = ctx.declare_event_output<float> ("top_pt");
  h_top_eta = ctx.declare_event_output<float> ("top_eta");
  h_top_phi = ctx.declare_event_output<float> ("top_phi"); 

  h_antitop_pt = ctx.declare_event_output<float> ("antitop_pt");
  h_antitop_eta = ctx.declare_event_output<float> ("antitop_eta"); 
  h_antitop_phi = ctx.declare_event_output<float> ("antitop_phi"); 

  h_tops_pt = ctx.declare_event_output<float> ("tops_pt");
  h_tops_eta = ctx.declare_event_output<float> ("tops_pt");
  h_tops_phi = ctx.declare_event_output<float> ("tops_pt"); 






  // Book histograms
  vector<string> histogram_tags = {"Input"};

  book_histograms(ctx, histogram_tags);

  lumihists.reset(new LuminosityHists(ctx, "lumi"));
}


bool ZprimePreselectionModule_gen::process(uhh2::Event& event){

  if(debug) cout << "++++++++++++ NEW EVENT ++++++++++++++" << endl;
  if(debug) cout << " run.event: " << event.run << ". " << event.event << endl;
  if(debug) cout << "++++++++++++++++++++++++++" << endl;

  event.set(h_top_pt,-100);
  event.set(h_top_eta,-100);
  event.set(h_top_phi,-100);

  event.set(h_antitop_pt,-100);
  event.set(h_antitop_eta,-100);
  event.set(h_antitop_phi,-100);

  event.set(h_tops_pt, -100);
  event.set(h_tops_eta, -100);
  event.set(h_tops_phi, -100);

  event.set(h_muon_pt, -100);
  event.set(h_muon_eta, -100);
  event.set(h_muon_phi, -100);

  event.set(h_ele_pt, -100);
  event.set(h_ele_eta, -100);
  event.set(h_ele_phi, -100);

  event.set(h_ttbar_mass, -100);

  event.set(h_lepton_pt, -100);
  event.set(h_lepton_eta,-100);
  event.set(h_lepton_phi,-100);
  
  event.set(h_MET,-100);
  event.set(h_bquark_pt,-100);
  event.set(h_bquark_eta,-100);
  event.set(h_angle_top_antitop,-100);

  event.set(h_motherPdgId,-100);
  event.set(h_topMultiplicity,-100);
  event.set(h_leptonFlavor,-100);

  event.set(h_nonTopMotherJets,-100);
  event.set(h_jetMultiplicity,-100);
  // event.set(h_jets, -100);

  ///beren

    // GenParticle electron, muon, top, antitop, topquarks, wboson, down, up, bottom, charm, strange, gluon, tneutrino, mneutrino, eneutrino;

  GenParticle top, antitop;

  double lepton_pt = 0.0;
  double lepton_eta = 0.0;
  double lepton_phi = 0.0;

  double ele_pt = 0.0;
  double ele_eta = 0.0;
  double ele_phi = 0.0;

  double muon_pt = 0.0;
  double muon_eta = 0.0;
  double muon_phi = 0.0;

  double bquark_pt = 0.0;
  double bquark_eta = 0.0;

  double tops_pt = 0.0;
  double tops_eta = 0.0;
  double tops_phi = 0.0;

  double top_pt = 0.0;
  double top_eta = 0.0;
  double top_phi = 0.0;

  double antitop_pt = 0.0;
  double antitop_eta = 0.0;
  double antitop_phi = 0.0;

  double MET_px = 0.0;
  double MET_py = 0.0;

  int nTops = 0;

  LorentzVector lv_top, lv_antitop;

  std::vector<int> leptonFlavors;

  // if(!htlep_sel->passes(event)) return false; //HT cut

  double HT = 0.0;
  for (const GenJet& genjet : *event.genjets) {
    if (genjet.pt() >= 10.0) {  // 10 GeV pT cut
      HT += genjet.pt();
    }
  }

  if (HT < 500.0) return false;  // HT cut



  for (const GenParticle& gp : *event.genparticles) {

    //top
    if (gp.pdgId() == 6) {
      if(debug) cout << "TOP: " << endl;
      top = gp;
      lv_top = LorentzVector(gp.pt(), gp.eta(), gp.phi(), gp.energy());

      top_pt = gp.pt();
      top_eta = gp.eta();
      top_phi = gp.phi(); 

      event.set(h_top_pt,top_pt);
      event.set(h_top_eta, top_eta);
      event.set(h_top_phi, top_phi);

      if(debug) cout << "Top pt: " << top_pt << endl;
      if(debug) cout << "Top eta: " << top_eta << endl;
      if(debug) cout << "Top phi: " << top_phi << endl;
    }

    //antitop
    if (gp.pdgId() == -6) {
      if(debug) cout << "ANTITOP: " << endl;
      antitop = gp;
      lv_antitop = LorentzVector(gp.pt(), gp.eta(), gp.phi(), gp.energy());

      antitop_pt = gp.pt();
      antitop_eta = gp.eta();
      antitop_phi = gp.phi(); 

      event.set(h_antitop_pt,antitop_pt);
      event.set(h_antitop_eta, antitop_eta);
      event.set(h_antitop_phi, antitop_phi);

      if(debug) cout << "\nAntiTop pt: " << antitop_pt << endl;
      if(debug) cout << "AntiTop eta: " << antitop_eta << endl;
      if(debug) cout << "AntiTop phi: " << antitop_phi << endl;
    }

    if (gp.pdgId() == 6 || gp.pdgId() == -6) {
      nTops++;
      if(debug) cout << "\nTop candidate found with pdgId: " << gp.pdgId() << endl;

      GenParticle const * mother = findMother(gp, event.genparticles);
      if(mother) {
          event.set(h_motherPdgId, mother->pdgId());
          if(debug) cout << "\nMother of top: pdgId " << mother->pdgId() << endl;
      }  
    }

    //tops
    if (abs(gp.pdgId()) == 6) {
      tops_pt = gp.pt();
      tops_eta = gp.eta();
      tops_phi = gp.phi(); 

      event.set(h_tops_pt, tops_pt);
      event.set(h_tops_eta, tops_eta);
      event.set(h_tops_phi, tops_phi);

      // if(debug) cout << "Tops pt: " << tops_pt << endl;
      // if(debug) cout << "Tops eta: " << tops_eta << endl;
      // if(debug) cout << "Tops phi: " << tops_phi << endl;

      vector<GenParticle const *> daughters = findDaughters(gp, event.genparticles);
      // bool hasW = false;
      // bool hasB = false;
      // bool wHasLepton = false;
      for (const GenParticle* daughter : daughters) {
        if(abs(daughter->pdgId()) == 24) {
          // hasW = true;
          if(debug) cout << "\nW boson found with daughters below (above b-quark): " << endl;
            vector<GenParticle const *> wDaughters = findDaughters(*daughter, event.genparticles);
            for (const GenParticle* wDaughter : wDaughters) {
                // if(debug) cout << wDaughter->pdgId() << " ";

                if(abs(wDaughter->pdgId()) == 11 || abs(wDaughter->pdgId()) == 13) {
                    // wHasLepton = true;
                    lepton_pt = wDaughter->pt();
                    lepton_eta = wDaughter->eta();
                    lepton_phi = wDaughter->phi();

                    event.set(h_lepton_pt, lepton_pt);
                    event.set(h_lepton_eta, lepton_eta);
                    event.set(h_lepton_phi, lepton_phi);

                    if(debug) cout << "lepton pt: " << lepton_pt << endl;
                    if(debug) cout << "lepton eta: " << lepton_eta << endl;
                    if(debug) cout << "lepton phi: " << lepton_phi << endl;
                }

                if (abs(wDaughter->pdgId()) == 11) {
                  if(debug)  cout << "\nElectron from W boson decay found with pdgId: " << wDaughter->pdgId() << endl;
                  ele_pt = wDaughter->pt();
                  ele_eta = wDaughter->eta();
                  ele_phi = wDaughter->phi();
                  
                  leptonFlavors.push_back(0); 

                  event.set(h_ele_pt, ele_pt);
                  event.set(h_ele_eta, ele_eta);
                  event.set(h_ele_phi, ele_phi);

                  if(debug) cout << "ele pt: " << ele_pt << endl;
                  if(debug) cout << "ele eta: " << ele_eta << endl;
                  if(debug) cout << "ele phi: " << ele_phi << endl;
                }

                if (abs(wDaughter->pdgId()) == 13) {
                  if(debug)  cout << "\nMuon from W boson decay found with pdgId: " << wDaughter->pdgId() << endl;
                  muon_pt = wDaughter->pt();
                  muon_eta = wDaughter->eta();
                  muon_phi = wDaughter->phi();

                  leptonFlavors.push_back(1); 

                  event.set(h_muon_pt, muon_pt);
                  event.set(h_muon_eta, muon_eta);
                  event.set(h_muon_phi, muon_phi);

                  if(debug) cout << "muon pt: " << muon_pt << endl;
                  if(debug) cout << "muon eta: " << muon_eta << endl;
                  if(debug) cout << "muon phi: " << muon_phi << endl;
                }  
              
            }
        }

        if(abs(daughter->pdgId()) == 5) {
          if (daughter->pt() < 10.0) continue;
          bquark_pt = daughter->pt();
          bquark_eta = daughter->eta();
          event.set(h_bquark_pt, bquark_pt);
          event.set(h_bquark_eta, bquark_eta);
          if(debug)  cout << "\nb-quark found with pdgId: " << daughter->pdgId() << endl;
        }
      } 

      //top bracket
    }

  
    //neutrinos -MET
    if (abs(gp.pdgId()) == 12 || abs(gp.pdgId()) == 14 || abs(gp.pdgId()) == 16) {
      MET_px += gp.v4().px();
      MET_py += gp.v4().py(); 
    }

  }

  if (top.pdgId() == 6 && antitop.pdgId() == -6) {
    double angle = calculateDeltaPhi(top.v4().phi(), antitop.v4().phi());
    event.set(h_angle_top_antitop, angle);

    if(debug) cout << "angle: " << angle << endl;
    
  }

  double MET = sqrt(MET_px * MET_px + MET_py * MET_py);
  if(debug) cout << "MET: " << MET << endl;
  event.set(h_MET ,MET);
  
  if(debug) cout << " \ntop multiplicity: " << nTops << endl;
  event.set(h_topMultiplicity, nTops);

  if (lv_top != LorentzVector() && lv_antitop != LorentzVector()) { 
    LorentzVector lv_ttbar = lv_top + lv_antitop;
    double ttbar_mass = lv_ttbar.M();
    event.set(h_ttbar_mass, ttbar_mass);

    cout << " \ninvariant mass 1: " << ttbar_mass << endl;

  }

  for (int leptonFlavor : leptonFlavors) {
    event.set(h_leptonFlavor, leptonFlavor);
  } 


//// END OF GEN PARTICLES///


/// BEGINNING OF GEN JETS ///

// Based on the class definition in /UHH2/common/include/GenJet.h, GenJet object keeps track of the indices of its constituent GenParticle objects via the m_genparticles_indices member

// first retrieved the GenJet collection from the event.
//  then loop over each jet in the collection.
// For each jet, I retrieve the indices of its constituents.
//  then loop over these indices, getting the corresponding GenParticle object for each index.
// For each constituent particle, I use the findMother function to get its mother particle.
// If the mother particle is not a top quark, count it and exit the inner loop.

// int nNonTopMotherJets = 0;

// for (const GenJet& genjet : *event.genjets) {
//   GenJet const * mother = findMother(genjet, event.genjets);
//   if(mother && abs(mother->pdgId()) != 6) {
//     nNonTopMotherJets++;
//   }
// }

int nJets = event.genjets->size();
if(debug) cout << "Jet: " << nJets << endl;
event.set(h_jetMultiplicity, nJets);
// event.set(h_nonTopMotherJets, nNonTopMotherJets);
// if(debug) cout << "\nJet: " << nNonTopMotherJets << endl;




//// beren

 
  fill_histograms(event, "Input");


  bool commonResult = common->process(event);
  if (!commonResult) return false;
  // if(debug) cout << "CommonModules: ok" << endl;
  // fill_histograms(event, "CommonModules");

  sort_by_pt<Muon>(*event.muons);
  sort_by_pt<Electron>(*event.electrons);

  // Correct AK4 CHS jets
  CHSjetCorr->process(event);

  if(isHOTVR){
    hotvrjetCorr->process(event);
    // fill_histograms(event, "HOTVRCorrections");
  }

  toppuppijetCorr->process(event);
  // if(debug) cout << "TopPuppiJetCorrections: ok" << endl;
  // fill_histograms(event, "PUPPICorrections");


  // GEN ME quark-flavor selection
  if(!event.isRealData){
    if(!genflavor_sel->passes(event)) return false;
  }
  // if(debug) cout << "GenFlavorSelection: ok" << endl;

  // cout << "event.muons->size(): " << event.muons->size() << endl;
  // cout << "event.electrons->size(): " << event.electrons->size() << endl;
  const bool pass_lep1 = ((event.muons->size() >= 1) || (event.electrons->size() >= 1));
  // cout << "pass_lep1: " << pass_lep1 << endl;
  if(!pass_lep1) return false;
  // if(debug) cout << "≥1 leptons: ok" << endl;
  // fill_histograms(event, "Lepton1");

  jet_IDcleaner->process(event);
  // fill_histograms(event, "JetID");
  // if(debug) cout << "JetCleaner ID: ok" << endl;

  jet_cleaner1->process(event);
  sort_by_pt<Jet>(*event.jets);
  // fill_histograms(event, "JetCleaner1");
  // if(debug) cout << "JetCleaner1: ok" << endl;

  // Lepton-2Dcut variables
  for(auto& muo : *event.muons){
    float    dRmin, pTrel;
    std::tie(dRmin, pTrel) = drmin_pTrel(muo, *event.jets);

    muo.set_tag(Muon::twodcut_dRmin, dRmin);
    muo.set_tag(Muon::twodcut_pTrel, pTrel);
  }

  for(auto& ele : *event.electrons){
    float    dRmin, pTrel;
    std::tie(dRmin, pTrel) = drmin_pTrel(ele, *event.jets);

    ele.set_tag(Electron::twodcut_dRmin, dRmin);
    ele.set_tag(Electron::twodcut_pTrel, pTrel);
  }


  jet_cleaner2->process(event);
  sort_by_pt<Jet>(*event.jets);
  // fill_histograms(event, "JetCleaner2");
  // if(debug) cout << "JetCleaner2: ok" << endl;

  hotvrjet_cleaner->process(event);
  sort_by_pt<TopJet>(*event.topjets);

  topjet_puppi_IDcleaner->process(event);
  topjet_puppi_cleaner->process(event);
  sort_by_pt<TopJet>(*event.toppuppijets);

  // fill_histograms(event, "TopjetCleaner");
  // if(debug) cout << "TopJetCleaner: ok" << endl;

  // 1st AK4 jet selection
  const bool pass_jet1 = jet1_sel->passes(event);
  if(!pass_jet1) return false;
  // if(debug) cout << "NJetSelection1: ok" << endl;
  // fill_histograms(event, "Jet1");

  // 2nd AK4 jet selection
  const bool pass_jet2 = jet2_sel->passes(event);
  if(!pass_jet2) return false;
  // if(debug) cout << "NJetSelection2: ok" << endl;
  // fill_histograms(event, "Jet2");

  // MET selection
  const bool pass_met = met_sel->passes(event);
  if(!pass_met) return false;
  // if(debug) cout << "METCut: ok" << endl;
  // fill_histograms(event, "MET");

  return true;

}

UHH2_REGISTER_ANALYSIS_MODULE(ZprimePreselectionModule_gen)