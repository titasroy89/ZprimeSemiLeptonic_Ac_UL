#include <iostream>
#include <iostream>
#include <memory>

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

#include <UHH2/ZprimeSemiLeptonic/include/ModuleBASE.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicSelections.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicPreselectionHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicGeneratorHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/CHSJetCorrections.h>
#include <UHH2/ZprimeSemiLeptonic/include/TopPuppiJetCorrections.h>
#include "UHH2/HOTVR/include/HOTVRJetCorrectionModule.h"

using namespace std;
using namespace uhh2;

class ZprimePreselectionModule_dY : public ModuleBASE {

public:
  explicit ZprimePreselectionModule_dY(uhh2::Context&);
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

  Event::Handle<float> h_DeltaY_gen_ele; //-beren 
  Event::Handle<float> h_DeltaY_gen_muon; //-beren 
  Event::Handle<float> h_DeltaY_gen_mass; //-beren

  Event::Handle<float> h_DeltaY_N_gen_ele; //-beren
  Event::Handle<float> h_DeltaY_N_gen_muon; //-beren
  Event::Handle<float> h_DeltaY_N_gen_pt_ele; //-beren
  Event::Handle<float> h_DeltaY_N_gen_pt_muon; //-beren
  Event::Handle<float> h_DeltaY_N_gen_eta_ele; //-beren
  Event::Handle<float> h_DeltaY_N_gen_eta_muon; //-beren
  Event::Handle<float> h_DeltaY_N_gen_2d_ele; //-beren
  Event::Handle<float> h_DeltaY_N_gen_2d_muon; //-beren
  Event::Handle<float> h_DeltaY_N_gen_met_ele; //-beren
  Event::Handle<float> h_DeltaY_N_gen_met_muon; //-beren

  Event::Handle<float> h_DeltaY_P_gen_ele; //-beren
  Event::Handle<float> h_DeltaY_P_gen_muon; //-beren
  Event::Handle<float> h_DeltaY_P_gen_pt_ele; //-beren
  Event::Handle<float> h_DeltaY_P_gen_pt_muon; //-beren
  Event::Handle<float> h_DeltaY_P_gen_eta_ele; //-beren
  Event::Handle<float> h_DeltaY_P_gen_eta_muon; //-beren
  Event::Handle<float> h_DeltaY_P_gen_2d_ele; //-beren
  Event::Handle<float> h_DeltaY_P_gen_2d_muon; //-beren
  Event::Handle<float> h_DeltaY_P_gen_met_ele; //-beren
  Event::Handle<float> h_DeltaY_P_gen_met_muon; //-beren

  Event::Handle<float> h_DeltaY_N_gen_jet_pt_ele; //-beren
  Event::Handle<float> h_DeltaY_P_gen_jet_pt_ele; //-beren
  Event::Handle<float> h_DeltaY_N_gen_jet_pt_muon; //-beren
  Event::Handle<float> h_DeltaY_P_gen_jet_pt_muon; //-beren
  Event::Handle<float> h_DeltaY_N_gen_jet_eta_ele; //-beren
  Event::Handle<float> h_DeltaY_P_gen_jet_eta_ele; //-beren
  Event::Handle<float> h_DeltaY_N_gen_jet_eta_muon; //-beren
  Event::Handle<float> h_DeltaY_P_gen_jet_eta_muon; //-beren

  


  bool isMC, isHOTVR;
  string Sys_PU;

  std::unique_ptr<Hists> lumihists;
  TString METcollection;

  bool isUL16preVFP, isUL16postVFP, isUL17, isUL18;

  // additional branch with AK4 CHS jets -> for b-tagging
  Event::Handle<vector<Jet>> h_CHSjets;
  // Event::Handle<vector<Particle>> h_mygenjets;


  //DeltaY variable to save them to tree
  Event::Handle<float> h_DeltaY; //-beren
  Event::Handle<float> h_DeltaY_N; //-beren
  Event::Handle<float> h_DeltaY_P; //-beren

};


void ZprimePreselectionModule_dY::book_histograms(uhh2::Context& ctx, vector<string> tags){
  for(const auto & tag : tags){
    string mytag = tag+"_General";
    book_HFolder(mytag, new ZprimeSemiLeptonicPreselectionHists(ctx,mytag));
  }
}

void ZprimePreselectionModule_dY::fill_histograms(uhh2::Event& event, string tag){
  string mytag = tag+"_General";
  HFolder(mytag)->fill(event);
}



