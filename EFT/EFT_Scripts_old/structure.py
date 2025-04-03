#!/usr/bin/env python2

import ROOT
import sys

# Open the ROOT file
file = ROOT.TFile.Open("Ntuple_1211.root")  # Replace with your ROOT file path
if not file or file.IsZombie():
    print("Error: Could not open the ROOT file.")
    sys.exit()

# Access the TTree
tree = file.Get("AnalysisTree")  # Replace with the correct TTree name if different
if not tree:
    print("Error: TTree 'AnalysisTree' not found.")
    sys.exit()

# Limit the number of events for testing
max_events = 10  # Adjust as needed
nentries = min(tree.GetEntries(), max_events)
print("\nProcessing {} events...".format(nentries))

# Initialize histograms
hist_gen_pt = ROOT.TH1F("hist_gen_pt", "GenParticle p_{T};p_{T} [GeV];Entries", 100, 0, 500)
hist_gen_eta = ROOT.TH1F("hist_gen_eta", "GenParticle #eta;#eta;Entries", 100, -5, 5)
hist_gen_phi = ROOT.TH1F("hist_gen_phi", "GenParticle #phi;#phi;Entries", 64, -3.2, 3.2)
hist_gen_pdgId = ROOT.TH1F("hist_gen_pdgId", "GenParticle PDG ID;PDG ID;Entries", 200, -100, 100)
hist_muon_pt = ROOT.TH1F("hist_muon_pt", "Muon GenParticle p_{T};p_{T} [GeV];Entries", 100, 0, 500)

# Event loop
for ientry in range(nentries):
    if ientry % 1000 == 0:
        print("Processed {} events".format(ientry))
        sys.stdout.flush()

    tree.GetEntry(ientry)

    # Access the GenParticles collection
    genparticles = getattr(tree, "GenParticles")  # Adjust if the branch name is different
    n_particles = genparticles.size()

    # Loop over genparticles in the event
    for idx in range(n_particles):
        particle = genparticles[idx]

        # For the first particle in the first event, print available attributes and methods
        if ientry == 0 and idx == 0:
            print("Type of particle:", type(particle))
            print("Available attributes and methods of GenParticle:")
            for attr in dir(particle):
                print(attr)

        # Access properties using the correct names (case-sensitive)
        pdgId_attr = getattr(particle, 'pdgId', None)
        if pdgId_attr is not None:
            pdgId = pdgId_attr() if callable(pdgId_attr) else pdgId_attr
        else:
            print("pdgId not found for particle at index", idx)
            continue

        pt_attr = getattr(particle, 'pt', None)
        if pt_attr is not None:
            pt = pt_attr() if callable(pt_attr) else pt_attr
        else:
            print("pt not found for particle at index", idx)
            continue

        eta_attr = getattr(particle, 'eta', None)
        if eta_attr is not None:
            eta = eta_attr() if callable(eta_attr) else eta_attr
        else:
            print("eta not found for particle at index", idx)
            continue

        phi_attr = getattr(particle, 'phi', None)
        if phi_attr is not None:
            phi = phi_attr() if callable(phi_attr) else phi_attr
        else:
            print("phi not found for particle at index", idx)
            continue

        # Ensure the values are of type float
        try:
            pdgId_value = float(pdgId)
            pt_value = float(pt)
            eta_value = float(eta)
            phi_value = float(phi)
        except (TypeError, ValueError) as e:
            print("Error converting particle properties to float:", e)
            continue

        # Fill histograms
        hist_gen_pdgId.Fill(pdgId_value)
        hist_gen_pt.Fill(pt_value)
        hist_gen_eta.Fill(eta_value)
        hist_gen_phi.Fill(phi_value)

        # Fill muon pT histogram
        if abs(pdgId_value) == 13:
            hist_muon_pt.Fill(pt_value)

# Create a canvas
canvas = ROOT.TCanvas("canvas", "GenParticle Histograms", 800, 600)

# Draw and save PDG ID histogram
hist_gen_pdgId.Draw()
canvas.SaveAs("GenParticles_pdgId.png")
canvas.Clear()

# Draw and save pT histogram
hist_gen_pt.Draw()
canvas.SaveAs("GenParticles_pt.png")
canvas.Clear()

# Draw and save eta histogram
hist_gen_eta.Draw()
canvas.SaveAs("GenParticles_eta.png")
canvas.Clear()

# Draw and save phi histogram
hist_gen_phi.Draw()
canvas.SaveAs("GenParticles_phi.png")
canvas.Clear()

# Draw and save muon pT histogram
hist_muon_pt.Draw()
canvas.SaveAs("GenParticles_muon_pt.png")
canvas.Clear()
