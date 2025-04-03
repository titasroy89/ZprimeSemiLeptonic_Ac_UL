# -*- coding: utf-8 -*-
import sys
import ROOT  # PyROOT
import numpy as np
from itertools import combinations

# 1. Define the Wilson coefficient names and mappings
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
# These indices are those in the genInfo->systweights array
SINGLE2_MAPPING = {
    "ctGRe": 219,  # EFTrwgt217
    "ctGIm": 235,  # EFTrwgt233
    "cQj18": 250,  # EFTrwgt248
    "cQj38": 264,  # EFTrwgt262
    "cQj11": 277,  # EFTrwgt275
    "cQj31": 289,  # EFTrwgt287
    "ctu8": 300,   # EFTrwgt298
    "ctd8": 310,   # EFTrwgt308
    "ctj8": 319,   # EFTrwgt317
    "cQu8": 327,   # EFTrwgt325
    "cQd8": 335,   # EFTrwgt332
    "ctu1": 340,   # EFTrwgt338
    "ctd1": 345,   # EFTrwgt343
    "ctj1": 349,   # EFTrwgt347
    "cQu1": 352,   # EFTrwgt350
    "cQd1": 354    # EFTrwgt352
}

# Verification mapping for all 120 pair indices
KNOWN_PAIRS = {
    # ctGRe (0) pairs: 15 pairs
    (0,1): 220,   # ctGRe_ctGIm_1_1 -> EFTrwgt218
    (0,2): 221,   # ctGRe_cQj18_1_1 -> EFTrwgt219
    (0,3): 222,   # ctGRe_cQj38_1_1 -> EFTrwgt220
    (0,4): 223,   # ctGRe_cQj11_1_1 -> EFTrwgt221
    (0,5): 224,   # ctGRe_cQj31_1_1 -> EFTrwgt222
    (0,6): 225,   # ctGRe_ctu8_1_1 -> EFTrwgt223
    (0,7): 226,   # ctGRe_ctd8_1_1 -> EFTrwgt224
    (0,8): 227,   # ctGRe_ctj8_1_1 -> EFTrwgt225
    (0,9): 228,   # ctGRe_cQu8_1_1 -> EFTrwgt226
    (0,10): 229,  # ctGRe_cQd8_1_1 -> EFTrwgt227
    (0,11): 230,  # ctGRe_ctu1_1_1 -> EFTrwgt228
    (0,12): 231,  # ctGRe_ctd1_1_1 -> EFTrwgt229
    (0,13): 232,  # ctGRe_ctj1_1_1 -> EFTrwgt230
    (0,14): 233,  # ctGRe_cQu1_1_1 -> EFTrwgt231
    (0,15): 234,  # ctGRe_cQd1_1_1 -> EFTrwgt232

    # ctGIm (1) pairs: 14 pairs
    (1,2): 236,   # ctGIm_cQj18_1_1 -> EFTrwgt234
    (1,3): 237,   # ctGIm_cQj38_1_1 -> EFTrwgt235
    (1,4): 238,   # ctGIm_cQj11_1_1 -> EFTrwgt236
    (1,5): 239,   # ctGIm_cQj31_1_1 -> EFTrwgt237
    (1,6): 240,   # ctGIm_ctu8_1_1 -> EFTrwgt238
    (1,7): 241,   # ctGIm_ctd8_1_1 -> EFTrwgt239
    (1,8): 242,   # ctGIm_ctj8_1_1 -> EFTrwgt240
    (1,9): 243,   # ctGIm_cQu8_1_1 -> EFTrwgt241
    (1,10): 244,  # ctGIm_cQd8_1_1 -> EFTrwgt242
    (1,11): 245,  # ctGIm_ctu1_1_1 -> EFTrwgt243
    (1,12): 246,  # ctGIm_ctd1_1_1 -> EFTrwgt244
    (1,13): 247,  # ctGIm_ctj1_1_1 -> EFTrwgt245
    (1,14): 248,  # ctGIm_cQu1_1_1 -> EFTrwgt246
    (1,15): 249,  # ctGIm_cQd1_1_1 -> EFTrwgt247

    # cQj18 (2) pairs: 13 pairs
    (2,3): 251,   # cQj18_cQj38_1_1 -> EFTrwgt249
    (2,4): 252,   # cQj18_cQj11_1_1 -> EFTrwgt250
    (2,5): 253,   # cQj18_cQj31_1_1 -> EFTrwgt251
    (2,6): 254,   # cQj18_ctu8_1_1 -> EFTrwgt252
    (2,7): 255,   # cQj18_ctd8_1_1 -> EFTrwgt253
    (2,8): 256,   # cQj18_ctj8_1_1 -> EFTrwgt254
    (2,9): 257,   # cQj18_cQu8_1_1 -> EFTrwgt255
    (2,10): 258,  # cQj18_cQd8_1_1 -> EFTrwgt256
    (2,11): 259,  # cQj18_ctu1_1_1 -> EFTrwgt257
    (2,12): 260,  # cQj18_ctd1_1_1 -> EFTrwgt258
    (2,13): 261,  # cQj18_ctj1_1_1 -> EFTrwgt259
    (2,14): 262,  # cQj18_cQu1_1_1 -> EFTrwgt260
    (2,15): 263,  # cQj18_cQd1_1_1 -> EFTrwgt261

    # cQj38 (3) pairs: 12 pairs
    (3,4): 265,   # cQj38_cQj11_1_1 -> EFTrwgt263
    (3,5): 266,   # cQj38_cQj31_1_1 -> EFTrwgt264
    (3,6): 267,   # cQj38_ctu8_1_1 -> EFTrwgt265
    (3,7): 268,   # cQj38_ctd8_1_1 -> EFTrwgt266
    (3,8): 269,   # cQj38_ctj8_1_1 -> EFTrwgt267
    (3,9): 270,   # cQj38_cQu8_1_1 -> EFTrwgt268
    (3,10): 271,  # cQj38_cQd8_1_1 -> EFTrwgt269
    (3,11): 272,  # cQj38_ctu1_1_1 -> EFTrwgt270
    (3,12): 273,  # cQj38_ctd1_1_1 -> EFTrwgt271
    (3,13): 274,  # cQj38_ctj1_1_1 -> EFTrwgt272
    (3,14): 275,  # cQj38_cQu1_1_1 -> EFTrwgt273
    (3,15): 276,  # cQj38_cQd1_1_1 -> EFTrwgt274

    # cQj11 (4) pairs: 11 pairs
    (4,5): 278,   # cQj11_cQj31_1_1 -> EFTrwgt276
    (4,6): 279,   # cQj11_ctu8_1_1 -> EFTrwgt277
    (4,7): 280,   # cQj11_ctd8_1_1 -> EFTrwgt278
    (4,8): 281,   # cQj11_ctj8_1_1 -> EFTrwgt279
    (4,9): 282,   # cQj11_cQu8_1_1 -> EFTrwgt280
    (4,10): 283,  # cQj11_cQd8_1_1 -> EFTrwgt281
    (4,11): 284,  # cQj11_ctu1_1_1 -> EFTrwgt282
    (4,12): 285,  # cQj11_ctd1_1_1 -> EFTrwgt283
    (4,13): 286,  # cQj11_ctj1_1_1 -> EFTrwgt284
    (4,14): 287,  # cQj11_cQu1_1_1 -> EFTrwgt285
    (4,15): 288,  # cQj11_cQd1_1_1 -> EFTrwgt286

    # cQj31 (5) pairs: 10 pairs
    (5,6): 290,   # cQj31_ctu8_1_1 -> EFTrwgt288
    (5,7): 291,   # cQj31_ctd8_1_1 -> EFTrwgt289
    (5,8): 292,   # cQj31_ctj8_1_1 -> EFTrwgt290
    (5,9): 293,   # cQj31_cQu8_1_1 -> EFTrwgt291
    (5,10): 294,  # cQj31_cQd8_1_1 -> EFTrwgt292
    (5,11): 295,  # cQj31_ctu1_1_1 -> EFTrwgt293
    (5,12): 296,  # cQj31_ctd1_1_1 -> EFTrwgt294
    (5,13): 297,  # cQj31_ctj1_1_1 -> EFTrwgt295
    (5,14): 298,  # cQj31_cQu1_1_1 -> EFTrwgt296
    (5,15): 299,  # cQj31_cQd1_1_1 -> EFTrwgt297

    # ctu8 (6) pairs: 9 pairs
    (6,7): 301,   # ctu8_ctd8_1_1 -> EFTrwgt299
    (6,8): 302,   # ctu8_ctj8_1_1 -> EFTrwgt300
    (6,9): 303,   # ctu8_cQu8_1_1 -> EFTrwgt301
    (6,10): 304,  # ctu8_cQd8_1_1 -> EFTrwgt302
    (6,11): 305,  # ctu8_ctu1_1_1 -> EFTrwgt303
    (6,12): 306,  # ctu8_ctd1_1_1 -> EFTrwgt304
    (6,13): 307,  # ctu8_ctj1_1_1 -> EFTrwgt305
    (6,14): 308,  # ctu8_cQu1_1_1 -> EFTrwgt306
    (6,15): 309,  # ctu8_cQd1_1_1 -> EFTrwgt307

    # ctd8 (7) pairs: 8 pairs
    (7,8): 311,   # ctd8_ctj8_1_1 -> EFTrwgt309
    (7,9): 312,   # ctd8_cQu8_1_1 -> EFTrwgt310
    (7,10): 313,  # ctd8_cQd8_1_1 -> EFTrwgt311
    (7,11): 314,  # ctd8_ctu1_1_1 -> EFTrwgt312
    (7,12): 315,  # ctd8_ctd1_1_1 -> EFTrwgt313
    (7,13): 316,  # ctd8_ctj1_1_1 -> EFTrwgt314
    (7,14): 317,  # ctd8_cQu1_1_1 -> EFTrwgt315
    (7,15): 318,  # ctd8_cQd1_1_1 -> EFTrwgt316

    # ctj8 (8) pairs: 7 pairs
    (8,9): 320,   # ctj8_cQu8_1_1 -> EFTrwgt318
    (8,10): 321,  # ctj8_cQd8_1_1 -> EFTrwgt319
    (8,11): 322,  # ctj8_ctu1_1_1 -> EFTrwgt320
    (8,12): 323,  # ctj8_ctd1_1_1 -> EFTrwgt321
    (8,13): 324,  # ctj8_ctj1_1_1 -> EFTrwgt322
    (8,14): 325,  # ctj8_cQu1_1_1 -> EFTrwgt323
    (8,15): 326,  # ctj8_cQd1_1_1 -> EFTrwgt324

    # cQu8 (9) pairs: 6 pairs
    (9,10): 328,  # cQu8_cQd8_1_1 -> EFTrwgt326
    (9,11): 329,  # cQu8_ctu1_1_1 -> EFTrwgt327
    (9,12): 330,  # cQu8_ctd1_1_1 -> EFTrwgt328
    (9,13): 331,  # cQu8_ctj1_1_1 -> EFTrwgt329
    (9,14): 332,  # cQu8_cQu1_1_1 -> EFTrwgt330
    (9,15): 333,  # cQu8_cQd1_1_1 -> EFTrwgt331

    # cQd8 (10) pairs: 5 pairs
    (10,11): 335, # cQd8_ctu1_1_1 -> EFTrwgt333
    (10,12): 336, # cQd8_ctd1_1_1 -> EFTrwgt334
    (10,13): 337, # cQd8_ctj1_1_1 -> EFTrwgt335
    (10,14): 338, # cQd8_cQu1_1_1 -> EFTrwgt336
    (10,15): 339, # cQd8_cQd1_1_1 -> EFTrwgt337

    # ctu1 (11) pairs: 4 pairs
    (11,12): 341, # ctu1_ctd1_1_1 -> EFTrwgt339
    (11,13): 342, # ctu1_ctj1_1_1 -> EFTrwgt340
    (11,14): 343, # ctu1_cQu1_1_1 -> EFTrwgt341
    (11,15): 344, # ctu1_cQd1_1_1 -> EFTrwgt342

    # ctd1 (12) pairs: 3 pairs
    (12,13): 346, # ctd1_ctj1_1_1 -> EFTrwgt344
    (12,14): 347, # ctd1_cQu1_1_1 -> EFTrwgt345
    (12,15): 348, # ctd1_cQd1_1_1 -> EFTrwgt346

    # ctj1 (13) pairs: 2 pairs
    (13,14): 350, # ctj1_cQu1_1_1 -> EFTrwgt348
    (13,15): 351, # ctj1_cQd1_1_1 -> EFTrwgt349

    # cQu1 (14) pairs: 1 pair
    (14,15): 353  # cQu1_cQd1_1_1 -> EFTrwgt351
}

