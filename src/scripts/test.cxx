#include <iostream>
#include <memory>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <stdexcept>
#include <cctype>

#include <UHH2/core/include/AnalysisModule.h>
#include <UHH2/core/include/Event.h>
#include <UHH2/core/include/Selection.h>
#include <UHH2/common/include/PrintingModules.h>

#include <UHH2/common/include/CleaningModules.h>
#include <UHH2/common/include/NSelections.h>
#include <UHH2/common/include/LumiSelection.h>
#include <UHH2/common/include/TriggerSelection.h>
#include <UHH2/common/include/JetCorrections.h>
#include <UHH2/common/include/ObjectIdUtils.h>
#include <UHH2/common/include/MuonIds.h>
#include <UHH2/common/include/ElectronIds.h>
#include <UHH2/common/include/JetIds.h>
#include <UHH2/common/include/TopJetIds.h>
#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/Utils.h>
#include <UHH2/common/include/AdditionalSelections.h>
#include <UHH2/common/include/LuminosityHists.h>
#include <UHH2/common/include/MCWeight.h>
#include <UHH2/common/include/MuonHists.h>
#include <UHH2/common/include/ElectronHists.h>
#include <UHH2/common/include/JetHists.h>
#include <UHH2/common/include/EventHists.h>
#include <UHH2/common/include/TopPtReweight.h>
#include <UHH2/common/include/CommonModules.h>
#include <UHH2/common/include/LeptonScaleFactors.h>
#include <UHH2/common/include/PSWeights.h>

#include <UHH2/ZprimeSemiLeptonic/include/ModuleBASE.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicSelections.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicModules.h>
#include <UHH2/ZprimeSemiLeptonic/include/TTbarLJHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicGeneratorHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicCHSMatchHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeCandidate.h>
#include <UHH2/ZprimeSemiLeptonic/include/ElecTriggerSF.h>
#include <UHH2/ZprimeSemiLeptonic/include/AK4JetCorrections.h>
#include <UHH2/ZprimeSemiLeptonic/include/TopPuppiJetCorrections.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicSystematicsModule.h>
#include <UHH2/ZprimeSemiLeptonic/include/TopTagScaleFactor.h>
#include <UHH2/ZprimeSemiLeptonic/include/TopMistagScaleFactor.h>

#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/TTbarReconstruction.h>
#include <UHH2/common/include/ReconstructionHypothesisDiscriminators.h>

#include <UHH2/HOTVR/include/HadronicTop.h>
#include <UHH2/HOTVR/include/HOTVRScaleFactor.h>
#include <UHH2/HOTVR/include/HOTVRIds.h>

using namespace std;
using namespace uhh2;

/** A small struct to hold:
 *  - the branch name you want in your output,
 *  - the index in systweights() from which to read the weight.
 */
struct NamedWeight {
    std::string branch_name;
    int idx_syst; // index inside systweights()
};

class ZprimeAnalysisModule_EFT : public ModuleBASE {
public:
  explicit ZprimeAnalysisModule_EFT(uhh2::Context&);
  virtual bool process(uhh2::Event&) override;
  void book_histograms(uhh2::Context&, vector<string>);
  void fill_histograms(uhh2::Event&, string);
  
private:
  // Debug flag:
  bool debug;
  // Flags and configuration:
  bool isEFT;
  bool isMC, ishotvr, isdeepAK8;
  bool isUL16preVFP, isUL16postVFP, isUL17, isUL18;
  bool isMuon, isElectron, isPhoton, isEleTriggerMeasurement;
  TString sample, year, channel;
  string Sys_PU, Prefiring_direction, Sys_TopPt_a, Sys_TopPt_b;
  int runnr_oldtriggers;
  TH2F *ratio_hist_muon;
  TH2F *ratio_hist_ele;
  
  // Common modules, cleaners, scale factors, analysis modules, etc.
  std::unique_ptr<CommonModules> common;
  std::unique_ptr<MuonCleaner> muon_cleaner_low, muon_cleaner_high;
  std::unique_ptr<ElectronCleaner> electron_cleaner_low, electron_cleaner_high;
  
