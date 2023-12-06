#include <iostream>
#include <memory>
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
#include <UHH2/common/include/ObjectIdUtils.h>
#include <UHH2/common/include/MuonIds.h>
#include <UHH2/common/include/ElectronIds.h>
#include <UHH2/common/include/JetIds.h>
#include <UHH2/common/include/TopJetIds.h>
#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/Utils.h>
#include <UHH2/common/include/AdditionalSelections.h>
#include "UHH2/common/include/LuminosityHists.h"
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
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicSystematicsHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicPDFHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicMulticlassNNHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicGeneratorHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicCHSMatchHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeSemiLeptonicMistagHists.h>
#include <UHH2/ZprimeSemiLeptonic/include/ZprimeCandidate.h>
#include <UHH2/ZprimeSemiLeptonic/include/ElecTriggerSF.h>
#include <UHH2/ZprimeSemiLeptonic/include/TopTagScaleFactor.h>
//#include <UHH2/ZprimeSemiLeptonic/include/TopMistagScaleFactor.h>

#include <UHH2/common/include/TTbarGen.h>
#include <UHH2/common/include/TTbarReconstruction.h>
#include <UHH2/common/include/ReconstructionHypothesisDiscriminators.h>

#include <UHH2/HOTVR/include/HadronicTop.h>
#include <UHH2/HOTVR/include/HOTVRScaleFactor.h>
#include <UHH2/HOTVR/include/HOTVRIds.h>

#include "UHH2/common/include/NeuralNetworkBase.hpp"

using namespace std;
using namespace uhh2;

/*
██████  ███████ ███████ ██ ███    ██ ██ ████████ ██  ██████  ███    ██
██   ██ ██      ██      ██ ████   ██ ██    ██    ██ ██    ██ ████   ██
██   ██ █████   █████   ██ ██ ██  ██ ██    ██    ██ ██    ██ ██ ██  ██
██   ██ ██      ██      ██ ██  ██ ██ ██    ██    ██ ██    ██ ██  ██ ██
██████  ███████ ██      ██ ██   ████ ██    ██    ██  ██████  ██   ████
*/


class NeuralNetworkModule: public NeuralNetworkBase {
public:
  explicit NeuralNetworkModule(uhh2::Context&, const std::string & ModelName, const std::string& ConfigName);
  virtual void CreateInputs(uhh2::Event & event) override;
protected:

  uhh2::Event::Handle<float> h_Ak4_j1_E;
  uhh2::Event::Handle<float> h_Ak4_j1_eta;
  uhh2::Event::Handle<float> h_Ak4_j1_m;
  uhh2::Event::Handle<float> h_Ak4_j1_phi;
  uhh2::Event::Handle<float> h_Ak4_j1_pt;
  uhh2::Event::Handle<float> h_Ak4_j1_deepjetbscore;

  uhh2::Event::Handle<float> h_Ak4_j2_E;
  uhh2::Event::Handle<float> h_Ak4_j2_eta;
  uhh2::Event::Handle<float> h_Ak4_j2_m;
  uhh2::Event::Handle<float> h_Ak4_j2_phi;
  uhh2::Event::Handle<float> h_Ak4_j2_pt;
  uhh2::Event::Handle<float> h_Ak4_j2_deepjetbscore;

  uhh2::Event::Handle<float> h_Ak4_j3_E;
  uhh2::Event::Handle<float> h_Ak4_j3_eta;
  uhh2::Event::Handle<float> h_Ak4_j3_m;
  uhh2::Event::Handle<float> h_Ak4_j3_phi;
  uhh2::Event::Handle<float> h_Ak4_j3_pt;
  uhh2::Event::Handle<float> h_Ak4_j3_deepjetbscore;

  uhh2::Event::Handle<float> h_Ak4_j4_E;
  uhh2::Event::Handle<float> h_Ak4_j4_eta;
  uhh2::Event::Handle<float> h_Ak4_j4_m;
  uhh2::Event::Handle<float> h_Ak4_j4_phi;
  uhh2::Event::Handle<float> h_Ak4_j4_pt;
  uhh2::Event::Handle<float> h_Ak4_j4_deepjetbscore;

  uhh2::Event::Handle<float> h_Ak4_j5_E;
  uhh2::Event::Handle<float> h_Ak4_j5_eta;
  uhh2::Event::Handle<float> h_Ak4_j5_m;
  uhh2::Event::Handle<float> h_Ak4_j5_phi;
  uhh2::Event::Handle<float> h_Ak4_j5_pt;
  uhh2::Event::Handle<float> h_Ak4_j5_deepjetbscore;

  uhh2::Event::Handle<float> h_Ele_E;
  uhh2::Event::Handle<float> h_Ele_eta;
  uhh2::Event::Handle<float> h_Ele_phi;
  uhh2::Event::Handle<float> h_Ele_pt;

  uhh2::Event::Handle<float> h_MET_phi;
  uhh2::Event::Handle<float> h_MET_pt;

  uhh2::Event::Handle<float> h_Mu_E;
  uhh2::Event::Handle<float> h_Mu_eta;
  uhh2::Event::Handle<float> h_Mu_phi;
  uhh2::Event::Handle<float> h_Mu_pt;

  uhh2::Event::Handle<float> h_N_Ak4;

  uhh2::Event::Handle<float> h_Ak8_j1_E;
  uhh2::Event::Handle<float> h_Ak8_j1_eta;
  uhh2::Event::Handle<float> h_Ak8_j1_mSD;
  uhh2::Event::Handle<float> h_Ak8_j1_phi;
  uhh2::Event::Handle<float> h_Ak8_j1_pt;
  uhh2::Event::Handle<float> h_Ak8_j1_tau21;
  uhh2::Event::Handle<float> h_Ak8_j1_tau32;

  uhh2::Event::Handle<float> h_Ak8_j2_E;
  uhh2::Event::Handle<float> h_Ak8_j2_eta;
  uhh2::Event::Handle<float> h_Ak8_j2_mSD;
  uhh2::Event::Handle<float> h_Ak8_j2_phi;
  uhh2::Event::Handle<float> h_Ak8_j2_pt;
  uhh2::Event::Handle<float> h_Ak8_j2_tau21;
  uhh2::Event::Handle<float> h_Ak8_j2_tau32;

  uhh2::Event::Handle<float> h_Ak8_j3_E;
  uhh2::Event::Handle<float> h_Ak8_j3_eta;
  uhh2::Event::Handle<float> h_Ak8_j3_mSD;
  uhh2::Event::Handle<float> h_Ak8_j3_phi;
  uhh2::Event::Handle<float> h_Ak8_j3_pt;
  uhh2::Event::Handle<float> h_Ak8_j3_tau21;
  uhh2::Event::Handle<float> h_Ak8_j3_tau32;

  uhh2::Event::Handle<float> h_N_Ak8;

};


NeuralNetworkModule::NeuralNetworkModule(Context& ctx, const std::string & ModelName, const std::string& ConfigName): NeuralNetworkBase(ctx, ModelName, ConfigName){


  h_Ak4_j1_E   = ctx.get_handle<float>("Ak4_j1_E");
  h_Ak4_j1_eta = ctx.get_handle<float>("Ak4_j1_eta");
  h_Ak4_j1_m   = ctx.get_handle<float>("Ak4_j1_m");
  h_Ak4_j1_phi = ctx.get_handle<float>("Ak4_j1_phi");
  h_Ak4_j1_pt  = ctx.get_handle<float>("Ak4_j1_pt");
  h_Ak4_j1_deepjetbscore  = ctx.get_handle<float>("Ak4_j1_deepjetbscore");

  h_Ak4_j2_E   = ctx.get_handle<float>("Ak4_j2_E");
  h_Ak4_j2_eta = ctx.get_handle<float>("Ak4_j2_eta");
  h_Ak4_j2_m   = ctx.get_handle<float>("Ak4_j2_m");
  h_Ak4_j2_phi = ctx.get_handle<float>("Ak4_j2_phi");
  h_Ak4_j2_pt  = ctx.get_handle<float>("Ak4_j2_pt");
  h_Ak4_j2_deepjetbscore  = ctx.get_handle<float>("Ak4_j2_deepjetbscore");

  h_Ak4_j3_E   = ctx.get_handle<float>("Ak4_j3_E");
  h_Ak4_j3_eta = ctx.get_handle<float>("Ak4_j3_eta");
  h_Ak4_j3_m   = ctx.get_handle<float>("Ak4_j3_m");
  h_Ak4_j3_phi = ctx.get_handle<float>("Ak4_j3_phi");
  h_Ak4_j3_pt  = ctx.get_handle<float>("Ak4_j3_pt");
  h_Ak4_j3_deepjetbscore  = ctx.get_handle<float>("Ak4_j3_deepjetbscore");

  h_Ak4_j4_E   = ctx.get_handle<float>("Ak4_j4_E");
  h_Ak4_j4_eta = ctx.get_handle<float>("Ak4_j4_eta");
  h_Ak4_j4_m   = ctx.get_handle<float>("Ak4_j4_m");
  h_Ak4_j4_phi = ctx.get_handle<float>("Ak4_j4_phi");
  h_Ak4_j4_pt  = ctx.get_handle<float>("Ak4_j4_pt");
  h_Ak4_j4_deepjetbscore  = ctx.get_handle<float>("Ak4_j4_deepjetbscore");

  h_Ak4_j5_E   = ctx.get_handle<float>("Ak4_j5_E");
  h_Ak4_j5_eta = ctx.get_handle<float>("Ak4_j5_eta");
  h_Ak4_j5_m   = ctx.get_handle<float>("Ak4_j5_m");
  h_Ak4_j5_phi = ctx.get_handle<float>("Ak4_j5_phi");
  h_Ak4_j5_pt  = ctx.get_handle<float>("Ak4_j5_pt");
  h_Ak4_j5_deepjetbscore  = ctx.get_handle<float>("Ak4_j5_deepjetbscore");

  h_Ele_E    = ctx.get_handle<float>("Ele_E");
  h_Ele_eta  = ctx.get_handle<float>("Ele_eta");
  h_Ele_phi  = ctx.get_handle<float>("Ele_phi");
  h_Ele_pt   = ctx.get_handle<float>("Ele_pt");

  h_MET_phi = ctx.get_handle<float>("MET_phi");
  h_MET_pt = ctx.get_handle<float>("MET_pt");

  h_Mu_E    = ctx.get_handle<float>("Mu_E");
  h_Mu_eta  = ctx.get_handle<float>("Mu_eta");
  h_Mu_phi  = ctx.get_handle<float>("Mu_phi");
  h_Mu_pt   = ctx.get_handle<float>("Mu_pt");

  h_N_Ak4 = ctx.get_handle<float>("N_Ak4");

  h_Ak8_j1_E     = ctx.get_handle<float>("Ak8_j1_E");
  h_Ak8_j1_eta   = ctx.get_handle<float>("Ak8_j1_eta");
  h_Ak8_j1_mSD   = ctx.get_handle<float>("Ak8_j1_mSD");
  h_Ak8_j1_phi   = ctx.get_handle<float>("Ak8_j1_phi");
  h_Ak8_j1_pt    = ctx.get_handle<float>("Ak8_j1_pt");
  h_Ak8_j1_tau21 = ctx.get_handle<float>("Ak8_j1_tau21");
  h_Ak8_j1_tau32 = ctx.get_handle<float>("Ak8_j1_tau32");

  h_Ak8_j2_E     = ctx.get_handle<float>("Ak8_j2_E");
  h_Ak8_j2_eta   = ctx.get_handle<float>("Ak8_j2_eta");
  h_Ak8_j2_mSD   = ctx.get_handle<float>("Ak8_j2_mSD");
  h_Ak8_j2_phi   = ctx.get_handle<float>("Ak8_j2_phi");
  h_Ak8_j2_pt    = ctx.get_handle<float>("Ak8_j2_pt");
  h_Ak8_j2_tau21 = ctx.get_handle<float>("Ak8_j2_tau21");
  h_Ak8_j2_tau32 = ctx.get_handle<float>("Ak8_j2_tau32");

  h_Ak8_j3_E     = ctx.get_handle<float>("Ak8_j3_E");
  h_Ak8_j3_eta   = ctx.get_handle<float>("Ak8_j3_eta");
  h_Ak8_j3_mSD   = ctx.get_handle<float>("Ak8_j3_mSD");
  h_Ak8_j3_phi   = ctx.get_handle<float>("Ak8_j3_phi");
  h_Ak8_j3_pt    = ctx.get_handle<float>("Ak8_j3_pt");
  h_Ak8_j3_tau21 = ctx.get_handle<float>("Ak8_j3_tau21");
  h_Ak8_j3_tau32 = ctx.get_handle<float>("Ak8_j3_tau32");

  h_N_Ak8 = ctx.get_handle<float>("N_Ak8");
}

void NeuralNetworkModule::CreateInputs(Event & event){
  NNInputs.clear();
  NNoutputs.clear();

  string varname[59];
  string scal[59];
  string mean[59];
  string std[59];
  double mean_val[59];
  double std_val[59];
  //Only Ele or Mu variables!!
  ifstream normfile ("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/KerasNN/NN_DeepAK8_UL17_muon/NormInfo.txt", ios::in);
  if(!normfile.good()) throw runtime_error("NeuralNetworkModule: The specified norm file does not exist.");
  if (normfile.is_open()){
    for(int i = 0; i < 59; ++i)
    {
      normfile >> varname[i] >> scal[i] >> mean[i] >> std[i];
      mean_val[i] = std::stod(mean[i]);
      std_val[i] = std::stod(std[i]);
    }
    normfile.close();
  }

  NNInputs.push_back( tensorflow::Tensor(tensorflow::DT_FLOAT, {1, 59}));

  //Only Ele or Mu variables!!
   vector<uhh2::Event::Handle<float>> inputs = {h_Ak4_j1_E, h_Ak4_j1_deepjetbscore, h_Ak4_j1_eta, h_Ak4_j1_m, h_Ak4_j1_phi, h_Ak4_j1_pt, h_Ak4_j2_E, h_Ak4_j2_deepjetbscore, h_Ak4_j2_eta, h_Ak4_j2_m, h_Ak4_j2_phi, h_Ak4_j2_pt, h_Ak4_j3_E, h_Ak4_j3_deepjetbscore, h_Ak4_j3_eta, h_Ak4_j3_m, h_Ak4_j3_phi, h_Ak4_j3_pt, h_Ak4_j4_E, h_Ak4_j4_deepjetbscore, h_Ak4_j4_eta, h_Ak4_j4_m, h_Ak4_j4_phi, h_Ak4_j4_pt, h_Ak4_j5_E, h_Ak4_j5_deepjetbscore, h_Ak4_j5_eta, h_Ak4_j5_m, h_Ak4_j5_phi, h_Ak4_j5_pt, h_Ak8_j1_E, h_Ak8_j1_eta, h_Ak8_j1_mSD, h_Ak8_j1_phi, h_Ak8_j1_pt, h_Ak8_j1_tau21, h_Ak8_j1_tau32, h_Ak8_j2_E, h_Ak8_j2_eta, h_Ak8_j2_mSD, h_Ak8_j2_phi, h_Ak8_j2_pt, h_Ak8_j2_tau21, h_Ak8_j2_tau32, h_Ak8_j3_E, h_Ak8_j3_eta, h_Ak8_j3_mSD, h_Ak8_j3_phi, h_Ak8_j3_pt, h_Ak8_j3_tau21, h_Ak8_j3_tau32, h_MET_phi, h_MET_pt, h_Mu_E, h_Mu_eta, h_Mu_phi, h_Mu_pt, h_N_Ak4, h_N_Ak8}; // in alphabetical order to match NormInfo.txt

  for(int i = 0; i < 59; ++i){
    NNInputs.at(0).tensor<float, 2>()(0,i)  = (event.get(inputs.at(i))   - mean_val[i]) / (std_val[i]);
  }

  if (NNInputs.size()!=LayerInputs.size()) throw logic_error("NeuralNetworkModule.cxx: Create a number of inputs diffetent wrt. LayerInputs.size()="+to_string(LayerInputs.size()));
}



class ZprimeAnalysisModule_applyNN : public ModuleBASE {

public:
  explicit ZprimeAnalysisModule_applyNN(uhh2::Context&);
  virtual bool process(uhh2::Event&) override;
  void book_histograms(uhh2::Context&, vector<string>);
  void fill_histograms(uhh2::Event&, string);

protected:

  bool debug;

  // Cleaners
  std::unique_ptr<MuonCleaner>     muon_cleaner_low, muon_cleaner_high;
  std::unique_ptr<ElectronCleaner> electron_cleaner_low, electron_cleaner_high;

  // scale factors
  unique_ptr<AnalysisModule> sf_muon_iso_low, sf_muon_id_low, sf_muon_id_high, sf_muon_trigger_low, sf_muon_trigger_high;
  unique_ptr<AnalysisModule> sf_muon_iso_low_dummy, sf_muon_id_dummy, sf_muon_trigger_dummy;
  unique_ptr<AnalysisModule> sf_ele_id_low, sf_ele_id_high, sf_ele_reco;
  unique_ptr<AnalysisModule> sf_ele_id_dummy, sf_ele_reco_dummy;
  unique_ptr<MuonRecoSF> sf_muon_reco;
  unique_ptr<AnalysisModule> sf_ele_trigger;
  unique_ptr<AnalysisModule> sf_btagging;

  // AnalysisModules
  unique_ptr<AnalysisModule> LumiWeight_module, PUWeight_module, TopPtReweight_module, MCScale_module;
  unique_ptr<AnalysisModule> NLOCorrections_module;
  unique_ptr<PSWeights> ps_weights;

  // Top tagging
  unique_ptr<HOTVRTopTagger> TopTaggerHOTVR;
  unique_ptr<AnalysisModule> hadronic_top;
  unique_ptr<AnalysisModule> sf_toptag;
  unique_ptr<DeepAK8TopTagger> TopTaggerDeepAK8;

  // TopTags veto
  unique_ptr<Selection> TopTagVetoSelection;

  // Mass reconstruction
  unique_ptr<ZprimeCandidateBuilder> CandidateBuilder;

  // Chi2 discriminator
  unique_ptr<ZprimeChi2Discriminator> Chi2DiscriminatorZprime;
  unique_ptr<ZprimeCorrectMatchDiscriminator> CorrectMatchDiscriminatorZprime;

  // Selections
  unique_ptr<Selection> Chi2_selection, TTbarMatchable_selection, Chi2CandidateMatched_selection, ZprimeTopTag_selection;
  std::unique_ptr<uhh2::Selection> met_sel;
  std::unique_ptr<uhh2::Selection> htlep_sel;
  std::unique_ptr<Selection> sel_1btag, sel_2btag;
  std::unique_ptr<Selection> HEM_selection;
  unique_ptr<Selection> ThetaStar_selection_bin1, ThetaStar_selection_bin2, ThetaStar_selection_bin3, ThetaStar_selection_bin4, ThetaStar_selection_bin5, ThetaStar_selection_bin6;
  unique_ptr<Selection> AbsThetaStar_selection_bin1, AbsThetaStar_selection_bin2, AbsThetaStar_selection_bin3, AbsThetaStar_selection_bin4, AbsThetaStar_selection_bin5;

  // systematics handles
 // unique_ptr<ZprimeSemiLeptonicSystematicsModule> SystematicsModule;

  // NN variables handles
  unique_ptr<Variables_NN> Variables_module;

  //Handles
  Event::Handle<bool> h_is_zprime_reconstructed_chi2, h_is_zprime_reconstructed_correctmatch;
  Event::Handle<float> h_chi2;
  Event::Handle<float> h_weight;

  uhh2::Event::Handle<ZprimeCandidate*> h_BestZprimeCandidateChi2;