# 2. Build a mapping from each EFT configuration to its MG index
# The idea is to assign:
#   - SM (all zeros): indices 201 and 202 (they are the same)
#   - Single=1: configurations with one coefficient=1, assigned in order from 203 to 218
#   - Single=2: configurations with one coefficient=2, using SINGLE2_MAPPING
#   - Pairs: the remaining indices between 218-354 that are not used above
def build_config_to_index():
    all_indices = set(range(201, 355))  # indices 201..354 inclusive
    sm_indices = {201, 202}  # Both 201 and 202 are SM points
    single1_indices = set(range(203, 219))  # 203..218 inclusive
    single2_indices = set(SINGLE2_MAPPING.values())
    used = sm_indices.union(single1_indices).union(single2_indices)
    pair_indices = sorted(list(all_indices - used))
    if len(pair_indices) != 120:
        raise RuntimeError("Expected 120 pair configurations, got %d" % len(pair_indices))
    
    config2index = {}
    # SM configuration maps to both 201 and 202
    sm_config = tuple([0]*16)
    config2index[sm_config] = 201  # We'll use 201 as the canonical SM index
    
    # Single=1: indices 203-218
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
    
    # Pairs (1,1): For each pair i<j, configuration with both set to 1
    pair_list = []
    for i in range(16):
        for j in range(i+1, 16):
            config = [0]*16
            config[i] = 1
            config[j] = 1
            pair_list.append((i, j, tuple(config)))
    
    if len(pair_list) != 120:
        raise RuntimeError("Expected 120 pair configurations, got %d" % len(pair_list))
    
    # Use KNOWN_PAIRS directly for pair indices
    for i in range(16):
        for j in range(i+1, 16):
            config = [0]*16
            config[i] = 1
            config[j] = 1
            config2index[tuple(config)] = KNOWN_PAIRS[(i,j)]
    
    return config2index

