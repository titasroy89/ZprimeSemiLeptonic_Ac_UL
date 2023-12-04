#include <TFileMerger.h>
#include <vector>
#include <string>

void mergeLargeFiles(const std::vector<std::string>& inputFileNames, const std::string& outputFileName) {
    TFileMerger merger(false); // Set 'fastMethod' to false for better memory management

    // Add input files
    for (const auto& fileName : inputFileNames) {
        merger.AddFile(fileName.c_str());
    }

    // Merge the input files into a single output file
    merger.OutputFile(outputFileName.c_str(), "RECREATE");
    if (!merger.Merge()) {
        std::cerr << "Error merging files." << std::endl;
    }
}

void merge() {
    std::vector<std::string> inputFileNames = {
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar1.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar2.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar3.root",
        "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_combine/UL18/muon/workdir_Zprime_Analysis_UL18_muon_combine_ttbar/nominal/uhh2.AnalysisModuleRunner.ttbar4.root"
        
    };

    std::string outputFileName = "uhh2.AnalysisModuleRunner.TTbar.root";

    mergeLargeFiles(inputFileNames, outputFileName);
}
