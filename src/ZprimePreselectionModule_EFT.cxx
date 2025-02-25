#include <iostream>
#include <memory>
#include <map>
#include <fstream>

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

class ZprimePreselectionModule_EFT : public ModuleBASE {

public:
  explicit ZprimePreselectionModule_EFT(uhh2::Context&);
  virtual bool process(uhh2::Event&) override;
  void book_histograms(uhh2::Context&, vector<string>);
  void fill_histograms(uhh2::Event&, string);

protected:
  bool debug;

  // Weight ID mapping
  std::map<int, std::string> weight_id_map;
  void load_weight_ids(const std::string& filename);

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
  unique_ptr<Selection> SignSplit;

  bool isMC, isHOTVR;
  string Sys_PU;

  std::unique_ptr<Hists> lumihists;
  TString METcollection;

  bool isUL16preVFP, isUL16postVFP, isUL17, isUL18;
  bool isEFT;  // Flag for EFT samples

  // Output handles for EFT weights
  std::vector<Event::Handle<float>> h_eft_weights;  // Vector of handles for each EFT weight
  Event::Handle<int> h_n_eft_weights;  // Handle for number of weights
  Event::Handle<float> h_ref_point_weight;  // Handle for reference point weight (systweights[0])

  // additional branch with AK4 CHS jets -> for b-tagging
  Event::Handle<vector<Jet>> h_CHSjets;

};

void ZprimePreselectionModule_EFT::book_histograms(uhh2::Context& ctx, vector<string> tags){
  for(const auto & tag : tags){
    string mytag = tag+"_General";
    book_HFolder(mytag, new ZprimeSemiLeptonicPreselectionHists(ctx,mytag));
  }
}

void ZprimePreselectionModule_EFT::fill_histograms(uhh2::Event& event, string tag){
  string mytag = tag+"_General";
  HFolder(mytag)->fill(event);
}

void ZprimePreselectionModule_EFT::load_weight_ids(const std::string& filename) {
    std::ifstream file(filename);
    std::string line;
    int index = 0;
    
    while(std::getline(file, line)) {
        // Skip empty lines
        if(line.empty()) continue;
        
        // Check if line contains "Weight ID:"
        if(line.find("Weight ID:") != std::string::npos) {
            // Extract the weight ID (between "Weight ID:" and ", Weight value:")
            size_t start = line.find("Weight ID:") + 10;  // +10 to skip "Weight ID:"
            size_t end = line.find(", Weight value:");
            
            if(end != std::string::npos) {
                std::string weight_id = line.substr(start, end - start);
                // Trim whitespace
                weight_id.erase(0, weight_id.find_first_not_of(" \t"));
                weight_id.erase(weight_id.find_last_not_of(" \t") + 1);
                
                // Add to both maps
                weight_id_map[index] = weight_id;
                index++;
            }
        }
    }

    // Print first few mappings for verification
    cout << "\nWeight ID Mapping (first 5 entries):\n";
    for(int i = 0; i < 5; i++) {
        if(weight_id_map.find(i) != weight_id_map.end()) {
            cout << "Index " << i << ":\n  " << weight_id_map[i] << "\n";
        }
    }
    cout << "Total weights mapped: " << weight_id_map.size() << "\n";
}

ZprimePreselectionModule_EFT::ZprimePreselectionModule_EFT(uhh2::Context& ctx){

  debug = false; // true/false

  for(auto & kv : ctx.get_all()){
    cout << " " << kv.first << " = " << kv.second << endl;
  }

  //// CONFIGURATION
  const TString METcollection = ctx.get("METName");
  isMC    = ctx.get("dataset_type") == "MC";
  isHOTVR = ctx.get("is_HOTVR") == "true";
  Sys_PU  = ctx.get("Sys_PU");

  // Check if this is an EFT sample and setup EFT weights
  isEFT = ctx.get("dataset_version").find("EFT") != string::npos;
  if(isEFT && isMC) {
    // Total number of EFT weights in the sample
    // Structure of weights:
    // - systweights[0]: Reference point weight (SM point)
    // - systweights[1-1676]: EFT parameter variations
    const int N_EFT_WEIGHTS = 1677;
    
    // Initialize handles for EFT weights
    h_n_eft_weights = ctx.declare_event_output<int>("n_eft_weights");
    h_ref_point_weight = ctx.declare_event_output<float>("ref_point_weight");
    
    // Create handles for each EFT weight
    h_eft_weights.reserve(N_EFT_WEIGHTS);  // Reserve space for efficiency
    for(int i = 0; i < N_EFT_WEIGHTS; i++) {
      std::string name = "eft_weight_" + std::to_string(i);
      h_eft_weights.push_back(ctx.declare_event_output<float>(name));
    }
  }

  // Print diagnostic information about weights in the first event
  // if(isEFT && isMC) {
  //   ctx.declare_event_output<bool>("first_event_processed", "first_event_processed");
  // }

  isUL16preVFP  = (ctx.get("dataset_version").find("UL16preVFP")  != std::string::npos);
  isUL16postVFP = (ctx.get("dataset_version").find("UL16postVFP") != std::string::npos);
  isUL17        = (ctx.get("dataset_version").find("UL17")        != std::string::npos);
  isUL18        = (ctx.get("dataset_version").find("UL18")        != std::string::npos);
  
  // lepton IDs
  // ElectronId eleID_veto = ElectronID_Fall17_tight_noIso;
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

  // Split interference signal samples by sign
  if(ctx.get("dataset_version").find("_int") != std::string::npos){
    if     (ctx.get("dataset_version").find("_pos") != std::string::npos) SignSplit.reset(new SignSelection("pos"));
    else if(ctx.get("dataset_version").find("_neg") != std::string::npos) SignSplit.reset(new SignSelection("neg"));
    else SignSplit.reset(new uhh2::AndSelection(ctx));
  }
  else SignSplit.reset(new uhh2::AndSelection(ctx));

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

  // Load weight IDs from file if this is an EFT sample
  if(isEFT && isMC) {
    string weight_id_file = ctx.get("weightIDFile", "/data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/EFT/EFTweights.txt");
    cout << "Loading weight IDs from: " << weight_id_file << endl;
    load_weight_ids(weight_id_file);
  }

  // Book histograms
  vector<string> histogram_tags = {"Input", "CommonModules", "HOTVRCorrections", "PUPPICorrections", "Lepton1", "JetID", "JetCleaner1", "JetCleaner2", "TopjetCleaner", "Jet1", "Jet2", "MET"};
  book_histograms(ctx, histogram_tags);

  lumihists.reset(new LuminosityHists(ctx, "lumi"));
}

