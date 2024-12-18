#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1F.h"

class LHEMttbarAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
public:
  explicit LHEMttbarAnalyzer(const edm::ParameterSet&);
  ~LHEMttbarAnalyzer();

private:
  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;

  edm::EDGetTokenT<LHEEventProduct> lheEventToken_;
  TH1F* hist_mttbar_;
};

LHEMttbarAnalyzer::LHEMttbarAnalyzer(const edm::ParameterSet& iConfig)
{
  usesResource("TFileService");
  lheEventToken_ = consumes<LHEEventProduct>(edm::InputTag("externalLHEProducer"));
  edm::Service<TFileService> fs;
  hist_mttbar_ = fs->make<TH1F>("mttbar", "mttbar", 100, 0, 2000);
}

LHEMttbarAnalyzer::~LHEMttbarAnalyzer() {}

void LHEMttbarAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  edm::Handle<LHEEventProduct> lheEvent;
  iEvent.getByToken(lheEventToken_, lheEvent);

  if (!lheEvent.isValid()) {
    edm::LogWarning("LHEMttbarAnalyzer") << "No LHEEventProduct found";
    return;
  }

  const auto& hepeup = lheEvent->hepeup();
  const auto& particles = hepeup.PUP;

  TLorentzVector top, antitop;

  for (size_t i = 0; i < particles.size(); ++i) {
    int pdgId = hepeup.IDUP[i];
    int status = hepeup.ISTUP[i];

    if (status != 1) continue; // Keep only final-state particles

    double px = particles[i][0];
    double py = particles[i][1];
    double pz = particles[i][2];
    double energy = particles[i][3];

    TLorentzVector particle(px, py, pz, energy);

    if (pdgId == 6) {
      top = particle;
    } else if (pdgId == -6) {
      antitop = particle;
    }
  }

  if (top.Pt() > 0 && antitop.Pt() > 0) {
    double mttbar = (top + antitop).M();
    hist_mttbar_->Fill(mttbar);
  }
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(LHEMttbarAnalyzer);