ZprimePreselectionModule_dY::ZprimePreselectionModule_dY(uhh2::Context& ctx){
    
  debug = false;

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

  //DeltaY variables
  h_DeltaY_gen_ele = ctx.declare_event_output<float> ("DeltaY_gen_ele"); //-beren DeltaY 
  h_DeltaY_gen_muon = ctx.declare_event_output<float> ("DeltaY_gen_muon"); //-beren DeltaY 

  h_DeltaY_N_gen_ele = ctx.declare_event_output<float> ("DeltaY_N_gen_ele"); //-beren DeltaY
  h_DeltaY_N_gen_muon = ctx.declare_event_output<float> ("DeltaY_N_gen_muon"); //-beren DeltaY
  h_DeltaY_N_gen_pt_ele = ctx.declare_event_output<float> ("DeltaY_N_gen_pt_ele"); //-beren DeltaY
  h_DeltaY_N_gen_pt_muon = ctx.declare_event_output<float> ("DeltaY_N_gen_pt_muon"); //-beren DeltaY
  h_DeltaY_N_gen_eta_ele = ctx.declare_event_output<float> ("DeltaY_N_gen_eta_ele"); //-beren DeltaY
  h_DeltaY_N_gen_eta_muon = ctx.declare_event_output<float> ("DeltaY_N_gen_eta_muon"); //-beren DeltaY
  h_DeltaY_N_gen_2d_ele = ctx.declare_event_output<float> ("DeltaY_N_gen_2d_ele"); //-beren DeltaY
  h_DeltaY_N_gen_2d_muon = ctx.declare_event_output<float> ("DeltaY_N_gen_2d_muon"); //-beren DeltaY
  h_DeltaY_N_gen_met_ele = ctx.declare_event_output<float> ("DeltaY_N_gen_met_ele"); //-beren DeltaY
  h_DeltaY_N_gen_met_muon = ctx.declare_event_output<float> ("DeltaY_N_gen_met_muon"); //-beren DeltaY

  h_DeltaY_P_gen_ele = ctx.declare_event_output<float> ("DeltaY_P_gen_ele"); //-beren DeltaY
  h_DeltaY_P_gen_muon = ctx.declare_event_output<float> ("DeltaY_P_gen_muon"); //-beren DeltaY
  h_DeltaY_P_gen_pt_ele = ctx.declare_event_output<float> ("DeltaY_P_gen_pt_ele"); //-beren DeltaY
  h_DeltaY_P_gen_pt_muon = ctx.declare_event_output<float> ("DeltaY_P_gen_pt_muon"); //-beren DeltaY
  h_DeltaY_P_gen_eta_ele = ctx.declare_event_output<float> ("DeltaY_P_gen_eta_ele"); //-beren DeltaY
  h_DeltaY_P_gen_eta_muon = ctx.declare_event_output<float> ("DeltaY_P_gen_eta_muon"); //-beren DeltaY
  
  h_DeltaY_P_gen_2d_ele = ctx.declare_event_output<float> ("DeltaY_P_gen_2d_ele"); //-beren DeltaY
  h_DeltaY_P_gen_2d_muon = ctx.declare_event_output<float> ("DeltaY_P_gen_2d_muon"); //-beren DeltaY
  h_DeltaY_P_gen_met_ele = ctx.declare_event_output<float> ("DeltaY_P_gen_met_ele"); //-beren DeltaY
  h_DeltaY_P_gen_met_muon = ctx.declare_event_output<float> ("DeltaY_P_gen_met_muon"); //-beren DeltaY

  h_DeltaY_N_gen_jet_pt_ele = ctx.declare_event_output<float> ("DeltaY_N_gen_jet_pt_ele"); //-beren DeltaY
  h_DeltaY_P_gen_jet_pt_ele = ctx.declare_event_output<float> ("DeltaY_P_gen_jet_pt_ele"); //-beren DeltaY
  h_DeltaY_N_gen_jet_pt_muon = ctx.declare_event_output<float> ("DeltaY_N_gen_jet_pt_muon"); //-beren DeltaY
  h_DeltaY_P_gen_jet_pt_muon = ctx.declare_event_output<float> ("DeltaY_P_gen_jet_pt_muon"); //-beren DeltaY

  h_DeltaY_N_gen_jet_eta_ele = ctx.declare_event_output<float> ("DeltaY_N_gen_jet_eta_ele"); //-beren DeltaY
  h_DeltaY_P_gen_jet_eta_ele = ctx.declare_event_output<float> ("DeltaY_P_gen_jet_eta_ele"); //-beren DeltaY
  h_DeltaY_N_gen_jet_eta_muon = ctx.declare_event_output<float> ("DeltaY_N_gen_jet_eta_muon"); //-beren DeltaY
  h_DeltaY_P_gen_jet_eta_muon = ctx.declare_event_output<float> ("DeltaY_P_gen_jet_eta_muon"); //-beren DeltaY


  // h_mygenjets = ctx.declare_event_output<vector<Particle>>("mygenjets");


  // Book histograms
  vector<string> histogram_tags = {"Input", "Gen_N", "Gen_P",

  "Ele_gen_N_0_250","Ele_N_Pt_0_250","Ele_N_Pt_Eta_0_250","Ele_N_JetPt_0_250","Ele_N_JetPt_Eta_0_250","Ele_gen_N_250_500","Ele_N_Pt_250_500","Ele_N_Pt_Eta_250_500","Ele_N_JetPt_250_500","Ele_N_JetPt_Eta_250_500", "Ele_gen_N_500_750","Ele_N_Pt_500_750","Ele_N_Pt_Eta_500_750","Ele_N_JetPt_500_750","Ele_N_JetPt_Eta_500_750","Ele_gen_N_750_900","Ele_N_Pt_750_900","Ele_N_Pt_Eta_750_900","Ele_N_JetPt_750_900","Ele_N_JetPt_Eta_750_900","Ele_gen_N_900Inf","Ele_N_Pt_900Inf","Ele_N_Pt_Eta_900Inf","Ele_N_JetPt_900Inf","Ele_N_JetPt_Eta_900Inf", 
  "Ele_gen_P_0_250","Ele_P_Pt_0_250","Ele_P_Pt_Eta_0_250","Ele_P_JetPt_0_250","Ele_P_JetPt_Eta_0_250","Ele_gen_P_250_500","Ele_P_Pt_250_500","Ele_P_Pt_Eta_250_500","Ele_P_JetPt_250_500","Ele_P_JetPt_Eta_250_500", "Ele_gen_P_500_750","Ele_P_Pt_500_750","Ele_P_Pt_Eta_500_750","Ele_P_JetPt_500_750","Ele_P_JetPt_Eta_500_750","Ele_gen_P_750_900","Ele_P_Pt_750_900","Ele_P_Pt_Eta_750_900","Ele_P_JetPt_750_900","Ele_P_JetPt_Eta_750_900","Ele_gen_P_900Inf","Ele_P_Pt_900Inf","Ele_P_Pt_Eta_900Inf","Ele_P_JetPt_900Inf","Ele_P_JetPt_Eta_900Inf", 
  "muon_gen_N_0_250","muon_N_Pt_0_250","muon_N_Pt_Eta_0_250","muon_N_JetPt_0_250","muon_N_JetPt_Eta_0_250","muon_gen_N_250_500","muon_N_Pt_250_500","muon_N_Pt_Eta_250_500","muon_N_JetPt_250_500","muon_N_JetPt_Eta_250_500", "muon_gen_N_500_750","muon_N_Pt_500_750","muon_N_Pt_Eta_500_750","muon_N_JetPt_500_750","muon_N_JetPt_Eta_500_750","muon_gen_N_750_900","muon_N_Pt_750_900","muon_N_Pt_Eta_750_900","muon_N_JetPt_750_900","muon_N_JetPt_Eta_750_900","muon_gen_N_900Inf","muon_N_Pt_900Inf","muon_N_Pt_Eta_900Inf","muon_N_JetPt_900Inf","muon_N_JetPt_Eta_900Inf", 
  "muon_gen_P_0_250","muon_P_Pt_0_250","muon_P_Pt_Eta_0_250","muon_P_JetPt_0_250","muon_P_JetPt_Eta_0_250","muon_gen_P_250_500","muon_P_Pt_250_500","muon_P_Pt_Eta_250_500","muon_P_JetPt_250_500","muon_P_JetPt_Eta_250_500", "muon_gen_P_500_750","muon_P_Pt_500_750","muon_P_Pt_Eta_500_750","muon_P_JetPt_500_750","muon_P_JetPt_Eta_500_750","muon_gen_P_750_900","muon_P_Pt_750_900","muon_P_Pt_Eta_750_900","muon_P_JetPt_750_900","muon_P_JetPt_Eta_750_900","muon_gen_P_900Inf","muon_P_Pt_900Inf","muon_P_Pt_Eta_900Inf","muon_P_JetPt_900Inf","muon_P_JetPt_Eta_900Inf", 
  
  "DeltaY_gen", "CommonModules", "HOTVRCorrections", "PUPPICorrections", "Lepton1", "JetID", "JetCleaner1", "JetCleaner2", "TopjetCleaner", "Jet1", "Jet2", "MET",
  
  "DY_0_500", "DY_500_750", "DY_750_1000", "DY_1000_1500", "DY_1500Inf"
  };
  
  book_histograms(ctx, histogram_tags);

  lumihists.reset(new LuminosityHists(ctx, "lumi"));
}