bool ZprimePreselectionModule_EFT::process(uhh2::Event& event){

  // Store EFT weights if this is an EFT sample
  if(!event.isRealData && event.genInfo && isEFT) {
    // Store number of weights
    event.set(h_n_eft_weights, event.genInfo->systweights().size());
    
    // Store reference point weight (first weight)
    if(event.genInfo->systweights().size() > 0) {
      event.set(h_ref_point_weight, event.genInfo->systweights().at(0));
    }
    
    // Store all weights
    for(size_t i = 0; i < event.genInfo->systweights().size() && i < h_eft_weights.size(); i++) {
      event.set(h_eft_weights[i], event.genInfo->systweights().at(i));
    }

    // Print weights for first event only (for debugging)
    static bool first_event = true;
    if(first_event) {
      cout << "\n=== Weight Information ===\n";
      size_t n_weights = event.genInfo->systweights().size();
      cout << "Total number of weights: " << n_weights << "\n\n";
      
      // Print first 10 weights with their names
      size_t weights_to_print = std::min(size_t(10), n_weights);
      cout << "First " << weights_to_print << " weights:\n";
      for(size_t i = 0; i < weights_to_print; i++) {
        cout << weight_id_map[i] << " = " << event.genInfo->systweights().at(i);
        if(i == 0) cout << " (reference point)";
        cout << "\n";
      }
      
      // Print last 10 weights if there are more than 20 weights
      if(n_weights > 20) {
        cout << "\nLast " << weights_to_print << " weights:\n";
        for(size_t i = n_weights - weights_to_print; i < n_weights; i++) {
          cout << weight_id_map[i] << " = " << event.genInfo->systweights().at(i) << "\n";
        }
      }
      cout << "=========================\n\n";
      first_event = false;
    }
  }

  if(!event.isRealData){
    if(!SignSplit->passes(event)) return false;
  }
  if(debug) cout << "beginning: ok" << endl;

  fill_histograms(event, "Input");
   if(debug) cout << "first plots input: ok" << endl;

  bool commonResult = common->process(event);
  if (!commonResult) return false;
  if(debug) cout << "CommonModules: ok" << endl;
  fill_histograms(event, "CommonModules");

  sort_by_pt<Muon>(*event.muons);
  sort_by_pt<Electron>(*event.electrons);

  // Correct AK4 CHS jets
  CHSjetCorr->process(event);

  if(isHOTVR){
    hotvrjetCorr->process(event);
    fill_histograms(event, "HOTVRCorrections");
  }

  toppuppijetCorr->process(event);
  if(debug) cout << "TopPuppiJetCorrections: ok" << endl;
  fill_histograms(event, "PUPPICorrections");


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
  fill_histograms(event, "Lepton1");

  jet_IDcleaner->process(event);
  fill_histograms(event, "JetID");
  if(debug) cout << "JetCleaner ID: ok" << endl;

  jet_cleaner1->process(event);
  sort_by_pt<Jet>(*event.jets);
  fill_histograms(event, "JetCleaner1");
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
  fill_histograms(event, "JetCleaner2");
  if(debug) cout << "JetCleaner2: ok" << endl;

  hotvrjet_cleaner->process(event);
  sort_by_pt<TopJet>(*event.topjets);

  topjet_puppi_IDcleaner->process(event);
  topjet_puppi_cleaner->process(event);
  sort_by_pt<TopJet>(*event.toppuppijets);

  fill_histograms(event, "TopjetCleaner");
  if(debug) cout << "TopJetCleaner: ok" << endl;

  // 1st AK4 jet selection
  const bool pass_jet1 = jet1_sel->passes(event);
  if(!pass_jet1) return false;
  if(debug) cout << "NJetSelection1: ok" << endl;
  fill_histograms(event, "Jet1");

  // 2nd AK4 jet selection
  const bool pass_jet2 = jet2_sel->passes(event);
  if(!pass_jet2) return false;
  if(debug) cout << "NJetSelection2: ok" << endl;
  fill_histograms(event, "Jet2");

  // MET selection
  const bool pass_met = met_sel->passes(event);
  if(!pass_met) return false;
  if(debug) cout << "METCut: ok" << endl;
  fill_histograms(event, "MET");

  return true;
}

UHH2_REGISTER_ANALYSIS_MODULE(ZprimePreselectionModule_EFT)