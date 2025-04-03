#!/usr/bin/env python
import sys
import ROOT  # PyROOT
import numpy as np
from itertools import combinations

#####################################################
# 1. Define the Wilson coefficient names and mappings
#####################################################
# Our 16 Wilson coefficients (use the order you need)
WC_NAMES = {
    0: "ctGRe",
    1: "ctGIm",
    2: "cQj18",
    3: "cQj38",
    4: "cQj11",
    5: "cQj31",
    6: "ctu8",
    7: "ctd8",
    8: "ctj8",
    9: "cQu8",
    10: "cQd8",
    11: "ctu1",
    12: "ctd1",
    13: "ctj1",
    14: "cQu1",
    15: "cQd1"
}
WC_INDICES = {name: idx for idx, name in WC_NAMES.items()}

# Hard-coded mapping for single WC = 2 weights.
# (These indices are those in the genInfo->systweights array.)
SINGLE2_MAPPING = {
    "ctGRe": 219,
    "ctGIm": 235,
    "cQj18": 250,
    "cQj38": 264,
    "cQj11": 277,
    "cQj31": 289,
    "ctu8": 300,
    "ctd8": 310,
    "ctj8": 319,
    "cQu8": 327,
    "cQd8": 335,
    "ctu1": 340,
    "ctd1": 345,
    "ctj1": 349,
    "cQu1": 352,
    "cQd1": 354
}

##########################################################
# 2. Build a mapping from each EFT configuration to its MG index
##########################################################
# The idea is to assign:
#   - SM (all zeros): index 201
#   - Single=1: configurations with one coefficient=1, assigned in order from 203 to 218.
#   - Single=2: configurations with one coefficient=2, using SINGLE2_MAPPING.
#   - Pairs: the remaining indices from 201 to 354 that are not used above.
def build_config_to_index():
    all_indices = set(range(201, 355))  # indices 201..354 inclusive
    sm_index = {201}
    single1_indices = set(range(203, 203+16))  # 203..218
    single2_indices = set(SINGLE2_MAPPING.values())
    used = sm_index.union(single1_indices).union(single2_indices)
    pair_indices = sorted(list(all_indices - used))
    if len(pair_indices) != 120:
        raise RuntimeError("Expected 120 pair indices but found %d" % len(pair_indices))
    config2index = {}
    # SM configuration
    config2index[tuple([0]*16)] = 201
    # Single=1
    for i in range(16):
        config = [0]*16
        config[i] = 1
        config2index[tuple(config)] = 203 + i
    # Single=2 using hard-coded mapping
    for i in range(16):
        config = [0]*16
        config[i] = 2
        wc_name = WC_NAMES[i]
        config2index[tuple(config)] = SINGLE2_MAPPING[wc_name]
    # Pairs (1,1): For each pair i<j, configuration with both set to 1.
    pair_list = []
    for i in range(16):
        for j in range(i+1, 16):
            config = [0]*16
            config[i] = 1
            config[j] = 1
            pair_list.append((i, j, tuple(config)))
    if len(pair_list) != 120:
        raise RuntimeError("Expected 120 pair configurations, got %d" % len(pair_list))
    for k, (_, _, cfg) in enumerate(pair_list):
        config2index[cfg] = pair_indices[k]
    return config2index

CONFIG2INDEX = build_config_to_index()

def print_config_mapping():
    print("=== Configuration to MG index mapping ===")
    for cfg, idx in sorted(CONFIG2INDEX.items(), key=lambda x: x[1]):
        # Print only a subset for verification
        if idx < 210 or (230 < idx < 240) or idx > 340:
            print("Config", cfg, "-> MG index", idx)
    print("===========================================")