  // Lumi hists
  std::unique_ptr<Hists> lumihists_Weights_Init, lumihists_Weights_PU, lumihists_Weights_Lumi, lumihists_Weights_TopPt, lumihists_Weights_MCScale, lumihists_Weights_PS, lumihists_Chi2;

  float inv_mass(const LorentzVector& p4){ return p4.isTimelike() ? p4.mass() : -sqrt(-p4.mass2()); }

  // DNN multiclass output hist
  std::unique_ptr<Hists> h_MulticlassNN_output;

  // Hists with systematics variations
  std::unique_ptr<Hists> DeltaY_SystVariations_DNN_output0;
  std::unique_ptr<Hists> DeltaY_SystVariations_DNN_output1;
  std::unique_ptr<Hists> DeltaY_SystVariations_DNN_output2;
  std::unique_ptr<Hists> DeltaY_SystVariations_DNN_output0_TopTag;
  std::unique_ptr<Hists> DeltaY_SystVariations_DNN_output1_TopTag;
  std::unique_ptr<Hists> DeltaY_SystVariations_DNN_output2_TopTag;
  std::unique_ptr<Hists> DeltaY_SystVariations_DNN_output0_NoTopTag;
  std::unique_ptr<Hists> DeltaY_SystVariations_DNN_output1_NoTopTag;
  std::unique_ptr<Hists> DeltaY_SystVariations_DNN_output2_NoTopTag;
  

  
  // Configuration
  bool isMC, ishotvr, isdeepAK8;
  string Sys_PU, Prefiring_direction, Sys_TopPt_a, Sys_TopPt_b;
  TString sample;
  int runnr_oldtriggers = 299368;

  bool isUL16preVFP, isUL16postVFP, isUL17, isUL18;
  bool isMuon, isElectron;
  bool isPhoton;
  TString year;

  TH2F *ratio_hist_muon;
  TH2F *ratio_hist_ele;

  Event::Handle<float> h_Ak4_j1_E;
  Event::Handle<float> h_Ak4_j1_eta;
  Event::Handle<float> h_Ak4_j1_m;
  Event::Handle<float> h_Ak4_j1_phi;
  Event::Handle<float> h_Ak4_j1_pt;
  Event::Handle<float> h_Ak4_j1_deepjetbscore;

  Event::Handle<float> h_Ak4_j2_E;
  Event::Handle<float> h_Ak4_j2_eta;
  Event::Handle<float> h_Ak4_j2_m;
  Event::Handle<float> h_Ak4_j2_phi;
  Event::Handle<float> h_Ak4_j2_pt;
  Event::Handle<float> h_Ak4_j2_deepjetbscore;

  Event::Handle<float> h_Ak4_j3_E;
  Event::Handle<float> h_Ak4_j3_eta;
  Event::Handle<float> h_Ak4_j3_m;
  Event::Handle<float> h_Ak4_j3_phi;
  Event::Handle<float> h_Ak4_j3_pt;
  Event::Handle<float> h_Ak4_j3_deepjetbscore;

  Event::Handle<float> h_Ak4_j4_E;
  Event::Handle<float> h_Ak4_j4_eta;
  Event::Handle<float> h_Ak4_j4_m;
  Event::Handle<float> h_Ak4_j4_phi;
  Event::Handle<float> h_Ak4_j4_pt;
  Event::Handle<float> h_Ak4_j4_deepjetbscore;

  Event::Handle<float> h_Ak4_j5_E;
  Event::Handle<float> h_Ak4_j5_eta;
  Event::Handle<float> h_Ak4_j5_m;
  Event::Handle<float> h_Ak4_j5_phi;
  Event::Handle<float> h_Ak4_j5_pt;
  Event::Handle<float> h_Ak4_j5_deepjetbscore;

  Event::Handle<float> h_Ele_E;
  Event::Handle<float> h_Ele_eta;
  Event::Handle<float> h_Ele_phi;
  Event::Handle<float> h_Ele_pt;

  Event::Handle<float> h_MET_phi;
  Event::Handle<float> h_MET_pt;

  Event::Handle<float> h_Mu_E;
  Event::Handle<float> h_Mu_eta;
  Event::Handle<float> h_Mu_phi;
  Event::Handle<float> h_Mu_pt;

  Event::Handle<float> h_N_Ak4;

  Event::Handle<float> h_Ak8_j1_E;
  Event::Handle<float> h_Ak8_j1_eta;
  Event::Handle<float> h_Ak8_j1_mSD;
  Event::Handle<float> h_Ak8_j1_phi;
  Event::Handle<float> h_Ak8_j1_pt;
  Event::Handle<float> h_Ak8_j1_tau21;
  Event::Handle<float> h_Ak8_j1_tau32;

  Event::Handle<float> h_Ak8_j2_E;
  Event::Handle<float> h_Ak8_j2_eta;
  Event::Handle<float> h_Ak8_j2_mSD;
  Event::Handle<float> h_Ak8_j2_phi;
  Event::Handle<float> h_Ak8_j2_pt;
  Event::Handle<float> h_Ak8_j2_tau21;
  Event::Handle<float> h_Ak8_j2_tau32;

  Event::Handle<float> h_Ak8_j3_E;
  Event::Handle<float> h_Ak8_j3_eta;
  Event::Handle<float> h_Ak8_j3_mSD;
  Event::Handle<float> h_Ak8_j3_phi;
  Event::Handle<float> h_Ak8_j3_pt;
  Event::Handle<float> h_Ak8_j3_tau21;
  Event::Handle<float> h_Ak8_j3_tau32;

  Event::Handle<float> h_N_Ak8;

  //beren_dy

  Event::Handle<float> h_DeltaY_gen_ele; //-beren 
  Event::Handle<float> h_DeltaY_gen_muon; //-beren 
  Event::Handle<float> h_DeltaY_gen_mass; //-beren
  Event::Handle<float> h_topQuarkCount;

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

  Event::Handle<float> h_DeltaR_leptonic_genparticle; //-beren
  Event::Handle<float> h_DeltaR_hadronic_genparticle; //-beren

  Event::Handle<float> h_not_reconstructed_muon; //-beren
  Event::Handle<float> h_not_reconstructed_0_500_muon; //-beren
  Event::Handle<float> h_not_reconstructed_500_750_muon; //-beren
  Event::Handle<float> h_not_reconstructed_750_1000_muon; //-beren
  Event::Handle<float> h_not_reconstructed_1000_1500_muon; //-beren
  Event::Handle<float> h_not_reconstructed_1500Inf_muon; //-beren

  Event::Handle<float> h_not_reconstructed_ele; //-beren
  Event::Handle<float> h_not_reconstructed_0_500_ele; //-beren
  Event::Handle<float> h_not_reconstructed_500_750_ele; //-beren
  Event::Handle<float> h_not_reconstructed_750_1000_ele; //-beren
  Event::Handle<float> h_not_reconstructed_1000_1500_ele; //-beren
  Event::Handle<float> h_not_reconstructed_1500Inf_ele; //-beren

  Event::Handle<float> h_DeltaY_reco; //-beren
  Event::Handle<float> h_DeltaY_reco_mass; //-beren
  Event::Handle<float> h_DeltaY_N_reco; //-beren
  Event::Handle<float> h_DeltaY_P_reco; //-beren
  Event::Handle<float> h_DeltaY_N_reco_nomass; //-beren
  Event::Handle<float> h_DeltaY_P_reco_nomass; //-beren
  Event::Handle<float> h_DeltaY_gen; //-beren 
  Event::Handle<float> h_DeltaY_N_gen; //-beren
  Event::Handle<float> h_DeltaY_N_gen_nomass; //-beren
  Event::Handle<float> h_DeltaY_P_gen; //-beren
  Event::Handle<float> h_DeltaY_P_gen_nomass; //-beren
  Event::Handle<float> h_DeltaY_P_P; //-beren
  Event::Handle<float> h_DeltaY_P_N; //-beren
  Event::Handle<float> h_DeltaY_N_P; //-beren
  Event::Handle<float> h_DeltaY_N_N; //-beren

  Event::Handle<float> h_DeltaY_P_P_nomass_muon; //-beren
  Event::Handle<float> h_DeltaY_P_N_nomass_muon; //-beren
  Event::Handle<float> h_DeltaY_N_P_nomass_muon; //-beren
  Event::Handle<float> h_DeltaY_N_N_nomass_muon; //-beren

  Event::Handle<float> h_DeltaY_P_N_0_500_muon; //-beren
  Event::Handle<float> h_DeltaY_P_P_0_500_muon; //-beren
  Event::Handle<float> h_DeltaY_N_P_0_500_muon; //-beren
  Event::Handle<float> h_DeltaY_N_N_0_500_muon; //-beren

  Event::Handle<float> h_DeltaY_P_P_500_750_muon; //-beren
  Event::Handle<float> h_DeltaY_P_N_500_750_muon; //-beren
  Event::Handle<float> h_DeltaY_N_P_500_750_muon; //-beren
  Event::Handle<float> h_DeltaY_N_N_500_750_muon; //-beren

  Event::Handle<float> h_DeltaY_P_P_750_1000_muon; //-beren
  Event::Handle<float> h_DeltaY_P_N_750_1000_muon; //-beren
  Event::Handle<float> h_DeltaY_N_P_750_1000_muon; //-beren
  Event::Handle<float> h_DeltaY_N_N_750_1000_muon; //-beren

  Event::Handle<float> h_DeltaY_P_P_1000_1500_muon; //-beren
  Event::Handle<float> h_DeltaY_P_N_1000_1500_muon; //-beren
  Event::Handle<float> h_DeltaY_N_P_1000_1500_muon; //-beren
  Event::Handle<float> h_DeltaY_N_N_1000_1500_muon; //-beren

  Event::Handle<float> h_DeltaY_P_P_1500Inf_muon; //-beren
  Event::Handle<float> h_DeltaY_P_N_1500Inf_muon; //-beren
  Event::Handle<float> h_DeltaY_N_P_1500Inf_muon; //-beren
  Event::Handle<float> h_DeltaY_N_N_1500Inf_muon; //-beren

  Event::Handle<float> h_DeltaY_P_P_750Inf_muon; //-beren
  Event::Handle<float> h_DeltaY_P_N_750Inf_muon; //-beren
  Event::Handle<float> h_DeltaY_N_P_750Inf_muon; //-beren
  Event::Handle<float> h_DeltaY_N_N_750Inf_muon; //-beren


  Event::Handle<float> h_DeltaY_P_P_nomass_ele; //-beren
  Event::Handle<float> h_DeltaY_P_N_nomass_ele; //-beren
  Event::Handle<float> h_DeltaY_N_P_nomass_ele; //-beren
  Event::Handle<float> h_DeltaY_N_N_nomass_ele; //-beren

  Event::Handle<float> h_DeltaY_P_N_0_500_ele; //-beren
  Event::Handle<float> h_DeltaY_P_P_0_500_ele; //-beren
  Event::Handle<float> h_DeltaY_N_P_0_500_ele; //-beren
  Event::Handle<float> h_DeltaY_N_N_0_500_ele; //-beren

  Event::Handle<float> h_DeltaY_P_P_500_750_ele; //-beren
  Event::Handle<float> h_DeltaY_P_N_500_750_ele; //-beren
  Event::Handle<float> h_DeltaY_N_P_500_750_ele; //-beren
  Event::Handle<float> h_DeltaY_N_N_500_750_ele; //-beren

  Event::Handle<float> h_DeltaY_P_P_750_1000_ele; //-beren
  Event::Handle<float> h_DeltaY_P_N_750_1000_ele; //-beren
  Event::Handle<float> h_DeltaY_N_P_750_1000_ele; //-beren
  Event::Handle<float> h_DeltaY_N_N_750_1000_ele; //-beren

  Event::Handle<float> h_DeltaY_P_P_1000_1500_ele; //-beren
  Event::Handle<float> h_DeltaY_P_N_1000_1500_ele; //-beren
  Event::Handle<float> h_DeltaY_N_P_1000_1500_ele; //-beren
  Event::Handle<float> h_DeltaY_N_N_1000_1500_ele; //-beren

  Event::Handle<float> h_DeltaY_P_P_1500Inf_ele; //-beren
  Event::Handle<float> h_DeltaY_P_N_1500Inf_ele; //-beren
  Event::Handle<float> h_DeltaY_N_P_1500Inf_ele; //-beren
  Event::Handle<float> h_DeltaY_N_N_1500Inf_ele; //-beren

  Event::Handle<float> h_DeltaY_P_P_750Inf_ele; //-beren
  Event::Handle<float> h_DeltaY_P_N_750Inf_ele; //-beren
  Event::Handle<float> h_DeltaY_N_P_750Inf_ele; //-beren
  Event::Handle<float> h_DeltaY_N_N_750Inf_ele; //-beren

  Event::Handle<std::vector<tensorflow::Tensor> > h_NNoutput;
  Event::Handle<double> h_NNoutput0;
  Event::Handle<double> h_NNoutput1;
  Event::Handle<double> h_NNoutput2;

  std::unique_ptr<NeuralNetworkModule> NNModule;

   //bool isEleTriggerMeasurement;

};

void ZprimeAnalysisModule_applyNN::book_histograms(uhh2::Context& ctx, vector<string> tags){
  for(const auto & tag : tags){
    string mytag = tag + "_Skimming";
    mytag = tag+"_General";
    book_HFolder(mytag, new ZprimeSemiLeptonicHists(ctx,mytag));
  }
}

void ZprimeAnalysisModule_applyNN::fill_histograms(uhh2::Event& event, string tag){
  string mytag = tag + "_Skimming";
  mytag = tag+"_General";
  HFolder(mytag)->fill(event);
}

/*
█  ██████  ██████  ███    ██ ███████ ████████ ██████  ██    ██  ██████ ████████  ██████  ██████
█ ██      ██    ██ ████   ██ ██         ██    ██   ██ ██    ██ ██         ██    ██    ██ ██   ██
█ ██      ██    ██ ██ ██  ██ ███████    ██    ██████  ██    ██ ██         ██    ██    ██ ██████
█ ██      ██    ██ ██  ██ ██      ██    ██    ██   ██ ██    ██ ██         ██    ██    ██ ██   ██
█  ██████  ██████  ██   ████ ███████    ██    ██   ██  ██████   ██████    ██     ██████  ██   ██
*/