  unique_ptr<AnalysisModule> sf_muon_iso_stat_low, sf_muon_iso_syst_low, sf_muon_id_stat_low, sf_muon_id_syst_low,
      sf_muon_id_stat_high, sf_muon_id_syst_high, sf_muon_trigger_stat_low, sf_muon_trigger_syst_low,
      sf_muon_trigger_stat_high, sf_muon_trigger_syst_high;
  unique_ptr<AnalysisModule> sf_muon_iso_stat_low_dummy, sf_muon_iso_syst_low_dummy, sf_muon_id_stat_dummy, sf_muon_id_syst_dummy,
      sf_muon_trigger_stat_dummy, sf_muon_trigger_syst_dummy;
  unique_ptr<AnalysisModule> sf_ele_id_low, sf_ele_id_high, sf_ele_reco;
  unique_ptr<AnalysisModule> sf_ele_id_dummy, sf_ele_reco_dummy;
  unique_ptr<MuonRecoSF> sf_muon_reco;
  unique_ptr<AnalysisModule> sf_ele_trigger;
  unique_ptr<AnalysisModule> sf_btagging;
  
  unique_ptr<AnalysisModule> LumiWeight_module, PUWeight_module, TopPtReweight_module, MCScale_module;
  unique_ptr<AnalysisModule> NLOCorrections_module;
  unique_ptr<PSWeights> ps_weights;
  
  std::unique_ptr<HOTVRTopTagger> TopTaggerHOTVR;
  std::unique_ptr<AnalysisModule> hadronic_top;
  std::unique_ptr<AnalysisModule> sf_toptag;
  std::unique_ptr<AnalysisModule> sf_topmistag;
  std::unique_ptr<DeepAK8TopTagger> TopTaggerDeepAK8;
  
  std::unique_ptr<ZprimeCandidateBuilder> CandidateBuilder;
  
  std::unique_ptr<ZprimeChi2Discriminator> Chi2DiscriminatorZprime;
  std::unique_ptr<ZprimeCorrectMatchDiscriminator> CorrectMatchDiscriminatorZprime;
  
  std::unique_ptr<Selection> MuonVeto_selection, EleVeto_selection, NMuon1_selection, NEle1_selection;
  std::unique_ptr<Selection> Trigger_mu_A_selection, Trigger_mu_B_selection, Trigger_mu_C_selection, Trigger_mu_D_selection,
                             Trigger_mu_E_selection, Trigger_mu_F_selection;
  std::unique_ptr<Selection> Trigger_ele_A_selection, Trigger_ele_B_selection, Trigger_ph_A_selection;
  std::unique_ptr<Selection> TwoDCut_selection, TwoDCut_selection_low1, TwoDCut_selection_low2, Jet1_selection, Jet2_selection,
                             Met_selection, Chi2_selection, TTbarMatchable_selection, Chi2CandidateMatched_selection, ZprimeTopTag_selection;
  std::unique_ptr<uhh2::Selection> met_sel, htlep_sel;
  std::unique_ptr<Selection> sel_1btag, sel_2btag, HEM_selection;
  std::unique_ptr<Selection> SignSplit;
  
  std::unique_ptr<Variables_NN> Variables_module;
  
  // Handles
  Event::Handle<bool> h_is_zprime_reconstructed_chi2, h_is_zprime_reconstructed_correctmatch;
  Event::Handle<float> h_weight;
  uhh2::Event::Handle<ZprimeCandidate*> h_BestZprimeCandidateChi2;
  
  // Luminosity histograms:
  std::unique_ptr<Hists> lumihists_Weights_Init, lumihists_Weights_PU, lumihists_Weights_Lumi, lumihists_Weights_TopPt,
                         lumihists_Weights_MCScale, lumihists_Weights_PS, lumihists_Muon1_LowPt, lumihists_Muon1_HighPt,
                         lumihists_Ele1_LowPt, lumihists_Ele1_HighPt, lumihists_TriggerMuon, lumihists_TriggerEle,
                         lumihists_TwoDCut_Muon, lumihists_TwoDCut_Ele, lumihists_Jet1, lumihists_Jet2, lumihists_MET,
                         lumihists_HTlep, lumihists_Chi2;
  