#####################################################
# 3. Build a simple name dictionary for convenience
#####################################################
# Here we want to be able to write, e.g., get_weight_by_name(mg_weights, "ctGRe_1")
# We define a dictionary WEIGHT_NAMES mapping name->index.
WEIGHT_NAMES = {"sm_point": 201}
def initialize_weight_names():
    # Single=1: assume they appear in order from 203 to 218.
    for i in range(16):
        wc_name = WC_NAMES[i]
        WEIGHT_NAMES[f"{wc_name}_1"] = 203 + i
    # Single=2: from our SINGLE2_MAPPING.
    for i in range(16):
        wc_name = WC_NAMES[i]
        WEIGHT_NAMES[f"{wc_name}_2"] = SINGLE2_MAPPING[wc_name]
    # Pairs: assign in lexicographic order over (i,j) using the remaining indices.
    all_indices = set(range(201,355))
    used = {201}.union(set(range(203,203+16))).union(set(SINGLE2_MAPPING.values()))
    pair_indices = sorted(list(all_indices - used))
    offset = 0
    for i in range(16):
        for j in range(i+1, 16):
            WEIGHT_NAMES[f"{WC_NAMES[i]}_{WC_NAMES[j]}_1_1"] = pair_indices[offset]
            offset += 1
    print("Initialized WEIGHT_NAMES with", len(WEIGHT_NAMES), "entries.")

def print_available_weights():
    print("\nAvailable weights:")
    print(f"{'Weight Name':<30} {'Index':<10}")
    print("-" * 40)
    for name, idx in sorted(WEIGHT_NAMES.items(), key=lambda x: x[1]):
        print(f"{name:<30} {idx:<10}")

###########################################################
# 4. Functions to generate the 153 EFT basis configurations
###########################################################
def generate_weight_configurations(num_WCs):
    """
    Generate 153 EFT configurations:
      - SM: all zeros (1 configuration)
      - Single=1: 16 configurations (one 1 each)
      - Single=2: 16 configurations (one 2 each)
      - Pairs: 120 configurations (two entries =1)
    """
    weight_configs = []
    weight_configs.append([0]*num_WCs)  # SM
    for i in range(num_WCs):
        config = [0]*num_WCs
        config[i] = 1
        weight_configs.append(config)
    for i in range(num_WCs):
        config = [0]*num_WCs
        config[i] = 2
        weight_configs.append(config)
    for i in range(num_WCs):
        for j in range(i+1, num_WCs):
            config = [0]*num_WCs
            config[i] = 1
            config[j] = 1
            weight_configs.append(config)
    if len(weight_configs) != 153:
        raise RuntimeError("Expected 153 configurations, got %d" % len(weight_configs))
    return weight_configs

###########################################################
# 5. Associate the EFT weights from mg_weights with the configurations
###########################################################
def associate_weights_to_configs(weight_configs, mg_weights):
    """
    For each configuration (a 16‐tuple) use CONFIG2INDEX to select
    the corresponding column from mg_weights.
    """
    weights_correspon = []
    for config in weight_configs:
        cfg_tuple = tuple(config)
        if cfg_tuple not in CONFIG2INDEX:
            raise KeyError("Configuration {} not found in CONFIG2INDEX".format(cfg_tuple))
        mg_idx = CONFIG2INDEX[cfg_tuple]
        col_data = mg_weights[:, mg_idx]
        weights_correspon.append(col_data)
    return weights_correspon

###########################################################
# 6. Solve for structure constants via least-squares fit
###########################################################
def obtain_structure_constant(num_WCs, mg_weights):
    weight_configs = generate_weight_configurations(num_WCs)
    weight_all = associate_weights_to_configs(weight_configs, mg_weights)
    num_events = mg_weights.shape[0]
    structures = []
    weight_matrix = np.stack(weight_all, axis=1)  # shape (nEvents, 153)
    # Build the design matrix A once (same for all events)
    poly_dim = 1 + num_WCs + num_WCs + (num_WCs*(num_WCs-1))//2
    A_rows = []
    for config in weight_configs:
        row = [1] + config[:]  # constant + linear terms
        for k in range(num_WCs):
            row.append(config[k]**2)
        for k1, k2 in combinations(range(num_WCs), 2):
            row.append(config[k1]*config[k2])
        A_rows.append(row)
    A_design = np.array(A_rows)  # shape (153, poly_dim)
    for i in range(num_events):
        w = weight_matrix[i]  # shape (153,)
        s, residuals, rank, sv = np.linalg.lstsq(A_design, w, rcond=None)
        structures.append(s)
    return structures

