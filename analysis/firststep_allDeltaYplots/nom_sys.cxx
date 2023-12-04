// #include <TFileMerger.h>

// int merge() {

//     // Create a TFileMerger object
//     TFileMerger *merger = new TFileMerger();

//     // Add the files to be merged
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar1.root");
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar2.root");
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar3.root");
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar4.root");
   
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/DATA/nominal/uhh2.AnalysisModuleRunner.DATA.root");
    
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/WJets/nominal/uhh2.AnalysisModuleRunner.WJets.root");
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/DY/nominal/uhh2.AnalysisModuleRunner.DY.root");
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/Diboson/nominal/uhh2.AnalysisModuleRunner.Diboson.root");
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/ST/nominal/uhh2.AnalysisModuleRunner.ST.root");
//     merger->AddFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/QCD/nominal/uhh2.AnalysisModuleRunner.QCD.root");

//     // Specify the name of the output file
//     merger->OutputFile("DeltaY_UL18_muon_750_900_sys.root");

//     // Merge the files
//     merger->Merge();

//     return 0;

// }

////ANOTHER SCRIPT OPTION

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

void nom_sys()

{

    gStyle->SetOptStat(0);

    // A chain is a collection of files containing TTree objects. 
    // TChain(const char *name, const char *title="", Mode mode=kWithGlobalRegistration or kWithoutGlobalReg)
    // TTree tree(name, title)

    TChain *reco = new TChain("AnalysisTree","");

    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar1.root");
    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar2.root");
    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar3.root");
    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar4.root");

    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/DATA/nominal/uhh2.AnalysisModuleRunner.DATA.root");
    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/WJets/nominal/uhh2.AnalysisModuleRunner.WJets.root");
    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/DY/nominal/uhh2.AnalysisModuleRunner.DY.root");
    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/Diboson/nominal/uhh2.AnalysisModuleRunner.Diboson.root");
    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/ST/nominal/uhh2.AnalysisModuleRunner.ST.root");
    reco-> Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_latest/QCD/nominal/uhh2.AnalysisModuleRunner.QCD.root");


    TTree *treereco = (TTree*) reco;

    cout << "Number of Events:"<< treereco-> GetEntries()<<endl;

    
    // TH1D DeltaY Plots

    //DeltaY gen without mass cut
    TH1D *h_DeltaY_gen = new TH1D("DeltaY_gen","#Delta_Y_{gen}",10,-2.5,2.5);
    //DeltaY gen with mass cut
    TH1D *h_DeltaY_gen_mass = new TH1D("DeltaY_gen_mass","(#Delta_Y)_{gen}, M > 750",10,-2.5,2.5);
    //POSITIVE gen without mass
    TH1D *h_DeltaY_P_gen_nomass = new TH1D("DeltaY_P_gen_nomass","#Delta_Y_{gen}>0",1,0,2.5);
    //POSITIVE gen with mass
    TH1D *h_DeltaY_P_gen = new TH1D("DeltaY_P_gen","#Delta_Y_{gen}>0, M > 750",1,0,2.5);
    //NEGATIVE gen without mass
    TH1D *h_DeltaY_N_gen_nomass = new TH1D("DeltaY_N_gen_nomass","#Delta_Y_{gen} < 0",1,-2.5,0);
    //NEGATIVE gen with mass
    TH1D *h_DeltaY_N_gen = new TH1D("DeltaY_N_gen","(#Delta_Y_{gen} < 0, M > 750",1,-2.5,0);

    //DeltaY reco without mass cut
    TH1D *h_DeltaY_reco = new TH1D("DeltaY_reco","#Delta_Y_{reco}",2,-2.5,2.5);
    //DeltaY with mass cut
    TH1D *h_DeltaY_reco_mass = new TH1D("DeltaY_reco_mass","(#Delta_Y)_{reco}, M > 750",2,-2.5,2.5);
    //POSITIVE reco without mass
    TH1D *h_DeltaY_P_reco_nomass = new TH1D("DeltaY_P_reco_nomass","#Delta_Y_{reco}>0",1,0,2.5);
    //POSITIVE reco with mass
    TH1D *h_DeltaY_P_reco = new TH1D("DeltaY_P_reco","#Delta_Y_{reco}>0, M>750",1,0,2.5);
    //NEGATIVE reco without mass
    TH1D *h_DeltaY_N_reco_nomass = new TH1D("DeltaY_N_reco_nomass","#Delta_Y_{reco}<0",1,-2.5,0);
    //NEGATIVE reco with mass
    TH1D *h_DeltaY_N_reco = new TH1D("DeltaY_N_reco","#Delta_Y_{reco}<0, M>750",1,-2.5,0);


    // POSITIVE gen, POSITIVE reco, without mass cut
    TH1D *h_DeltaY_P_P_nomass = new TH1D("DeltaY_P_P_nomass","#Delta_Y_{gen} > 0, #Delta_Y_{reco} > 0 ",1,0,2.5);
    // POSITIVE gen, POSITIVE reco, with mass cut
    TH1D *h_DeltaY_P_P = new TH1D("DeltaY_P_P","#Delta_Y_{gen} > 0, #Delta_Y_{reco} > 0, M >750",1,0,2.5);
    // POSITIVE gen, NEGATIVE reco, without mass cut
    TH1D *h_DeltaY_P_N_nomass = new TH1D("DeltaY_P_N_nomass","#Delta_Y_{gen} > 0, #Delta_Y_{reco} < 0",1,-2.5,2.5);
    // POSITIVE gen, NEGATIVE reco, with mass cut
    TH1D *h_DeltaY_P_N = new TH1D("DeltaY_P_N","#Delta_Y_{gen} > 0, #Delta_Y_{reco} < 0, M >750",1,-2.5,2.5);
    // NEAGATIVE gen, POSITIVE reco, without mass cut
    TH1D *h_DeltaY_N_P_nomass = new TH1D("DeltaY_N_P_nomass","#Delta_Y_{gen} < 0, #Delta_Y_{reco} > 0",1,-2.5,2.5);
    // NEGATIVE gen, POSITIVE reco, with mass cut
    TH1D *h_DeltaY_N_P = new TH1D("DeltaY_N_P","#Delta_Y_{gen} < 0, #Delta_Y_{reco} > 0, M >750",1,-2.5,2.5);
    // NEGATIVE gen, NEGATIVE reco, without mass cut
    TH1D *h_DeltaY_N_N_nomass = new TH1D("DeltaY_N_N_nomass","#Delta_Y_{gen} < 0, #Delta_Y_{reco} < 0",1,-2.5,0);
    // NEGATIVE gen, NEGATIVE reco, with mass cut
    TH1D *h_DeltaY_N_N = new TH1D("DeltaY_N_N","#Delta_Y_{gen} < 0, #Delta_Y_{reco} < 0, M >750",1,-2.5,0);
    

    // TH1D Projection Plots

    TH1D *ProjY_1 = new TH1D("ProjY_1","Project along Y , #Delta_Y_{reco} < 0 ",2,-2.5,2.5);
    TH1D *ProjY_2 = new TH1D("ProjY_2","Project along Y , #Delta_Y_{reco} > 0 ",2,-2.5,2.5);

    TH1D *ProjX_1 = new TH1D("ProjX_1","Project along X , #Delta_Y_{gen} < 0 ",2,-2.5,2.5);
    TH1D *ProjX_2 = new TH1D("ProjX_2","Project along X ,#Delta_Y_{gen} > 0 ",2,-2.5,2.5);

    // TH1F Pileup 

    TH1D *h_weight_pu_down = new TH1D("weight_pu_down","weight_pu_down",1,-1,1);
    TH1D *h_weight_pu_up = new TH1D("weight_pu_up","weight_pu_up",1,-1,1);


    // TH2D Matrix 
    TH2D *Matrix = new TH2D("Matrix","", 2,-2.5,2.5,2,-2.5,2.5);

    float DeltaY_gen;
    float DeltaY_gen_mass;
    float DeltaY_P_gen;
    float DeltaY_P_gen_nomass;
    float DeltaY_N_gen;
    float DeltaY_N_gen_nomass;
    
    float DeltaY_reco;
    float DeltaY_reco_mass;
    float DeltaY_P_reco;
    float DeltaY_P_reco_nomass;
    float DeltaY_N_reco;
    float DeltaY_N_reco_nomass;

    float DeltaY_N_N;
    float DeltaY_N_P;
    float DeltaY_P_N;
    float DeltaY_P_P;
    float DeltaY_N_N_nomass;
    float DeltaY_N_P_nomass;
    float DeltaY_P_N_nomass;
    float DeltaY_P_P_nomass;

    float weight_pu_down;
    float weight_pu_up;
    
    
    treereco->SetBranchAddress("DeltaY_gen", &DeltaY_gen);
    treereco->SetBranchAddress("DeltaY_gen_mass", &DeltaY_gen_mass);
    treereco->SetBranchAddress("DeltaY_P_gen", &DeltaY_P_gen);
    treereco->SetBranchAddress("DeltaY_P_gen_nomass", &DeltaY_P_gen_nomass);
    treereco->SetBranchAddress("DeltaY_N_gen", &DeltaY_N_gen);
    treereco->SetBranchAddress("DeltaY_N_gen_nomass", &DeltaY_N_gen_nomass);

    treereco->SetBranchAddress("DeltaY_reco", &DeltaY_reco);
    treereco->SetBranchAddress("DeltaY_reco_mass", &DeltaY_reco_mass);
    treereco->SetBranchAddress("DeltaY_P_reco", &DeltaY_P_reco);
    treereco->SetBranchAddress("DeltaY_P_reco_nomass", &DeltaY_P_reco_nomass);
    treereco->SetBranchAddress("DeltaY_N_reco", &DeltaY_N_reco);
    treereco->SetBranchAddress("DeltaY_N_reco_nomass", &DeltaY_N_reco_nomass);

    treereco->SetBranchAddress("DeltaY_N_N", &DeltaY_N_N);
    treereco->SetBranchAddress("DeltaY_N_P", &DeltaY_N_P);
    treereco->SetBranchAddress("DeltaY_P_P", &DeltaY_P_P);
    treereco->SetBranchAddress("DeltaY_P_N", &DeltaY_P_N);
    treereco->SetBranchAddress("DeltaY_N_N_nomass", &DeltaY_N_N_nomass);
    treereco->SetBranchAddress("DeltaY_N_P_nomass", &DeltaY_N_P_nomass);
    treereco->SetBranchAddress("DeltaY_P_N_nomass", &DeltaY_P_N_nomass);
    treereco->SetBranchAddress("DeltaY_P_P_nomass", &DeltaY_P_P_nomass);

    treereco->SetBranchAddress("weight_pu_down", &weight_pu_down);
    treereco->SetBranchAddress("weight_pu_up", &weight_pu_up);

    for (Int_t i = 0; i < treereco->GetEntries(); i++){
    // for (Int_t i = 0; i < 10000; i++){

        treereco->GetEntry(i);
        if (i%1000000 == 0) std::cout << "--- ... Processing event: " << i <<std::endl;
       
        h_DeltaY_gen->Fill(DeltaY_gen);
        h_DeltaY_gen_mass->Fill(DeltaY_gen_mass);
        h_DeltaY_P_gen_nomass->Fill(DeltaY_P_gen_nomass);
        h_DeltaY_P_gen->Fill(DeltaY_P_gen);
        h_DeltaY_N_gen_nomass->Fill(DeltaY_N_gen_nomass);
        h_DeltaY_N_gen->Fill(DeltaY_N_gen);

        h_DeltaY_reco->Fill(DeltaY_reco);
        h_DeltaY_reco_mass->Fill(DeltaY_reco_mass);
        h_DeltaY_P_reco_nomass->Fill(DeltaY_P_reco_nomass);
        h_DeltaY_P_reco->Fill(DeltaY_P_reco);
        h_DeltaY_N_reco_nomass->Fill(DeltaY_N_reco_nomass);
        h_DeltaY_N_reco->Fill(DeltaY_N_reco);

        h_DeltaY_P_P->Fill(DeltaY_P_P);
        h_DeltaY_P_N->Fill(DeltaY_P_N);
        h_DeltaY_N_N->Fill(DeltaY_N_N);
        h_DeltaY_N_P->Fill(DeltaY_N_P);
        h_DeltaY_P_P_nomass->Fill(DeltaY_P_P_nomass);
        h_DeltaY_P_N_nomass->Fill(DeltaY_P_N_nomass);
        h_DeltaY_N_P_nomass->Fill(DeltaY_N_P_nomass);
        h_DeltaY_N_N_nomass->Fill(DeltaY_N_N_nomass);

        h_weight_pu_down->Fill(weight_pu_down);
        h_weight_pu_up->Fill(weight_pu_up);
        
    }

    double integral [2][2] = {{h_DeltaY_N_N->Integral(),h_DeltaY_P_N->Integral()},{h_DeltaY_N_P->Integral(),h_DeltaY_P_P->Integral()}};

     for(int i=0; i<2; i++){
        for(int j=0; j<2; j++){
              Matrix->SetBinContent(i+1,j+1,integral[i][j]);
       }
    }

    
  
    ProjY_1->GetXaxis()->SetTitle("#Delta_Y_{gen}");
    ProjY_2->GetXaxis()->SetTitle("#Delta_Y_{gen}");
    ProjX_1->GetXaxis()->SetTitle("#Delta_Y_{reco}");
    ProjX_2->GetXaxis()->SetTitle("#Delta_Y_{reco}");

    ProjY_1 = Matrix->ProjectionY("py1",1,1);
    ProjY_2 = Matrix->ProjectionY("py2",2,2);

    ProjX_1 = Matrix->ProjectionX("px1",1,1);
    ProjX_2 = Matrix->ProjectionX("px2", 2,2);


  // --------------- Output File ------------------

    TFile* myFile = new TFile("DeltaY_UL18_muon_750_900_ttbar_test.root", "RECREATE");
    
    h_DeltaY_gen->Write();
    h_DeltaY_gen_mass->Write();
    h_DeltaY_P_gen_nomass->Write();
    h_DeltaY_P_gen->Write();
    h_DeltaY_N_gen_nomass->Write();
    h_DeltaY_N_gen->Write();

    h_DeltaY_reco->Write();
    h_DeltaY_reco_mass->Write();
    h_DeltaY_P_reco_nomass->Write();
    h_DeltaY_P_reco->Write();
    h_DeltaY_N_reco_nomass->Write();
    h_DeltaY_N_reco->Write();  
    
    h_DeltaY_P_P->Write();
    h_DeltaY_P_N->Write();
    h_DeltaY_N_P->Write();
    h_DeltaY_N_N->Write();
    h_DeltaY_P_P_nomass->Write();
    h_DeltaY_P_N_nomass->Write();
    h_DeltaY_N_P_nomass->Write();
    h_DeltaY_N_N_nomass->Write();

    Matrix->Write();

    ProjY_1->Write();
    ProjY_2->Write();
    ProjX_1->Write();
    ProjX_2->Write();

    h_weight_pu_down->Write();
    h_weight_pu_up->Write();



}