  // Puppi CHS matching:
  std::unique_ptr<PuppiCHS_matching> AK4PuppiCHS_matching;
  std::unique_ptr<Selection> AK4PuppiCHS_BTagging;
  std::unique_ptr<Hists> h_CHSMatchHists, h_CHSMatchHists_beforeBTagSF, h_CHSMatchHists_afterBTagSF,
                         h_CHSMatchHists_after2DBTagSF, h_CHSMatchHists_afterBTag;
  
  // --- EFT Weight members ---
  // These are the preselection output handles
  std::vector<Event::Handle<float>> h_eft_weights;
  Event::Handle<int> h_n_eft_weights;
  Event::Handle<float> h_ref_point_weight;
  // And our vector of NamedWeight (which stores the branch name we want and the corresponding systweights() index)
  std::vector<NamedWeight> m_all_weights;
  // And the vector of output handles (one per named weight)
  std::vector<Event::Handle<float>> m_all_handles;
  
  // --- Helper function declaration ---
  void parse_single_block(const std::string & block, int index);
  
  // No separate load_first_355_eft: our load_weight_ids() now fills the maps and (for indices <355) m_all_weights.
  
  // --- Other helper: get_weight_by_name ---
  float get_weight_by_name(const uhh2::Event& event, const std::string& weight_name);
};

//////////////////////
//  Member functions
//////////////////////

void ZprimeAnalysisModule_EFT::book_histograms(uhh2::Context& ctx, vector<string> tags){
  for(const auto & tag : tags){
    string mytag = tag + "_General";
    book_HFolder(mytag, new ZprimeSemiLeptonicHists(ctx, mytag));
  }
}

void ZprimeAnalysisModule_EFT::fill_histograms(uhh2::Event& event, string tag){
  string mytag = tag + "_General";
  HFolder(mytag)->fill(event);
}

// ------------------------------------------------------------------
// parse_single_block: extracts the substring after "Weight ID:" and up to ", Weight value:".
// For indices <355, also adds the NamedWeight to m_all_weights.
// ------------------------------------------------------------------
void ZprimeAnalysisModule_EFT::parse_single_block(const std::string & block, int index) {
    size_t start_pos = block.find("Weight ID:");
    if(start_pos == std::string::npos) return;
    start_pos += 10; // skip "Weight ID:"
    size_t end_pos = block.find(", Weight value:");
    if(end_pos == std::string::npos) end_pos = block.size();
    std::string name = block.substr(start_pos, end_pos - start_pos);
    // Trim leading/trailing whitespace
    name.erase(name.begin(), std::find_if(name.begin(), name.end(), [](int ch){ return !std::isspace(ch); }));
    name.erase(std::find_if(name.rbegin(), name.rend(), [](int ch){ return !std::isspace(ch); }).base(), name.end());
    // Fill our maps:
    weight_index_to_name[index] = name;
    weight_name_to_index[name] = index;
    if(debug && index < 10) {
      std::cout << "parse_single_block: index " << index << " => name: " << name << std::endl;
    }
    // For the first 355 EFT weights, store in m_all_weights:
    if(index < 355) {
      NamedWeight w;
      w.branch_name = name;
      w.idx_syst = index;
      m_all_weights.push_back(w);
    }
}

// ------------------------------------------------------------------
// load_weight_ids: Reads the text file, builds blocks, and calls parse_single_block.
// ------------------------------------------------------------------
void ZprimeAnalysisModule_EFT::load_weight_ids(const std::string & filename) {
  std::ifstream file(filename);
  if(!file.is_open()) {
    std::cerr << "ERROR: Could not open weight ID file: " << filename << std::endl;
    return;
  }
  std::string line, block;
  bool reading_block = false;
  int index = 0;
  while(std::getline(file, line)) {
    if(line.empty()) continue;
    if(line.find("Weight ID:") != std::string::npos) {
      if(!block.empty()) {
        parse_single_block(block, index);
        block.clear();
        ++index;
      }
      block = line;
      reading_block = true;
    }
    else if(reading_block) {
      block += " " + line;
    }
    if(block.find("Weight value:") != std::string::npos) {
      parse_single_block(block, index);
      block.clear();
      reading_block = false;
      ++index;
    }
  }
  if(!block.empty()) {
    parse_single_block(block, index);
    ++index;
  }
  file.close();
  if(debug) {
    std::cout << "\n=== Weight ID Mapping Summary ===" << std::endl;
    std::cout << "Total weights mapped: " << weight_name_to_index.size() << std::endl;
    if(!weight_index_to_name.empty()) {
      std::cout << "First weight name: " << weight_index_to_name.begin()->second << std::endl;
      std::cout << "Last weight name:  " << weight_index_to_name.rbegin()->second << std::endl;
    }
    std::cout << "=================================" << std::endl << std::endl;
  }
}

