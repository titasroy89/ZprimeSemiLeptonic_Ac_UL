
//  importing libraries

#include <algorithm>
#include <iterator>
#include <TROOT.h>
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TLatex.h>
#include "TCanvas.h"
#include "RooPlot.h"
#include "TTree.h"
#include "TH1D.h"
#include "TH1D.h"
#include "THStack.h"
#include "TRandom.h"
#include "TUnfoldDensity.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TFrame.h"
#include "TPaveLabel.h"
#include "TPad.h"
#include "TLegend.h"
#include "TRandom3.h"
#include "TFile.h"
#include "TMath.h"

using namespace RooFit ;

void nom_sys_DY()

{

    gStyle->SetOptStat(0);

    // A chain is a collection of files containing TTree objects. 
    // TChain(const char *name, const char *title="", Mode mode=kWithGlobalRegistration or kWithoutGlobalReg)
    // TTree tree(name, title)

    TChain *reco = new TChain("AnalysisTree","");

    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Analysis_UL18_muon_new_massranges/nominal/DY.root");
    
    TTree *treereco = (TTree*) reco;

    cout << "Number of Events:"<< treereco-> GetEntries()<<endl;

    
    // TH1D DeltaY Plots


    //DeltaY reco 
  
    TFile *file = TFile::Open("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Analysis_UL18_muon_new_massranges/nominal/DY.root"); 
    TH1D *h_DeltaY_reco = (TH1D*) file->Get("DeltaY_reco_750_1000_muon_General/DeltaY_reco");



   // TH1F Pileup 
    
    TH1D *h_weight_pu = new TH1D("weight_pu","weight_pu",1,-1,1);
    TH1D *h_weight_pu_down = new TH1D("weight_pu_down","weight_pu_down",1,-1,1);
    TH1D *h_weight_pu_up = new TH1D("weight_pu_up","weight_pu_up",1,-1,1);

    // TH1F Muon ID 
    
    TH1D *h_weight_sfmu_id = new TH1D("weight_sfmu_id","weight_sfmu_id",1,-1,1);
    TH1D *h_weight_sfmu_id_down = new TH1D("weight_sfmu_id_down","weight_sfmu_id_down",1,-1,1);
    TH1D *h_weight_sfmu_id_up = new TH1D("weight_sfmu_id_up","weight_sfmu_id_up",1,-1,1);

    // TH1F Muon Reconstruction

    TH1D *h_muonrecSF_nominal = new TH1D("muonrecSF_nominal","muonrecSF_nominal",1,-1,1);
    TH1D *h_muonrecSF_down = new TH1D("muonrecSF_down","muonrecSF_down",1,-1,1);
    TH1D *h_muonrecSF_up = new TH1D("muonrecSF_up","muonrecSF_up",1,-1,1);

    
    // TH1F Muon Trigger
    TH1D *h_weight_sfmu_trigger = new TH1D("weight_sfmu_trigger","weight_sfmu_trigger",1,-1,1);
    TH1D *h_weight_sfmu_trigger_down = new TH1D("weight_sfmu_trigger_down","weight_sfmu_trigger_down",1,-1,1);
    TH1D *h_weight_sfmu_trigger_up = new TH1D("weight_sfmu_trigger_up","weight_sfmu_trigger_up",1,-1,1);

    
    // TH1F Muon Isolation
    TH1D *h_weight_sfmu_iso = new TH1D("weight_sfmu_iso","weight_sfmu_iso",1,-1,1);
    TH1D *h_weight_sfmu_iso_down = new TH1D("weight_sfmu_iso_down","weight_sfmu_iso_down",1,-1,1);
    TH1D *h_weight_sfmu_iso_up = new TH1D("weight_sfmu_iso_up","weight_sfmu_iso_up",1,-1,1);

    
    // TH1F Electron Reconstruction

    TH1D *h_weight_sfelec_reco = new TH1D("weight_sfelec_reco","weight_sfelec_reco",1,-1,1);
    TH1D *h_weight_sfelec_reco_down = new TH1D("weight_sfelec_reco_down","weight_sfelec_reco_down",1,-1,1);
    TH1D *h_weight_sfelec_reco_up = new TH1D("weight_sfelec_reco_up","weight_sfelec_reco_up",1,-1,1);

   
    // TH1F Electron ID+isolation
    TH1D *h_weight_sfelec_id = new TH1D("weight_sfelec_id","weight_sfelec_id",1,-1,1);
    TH1D *h_weight_sfelec_id_down = new TH1D("weight_sfelec_id_down","weight_sfelec_id_down",1,-1,1);
    TH1D *h_weight_sfelec_id_up = new TH1D("weight_sfelec_id_up","weight_sfelec_id_up",1,-1,1);

    //Trigger Prefiring

    TH1D *h_prefiringWeight = new TH1D("prefiringWeight","prefiringWeight",1,-1,1);
    TH1D *h_prefiringWeightDown = new TH1D("prefiringWeightDown","prefiringWeightDown",1,-1,1);
    TH1D *h_prefiringWeightUp = new TH1D("prefiringWeightUp","prefiringWeightUp",1,-1,1);


 //Btagging Discriminator

    TH1D *h_weight_btagdisc_central = new TH1D("weight_btagdisc_central","weight_btagdisc_central",1,-1,1);
    TH1D *h_weight_btagdisc_cferr1_down = new TH1D("weight_btagdisc_cferr1_down","weight_btagdisc_cferr1_down",1,-1,1);
    TH1D *h_weight_btagdisc_cferr1_up = new TH1D("weight_btagdisc_cferr1_up","weight_btagdisc_cferr1_up",1,-1,1);
    TH1D *h_weight_btagdisc_cferr2_down = new TH1D("weight_btagdisc_cferr2_down","weight_btagdisc_cferr2_down",1,-1,1);
    TH1D *h_weight_btagdisc_cferr2_up = new TH1D("weight_btagdisc_cferr2_up","weight_btagdisc_cferr2_up",1,-1,1);
    TH1D *h_weight_btagdisc_hf_down = new TH1D("weight_btagdisc_hf_down","weight_btagdisc_hf_down",1,-1,1);
    TH1D *h_weight_btagdisc_hf_up = new TH1D("weight_btagdisc_hf_up","weight_btagdisc_hf_up",1,-1,1);
    TH1D *h_weight_btagdisc_hfstats1_down = new TH1D("weight_btagdisc_hfstats1_down","weight_btagdisc_hfstats1_down",1,-1,1);
    TH1D *h_weight_btagdisc_hfstats1_up = new TH1D("weight_btagdisc_hfstats1_up","weight_btagdisc_hfstats1_up",1,-1,1);
    TH1D *h_weight_btagdisc_hfstats2_down = new TH1D("weight_btagdisc_hfstats2_down","weight_btagdisc_hfstats2_down",1,-1,1);
    TH1D *h_weight_btagdisc_hfstats2_up = new TH1D("weight_btagdisc_hfstats2_up","weight_btagdisc_hfstats2_up",1,-1,1);
    TH1D *h_weight_btagdisc_lf_down = new TH1D("weight_btagdisc_lf_down","weight_btagdisc_lf_down",1,-1,1);
    TH1D *h_weight_btagdisc_lf_up = new TH1D("weight_btagdisc_lf_up","weight_btagdisc_lf_up",1,-1,1);
    TH1D *h_weight_btagdisc_lfstats1_down = new TH1D("weight_btagdisc_lfstats1_down","weight_btagdisc_lfstats1_down",1,-1,1);
    TH1D *h_weight_btagdisc_lfstats1_up = new TH1D("weight_btagdisc_lfstats1_up","weight_btagdisc_lfstats1_up",1,-1,1);
    TH1D *h_weight_btagdisc_lfstats2_down = new TH1D("weight_btagdisc_lfstats2_down","weight_btagdisc_lfstats2_down",1,-1,1);
    TH1D *h_weight_btagdisc_lfstats2_up = new TH1D("weight_btagdisc_lfstats2_up","weight_btagdisc_lfstats2_up",1,-1,1);

    //mu_r mu_f

    TH1D *h_weight_murmuf_downdown = new TH1D("weight_murmuf_downdown","weight_murmuf_downdown",1,-1,1);
    TH1D *h_weight_murmuf_downnone = new TH1D("weight_murmuf_downnone","weight_murmuf_downnone",1,-1,1);
    TH1D *h_weight_murmuf_nonedown = new TH1D("weight_murmuf_nonedown","weight_murmuf_nonedown",1,-1,1);
    TH1D *h_weight_murmuf_noneup = new TH1D("weight_murmuf_noneup","weight_murmuf_noneup",1,-1,1);
    TH1D *h_weight_murmuf_upnone = new TH1D("weight_murmuf_upnone","weight_murmuf_upnone",1,-1,1);
    TH1D *h_weight_murmuf_upup = new TH1D("weight_murmuf_upup","weight_murmuf_upup",1,-1,1);
    TH1D *h_weight_murmuf_dyn1_downdown = new TH1D("weight_murmuf_dyn1_downdown","weight_murmuf_dyn1_downdown",1,-1,1);
    TH1D *h_weight_murmuf_dyn1_downnone = new TH1D("weight_murmuf_dyn1_downnone","weight_murmuf_dyn1_downnone",1,-1,1);
    TH1D *h_weight_murmuf_dyn1_nonedown = new TH1D("weight_murmuf_dyn1_nonedown","weight_murmuf_dyn1_nonedown",1,-1,1);
    TH1D *h_weight_murmuf_dyn1_noneup = new TH1D("weight_murmuf_dyn1_noneup","weight_murmuf_dyn1_noneup",1,-1,1);
    TH1D *h_weight_murmuf_dyn1_upnone = new TH1D("weight_murmuf_dyn1_upnone","weight_murmuf_dyn1_upnone",1,-1,1);
    TH1D *h_weight_murmuf_dyn1_upup = new TH1D("weight_murmuf_dyn1_upup","weight_murmuf_dyn1_upup",1,-1,1);
    TH1D *h_weight_murmuf_dyn2_downdown = new TH1D("weight_murmuf_dyn2_downdown","weight_murmuf_dyn2_downdown",1,-1,1);
    TH1D *h_weight_murmuf_dyn2_downnone = new TH1D("h_weight_murmuf_dyn2_downnone","h_weight_murmuf_dyn2_downnone",1,-1,1);
    TH1D *h_weight_murmuf_dyn2_nonedown = new TH1D("weight_murmuf_dyn2_nonedown","weight_murmuf_dyn2_nonedown",1,-1,1);
    TH1D *h_weight_murmuf_dyn2_noneup = new TH1D("weight_murmuf_dyn2_noneup","weight_murmuf_dyn2_noneup",1,-1,1);
    TH1D *h_weight_murmuf_dyn2_upnone = new TH1D("weight_murmuf_dyn2_upnone","weight_murmuf_dyn2_upnone",1,-1,1);
    TH1D *h_weight_murmuf_dyn2_upup = new TH1D("weight_murmuf_dyn2_upup","weight_murmuf_dyn2_upup",1,-1,1);
    TH1D *h_weight_murmuf_dyn3_downdown = new TH1D("weight_murmuf_dyn3_downdown","weight_murmuf_dyn3_downdown",1,-1,1);
    TH1D *h_weight_murmuf_dyn3_downnone = new TH1D("weight_murmuf_dyn3_downnone","weight_murmuf_dyn3_downnone",1,-1,1);
    TH1D *h_weight_murmuf_dyn3_nonedown = new TH1D("weight_murmuf_dyn3_nonedown","weight_murmuf_dyn3_nonedown",1,-1,1);
    TH1D *h_weight_murmuf_dyn3_noneup = new TH1D("weight_murmuf_dyn3_noneup","weight_murmuf_dyn3_noneup",1,-1,1);
    TH1D *h_weight_murmuf_dyn3_upnone = new TH1D("weight_murmuf_dyn3_upnone","weight_murmuf_dyn3_upnone",1,-1,1);
    TH1D *h_weight_murmuf_dyn3_upup = new TH1D("weight_murmuf_dyn3_upup","weight_murmuf_dyn3_upup",1,-1,1);
    TH1D *h_weight_murmuf_dyn4_downdown = new TH1D("weight_murmuf_dyn4_downdown","weight_murmuf_dyn4_downdown",1,-1,1);
    TH1D *h_weight_murmuf_dyn4_downnone = new TH1D("weight_murmuf_dyn4_downnone","weight_murmuf_dyn4_downnone",1,-1,1);
    TH1D *h_weight_murmuf_dyn4_nonedown = new TH1D("weight_murmuf_dyn4_nonedown","weight_murmuf_dyn4_nonedown",1,-1,1);
    TH1D *h_weight_murmuf_dyn4_noneup = new TH1D("weight_murmuf_dyn4_noneup","weight_murmuf_dyn4_noneup",1,-1,1);
    TH1D *h_weight_murmuf_dyn4_upnone = new TH1D("weight_murmuf_dyn4_upnone","weight_murmuf_dyn4_upnone",1,-1,1);
    TH1D *h_weight_murmuf_dyn4_upup = new TH1D("weight_murmuf_dyn4_upup","weight_murmuf_dyn4_upup",1,-1,1);



    float weight_pu;
    float weight_pu_down;
    float weight_pu_up;
    
    float weight_sfmu_id;
    float weight_sfmu_id_down;
    float weight_sfmu_id_up;

    float muonrecSF_nominal;
    float muonrecSF_down;
    float muonrecSF_up;
    
    float weight_sfmu_trigger;
    float weight_sfmu_trigger_down;
    float weight_sfmu_trigger_up;

    float weight_sfmu_iso;
    float weight_sfmu_iso_down;
    float weight_sfmu_iso_up;

    float weight_sfelec_reco;
    float weight_sfelec_reco_down;
    float weight_sfelec_reco_up;

    float weight_sfelec_id;
    float weight_sfelec_id_down;
    float weight_sfelec_id_up;

    float prefiringWeight;
    float prefiringWeightDown;
    float prefiringWeightUp;

    float weight_btagdisc_central;
    float weight_btagdisc_cferr1_down;
    float weight_btagdisc_cferr1_up;
    float weight_btagdisc_cferr2_down;
    float weight_btagdisc_cferr2_up;
    float weight_btagdisc_hf_down;
    float weight_btagdisc_hf_up;
    float weight_btagdisc_hfstats1_down;
    float weight_btagdisc_hfstats1_up;
    float weight_btagdisc_hfstats2_down;
    float weight_btagdisc_hfstats2_up;
    float weight_btagdisc_lf_down;
    float weight_btagdisc_lf_up;
    float weight_btagdisc_lfstats1_down;
    float weight_btagdisc_lfstats1_up;
    float weight_btagdisc_lfstats2_down;
    float weight_btagdisc_lfstats2_up;


    float weight_murmuf_downdown;
    float weight_murmuf_downnone;
    float weight_murmuf_nonedown;
    float weight_murmuf_noneup;
    float weight_murmuf_upnone;
    float weight_murmuf_upup;
    float weight_murmuf_dyn1_downdown;
    float weight_murmuf_dyn1_downnone;
    float weight_murmuf_dyn1_nonedown;
    float weight_murmuf_dyn1_noneup;
    float weight_murmuf_dyn1_upnone;
    float weight_murmuf_dyn1_upup;
    float weight_murmuf_dyn2_downdown;
    float weight_murmuf_dyn2_downnone;
    float weight_murmuf_dyn2_nonedown;
    float weight_murmuf_dyn2_noneup;
    float weight_murmuf_dyn2_upnone;
    float weight_murmuf_dyn2_upup;
    float weight_murmuf_dyn3_downdown;
    float weight_murmuf_dyn3_downnone;
    float weight_murmuf_dyn3_nonedown;
    float weight_murmuf_dyn3_noneup;
    float weight_murmuf_dyn3_upnone;
    float weight_murmuf_dyn3_upup;
    float weight_murmuf_dyn4_downdown;
    float weight_murmuf_dyn4_downnone;
    float weight_murmuf_dyn4_nonedown;
    float weight_murmuf_dyn4_noneup;
    float weight_murmuf_dyn4_upnone;
    float weight_murmuf_dyn4_upup;
    

    treereco->SetBranchAddress("weight_pu", &weight_pu);
    treereco->SetBranchAddress("weight_pu_down", &weight_pu_down);
    treereco->SetBranchAddress("weight_pu_up", &weight_pu_up);

    treereco->SetBranchAddress("weight_sfmu_id", &weight_sfmu_id);
    treereco->SetBranchAddress("weight_sfmu_id_down", &weight_sfmu_id_down);
    treereco->SetBranchAddress("weight_sfmu_id_up", &weight_sfmu_id_up);

    treereco->SetBranchAddress("weight_sfmu_trigger", &weight_sfmu_trigger);
    treereco->SetBranchAddress("weight_sfmu_trigger_down", &weight_sfmu_trigger_down);
    treereco->SetBranchAddress("weight_sfmu_trigger_up", &weight_sfmu_trigger_up);

    treereco->SetBranchAddress("weight_sfmu_iso", &weight_sfmu_iso);
    treereco->SetBranchAddress("weight_sfmu_iso_down", &weight_sfmu_iso_down);
    treereco->SetBranchAddress("weight_sfmu_iso_up", &weight_sfmu_iso_up);

    treereco->SetBranchAddress("weight_sfelec_reco", &weight_sfelec_reco);
    treereco->SetBranchAddress("weight_sfelec_reco_down", &weight_sfelec_reco_down);
    treereco->SetBranchAddress("weight_sfelec_reco_up", &weight_sfelec_reco_up);

    treereco->SetBranchAddress("weight_sfelec_id", &weight_sfelec_id);
    treereco->SetBranchAddress("weight_sfelec_id_down", &weight_sfelec_id_down);
    treereco->SetBranchAddress("weight_sfelec_id_up", &weight_sfelec_id_up);

    treereco->SetBranchAddress("prefiringWeight", &prefiringWeight);
    treereco->SetBranchAddress("prefiringWeightDown", &prefiringWeightDown);
    treereco->SetBranchAddress("prefiringWeightUp", &prefiringWeightUp);

    treereco->SetBranchAddress("weight_btagdisc_central", &weight_btagdisc_central);
    treereco->SetBranchAddress("weight_btagdisc_cferr1_down", &weight_btagdisc_cferr1_down);
    treereco->SetBranchAddress("weight_btagdisc_cferr1_up", &weight_btagdisc_cferr1_up);
    treereco->SetBranchAddress("weight_btagdisc_cferr2_down", &weight_btagdisc_cferr2_down);
    treereco->SetBranchAddress("weight_btagdisc_cferr2_up", &weight_btagdisc_cferr2_up);
    treereco->SetBranchAddress("weight_btagdisc_hf_down", &weight_btagdisc_hf_down);
    treereco->SetBranchAddress("weight_btagdisc_hf_up", &weight_btagdisc_hf_up);
    treereco->SetBranchAddress("weight_btagdisc_hfstats1_down", &weight_btagdisc_hfstats1_down);
    treereco->SetBranchAddress("weight_btagdisc_hfstats1_up", &weight_btagdisc_hfstats1_up);
    treereco->SetBranchAddress("weight_btagdisc_hfstats2_down", &weight_btagdisc_hfstats2_down);
    treereco->SetBranchAddress("weight_btagdisc_hfstats2_up", &weight_btagdisc_hfstats2_up);
    treereco->SetBranchAddress("weight_btagdisc_lf_down", &weight_btagdisc_lf_down);
    treereco->SetBranchAddress("weight_btagdisc_lf_up", &weight_btagdisc_lf_up);
    treereco->SetBranchAddress("weight_btagdisc_lfstats1_down", &weight_btagdisc_lfstats1_down);
    treereco->SetBranchAddress("weight_btagdisc_lfstats1_up", &weight_btagdisc_lfstats1_up);
    treereco->SetBranchAddress("weight_btagdisc_lfstats2_down", &weight_btagdisc_lfstats2_down);
    treereco->SetBranchAddress("weight_btagdisc_lfstats2_up", &weight_btagdisc_lfstats2_up);

    treereco->SetBranchAddress("weight_murmuf_downdown", &weight_murmuf_downdown);
    treereco->SetBranchAddress("weight_murmuf_downnone", &weight_murmuf_downnone);
    treereco->SetBranchAddress("weight_murmuf_nonedown", &weight_murmuf_nonedown);
    treereco->SetBranchAddress("weight_murmuf_noneup", &weight_murmuf_noneup);
    treereco->SetBranchAddress("weight_murmuf_upnone", &weight_murmuf_upnone);
    treereco->SetBranchAddress("weight_murmuf_upup", &weight_murmuf_upup);
    treereco->SetBranchAddress("weight_murmuf_dyn1_downdown", &weight_murmuf_dyn1_downdown);
    treereco->SetBranchAddress("weight_murmuf_dyn1_downnone", &weight_murmuf_dyn1_downnone);
    treereco->SetBranchAddress("weight_murmuf_dyn1_nonedown", &weight_murmuf_dyn1_nonedown);
    treereco->SetBranchAddress("weight_murmuf_dyn1_noneup", &weight_murmuf_dyn1_noneup);
    treereco->SetBranchAddress("weight_murmuf_dyn1_upnone", &weight_murmuf_dyn1_upnone);
    treereco->SetBranchAddress("weight_murmuf_dyn1_upup", &weight_murmuf_dyn1_upup);
    treereco->SetBranchAddress("weight_murmuf_dyn2_downdown", &weight_murmuf_dyn2_downdown);
    treereco->SetBranchAddress("weight_murmuf_dyn2_downnone", &weight_murmuf_dyn2_downnone);
    treereco->SetBranchAddress("weight_murmuf_dyn2_nonedown", &weight_murmuf_dyn2_nonedown);
    treereco->SetBranchAddress("weight_murmuf_dyn2_noneup", &weight_murmuf_dyn2_noneup);
    treereco->SetBranchAddress("weight_murmuf_dyn2_upnone", &weight_murmuf_dyn2_upnone);
    treereco->SetBranchAddress("weight_murmuf_dyn2_upup", &weight_murmuf_dyn2_upup);
    treereco->SetBranchAddress("weight_murmuf_dyn3_downdown", &weight_murmuf_dyn3_downdown);
    treereco->SetBranchAddress("weight_murmuf_dyn3_downnone", &weight_murmuf_dyn3_downnone);
    treereco->SetBranchAddress("weight_murmuf_dyn3_nonedown", &weight_murmuf_dyn3_nonedown);
    treereco->SetBranchAddress("weight_murmuf_dyn3_noneup", &weight_murmuf_dyn3_noneup);
    treereco->SetBranchAddress("weight_murmuf_dyn3_upnone", &weight_murmuf_dyn3_upnone);
    treereco->SetBranchAddress("weight_murmuf_dyn3_upup", &weight_murmuf_dyn3_upup);
    treereco->SetBranchAddress("weight_murmuf_dyn4_downdown", &weight_murmuf_dyn4_downdown);
    treereco->SetBranchAddress("weight_murmuf_dyn4_downnone", &weight_murmuf_dyn4_downnone);
    treereco->SetBranchAddress("weight_murmuf_dyn4_nonedown", &weight_murmuf_dyn4_nonedown);
    treereco->SetBranchAddress("weight_murmuf_dyn4_noneup", &weight_murmuf_dyn4_noneup);
    treereco->SetBranchAddress("weight_murmuf_dyn4_upnone", &weight_murmuf_dyn4_upnone);
    treereco->SetBranchAddress("weight_murmuf_dyn4_upup", &weight_murmuf_dyn4_upup);


    for (Int_t i = 0; i < treereco->GetEntries(); i++){
    // for (Int_t i = 0; i < 10000; i++){

        treereco->GetEntry(i);
        if (i%1000000 == 0) std::cout << "--- ... Processing event: " << i <<std::endl;
       

        h_weight_pu->Fill(weight_pu);
        h_weight_pu_down->Fill(weight_pu_down);
        h_weight_pu_up->Fill(weight_pu_up);
        
        h_weight_sfmu_id->Fill(weight_sfmu_id);
        h_weight_sfmu_id_down->Fill(weight_sfmu_id_down);
        h_weight_sfmu_id_up->Fill(weight_sfmu_id_up);

        h_weight_sfmu_trigger->Fill(weight_sfmu_trigger); 
        h_weight_sfmu_trigger_down->Fill(weight_sfmu_trigger_down); 
        h_weight_sfmu_trigger_up->Fill(weight_sfmu_trigger_up); 

        h_weight_sfmu_iso->Fill(weight_sfmu_iso); 
        h_weight_sfmu_iso_down->Fill(weight_sfmu_iso_down); 
        h_weight_sfmu_iso_up->Fill(weight_sfmu_iso_up);

        h_weight_sfelec_reco->Fill(weight_sfelec_reco);
        h_weight_sfelec_reco_down->Fill(weight_sfelec_reco_down);
        h_weight_sfelec_reco_up->Fill(weight_sfelec_reco_up); 

        h_weight_sfelec_id->Fill(weight_sfelec_id);
        h_weight_sfelec_id_down->Fill(weight_sfelec_id_down); 
        h_weight_sfelec_id_up->Fill(weight_sfelec_id_up); 

        h_prefiringWeight->Fill(prefiringWeight);
        h_prefiringWeightDown->Fill(prefiringWeightDown); 
        h_prefiringWeightUp->Fill(prefiringWeightUp); 

        h_weight_btagdisc_central->Fill(weight_btagdisc_central); 
        h_weight_btagdisc_cferr1_down->Fill(weight_btagdisc_cferr1_down); 
        h_weight_btagdisc_cferr1_up->Fill(weight_btagdisc_cferr1_up); 
        h_weight_btagdisc_cferr2_down->Fill(weight_btagdisc_cferr2_down); 
        h_weight_btagdisc_cferr2_up->Fill(weight_btagdisc_cferr2_up); 
        h_weight_btagdisc_hf_down->Fill(weight_btagdisc_hf_down); 
        h_weight_btagdisc_hf_up->Fill(weight_btagdisc_hf_up); 
        h_weight_btagdisc_hfstats1_down->Fill(weight_btagdisc_hfstats1_down); 
        h_weight_btagdisc_hfstats1_up->Fill(weight_btagdisc_hfstats1_up); 
        h_weight_btagdisc_hfstats2_down->Fill(weight_btagdisc_hfstats2_down); 
        h_weight_btagdisc_hfstats2_up->Fill(weight_btagdisc_hfstats2_up); 
        h_weight_btagdisc_lf_down->Fill(weight_btagdisc_lf_down); 
        h_weight_btagdisc_lf_up->Fill(weight_btagdisc_lf_up); 
        h_weight_btagdisc_lfstats1_down->Fill(weight_btagdisc_lfstats1_down); 
        h_weight_btagdisc_lfstats1_up->Fill(weight_btagdisc_lfstats1_up); 
        h_weight_btagdisc_lfstats2_down->Fill(weight_btagdisc_lfstats2_down); 
        h_weight_btagdisc_lfstats2_up->Fill(weight_btagdisc_lfstats2_up); 


        h_weight_murmuf_downdown->Fill(weight_murmuf_downdown); 
        h_weight_murmuf_downnone->Fill(weight_murmuf_downnone); 
        h_weight_murmuf_nonedown->Fill(weight_murmuf_nonedown); 
        h_weight_murmuf_noneup->Fill(weight_murmuf_noneup); 
        h_weight_murmuf_upnone->Fill(weight_murmuf_upnone); 
        h_weight_murmuf_upup->Fill(weight_murmuf_upup); 
        h_weight_murmuf_dyn1_downdown->Fill(weight_murmuf_dyn1_downdown); 
        h_weight_murmuf_dyn1_downnone->Fill(weight_murmuf_dyn1_downnone); 
        h_weight_murmuf_dyn1_nonedown->Fill(weight_murmuf_dyn1_nonedown); 
        h_weight_murmuf_dyn1_noneup->Fill(weight_murmuf_dyn1_noneup); 
        h_weight_murmuf_dyn1_upnone->Fill(weight_murmuf_dyn1_upnone); 
        h_weight_murmuf_dyn1_upup->Fill(weight_murmuf_dyn1_upup); 
        h_weight_murmuf_dyn2_downdown->Fill(weight_murmuf_dyn2_downdown); 
        h_weight_murmuf_dyn2_downnone->Fill(weight_murmuf_dyn2_downnone); 
        h_weight_murmuf_dyn2_nonedown->Fill(weight_murmuf_dyn2_nonedown); 
        h_weight_murmuf_dyn2_noneup->Fill(weight_murmuf_dyn2_noneup); 
        h_weight_murmuf_dyn2_upnone->Fill(weight_murmuf_dyn2_upnone); 
        h_weight_murmuf_dyn2_upup->Fill(weight_murmuf_dyn2_upup); 
        h_weight_murmuf_dyn3_downdown->Fill(weight_murmuf_dyn3_downdown); 
        h_weight_murmuf_dyn3_downnone->Fill(weight_murmuf_dyn3_downnone); 
        h_weight_murmuf_dyn3_nonedown->Fill(weight_murmuf_dyn3_nonedown); 
        h_weight_murmuf_dyn3_noneup->Fill(weight_murmuf_dyn3_noneup); 
        h_weight_murmuf_dyn3_upnone->Fill(weight_murmuf_dyn3_upnone); 
        h_weight_murmuf_dyn3_upup->Fill(weight_murmuf_dyn3_upup); 
        h_weight_murmuf_dyn4_downdown->Fill(weight_murmuf_dyn4_downdown); 
        h_weight_murmuf_dyn4_downnone->Fill(weight_murmuf_dyn4_downnone); 
        h_weight_murmuf_dyn4_nonedown->Fill(weight_murmuf_dyn4_nonedown); 
        h_weight_murmuf_dyn4_noneup->Fill(weight_murmuf_dyn4_noneup); 
        h_weight_murmuf_dyn4_upnone->Fill(weight_murmuf_dyn4_upnone); 
        h_weight_murmuf_dyn4_upup->Fill(weight_murmuf_dyn4_upup); 


    }


  // --------------- Output File ------------------

    TFile* myFile = new TFile("dY_UL18_muon_750_1000_DY.root", "RECREATE");
    

    h_DeltaY_reco->Write();

    h_weight_pu->Write();
    h_weight_pu_down->Write();
    h_weight_pu_up->Write();

    h_weight_sfmu_id->Write();
    h_weight_sfmu_id_down->Write();
    h_weight_sfmu_id_up->Write();

    h_weight_sfmu_trigger->Write();
    h_weight_sfmu_trigger_down->Write(); 
    h_weight_sfmu_trigger_up->Write();

    h_weight_sfmu_iso->Write();
    h_weight_sfmu_iso_down->Write();
    h_weight_sfmu_iso_up->Write();

    h_weight_sfelec_reco->Write();
    h_weight_sfelec_reco_down->Write();
    h_weight_sfelec_reco_up->Write();

    h_weight_sfelec_id->Write();
    h_weight_sfelec_id_down->Write();
    h_weight_sfelec_id_up->Write();

    h_prefiringWeight->Write();
    h_prefiringWeightDown->Write();
    h_prefiringWeightUp->Write();

    h_weight_btagdisc_central->Write();
    h_weight_btagdisc_cferr1_down->Write();
    h_weight_btagdisc_cferr1_up->Write(); 
    h_weight_btagdisc_cferr2_down->Write();
    h_weight_btagdisc_cferr2_up->Write();
    h_weight_btagdisc_hf_down->Write();
    h_weight_btagdisc_hf_up->Write();
    h_weight_btagdisc_hfstats1_down->Write();
    h_weight_btagdisc_hfstats1_up->Write();
    h_weight_btagdisc_hfstats2_down->Write();
    h_weight_btagdisc_hfstats2_up->Write();
    h_weight_btagdisc_lf_down->Write();
    h_weight_btagdisc_lf_up->Write();
    h_weight_btagdisc_lfstats1_down->Write();
    h_weight_btagdisc_lfstats1_up->Write();
    h_weight_btagdisc_lfstats2_down->Write();
    h_weight_btagdisc_lfstats2_up->Write();


    h_weight_murmuf_downdown->Write();
    h_weight_murmuf_downnone->Write();
    h_weight_murmuf_nonedown->Write();
    h_weight_murmuf_noneup->Write();
    h_weight_murmuf_upnone->Write();
    h_weight_murmuf_upup->Write();
    h_weight_murmuf_dyn1_downdown->Write();
    h_weight_murmuf_dyn1_downnone->Write();
    h_weight_murmuf_dyn1_nonedown->Write();
    h_weight_murmuf_dyn1_noneup->Write();
    h_weight_murmuf_dyn1_upnone->Write();
    h_weight_murmuf_dyn1_upup->Write();
    h_weight_murmuf_dyn2_downdown->Write();
    h_weight_murmuf_dyn2_downnone->Write();
    h_weight_murmuf_dyn2_nonedown->Write(); 
    h_weight_murmuf_dyn2_noneup->Write();
    h_weight_murmuf_dyn2_upnone->Write(); 
    h_weight_murmuf_dyn2_upup->Write();
    h_weight_murmuf_dyn3_downdown->Write();
    h_weight_murmuf_dyn3_downnone->Write();
    h_weight_murmuf_dyn3_nonedown->Write();
    h_weight_murmuf_dyn3_noneup->Write();
    h_weight_murmuf_dyn3_upnone->Write();
    h_weight_murmuf_dyn3_upup->Write();
    h_weight_murmuf_dyn4_downdown->Write();
    h_weight_murmuf_dyn4_downnone->Write();
    h_weight_murmuf_dyn4_nonedown->Write();
    h_weight_murmuf_dyn4_noneup->Write();
    h_weight_murmuf_dyn4_upnone->Write();
    h_weight_murmuf_dyn4_upup->Write();

    TDirectory* dirMiddle = (TDirectory*)file->Get("Middle_General");
    TDirectory* dirLast = (TDirectory*)file->Get("Last_General");

  if (dirMiddle) {
        TDirectory* newDirMiddle = myFile->mkdir("Middle");
        newDirMiddle->cd(); // change to the new directory in the output file
        TList* list = dirMiddle->GetListOfKeys();
        TIter next(list);
        TKey* key;
        while ((key = (TKey*)next())) {
            TObject* obj = key->ReadObj();
            if (obj) {
                obj->Write();
                delete obj;
            } else {
                std::cerr << "Error reading object from 'Middle' directory!" << std::endl;
            }
        }
    } else {
        std::cerr << "No 'Middle' directory found in input file!" << std::endl;
    }
    if (dirLast) {
        TDirectory* newDirLast = myFile->mkdir("Last");
        newDirLast->cd(); // change to the new directory in the output file
        TList* list = dirLast->GetListOfKeys();
        TIter next(list);
        TKey* key;
        while ((key = (TKey*)next())) {
            TObject* obj = key->ReadObj();
            if (obj) {
                obj->Write();
                delete obj;
            } else {
                std::cerr << "Error reading object from 'Last' directory!" << std::endl;
            }
        }
    } else {
        std::cerr << "No 'Last' directory found in input file!" << std::endl;
    }
    

    myFile->Close();
    file->Close();

}