CONFIG2INDEX = build_config_to_index()

def print_config_mapping():
    print "=== Configuration to MG index mapping ==="
    
    for cfg, idx in sorted(CONFIG2INDEX.items(), key=lambda x: x[1]):
        # Print only a subset for verification
        if idx < 210 or (230 < idx < 240) or idx > 340:
            print "Config %s -> MG index %d" % (str(cfg), idx)
    
    print "==========================================="

# 3. Build a simple name dictionary for convenience
WEIGHT_NAMES = {
    "sm_point": 201,  # Both 201 and 202 are SM points
    "sm_point_alt": 202
}

def initialize_weight_names():
    # Single=1: indices 203-218
    for i in range(16):
        wc_name = WC_NAMES[i]
        WEIGHT_NAMES["%s_1" % wc_name] = 203 + i
    
    # Single=2: from our SINGLE2_MAPPING
    for wc_name, idx in SINGLE2_MAPPING.items():
        WEIGHT_NAMES["%s_2" % wc_name] = idx
    
    # Pairs: assign in lexicographic order over (i,j) using the remaining indices
    all_indices = set(range(201, 355))
    used = {201, 202}.union(set(range(203, 219))).union(set(SINGLE2_MAPPING.values()))
    pair_indices = sorted(list(all_indices - used))
    offset = 0
    for i in range(16):
        for j in range(i+1, 16):
            WEIGHT_NAMES["%s_%s_1_1" % (WC_NAMES[i], WC_NAMES[j])] = pair_indices[offset]
            offset += 1
    print "Initialized WEIGHT_NAMES with %d entries." % len(WEIGHT_NAMES)

