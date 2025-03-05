For ZprimeAnalysisModule_EFT.cxx:

DeltaY_reco is calculated in the ttbar rest frame.

It works with reconstructed objects:
- Uses BestZprimeCandidate which is a reconstructed object
- Uses reconstructed leptons from the event

The calculation process:
- Identifies the hadronic b-jet with the highest b-tag score from reconstructed jets
- Creates 4-vectors for the reconstructed hadronic b-jet and lepton
- Uses reconstructed top quarks (leptonic and hadronic) to define the ttbar system
- Performs kinematic transformations (boosts and rotations) on these reconstructed objects
- Calculates DeltaY_reco from the reconstructed objects

No generator information is used:
- No matching to generator-level particles




Delta_phi and Sigma_phi are calculated in the ttbar CM-Frame.

It works with reconstructed objects:
- Uses BestZprimeCandidate which is a reconstructed object
- Works with reconstructed jets (AK4CHSjets_matched, TopTaggedJets)
- Uses reconstructed leptons from the event

The calculation process:
- Identifies the hadronic b-jet with the highest b-tag score from reconstructed jets
- Creates 4-vectors for the reconstructed hadronic b-jet and lepton
- Uses reconstructed top quarks (leptonic and hadronic) to define the ttbar system
- Performs kinematic transformations (boosts and rotations) on these reconstructed objects
- Calculates Delta_phi and Sigma_phi from the reconstructed objects

No generator information is used:
- No matching to generator-level particles