ZprimeAnalysisModule_applyNN::ZprimeAnalysisModule_applyNN(uhh2::Context& ctx){
  // debug = true;
  debug = false;
  for(auto & kv : ctx.get_all()){
    cout << " " << kv.first << " = " << kv.second << endl;
  }
  // Configuration
  isMC = (ctx.get("dataset_type") == "MC");
  ishotvr = (ctx.get("is_hotvr") == "true");
  isdeepAK8 = (ctx.get("is_deepAK8") == "true");
  TString mode = "hotvr";
  if(isdeepAK8) mode = "deepAK8";
  string tmp = ctx.get("dataset_version");
  sample = tmp;
  isUL16preVFP  = (ctx.get("dataset_version").find("UL16preVFP")  != std::string::npos);
  isUL16postVFP = (ctx.get("dataset_version").find("UL16postVFP") != std::string::npos);
  isUL17        = (ctx.get("dataset_version").find("UL17")        != std::string::npos);
  isUL18        = (ctx.get("dataset_version").find("UL18")        != std::string::npos);
  if(isUL16preVFP) year = "UL16preVFP";
  if(isUL16postVFP) year = "UL16postVFP";
  if(isUL17) year = "UL17";
  if(isUL18) year = "UL18";

  isPhoton = (ctx.get("dataset_version").find("SinglePhoton") != std::string::npos);
  // isEleTriggerMeasurement = (ctx.get("is_EleTriggerMeasurement") == "true");

  // Lepton IDs
  ElectronId eleID_low  = ElectronTagID(Electron::mvaEleID_Fall17_iso_V2_wp80);
  ElectronId eleID_high = ElectronTagID(Electron::mvaEleID_Fall17_noIso_V2_wp80);
  MuonId     muID_low   = AndId<Muon>(MuonID(Muon::CutBasedIdTight), MuonID(Muon::PFIsoTight));
  MuonId     muID_high  = MuonID(Muon::CutBasedIdGlobalHighPt);

  double electron_pt_low;
  if(isUL17){
    electron_pt_low = 38.; // UL17 ele trigger threshold is 35 (HLT_Ele35WPTight _Gsf) -> be above turn on
  }
  else{
    electron_pt_low = 35.;
  }
  double muon_pt_low(30.);
  double electron_pt_high(120.);
  double muon_pt_high(55.);

  const MuonId muonID_low(AndId<Muon>(PtEtaCut(muon_pt_low, 2.4), muID_low));
  const ElectronId electronID_low(AndId<Electron>(PtEtaSCCut(electron_pt_low, 2.5), eleID_low));
  const MuonId muonID_high(AndId<Muon>(PtEtaCut(muon_pt_high, 2.4), muID_high));
  const ElectronId electronID_high(AndId<Electron>(PtEtaSCCut(electron_pt_high, 2.5), eleID_high));

  muon_cleaner_low.reset(new MuonCleaner(muonID_low));
  electron_cleaner_low.reset(new ElectronCleaner(electronID_low));
  muon_cleaner_high.reset(new MuonCleaner(muonID_high));
  electron_cleaner_high.reset(new ElectronCleaner(electronID_high));

  // Important selection values
  double chi2_max(30.);
  string trigger_mu_A, trigger_mu_B, trigger_mu_C, trigger_mu_D, trigger_mu_E, trigger_mu_F;
  string trigger_ele_A, trigger_ele_B;
  string trigger_ph_A;
  isMuon = false; isElectron = false;
  if(ctx.get("channel") == "muon") isMuon = true;
  if(ctx.get("channel") == "electron") isElectron = true;

  if(isMuon){//semileptonic muon channel
    if(isUL17){
      trigger_mu_A = "HLT_IsoMu27_v*";
    }
    else{
      trigger_mu_A = "HLT_IsoMu24_v*";
    }
    trigger_mu_B = "HLT_IsoTkMu24_v*";
    trigger_mu_C = "HLT_Mu50_v*";
    trigger_mu_D = "HLT_TkMu50_v*";
    trigger_mu_E = "HLT_OldMu100_v*";
    trigger_mu_F = "HLT_TkMu100_v*";

  }
  if(isElectron){//semileptonic electron channel
    trigger_ele_B = "HLT_Ele115_CaloIdVT_GsfTrkIdT_v*";
    if(isUL16preVFP || isUL16postVFP){
      trigger_ele_A = "HLT_Ele27_WPTight_Gsf_v*";
    }
    if(isUL17){
      trigger_ele_A = "HLT_Ele35_WPTight_Gsf_v*";
    }
    if(isUL18){
      trigger_ele_A = "HLT_Ele32_WPTight_Gsf_v*";
    }
    if(isUL16preVFP || isUL16postVFP){
      trigger_ph_A = "HLT_Photon175_v*";
    }
    else{
      trigger_ph_A = "HLT_Photon200_v*";
    }
  }


  const TopJetId toptagID = AndId<TopJet>(HOTVRTopTag(0.8, 140.0, 220.0, 50.0), Tau32Groomed(0.56));

  Sys_PU = ctx.get("Sys_PU");
  Prefiring_direction = ctx.get("Sys_prefiring");
  Sys_TopPt_a = ctx.get("Systematic_TopPt_a");
  Sys_TopPt_b = ctx.get("Systematic_TopPt_b");

  BTag::algo btag_algo = BTag::DEEPJET;
  BTag::wp btag_wp = BTag::WP_MEDIUM;
  JetId id_btag = BTag(btag_algo, btag_wp);

  // double a_toppt = 0.0615; // par a TopPt Reweighting
  // double b_toppt = -0.0005; // par b TopPt Reweighting

  // Modules
  LumiWeight_module.reset(new MCLumiWeight(ctx));
  PUWeight_module.reset(new MCPileupReweight(ctx, Sys_PU));
  //TopPtReweight_module.reset(new TopPtReweighting(ctx, a_toppt, b_toppt, Sys_TopPt_a, Sys_TopPt_b, ""));
  MCScale_module.reset(new MCScaleVariation(ctx));
  hadronic_top.reset(new HadronicTop(ctx));
  // sf_toptag.reset(new HOTVRScaleFactor(ctx, toptagID, ctx.get("Sys_TopTag", "nominal"), "HadronicTop", "TopTagSF", "HOTVRTopTagSFs"));
  sf_toptag.reset(new TopTagScaleFactor(ctx));
  NLOCorrections_module.reset(new NLOCorrections(ctx));
  ps_weights.reset(new PSWeights(ctx));

  // b-tagging SFs
  sf_btagging.reset(new MCBTagDiscriminantReweighting(ctx, BTag::algo::DEEPJET, "CHS_matched"));

  // set lepton scale factors: see UHH2/common/include/LeptonScaleFactors.h
  sf_muon_iso_low.reset(new uhh2::MuonIsoScaleFactors(ctx, Muon::Selector::PFIsoTight, Muon::Selector::CutBasedIdTight, true));
  sf_muon_id_low.reset(new uhh2::MuonIdScaleFactors(ctx, Muon::Selector::CutBasedIdTight, true));
  sf_muon_id_high.reset(new uhh2::MuonIdScaleFactors(ctx, Muon::Selector::CutBasedIdGlobalHighPt, true));
  sf_muon_trigger_low.reset(new uhh2::MuonTriggerScaleFactors(ctx, false, true));
  sf_muon_trigger_high.reset(new uhh2::MuonTriggerScaleFactors(ctx, true, false));
  sf_muon_reco.reset(new MuonRecoSF(ctx));
  sf_ele_id_low.reset(new uhh2::ElectronIdScaleFactors(ctx, Electron::tag::mvaEleID_Fall17_iso_V2_wp80, true));
  sf_ele_id_high.reset(new uhh2::ElectronIdScaleFactors(ctx, Electron::tag::mvaEleID_Fall17_noIso_V2_wp80, true));
  sf_ele_reco.reset(new uhh2::ElectronRecoScaleFactors(ctx, false, true));

  sf_ele_trigger.reset( new uhh2::ElecTriggerSF(ctx, "central", "eta_ptbins", year) );

  // dummies (needed to aviod set value errors)
  sf_muon_iso_low_dummy.reset(new uhh2::MuonIsoScaleFactors(ctx, boost::none, boost::none, boost::none, boost::none, boost::none, true));
  sf_muon_id_dummy.reset(new uhh2::MuonIdScaleFactors(ctx, boost::none, boost::none, boost::none, boost::none, true));
  sf_muon_trigger_dummy.reset(new uhh2::MuonTriggerScaleFactors(ctx, boost::none, boost::none, boost::none, boost::none, boost::none, true));
  sf_ele_id_dummy.reset(new uhh2::ElectronIdScaleFactors(ctx, boost::none, boost::none, boost::none, boost::none, true));
  sf_ele_reco_dummy.reset(new uhh2::ElectronRecoScaleFactors(ctx, boost::none, boost::none, boost::none, boost::none, true));

  // Selection modules
  Chi2_selection.reset(new Chi2Cut(ctx, 0., chi2_max));
  TTbarMatchable_selection.reset(new TTbarSemiLepMatchableSelection());
  Chi2CandidateMatched_selection.reset(new Chi2CandidateMatchedSelection(ctx));
  ZprimeTopTag_selection.reset(new ZprimeTopTagSelection(ctx));

  HEM_selection.reset(new HEMSelection(ctx)); // HEM issue in 2018, veto on leptons and jets

  Variables_module.reset(new Variables_NN(ctx, mode)); // variables for NN

 //  if(!isEleTriggerMeasurement) SystematicsModule.reset(new ZprimeSemiLeptonicSystematicsModule(ctx));

  // Top Taggers
  TopTaggerHOTVR.reset(new HOTVRTopTagger(ctx));
  TopTaggerDeepAK8.reset(new DeepAK8TopTagger(ctx));

  // TopTags veto
  TopTagVetoSelection.reset(new TopTag_VetoSelection(ctx, mode));

  // Zprime candidate builder
  CandidateBuilder.reset(new ZprimeCandidateBuilder(ctx, mode));

  // Zprime discriminators
  Chi2DiscriminatorZprime.reset(new ZprimeChi2Discriminator(ctx));
  h_is_zprime_reconstructed_chi2 = ctx.get_handle<bool>("is_zprime_reconstructed_chi2");
  CorrectMatchDiscriminatorZprime.reset(new ZprimeCorrectMatchDiscriminator(ctx));
  h_is_zprime_reconstructed_correctmatch = ctx.get_handle<bool>("is_zprime_reconstructed_correctmatch");
  h_BestZprimeCandidateChi2 = ctx.get_handle<ZprimeCandidate*>("ZprimeCandidateBestChi2");
  h_chi2 = ctx.declare_event_output<float> ("rec_chi2");

  h_weight = ctx.declare_event_output<float> ("weight");

  sel_1btag.reset(new NJetSelection(1, -1, id_btag));
  sel_2btag.reset(new NJetSelection(2,-1, id_btag));

  // Hist with Syst Variations
  DeltaY_SystVariations_DNN_output0.reset(new ZprimeSemiLeptonicSystematicsHists(ctx, "DeltaY_SystVariations_DNN_output0"));
  DeltaY_SystVariations_DNN_output1.reset(new ZprimeSemiLeptonicSystematicsHists(ctx, "DeltaY_SystVariations_DNN_output1"));
  DeltaY_SystVariations_DNN_output2.reset(new ZprimeSemiLeptonicSystematicsHists(ctx, "DeltaY_SystVariations_DNN_output2"));
  DeltaY_SystVariations_DNN_output0_TopTag.reset(new ZprimeSemiLeptonicSystematicsHists(ctx, "DeltaY_SystVariations_DNN_output0_TopTag"));
  DeltaY_SystVariations_DNN_output1_TopTag.reset(new ZprimeSemiLeptonicSystematicsHists(ctx, "DeltaY_SystVariations_DNN_output1_TopTag"));
  DeltaY_SystVariations_DNN_output2_TopTag.reset(new ZprimeSemiLeptonicSystematicsHists(ctx, "DeltaY_SystVariations_DNN_output2_TopTag"));
  DeltaY_SystVariations_DNN_output0_NoTopTag.reset(new ZprimeSemiLeptonicSystematicsHists(ctx, "DeltaY_SystVariations_DNN_output0_NoTopTag"));
  DeltaY_SystVariations_DNN_output1_NoTopTag.reset(new ZprimeSemiLeptonicSystematicsHists(ctx, "DeltaY_SystVariations_DNN_output1_NoTopTag"));
  DeltaY_SystVariations_DNN_output2_NoTopTag.reset(new ZprimeSemiLeptonicSystematicsHists(ctx, "DeltaY_SystVariations_DNN_output2_NoTopTag"));

  h_DeltaY_reco = ctx.declare_event_output<float> ("DeltaY_reco"); //-beren DeltaY
  h_DeltaY_reco_mass = ctx.declare_event_output<float> ("DeltaY_reco_mass"); //-beren DeltaY
  h_DeltaY_N_reco = ctx.declare_event_output<float> ("DeltaY_N_reco"); //-beren DeltaY
  h_DeltaY_P_reco = ctx.declare_event_output<float> ("DeltaY_P_reco"); //-beren DeltaY
  h_DeltaY_N_reco_nomass = ctx.declare_event_output<float> ("DeltaY_N_reco_nomass"); //-beren DeltaY
  h_DeltaY_P_reco_nomass = ctx.declare_event_output<float> ("DeltaY_P_reco_nomass"); //-beren DeltaY
  h_DeltaY_gen = ctx.declare_event_output<float> ("DeltaY_gen"); //-beren DeltaY 
  h_DeltaY_gen_mass = ctx.declare_event_output<float> ("DeltaY_gen_mass"); //-beren
  h_DeltaY_N_gen = ctx.declare_event_output<float> ("DeltaY_N_gen"); //-beren DeltaY
  h_DeltaY_N_gen_nomass = ctx.declare_event_output<float> ("DeltaY_N_gen_nomass"); //-beren DeltaY
  h_DeltaY_P_gen = ctx.declare_event_output<float> ("DeltaY_P_gen"); //-beren DeltaY
  h_DeltaY_P_gen_nomass = ctx.declare_event_output<float> ("DeltaY_P_gen_nomass"); //-beren DeltaY
  h_DeltaY_P_P = ctx.declare_event_output<float> ("DeltaY_P_P"); //-beren DeltaY
  h_DeltaY_P_N = ctx.declare_event_output<float> ("DeltaY_P_N"); //-beren DeltaY
  h_DeltaY_N_P = ctx.declare_event_output<float> ("DeltaY_N_P"); //-beren DeltaY
  h_DeltaY_N_N = ctx.declare_event_output<float> ("DeltaY_N_N"); //-beren DeltaY

  h_DeltaY_P_P_nomass_muon = ctx.declare_event_output<float> ("DeltaY_P_P_nomass_muon"); //-beren DeltaY
  h_DeltaY_P_N_nomass_muon = ctx.declare_event_output<float> ("DeltaY_P_N_nomass_muon"); //-beren DeltaY
  h_DeltaY_N_P_nomass_muon = ctx.declare_event_output<float> ("DeltaY_N_P_nomass_muon"); //-beren DeltaY
  h_DeltaY_N_N_nomass_muon = ctx.declare_event_output<float> ("DeltaY_N_N_nomass_muon"); //-beren DeltaY

  h_DeltaY_P_P_0_500_muon = ctx.declare_event_output<float> ("DeltaY_P_P_0_500_muon"); //-beren
  h_DeltaY_P_N_0_500_muon = ctx.declare_event_output<float> ("DeltaY_P_N_0_500_muon"); //-beren
  h_DeltaY_N_P_0_500_muon = ctx.declare_event_output<float> ("DeltaY_N_P_0_500_muon"); //-beren
  h_DeltaY_N_N_0_500_muon = ctx.declare_event_output<float> ("DeltaY_N_N_0_500_muon"); //-beren

  h_DeltaY_P_P_500_750_muon = ctx.declare_event_output<float> ("DeltaY_P_P_500_750_muon"); //-beren
  h_DeltaY_P_N_500_750_muon = ctx.declare_event_output<float> ("DeltaY_P_N_500_750_muon"); //-beren
  h_DeltaY_N_P_500_750_muon = ctx.declare_event_output<float> ("DeltaY_N_P_500_750_muon"); //-beren
  h_DeltaY_N_N_500_750_muon = ctx.declare_event_output<float> ("DeltaY_N_N_500_750_muon"); //-beren 

  h_DeltaY_P_P_750_1000_muon = ctx.declare_event_output<float> ("DeltaY_P_P_750_1000_muon"); //-beren
  h_DeltaY_P_N_750_1000_muon = ctx.declare_event_output<float> ("DeltaY_P_N_750_1000_muon"); //-beren
  h_DeltaY_N_P_750_1000_muon = ctx.declare_event_output<float> ("DeltaY_N_P_750_1000_muon"); //-beren
  h_DeltaY_N_N_750_1000_muon = ctx.declare_event_output<float> ("DeltaY_N_N_750_1000_muon"); //-beren

  h_DeltaY_P_P_1000_1500_muon = ctx.declare_event_output<float> ("DeltaY_P_P_1000_1500_muon"); //-beren
  h_DeltaY_P_N_1000_1500_muon = ctx.declare_event_output<float> ("DeltaY_P_N_1000_1500_muon"); //-beren
  h_DeltaY_N_P_1000_1500_muon = ctx.declare_event_output<float> ("DeltaY_N_P_1000_1500_muon"); //-beren
  h_DeltaY_N_N_1000_1500_muon = ctx.declare_event_output<float> ("DeltaY_N_N_1000_1500_muon"); //-beren 

  h_DeltaY_P_P_1500Inf_muon = ctx.declare_event_output<float> ("DeltaY_P_P_1500Inf_muon"); //-beren
  h_DeltaY_P_N_1500Inf_muon = ctx.declare_event_output<float> ("DeltaY_P_N_1500Inf_muon"); //-beren
  h_DeltaY_N_P_1500Inf_muon = ctx.declare_event_output<float> ("DeltaY_N_P_1500Inf_muon"); //-beren
  h_DeltaY_N_N_1500Inf_muon = ctx.declare_event_output<float> ("DeltaY_N_N_1500Inf_muon"); //-beren

  h_DeltaY_P_P_750Inf_muon = ctx.declare_event_output<float> ("DeltaY_P_P_750Inf_muon"); //-beren
  h_DeltaY_P_N_750Inf_muon = ctx.declare_event_output<float> ("DeltaY_P_N_750Inf_muon"); //-beren
  h_DeltaY_N_P_750Inf_muon = ctx.declare_event_output<float> ("DeltaY_N_P_750Inf_muon"); //-beren
  h_DeltaY_N_N_750Inf_muon = ctx.declare_event_output<float> ("DeltaY_N_N_750Inf_muon"); //-beren 

  ///=====//

  h_DeltaY_P_P_nomass_ele = ctx.declare_event_output<float> ("DeltaY_P_P_nomass_ele"); //-beren DeltaY
  h_DeltaY_P_N_nomass_ele = ctx.declare_event_output<float> ("DeltaY_P_N_nomass_ele"); //-beren DeltaY
  h_DeltaY_N_P_nomass_ele = ctx.declare_event_output<float> ("DeltaY_N_P_nomass_ele"); //-beren DeltaY
  h_DeltaY_N_N_nomass_ele = ctx.declare_event_output<float> ("DeltaY_N_N_nomass_ele"); //-beren DeltaY

  h_DeltaY_P_P_0_500_ele = ctx.declare_event_output<float> ("DeltaY_P_P_0_500_ele"); //-beren
  h_DeltaY_P_N_0_500_ele = ctx.declare_event_output<float> ("DeltaY_P_N_0_500_ele"); //-beren
  h_DeltaY_N_P_0_500_ele = ctx.declare_event_output<float> ("DeltaY_N_P_0_500_ele"); //-beren
  h_DeltaY_N_N_0_500_ele = ctx.declare_event_output<float> ("DeltaY_N_N_0_500_ele"); //-beren

  h_DeltaY_P_P_500_750_ele = ctx.declare_event_output<float> ("DeltaY_P_P_500_750_ele"); //-beren
  h_DeltaY_P_N_500_750_ele = ctx.declare_event_output<float> ("DeltaY_P_N_500_750_ele"); //-beren
  h_DeltaY_N_P_500_750_ele = ctx.declare_event_output<float> ("DeltaY_N_P_500_750_ele"); //-beren
  h_DeltaY_N_N_500_750_ele = ctx.declare_event_output<float> ("DeltaY_N_N_500_750_ele"); //-beren 

  h_DeltaY_P_P_750_1000_ele = ctx.declare_event_output<float> ("DeltaY_P_P_750_1000_ele"); //-beren
  h_DeltaY_P_N_750_1000_ele = ctx.declare_event_output<float> ("DeltaY_P_N_750_1000_ele"); //-beren
  h_DeltaY_N_P_750_1000_ele = ctx.declare_event_output<float> ("DeltaY_N_P_750_1000_ele"); //-beren
  h_DeltaY_N_N_750_1000_ele = ctx.declare_event_output<float> ("DeltaY_N_N_750_1000_ele"); //-beren

  h_DeltaY_P_P_1000_1500_ele = ctx.declare_event_output<float> ("DeltaY_P_P_1000_1500_ele"); //-beren
  h_DeltaY_P_N_1000_1500_ele = ctx.declare_event_output<float> ("DeltaY_P_N_1000_1500_ele"); //-beren
  h_DeltaY_N_P_1000_1500_ele = ctx.declare_event_output<float> ("DeltaY_N_P_1000_1500_ele"); //-beren
  h_DeltaY_N_N_1000_1500_ele = ctx.declare_event_output<float> ("DeltaY_N_N_1000_1500_ele"); //-beren 

  h_DeltaY_P_P_1500Inf_ele = ctx.declare_event_output<float> ("DeltaY_P_P_1500Inf_ele"); //-beren
  h_DeltaY_P_N_1500Inf_ele = ctx.declare_event_output<float> ("DeltaY_P_N_1500Inf_ele"); //-beren
  h_DeltaY_N_P_1500Inf_ele = ctx.declare_event_output<float> ("DeltaY_N_P_1500Inf_ele"); //-beren
  h_DeltaY_N_N_1500Inf_ele = ctx.declare_event_output<float> ("DeltaY_N_N_1500Inf_ele"); //-beren

  h_DeltaY_P_P_750Inf_ele = ctx.declare_event_output<float> ("DeltaY_P_P_750Inf_ele"); //-beren
  h_DeltaY_P_N_750Inf_ele = ctx.declare_event_output<float> ("DeltaY_P_N_750Inf_ele"); //-beren
  h_DeltaY_N_P_750Inf_ele = ctx.declare_event_output<float> ("DeltaY_N_P_750Inf_ele"); //-beren
  h_DeltaY_N_N_750Inf_ele = ctx.declare_event_output<float> ("DeltaY_N_N_750Inf_ele"); //-beren







  h_DeltaY_gen_ele = ctx.declare_event_output<float> ("DeltaY_gen_ele"); //-beren DeltaY 
  h_DeltaY_gen_muon = ctx.declare_event_output<float> ("DeltaY_gen_muon"); //-beren DeltaY 
  h_topQuarkCount = ctx.declare_event_output<float> ("topQuarkCount"); 

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
  h_DeltaR_leptonic_genparticle = ctx.declare_event_output<float> ("DeltaR_leptonic_genparticle"); //-beren DeltaY
  h_DeltaR_hadronic_genparticle = ctx.declare_event_output<float> ("DeltaR_hadronic_genparticle"); //-beren DeltaY

  h_not_reconstructed_muon = ctx.declare_event_output<float> ("not_reconstructed"); //-beren DeltaY
  h_not_reconstructed_0_500_muon = ctx.declare_event_output<float> ("not_reconstructed_0_500"); //-beren DeltaY
  h_not_reconstructed_500_750_muon = ctx.declare_event_output<float> ("not_reconstructed_500_750"); //-beren DeltaY
  h_not_reconstructed_750_1000_muon = ctx.declare_event_output<float> ("not_reconstructed_750_1000"); //-beren DeltaY
  h_not_reconstructed_1000_1500_muon = ctx.declare_event_output<float> ("not_reconstructed_1000_1500"); //-beren DeltaY
  h_not_reconstructed_1500Inf_muon = ctx.declare_event_output<float> ("not_reconstructed_1500Inf"); //-beren DeltaY

  h_not_reconstructed_ele = ctx.declare_event_output<float> ("not_reconstructed"); //-beren DeltaY
  h_not_reconstructed_0_500_ele = ctx.declare_event_output<float> ("not_reconstructed_0_500"); //-beren DeltaY
  h_not_reconstructed_500_750_ele = ctx.declare_event_output<float> ("not_reconstructed_500_750"); //-beren DeltaY
  h_not_reconstructed_750_1000_ele = ctx.declare_event_output<float> ("not_reconstructed_750_1000"); //-beren DeltaY
  h_not_reconstructed_1000_1500_ele = ctx.declare_event_output<float> ("not_reconstructed_1000_1500"); //-beren DeltaY
  h_not_reconstructed_1500Inf_ele = ctx.declare_event_output<float> ("not_reconstructed_1500Inf"); //-beren DeltaY
  
  h_MistagHists.reset(new ZprimeSemiLeptonicMistagHists(ctx, "Mistag"));
  
  // Book histograms
  vector<string> histogram_tags = {"BeforeCuts", "AfterBaseline", "AfterDNN", "AfterChi2", "Weights_Init", "Weights_HEM", "Weights_PU", "Weights_Lumi", "Weights_TopPt", "Weights_MCScale", "Weights_Prefiring", "Weights_TopTag_SF", "Weights_PS", "NLOCorrections", "IdMuon_SF", "IdEle_SF", "IsoMuon_SF", "RecoEle_SF", "MuonReco_SF", "TriggerMuon_SF", "BeforeBtagSF", "AfterBtagSF", "AfterCustomBtagSF", "TriggerEle_SF", "NNInputsBeforeReweight", "TopTagVeto", "DNN_output0_beforeChi2Cut", "DNN_output0_TopTag_beforeChi2Cut", "DNN_output0_NoTopTag_beforeChi2Cut", "DNN_output0","DNN_output1","DNN_output2","DNN_output0_TopTag","DNN_output1_TopTag","DNN_output2_TopTag","DNN_output0_NoTopTag","DNN_output1_NoTopTag","DNN_output2_NoTopTag", "DNN_output0_abs_thetastar_bin1", "DNN_output0_abs_thetastar_bin2", "DNN_output0_abs_thetastar_bin3", "DNN_output0_abs_thetastar_bin4", "DNN_output0_abs_thetastar_bin5", "DNN_output0_TopTag_abs_thetastar_bin1", "DNN_output0_TopTag_abs_thetastar_bin2", "DNN_output0_TopTag_abs_thetastar_bin3", "DNN_output0_TopTag_abs_thetastar_bin4", "DNN_output0_TopTag_abs_thetastar_bin5", "DNN_output0_NoTopTag_abs_thetastar_bin1", "DNN_output0_NoTopTag_abs_thetastar_bin2", "DNN_output0_NoTopTag_abs_thetastar_bin3", "DNN_output0_NoTopTag_abs_thetastar_bin4", "DNN_output0_NoTopTag_abs_thetastar_bin5", "DNN_output0_thetastar_bin1", "DNN_output0_thetastar_bin2", "DNN_output0_thetastar_bin3", "DNN_output0_thetastar_bin4", "DNN_output0_thetastar_bin5", "DNN_output0_thetastar_bin6", "DNN_output0_TopTag_thetastar_bin1", "DNN_output0_TopTag_thetastar_bin2", "DNN_output0_TopTag_thetastar_bin3", "DNN_output0_TopTag_thetastar_bin4", "DNN_output0_TopTag_thetastar_bin5", "DNN_output0_TopTag_thetastar_bin6", "DNN_output0_NoTopTag_thetastar_bin1", "DNN_output0_NoTopTag_thetastar_bin2", "DNN_output0_NoTopTag_thetastar_bin3", "DNN_output0_NoTopTag_thetastar_bin4", "DNN_output0_NoTopTag_thetastar_bin5", "DNN_output0_NoTopTag_thetastar_bin6",
   "DeltaY_gen_0_500", "DeltaY_gen_500_750","DeltaY_gen_750_1000","DeltaY_gen_1000_1500","DeltaY_gen_1500Inf", 
   "DeltaY_gen_N", "DeltaY_N_gen_0_500","DeltaY_N_gen_500_750", "DeltaY_N_gen_750_1000", "DeltaY_N_gen_1000_1500", "DeltaY_N_gen_1500Inf", 
   "DeltaY_gen_P", "DeltaY_P_gen_0_500", "DeltaY_P_gen_500_750", "DeltaY_P_gen_750_1000", "DeltaY_P_gen_1000_1500", "DeltaY_P_gen_1500Inf", 
   "DeltaY_reco_1500Inf_muon" ,"DeltaY_reco_1000_1500_muon" ,"DeltaY_reco_750_1000_muon" ,"DeltaY_reco_500_750_muon", "DeltaY_reco_0_500_muon",
   "DeltaY_reco_N_muon", "DeltaY_N_reco_1500Inf_muon" ,"DeltaY_N_reco_1000_1500_muon" ,"DeltaY_N_reco_750_1000_muon" ,"DeltaY_N_reco_500_750_muon", "DeltaY_N_reco_0_500_muon", 
   "DeltaY_reco_P_muon", "DeltaY_P_reco_1500Inf_muon" ,"DeltaY_P_reco_1000_1500_muon" ,"DeltaY_P_reco_750_1000_muon" ,"DeltaY_P_reco_500_750_muon", "DeltaY_P_reco_0_500_muon",
   "Not_reco_gens_muon", "Not_reco_gens_0_500_muon", "Not_reco_gens_500_750_muon", "Not_reco_gens_750_1000_muon", "Not_reco_gens_1000_1500_muon", "Not_reco_gens_1500Inf_muon",
   "DY_P_equal_gen_muon", "DY_N_equal_gen_muon" , "DY_P_equal_reco_muon", "DY_N_equal_reco_muon",
   "DY_P_P_muon", "DY_P_P_0_500_muon", "DY_P_P_500_750_muon", "DY_P_P_750_1000_muon", "DY_P_P_1000_1500_muon", "DY_P_P_1500Inf_muon", "DY_P_P_750Inf_muon", 
   "DY_P_N_muon", "DY_P_N_0_500_muon", "DY_P_N_500_750_muon", "DY_P_N_750_1000_muon", "DY_P_N_1000_1500_muon", "DY_P_N_1500Inf_muon", "DY_P_N_750Inf_muon", 
   "DY_N_P_muon", "DY_N_P_0_500_muon", "DY_N_P_500_750_muon", "DY_N_P_750_1000_muon", "DY_N_P_1000_1500_muon", "DY_N_P_1500Inf_muon", "DY_N_P_750Inf_muon", 
   "DY_N_N_muon", "DY_N_N_0_500_muon", "DY_N_N_500_750_muon", "DY_N_N_750_1000_muon", "DY_N_N_1000_1500_muon", "DY_N_N_1500Inf_muon", "DY_N_N_750Inf_muon", 
   "DY_0_500_recogenmatch_muon", "DY_Match_N_N_0_500_muon", "DY_Match_N_P_0_500_muon", "DY_Match_P_N_0_500_muon", "DY_Match_P_P_0_500_muon", "UnMatched_0_500_muon", 
   "DY_500_750_recogenmatch_muon", "DY_Match_N_N_500_750_muon", "DY_Match_N_P_500_750_muon", "DY_Match_P_N_500_750_muon", "DY_Match_P_P_500_750_muon", "UnMatched_500_750_muon", 
   "DY_750_1000_recogenmatch_muon", "DY_Match_N_N_750_1000_muon", "DY_Match_N_P_750_1000_muon", "DY_Match_P_N_750_1000_muon", "DY_Match_P_P_750_1000_muon", "UnMatched_750_1000_muon", 
   "DY_1000_1500_recogenmatch_muon", "DY_Match_N_N_1000_1500_muon", "DY_Match_N_P_1000_1500_muon", "DY_Match_P_N_1000_1500_muon", "DY_Match_P_P_1000_1500_muon", "UnMatched_1000_1500_muon", 
   "DY_1500Inf_recogenmatch_muon", "DY_Match_N_N_1500Inf_muon", "DY_Match_N_P_1500Inf_muon", "DY_Match_P_N_1500Inf_muon", "DY_Match_P_P_1500Inf_muon", "UnMatched_1500Inf_muon", 
   "DY_Mass_0_500_NOT_reco_muon", "DY_Mass_500_750_NOT_reco_muon", "DY_Mass_750_1000_NOT_reco_muon", "DY_Mass_1000_1500_NOT_reco_muon", "DY_Mass_1500Inf_NOT_reco_muon",  
   "GenTop",
   "DeltaY_reco_1500Inf_ele" ,"DeltaY_reco_1000_1500_ele" ,"DeltaY_reco_750_1000_ele" ,"DeltaY_reco_500_750_ele", "DeltaY_reco_0_500_ele",
   "DeltaY_reco_N_ele", "DeltaY_N_reco_1500Inf_ele" ,"DeltaY_N_reco_1000_1500_ele" ,"DeltaY_N_reco_750_1000_ele" ,"DeltaY_N_reco_500_750_ele", "DeltaY_N_reco_0_500_ele", 
   "DeltaY_reco_P_ele", "DeltaY_P_reco_1500Inf_ele" ,"DeltaY_P_reco_1000_1500_ele" ,"DeltaY_P_reco_750_1000_ele" ,"DeltaY_P_reco_500_750_ele", "DeltaY_P_reco_0_500_ele",
   "Not_reco_gens_ele", "Not_reco_gens_0_500_ele", "Not_reco_gens_500_750_ele", "Not_reco_gens_750_1000_ele", "Not_reco_gens_1000_1500_ele", "Not_reco_gens_1500Inf_ele",
   "DY_P_equal_gen_ele", "DY_N_equal_gen_ele" , "DY_P_equal_reco_ele", "DY_N_equal_reco_ele",
   "DY_P_P_ele", "DY_P_P_0_500_ele", "DY_P_P_500_750_ele", "DY_P_P_750_1000_ele", "DY_P_P_1000_1500_ele", "DY_P_P_1500Inf_ele", "DY_P_P_750Inf_ele", 
   "DY_P_N_ele", "DY_P_N_0_500_ele", "DY_P_N_500_750_ele", "DY_P_N_750_1000_ele", "DY_P_N_1000_1500_ele", "DY_P_N_1500Inf_ele", "DY_P_N_750Inf_ele", 
   "DY_N_P_ele", "DY_N_P_0_500_ele", "DY_N_P_500_750_ele", "DY_N_P_750_1000_ele", "DY_N_P_1000_1500_ele", "DY_N_P_1500Inf_ele", "DY_N_P_750Inf_ele", 
   "DY_N_N_ele", "DY_N_N_0_500_ele", "DY_N_N_500_750_ele", "DY_N_N_750_1000_ele", "DY_N_N_1000_1500_ele", "DY_N_N_1500Inf_ele", "DY_N_N_750Inf_ele", 
   "DY_0_500_recogenmatch_ele", "DY_Match_N_N_0_500_ele", "DY_Match_N_P_0_500_ele", "DY_Match_P_N_0_500_ele", "DY_Match_P_P_0_500_ele", "UnMatched_0_500_ele", 
   "DY_500_750_recogenmatch_ele", "DY_Match_N_N_500_750_ele", "DY_Match_N_P_500_750_ele", "DY_Match_P_N_500_750_ele", "DY_Match_P_P_500_750_ele", "UnMatched_500_750_ele", 
   "DY_750_1000_recogenmatch_ele", "DY_Match_N_N_750_1000_ele", "DY_Match_N_P_750_1000_ele", "DY_Match_P_N_750_1000_ele", "DY_Match_P_P_750_1000_ele", "UnMatched_750_1000_ele", 
   "DY_1000_1500_recogenmatch_ele", "DY_Match_N_N_1000_1500_ele", "DY_Match_N_P_1000_1500_ele", "DY_Match_P_N_1000_1500_ele", "DY_Match_P_P_1000_1500_ele", "UnMatched_1000_1500_ele", 
   "DY_1500Inf_recogenmatch_ele", "DY_Match_N_N_1500Inf_ele", "DY_Match_N_P_1500Inf_ele", "DY_Match_P_N_1500Inf_ele", "DY_Match_P_P_1500Inf_ele", "UnMatched_1500Inf_ele", 
   "DY_Mass_0_500_NOT_reco_ele", "DY_Mass_500_750_NOT_reco_ele", "DY_Mass_750_1000_NOT_reco_ele", "DY_Mass_1000_1500_NOT_reco_ele", "DY_Mass_1500Inf_NOT_reco_ele"
  };
  // vector<string> histogram_tags = {"BeforeCuts", "AfterBaseline", "AfterDNN", "AfterChi2" };
  book_histograms(ctx, histogram_tags);

  h_MulticlassNN_output.reset(new ZprimeSemiLeptonicMulticlassNNHists(ctx, "MulticlassNN"));

  lumihists_Weights_Init.reset(new LuminosityHists(ctx, "Lumi_Weights_Init"));
  lumihists_Weights_PU.reset(new LuminosityHists(ctx, "Lumi_Weights_PU"));
  lumihists_Weights_Lumi.reset(new LuminosityHists(ctx, "Lumi_Weights_Lumi"));
  lumihists_Weights_TopPt.reset(new LuminosityHists(ctx, "Lumi_Weights_TopPt"));
  lumihists_Weights_MCScale.reset(new LuminosityHists(ctx, "Lumi_Weights_MCScale"));
  lumihists_Weights_PS.reset(new LuminosityHists(ctx, "Lumi_Weights_PS"));
  lumihists_Chi2.reset(new LuminosityHists(ctx, "Lumi_Chi2"));

  if(isMC){
    TString sample_name = "";
    vector<TString> names = {"ST", "WJets", "DY", "QCD", "ALP_ttbar_signal", "ALP_ttbar_interference", "HscalarToTTTo1L1Nu2J_m365_w36p5_res", "HscalarToTTTo1L1Nu2J_m400_w40p0_res", "HscalarToTTTo1L1Nu2J_m500_w50p0_res", "HscalarToTTTo1L1Nu2J_m600_w60p0_res", "HscalarToTTTo1L1Nu2J_m800_w80p0_res", "HscalarToTTTo1L1Nu2J_m1000_w100p0_res", "HscalarToTTTo1L1Nu2J_m365_w36p5_int_pos", "HscalarToTTTo1L1Nu2J_m400_w40p0_int_pos", "HscalarToTTTo1L1Nu2J_m500_w50p0_int_pos", "HscalarToTTTo1L1Nu2J_m600_w60p0_int_pos", "HscalarToTTTo1L1Nu2J_m800_w80p0_int_pos", "HscalarToTTTo1L1Nu2J_m1000_w100p0_int_pos", "HscalarToTTTo1L1Nu2J_m365_w36p5_int_neg", "HscalarToTTTo1L1Nu2J_m400_w40p0_int_neg", "HscalarToTTTo1L1Nu2J_m500_w50p0_int_neg", "HscalarToTTTo1L1Nu2J_m600_w60p0_int_neg", "HscalarToTTTo1L1Nu2J_m800_w80p0_int_neg", "HscalarToTTTo1L1Nu2J_m1000_w100p0_int_neg", "HpseudoToTTTo1L1Nu2J_m365_w36p5_res", "HpseudoToTTTo1L1Nu2J_m400_w40p0_res", "HpseudoToTTTo1L1Nu2J_m500_w50p0_res", "HpseudoToTTTo1L1Nu2J_m600_w60p0_res", "HpseudoToTTTo1L1Nu2J_m800_w80p0_res", "HpseudoToTTTo1L1Nu2J_m1000_w100p0_res", "HpseudoToTTTo1L1Nu2J_m365_w36p5_int_pos", "HpseudoToTTTo1L1Nu2J_m400_w40p0_int_pos", "HpseudoToTTTo1L1Nu2J_m500_w50p0_int_pos", "HpseudoToTTTo1L1Nu2J_m600_w60p0_int_pos", "HpseudoToTTTo1L1Nu2J_m800_w80p0_int_pos", "HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_pos", "HpseudoToTTTo1L1Nu2J_m365_w36p5_int_neg", "HpseudoToTTTo1L1Nu2J_m400_w40p0_int_neg", "HpseudoToTTTo1L1Nu2J_m500_w50p0_int_neg", "HpseudoToTTTo1L1Nu2J_m600_w60p0_int_neg", "HpseudoToTTTo1L1Nu2J_m800_w80p0_int_neg", "HpseudoToTTTo1L1Nu2J_m1000_w100p0_int_neg", "HscalarToTTTo1L1Nu2J_m365_w91p25_res", "HscalarToTTTo1L1Nu2J_m400_w100p0_res", "HscalarToTTTo1L1Nu2J_m500_w125p0_res", "HscalarToTTTo1L1Nu2J_m600_w150p0_res", "HscalarToTTTo1L1Nu2J_m800_w200p0_res", "HscalarToTTTo1L1Nu2J_m1000_w250p0_res", "HscalarToTTTo1L1Nu2J_m365_w91p25_int_pos", "HscalarToTTTo1L1Nu2J_m400_w100p0_int_pos", "HscalarToTTTo1L1Nu2J_m500_w125p0_int_pos", "HscalarToTTTo1L1Nu2J_m600_w150p0_int_pos", "HscalarToTTTo1L1Nu2J_m800_w200p0_int_pos", "HscalarToTTTo1L1Nu2J_m1000_w250p0_int_pos", "HscalarToTTTo1L1Nu2J_m365_w91p25_int_neg", "HscalarToTTTo1L1Nu2J_m400_w100p0_int_neg", "HscalarToTTTo1L1Nu2J_m500_w125p0_int_neg", "HscalarToTTTo1L1Nu2J_m600_w150p0_int_neg", "HscalarToTTTo1L1Nu2J_m800_w200p0_int_neg", "HscalarToTTTo1L1Nu2J_m1000_w250p0_int_neg", "HpseudoToTTTo1L1Nu2J_m365_w91p25_res", "HpseudoToTTTo1L1Nu2J_m400_w100p0_res", "HpseudoToTTTo1L1Nu2J_m500_w125p0_res", "HpseudoToTTTo1L1Nu2J_m600_w150p0_res", "HpseudoToTTTo1L1Nu2J_m800_w200p0_res", "HpseudoToTTTo1L1Nu2J_m1000_w250p0_res", "HpseudoToTTTo1L1Nu2J_m365_w91p25_int_pos", "HpseudoToTTTo1L1Nu2J_m400_w100p0_int_pos", "HpseudoToTTTo1L1Nu2J_m500_w125p0_int_pos", "HpseudoToTTTo1L1Nu2J_m600_w150p0_int_pos", "HpseudoToTTTo1L1Nu2J_m800_w200p0_int_pos", "HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_pos", "HpseudoToTTTo1L1Nu2J_m365_w91p25_int_neg", "HpseudoToTTTo1L1Nu2J_m400_w100p0_int_neg", "HpseudoToTTTo1L1Nu2J_m500_w125p0_int_neg", "HpseudoToTTTo1L1Nu2J_m600_w150p0_int_neg", "HpseudoToTTTo1L1Nu2J_m800_w200p0_int_neg", "HpseudoToTTTo1L1Nu2J_m1000_w250p0_int_neg", "HscalarToTTTo1L1Nu2J_m365_w9p125_res", "HscalarToTTTo1L1Nu2J_m400_w10p0_res", "HscalarToTTTo1L1Nu2J_m500_w12p5_res", "HscalarToTTTo1L1Nu2J_m600_w15p0_res", "HscalarToTTTo1L1Nu2J_m800_w20p0_res", "HscalarToTTTo1L1Nu2J_m1000_w25p0_res", "HscalarToTTTo1L1Nu2J_m365_w9p125_int_pos", "HscalarToTTTo1L1Nu2J_m400_w10p0_int_pos", "HscalarToTTTo1L1Nu2J_m500_w12p5_int_pos", "HscalarToTTTo1L1Nu2J_m600_w15p0_int_pos", "HscalarToTTTo1L1Nu2J_m800_w20p0_int_pos", "HscalarToTTTo1L1Nu2J_m1000_w25p0_int_pos", "HscalarToTTTo1L1Nu2J_m365_w9p125_int_neg", "HscalarToTTTo1L1Nu2J_m400_w10p0_int_neg", "HscalarToTTTo1L1Nu2J_m500_w12p5_int_neg", "HscalarToTTTo1L1Nu2J_m600_w15p0_int_neg", "HscalarToTTTo1L1Nu2J_m800_w20p0_int_neg", "HscalarToTTTo1L1Nu2J_m1000_w25p0_int_neg", "HpseudoToTTTo1L1Nu2J_m365_w9p125_res", "HpseudoToTTTo1L1Nu2J_m400_w10p0_res", "HpseudoToTTTo1L1Nu2J_m500_w12p5_res", "HpseudoToTTTo1L1Nu2J_m600_w15p0_res", "HpseudoToTTTo1L1Nu2J_m800_w20p0_res", "HpseudoToTTTo1L1Nu2J_m1000_w25p0_res", "HpseudoToTTTo1L1Nu2J_m365_w9p125_int_pos", "HpseudoToTTTo1L1Nu2J_m400_w10p0_int_pos", "HpseudoToTTTo1L1Nu2J_m500_w12p5_int_pos", "HpseudoToTTTo1L1Nu2J_m600_w15p0_int_pos", "HpseudoToTTTo1L1Nu2J_m800_w20p0_int_pos", "HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_pos", "HpseudoToTTTo1L1Nu2J_m365_w9p125_int_neg", "HpseudoToTTTo1L1Nu2J_m400_w10p0_int_neg", "HpseudoToTTTo1L1Nu2J_m500_w12p5_int_neg", "HpseudoToTTTo1L1Nu2J_m600_w15p0_int_neg", "HpseudoToTTTo1L1Nu2J_m800_w20p0_int_neg", "HpseudoToTTTo1L1Nu2J_m1000_w25p0_int_neg", "RSGluonToTT_M-500", "RSGluonToTT_M-1000", "RSGluonToTT_M-1500", "RSGluonToTT_M-2000", "RSGluonToTT_M-2500", "RSGluonToTT_M-3000", "RSGluonToTT_M-3500", "RSGluonToTT_M-4000", "RSGluonToTT_M-4500", "RSGluonToTT_M-5000", "RSGluonToTT_M-5500", "RSGluonToTT_M-6000", "ZPrimeToTT_M400_W40", "ZPrimeToTT_M500_W50", "ZPrimeToTT_M600_W60", "ZPrimeToTT_M700_W70", "ZPrimeToTT_M800_W80", "ZPrimeToTT_M900_W90", "ZPrimeToTT_M1000_W100", "ZPrimeToTT_M1200_W120", "ZPrimeToTT_M1400_W140", "ZPrimeToTT_M1600_W160", "ZPrimeToTT_M1800_W180", "ZPrimeToTT_M2000_W200", "ZPrimeToTT_M2500_W250", "ZPrimeToTT_M3000_W300", "ZPrimeToTT_M3500_W350", "ZPrimeToTT_M4000_W400", "ZPrimeToTT_M4500_W450", "ZPrimeToTT_M5000_W500", "ZPrimeToTT_M6000_W600",  "ZPrimeToTT_M7000_W700", "ZPrimeToTT_M8000_W800", "ZPrimeToTT_M9000_W900", "ZPrimeToTT_M400_W120", "ZPrimeToTT_M500_W150", "ZPrimeToTT_M600_W180", "ZPrimeToTT_M700_W210", "ZPrimeToTT_M800_W240", "ZPrimeToTT_M900_W270", "ZPrimeToTT_M1000_W300", "ZPrimeToTT_M1200_W360", "ZPrimeToTT_M1400_W420", "ZPrimeToTT_M1600_W480", "ZPrimeToTT_M1800_W540", "ZPrimeToTT_M2000_W600", "ZPrimeToTT_M2500_W750", "ZPrimeToTT_M3000_W900", "ZPrimeToTT_M3500_W1050", "ZPrimeToTT_M4000_W1200", "ZPrimeToTT_M4500_W1350", "ZPrimeToTT_M5000_W1500", "ZPrimeToTT_M6000_W1800", "ZPrimeToTT_M7000_W2100", "ZPrimeToTT_M8000_W2400", "ZPrimeToTT_M9000_W2700", "ZPrimeToTT_M400_W4", "ZPrimeToTT_M500_W5", "ZPrimeToTT_M600_W6", "ZPrimeToTT_M700_W7", "ZPrimeToTT_M800_W8", "ZPrimeToTT_M900_W9", "ZPrimeToTT_M1000_W10", "ZPrimeToTT_M1200_W12", "ZPrimeToTT_M1400_W14", "ZPrimeToTT_M1600_W16", "ZPrimeToTT_M1800_W18", "ZPrimeToTT_M2000_W20", "ZPrimeToTT_M2500_W25", "ZPrimeToTT_M3000_W30", "ZPrimeToTT_M3500_W35", "ZPrimeToTT_M4000_W40", "ZPrimeToTT_M4500_W45", "ZPrimeToTT_M5000_W50", "ZPrimeToTT_M6000_W60", "ZPrimeToTT_M7000_W70", "ZPrimeToTT_M8000_W80", "ZPrimeToTT_M9000_W90"};

    for(unsigned int i=0; i<names.size(); i++){
      if( ctx.get("dataset_version").find(names.at(i)) != std::string::npos ) sample_name = names.at(i);
    }
    if( (ctx.get("dataset_version").find("TTToHadronic") != std::string::npos) || (ctx.get("dataset_version").find("TTToSemiLeptonic") != std::string::npos) || (ctx.get("dataset_version").find("TTTo2L2Nu") != std::string::npos) ) sample_name = "TTbar";
    if( (ctx.get("dataset_version").find("WW") != std::string::npos) || (ctx.get("dataset_version").find("ZZ") != std::string::npos) || (ctx.get("dataset_version").find("WZ") != std::string::npos) ) sample_name = "Diboson";

    if(isMuon){
      TFile* f_btag2Dsf_muon = new TFile("/nfs/dust/cms/user/deleokse/RunII_106_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/macros/src/files_BTagSF/customBtagSF_muon_"+year+".root");
      ratio_hist_muon = (TH2F*)f_btag2Dsf_muon->Get("N_Jets_vs_HT_" + sample_name);
      ratio_hist_muon->SetDirectory(0);
    }
    else if(!isMuon){
      TFile* f_btag2Dsf_ele = new TFile("/nfs/dust/cms/user/deleokse/RunII_106_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/macros/src/files_BTagSF/customBtagSF_electron_"+year+".root");
      ratio_hist_ele = (TH2F*)f_btag2Dsf_ele->Get("N_Jets_vs_HT_" + sample_name);
      ratio_hist_ele->SetDirectory(0);
    }
  }

  h_Ak4_j1_E   = ctx.get_handle<float>("Ak4_j1_E");
  h_Ak4_j1_eta = ctx.get_handle<float>("Ak4_j1_eta");
  h_Ak4_j1_m   = ctx.get_handle<float>("Ak4_j1_m");
  h_Ak4_j1_phi = ctx.get_handle<float>("Ak4_j1_phi");
  h_Ak4_j1_pt  = ctx.get_handle<float>("Ak4_j1_pt");
  h_Ak4_j1_deepjetbscore  = ctx.get_handle<float>("Ak4_j1_deepjetbscore");

  h_Ak4_j2_E   = ctx.get_handle<float>("Ak4_j2_E");
  h_Ak4_j2_eta = ctx.get_handle<float>("Ak4_j2_eta");
  h_Ak4_j2_m   = ctx.get_handle<float>("Ak4_j2_m");
  h_Ak4_j2_phi = ctx.get_handle<float>("Ak4_j2_phi");
  h_Ak4_j2_pt  = ctx.get_handle<float>("Ak4_j2_pt");
  h_Ak4_j2_deepjetbscore  = ctx.get_handle<float>("Ak4_j2_deepjetbscore");

  h_Ak4_j3_E   = ctx.get_handle<float>("Ak4_j3_E");
  h_Ak4_j3_eta = ctx.get_handle<float>("Ak4_j3_eta");
  h_Ak4_j3_m   = ctx.get_handle<float>("Ak4_j3_m");
  h_Ak4_j3_phi = ctx.get_handle<float>("Ak4_j3_phi");
  h_Ak4_j3_pt  = ctx.get_handle<float>("Ak4_j3_pt");
  h_Ak4_j3_deepjetbscore  = ctx.get_handle<float>("Ak4_j3_deepjetbscore");

  h_Ak4_j4_E   = ctx.get_handle<float>("Ak4_j4_E");
  h_Ak4_j4_eta = ctx.get_handle<float>("Ak4_j4_eta");
  h_Ak4_j4_m   = ctx.get_handle<float>("Ak4_j4_m");
  h_Ak4_j4_phi = ctx.get_handle<float>("Ak4_j4_phi");
  h_Ak4_j4_pt  = ctx.get_handle<float>("Ak4_j4_pt");
  h_Ak4_j4_deepjetbscore  = ctx.get_handle<float>("Ak4_j4_deepjetbscore");

  h_Ak4_j5_E   = ctx.get_handle<float>("Ak4_j5_E");
  h_Ak4_j5_eta = ctx.get_handle<float>("Ak4_j5_eta");
  h_Ak4_j5_m   = ctx.get_handle<float>("Ak4_j5_m");
  h_Ak4_j5_phi = ctx.get_handle<float>("Ak4_j5_phi");
  h_Ak4_j5_pt  = ctx.get_handle<float>("Ak4_j5_pt");
  h_Ak4_j5_deepjetbscore  = ctx.get_handle<float>("Ak4_j5_deepjetbscore");

  h_Ele_E    = ctx.get_handle<float>("Ele_E");
  h_Ele_eta  = ctx.get_handle<float>("Ele_eta");
  h_Ele_phi  = ctx.get_handle<float>("Ele_phi");
  h_Ele_pt   = ctx.get_handle<float>("Ele_pt");

  h_MET_phi = ctx.get_handle<float>("MET_phi");
  h_MET_pt = ctx.get_handle<float>("MET_pt");

  h_Mu_E    = ctx.get_handle<float>("Mu_E");
  h_Mu_eta  = ctx.get_handle<float>("Mu_eta");
  h_Mu_phi  = ctx.get_handle<float>("Mu_phi");
  h_Mu_pt   = ctx.get_handle<float>("Mu_pt");

  h_N_Ak4 = ctx.get_handle<float>("N_Ak4");

  h_Ak8_j1_E     = ctx.get_handle<float>("Ak8_j1_E");
  h_Ak8_j1_eta   = ctx.get_handle<float>("Ak8_j1_eta");
  h_Ak8_j1_mSD   = ctx.get_handle<float>("Ak8_j1_mSD");
  h_Ak8_j1_phi   = ctx.get_handle<float>("Ak8_j1_phi");
  h_Ak8_j1_pt    = ctx.get_handle<float>("Ak8_j1_pt");
  h_Ak8_j1_tau21 = ctx.get_handle<float>("Ak8_j1_tau21");
  h_Ak8_j1_tau32 = ctx.get_handle<float>("Ak8_j1_tau32");

  h_Ak8_j2_E     = ctx.get_handle<float>("Ak8_j2_E");
  h_Ak8_j2_eta   = ctx.get_handle<float>("Ak8_j2_eta");
  h_Ak8_j2_mSD   = ctx.get_handle<float>("Ak8_j2_mSD");
  h_Ak8_j2_phi   = ctx.get_handle<float>("Ak8_j2_phi");
  h_Ak8_j2_pt    = ctx.get_handle<float>("Ak8_j2_pt");
  h_Ak8_j2_tau21 = ctx.get_handle<float>("Ak8_j2_tau21");
  h_Ak8_j2_tau32 = ctx.get_handle<float>("Ak8_j2_tau32");

  h_Ak8_j3_E     = ctx.get_handle<float>("Ak8_j3_E");
  h_Ak8_j3_eta   = ctx.get_handle<float>("Ak8_j3_eta");
  h_Ak8_j3_mSD   = ctx.get_handle<float>("Ak8_j3_mSD");
  h_Ak8_j3_phi   = ctx.get_handle<float>("Ak8_j3_phi");
  h_Ak8_j3_pt    = ctx.get_handle<float>("Ak8_j3_pt");
  h_Ak8_j3_tau21 = ctx.get_handle<float>("Ak8_j3_tau21");
  h_Ak8_j3_tau32 = ctx.get_handle<float>("Ak8_j3_tau32");

  h_N_Ak8 = ctx.get_handle<float>("N_Ak8");

  h_NNoutput = ctx.get_handle<std::vector<tensorflow::Tensor>>("NNoutput");
  h_NNoutput0 = ctx.declare_event_output<double>("NNoutput0");
  h_NNoutput1 = ctx.declare_event_output<double>("NNoutput1");
  h_NNoutput2 = ctx.declare_event_output<double>("NNoutput2");
  //Only Ele or Mu variables!!
  NNModule.reset( new NeuralNetworkModule(ctx, "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/KerasNN/NN_DeepAK8_UL17_muon/model.pb", "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/KerasNN/NN_DeepAK8_UL17_muon/model.config.pbtxt"));
}