###########################################################
# 7. Evaluate polynomial at a chosen WC point
###########################################################
def event_weights_lin_quad(structure_constants, wc_values):
    num_WCs = len(wc_values)
    sc_array = np.array(structure_constants)  # shape (nEvents, poly_dim)
    c0 = sc_array[:, 0]
    s_linear = sc_array[:, 1:1+num_WCs]
    w_linear = np.dot(s_linear, wc_values)
    quad_terms = [x**2 for x in wc_values]
    for i, j in combinations(range(num_WCs), 2):
        quad_terms.append(wc_values[i]*wc_values[j])
    idx_quad_start = 1 + num_WCs
    s_quad = sc_array[:, idx_quad_start:]
    w_quad = np.dot(s_quad, quad_terms)
    total_weight = c0 + w_linear + w_quad
    w_linear_with_sm = c0 + w_linear
    w_quad_with_sm = c0 + w_quad
    return total_weight, w_linear_with_sm, w_quad_with_sm

###########################################################
# 8. MAIN: Read the weights from the TTree and solve
###########################################################
def main():
    if len(sys.argv) < 2:
        print("Usage: python collect_EFT_reweight.py <myFile.root>")
        sys.exit(1)
    root_filename = sys.argv[1]
    f = ROOT.TFile.Open(root_filename)
    if not f or f.IsZombie():
        print("Error: cannot open file", root_filename)
        sys.exit(1)
    # Initialize our mapping dictionaries.
    initialize_weight_names()
    print_available_weights()
    print_config_mapping()
    
    # Get the TTree. (Assume the tree is named "Events".)
    t = f.Get("Events")
    if not t:
        print("Error: cannot find TTree 'Events'")
        sys.exit(1)
    nentries = t.GetEntries()
    print("Found", nentries, "events in the tree.")
    
    # Build an array mg_weights (shape: nEvents x nTotalWeights) by reading genInfo->systweights().
    # In PyROOT, if each event has a member genInfo, and genInfo has a method systweights()
    # that returns a vector, then for each event we can do:
    mg_weights_list = []
    for ientry in range(nentries):
        t.GetEntry(ientry)
        # Access the vector of EFT weights from the genInfo object.
        syst = t.genInfo.systweights()  # assuming this works in PyROOT
        # Convert to a Python list.
        arr = [syst[j] for j in range(syst.size())]
        mg_weights_list.append(arr)
    mg_weights = np.array(mg_weights_list, dtype=np.float64)
    print("mg_weights shape:", mg_weights.shape)
    
    # Example: print a few weights from the first event using our WEIGHT_NAMES mapping.
    print("\nExample weights for first event:")
    for key in ["sm_point", "ctGRe_1", "ctGRe_2"]:
        if key in WEIGHT_NAMES:
            idx = WEIGHT_NAMES[key]
            print(f"{key}: mg_weights[0, {idx}] = {mg_weights[0, idx]}")
    
    # Now solve for structure constants using the EFT weights from index 201 to 354.
    num_WCs = 16
    structures = obtain_structure_constant(num_WCs, mg_weights)
    print("Obtained structure constants for", len(structures), "events.")
    
    # Evaluate at SM (all zeros)
    wc_values_sm = [0]*num_WCs
    w_sm, w_lin_sm, w_quad_sm = event_weights_lin_quad(structures, wc_values_sm)
    print("Event 0 SM weight (from structure constants):", w_sm[0])
    
    # Evaluate at a test point (for example, ctGRe=2, all others 0)
    wc_test = [2.0] + [0.0]*(num_WCs-1)
    w_test, _, _ = event_weights_lin_quad(structures, wc_test)
    print("Event 0 test weight (ctGRe=2):", w_test[0])
    
    f.Close()

if __name__ == "__main__":
    main()
