#!/usr/bin/env python2

import ROOT
import sys
import argparse
import multiprocessing
import os

# Set debug to False to suppress debug prints
debug = False

def reconstruct_particle(particle1, particle2):
    #Reconstructs a particle by adding the four-momenta of two particles.
    p4_1 = ROOT.TLorentzVector()
    p4_1.SetPtEtaPhiE(particle1.pt(), particle1.eta(), particle1.phi(), particle1.energy())

    p4_2 = ROOT.TLorentzVector()
    p4_2.SetPtEtaPhiE(particle2.pt(), particle2.eta(), particle2.phi(), particle2.energy())

    return p4_1 + p4_2

def is_last_copy(particle):
    return particle.status() == 22  # https://pythia.org//latest-manual/Welcome.html. 22 might not be the last copy. This is the only status tops have in the events. 
# 22: intermediate (heaviest) resonance decaying in the hard process

def process_file(args):
    input_file = args['input_file']

    # Histograms for last copy and reconstructed tops
    hist_mttbar_lastcopy = args['hist_mttbar_template'].Clone("hist_mttbar_lastcopy")
    hist_mttbar_lastcopy.Reset()

    hist_mttbar_reconstructed = args['hist_mttbar_template'].Clone("hist_mttbar_reconstructed")
    hist_mttbar_reconstructed.Reset()

    print("\nProcessing file:", input_file)
    file = ROOT.TFile.Open(input_file)
    if not file or file.IsZombie():
        print("Error: Could not open the ROOT file:", input_file)
        return (hist_mttbar_lastcopy, hist_mttbar_reconstructed, 0)  # Return empty histograms and zero events

    # TTree
    tree = file.Get("AnalysisTree")
    if not tree:
        print("Error: TTree 'AnalysisTree' not found in file:", input_file)
        file.Close()
        return (hist_mttbar_lastcopy, hist_mttbar_reconstructed, 0)  # Return empty histograms and zero events

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

        # GenParticles collection
        genparticles = getattr(tree, "GenParticles")
        n_particles = genparticles.size()

        leptons = []
        jets = []
        b_quarks = {}
        w_bosons = {}

        met_px = 0.0
        met_py = 0.0

        top_quark = None
        antitop_quark = None

        # Loop over genparticles in the event
        for idx in range(n_particles):
            particle = genparticles[idx]
            pdgId = particle.pdgId()
            status = particle.status()
            pt = particle.pt()
            eta = particle.eta()
            phi = particle.phi()
            energy = particle.energy()
            mother1_idx = particle.mother1()  # first mother
            mother2_idx = particle.mother2()  # second mother


            # Check if particle is last copy of top and antitop
            if pdgId == 6 and is_last_copy(particle):
                top_quark = particle
            elif pdgId == -6 and is_last_copy(particle):
                antitop_quark = particle

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

        event_processed = False

        # Calculating mttbar using last copy of top quarks
        if top_quark and antitop_quark:
            top_p4 = ROOT.TLorentzVector()
            top_p4.SetPtEtaPhiE(top_quark.pt(), top_quark.eta(), top_quark.phi(), top_quark.energy())

            antitop_p4 = ROOT.TLorentzVector()
            antitop_p4.SetPtEtaPhiE(antitop_quark.pt(), antitop_quark.eta(), antitop_quark.phi(), antitop_quark.energy())

            ttbar_p4 = top_p4 + antitop_p4
            mttbar = ttbar_p4.M()

            hist_mttbar_lastcopy.Fill(mttbar, weight)
            event_processed = True  # Mark event as processed

        # Reconstruct tops from decay products
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

            hist_mttbar_reconstructed.Fill(mttbar, weight)
            event_processed = True
        else:
            if debug:
                print("Event {}: Could not reconstruct both top and antitop quarks".format(ientry))

        if event_processed:
            events_processed_in_file += 1
    file.Close()
    print("Total events processed in this file:", events_processed_in_file)
    return (hist_mttbar_lastcopy, hist_mttbar_reconstructed, events_processed_in_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process multiple ROOT files to produce m_ttbar histogram with reference weight.')
    parser.add_argument('input_files', nargs='+', help='List of input ROOT files')
    parser.add_argument('--output_file', default='mttbar_multiprocess_0700_2.root', help='Output ROOT file name')
    parser.add_argument('--n_cores', type=int, default=None, help='Number of CPU cores to use')

    args = parser.parse_args()
    input_files = args.input_files
    output_file_name = args.output_file
    n_cores = args.n_cores

    # Create a template histogram
    hist_mttbar_template = ROOT.TH1F("hist_mttbar_template", "Invariant Mass of t#bar{t}; m_{t#bar{t}} [GeV]; Entries", 100, 200, 2000)

    total_events_processed = 0

    # Prepare arguments for each worker
    worker_args = [{'input_file': f, 'hist_mttbar_template': hist_mttbar_template} for f in input_files]

    # Use multiprocessing Pool
    pool = multiprocessing.Pool(processes=n_cores)

    # Map the function to the pool
    results = pool.map(process_file, worker_args)

    # Close the pool and wait for the work to finish
    pool.close()
    pool.join()

    # Combine the histograms and count total events
    hist_mttbar_lastcopy = hist_mttbar_template.Clone("hist_mttbar_lastcopy")
    hist_mttbar_lastcopy.Reset()

    hist_mttbar_reconstructed = hist_mttbar_template.Clone("hist_mttbar_reconstructed")
    hist_mttbar_reconstructed.Reset()

    for hist_lastcopy, hist_reconstructed, events_processed_in_file in results:
        hist_mttbar_lastcopy.Add(hist_lastcopy)
        hist_mttbar_reconstructed.Add(hist_reconstructed)
        total_events_processed += events_processed_in_file

    print("\nTotal events processed across all files:", total_events_processed)
    print("Total events where last copy method succeeded:", hist_mttbar_lastcopy.GetEntries())
    print("Total events where reconstructed method succeeded:", hist_mttbar_reconstructed.GetEntries())

    # Save the combined histograms
    output_file = ROOT.TFile(output_file_name, "RECREATE")
    hist_mttbar_lastcopy.Write()
    hist_mttbar_reconstructed.Write()
    output_file.Close()

    # Draw and save the last copy histogram
    canvas_lastcopy = ROOT.TCanvas("canvas_lastcopy", "m_ttbar Histogram (Last Copy)", 800, 600)
    hist_mttbar_lastcopy.Draw()
    canvas_lastcopy.SaveAs("mttbar_lastcopy_0700_2.png")

    # Draw and save the reconstructed histogram
    canvas_reconstructed = ROOT.TCanvas("canvas_reconstructed", "m_ttbar Histogram (Reconstructed)", 800, 600)
    hist_mttbar_reconstructed.Draw()
    canvas_reconstructed.SaveAs("mttbar_reconstructed_0700_2.png")

    print("\nProcessing complete. Histograms saved as 'mttbar_lastcopy.png', 'mttbar_reconstructed.png', and '{}'.".format(output_file_name))