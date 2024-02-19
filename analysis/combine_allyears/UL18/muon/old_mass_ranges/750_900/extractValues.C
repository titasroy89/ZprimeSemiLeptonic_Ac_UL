#include <TFile.h>
#include <RooFitResult.h>
#include <RooRealVar.h>
#include <iostream>

void extractValues(TString filename) {
    TFile* file = TFile::Open(filename);
    if (!file || file->IsZombie()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return;
    }

    // Get the fit result
    RooFitResult* fitResult = (RooFitResult*)file->Get("fit_s");
    if (!fitResult) {
        std::cerr << "Error retrieving fit result from file: " << filename << std::endl;
        return;
    }


    RooRealVar* Ac = (RooRealVar*)fitResult->floatParsFinal().find("Ac");
    RooRealVar* r_neg = (RooRealVar*)fitResult->floatParsFinal().find("r_neg");

    double Ac_value = Ac->getValV();
    double Ac_error = Ac->getError();
    
    double r_neg_value = r_neg->getValV();
    double r_neg_error = r_neg->getError();

    std::cout << "For file: " << filename << std::endl;
    std::cout << "Ac: " << Ac_value << " +/- " << Ac_error << std::endl;
    std::cout << "r_neg: " << r_neg_value << " +/- " << r_neg_error << std::endl;
    std::cout << "-------------------------------------------" << std::endl;

    

    // Clean up
    delete file;

    // // Extract the best-fit values and uncertainties
    // double Ac_value = fitResult->floatParsFinal().find("Ac")->getValV();
    // double Ac_error = fitResult->floatParsFinal().find("Ac")->getError();
    // double r_neg_value = fitResult->floatParsFinal().find("r_neg")->getValV();
    // double r_neg_error = fitResult->floatParsFinal().find("r_neg")->getError();

    // std::cout << "For file: " << filename << std::endl;
    // std::cout << "Ac: " << Ac_value << " +/- " << Ac_error << std::endl;
    // std::cout << "r_neg: " << r_neg_value << " +/- " << r_neg_error << std::endl;
    // std::cout << "-------------------------------------------" << std::endl;

    // file->Close();
}


