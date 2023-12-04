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
#include "TH1F.h"
#include "THStack.h"
#include "TRandom.h"
#include "TUnfoldDensity.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TFrame.h"
#include "TPaveLabel.h"
#include "TPad.h"
#include "TLegend.h"
#include "sigma.h"
#include "mean.h"
#include "TRandom3.h"

void all_unfolding_data(string var_name = "", string var_gen = "", string year = "")
{

//----obetener_toda_la_informacion_de_entrada--------??

    gStyle->SetOptStat(0);
    TChain *chreco_data = new TChain("AnalysisTree","");
    chreco_data->Add(Form("/nfs/dust/cms/user/hugobg/Zprime_102X/analysis_output/%s/muon/workdir_Zprime_Analysis_muon/uhh2.AnalysisModuleRunner.DATA.DATA.root/AnalysisTree",year.c_str()));
    TTree *treereco_data = (TTree*) chreco_data;

    TChain *chreco_ttbar = new TChain("AnalysisTree","");
    chreco_ttbar->Add(Form("/nfs/dust/cms/user/hugobg/Zprime_102X/analysis_output/%s/muon/workdir_Zprime_Analysis_muon/uhh2.AnalysisModuleRunner.MC.TTbar.root/AnalysisTree",year.c_str()));
    TTree *treereco_ttbar = (TTree*) chreco_ttbar;

    TChain *chreco_wjets = new TChain("AnalysisTree","");
    chreco_wjets->Add(Form("/nfs/dust/cms/user/hugobg/Zprime_102X/analysis_output/%s/muon/workdir_Zprime_Analysis_muon/uhh2.AnalysisModuleRunner.MC.WJets.root/AnalysisTree",year.c_str()));
    TTree *treereco_wjets = (TTree*) chreco_wjets;

    TChain *chreco_ST = new TChain("AnalysisTree","");
    chreco_ST->Add(Form("/nfs/dust/cms/user/hugobg/Zprime_102X/analysis_output/%s/muon/workdir_Zprime_Analysis_muon/uhh2.AnalysisModuleRunner.MC.ST.root/AnalysisTree",year.c_str()));
    TTree *treereco_ST = (TTree*) chreco_ST;

    TChain *chreco_DY = new TChain("AnalysisTree","");
    chreco_DY->Add(Form("/nfs/dust/cms/user/hugobg/Zprime_102X/analysis_output/%s/muon/workdir_Zprime_Analysis_muon/uhh2.AnalysisModuleRunner.MC.DYJets.root/AnalysisTree",year.c_str()));
    TTree *treereco_DY = (TTree*) chreco_DY;

    TChain *chreco_QCD = new TChain("AnalysisTree","");
    chreco_QCD->Add(Form("/nfs/dust/cms/user/hugobg/Zprime_102X/analysis_output/%s/muon/workdir_Zprime_Analysis_muon/uhh2.AnalysisModuleRunner.MC.QCD.root/AnalysisTree",year.c_str()));
    TTree *treereco_QCD = (TTree*) chreco_QCD;

//array for variable 

    int len = 0; int len_rec = 0;
    if(var_name == "DeltaY") len = 9, len_rec = 15;
    if(var_name == "Mttbar") len = 8, len_rec = 13;   
    if(var_name == "Rapidity_ttbar") len = 13, len_rec = 23;
    if(var_name == "tlead_pT") len = 6, len_rec = 9;
    if(var_name == "pT_ttbar") len = 6, len_rec = 9;

    Float_t bins_gen[len];
    Float_t new_rec[len_rec];

    if(var_name == "pT_ttbar"){
        Float_t Bins_gen[] = {0,200,400,600,800,1200};
        Float_t New_rec[] = {0,200,300,400,500,600,700,800,1200};
        std::copy(Bins_gen, Bins_gen+len, bins_gen);
        std::copy(New_rec, New_rec+len_rec, new_rec);

    }

    if(var_name == "DeltaY"){ 
        Float_t Bins_gen[] = {-2.,-1.5,-1.,-0.5,0.,0.5,1.,1.5,2.};
        Float_t New_rec[] = {-2.,-1.5,-1.25,-1.,-0.75,-0.5,-0.25,0.,0.25,0.5,0.75,1.,1.25,1.5,2.};
        std::copy(Bins_gen, Bins_gen+len, bins_gen);
        std::copy(New_rec, New_rec+len_rec, new_rec);

    }
    if(var_name == "Mttbar"){
        Float_t Bins_gen[] = {880,1050,1300,1500,1800,2200,2600,4000};
        Float_t New_rec[] = {880,1050,1175,1300,1400,1500,1650,1800,2000,2200,2400,2600,4000};
        std::copy(Bins_gen, Bins_gen+len, bins_gen);
        std::copy(New_rec, New_rec+len_rec, new_rec);
    }

    if(var_name == "Rapidity_ttbar"){
        Float_t Bins_gen[] = {-2.4,-2.,-1.6,-1.2,-0.8,-0.4,0.0,0.4,0.8,1.2,1.6,2,2.4};
        Float_t New_rec[] = {-2.4,-2.,-1.8,-1.6,-1.4,-1.2,-1.,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1.,1.2,1.4,1.6,1.8,2,2.4};
        std::copy(Bins_gen, Bins_gen+len, bins_gen);
        std::copy(New_rec, New_rec+len_rec, new_rec);
    }

    if(var_name == "tlead_pT"){
        Float_t Bins_gen[] = {0,200,400,600,800,1200};
        Float_t New_rec[] = {0,200,300,400,500,600,700,800,1200};
        std::copy(Bins_gen, Bins_gen+len, bins_gen);
        std::copy(New_rec, New_rec+len_rec, new_rec);
    }

    Int_t  newrec = sizeof(new_rec)/sizeof(Float_t) - 1;
    Int_t  binnum_gen = sizeof(bins_gen)/sizeof(Float_t) - 1;

//-----Bacgrounds------??
    TH1F *Data = new TH1F("Data","",newrec,new_rec);
    TH1F *TTbar = new TH1F("TTbar","",newrec,new_rec);
    TH1F *WJets = new TH1F("WJets","",newrec,new_rec);
    TH1F *ST = new TH1F("ST","",newrec,new_rec);
    TH1F *DY = new TH1F("DY","",newrec,new_rec);
    TH1F *QCD = new TH1F("QCD","",newrec,new_rec);

//-------Syst----------??

    TH1F *ttbar_pu_up = new TH1F("ttbar_pu_up","",newrec,new_rec);
    TH1F *ttbar_pu_down  = new TH1F("ttbar_pu_down","",newrec,new_rec);
    TH1F *ttbar_cferr1_up = new TH1F("ttbar_cferr1_up","",newrec,new_rec);
    TH1F *ttbar_cferr1_down = new TH1F("ttbar_cferr1_down","",newrec,new_rec);
    TH1F *ttbar_cferr2_up = new TH1F("ttbar_cferr2_up","",newrec,new_rec);
    TH1F *ttbar_cferr2_down  = new TH1F("ttbar_cferr2_down","",newrec,new_rec);
    TH1F *ttbar_hf_up = new TH1F("ttbar_hf_up","",newrec,new_rec);
    TH1F *ttbar_hf_down  = new TH1F("ttbar_hf_down","",newrec,new_rec);
    TH1F *ttbar_hfstats1_up = new TH1F("ttbar_hfstats1_up","",newrec,new_rec);
    TH1F *ttbar_hfstats1_down  = new TH1F("ttbar_hfstats1_down","",newrec,new_rec);
    TH1F *ttbar_hfstats2_up = new TH1F("ttbar_hfstats2_up","",newrec,new_rec);
    TH1F *ttbar_hfstats2_down  = new TH1F("ttbar_hfstats2_down","",newrec,new_rec);
    TH1F *ttbar_jes_up = new TH1F("ttbar_jes_up","",newrec,new_rec);
    TH1F *ttbar_jes_down  = new TH1F("ttbar_jes_down","",newrec,new_rec);
    TH1F *ttbar_lf_up = new TH1F("ttbar_lf_up","",newrec,new_rec);
    TH1F *ttbar_lf_down  = new TH1F("ttbar_lf_down","",newrec,new_rec);
    TH1F *ttbar_lfstats1_up = new TH1F("ttbar_lfstats1_up","",newrec,new_rec);
    TH1F *ttbar_lfstats1_down  = new TH1F("ttbar_lfstats1_down","",newrec,new_rec);
    TH1F *ttbar_lfstats2_up = new TH1F("ttbar_lfstats2_up","",newrec,new_rec);
    TH1F *ttbar_lfstats2_down  = new TH1F("ttbar_lfstats2_down","",newrec,new_rec);
    TH1F *ttbar_MuonID_up  = new TH1F("ttbar_MuonID_up","",newrec,new_rec);
    TH1F *ttbar_MuonID_down  = new TH1F("ttbar_MuonID_down","",newrec,new_rec);
    TH1F *ttbar_Trigger_up  = new TH1F("ttbar_Trigger_up","",newrec,new_rec);
    TH1F *ttbar_Trigger_down  = new TH1F("ttbar_Trigger_down","",newrec,new_rec);

    TH2F *Migration_Matrix_pu = new TH2F("Migration_Matrix_pu","",newrec,new_rec,binnum_gen,bins_gen);
    TH2F *Migration_Matrix_cferr1 = new TH2F("Migration_Matrix_cferr1","",newrec,new_rec,binnum_gen,bins_gen);
    TH2F *Migration_Matrix_cferr2 = new TH2F("Migration_Matrix_cferr2","",newrec,new_rec,binnum_gen,bins_gen);
    TH2F *Migration_Matrix_hf = new TH2F("Migration_Matrix_hf","",newrec,new_rec,binnum_gen,bins_gen);
    TH2F *Migration_Matrix_hfstats1 = new TH2F("Migration_Matrix_hfstats1","",newrec,new_rec,binnum_gen,bins_gen);
    TH2F *Migration_Matrix_hfstats2 = new TH2F("Migration_Matrix_hfstats2","",newrec,new_rec,binnum_gen,bins_gen);
    TH2F *Migration_Matrix_jes = new TH2F("Migration_Matrix_jes","",newrec,new_rec,binnum_gen,bins_gen);
    TH2F *Migration_Matrix_lf = new TH2F("Migration_Matrix_lf","",newrec,new_rec,binnum_gen,bins_gen);
    TH2F *Migration_Matrix_lfstats1 = new TH2F("Migration_Matrix_lfstats1","",newrec,new_rec,binnum_gen,bins_gen);
    TH2F *Migration_Matrix_lfstats2 = new TH2F("Migration_Matrix_lfstats2","",newrec,new_rec,binnum_gen,bins_gen);


//--------Unfold----------??
    TH2F *Migration_Matrix = new TH2F("Migration_Matrix","",newrec,new_rec,binnum_gen,bins_gen);
    TH1F *Var_gen = new TH1F("Var_gen","",binnum_gen,bins_gen);


//---------selection_cuts && weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*s --------??

    string selcuts = "(ttagN == 0 && btagN == 1)";

//-------gen_variable------??
//

//    string var_gen = "";
//    if(var_name == "DeltaY") var_gen= "TMath::Abs(0.5*TMath::Log((GenParticles.m_energy[2] + GenParticles.m_pt[2]*TMath::SinH(GenParticles.m_eta[2]))/(GenParticles.m_energy[2] - GenParticles.m_pt[2]*TMath::SinH(GenParticles.m_eta[2])))) - TMath::Abs(0.5*TMath::Log((GenParticles.m_energy[3] + GenParticles.m_pt[3]*TMath::SinH(GenParticles.m_eta[3]))/(GenParticles.m_energy[3] - GenParticles.m_pt[3]*TMath::SinH(GenParticles.m_eta[3]))))";

//------Filling_bkgs---------??
    treereco_data->Project("Data",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s",selcuts.c_str()));
    treereco_ttbar->Project("TTbar",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_central*0.80",selcuts.c_str()));
    treereco_wjets->Project("WJets",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_central",selcuts.c_str()));
    treereco_ST->Project("ST",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_central",selcuts.c_str()));
    treereco_DY->Project("DY",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_central",selcuts.c_str()));
    treereco_QCD->Project("QCD",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_central",selcuts.c_str()));

// ------ filling_syst_1D_histograms----------??

    treereco_ttbar->Project("ttbar_pu_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu_up*weight_btagdisc_central*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_pu_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu_down*weight_btagdisc_central*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_cferr1_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_cferr1up*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_cferr1_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_cferr1down*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_cferr2_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_cferr2up*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_cferr2_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_cferr2down*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_hf_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_hfup*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_hf_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_hfdown*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_hfstats1_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_hfstats1up*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_hfstats1_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_hfstats1down*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_hfstats2_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_hfstats2up*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_hfstats2_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_hfstats2down*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_jes_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_jesup*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_jes_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_jesdown*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_lf_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfup*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_lf_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfdown*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_lfstats1_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfstats1up*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_lfstats1_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfstats1down*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_lfstats2_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfstats2up*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_lfstats2_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfstats2down*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_MuonID_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID_up*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfstats2down*0.80",selcuts.c_str())); 
    treereco_ttbar->Project("ttbar_MuonID_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID_down*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfstats2down*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_Trigger_up",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger_up*weight_pu*weight_btagdisc_lfstats2down*0.80",selcuts.c_str()));
    treereco_ttbar->Project("ttbar_Trigger_down",Form("%s < %f ? TMath::Max(%f,%s): (%s > %f ? TMath::Min(%f,%s) : %s)",var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger_down*weight_pu*weight_btagdisc_lfstats2down*0.80",selcuts.c_str()));


//-------Migration_Matrix_for_nominal_unfolding------??  
    treereco_ttbar->Project("Migration_Matrix",Form("%s < %f ? %f : (%s > %f ? %f : %s) : %s < %f ? %f : (%s > %f ? %f : %s)",var_gen.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_gen.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_gen.c_str(),var_name.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_name.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_central*0.80",selcuts.c_str()));
    treereco_ttbar->Project("Var_gen",Form("%s < %f ? %f : (%s > %f ? %f : %s)",var_gen.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_gen.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_gen.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_central*0.80",selcuts.c_str()));
    
//      treereco_ttbar->Project("Var_gen",Form("%s < 0 ? 0.01 : %s",var_gen.c_str(),var_gen.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_central*0.80",selcuts.c_str())); 

//< %f ? TMath::Max(%f,%s) : (%s > %f ? TMath::Min(%f,%s) : %s)",var_gen.c_str(),bins_gen[0]+0.01,bins_gen[0]+0.01,var_gen.c_str(),var_gen.c_str(),bins_gen[binnum_gen]-0.01,bins_gen[binnum_gen]-0.01,var_gen.c_str(),var_gen.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_central*0.80",selcuts.c_str()));





//------Migration_Matrices_for_syst_propagation-----?? 
//    treereco_ttbar->Project("Migration_Matrix_pu",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu_up*weight_btagdisc_central*0.80",selcuts.c_str()));
//    treereco_ttbar->Project("Migration_Matrix_cferr1",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu_up*weight_btagdisc_cferr1up*0.80",selcuts.c_str()));
//    treereco_ttbar->Project("Migration_Matrix_cferr2",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_cferr2up*0.80",selcuts.c_str()));
//    treereco_ttbar->Project("Migration_Matrix_hf",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_hfup*0.80",selcuts.c_str())); 
//   treereco_ttbar->Project("Migration_Matrix_hfstats1",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_hfstats1up*0.80",selcuts.c_str()));
//    treereco_ttbar->Project("Migration_Matrix_hfstats2",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_hfstats2up*0.80",selcuts.c_str()));
//    treereco_ttbar->Project("Migration_Matrix_jes",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_jesup*0.80",selcuts.c_str()));
//    treereco_ttbar->Project("Migration_Matrix_lf",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfup*0.80",selcuts.c_str()));
//    treereco_ttbar->Project("Migration_Matrix_lfstats2",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfstats1up*0.80",selcuts.c_str()));
//    treereco_ttbar->Project("Migration_Matrix_lfstats1",Form("%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s):%s < bin_gen[0] ? TMath::Max(bin_gen[0],%s): (%s > bin_gen[binnum_gen] ? TMath::Min(bin_gen[binnum_gen],%s) : %s)",var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_gen.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str(),var_name.c_str()),Form("%s*weight*weight_sfmu_HighPtID*weight_sfmu_Trigger*weight_pu*weight_btagdisc_lfstats2up*0.80",selcuts.c_str()));



//----------Making_input_root_file_for_unfolding-----------?

    TFile out("Input_undfolding_data_.root","recreate");
    Data->Write();
    TTbar->Write();
    WJets->Write(); 
    ST->Write(); 
    DY->Write();
    QCD->Write();
    Migration_Matrix->Write();    
    Var_gen->Write();

    ttbar_pu_down->Write();
    ttbar_pu_up->Write();
    ttbar_cferr1_up->Write();
    ttbar_cferr1_down->Write();
    ttbar_cferr2_up->Write();
    ttbar_cferr2_down->Write();
    ttbar_hf_up->Write();
    ttbar_hf_down->Write();
    ttbar_hfstats1_down->Write();
    ttbar_hfstats1_up->Write();
    ttbar_hfstats2_up->Write();
    ttbar_hfstats2_down->Write();
    ttbar_jes_up->Write();
    ttbar_jes_down->Write();
    ttbar_lf_up->Write();
    ttbar_lf_down->Write();
    ttbar_lfstats1_up->Write();
    ttbar_lfstats1_down->Write();
    ttbar_lfstats2_up->Write();
    ttbar_lfstats2_down->Write();
    ttbar_MuonID_up->Write();
    ttbar_MuonID_down->Write();
    ttbar_Trigger_up->Write();
    ttbar_Trigger_down->Write();


//    Migration_Matrix_pu->Write();
//    Migration_Matrix_cferr1->Write();
//    Migration_Matrix_cferr2->Write();
//    Migration_Matrix_hf->Write();
//    Migration_Matrix_hfstats1->Write();
//    Migration_Matrix_hfstats2->Write();
//    Migration_Matrix_jes->Write();
//    Migration_Matrix_lf->Write();
//    Migration_Matrix_lfstats1->Write();
//    Migration_Matrix_lfstats2->Write();



}


