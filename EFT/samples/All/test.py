#!/usr/bin/env python2

import ROOT
import sys
import argparse
import multiprocessing
import os

# Set debug to False to suppress debug prints
debug = False

def deltaR(eta1, phi1, eta2, phi2):
    # Calculate delta R between two particles
    deta = eta1 - eta2
    dphi = phi1 - phi2
    # Adjust dphi to be within -pi to pi
    while dphi > ROOT.TMath.Pi():
        dphi -= 2 * ROOT.TMath.Pi()
    while dphi <= -ROOT.TMath.Pi():
        dphi += 2 * ROOT.TMath.Pi()
    return ROOT.TMath.Sqrt(deta * deta + dphi * dphi)

def process_file(args):
    input_file = args['input_file']

    # Histograms for last copy and reconstructed tops
    hist_njets = ROOT.TH1F("hist_njets", "Number of Jets from b quark and W decay; N_{jets}; Entries", 10, 0, 10)
    hist_njets.Reset()
    hist_mttbar = ROOT.TH1F("hist_mttbar", "Invariant Mass of t#bar{t}; m_{t#bar{t}} [GeV]; Entries", 100, 200, 2000)
    hist_mttbar.Reset()

    print("\nProcessing file:", input_file)
    file = ROOT.TFile.Open(input_file)
    if not file or file.IsZombie():
        print("Error: Could not open the ROOT file:", input_file)
        return (hist_njets, hist_mttbar, 0)  # Return empty histograms and zero events

    # TTree
    tree = file.Get("AnalysisTree")
    if not tree:
        print("Error: TTree 'AnalysisTree' not found in file:", input_file)
        file.Close()
        return (hist_njets, hist_mttbar, 0)  # Return empty histograms and zero events

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

        b_quarks = []
        w_bosons = []
        w_decay_quarks = []
        leptons = []
        neutrinos = []
        top_quarks = []

        # Variables to hold reconstructed tops
        hadronic_top = None
        leptonic_top = None

        # Loop over genparticles in the event
        for idx in range(n_particles):
            particle = genparticles[idx]
            pdgId = particle.pdgId()
            status = particle.status()

            # Check if particle is last copy of top and antitop
            if abs(pdgId) == 6:
                top_quarks.append({'idx': idx, 'particle': particle, 'pdgId': pdgId})

        # for each top quark, find its decay products
        for top in top_quarks:
            top_particle = top['particle']
            top_idx = top['idx']
            top_pdgId = top['pdgId']

            # Initialize variables to store b quark and W boson
            b_quark = None
            w_boson = None

            # Loop over genparticles to find daughters of the top quark
            for idx in range(n_particles):
                particle = genparticles[idx]
                pdgId = particle.pdgId()
                mother1_idx = particle.mother1()
                mother2_idx = particle.mother2()

                # Check if the particle is a daughter of the top quark
                if mother1_idx == top_idx or mother2_idx == top_idx:
                    if abs(pdgId) == 5:
                        b_quark = {'idx': idx, 'particle': particle, 'pdgId': pdgId}
                    elif abs(pdgId) == 24:
                        w_boson = {'idx': idx, 'particle': particle, 'pdgId': pdgId}

            # Proceed only if both b quark and W boson are found
            if b_quark and w_boson:
                b_quarks.append(b_quark)
                w_bosons.append(w_boson)

                # Find the decay products of the W boson
                w_boson_idx = w_boson['idx']
                w_decay_products = []

                for idx in range(n_particles):
                    particle = genparticles[idx]
                    pdgId = particle.pdgId()
                    mother1_idx = particle.mother1()
                    mother2_idx = particle.mother2()

                    # Check if the particle is a daughter of the W boson
                    if mother1_idx == w_boson_idx or mother2_idx == w_boson_idx:
                        w_decay_products.append({'idx': idx, 'particle': particle, 'pdgId': pdgId})

                # Identify if the W boson decays hadronically or leptonically
                hadronic_decay = False
                leptonic_decay = False

                w_decay_quark_candidates = []

                for decay_product in w_decay_products:
                    pdgId = abs(decay_product['pdgId'])
                    if pdgId in [1, 2, 3, 4, 5]:
                        hadronic_decay = True
                        w_decay_quark_candidates.append(decay_product)
                    elif pdgId in [11, 13, 15]:  # e, mu, tau
                        leptonic_decay = True

                # To focus on hadronic decays to get quarks (for number jet plot):
                if hadronic_decay and len(w_decay_quark_candidates) >= 2:
                    # Collect the first two quarks (assuming they are from W decay)
                    w_decay_quarks.extend(w_decay_quark_candidates[:2])

                # Handle leptonic decays for mttbar reconstruction
                if leptonic_decay:
                    for decay_product in w_decay_products:
                        pdgId = decay_product['pdgId']
                        abs_pdgId = abs(pdgId)
                        if abs_pdgId in [11, 13, 15]:  # e, mu, tau
                            leptons.append(decay_product)
                        elif abs_pdgId in [12, 14, 16]:  # neutrinos
                            neutrinos.append(decay_product)

        # Collect all partons (b quarks and W decay quarks)
        partons = b_quarks + w_decay_quarks

       # Proceed only if there are partons to match
        if not partons:
            continue

        try:
            genjets = getattr(tree, "slimmedGenJets")
            n_genjets = genjets.size()
        except AttributeError:
            print("Error: 'slimmedGenJets' collection not found in the ROOT file.")
            continue  

        jets = []
        for j in range(n_genjets):
            genjet = genjets[j]
            jet_p4 = ROOT.TLorentzVector()
            jet_p4.SetPtEtaPhiE(genjet.pt(), genjet.eta(), genjet.phi(), genjet.energy())
            jets.append({'idx': j, 'p4': jet_p4})

        # delta R matching between partons and jets
        matched_jets_indices = set()
        matched_partons_indices = set()
        matches = []

        for jet in jets:
            jet_p4 = jet['p4']
            jet_idx = jet['idx']
            closest_dR = float('inf')
            closest_parton = None
            closest_parton_idx = -1

            for idx, parton in enumerate(partons):
                if idx in matched_partons_indices:
                    continue
                parton_particle = parton['particle']
                parton_p4 = ROOT.TLorentzVector()
                parton_p4.SetPtEtaPhiE(parton_particle.pt(), parton_particle.eta(), parton_particle.phi(), parton_particle.energy())

                dR = jet_p4.DeltaR(parton_p4)
                if dR < closest_dR:
                    closest_dR = dR
                    closest_parton = parton
                    closest_parton_idx = idx

            if closest_dR < 0.4:
                matched_jets_indices.add(jet_idx)
                matched_partons_indices.add(closest_parton_idx)
                matches.append({'jet': jet, 'parton': closest_parton})

        # combined_jets from matched jets
        combined_jets = [match['jet']['p4'] for match in matches]

        # the number of combined_jets
        hist_njets.Fill(len(combined_jets), weight)

        # Reconstruct Hadronic Top Quark
        if len(b_quarks) >= 1 and len(w_decay_quarks) >= 2:
            b_p4 = b_quarks[0]['particle']
            q1_p4 = w_decay_quarks[0]['particle']
            q2_p4 = w_decay_quarks[1]['particle']

            b_tlv = ROOT.TLorentzVector()
            b_tlv.SetPtEtaPhiE(b_p4.pt(), b_p4.eta(), b_p4.phi(), b_p4.energy())

            q1_tlv = ROOT.TLorentzVector()
            q1_tlv.SetPtEtaPhiE(q1_p4.pt(), q1_p4.eta(), q1_p4.phi(), q1_p4.energy())

            q2_tlv = ROOT.TLorentzVector()
            q2_tlv.SetPtEtaPhiE(q2_p4.pt(), q2_p4.eta(), q2_p4.phi(), q2_p4.energy())

            hadronic_top = b_tlv + q1_tlv + q2_tlv

        else:
            hadronic_top = None

        # Reconstruct Leptonic Top Quark
        # Using generator-level information (b quark, lepton, neutrino)
        if len(b_quarks) >= 2 and len(leptons) >= 1 and len(neutrinos) >= 1:
            # Use the second b quark for the antitop
            b_leptonic_p4 = b_quarks[1]['particle']
            lepton_p4 = leptons[0]['particle']
            neutrino_p4 = neutrinos[0]['particle']

            # Convert GenParticles to TLorentzVector
            b_leptonic_tlv = ROOT.TLorentzVector()
            b_leptonic_tlv.SetPtEtaPhiE(b_leptonic_p4.pt(), b_leptonic_p4.eta(), b_leptonic_p4.phi(), b_leptonic_p4.energy())

            lepton_tlv = ROOT.TLorentzVector()
            lepton_tlv.SetPtEtaPhiE(lepton_p4.pt(), lepton_p4.eta(), lepton_p4.phi(), lepton_p4.energy())

            neutrino_tlv = ROOT.TLorentzVector()
            neutrino_tlv.SetPtEtaPhiE(neutrino_p4.pt(), neutrino_p4.eta(), neutrino_p4.phi(), neutrino_p4.energy())

            leptonic_top = b_leptonic_tlv + lepton_tlv + neutrino_tlv
        else:
            leptonic_top = None

        # Compute mttbar if both tops are reconstructed
        if hadronic_top and leptonic_top:
            mttbar = (hadronic_top + leptonic_top).M()
            hist_mttbar.Fill(mttbar, weight)

        events_processed_in_file += 1

    file.Close()
    print("Total events processed in this file:", events_processed_in_file)
    return (hist_njets, hist_mttbar, events_processed_in_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process multiple ROOT files to produce m_ttbar histogram with reference weight.')
    parser.add_argument('input_files', nargs='+', help='List of input ROOT files')
    parser.add_argument('--output_file', default='mttbar_multiprocess_900Inf.root', help='Output ROOT file name')
    parser.add_argument('--n_cores', type=int, default=None, help='Number of CPU cores to use')

    args = parser.parse_args()
    input_files = args.input_files
    output_file_name = args.output_file
    n_cores = args.n_cores

    # Create a template histogram
    hist_mttbar_template = ROOT.TH1F("hist_mttbar_template", "Invariant Mass of t#bar{t}; m_{t#bar{t}} [GeV]; Entries", 100, 200, 2000)

    total_events_processed = 0

    # Prepare arguments for each worker
    worker_args = [{'input_file': f} for f in input_files]

    # Use multiprocessing Pool
    pool = multiprocessing.Pool(processes=n_cores)

    try:
        # Map the function to the pool
        results = pool.map(process_file, worker_args)
    except Exception as e:
        print("An error occurred during multiprocessing:", e)
        pool.terminate()
        pool.join()
        sys.exit(1)

    # Close the pool and wait for the work to finish
    pool.close()
    pool.join()

    # Combine the histograms and count total events
    hist_njets_total = ROOT.TH1F("hist_njets_total", "Number of Jets from b quark and W decay; N_{jets}; Entries", 10, 0, 10)
    hist_njets_total.Reset()

    hist_mttbar_total = ROOT.TH1F("hist_mttbar_total", "Invariant Mass of t#bar{t}; m_{t#bar{t}} [GeV]; Entries", 100, 200, 2000)
    hist_mttbar_total.Reset()

    for hist_njets, hist_mttbar, events_processed_in_file in results:
        hist_njets_total.Add(hist_njets)
        hist_mttbar_total.Add(hist_mttbar)
        total_events_processed += events_processed_in_file

    print("\nTotal events processed across all files:", total_events_processed)
    print("Total entries in hist_njets:", hist_njets_total.GetEntries())
    print("Total entries in hist_mttbar:", hist_mttbar_total.GetEntries())

    # Save the combined histograms
    output_file = ROOT.TFile(output_file_name, "RECREATE")
    hist_njets_total.Write()
    hist_mttbar_total.Write()
    output_file.Close()

    # Create separate canvases for njets and mttbar
    canvas_njets = ROOT.TCanvas("canvas_njets", "Number of Jets from b quark and W decay", 800, 600)
    hist_njets_total.SetLineColor(ROOT.kBlue)
    hist_njets_total.SetLineWidth(2)
    hist_njets_total.SetStats(0)  # Disable statistics box
    hist_njets_total.Draw("HIST")
    canvas_njets.SaveAs("number_of_jets_900Inf.png")

    # Draw and save the reconstructed histogram without the statistics box
    canvas_mttbar = ROOT.TCanvas("canvas_mttbar", "Invariant Mass of t#bar{t}", 800, 600)
    hist_mttbar_total.SetLineColor(ROOT.kRed)
    hist_mttbar_total.SetLineWidth(2)
    hist_mttbar_total.SetStats(0)  # Disable statistics box
    hist_mttbar_total.Draw("HIST")
    canvas_mttbar.SaveAs("mttbar_reconstructed_900Inf.png")

    print("\nProcessing complete. Histograms saved as 'number_of_jets_900Inf.png', 'mttbar_reconstructed_900Inf.png', and '{}'.".format(output_file_name))