// ------------------------------------------------------------------
// get_weight_by_name: retrieves the weight value from the event given its name.
// ------------------------------------------------------------------
float ZprimeAnalysisModule_EFT::get_weight_by_name(const uhh2::Event& event, const std::string& weight_name) {
  auto it = weight_name_to_index.find(weight_name);
  if(it == weight_name_to_index.end()) {
    throw std::runtime_error("Weight name not found in map: " + weight_name);
  }
  int idx = it->second;
  if(idx < 0 || idx >= static_cast<int>(h_eft_weights.size())) {
    throw std::runtime_error("Weight index out of range: " + std::to_string(idx));
  }
  return event.get(h_eft_weights[idx]);
}

// ------------------------------------------------------------------
// Constructor
// ------------------------------------------------------------------
ZprimeAnalysisModule_EFT::ZprimeAnalysisModule_EFT(uhh2::Context& ctx) {
  debug = false; // Set to true for debugging output.
  runnr_oldtriggers = 299368;
  
  // Print context settings.
  for(auto & kv : ctx.get_all()){
    std::cout << " " << kv.first << " = " << kv.second << std::endl;
  }
  
  isMC = (ctx.get("dataset_type") == "MC");
  ishotvr = (ctx.get("is_hotvr") == "true");
  isdeepAK8 = (ctx.get("is_deepAK8") == "true");
  TString mode = isdeepAK8 ? "deepAK8" : "hotvr";
  sample = ctx.get("dataset_version");
  isUL16preVFP  = (ctx.get("dataset_version").find("UL16preVFP") != std::string::npos);
  isUL16postVFP = (ctx.get("dataset_version").find("UL16postVFP") != std::string::npos);
  isUL17        = (ctx.get("dataset_version").find("UL17") != std::string::npos);
  isUL18        = (ctx.get("dataset_version").find("UL18") != std::string::npos);
  if(isUL16preVFP)  year = "UL16preVFP";
  if(isUL16postVFP) year = "UL16postVFP";
  if(isUL17)        year = "UL17";
  if(isUL18)        year = "UL18";
  isPhoton = (ctx.get("dataset_version").find("SinglePhoton") != std::string::npos);
  isEleTriggerMeasurement = (ctx.get("is_EleTriggerMeasurement") == "true");
  
  // [Set up lepton IDs, cleaners, selections, modules, histograms, etc.]
  // … (Assume the remainder of your initialization code remains the same.)
  // For brevity, these parts are not shown here.
  
  // --- EFT Weight Setup ---
  // Check if this is an EFT sample.
  isEFT = (ctx.get("dataset_version").find("EFT") != std::string::npos);
  if(isEFT) {
    // Get the preselection handles.
    h_n_eft_weights    = ctx.get_handle<int>("n_eft_weights");
    h_ref_point_weight = ctx.get_handle<float>("ref_point_weight");
    const int N_EFT_WEIGHTS = 1677;
    h_eft_weights.reserve(N_EFT_WEIGHTS);
    for(int i = 0; i < N_EFT_WEIGHTS; i++) {
      h_eft_weights.push_back(ctx.get_handle<float>("eft_weight_" + std::to_string(i)));
    }
    // Load the weight IDs from the text file. This fills the maps and, for indices <355, m_all_weights.
    std::string weight_id_file = ctx.get("weightIDFile", "/data/dust/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/src/EFTweights.txt");
    if(debug) std::cout << "Loading weight IDs from: " << weight_id_file << std::endl;
    load_weight_ids(weight_id_file);
  }
  
  // --- Add additional weights: scale variations and PDF weights ---
  // Scale variations: IDs 1001, 1006, 1011, 1016, 1021, 1031, 1041.
  std::vector<int> scale_ids = {1001, 1006, 1011, 1016, 1021, 1031, 1041};
  std::vector<std::string> scale_names = {"mur1_muf1", "mur1_muf2", "mur1_muf0p5", "mur2_muf1", "mur0p5_muf1", "murSome5", "murSome6"};
  for(unsigned i = 0; i < scale_ids.size(); i++){
      int offset = scale_ids[i] - 1001;  // offset from 1001
      int idx_syst = 355 + offset;       // index for ID=1001 is 355
      NamedWeight w;
      w.branch_name = scale_names[i];
      w.idx_syst = idx_syst;
      m_all_weights.push_back(w);
  }
  // PDF weights: IDs 1151..1251 => 101 weights.
  int pdf_id_start = 1151, pdf_id_end = 1251;
  for(int pdf_id = pdf_id_start; pdf_id <= pdf_id_end; pdf_id++){
      int offset = pdf_id - 1001;
      int idx_syst = 355 + offset;  // e.g., for 1151: idx = 355+150 = 505.
      int pdf_num = pdf_id - pdf_id_start + 1;
      NamedWeight w;
      w.branch_name = "PDF_" + std::to_string(pdf_num);
      w.idx_syst = idx_syst;
      m_all_weights.push_back(w);
  }
  
  // Declare the output handles for each weight branch.
  for(const auto & w : m_all_weights){
      m_all_handles.push_back(ctx.declare_event_output<float>(w.branch_name));
  }
  
  // ... (The remainder of your constructor: initialize selections, modules, histograms, etc.)
  
  // (For brevity, the rest of the constructor code remains unchanged.)
}

  
// ------------------------------------------------------------------
// process: For each event, fill the EFT weight branches using the systweights vector.
// ------------------------------------------------------------------
bool ZprimeAnalysisModule_EFT::process(uhh2::Event& event) {
  if(debug) {
      std::cout << "++++++++++++ NEW EVENT ++++++++++++++" << std::endl;
      std::cout << " run.event: " << event.run << ", " << event.event << std::endl;
  }
  event.set(h_is_zprime_reconstructed_chi2, false);
  event.set(h_is_zprime_reconstructed_correctmatch, false);
  if(!event.isRealData && !SignSplit->passes(event)) return false;
  
  // Retrieve systweights from GenInfo.
  const auto & sw = event.genInfo->systweights();
  if(sw.size() < 606) {
      if(debug) std::cout << "Not enough systweights: " << sw.size() << std::endl;
      return false;
  }
  
  // Loop over all our named weights and fill the corresponding output branch.
  for(unsigned i = 0; i < m_all_weights.size(); i++){
      int idx = m_all_weights[i].idx_syst;
      float val = sw[idx];
      event.set(m_all_handles[i], val);
      if(debug && i < 5) {
          std::cout << "Filling branch " << m_all_weights[i].branch_name 
                    << " (systweights index " << idx << ") with value " << val << std::endl;
      }
  }
  
  // (Rest of your analysis processing remains unchanged.)
  // For example: trigger selections, top-tagging, histograms, etc.
  // ...
  
  // (For brevity, the remainder of your process() code is unchanged.)
  
  // Example: Print first five EFT weights for debugging.
  if(isEFT && !event.isRealData && debug) {
      static bool first_event = true;
      if(first_event) {
          std::cout << "\n=== First Event EFT Weights ===" << std::endl;
          try {
              float refw = get_weight_by_name(event, "reference_point");
              std::cout << "Reference point weight: " << refw << std::endl;
          } catch(...) {
              std::cout << "Could not retrieve 'reference_point'" << std::endl;
          }
          std::cout << "First 5 EFT weights:" << std::endl;
          for (int i = 0; i < 5; i++){
              if(weight_index_to_name.find(i) != weight_index_to_name.end()){
                  std::string name = weight_index_to_name[i];
                  try {
                      float val = get_weight_by_name(event, name);
                      std::cout << "Weight " << i << ": Name: " << name << ", Value: " << val << std::endl;
                  } catch(std::runtime_error &e) {
                      std::cout << "Error retrieving weight " << i << ": " << e.what() << std::endl;
                  }
              }
          }
          std::cout << "===========================" << std::endl;
          first_event = false;
      }
  }
  
  // ... (Continue with the remainder of your event processing)
  
  return true;
}

UHH2_REGISTER_ANALYSIS_MODULE(ZprimeAnalysisModule_EFT)
