#!/usr/bin/env python2

import ROOT
import sys
import argparse

# Set debug to False to suppress debug prints
debug = False

def reconstruct_particle(particle1, particle2):
    p4_1 = ROOT.TLorentzVector()
    p4_1.SetPtEtaPhiE(particle1.pt(), particle1.eta(), particle1.phi(), particle1.energy())

    p4_2 = ROOT.TLorentzVector()
    p4_2.SetPtEtaPhiE(particle2.pt(), particle2.eta(), particle2.phi(), particle2.energy())

    return p4_1 + p4_2

def process_file(input_file, hist_mttbar, total_events_processed):

    print("\nProcessing file:", input_file)
    file = ROOT.TFile.Open(input_file)
    if not file or file.IsZombie():
        print("Error: Could not open the ROOT file:", input_file)
        return 0 

    # TTree
    tree = file.Get("AnalysisTree")
    if not tree:
        print("Error: TTree 'AnalysisTree' not found in file:", input_file)
        file.Close()
        return 0 
    
    nentries_in_file = tree.GetEntries()
    print("Number of events in this file:", nentries_in_file)

    events_processed_in_file = 0

    # Loop over events
    for ientry in range(nentries_in_file):
        if (ientry + 1) % 10000 == 0:
            print("Processed {} events in this file".format(ientry + 1))
            sys.stdout.flush()

        tree.GetEntry(ientry)

        # m_systweights
        try:
            m_systweights = tree.m_systweights 
            if not m_systweights:
                raise AttributeError("m_systweights is None")
            if m_systweights.size() == 0:
                if debug:
                    print("Warning: m_systweights vector is empty in event {}".format(ientry))
                weight = 1.0 
            else:
                weight = m_systweights[0]  # Reference weight at index 0 using direct indexing
        except AttributeError as e:
            if debug:
                print("Warning: 'm_systweights' branch not found or inaccessible in event {}: {}".format(ientry, e))
            weight = 1.0  # Default weight if branch is missing

        # Print the weight
        # print("File: {}, Event: {}, Reference Weight: {}".format(input_file, ientry, weight))

        #GenParticles collection
        genparticles = getattr(tree, "GenParticles")
        n_particles = genparticles.size()

        leptons = []
        jets = []
        b_quarks = {}
        w_bosons = {}

        met_px = 0.0
        met_py = 0.0

        # Loop over genparticles in the event
        for idx in range(n_particles):
            particle = genparticles[idx]
            pdgId = particle.pdgId()
            status = particle.status()
            pt = particle.pt()
            eta = particle.eta()
            phi = particle.phi()
            energy = particle.energy()
            mother1_idx = particle.mother1()
            mother2_idx = particle.mother2()

            # b quarks
            if abs(pdgId) == 5:
                b_quarks[idx] = {
                    'particle': particle,
                    'mother_indices': [mother1_idx, mother2_idx]
                }
            # W bosons
            elif abs(pdgId) == 24:
                w_bosons[idx] = {
                    'particle': particle,
                    'mother_indices': [mother1_idx, mother2_idx]
                }
            # Leptons (electron and muon)
            elif abs(pdgId) in [11, 13]:
                if pt > 30 and abs(eta) < 2.5:
                    leptons.append(particle)
            # Jets (light quarks and gluon)
            elif abs(pdgId) <= 5 or pdgId == 21:
                if pt > 30 and abs(eta) < 2.5:
                    jets.append(particle)

            # MET
            elif abs(pdgId) in [12, 14, 16]:
                met_px += pt * ROOT.TMath.Cos(phi)
                met_py += pt * ROOT.TMath.Sin(phi)

        met_pt = ROOT.TMath.Sqrt(met_px**2 + met_py**2)

        # one lepton
        if len(leptons) < 1:
            continue  # Skip event if no lepton

        # # Require at least two jets
        # if len(jets) < 2:
        #     continue  # Skip event if not enough jets

        # # MET cut
        # if met_pt < 20:
        #     continue  # Skip event if MET is insufficient

        reconstructed_tops = []
        reconstructed_antitops = []

        # Match b quarks and W bosons based on common mother index
        for b_idx, b_info in b_quarks.items():
            b_particle = b_info['particle']
            b_mothers = b_info['mother_indices']

            for w_idx, w_info in w_bosons.items():
                w_particle = w_info['particle']
                w_mothers = w_info['mother_indices']

                common_mothers = set(b_mothers).intersection(w_mothers)

                if debug:
                    print("b_mothers:", b_mothers)
                    print("w_mothers:", w_mothers)

                for mother_idx in common_mothers:
                    if mother_idx < 0 or mother_idx >= n_particles:
                        continue  # Skip invalid mother indices

                    mother_particle = genparticles[mother_idx]
                    mother_pdgId = mother_particle.pdgId()

                    # Check if the mother is a top or antitop quark
                    if mother_pdgId == 6:
                        top_p4 = reconstruct_particle(b_particle, w_particle)
                        reconstructed_tops.append(top_p4)
                    elif mother_pdgId == -6:
                        antitop_p4 = reconstruct_particle(b_particle, w_particle)
                        reconstructed_antitops.append(antitop_p4)

        # Ensure we have at least one top and one antitop
        if reconstructed_tops and reconstructed_antitops:
            top_p4 = reconstructed_tops[0]
            antitop_p4 = reconstructed_antitops[0]

            ttbar_p4 = top_p4 + antitop_p4
            mttbar = ttbar_p4.M()

            hist_mttbar.Fill(mttbar, weight)

            events_processed_in_file += 1
        else:
            if debug:
                print("Event {}: Could not reconstruct both top and antitop quarks".format(ientry))

    file.Close()
    print("Total events processed in this file:", events_processed_in_file)
    return events_processed_in_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process multiple ROOT files to produce m_ttbar histogram with reference weight.')
    parser.add_argument('input_files', nargs='+', help='List of input ROOT files')
    parser.add_argument('--output_file', default='histograms.root', help='Output ROOT file name')

    args = parser.parse_args()
    input_files = args.input_files
    output_file_name = args.output_file

    hist_mttbar = ROOT.TH1F("hist_mttbar", "Invariant Mass of t#bar{t}; m_{t#bar{t}} [GeV]; Entries", 100, 200, 2000)

    total_events_processed = 0

    for input_file in input_files:
        events_processed_in_file = process_file(
            input_file,
            hist_mttbar,
            total_events_processed
        )
        total_events_processed += events_processed_in_file
        print("Total events processed so far:", total_events_processed)

    print("\nTotal events processed across all files:", total_events_processed)

    output_file = ROOT.TFile(output_file_name, "RECREATE")
    hist_mttbar.Write()
    output_file.Close()

    canvas = ROOT.TCanvas("canvas", "m_ttbar Histogram", 800, 600)
    hist_mttbar.Draw()
    canvas.SaveAs("mttbar.png")

    print("\nProcessing complete. Histogram saved as 'mttbar.png' and '{}'.".format(output_file_name))