def print_available_weights():
    """Print all available weight names and their indices"""
    print "\nAvailable weights:"
    
    print "%-30s %-10s" % ("Weight Name", "Index")
    
    print "-" * 40
    
    for name, idx in sorted(WEIGHT_NAMES.items(), key=lambda x: x[1]):
        print "%-30s %-10d" % (name, idx)

# ---------------------------------------------------------
# 4. Functions to generate the 153 EFT basis configurations

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

# ---------------------------------------------------------
# 5. Associate the EFT weights from mg_weights with the configurations

def associate_weights_to_configs(weight_configs, mg_weights):
    """
    For each configuration (a 16tuple) use CONFIG2INDEX to select
    the corresponding column from mg_weights.
    """
    weights_correspon = []
    for config in weight_configs:
        cfg_tuple = tuple(config)
        if cfg_tuple not in CONFIG2INDEX:
            raise KeyError("Configuration %s not found in CONFIG2INDEX" % str(cfg_tuple))
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
# Print structure constants for an event
###########################################################
def print_structure_constants(structure_constants, event_idx):
    """Print the structure constants for a given event"""
    num_WCs = 16
    print "\nStructure constants for event %d:" % event_idx
    print "Constant term: %g" % structure_constants[0]
    
    print "\nLinear terms:"
    for i in range(num_WCs):
        print "  %s: %g" % (WC_NAMES[i], structure_constants[1 + i])
    
    print "\nQuadratic terms (diagonal):"
    for i in range(num_WCs):
        print "  %s^2: %g" % (WC_NAMES[i], structure_constants[1 + num_WCs + i])
    
    print "\nQuadratic terms (cross terms):"
    idx = 1 + num_WCs + num_WCs  # Start of cross terms
    for i in range(num_WCs):
        for j in range(i+1, num_WCs):
            print "  %s*%s: %g" % (WC_NAMES[i], WC_NAMES[j], structure_constants[idx])
            idx += 1