/*
██████  ██████   ██████   ██████ ███████ ███████ ███████
██   ██ ██   ██ ██    ██ ██      ██      ██      ██
██████  ██████  ██    ██ ██      █████   ███████ ███████
██      ██   ██ ██    ██ ██      ██           ██      ██
██      ██   ██  ██████   ██████ ███████ ███████ ███████
*/

bool ZprimeAnalysisModule_applyNN::process(uhh2::Event& event){

  if(debug) cout << "++++++++++++ NEW EVENT ++++++++++++++" << endl;
  if(debug) cout << " run.event: " << event.run << ". " << event.event << endl;
  // Initialize reco flags with false
  event.set(h_is_zprime_reconstructed_chi2, false);
  event.set(h_is_zprime_reconstructed_correctmatch, false);
  event.set(h_chi2,-100);
  event.set(h_weight,-100);

  event.set(h_NNoutput0, 0);
  event.set(h_NNoutput1, 0);
  event.set(h_NNoutput2, 0);

  event.set(h_topQuarkCount,-100);

  event.set(h_DeltaY_reco,-100); //-beren
  event.set(h_DeltaY_reco_mass,-100); //-beren
  event.set(h_DeltaY_N_reco,-100); //-beren
  event.set(h_DeltaY_P_reco,-100); //-beren
  event.set(h_DeltaY_N_reco_nomass,-100); //-beren
  event.set(h_DeltaY_P_reco_nomass,-100); //-beren
  event.set(h_DeltaY_gen,-100); //-beren
  event.set(h_DeltaY_gen_mass,-100); //-beren
  event.set(h_DeltaY_N_gen,-100); //-beren
  event.set(h_DeltaY_P_gen,-100); //-beren
  event.set(h_DeltaY_P_gen_nomass,-100); //-beren
  event.set(h_DeltaY_N_gen_nomass,-100); //-beren
  event.set(h_DeltaY_P_P,-100); //-beren
  event.set(h_DeltaY_P_N,-100); //-beren
  event.set(h_DeltaY_N_P,-100); //-beren
  event.set(h_DeltaY_N_N,-100); //-beren


  event.set(h_DeltaY_P_P_nomass_muon,-100); //-beren
  event.set(h_DeltaY_P_N_nomass_muon,-100); //-beren
  event.set(h_DeltaY_N_P_nomass_muon,-100); //-beren
  event.set(h_DeltaY_N_N_nomass_muon,-100); //-beren

  event.set(h_DeltaY_P_P_0_500_muon,-100); //-beren
  event.set(h_DeltaY_P_N_0_500_muon,-100); //-beren
  event.set(h_DeltaY_N_P_0_500_muon,-100); //-beren
  event.set(h_DeltaY_N_N_0_500_muon,-100); //-beren

  event.set(h_DeltaY_P_P_500_750_muon,-100); //-beren
  event.set(h_DeltaY_P_N_500_750_muon,-100); //-beren
  event.set(h_DeltaY_N_P_500_750_muon,-100); //-beren
  event.set(h_DeltaY_N_N_500_750_muon,-100); //-beren

  event.set(h_DeltaY_P_P_750_1000_muon,-100); //-beren
  event.set(h_DeltaY_P_N_750_1000_muon,-100); //-beren
  event.set(h_DeltaY_N_P_750_1000_muon,-100); //-beren
  event.set(h_DeltaY_N_N_750_1000_muon,-100); //-beren

  event.set(h_DeltaY_P_P_1000_1500_muon,-100); //-beren
  event.set(h_DeltaY_P_N_1000_1500_muon,-100); //-beren
  event.set(h_DeltaY_N_P_1000_1500_muon,-100); //-beren
  event.set(h_DeltaY_N_N_1000_1500_muon,-100); //-beren

  event.set(h_DeltaY_P_P_1500Inf_muon,-100); //-beren
  event.set(h_DeltaY_P_N_1500Inf_muon,-100); //-beren
  event.set(h_DeltaY_N_P_1500Inf_muon,-100); //-beren
  event.set(h_DeltaY_N_N_1500Inf_muon,-100); //-beren

  event.set(h_DeltaY_P_P_750Inf_muon,-100); //-beren
  event.set(h_DeltaY_P_N_750Inf_muon,-100); //-beren
  event.set(h_DeltaY_N_P_750Inf_muon,-100); //-beren
  event.set(h_DeltaY_N_N_750Inf_muon,-100); //-beren


  event.set(h_DeltaY_P_P_nomass_ele,-100); //-beren
  event.set(h_DeltaY_P_N_nomass_ele,-100); //-beren
  event.set(h_DeltaY_N_P_nomass_ele,-100); //-beren
  event.set(h_DeltaY_N_N_nomass_ele,-100); //-beren

  event.set(h_DeltaY_P_P_0_500_ele,-100); //-beren
  event.set(h_DeltaY_P_N_0_500_ele,-100); //-beren
  event.set(h_DeltaY_N_P_0_500_ele,-100); //-beren
  event.set(h_DeltaY_N_N_0_500_ele,-100); //-beren

  event.set(h_DeltaY_P_P_500_750_ele,-100); //-beren
  event.set(h_DeltaY_P_N_500_750_ele,-100); //-beren
  event.set(h_DeltaY_N_P_500_750_ele,-100); //-beren
  event.set(h_DeltaY_N_N_500_750_ele,-100); //-beren

  event.set(h_DeltaY_P_P_750_1000_ele,-100); //-beren
  event.set(h_DeltaY_P_N_750_1000_ele,-100); //-beren
  event.set(h_DeltaY_N_P_750_1000_ele,-100); //-beren
  event.set(h_DeltaY_N_N_750_1000_ele,-100); //-beren

  event.set(h_DeltaY_P_P_1000_1500_ele,-100); //-beren
  event.set(h_DeltaY_P_N_1000_1500_ele,-100); //-beren
  event.set(h_DeltaY_N_P_1000_1500_ele,-100); //-beren
  event.set(h_DeltaY_N_N_1000_1500_ele,-100); //-beren

  event.set(h_DeltaY_P_P_1500Inf_ele,-100); //-beren
  event.set(h_DeltaY_P_N_1500Inf_ele,-100); //-beren
  event.set(h_DeltaY_N_P_1500Inf_ele,-100); //-beren
  event.set(h_DeltaY_N_N_1500Inf_ele,-100); //-beren

  event.set(h_DeltaY_P_P_750Inf_ele,-100); //-beren
  event.set(h_DeltaY_P_N_750Inf_ele,-100); //-beren
  event.set(h_DeltaY_N_P_750Inf_ele,-100); //-beren
  event.set(h_DeltaY_N_N_750Inf_ele,-100); //-beren


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
  event.set(h_DeltaR_hadronic_genparticle, -100); //-beren
  event.set(h_DeltaR_leptonic_genparticle, -100); //-beren

  event.set(h_not_reconstructed_muon,-100); //-beren
  event.set(h_not_reconstructed_0_500_muon,-100); //-beren
  event.set(h_not_reconstructed_500_750_muon,-100); //-beren
  event.set(h_not_reconstructed_750_1000_muon,-100); //-beren
  event.set(h_not_reconstructed_1000_1500_muon, -100); //-beren
  event.set(h_not_reconstructed_1500Inf_muon, -100); //-beren

  event.set(h_not_reconstructed_ele,-100); //-beren
  event.set(h_not_reconstructed_0_500_ele,-100); //-beren
  event.set(h_not_reconstructed_500_750_ele,-100); //-beren
  event.set(h_not_reconstructed_750_1000_ele,-100); //-beren
  event.set(h_not_reconstructed_1000_1500_ele, -100); //-beren
  event.set(h_not_reconstructed_1500Inf_ele, -100); //-beren

  // Run top-tagging
  if(ishotvr){
    TopTaggerHOTVR->process(event);
    hadronic_top->process(event);
  }else if(isdeepAK8){
    TopTaggerDeepAK8->process(event);
    hadronic_top->process(event);
  }
  if(debug) cout<<"Top Tagger ok"<<endl;

  fill_histograms(event, "BeforeCuts");
  if(debug)  cout<<"BeforeCuts"<<endl;
  fill_histograms(event, "Weights_Init");
  if(debug)  cout<<"Weights_Init"<<endl;
  lumihists_Weights_Init->fill(event);
  if(debug)  cout<<"lumi_Weights_Init"<<endl;

  

  if(!HEM_selection->passes(event)){
    if(!isMC) return false;
    else event.weight = event.weight*(1-0.64774715284); // calculated following instructions ar https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2018Analysis
  }
  fill_histograms(event, "Weights_HEM");

  // pileup weight
  PUWeight_module->process(event);
  if(debug)  cout<<"PUWeight ok"<<endl;
  fill_histograms(event, "Weights_PU");
  lumihists_Weights_PU->fill(event);

  // lumi weight
  LumiWeight_module->process(event);
  if(debug)  cout<<"LumiWeight ok"<<endl;
  fill_histograms(event, "Weights_Lumi");
  lumihists_Weights_Lumi->fill(event);

  // top pt reweighting
  //TopPtReweight_module->process(event);
  //fill_histograms(event, "Weights_TopPt");
  //lumihists_Weights_TopPt->fill(event);

  // MC scale
  MCScale_module->process(event);
  fill_histograms(event, "Weights_MCScale");
  lumihists_Weights_MCScale->fill(event);

  // Prefiring weights
  if (isMC) {
    if (Prefiring_direction == "nominal") event.weight *= event.prefiringWeight;
    else if (Prefiring_direction == "up") event.weight *= event.prefiringWeightUp;
    else if (Prefiring_direction == "down") event.weight *= event.prefiringWeightDown;
  }
  fill_histograms(event, "Weights_Prefiring");

  // Write PSWeights from genInfo to own branch in output tree
  ps_weights->process(event);
  fill_histograms(event, "Weights_PS");
  lumihists_Weights_PS->fill(event);

  // DeepAK8 TopTag SFs
  if(isdeepAK8) sf_toptag->process(event);
  if(debug) cout << "Weights_TopTag_SF: ok" << endl;
  fill_histograms(event, "Weights_TopTag_SF");

  //Clean muon collection with ID based on muon pT
  double muon_pt_high(55.);
  bool muon_is_low = false;
  bool muon_is_high = false;

  if(isMuon){
    vector<Muon>* muons = event.muons;
    for(unsigned int i=0; i<muons->size(); i++){
      if(event.muons->at(i).pt()<=muon_pt_high){
        muon_is_low = true;
      }else{
        muon_is_high = true;
      }
    }
  }
  sort_by_pt<Muon>(*event.muons);

  //Clean ele collection with ID based on ele pT
  double electron_pt_high(120.);
  bool ele_is_low = false;
  bool ele_is_high = false;

  if(isElectron){
    vector<Electron>* electrons = event.electrons;
    for(unsigned int i=0; i<electrons->size(); i++){
      if(event.electrons->at(i).pt()<=electron_pt_high){
        ele_is_low = true;
      }else{
        ele_is_high = true;
      }
    }
  }
  sort_by_pt<Electron>(*event.electrons);

  // apply electron id scale factors
  if(isMuon){
    sf_ele_id_dummy->process(event);
  }
  if(isElectron){
    if(ele_is_low){
      sf_ele_id_low->process(event);
    }
    else if(ele_is_high){
      sf_ele_id_high->process(event);
    }
    fill_histograms(event, "IdEle_SF");
  }

  // apply muon isolation scale factors (low pT only)
  if(isMuon){
    if(muon_is_low){
      sf_muon_iso_low->process(event);
    }
    else if(muon_is_high){
      sf_muon_iso_low_dummy->process(event);
    }
    fill_histograms(event, "IsoMuon_SF");
  }
  if(isElectron){
    sf_muon_iso_low_dummy->process(event);
  }
  // apply muon id scale factors
  if(isMuon){
    if(muon_is_low){
      sf_muon_id_low->process(event);
    }
    else if(muon_is_high){
      sf_muon_id_high->process(event);
    }
    fill_histograms(event, "IdMuon_SF");
  }
  if(isElectron){
    sf_muon_id_dummy->process(event);
  }

  // apply electron reco scale factors
  if(isMuon){
    sf_ele_reco_dummy->process(event);
  }
  if(isElectron){
    sf_ele_reco->process(event);
    fill_histograms(event, "RecoEle_SF");
  }

  // apply muon reco scale factors
  sf_muon_reco->process(event);
  fill_histograms(event, "MuonReco_SF");


  // apply lepton trigger scale factors
  if(isMuon){
    if(muon_is_low){
      sf_muon_trigger_low->process(event);
    }
    if(muon_is_high){
      sf_muon_trigger_high->process(event);
    }
    fill_histograms(event, "TriggerMuon_SF");
  }
  if(isElectron){
    sf_muon_trigger_dummy->process(event);
  }

  //Fill histograms before BTagging SF - used to extract Custom BTag SF in (NJets,HT)
  fill_histograms(event, "BeforeBtagSF");

  // btag shape sf (Ak4 chs jets)
  // new: using new modules, with PUPPI-CHS matching
  sf_btagging->process(event);
  fill_histograms(event, "AfterBtagSF");

  // apply custom SF to correct for BTag SF shape effects on NJets/HT
  if(isMC && isMuon){
    float custom_sf;

    vector<Jet>* jets = event.jets;
    int Njets = jets->size();
    double st_jets = 0.;
    for(const auto & jet : *jets) st_jets += jet.pt();
    custom_sf = ratio_hist_muon->GetBinContent( ratio_hist_muon->GetXaxis()->FindBin(Njets), ratio_hist_muon->GetYaxis()->FindBin(st_jets) );

    event.weight *= custom_sf;
  }
  if(isMC && !isMuon){
    float custom_sf;

    vector<Jet>* jets = event.jets;
    int Njets = jets->size();
    double st_jets = 0.;
    for(const auto & jet : *jets) st_jets += jet.pt();
    custom_sf = ratio_hist_ele->GetBinContent( ratio_hist_ele->GetXaxis()->FindBin(Njets), ratio_hist_ele->GetYaxis()->FindBin(st_jets) );

    event.weight *= custom_sf;
  }
  fill_histograms(event, "AfterCustomBtagSF");

  // Higher order corrections - EWK & QCD NLO
  NLOCorrections_module->process(event);
  fill_histograms(event, "NLOCorrections");

  //apply ele trigger sf
  sf_ele_trigger->process(event);
  fill_histograms(event, "TriggerEle_SF");
  fill_histograms(event, "AfterBaseline");

  CandidateBuilder->process(event);
  if(debug) cout << "CandidateBuilder: ok" << endl;
  Chi2DiscriminatorZprime->process(event);
  if(debug) cout << "Chi2DiscriminatorZprime: ok" << endl;
  CorrectMatchDiscriminatorZprime->process(event);
  if(debug) cout << "CorrectMatchDiscriminatorZprime: ok" << endl;

  // Variables for NN
  Variables_module->process(event);
  fill_histograms(event, "NNInputsBeforeReweight");
  if(debug) cout << "Variables_module: ok" << endl;

  // NN module
  NNModule->process(event);
  std::vector<tensorflow::Tensor> NNoutputs = NNModule->GetOutputs();

  event.set(h_NNoutput0, (double)(NNoutputs[0].tensor<float, 2>()(0,0)));
  event.set(h_NNoutput1, (double)(NNoutputs[0].tensor<float, 2>()(0,1)));
  event.set(h_NNoutput2, (double)(NNoutputs[0].tensor<float, 2>()(0,2)));
  event.set(h_NNoutput, NNoutputs);

  double out0 = (double)(NNoutputs[0].tensor<float, 2>()(0,0));
  double out1 = (double)(NNoutputs[0].tensor<float, 2>()(0,1));
  double out2 = (double)(NNoutputs[0].tensor<float, 2>()(0,2));
  vector<double> out_event = {out0, out1, out2};

  h_MulticlassNN_output->fill(event);

  double max_score = 0.0;
  for ( int i = 0; i < 3; i++ ) {
    if ( out_event[i] > max_score) {
      max_score = out_event[i];
    }
  }
  // Veto events with >= 2 TopTagged large-R jets
  if(!TopTagVetoSelection->passes(event)) return false;
  fill_histograms(event, "TopTagVeto");

  // out0=TTbar, out1=ST, out2=WJets
  if( out0 == max_score ){
    fill_histograms(event, "DNN_output0_beforeChi2Cut");
    if( ZprimeTopTag_selection->passes(event) ){
      fill_histograms(event, "DNN_output0_TopTag_beforeChi2Cut");
    }
    else{
      fill_histograms(event, "DNN_output0_NoTopTag_beforeChi2Cut");
    }
    if(Chi2_selection->passes(event)){  // cut on chi2<30 - only in SR == out0)
      fill_histograms(event, "DNN_output0");
      //cout << "fill systematics 0"<<endl;
      DeltaY_SystVariations_DNN_output0->fill(event);
      // h_Zprime_PDFVariations_DNN_output0->fill(event);
      if( ZprimeTopTag_selection->passes(event) ){
        fill_histograms(event, "DNN_output0_TopTag");
        DeltaY_SystVariations_DNN_output0_TopTag->fill(event);
        // h_Zprime_PDFVariations_DNN_output0_TopTag->fill(event);
      }
      else{
        fill_histograms(event, "DNN_output0_NoTopTag");
        DeltaY_SystVariations_DNN_output0_NoTopTag->fill(event);
        // h_Zprime_PDFVariations_DNN_output0_NoTopTag->fill(event);
      }
    }
  }

  if( out1 == max_score ){
    fill_histograms(event, "DNN_output1");
   // cout << "fill systematics 1"<<endl;
    DeltaY_SystVariations_DNN_output1->fill(event);
    // h_Zprime_PDFVariations_DNN_output1->fill(event);
    if( ZprimeTopTag_selection->passes(event) ){
      fill_histograms(event, "DNN_output1_TopTag");
      DeltaY_SystVariations_DNN_output1_TopTag->fill(event);
      // h_Zprime_PDFVariations_DNN_output1_TopTag->fill(event);
    }else{
      fill_histograms(event, "DNN_output1_NoTopTag");
      DeltaY_SystVariations_DNN_output1_NoTopTag->fill(event);
      // h_Zprime_PDFVariations_DNN_output1_NoTopTag->fill(event);
    }
  }

  if( out2 == max_score ){
    fill_histograms(event, "DNN_output2");
    DeltaY_SystVariations_DNN_output2->fill(event);
    // h_Zprime_PDFVariations_DNN_output2->fill(event);
    // h_MistagHists->fill(event);
    if( ZprimeTopTag_selection->passes(event) ){
      fill_histograms(event, "DNN_output2_TopTag");
      DeltaY_SystVariations_DNN_output2_TopTag->fill(event);
      // h_Zprime_PDFVariations_DNN_output2_TopTag->fill(event);
    }else{
      fill_histograms(event, "DNN_output2_NoTopTag");
      DeltaY_SystVariations_DNN_output2_NoTopTag->fill(event);
      // h_Zprime_PDFVariations_DNN_output2_NoTopTag->fill(event);
    }
  }

  fill_histograms(event, "AfterChi2");

  if( out0 == max_score ){
    if(Chi2_selection->passes(event)){


  if(isMC){
    vector<GenParticle>* genparticles = event.genparticles;
    GenParticle top, antitop;
    for(const GenParticle & gp : *event.genparticles){

      if(gp.pdgId() == 6){
        top = gp;
      }
      else if(gp.pdgId() == -6){
      antitop = gp;
        }
    }
    if(debug) cout << "1" << endl;

    float m_ttbar = inv_mass(top.v4() + antitop.v4());

    double_t DeltaY_gen= TMath::Abs(0.5*TMath::Log((top.energy() + top.pt()*TMath::SinH(top.eta()))/(top.energy() - top.pt()*TMath::SinH(top.eta())))) - TMath::Abs(0.5*TMath::Log((antitop.energy() + antitop.pt()*TMath::SinH(antitop.eta()))/(antitop.energy() - antitop.pt()*TMath::SinH(antitop.eta()))));
   
    event.set(h_DeltaY_gen,DeltaY_gen);

    if(debug) cout << "2" << endl;
    //Number of deltaY gen events
    if(m_ttbar>=0 && m_ttbar < 500){
      fill_histograms(event, "DeltaY_gen_0_500");
    }
    if(m_ttbar>=500 && m_ttbar < 750){
      fill_histograms(event, "DeltaY_gen_500_750");
    }
    if(m_ttbar>=750 && m_ttbar < 1000){
      fill_histograms(event, "DeltaY_gen_750_1000");
    }
    if(m_ttbar>=1000 && m_ttbar < 1500){
      fill_histograms(event, "DeltaY_gen_1000_1500");
    }
    if(m_ttbar>=1500){
      fill_histograms(event, "DeltaY_gen_1500Inf");
    }
    if(debug) cout << "3" << endl;
    //Number of deltaY gen events with NEGATIVE DY
    if (DeltaY_gen<0){
      fill_histograms(event, "DeltaY_gen_N");

      if(m_ttbar>=0 && m_ttbar < 500){
        fill_histograms(event, "DeltaY_N_gen_0_500");
      }
      if(m_ttbar>=500 && m_ttbar < 750){
        fill_histograms(event, "DeltaY_N_gen_500_750");
      }
      if(m_ttbar>=750 && m_ttbar < 1000){
        fill_histograms(event, "DeltaY_N_gen_750_1000");
      }
      if(m_ttbar>=1000 && m_ttbar < 1500){
        fill_histograms(event, "DeltaY_N_gen_1000_1500");
      }
      if(m_ttbar>=1500){
        fill_histograms(event, "DeltaY_N_gen_1500Inf");
      }
    }

    //Number of deltaY gen events with POSITIVE DY
    if (DeltaY_gen>0){
      fill_histograms(event, "DeltaY_gen_P");

      if(m_ttbar>=0 && m_ttbar < 500){
        fill_histograms(event, "DeltaY_P_gen_0_500");
      }
      if(m_ttbar>=500 && m_ttbar < 750){
        fill_histograms(event, "DeltaY_P_gen_500_750");
      }
      if(m_ttbar>=750 && m_ttbar < 1000){
        fill_histograms(event, "DeltaY_P_gen_750_1000");
      }
      if(m_ttbar>=1000 && m_ttbar < 1500){
        fill_histograms(event, "DeltaY_P_gen_1000_1500");
      }
      if(m_ttbar>=1500){
        fill_histograms(event, "DeltaY_P_gen_1500Inf");
      }
    }
    if(debug) cout << "3" << endl;

    // ========= MUON ========

    if(isMuon){

if(debug) cout << "4" << endl;
    ZprimeCandidate* BestZprimeCandidate = event.get(h_BestZprimeCandidateChi2);
    float Mass_tt = BestZprimeCandidate->Zprime_v4().M();
      if(debug) cout << "5" << endl;
    double_t DeltaY_reco= TMath::Abs(0.5*TMath::Log((BestZprimeCandidate->top_leptonic_v4().energy() + BestZprimeCandidate->top_leptonic_v4().pt()*TMath::SinH(BestZprimeCandidate->top_leptonic_v4().eta()))/(BestZprimeCandidate->top_leptonic_v4().energy() - BestZprimeCandidate->top_leptonic_v4().pt()*TMath::SinH(BestZprimeCandidate->top_leptonic_v4().eta())))) - TMath::Abs(0.5*TMath::Log((BestZprimeCandidate->top_hadronic_v4().energy() + BestZprimeCandidate->top_hadronic_v4().pt()*TMath::SinH(BestZprimeCandidate->top_hadronic_v4().eta()))/(BestZprimeCandidate->top_hadronic_v4().energy() - BestZprimeCandidate->top_hadronic_v4().pt()*TMath::SinH(BestZprimeCandidate->top_hadronic_v4().eta()))));
    // float DeltaY_reco = TMath::Abs(BestZprimeCandidate->top_leptonic_v4().Rapidity()) - TMath::Abs(BestZprimeCandidate->top_hadronic_v4().Rapidity());
    if(debug) cout << "6" << endl;
    event.set(h_DeltaY_reco,DeltaY_reco);
if(debug) cout << "7" << endl;
    //Number of deltaY reco events
    if(Mass_tt>=0 && Mass_tt < 500){
      fill_histograms(event, "DeltaY_reco_0_500_muon");
    }
    if(Mass_tt>=500 && Mass_tt < 750){
      fill_histograms(event, "DeltaY_reco_500_750_muon");
    }
    if(Mass_tt>=750 && Mass_tt < 1000){
      fill_histograms(event, "DeltaY_reco_750_1000_muon");
    }
    if(Mass_tt>=1000 && Mass_tt < 1500){
      fill_histograms(event, "DeltaY_reco_1000_1500_muon");
    }
    if(Mass_tt>=1500){
      fill_histograms(event, "DeltaY_reco_1500Inf_muon");
    }
    
    //Number of deltaY reco events with NEGATIVE DY
    if (DeltaY_reco<0){
      fill_histograms(event, "DeltaY_reco_N_muon");

      if(Mass_tt>=0 && Mass_tt < 500){
        fill_histograms(event, "DeltaY_N_reco_0_500_muon");
      }
      if(Mass_tt>=500 && Mass_tt < 750){
        fill_histograms(event, "DeltaY_N_reco_500_750_muon");
      }
      if(Mass_tt>=750 && Mass_tt < 1000){
        fill_histograms(event, "DeltaY_N_reco_750_1000_muon");
      }
      if(Mass_tt>=1000 && Mass_tt < 1500){
        fill_histograms(event, "DeltaY_N_reco_1000_1500_muon");
      }
      if(Mass_tt>=1500){
        fill_histograms(event, "DeltaY_N_reco_1500Inf_muon");
      }
    }
if(debug) cout << "8" << endl;
    //Number of deltaY reco events with POSITIVE DY
    if (DeltaY_reco>0){
      fill_histograms(event, "DeltaY_reco_P_muon");

      if(Mass_tt>=0 && Mass_tt < 500){
        fill_histograms(event, "DeltaY_P_reco_0_500_muon");
      }
      if(Mass_tt>=500 && Mass_tt < 750){
        fill_histograms(event, "DeltaY_P_reco_500_750_muon");
      }
      if(Mass_tt>=750 && Mass_tt < 1000){
        fill_histograms(event, "DeltaY_P_reco_750_1000_muon");
      }
      if(Mass_tt>=1000 && Mass_tt < 1500){
        fill_histograms(event, "DeltaY_P_reco_1000_1500_muon");
      }
      if(Mass_tt>=1500){
        fill_histograms(event, "DeltaY_P_reco_1500Inf_muon");
      }
    }
     

     // ==== MATCHING with DELTA R === This section has explanation for each code snip

    
    // This section loops over the generator particles in the event,for pdgId of 6 (top quark) and -6 (anti-top quark). The found particles are then stored in the tops vector.
    GenParticle top, antitop;
    for(const GenParticle & gp : *event.genparticles){
      if(gp.pdgId() == 6){
        top = gp;
      }
      else if(gp.pdgId() == -6){
        antitop = gp;
      }
    }
    std::vector<GenParticle> tops = {top, antitop};

if(debug) cout << "9" << endl;
    // The Lorentz vectors represent the 4-momenta (energy, and three spatial momentum components) for the leptonic and hadronic tops from the "BestZprimeCandidate" object
    LorentzVector lep_top = BestZprimeCandidate->top_leptonic_v4();
    LorentzVector had_top = BestZprimeCandidate->top_hadronic_v4();

    //// vectors to store the deltaR values for the leptonic and hadronic tops with each gen particle
    std::vector<double> deltaR_leptonic_values(genparticles->size(), 99.0);
    std::vector<double> deltaR_hadronic_values(genparticles->size(), 99.0);

    // deltaR is a measure of separation in the eta-phi space. The next few sections calculate the deltaR values between the leptonic and hadronic tops and each generator particle
    // this part initializes vectors to store deltaR values with a default of 99.0 and fills in the actual deltaR values by looping over the gen particles (top)
    for(unsigned int j=0; j<genparticles->size(); ++j) {
      if(abs(genparticles->at(j).pdgId()) == 6) {
      LorentzVector genparticle_p4(genparticles->at(j).pt(), genparticles->at(j).eta(), genparticles->at(j).phi(), genparticles->at(j).energy());
      deltaR_leptonic_values[j] = deltaR(lep_top, genparticle_p4);
      deltaR_hadronic_values[j] = deltaR(had_top, genparticle_p4);
    }
    }
    if(debug) cout << "10" << endl;
    // vectors to store the best gen particle for each top
    // it determines which gen particle is closest in the eta-phi space to the leptonic and hadronic tops
    int best_gen_for_leptop = -1;
    int best_gen_for_hadtop = -1;
    std::vector<int> best_leptop_for_gen(genparticles->size(), -1);
    std::vector<int> best_hadtop_for_gen(genparticles->size(), -1);

    // Find closest gen particle for each top
    // These loops determine whether each gen particle is closer to the leptonic or hadronic top and assigns an index accordingly
    double deltaR_min_leptonic = 99.0;
    for(unsigned int j=0; j<genparticles->size(); ++j) {
      if(abs(genparticles->at(j).pdgId()) == 6) {
        if (deltaR_leptonic_values[j] < deltaR_min_leptonic && deltaR_leptonic_values[j]<0.4) {
            deltaR_min_leptonic = deltaR_leptonic_values[j];
            best_gen_for_leptop = j;
        }
    }   
    }
    double deltaR_min_hadronic = 99.0;
    for(unsigned int j=0; j<genparticles->size(); ++j) {
      if(abs(genparticles->at(j).pdgId()) == 6) {
        if (deltaR_hadronic_values[j] < deltaR_min_hadronic && deltaR_hadronic_values[j]<0.4) {
            deltaR_min_hadronic = deltaR_hadronic_values[j];
            best_gen_for_hadtop = j;
        }
    }
    }
  if(debug) cout << "11" << endl;
    for(unsigned int j=0; j<genparticles->size(); ++j) {
    if(abs(genparticles->at(j).pdgId()) == 6) {
      if(deltaR_leptonic_values[j] < deltaR_hadronic_values[j]) {
          best_leptop_for_gen[j] = 0;  // 0 is the index for the single leptonic top
      } else {
          best_hadtop_for_gen[j] = 0;  // 0 is the index for the single hadronic top
      }
      }
    }
    
    event.set(h_DeltaR_hadronic_genparticle, deltaR_min_hadronic);
    event.set(h_DeltaR_leptonic_genparticle, deltaR_min_leptonic);

    
    // deltaY values calculation

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
       if(debug) cout << "12" << endl;
       
    double_t DeltaY_reco_best = TMath::Abs(0.5*TMath::Log((lep_top.energy() + lep_top.pt()*TMath::SinH(lep_top.eta()))/(lep_top.energy() - lep_top.pt()*TMath::SinH(lep_top.eta())))) - TMath::Abs(0.5*TMath::Log((had_top.energy() + had_top.pt()*TMath::SinH(had_top.eta()))/(had_top.energy() - had_top.pt()*TMath::SinH(had_top.eta()))));
    double_t DeltaY_gen_best = 0.0;
    if(valid_leptop && valid_hadtop) {
        DeltaY_gen_best = TMath::Abs(0.5*TMath::Log((best_matched_gen_leptop.energy() + best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta()))/(best_matched_gen_leptop.energy() - best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta())))) - TMath::Abs(0.5*TMath::Log((best_matched_gen_hadtop.energy() + best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))/(best_matched_gen_hadtop.energy() - best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))));
    } 

    // This loop checks each gen particle and if it's not one of the "best matched" gen particles for the tops, the particle's pt is set to a histogram based on the invariant mass m_ttbar of the top-antitop system.
    
    for(unsigned int j=0; j<genparticles->size(); ++j) {
      if(abs(genparticles->at(j).pdgId()) == 6) {
        if (!(valid_leptop && static_cast<int>(j) == best_gen_for_leptop) && !(valid_hadtop && static_cast<int>(j) == best_gen_for_hadtop)) {
          
          fill_histograms(event, "Not_reco_gens_muon");
          event.set(h_not_reconstructed_muon, genparticles->at(j).pt());

          if (0 < m_ttbar && m_ttbar < 500) {
            fill_histograms(event, "Not_reco_gens_0_500_muon");
            event.set(h_not_reconstructed_0_500_muon, genparticles->at(j).pt());            
          } 
          else if (500 <= m_ttbar && m_ttbar < 750) {
            fill_histograms(event, "Not_reco_gens_500_750_muon");
            event.set(h_not_reconstructed_500_750_muon, genparticles->at(j).pt());
          }
          else if (750 <= m_ttbar && m_ttbar < 1000) {
            fill_histograms(event, "Not_reco_gens_750_1000_muon");
            event.set(h_not_reconstructed_750_1000_muon, genparticles->at(j).pt());
          }
          else if (1000 <= m_ttbar && m_ttbar < 1500) {
            fill_histograms(event, "Not_reco_gens_1000_1500_muon");
            event.set(h_not_reconstructed_1000_1500_muon, genparticles->at(j).pt());
          }
          else if (1500 <= m_ttbar ) {
            fill_histograms(event, "Not_reco_gens_1500Inf_muon");
            event.set(h_not_reconstructed_1500Inf_muon, genparticles->at(j).pt());
          }
        }
      }
    }

    // Explanation:
    //A histogram of the ΔR distances between the jets and their matched genparticles. 
    //This gives an overall sense of the matching quality. 
    //If the matching is good, one should expect to see most of the entries at small ΔR values.


if(debug) cout << "13" << endl;
    /// ------ RECO & GEN P_P -----

    //Number of events with DeltaY_gen_best POSITIVE and DeltaY_reco_best POSITIVE
    if(DeltaY_gen_best>0 && DeltaY_reco_best>0){
        fill_histograms(event, "DY_P_P_muon");
        event.set(h_DeltaY_P_P_nomass_muon, DeltaY_reco_best);
    
      if(Mass_tt>=0 && Mass_tt<500){
        fill_histograms(event, "DY_P_P_0_500_muon");
        event.set(h_DeltaY_P_P_0_500_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=500 && Mass_tt<750){
          fill_histograms(event, "DY_P_P_500_750_muon");
          event.set(h_DeltaY_P_P_500_750_muon, DeltaY_reco_best);
      } 
      if(Mass_tt>=750 && Mass_tt<1000){
          fill_histograms(event, "DY_P_P_750_1000_muon");
          event.set(h_DeltaY_P_P_750_1000_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=1000 && Mass_tt<1500){
          fill_histograms(event, "DY_P_P_1000_1500_muon");
          event.set(h_DeltaY_P_P_1000_1500_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=1500){
          fill_histograms(event, "DY_P_P_1500Inf_muon");
          event.set(h_DeltaY_P_P_1500Inf_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=750){
          fill_histograms(event, "DY_P_P_750Inf_muon");
          event.set(h_DeltaY_P_P_750Inf_muon, DeltaY_reco_best);
      }
    }

    // in order to check how many 0 dY there are
    if(DeltaY_gen_best>=0){
        fill_histograms(event, "DY_P_equal_gen_muon");
    }
    if(DeltaY_gen_best<=0){
        fill_histograms(event, "DY_N_equal_gen_muon");
    }
    if(DeltaY_reco_best>=0){
        fill_histograms(event, "DY_P_equal_reco_muon");
    }
    if(DeltaY_reco_best<=0){
        fill_histograms(event, "DY_N_equal_reco_muon");
    }
    
  if(debug) cout << "14" << endl;

    /// ------ RECO & GEN P_N -----

    //Number of events with DeltaY_gen_best POSITIVE and DeltaY_reco_best POSITIVE
    if(DeltaY_gen_best>0 && DeltaY_reco_best<0){
        fill_histograms(event, "DY_P_N_muon");
        event.set(h_DeltaY_P_N_nomass_muon, DeltaY_reco_best);
    
      if(Mass_tt>=0 && Mass_tt<500){
        fill_histograms(event, "DY_P_N_0_500_muon");
        event.set(h_DeltaY_P_N_0_500_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=500 && Mass_tt<750){
          fill_histograms(event, "DY_P_N_500_750_muon");
          event.set(h_DeltaY_P_N_500_750_muon, DeltaY_reco_best);
      } 
      if(Mass_tt>=750 && Mass_tt<1000){
          fill_histograms(event, "DY_P_N_750_1000_muon");
          event.set(h_DeltaY_P_N_750_1000_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=1000 && Mass_tt<1500){
          fill_histograms(event, "DY_P_N_1000_1500_muon");
          event.set(h_DeltaY_P_N_1000_1500_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=1500){
          fill_histograms(event, "DY_P_N_1500Inf_muon");
          event.set(h_DeltaY_P_N_1500Inf_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=750){
          fill_histograms(event, "DY_P_N_750Inf_muon");
          event.set(h_DeltaY_P_N_750Inf_muon, DeltaY_reco_best);
      }
    }


    /// ------ RECO & GEN N_P -----

    //Number of events with DeltaY_gen_best POSITIVE and DeltaY_reco_best POSITIVE
    if(DeltaY_gen_best<0 && DeltaY_reco_best>0){
        fill_histograms(event, "DY_N_P_muon");
        event.set(h_DeltaY_N_P_nomass_muon, DeltaY_reco_best);
    
      if(Mass_tt>=0 && Mass_tt<500){
        fill_histograms(event, "DY_N_P_0_500_muon");
        event.set(h_DeltaY_N_P_0_500_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=500 && Mass_tt<750){
          fill_histograms(event, "DY_N_P_500_750_muon");
          event.set(h_DeltaY_N_P_500_750_muon, DeltaY_reco_best);
      } 
      if(Mass_tt>=750 && Mass_tt<1000){
          fill_histograms(event, "DY_N_P_750_1000_muon");
          event.set(h_DeltaY_N_P_750_1000_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=1000 && Mass_tt<1500){
          fill_histograms(event, "DY_N_P_1000_1500_muon");
          event.set(h_DeltaY_N_P_1000_1500_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=1500){
          fill_histograms(event, "DY_N_P_1500Inf_muon");
          event.set(h_DeltaY_N_P_1500Inf_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=750){
          fill_histograms(event, "DY_N_P_750Inf_muon");
          event.set(h_DeltaY_N_P_750Inf_muon, DeltaY_reco_best);
      }
    }

    /// ------ RECO & GEN N_N -----
if(debug) cout << "15" << endl;
    //Number of events with DeltaY_gen_best POSITIVE and DeltaY_reco_best POSITIVE
    if(DeltaY_gen_best<0 && DeltaY_reco_best<0){
        fill_histograms(event, "DY_N_N_muon");
        event.set(h_DeltaY_N_N_nomass_muon, DeltaY_reco_best);
    
      if(Mass_tt>=0 && Mass_tt<500){
        fill_histograms(event, "DY_N_N_0_500_muon");
        event.set(h_DeltaY_N_N_0_500_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=500 && Mass_tt<750){
          fill_histograms(event, "DY_N_N_500_750_muon");
          event.set(h_DeltaY_N_N_500_750_muon, DeltaY_reco_best);
      } 
      if(Mass_tt>=750 && Mass_tt<1000){
          fill_histograms(event, "DY_N_N_750_1000_muon");
          event.set(h_DeltaY_N_N_750_1000_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=1000 && Mass_tt<1500){
          fill_histograms(event, "DY_N_N_1000_1500_muon");
          event.set(h_DeltaY_N_N_1000_1500_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=1500){
          fill_histograms(event, "DY_N_N_1500Inf_muon");
          event.set(h_DeltaY_N_N_1500Inf_muon, DeltaY_reco_best);
      }
      if(Mass_tt>=750){
          fill_histograms(event, "DY_N_N_750Inf_muon");
          event.set(h_DeltaY_N_N_750Inf_muon, DeltaY_reco_best);
      }
    }



    // ----- IN DeltaY GEN BUT NOT IN RECO - Double check------

    
    int topQuarkCount = 0;
    for(unsigned int j=0; j<genparticles->size(); ++j) {
      if(abs(genparticles->at(j).pdgId()) == 6){
        topQuarkCount++;

        int genBin = (DeltaY_gen_best < 0) ? 0 : 1;
        int recoBin;

        // Checking if the gen particle is associated with a top (leptonic or hadronic)
        if (best_leptop_for_gen[j] != -1 || best_hadtop_for_gen[j] != -1) {
          recoBin = (DeltaY_reco_best < 0) ? 0 : 1;
          int binNumber = 2 * genBin + recoBin;

          if(Mass_tt<500 && Mass_tt>=0 ){
            fill_histograms(event, "DY_0_500_recogenmatch_muon");
              if(binNumber == 0) {
              fill_histograms(event, "DY_Match_N_N_0_500_muon"); 
              }
              else if(binNumber == 1) {
                fill_histograms(event, "DY_Match_N_P_0_500_muon"); 
              }
              else if(binNumber == 2) {
                fill_histograms(event, "DY_Match_P_N_0_500_muon");
              }
              else if(binNumber == 3) {
                fill_histograms(event, "DY_Match_P_P_0_500_muon"); 
              }
              else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
                fill_histograms(event, "UnMatched_0_500_muon"); 
              }
          }

          if( Mass_tt>=500 && Mass_tt<750 ){
            fill_histograms(event, "DY_500_750_recogenmatch_muon");

            if(binNumber == 0) {
            fill_histograms(event, "DY_Match_N_N_500_750_muon"); 

            }
            else if(binNumber == 1) {
              fill_histograms(event, "DY_Match_N_P_500_750_muon"); 
            }
            else if(binNumber == 2) {
              fill_histograms(event, "DY_Match_P_N_500_750_muon");
            }
            else if(binNumber == 3) {
              fill_histograms(event, "DY_Match_P_P_500_750_muon"); 
            }
            else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
              fill_histograms(event, "UnMatched_500_750_muon"); 
            }
          }

          if( Mass_tt>=750 && Mass_tt<1000 ){
              fill_histograms(event, "DY_750_1000_recogenmatch_muon");
              if(binNumber == 0) {
              fill_histograms(event, "DY_Match_N_N_750_1000_muon"); 
              }
              else if(binNumber == 1) {
                fill_histograms(event, "DY_Match_N_P_750_1000_muon"); 
              }
              else if(binNumber == 2) {
                fill_histograms(event, "DY_Match_P_N_750_1000_muon");
              }
              else if(binNumber == 3) {
                fill_histograms(event, "DY_Match_P_P_750_1000_muon"); 
              }
              else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
                fill_histograms(event, "UnMatched_750_1000_muon"); 
              }
          }
                
          if( Mass_tt>=1000 && Mass_tt<1500 ){
              fill_histograms(event, "DY_1000_1500_recogenmatch_muon");
              if(binNumber == 0) {
              fill_histograms(event, "DY_Match_N_N_1000_1500_muon"); 
              }
              else if(binNumber == 1) {
                fill_histograms(event, "DY_Match_N_P_1000_1500_muon");   
              }
              else if(binNumber == 2) {
                fill_histograms(event, "DY_Match_P_N_1000_1500_muon"); 
              }
              else if(binNumber == 3) {
                fill_histograms(event, "DY_Match_P_P_1000_1500_muon"); 
              }
              else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
                fill_histograms(event, "UnMatched_1000_1500_muon"); 
              }
          }


          if( Mass_tt>=1500){
              fill_histograms(event, "DY_1500Inf_recogenmatch_muon");

              if(binNumber == 0) {
              fill_histograms(event, "DY_Match_N_N_1500Inf_muon"); 

              }
              else if(binNumber == 1) {
                fill_histograms(event, "DY_Match_N_P_1500Inf_muon"); 
    
              }
              else if(binNumber == 2) {
                fill_histograms(event, "DY_Match_P_N_1500Inf_muon");
    
              }
              else if(binNumber == 3) {
                fill_histograms(event, "DY_Match_P_P_1500Inf_muon"); 
    
              }
              else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
                fill_histograms(event, "UnMatched_1500Inf_muon"); 
    
              }
          }
          } 
          else {
            if(Mass_tt<500 && Mass_tt>=0){
              // The top gen particle wasn't reconstructed. Please ignore P_P part, there is no meaning behind it.
              fill_histograms(event, "DY_Mass_0_500_NOT_reco_muon");
            }
            if( Mass_tt>=500 && Mass_tt<750){
              fill_histograms(event, "DY_Mass_500_750_NOT_reco_muon");
            }
            if( Mass_tt>=750 && Mass_tt<1000){
              fill_histograms(event, "DY_Mass_750_1000_NOT_reco_muon");
            }
            if(  Mass_tt>=1000 && Mass_tt<1500){
              fill_histograms(event, "DY_Mass_1000_1500_NOT_reco_muon");
            }
            if( Mass_tt>=1500){
              fill_histograms(event, "DY_Mass_1500Inf_NOT_reco_muon");
            }
          }
          }
      }
          // gen particle (index j) was not matched to a jet
          // cout << "Gen particle at index " << j << " was not reconstructed." << endl;
if(debug) cout << "16" << endl;
      // std::cout << "Number of top quarks: " << topQuarkCount << std::endl;
      event.set(h_topQuarkCount, topQuarkCount);
      fill_histograms(event, "GenTop"); 
if(debug) cout << "17" << endl;
    // muon bracket  ===== MUON END ==== 
    }
       
  if (isElectron){
if(debug) cout << "18" << endl;
   ZprimeCandidate* BestZprimeCandidate = event.get(h_BestZprimeCandidateChi2);
    float Mass_tt = BestZprimeCandidate->Zprime_v4().M();
      
    double_t DeltaY_reco= TMath::Abs(0.5*TMath::Log((BestZprimeCandidate->top_leptonic_v4().energy() + BestZprimeCandidate->top_leptonic_v4().pt()*TMath::SinH(BestZprimeCandidate->top_leptonic_v4().eta()))/(BestZprimeCandidate->top_leptonic_v4().energy() - BestZprimeCandidate->top_leptonic_v4().pt()*TMath::SinH(BestZprimeCandidate->top_leptonic_v4().eta())))) - TMath::Abs(0.5*TMath::Log((BestZprimeCandidate->top_hadronic_v4().energy() + BestZprimeCandidate->top_hadronic_v4().pt()*TMath::SinH(BestZprimeCandidate->top_hadronic_v4().eta()))/(BestZprimeCandidate->top_hadronic_v4().energy() - BestZprimeCandidate->top_hadronic_v4().pt()*TMath::SinH(BestZprimeCandidate->top_hadronic_v4().eta()))));
    // float DeltaY_reco = TMath::Abs(BestZprimeCandidate->top_leptonic_v4().Rapidity()) - TMath::Abs(BestZprimeCandidate->top_hadronic_v4().Rapidity());
    
    event.set(h_DeltaY_reco,DeltaY_reco);
if(debug) cout << "19" << endl;
    //Number of deltaY reco events
    if(Mass_tt>=0 && Mass_tt < 500){
      fill_histograms(event, "DeltaY_reco_0_500_ele");
    }
    if(Mass_tt>=500 && Mass_tt < 750){
      fill_histograms(event, "DeltaY_reco_500_750_ele");
    }
    if(Mass_tt>=750 && Mass_tt < 1000){
      fill_histograms(event, "DeltaY_reco_750_1000_ele");
    }
    if(Mass_tt>=1000 && Mass_tt < 1500){
      fill_histograms(event, "DeltaY_reco_1000_1500_ele");
    }
    if(Mass_tt>=1500){
      fill_histograms(event, "DeltaY_reco_1500Inf_ele");
    }
    
    //Number of deltaY reco events with NEGATIVE DY
    if (DeltaY_reco<0){
      fill_histograms(event, "DeltaY_reco_N_ele");

      if(Mass_tt>=0 && Mass_tt < 500){
        fill_histograms(event, "DeltaY_N_reco_0_500_ele");
      }
      if(Mass_tt>=500 && Mass_tt < 750){
        fill_histograms(event, "DeltaY_N_reco_500_750_ele");
      }
      if(Mass_tt>=750 && Mass_tt < 1000){
        fill_histograms(event, "DeltaY_N_reco_750_1000_ele");
      }
      if(Mass_tt>=1000 && Mass_tt < 1500){
        fill_histograms(event, "DeltaY_N_reco_1000_1500_ele");
      }
      if(Mass_tt>=1500){
        fill_histograms(event, "DeltaY_N_reco_1500Inf_ele");
      }
    }
if(debug) cout << "20" << endl;
    //Number of deltaY reco events with POSITIVE DY
    if (DeltaY_reco>0){
      fill_histograms(event, "DeltaY_reco_P_ele");

      if(Mass_tt>=0 && Mass_tt < 500){
        fill_histograms(event, "DeltaY_P_reco_0_500_ele");
      }
      if(Mass_tt>=500 && Mass_tt < 750){
        fill_histograms(event, "DeltaY_P_reco_500_750_ele");
      }
      if(Mass_tt>=750 && Mass_tt < 1000){
        fill_histograms(event, "DeltaY_P_reco_750_1000_ele");
      }
      if(Mass_tt>=1000 && Mass_tt < 1500){
        fill_histograms(event, "DeltaY_P_reco_1000_1500_ele");
      }
      if(Mass_tt>=1500){
        fill_histograms(event, "DeltaY_P_reco_1500Inf_ele");
      }
    }
     

     // ==== MATCHING with DELTA R === This section has explanation for each code snip

    
    // This section loops over the generator particles in the event,for pdgId of 6 (top quark) and -6 (anti-top quark). The found particles are then stored in the tops vector.
    GenParticle top, antitop;
    for(const GenParticle & gp : *event.genparticles){
      if(gp.pdgId() == 6){
        top = gp;
      }
      else if(gp.pdgId() == -6){
        antitop = gp;
      }
    }
    std::vector<GenParticle> tops = {top, antitop};


    // The Lorentz vectors represent the 4-momenta (energy, and three spatial momentum components) for the leptonic and hadronic tops from the "BestZprimeCandidate" object
    LorentzVector lep_top = BestZprimeCandidate->top_leptonic_v4();
    LorentzVector had_top = BestZprimeCandidate->top_hadronic_v4();

    //// vectors to store the deltaR values for the leptonic and hadronic tops with each gen particle
    std::vector<double> deltaR_leptonic_values(genparticles->size(), 99.0);
    std::vector<double> deltaR_hadronic_values(genparticles->size(), 99.0);

    // deltaR is a measure of separation in the eta-phi space. The next few sections calculate the deltaR values between the leptonic and hadronic tops and each generator particle
    // this part initializes vectors to store deltaR values with a default of 99.0 and fills in the actual deltaR values by looping over the gen particles (top)
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
    for(unsigned int j=0; j<genparticles->size(); ++j) {
      if(abs(genparticles->at(j).pdgId()) == 6) {
        if (deltaR_leptonic_values[j] < deltaR_min_leptonic && deltaR_leptonic_values[j]<0.4) {
            deltaR_min_leptonic = deltaR_leptonic_values[j];
            best_gen_for_leptop = j;
        }
    }   
    }
    double deltaR_min_hadronic = 99.0;
    for(unsigned int j=0; j<genparticles->size(); ++j) {
      if(abs(genparticles->at(j).pdgId()) == 6) {
        if (deltaR_hadronic_values[j] < deltaR_min_hadronic && deltaR_hadronic_values[j]<0.4) {
            deltaR_min_hadronic = deltaR_hadronic_values[j];
            best_gen_for_hadtop = j;
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
    
    event.set(h_DeltaR_hadronic_genparticle, deltaR_min_hadronic);
    event.set(h_DeltaR_leptonic_genparticle, deltaR_min_leptonic);

    
    // deltaY values calculation

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
       
       if(debug) cout << "21" << endl;
    double_t DeltaY_reco_best = TMath::Abs(0.5*TMath::Log((lep_top.energy() + lep_top.pt()*TMath::SinH(lep_top.eta()))/(lep_top.energy() - lep_top.pt()*TMath::SinH(lep_top.eta())))) - TMath::Abs(0.5*TMath::Log((had_top.energy() + had_top.pt()*TMath::SinH(had_top.eta()))/(had_top.energy() - had_top.pt()*TMath::SinH(had_top.eta()))));
    double_t DeltaY_gen_best = 0.0;
    if(valid_leptop && valid_hadtop) {
        DeltaY_gen_best = TMath::Abs(0.5*TMath::Log((best_matched_gen_leptop.energy() + best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta()))/(best_matched_gen_leptop.energy() - best_matched_gen_leptop.pt()*TMath::SinH(best_matched_gen_leptop.eta())))) - TMath::Abs(0.5*TMath::Log((best_matched_gen_hadtop.energy() + best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))/(best_matched_gen_hadtop.energy() - best_matched_gen_hadtop.pt()*TMath::SinH(best_matched_gen_hadtop.eta()))));
    } 

    // This loop checks each gen particle and if it's not one of the "best matched" gen particles for the tops, the particle's pt is set to a histogram based on the invariant mass m_ttbar of the top-antitop system.
    
    for(unsigned int j=0; j<genparticles->size(); ++j) {
      if(abs(genparticles->at(j).pdgId()) == 6) {
        if (!(valid_leptop && static_cast<int>(j) == best_gen_for_leptop) && !(valid_hadtop && static_cast<int>(j) == best_gen_for_hadtop)) {
          
          fill_histograms(event, "Not_reco_gens_ele");
          event.set(h_not_reconstructed_ele, genparticles->at(j).pt());

          if (0 < m_ttbar && m_ttbar < 500) {
            fill_histograms(event, "Not_reco_gens_0_500_ele");
            event.set(h_not_reconstructed_0_500_ele, genparticles->at(j).pt());            
          } 
          else if (500 <= m_ttbar && m_ttbar < 750) {
            fill_histograms(event, "Not_reco_gens_500_750_ele");
            event.set(h_not_reconstructed_500_750_ele, genparticles->at(j).pt());
          }
          else if (750 <= m_ttbar && m_ttbar < 1000) {
            fill_histograms(event, "Not_reco_gens_750_1000_ele");
            event.set(h_not_reconstructed_750_1000_ele, genparticles->at(j).pt());
          }
          else if (1000 <= m_ttbar && m_ttbar < 1500) {
            fill_histograms(event, "Not_reco_gens_1000_1500_ele");
            event.set(h_not_reconstructed_1000_1500_ele, genparticles->at(j).pt());
          }
          else if (1500 <= m_ttbar ) {
            fill_histograms(event, "Not_reco_gens_1500Inf_ele");
            event.set(h_not_reconstructed_1500Inf_ele, genparticles->at(j).pt());
          }
        }
      }
    }

    // Explanation:
    //A histogram of the ΔR distances between the jets and their matched genparticles. 
    //This gives an overall sense of the matching quality. 
    //If the matching is good, one should expect to see most of the entries at small ΔR values.



    /// ------ RECO & GEN P_P -----

    //Number of events with DeltaY_gen_best POSITIVE and DeltaY_reco_best POSITIVE
    if(DeltaY_gen_best>0 && DeltaY_reco_best>0){
        fill_histograms(event, "DY_P_P_ele");
        event.set(h_DeltaY_P_P_nomass_ele, DeltaY_reco_best);
    
      if(Mass_tt>=0 && Mass_tt<500){
        fill_histograms(event, "DY_P_P_0_500_ele");
        event.set(h_DeltaY_P_P_0_500_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=500 && Mass_tt<750){
          fill_histograms(event, "DY_P_P_500_750_ele");
          event.set(h_DeltaY_P_P_500_750_ele, DeltaY_reco_best);
      } 
      if(Mass_tt>=750 && Mass_tt<1000){
          fill_histograms(event, "DY_P_P_750_1000_ele");
          event.set(h_DeltaY_P_P_750_1000_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=1000 && Mass_tt<1500){
          fill_histograms(event, "DY_P_P_1000_1500_ele");
          event.set(h_DeltaY_P_P_1000_1500_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=1500){
          fill_histograms(event, "DY_P_P_1500Inf_ele");
          event.set(h_DeltaY_P_P_1500Inf_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=750){
          fill_histograms(event, "DY_P_P_750Inf_ele");
          event.set(h_DeltaY_P_P_750Inf_ele, DeltaY_reco_best);
      }
    }

    // in order to check how many 0 dY there are
    if(DeltaY_gen_best>=0){
        fill_histograms(event, "DY_P_equal_gen_ele");
    }
    if(DeltaY_gen_best<=0){
        fill_histograms(event, "DY_N_equal_gen_ele");
    }
    if(DeltaY_reco_best>=0){
        fill_histograms(event, "DY_P_equal_reco_ele");
    }
    if(DeltaY_reco_best<=0){
        fill_histograms(event, "DY_N_equal_reco_ele");
    }
    
  if(debug) cout << "22" << endl;

    /// ------ RECO & GEN P_N -----

    //Number of events with DeltaY_gen_best POSITIVE and DeltaY_reco_best POSITIVE
    if(DeltaY_gen_best>0 && DeltaY_reco_best<0){
        fill_histograms(event, "DY_P_N_ele");
        event.set(h_DeltaY_P_N_nomass_ele, DeltaY_reco_best);
    
      if(Mass_tt>=0 && Mass_tt<500){
        fill_histograms(event, "DY_P_N_0_500_ele");
        event.set(h_DeltaY_P_N_0_500_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=500 && Mass_tt<750){
          fill_histograms(event, "DY_P_N_500_750_ele");
          event.set(h_DeltaY_P_N_500_750_ele, DeltaY_reco_best);
      } 
      if(Mass_tt>=750 && Mass_tt<1000){
          fill_histograms(event, "DY_P_N_750_1000_ele");
          event.set(h_DeltaY_P_N_750_1000_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=1000 && Mass_tt<1500){
          fill_histograms(event, "DY_P_N_1000_1500_ele");
          event.set(h_DeltaY_P_N_1000_1500_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=1500){
          fill_histograms(event, "DY_P_N_1500Inf_ele");
          event.set(h_DeltaY_P_N_1500Inf_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=750){
          fill_histograms(event, "DY_P_N_750Inf_ele");
          event.set(h_DeltaY_P_N_750Inf_ele, DeltaY_reco_best);
      }
    }


    /// ------ RECO & GEN N_P -----

    //Number of events with DeltaY_gen_best POSITIVE and DeltaY_reco_best POSITIVE
    if(DeltaY_gen_best<0 && DeltaY_reco_best>0){
        fill_histograms(event, "DY_N_P_ele");
        event.set(h_DeltaY_N_P_nomass_ele, DeltaY_reco_best);
    
      if(Mass_tt>=0 && Mass_tt<500){
        fill_histograms(event, "DY_N_P_0_500_ele");
        event.set(h_DeltaY_N_P_0_500_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=500 && Mass_tt<750){
          fill_histograms(event, "DY_N_P_500_750_ele");
          event.set(h_DeltaY_N_P_500_750_ele, DeltaY_reco_best);
      } 
      if(Mass_tt>=750 && Mass_tt<1000){
          fill_histograms(event, "DY_N_P_750_1000_ele");
          event.set(h_DeltaY_N_P_750_1000_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=1000 && Mass_tt<1500){
          fill_histograms(event, "DY_N_P_1000_1500_ele");
          event.set(h_DeltaY_N_P_1000_1500_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=1500){
          fill_histograms(event, "DY_N_P_1500Inf_ele");
          event.set(h_DeltaY_N_P_1500Inf_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=750){
          fill_histograms(event, "DY_N_P_750Inf_ele");
          event.set(h_DeltaY_N_P_750Inf_ele, DeltaY_reco_best);
      }
    }

    /// ------ RECO & GEN N_N -----

    //Number of events with DeltaY_gen_best POSITIVE and DeltaY_reco_best POSITIVE
    if(DeltaY_gen_best<0 && DeltaY_reco_best<0){
        fill_histograms(event, "DY_N_N_ele");
        event.set(h_DeltaY_N_N_nomass_ele, DeltaY_reco_best);
    
      if(Mass_tt>=0 && Mass_tt<500){
        fill_histograms(event, "DY_N_N_0_500_ele");
        event.set(h_DeltaY_N_N_0_500_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=500 && Mass_tt<750){
          fill_histograms(event, "DY_N_N_500_750_ele");
          event.set(h_DeltaY_N_N_500_750_ele, DeltaY_reco_best);
      } 
      if(Mass_tt>=750 && Mass_tt<1000){
          fill_histograms(event, "DY_N_N_750_1000_ele");
          event.set(h_DeltaY_N_N_750_1000_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=1000 && Mass_tt<1500){
          fill_histograms(event, "DY_N_N_1000_1500_ele");
          event.set(h_DeltaY_N_N_1000_1500_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=1500){
          fill_histograms(event, "DY_N_N_1500Inf_ele");
          event.set(h_DeltaY_N_N_1500Inf_ele, DeltaY_reco_best);
      }
      if(Mass_tt>=750){
          fill_histograms(event, "DY_N_N_750Inf_ele");
          event.set(h_DeltaY_N_N_750Inf_ele, DeltaY_reco_best);
      }
    }



    // ----- IN DeltaY GEN BUT NOT IN RECO - Double check------

    

    for(unsigned int j=0; j<genparticles->size(); ++j) {
      if(abs(genparticles->at(j).pdgId()) == 6){


        int genBin = (DeltaY_gen_best < 0) ? 0 : 1;
        int recoBin;

        // Checking if the gen particle is associated with a top (leptonic or hadronic)
        if (best_leptop_for_gen[j] != -1 || best_hadtop_for_gen[j] != -1) {
          recoBin = (DeltaY_reco_best < 0) ? 0 : 1;
          int binNumber = 2 * genBin + recoBin;

          if(Mass_tt<500 && Mass_tt>=0 ){
            fill_histograms(event, "DY_0_500_recogenmatch_ele");
              if(binNumber == 0) {
              fill_histograms(event, "DY_Match_N_N_0_500_ele"); 
              }
              else if(binNumber == 1) {
                fill_histograms(event, "DY_Match_N_P_0_500_ele"); 
              }
              else if(binNumber == 2) {
                fill_histograms(event, "DY_Match_P_N_0_500_ele");
              }
              else if(binNumber == 3) {
                fill_histograms(event, "DY_Match_P_P_0_500_ele"); 
              }
              else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
                fill_histograms(event, "UnMatched_0_500_ele"); 
              }
          }

          if( Mass_tt>=500 && Mass_tt<750 ){
            fill_histograms(event, "DY_500_750_recogenmatch_ele");

            if(binNumber == 0) {
            fill_histograms(event, "DY_Match_N_N_500_750_ele"); 

            }
            else if(binNumber == 1) {
              fill_histograms(event, "DY_Match_N_P_500_750_ele"); 
            }
            else if(binNumber == 2) {
              fill_histograms(event, "DY_Match_P_N_500_750_ele");
            }
            else if(binNumber == 3) {
              fill_histograms(event, "DY_Match_P_P_500_750_ele"); 
            }
            else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
              fill_histograms(event, "UnMatched_500_750_ele"); 
            }
          }

          if( Mass_tt>=750 && Mass_tt<1000 ){
              fill_histograms(event, "DY_750_1000_recogenmatch_ele");
              if(binNumber == 0) {
              fill_histograms(event, "DY_Match_N_N_750_1000_ele"); 
              }
              else if(binNumber == 1) {
                fill_histograms(event, "DY_Match_N_P_750_1000_ele"); 
              }
              else if(binNumber == 2) {
                fill_histograms(event, "DY_Match_P_N_750_1000_ele");
              }
              else if(binNumber == 3) {
                fill_histograms(event, "DY_Match_P_P_750_1000_ele"); 
              }
              else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
                fill_histograms(event, "UnMatched_750_1000_ele"); 
              }
          }
                
          if( Mass_tt>=1000 && Mass_tt<1500 ){
              fill_histograms(event, "DY_1000_1500_recogenmatch_ele");
              if(binNumber == 0) {
              fill_histograms(event, "DY_Match_N_N_1000_1500_ele"); 
              }
              else if(binNumber == 1) {
                fill_histograms(event, "DY_Match_N_P_1000_1500_ele");   
              }
              else if(binNumber == 2) {
                fill_histograms(event, "DY_Match_P_N_1000_1500_ele"); 
              }
              else if(binNumber == 3) {
                fill_histograms(event, "DY_Match_P_P_1000_1500_ele"); 
              }
              else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
                fill_histograms(event, "UnMatched_1000_1500_ele"); 
              }
          }


          if( Mass_tt>=1500){
              fill_histograms(event, "DY_1500Inf_recogenmatch_ele");

              if(binNumber == 0) {
              fill_histograms(event, "DY_Match_N_N_1500Inf_ele"); 

              }
              else if(binNumber == 1) {
                fill_histograms(event, "DY_Match_N_P_1500Inf_ele"); 
    
              }
              else if(binNumber == 2) {
                fill_histograms(event, "DY_Match_P_N_1500Inf_ele");
    
              }
              else if(binNumber == 3) {
                fill_histograms(event, "DY_Match_P_P_1500Inf_ele"); 
    
              }
              else if(binNumber !=0 && binNumber !=1 && binNumber !=2 && binNumber !=3){
                fill_histograms(event, "UnMatched_1500Inf_ele"); 
    
              }
          }
          } 
          else {
            if(Mass_tt<500 && Mass_tt>=0){
              // The top gen particle wasn't reconstructed. Please ignore P_P part, there is no meaning behind it.
              fill_histograms(event, "DY_Mass_0_500_NOT_reco_ele");
            }
            if( Mass_tt>=500 && Mass_tt<750){
              fill_histograms(event, "DY_Mass_500_750_NOT_reco_ele");
            }
            if( Mass_tt>=750 && Mass_tt<1000){
              fill_histograms(event, "DY_Mass_750_1000_NOT_reco_ele");
            }
            if(  Mass_tt>=1000 && Mass_tt<1500){
              fill_histograms(event, "DY_Mass_1000_1500_NOT_reco_ele");
            }
            if( Mass_tt>=1500){
              fill_histograms(event, "DY_Mass_1500Inf_NOT_reco_ele");
            }
          }
          }
      }
      if(debug) cout << "22" << endl;
    // ===== ELECTRON END ==== 
    // electron bracket 
    }
    if(debug) cout << "23" << endl;
    
  }
    }
  }

  // if(!isEleTriggerMeasurement) SystematicsModule->process(event);


  return true;
}

UHH2_REGISTER_ANALYSIS_MODULE(ZprimeAnalysisModule_applyNN)
