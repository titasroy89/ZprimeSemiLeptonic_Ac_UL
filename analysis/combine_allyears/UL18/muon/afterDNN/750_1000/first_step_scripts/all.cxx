#include <iostream>
#include <vector>
#include <TString.h>
#include <TH1F.h>
#include <TH2D.h>
#include <TFile.h>
#include <TChain.h>
#include <TTree.h>

using namespace std;

TString analysis_step = "after_dnn";
TString input_base_dir = "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_combine_correctlatest/nominal"; // Update this path
vector<TString> v_years = {"UL18"};
vector<TString> v_channels = { "muon"};
// vector<TString> v_samples = {"DATA", "TTbar", "WJets", "ST", "DY", "Diboson", "QCD"};
vector<TString> v_samples = {"TTbar"};


void createNominalHistograms(TH1D*& ProjX_1, TH1D*& ProjX_2);
void prepare_combine_input();

void createNominalHistograms(TH1D*& ProjX_1, TH1D*& ProjX_2) {
    TChain *reco = new TChain("AnalysisTree","");
    reco->Add("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_combine_correctlatest/nominal/TTbar.root");
    TTree *treereco = (TTree*)reco;

    cout << "Number of Events:"<< treereco-> GetEntries()<<endl;


    // POSITIVE gen, POSITIVE reco, with mass cut
    TH1D *h_DeltaY_P_P_750_1000_muon = new TH1D("DeltaY_P_P_750_1000_muon","0<Mtt<250, #Delta_Y_{gen} > 0, #Delta_Y_{reco} > 0 ",1,0,2.5);
    // POSITIVE gen, NEGATIVE reco, with mass cut
    TH1D *h_DeltaY_P_N_750_1000_muon = new TH1D("DeltaY_P_N_750_1000_muon","0<Mtt<250, #Delta_Y_{gen} > 0, #Delta_Y_{reco} < 0",1,-2.5,0);
    // NEGATIVE gen, POSITIVE reco, with mass cut
    TH1D *h_DeltaY_N_P_750_1000_muon = new TH1D("h_DeltaY_N_P_750_1000_muon","0<Mtt<250, #Delta_Y_{gen} < 0, #Delta_Y_{reco} > 0",1,0,2.5);
    // NEAGATIVE gen, NEGATIVE reco, without mass cut
    TH1D *h_DeltaY_N_N_750_1000_muon = new TH1D("h_DeltaY_N_N_750_1000_muon","0<Mtt<250, #Delta_Y_{gen} < 0, #Delta_Y_{reco} < 0",1,-2.5,0);

    // TH1D Projection Plots

    TH1D *ProjY_1 = new TH1D("ProjY_1","Project along Y , #Delta_Y_{reco} < 0 ",2,-2.5,2.5);
    TH1D *ProjY_2 = new TH1D("ProjY_2","Project along Y , #Delta_Y_{reco} > 0 ",2,-2.5,2.5);

    TH1D *ProjX_1 = new TH1D("ProjX_1","Project along X , #Delta_Y_{gen} < 0 ",2,-2.5,2.5);
    TH1D *ProjX_2 = new TH1D("ProjX_2","Project along X ,#Delta_Y_{gen} > 0 ",2,-2.5,2.5);

    // TH2D Matrix 
    TH2D *Matrix = new TH2D("Matrix","", 2,-2.5,2.5,2,-2.5,2.5);

    float DeltaY_P_P_750_1000_muon;
    float DeltaY_P_N_750_1000_muon;
    float DeltaY_N_P_750_1000_muon;
    float DeltaY_N_N_750_1000_muon;

    treereco->SetBranchAddress("DeltaY_P_P_750_1000_muon",&DeltaY_P_P_750_1000_muon);
    treereco->SetBranchAddress("DeltaY_P_N_750_1000_muon",&DeltaY_P_N_750_1000_muon);
    treereco->SetBranchAddress("DeltaY_N_P_750_1000_muon",&DeltaY_N_P_750_1000_muon);
    treereco->SetBranchAddress("DeltaY_N_N_750_1000_muon",&DeltaY_N_N_750_1000_muon);

    for (Int_t i = 0; i < treereco->GetEntries(); i++){

        treereco->GetEntry(i);
        if (i%1000000 == 0) std::cout << "--- ... Processing event: " << i <<std::endl;
       
    

       h_DeltaY_P_P_750_1000_muon->Fill(DeltaY_P_P_750_1000_muon);
       h_DeltaY_P_N_750_1000_muon->Fill(DeltaY_P_N_750_1000_muon);
       h_DeltaY_N_P_750_1000_muon->Fill(DeltaY_N_P_750_1000_muon);
       h_DeltaY_N_N_750_1000_muon->Fill(DeltaY_N_N_750_1000_muon);
    }

    double integral [2][2] = {{h_DeltaY_N_N_750_1000_muon->Integral(),h_DeltaY_P_N_750_1000_muon->Integral()},{h_DeltaY_N_P_750_1000_muon->Integral(),h_DeltaY_P_P_750_1000_muon->Integral()}};

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
}


