import ROOT

# file = ROOT.TFile.Open("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/Preselection/workdir_EFT_preselection/uhh2.AnalysisModuleRunner.MC.EFT_sample_UL18_0.root")

file = ROOT.TFile.Open("/nfs/dust/cms/group/zprime-uhh/Analysis_UL18/muon/workdir_Analysis_UL18_muon/uhh2.AnalysisModuleRunner.MC.TTToSemiLeptonic_UL18_0.root")

tree = file.Get("AnalysisTree")

for entry in xrange(tree.GetEntries()):
    tree.GetEntry(entry)
    
    particles = tree.GenParticles
        
    for particle in particles:
        pdgId = particle.pdgId()
        mother1 = particle.mother1()
        mother2 = particle.mother2()
            
        if abs(pdgId) == 24:
            
            if (abs(mother1) == 6 or abs(mother2) == 6):
                print("W boson from top found in event:", entry)
                
        if abs(pdgId) == 5:
            
            if (abs(mother1) == 6 or abs(mother2) == 6):
                print("b quark from top found in event:", entry)