###########################################################
# Save and load structure constants
###########################################################
def save_structure_constants(structures, output_file):
    """Save structure constants to a .npy file"""
    np.save(output_file, structures)
    print "Saved structure constants to %s" % output_file

def load_structure_constants(input_file):
    """Load structure constants from a .npy file"""
    structures = np.load(input_file)
    print "Loaded structure constants from %s" % input_file
    print "Shape:", structures.shape
    return structures

def calculate_new_weights(structures, wc_values):
    """Calculate weights for new WC points using pre-computed structure constants"""
    total_weights, linear_weights, quad_weights = event_weights_lin_quad(structures, wc_values)
    return total_weights

###########################################################
# 8. MAIN: Read the weights from the TTree and solve
###########################################################
def main():
    if len(sys.argv) < 3:
        print "Usage: python collect_EFT_reweight.py <myFile.root> <output_structure_constants.npy>"
        sys.exit(1)
    
    root_filename = sys.argv[1]
    output_file = sys.argv[2]
    f = ROOT.TFile.Open(root_filename)
    
    if not f or f.IsZombie():
        print "Error: cannot open file", root_filename
        sys.exit(1)
    
    # Initialize our mapping dictionaries.
    initialize_weight_names()
    print_available_weights()
    print_config_mapping()
    
    # Get the TTree. (The tree is named "AnalysisTree".)
    t = f.Get("AnalysisTree")
    if not t:
        print "Error: cannot find TTree 'AnalysisTree'"
        sys.exit(1)
    
    nentries = t.GetEntries()
    print "Found %d events in the tree." % nentries
    
    # First determine the size of the weights vector from the first event
    t.GetEntry(0)
    syst = t.genInfo.systweights()
    print "Number of weights per event:", syst.size()
    
    # Pre-allocate the numpy array with the correct shape for indices 201-354
    mg_weights = np.zeros((nentries, 355), dtype=np.float64)  # Include 0-200 for simplicity
    
    # Now fill the array with only the weights we need (201-354)
    for ientry in range(nentries):
        t.GetEntry(ientry)
        syst = t.genInfo.systweights()
        for j in range(201, 355):  # Only collect weights 201-354
            mg_weights[ientry, j] = syst[j]
    
    print "mg_weights shape:", mg_weights.shape
    
    # Example: print a few weights from the first event using our WEIGHT_NAMES mapping.
    print "\nExample weights for first event:"
    for key in ["sm_point", "ctGRe_1", "ctGRe_2"]:
        if key in WEIGHT_NAMES:
            idx = WEIGHT_NAMES[key]
            print "%s: mg_weights[0, %d] = %g" % (key, idx, mg_weights[0, idx])
    
    # Now solve for structure constants using the EFT weights from index 201 to 354.
    num_WCs = 16
    structures = obtain_structure_constant(num_WCs, mg_weights)
    print "Obtained structure constants for %d events." % len(structures)
    
    # Save structure constants
    save_structure_constants(structures, output_file)
    
    # Print structure constants for first event
    print_structure_constants(structures[0], 0)
    
    # Example usage with saved structure constants:
    print "\nExample reweighting using saved structure constants:"
    # Load the saved constants (just to demonstrate)
    loaded_structures = load_structure_constants(output_file)
    
    # Calculate weights for some example points
    print "\nCalculating weights for example points:"
    
    # SM point
    wc_values_sm = [0]*num_WCs
    w_sm = calculate_new_weights(loaded_structures, wc_values_sm)
    print "SM weight (first event): %g" % w_sm[0]
    
    # ctGRe = 2
    wc_test1 = [2.0] + [0.0]*(num_WCs-1)
    w_test1 = calculate_new_weights(loaded_structures, wc_test1)
    print "Weight for ctGRe=2 (first event): %g" % w_test1[0]
    
    # ctGRe = 1, ctGIm = 1
    wc_test2 = [1.0, 1.0] + [0.0]*(num_WCs-2)
    w_test2 = calculate_new_weights(loaded_structures, wc_test2)
    print "Weight for ctGRe=1, ctGIm=1 (first event): %g" % w_test2[0]
    
    f.Close()

if __name__ == "__main__":
    main()