void prepare_combine_input() {
    cout << "starting..." << endl;

    TH1D *ProjX_1, *ProjX_2;
    createNominalHistograms(ProjX_1, ProjX_2);

    // Iterating over years and channels
    for(unsigned int a = 0; a < v_years.size(); ++a) {
        TString year = v_years.at(a);
        cout << "year: " << year << endl;

        for(unsigned int b = 0; b < v_channels.size(); ++b) {
            TString channel = v_channels.at(b);
            cout << "channel: " << channel << endl;

            TFile* output_file = new TFile("output_" + year + "_" + channel + "_" + sample + ".root", "RECREATE");

            for(unsigned int c = 0; c < v_samples.size(); ++c) {
                vector<TH1F*> v_hists;
                TString sample = v_samples.at(c);
                cout << sample << endl;

                // Use ProjX_1 and ProjX_2 for nominal histograms
                vector<TH1F*> v_nominal;
                v_nominal.push_back((TH1F*)ProjX_1->Clone());
                v_nominal.push_back((TH1F*)ProjX_2->Clone());

                while((dir_key = (TKey *) next_dir())){ // root subdir loop
                    dir = input_file->Get(dir_key->GetName());
                    TString dir_name = dir->GetName();
                    // cout << dir_name << endl;

                    bool is_nominal = false;
                    bool is_multiclass_nn = false;
                    bool is_sr = false;
                    bool is_cr1 = false;
                    bool is_cr2 = false;
                    bool is_up_variation = false;
                    bool is_down_variation = false;
                    bool is_murmuf_upup = false;
                    bool is_murmuf_upnone = false;
                    bool is_murmuf_noneup = false;
                    bool is_murmuf_nonedown = false;
                    bool is_murmuf_downnone = false;
                    bool is_murmuf_downdown = false;
                    bool is_pdf = false;

                    if(dir_name == "nominal") is_nominal = true;
                    else if(dir_name == "MulticlassNN") is_multiclass_nn = true;
                    else if(dir_name == "DNN_output0_General") is_sr = true;
                    else if(dir_name == "DNN_output1_General") is_cr1 = true;
                    else if(dir_name == "DNN_output2_General") is_cr2 = true;
                    else if(dir_name.EndsWith("_up")) is_up_variation = true;
                    else if(dir_name.EndsWith("_down")) is_down_variation = true;
                    else if(dir_name == "murmuf_upup") is_murmuf_upup = true;
                    else if(dir_name == "murmuf_upnone") is_murmuf_upnone = true;
                    else if(dir_name == "murmuf_noneup") is_murmuf_noneup = true;
                    else if(dir_name == "murmuf_nonedown") is_murmuf_nonedown = true;
                    else if(dir_name == "murmuf_downnone") is_murmuf_downnone = true;
                    else if(dir_name == "murmuf_downdown") is_murmuf_downdown = true;
                    else if(dir_name.BeginsWith("pdf")) is_pdf = true;
                    else if(dir_name == "uhh2_meta" || dir_name == "AnalysisTree") continue; // skip if in case hadded files have tree

                    input_file->cd(dir_name);

                    TH1F *hist;
                    TKey *hist_key;
                    TIter next_hist(gDirectory->GetListOfKeys());

                    if(is_nominal || is_multiclass_nn || is_sr || is_cr1 || is_cr2){
                        TString region_tag;
                        if(is_multiclass_nn) region_tag = "_outputnodes";
                        else if(is_sr) region_tag = "_SR";
                        else if(is_cr1) region_tag = "_CR1";
                        else if(is_cr2) region_tag = "_CR2";

                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        TString hist_name = hist->GetName();
                        hist->SetName(hist_name + "_" + sample + region_tag);
                        v_nominal.push_back(hist);
                        v_hists.push_back(hist);
                        }
                    }

                    if(is_up_variation){ // simple up variation
                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        TString hist_name = hist->GetName();
                        hist->SetName(hist_name + "_" + sample + "_" + dir_name.ReplaceAll("_up", "Up"));
                        v_hists.push_back(hist);
                        }
                    }

                    else if(is_down_variation){ // simple down variation
                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        TString hist_name = hist->GetName();
                        hist->SetName(hist_name + "_" + sample + "_" + dir_name.ReplaceAll("_down", "Down"));
                        v_hists.push_back(hist);
                        }
                    }
                    else if(is_murmuf_upup){
                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        v_murmuf_upup.push_back(hist);
                        }
                    }
                    else if(is_murmuf_upnone){
                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        v_murmuf_upnone.push_back(hist);
                        }
                    }
                    else if(is_murmuf_noneup){
                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        v_murmuf_noneup.push_back(hist);
                        }
                    }
                    else if(is_murmuf_nonedown){
                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        v_murmuf_nonedown.push_back(hist);
                        }
                    }
                    else if(is_murmuf_downnone){
                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        v_murmuf_downnone.push_back(hist);
                        }
                    }
                    else if(is_murmuf_downdown){
                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        v_murmuf_downdown.push_back(hist);
                        }
                    }
                    else if(is_pdf){
                        // cout << "pdf" << endl;
                        while((hist_key = (TKey *) next_hist())){ // hist loop
                        hist = (TH1F*) gDirectory->Get(hist_key->GetName());
                        v_pdf.push_back(hist);
                        }
                    }
                    else {
                        continue;
                    }
                }

                // mcscale
                if(sample == "Diboson"){ // Diboson has no mcscale variations -> take nominal hists
                    for(unsigned int i=0; i<v_nominal.size(); ++i){
                        TH1F *hist_mcscaleUp = (TH1F*) v_nominal.at(i)->Clone();
                        TH1F *hist_mcscaleDown = (TH1F*) v_nominal.at(i)->Clone();
                        TString hist_name = hist_mcscaleUp->GetName();
                        hist_mcscaleUp->SetName(hist_name + "_mcscaleUp");
                        hist_mcscaleDown->SetName(hist_name + "_mcscaleDown");
                        v_hists.push_back(hist_mcscaleUp);
                        v_hists.push_back(hist_mcscaleDown);
                    }
                }
                else{
                    // get hists for normalization from presel files
                    TFile *presel_file = TFile::Open(input_base_dir + "/Presel_" + year + "/" + file_prefix + sample + ".root");
                    TH1F *nominal = (TH1F*) presel_file->Get("Input_General/sum_event_weights");
                    TH1F *upup = (TH1F*) presel_file->Get("Input_General/sum_event_weights_mcscale_upup");
                    TH1F *upnone = (TH1F*) presel_file->Get("Input_General/sum_event_weights_mcscale_upnone");
                    TH1F *noneup = (TH1F*) presel_file->Get("Input_General/sum_event_weights_mcscale_noneup");
                    TH1F *nonedown = (TH1F*) presel_file->Get("Input_General/sum_event_weights_mcscale_nonedown");
                    TH1F *downnone = (TH1F*) presel_file->Get("Input_General/sum_event_weights_mcscale_downnone");
                    TH1F *downdown = (TH1F*) presel_file->Get("Input_General/sum_event_weights_mcscale_downdown");
                    // presel_file->Close();

                    double norm_scale_upup = upup->GetBinContent(1) / nominal->GetBinContent(1);
                    double norm_scale_upnone = upnone->GetBinContent(1) / nominal->GetBinContent(1);
                    double norm_scale_noneup = noneup->GetBinContent(1) / nominal->GetBinContent(1);
                    double norm_scale_nonedown = nonedown->GetBinContent(1) / nominal->GetBinContent(1);
                    double norm_scale_downnone = downnone->GetBinContent(1) / nominal->GetBinContent(1);
                    double norm_scale_downdown = downdown->GetBinContent(1) / nominal->GetBinContent(1);

                    for(unsigned int i=0; i<v_murmuf_upup.size(); ++i){ // hist loop
                        vector<TH1F*> v_murmuf_variations;
                        v_murmuf_upup.at(i)->Scale(1. / norm_scale_upup);
                        v_murmuf_upnone.at(i)->Scale(1. / norm_scale_upnone);
                        v_murmuf_noneup.at(i)->Scale(1. / norm_scale_noneup);
                        v_murmuf_nonedown.at(i)->Scale(1. / norm_scale_nonedown);
                        v_murmuf_downnone.at(i)->Scale(1. / norm_scale_downnone);
                        v_murmuf_downdown.at(i)->Scale(1. / norm_scale_downdown);

                        v_murmuf_variations.push_back(v_murmuf_upup.at(i));
                        v_murmuf_variations.push_back(v_murmuf_upnone.at(i));
                        v_murmuf_variations.push_back(v_murmuf_noneup.at(i));
                        v_murmuf_variations.push_back(v_murmuf_nonedown.at(i));
                        v_murmuf_variations.push_back(v_murmuf_downnone.at(i));
                        v_murmuf_variations.push_back(v_murmuf_downdown.at(i));

                        TH1F *hist_mcscaleUp = (TH1F*) v_murmuf_variations.at(0)->Clone();
                        TH1F *hist_mcscaleDown = (TH1F*) v_murmuf_variations.at(0)->Clone();
                        for(unsigned int j=0; j<hist_mcscaleUp->GetNbinsX()+2; ++j){ // bin loop
                        float max = 0.;
                        float min = 10000000000.;
                        for(unsigned int k=0; k<v_murmuf_variations.size(); ++k){ // variation loop
                            float bin_content = v_murmuf_variations.at(k)->GetBinContent(j);
                            if(bin_content > max) max = bin_content;
                            if(bin_content < min) min = bin_content;
                        }
                        hist_mcscaleUp->SetBinContent(j, max);
                        hist_mcscaleDown->SetBinContent(j, min);
                        }
                        TString hist_name = hist_mcscaleUp->GetName();
                        hist_mcscaleUp->SetName(hist_name + "_" + sample + "_mcscaleUp");
                        hist_mcscaleDown->SetName(hist_name + "_" + sample + "_mcscaleDown");
                        v_hists.push_back(hist_mcscaleUp);
                        v_hists.push_back(hist_mcscaleDown);
                    }
                }

                // pdf
                if(sample == "Diboson"){ // Diboson has no pdf variations -> take nominal hists
                    for(unsigned int i=0; i<v_nominal.size(); ++i){
                        TH1F *hist_pdfUp = (TH1F*) v_nominal.at(i)->Clone();
                        TH1F *hist_pdfDown = (TH1F*) v_nominal.at(i)->Clone();
                        TString hist_name = hist_pdfUp->GetName();
                        hist_pdfUp->SetName(hist_name + "_pdfUp");
                        hist_pdfDown->SetName(hist_name + "_pdfDown");
                        v_hists.push_back(hist_pdfUp);
                        v_hists.push_back(hist_pdfDown);
                    }
                }
                else{
                    TFile *presel_file = TFile::Open(input_base_dir + "/Presel_" + year + "/" + file_prefix + sample + ".root");
                    TH1F *nominal = (TH1F*) presel_file->Get("Input_General/sum_event_weights");
                    vector<double> v_pdf_norm;
                    for(unsigned int i=1; i<101; ++i){
                        TH1F *pdf = (TH1F*) presel_file->Get((TString) "Input_General/sum_event_weights_PDF_" + to_string(i));
                        double norm_scale_pdf = pdf->GetBinContent(1) / nominal->GetBinContent(1);
                        v_pdf_norm.push_back(norm_scale_pdf);
                    }
                    // presel_file->Close();
                    int n_hists = v_pdf.size()/100; // = 546
                    for(unsigned int i=0; i<n_hists; ++i){ // hist loop
                        TH1F *hist_pdfUp = (TH1F*) v_pdf.at(i)->Clone();
                        TH1F *hist_pdfDown = (TH1F*) v_pdf.at(i)->Clone();
                        for(unsigned int j=0; j<hist_pdfUp->GetNbinsX()+2; ++j){ // bin loop
                            float nominal_bin_content = v_nominal.at(i)->GetBinContent(j);
                            float sum_bins = 0.;
                            for(unsigned int k=0; k<100; ++k){ // variation loop
                                TH1F *hist_pdf = v_pdf.at(k * n_hists + i);
                                if(j==0) hist_pdf->Scale(1. / v_pdf_norm.at(k)); // scale only once and not again for each bin!
                                float bin_content = hist_pdf->GetBinContent(j);
                                sum_bins += pow(bin_content - nominal_bin_content, 2);
                            }

                            float rms = sqrt(sum_bins / 100);
                            hist_pdfUp->SetBinContent(j, nominal_bin_content + rms);
                            hist_pdfDown->SetBinContent(j, nominal_bin_content - rms);
                        }
                        TString hist_name = hist_pdfUp->GetName();
                        hist_pdfUp->SetName(hist_name + "_" + sample + "_pdfUp");
                        hist_pdfDown->SetName(hist_name + "_" + sample + "_pdfDown");
                        v_hists.push_back(hist_pdfUp);
                        v_hists.push_back(hist_pdfDown);
                    }
                }
                if(!is_data && analysis_step == "after_baseline_selection"){ // JEC + JER files exist for MC only
                    // JEC
                    TFile *input_file_jec_up = TFile::Open(input_base_dir + "/" + input_dir_prefix + year + "/JEC_up/" + channel + "/" + file_prefix + sample + ".root");
                    TObject *dir_jec_up;
                    TKey *dir_key_jec_up;
                    TIter next_dir_jec_up(input_file_jec_up->GetListOfKeys());
                    while((dir_key_jec_up = (TKey *) next_dir_jec_up())){ // root subdir loop
                        dir_jec_up = input_file_jec_up->Get(dir_key_jec_up->GetName());
                        TString dir_name_jec_up = dir_jec_up->GetName();
                        if(dir_name_jec_up == "nominal"){
                            input_file_jec_up->cd(dir_name_jec_up);
                            TH1F *hist_jec_up;
                            TKey *hist_key_jec_up;
                            TIter next_hist_jec_up(gDirectory->GetListOfKeys());
                            while((hist_key_jec_up = (TKey *) next_hist_jec_up())){ // hist loop
                                hist_jec_up = (TH1F*) gDirectory->Get(hist_key_jec_up->GetName());
                                TString hist_name_jec_up = hist_jec_up->GetName();
                                hist_jec_up->SetName(hist_name_jec_up + "_" + sample + "_jecUp");
                                v_hists.push_back(hist_jec_up);
                            }
                        }
                    }
                    TFile *input_file_jec_down = TFile::Open(input_base_dir + "/" + input_dir_prefix + year + "/JEC_down/" + channel + "/" + file_prefix + sample + ".root");
                    TObject *dir_jec_down;
                    TKey *dir_key_jec_down;
                    TIter next_dir_jec_down(input_file_jec_down->GetListOfKeys());
                    while((dir_key_jec_down = (TKey *) next_dir_jec_down())){ // root subdir loop
                        dir_jec_down = input_file_jec_down->Get(dir_key_jec_down->GetName());
                        TString dir_name_jec_down = dir_jec_down->GetName();
                        if(dir_name_jec_down == "nominal"){
                            input_file_jec_down->cd(dir_name_jec_down);
                            TH1F *hist_jec_down;
                            TKey *hist_key_jec_down;
                            TIter next_hist_jec_down(gDirectory->GetListOfKeys());
                            while((hist_key_jec_down = (TKey *) next_hist_jec_down())){ // hist loop
                                hist_jec_down = (TH1F*) gDirectory->Get(hist_key_jec_down->GetName());
                                TString hist_name_jec_down = hist_jec_down->GetName();
                                hist_jec_down->SetName(hist_name_jec_down + "_" + sample + "_jecDown");
                                v_hists.push_back(hist_jec_down);
                            }
                        }
                    }
                    // JER
                    TFile *input_file_jer_up = TFile::Open(input_base_dir + "/" + input_dir_prefix + year + "/JER_up/" + channel + "/" + file_prefix + sample + ".root");
                    TObject *dir_jer_up;
                    TKey *dir_key_jer_up;
                    TIter next_dir_jer_up(input_file_jer_up->GetListOfKeys());
                    while((dir_key_jer_up = (TKey *) next_dir_jer_up())){ // root subdir loop
                        dir_jer_up = input_file_jer_up->Get(dir_key_jer_up->GetName());
                        TString dir_name_jer_up = dir_jer_up->GetName();
                            if(dir_name_jer_up == "nominal"){
                            input_file_jer_up->cd(dir_name_jer_up);
                            TH1F *hist_jer_up;
                            TKey *hist_key_jer_up;
                            TIter next_hist_jer_up(gDirectory->GetListOfKeys());
                            while((hist_key_jer_up = (TKey *) next_hist_jer_up())){ // hist loop
                                hist_jer_up = (TH1F*) gDirectory->Get(hist_key_jer_up->GetName());
                                TString hist_name_jer_up = hist_jer_up->GetName();
                                hist_jer_up->SetName(hist_name_jer_up + "_" + sample + "_jerUp");
                                v_hists.push_back(hist_jer_up);
                            }
                        }
                    }
                    TFile *input_file_jer_down = TFile::Open(input_base_dir + "/" + input_dir_prefix + year + "/JER_down/" + channel + "/" + file_prefix + sample + ".root");
                    TObject *dir_jer_down;
                    TKey *dir_key_jer_down;
                    TIter next_dir_jer_down(input_file_jer_down->GetListOfKeys());
                    while((dir_key_jer_down = (TKey *) next_dir_jer_down())){ // root subdir loop
                        dir_jer_down = input_file_jer_down->Get(dir_key_jer_down->GetName());
                        TString dir_name_jer_down = dir_jer_down->GetName();
                        if(dir_name_jer_down == "nominal"){
                            input_file_jer_down->cd(dir_name_jer_down);
                            TH1F *hist_jer_down;
                            TKey *hist_key_jer_down;
                            TIter next_hist_jer_down(gDirectory->GetListOfKeys());
                            while((hist_key_jer_down = (TKey *) next_hist_jer_down())){ // hist loop
                                hist_jer_down = (TH1F*) gDirectory->Get(hist_key_jer_down->GetName());
                                TString hist_name_jer_down = hist_jer_down->GetName();
                                hist_jer_down->SetName(hist_name_jer_down + "_" + sample + "_jerDown");
                                v_hists.push_back(hist_jer_down);
                            }
                        }
                    }
                }
                output_file->cd();
                for(unsigned int i=0; i<v_hists.size(); ++i) v_hists.at(i)->Write();
            } // end sample loop
            output_file->Close("R");
        } // end channel loop
    } // end year loop
    cout << "done!" << endl;
    cout << "if root does not manage to end this script properly (might happen after writing lots of histograms) simply end it manually via: control + Z" << endl;
    return;
}

               
    

    


int main() {
    try {
        prepare_combine_input();
    } catch (const std::exception& e) {
        cerr << "Error: " << e.what() << endl;
        return 1;
    }
    return 0;
}