bool ZprimePreselectionModule_dY::process(uhh2::Event& event){

  if(debug) cout << "++++++++++++ NEW EVENT ++++++++++++++" << endl;
  if(debug) cout << " run.event: " << event.run << ". " << event.event << endl;

  event.set(h_DeltaY_gen_ele,-100); //-beren
  event.set(h_DeltaY_gen_muon,-100); //-beren
  event.set(h_DeltaY_N_gen_ele,-100); //-beren
  event.set(h_DeltaY_N_gen_muon,-100); //-beren
  event.set(h_DeltaY_N_gen_pt_ele,-100); //-beren
  event.set(h_DeltaY_N_gen_pt_muon,-100); //-beren
  event.set(h_DeltaY_N_gen_eta_ele,-100); //-beren
  event.set(h_DeltaY_N_gen_eta_muon,-100); //-beren
  event.set(h_DeltaY_N_gen_2d_ele,-100); //-beren
  event.set(h_DeltaY_N_gen_2d_muon,-100); //-beren
  event.set(h_DeltaY_N_gen_met_ele,-100); //-beren
  event.set(h_DeltaY_N_gen_met_muon,-100); //-beren

  event.set(h_DeltaY_P_gen_ele,-100); //-beren
  event.set(h_DeltaY_P_gen_muon,-100); //-beren
  event.set(h_DeltaY_P_gen_pt_ele,-100); //-beren
  event.set(h_DeltaY_P_gen_pt_muon,-100); //-beren
  event.set(h_DeltaY_P_gen_eta_ele,-100); //-beren
  event.set(h_DeltaY_P_gen_eta_muon,-100); //-beren
  event.set(h_DeltaY_P_gen_2d_ele,-100); //-beren
  event.set(h_DeltaY_P_gen_2d_muon,-100); //-beren
  event.set(h_DeltaY_P_gen_met_ele,-100); //-beren
  event.set(h_DeltaY_P_gen_met_muon,-100); //-beren

  event.set(h_DeltaY_N_gen_jet_pt_ele,-100); //-beren
  event.set(h_DeltaY_P_gen_jet_pt_ele,-100); //-beren
  event.set(h_DeltaY_N_gen_jet_pt_muon,-100); //-beren
  event.set(h_DeltaY_P_gen_jet_pt_muon,-100); //-beren

  event.set(h_DeltaY_N_gen_jet_eta_ele,-100); //-beren
  event.set(h_DeltaY_P_gen_jet_eta_ele,-100); //-beren
  event.set(h_DeltaY_N_gen_jet_eta_muon,-100); //-beren
  event.set(h_DeltaY_P_gen_jet_eta_muon,-100); //-beren

  fill_histograms(event, "Input");
  if(debug) cout << "1" << endl;

  //-beren

 GenParticle electron, antielectron, muon, antimuon, top, antitop;

  for (const GenParticle& gp : *event.genparticles) {
      if (gp.pdgId() == 11) {
        electron = gp;
      }
      else if (gp.pdgId() == -11) {
        antielectron = gp;
      }
      else if (gp.pdgId() == 13) {
        muon = gp;
      }
      else if (gp.pdgId() == -13) {
        antimuon = gp;
      }
      else if(gp.pdgId() == 6){
        top = gp;
      }
      else if(gp.pdgId() == -6){
        antitop = gp;
    }
  }


  
  double_t pt_ele = electron.pt();
  double_t pt_muon = muon.pt();
  double_t eta_ele = electron.eta();
  double_t eta_muon = muon.eta();
  if(debug) cout << "3" << endl;

  // double_t DeltaY_gen_ele = TMath::Abs(0.5*TMath::Log((electron.energy() + electron.pt()*TMath::SinH(electron.eta()))/(electron.energy() - electron.pt()*TMath::SinH(electron.eta())))) - TMath::Abs(0.5*TMath::Log((antielectron.energy() + antielectron.pt()*TMath::SinH(antielectron.eta()))/(antielectron.energy() - antielectron.pt()*TMath::SinH(antielectron.eta()))));
  // double_t DeltaY_gen_muon= TMath::Abs(0.5*TMath::Log((muon.energy() + muon.pt()*TMath::SinH(muon.eta()))/(muon.energy() - muon.pt()*TMath::SinH(muon.eta())))) - TMath::Abs(0.5*TMath::Log((antimuon.energy() + antimuon.pt()*TMath::SinH(antimuon.eta()))/(antimuon.energy() - antimuon.pt()*TMath::SinH(antimuon.eta()))));
  
  float m_ttbar = inv_mass(top.v4() + antitop.v4());

  double_t DeltaY_gen= TMath::Abs(0.5*TMath::Log((top.energy() + top.pt()*TMath::SinH(top.eta()))/(top.energy() - top.pt()*TMath::SinH(top.eta())))) - TMath::Abs(0.5*TMath::Log((antitop.energy() + antitop.pt()*TMath::SinH(antitop.eta()))/(antitop.energy() - antitop.pt()*TMath::SinH(antitop.eta()))));



  if((DeltaY_gen < 0)) {
    fill_histograms(event, "Gen_N");
  }
  
  if((DeltaY_gen > 0)) {
    fill_histograms(event, "Gen_P");
  }


//////////////////////////////////////
 /////////////////////////////////////
 ////////        ELECTRON   
 //////////////////////////////////////
 /////////////////////////////////////

  // 0 <mtt <250 Negative
  if(m_ttbar>0 && m_ttbar<250 && DeltaY_gen < 0){
    fill_histograms(event, "Ele_gen_N_0_250");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_0_250");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_Eta_0_250");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_0_250");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_Eta_0_250");

    
    }
  }

  // 0 <mtt <250 Positive
  if(m_ttbar>0 && m_ttbar<250 && DeltaY_gen > 0){
    fill_histograms(event, "Ele_gen_P_0_250");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_0_250");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_Eta_0_250");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_0_250");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_Eta_0_250");

    
    }
  }

   // 250 <mtt <500 Negative
  if(m_ttbar>250 && m_ttbar<500 && DeltaY_gen < 0){
    fill_histograms(event, "Ele_gen_N_250_500");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_250_500");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_Eta_250_500");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_250_500");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_Eta_250_500");

    
    }
  }

  // 250 <mtt <500 Positive
  if(m_ttbar>250 && m_ttbar<500 && DeltaY_gen > 0){
    fill_histograms(event, "Ele_gen_P_250_500");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_250_500");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_Eta_250_500");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_250_500");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_Eta_250_500");

    
    }
  }

  /// -----

  // 500 <mtt < 750 Negative
  if(m_ttbar>500 && m_ttbar<750 && DeltaY_gen < 0){
    fill_histograms(event, "Ele_gen_N_500_750");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_500_750");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_Eta_500_750");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_500_750");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_Eta_500_750");

    
    }
  }

  // 500 <mtt < 750 Positive
  if(m_ttbar>500 && m_ttbar<750 && DeltaY_gen > 0){
    fill_histograms(event, "Ele_gen_P_500_750");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_500_750");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_Eta_500_750");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_500_750");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_Eta_500_750");

    
    }
  }

  // -----



  // 750 <mtt < 900 Negative
  if(m_ttbar>750 && m_ttbar<900 && DeltaY_gen < 0){
    fill_histograms(event, "Ele_gen_N_750_900");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_750_900");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_Eta_750_900");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_750_900");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_Eta_750_900");

    
    }
  }

  // 750 <mtt < 900 Positive
  if(m_ttbar>750 && m_ttbar<900 && DeltaY_gen > 0){
    fill_histograms(event, "Ele_gen_P_750_900");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_750_900");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_Eta_750_900");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_750_900");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_Eta_750_900");

    
    }
  }



  //--- 
  
  // 900 <mtt  Negative
  if(m_ttbar>900 && DeltaY_gen < 0){
    fill_histograms(event, "Ele_gen_N_900Inf");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_900Inf");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_N_Pt_Eta_900Inf");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_900Inf");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_N_JetPt_Eta_900Inf");

    
    }
  }

  // 900 <mtt Positive
  if(m_ttbar>900 && DeltaY_gen > 0){
    fill_histograms(event, "Ele_gen_P_900Inf");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_ele > 35)){
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_900Inf");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_ele > 35 && TMath::Abs(eta_ele) < 2.5)) {
        return false;
      }
      fill_histograms(event, "Ele_P_Pt_Eta_900Inf");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_900Inf");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_ele > 35 && (TMath::Abs(eta_ele) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "Ele_P_JetPt_Eta_900Inf");

    
    }
  }
  //////////////////////////////////////
 /////////////////////////////////////
 ////////          END OF ELECTRON   
 //////////////////////////////////////
 /////////////////////////////////////

    
 //////////////////////////////////////
 /////////////////////////////////////
 ////////              MUON
 //////////////////////////////////////
 /////////////////////////////////////



 // 0 <mtt <250 Negative
  if(m_ttbar>0 && m_ttbar<250 && DeltaY_gen < 0){
    fill_histograms(event, "muon_gen_N_0_250");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_N_Pt_0_250");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_N_Pt_Eta_0_250");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_0_250");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_Eta_0_250");

    
    }
  }

  // 0 <mtt <250 Positive
  if(m_ttbar>0 && m_ttbar<250 && DeltaY_gen > 0){
    fill_histograms(event, "muon_gen_P_0_250");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_P_Pt_0_250");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_P_Pt_Eta_0_250");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_0_250");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_Eta_0_250");

    
    }
  }

   // 250 <mtt <500 Negative
  if(m_ttbar>250 && m_ttbar<500 && DeltaY_gen < 0){
    fill_histograms(event, "muon_gen_N_250_500");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_N_Pt_250_500");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_N_Pt_Eta_250_500");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_250_500");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_Eta_250_500");

    
    }
  }

  // 250 <mtt <500 Positive
  if(m_ttbar>250 && m_ttbar<500 && DeltaY_gen > 0){
    fill_histograms(event, "muon_gen_P_250_500");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_P_Pt_250_500");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_P_Pt_Eta_250_500");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_250_500");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_Eta_250_500");

    
    }
  }

  /// -----

  // 500 <mtt < 750 Negative
  if(m_ttbar>500 && m_ttbar<750 && DeltaY_gen < 0){
    fill_histograms(event, "muon_gen_N_500_750");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_N_Pt_500_750");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_N_Pt_Eta_500_750");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_500_750");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_Eta_500_750");

    
    }
  }

  // 500 <mtt < 750 Positive
  if(m_ttbar>500 && m_ttbar<750 && DeltaY_gen > 0){
    fill_histograms(event, "muon_gen_P_500_750");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_P_Pt_500_750");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_P_Pt_Eta_500_750");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_500_750");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_Eta_500_750");

    
    }
  }

  // -----



  // 750 <mtt < 900 Negative
  if(m_ttbar>750 && m_ttbar<900 && DeltaY_gen < 0){
    fill_histograms(event, "muon_gen_N_750_900");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_N_Pt_750_900");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_N_Pt_Eta_750_900");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_750_900");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_Eta_750_900");

    
    }
  }

  // 750 <mtt < 900 Positive
  if(m_ttbar>750 && m_ttbar<900 && DeltaY_gen > 0){
    fill_histograms(event, "muon_gen_P_750_900");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_P_Pt_750_900");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_P_Pt_Eta_750_900");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_750_900");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_Eta_750_900");

    
    }
  }



  //--- 
  
  // 900 <mtt  Negative
  if(m_ttbar>900 && DeltaY_gen < 0){
    fill_histograms(event, "muon_gen_N_900Inf");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen< 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_N_Pt_900Inf");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen< 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_N_Pt_Eta_900Inf");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_900Inf");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen<0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_N_JetPt_Eta_900Inf");

    
    }
  }

  // 900 <mtt Positive
  if(m_ttbar>900 && DeltaY_gen > 0){
    fill_histograms(event, "muon_gen_P_900Inf");
  
    //pt & eta & jet_pt cut
    for (const auto gj : *event.genjets) {

      double_t jet_pt = gj.pt();
      double_t jet_eta = gj.eta();
    
      // Apply pt cuts and plot  //1
      if (!(DeltaY_gen> 0 && pt_muon > 30)){
        return false;
      }
      fill_histograms(event, "muon_P_Pt_900Inf");

      // Apply pt and eta cuts and plot 
      if(!(DeltaY_gen > 0 && pt_muon > 30 && TMath::Abs(eta_muon) < 2.5)) {
        return false;
      }
      fill_histograms(event, "muon_P_Pt_Eta_900Inf");

      // pt & eta & jet_pt cut   
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt > 40))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_900Inf");


    // pt & eta & jet_pt eta cut
      if(!(DeltaY_gen > 0 && pt_muon > 30 && (TMath::Abs(eta_muon) < 2.5) && (jet_pt >40) && (TMath::Abs(jet_eta) < 2.5))){
        return false;
      }
      fill_histograms(event, "muon_P_JetPt_Eta_900Inf");

    
    }
  }



  //////////////////////////////////////
 /////////////////////////////////////
 ////////             END OF mUON
 //////////////////////////////////////
 /////////////////////////////////////
  fill_histograms(event, "DeltaY_gen");

  //beren
  if(debug) cout << "7" << endl;

  bool commonResult = common->process(event);
  if (!commonResult) return false;
  if(debug) cout << "CommonModules: ok" << endl;
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
  if(debug) cout << "TopPuppiJetCorrections: ok" << endl;
  // fill_histograms(event, "PUPPICorrections");


  // GEN ME quark-flavor selection
  if(!event.isRealData){
    if(!genflavor_sel->passes(event)) return false;
  }
  if(debug) cout << "GenFlavorSelection: ok" << endl;

  // cout << "event.muons->size(): " << event.muons->size() << endl;
  // cout << "event.electrons->size(): " << event.electrons->size() << endl;
  const bool pass_lep1 = ((event.muons->size() >= 1) || (event.electrons->size() >= 1));
  // cout << "pass_lep1: " << pass_lep1 << endl;
  if(!pass_lep1) return false;
  if(debug) cout << "≥1 leptons: ok" << endl;
  // fill_histograms(event, "Lepton1");

  jet_IDcleaner->process(event);
  // fill_histograms(event, "JetID");
  if(debug) cout << "JetCleaner ID: ok" << endl;

  jet_cleaner1->process(event);
  sort_by_pt<Jet>(*event.jets);
  // fill_histograms(event, "JetCleaner1");
  if(debug) cout << "JetCleaner1: ok" << endl;

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
  if(debug) cout << "JetCleaner2: ok" << endl;

  hotvrjet_cleaner->process(event);
  sort_by_pt<TopJet>(*event.topjets);

  topjet_puppi_IDcleaner->process(event);
  topjet_puppi_cleaner->process(event);
  sort_by_pt<TopJet>(*event.toppuppijets);

  // fill_histograms(event, "TopjetCleaner");
  if(debug) cout << "TopJetCleaner: ok" << endl;

  // 1st AK4 jet selection
  const bool pass_jet1 = jet1_sel->passes(event);
  if(!pass_jet1) return false;
  if(debug) cout << "NJetSelection1: ok" << endl;
  // fill_histograms(event, "Jet1");

  // 2nd AK4 jet selection
  const bool pass_jet2 = jet2_sel->passes(event);
  if(!pass_jet2) return false;
  if(debug) cout << "NJetSelection2: ok" << endl;
  // fill_histograms(event, "Jet2");

  // MET selection
  const bool pass_met = met_sel->passes(event);
  if(!pass_met) return false;
  if(debug) cout << "METCut: ok" << endl;
  // fill_histograms(event, "MET");

  if(m_ttbar>=0 &&  m_ttbar<500){
    fill_histograms(event, "DY_0_500");
  }

  if(m_ttbar>=500 &&  m_ttbar<750){
    fill_histograms(event, "DY_500_750");
  }

  if(m_ttbar>=750 &&  m_ttbar<1000){
    fill_histograms(event, "DY_750_1000");
  }

  if(m_ttbar>=1000 &&  m_ttbar<1500){
    fill_histograms(event, "DY_1000_1500");
  }

  if(m_ttbar>=1500){
    fill_histograms(event, "DY_1500Inf");
  }

  return true;
}

UHH2_REGISTER_ANALYSIS_MODULE(ZprimePreselectionModule_dY)