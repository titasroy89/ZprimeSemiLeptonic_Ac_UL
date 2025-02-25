import sys
import ROOT  # PyROOT
import numpy as np
from itertools import combinations

# ---------------------------------------------------------
# 1) Generate the 153 "basis" configurations (SM, single=1, single=2, pairs=1,1)

def generate_weight_configurations(num_WCs):
    """
    Generates the Wilson coefficient configurations for 153 weights:
      - 1 SM point
      - 16 single WCs=1
      - 16 single WCs=2
      - pairs of WCs=1 (16 choose 2 = 120)
    """
    weight_configs = []
    # SM (all zeros)
    weight_configs.append([0]*num_WCs)

    # single WCs=1
    for i in range(num_WCs):
        config = [0]*num_WCs
        config[i] = 1
        weight_configs.append(config)

    # single WCs=2 + pairs=1,1
    for i in range(num_WCs):
        config = [0]*num_WCs
        config[i] = 2
        weight_configs.append(config)

        for j in range(i+1, num_WCs):
            config = [0]*num_WCs
            config[i] = 1
            config[j] = 1
            weight_configs.append(config)

    return weight_configs

# ---------------------------------------------------------
# 2) Associate your mg_weights with these configurations

def associate_weights_to_configs(weight_configs, mg_weights):
    """
    Assumes your 153 EFT reweights start at column index 200 in mg_weights.
    mg_weights has shape (nEvents, nTotalWeights).
    """
    # For each of the 153 basis configurations,
    # pick out the corresponding column in mg_weights.
    # If your EFT weights start at a different index (not 200),
    # change '200' accordingly.
    weights_correspon = []
    for i in range(len(weight_configs)):
        col_data = mg_weights[:, 200 + i]  # slice out the column for this reweight
        weights_correspon.append(col_data)
    return weights_correspon

# ---------------------------------------------------------
# 3) Solve for structure constants via a least-squares fit

def obtain_structure_constant(num_WCs, mg_weights):
    """
    Builds the matrix A of (153 x polynomial dimension) for each event,
    and solves for that event's polynomial coefficients s (the structure constants).
    """
    weight_configs = generate_weight_configurations(num_WCs)
    weight_all = associate_weights_to_configs(weight_configs, mg_weights)

    num_events = len(weight_all[0])  # same as mg_weights.shape[0]
    structures = []

    # Stack the columns (list of arrays) into a shape (nEvents, 153)
    weight_matrix = np.stack(weight_all, axis=1)

    # For each event, solve the system A*s = w
    for i in range(num_events):
        A_rows = []
        # Build one row in matrix A for each of the 153 configs
        # row = [1, wc1, wc2, ..., wcN, wc1^2, ..., wcN^2, wc1*wc2, ...]
        for wc_values in weight_configs:
            row = [1] + wc_values[:]  # constant + linear
            # squares
            for k in range(num_WCs):
                row.append(wc_values[k]**2)
            # cross terms
            for k1, k2 in combinations(range(num_WCs), 2):
                row.append(wc_values[k1] * wc_values[k2])
            A_rows.append(row)

        A = np.array(A_rows)
        w = weight_matrix[i]  # shape (153,)

        s, residuals, rank, sv = np.linalg.lstsq(A, w, rcond=None)
        structures.append(s)

    return structures

# ---------------------------------------------------------
# 4) Evaluate polynomial at any WC point

def event_weights_lin_quad(structure_constants, wc_values):
    """
    Computes (total_weight, linear+SM_weight, quadratic+SM_weight) for each event,
    given the array of polynomial coefficients `structure_constants` and
    the desired WC vector `wc_values`.
    """
    num_WCs = len(wc_values)
    sc_array = np.array(structure_constants)  # shape: (nEvents, polynomialDimension)

    # sc_array[:,0] is c0 for each event (the SM part)
    c0 = sc_array[:, 0]

    # linear region -> columns 1..(N)
    s_linear = sc_array[:, 1:1+num_WCs]
    w_linear = np.dot(s_linear, wc_values)

    # quadratic region -> next come N squares + N(N-1)/2 cross terms
    quad_terms = []
    for i in range(num_WCs):
        quad_terms.append(wc_values[i]**2)
    for i, j in combinations(range(num_WCs), 2):
        quad_terms.append(wc_values[i]*wc_values[j])

    # columns after the linear part
    idx_quad_start = 1 + num_WCs
    s_quad = sc_array[:, idx_quad_start:]
    w_quad = np.dot(s_quad, quad_terms)

    total_weight = c0 + w_linear + w_quad
    w_linear_with_sm = c0 + w_linear
    w_quad_with_sm = c0 + w_quad

    return total_weight, w_linear_with_sm, w_quad_with_sm

# ---------------------------------------------------------
# MAIN: PyROOT portion to read in mg_weights

def main():
    if len(sys.argv) < 2:
        print("Usage: python2 myEFTScript.py <myFile.root>")
        sys.exit(1)

    root_filename = sys.argv[1]
    # Open the ROOT file
    f = ROOT.TFile.Open(root_filename)
    if not f or f.IsZombie():
        print("Error: cannot open file", root_filename)
        sys.exit(1)

    # Grab the TTree, e.g. "Events"
    t = f.Get("Events")
    if not t:
        print("Error: cannot find TTree named 'Events'")
        sys.exit(1)

    nentries = t.GetEntries()
    print("Found", nentries, "events in the tree.")

    # Here we must figure out how to retrieve the LHE/EFT reweights.
    # The exact method depends on how the weights are stored. For demonstration,
    # let's assume there's a branch "lheWeights" of type std::vector<double>.
    # We'll read them event-by-event and store them in a Python list.

    mg_weights_list = []
    for ientry in range(nentries):
        t.GetEntry(ientry)
        # Suppose we have a branch called "lheWeights" that's a std::vector<double>
        # in the TTree. We'll read it like this:
        # (In real miniAOD, you might have LHEEventProduct. We do a toy example.)
        lhevec = getattr(t, "lheWeights", None)
        if not lhevec:
            print("Error: cannot find 'lheWeights' branch or object in the event!")
            sys.exit(1)

        # Convert the std::vector<double> to a Python list
        arr = [lhevec[j] for j in range(lhevec.size())]
        mg_weights_list.append(arr)

    mg_weights = np.array(mg_weights_list, dtype=np.float64)  # shape: (nEvents, nTotalWeights)

    print("mg_weights shape:", mg_weights.shape)

    # ----------------------------------------------------------------
    # Now we can run the structure-constant extraction with N=16 WCs
    # Adjust the number if you have fewer or more WCs.

    num_WCs = 16
    structures = obtain_structure_constant(num_WCs, mg_weights)
    print("Fitted structure constants for", len(structures), "events.")

    # Example: Evaluate the SM weight (all WCs=0) for each event
    wc_values_sm = [0]*num_WCs
    w_sm, w_lin_sm, w_quad_sm = event_weights_lin_quad(structures, wc_values_sm)
    print("Example SM reweight for event 0:", w_sm[0])

    # Example: Evaluate at some arbitrary point (ctGRe=2, etc.),
    # just as a demonstration. You must match the ordering in generate_weight_configurations
    # if it is c1=ctGRe, c2=ctGIm, ...
    wc_test = [2.0] + [0.0]*(num_WCs-1)
    w_test, _, _ = event_weights_lin_quad(structures, wc_test)
    print("Test reweight for event 0:", w_test[0])

    f.Close()

if __name__ == "__main__":
    main()
