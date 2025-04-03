import sys
import ROOT  # PyROOT
import numpy as np
from itertools import combinations

# 1) Define the Wilson coefficient names and indices
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

# mapping for single=2
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

# pairs
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

# 2. Build a mapping from each EFT configuration to its index
#   - SM (all zeros): indices 201 and 202 (they are the same)
#   - Single=1: configurations with one coefficient=1, assigned in order from 203 to 218
#   - Single=2: configurations with one coefficient=2, using SINGLE2_MAPPING
#   - Pairs: the remaining indices between 218-354 that are not used above
def build_config_to_index():
    all_indices = set(range(201, 355))
    sm_indices = {201, 202}  # SM
    single1_indices = set(range(203, 219))  # single=1
    single2_indices = set(SINGLE2_MAPPING.values())

    used = sm_indices.union(single1_indices).union(single2_indices)
    pair_indices = sorted(list(all_indices - used))
    if len(pair_indices) != 120:
        raise RuntimeError("Expected 120 pair configs, got %d" % len(pair_indices))
    
    config2index = {}
    # SM -> index 201
    sm_config = tuple([0]*16)
    config2index[sm_config] = 201

    # Single=1 -> indices 203..218
    for i in range(16):
        arr = [0]*16
        arr[i] = 1
        config2index[tuple(arr)] = 203 + i

    # Single=2 -> from SINGLE2_MAPPING
    for i in range(16):
        arr = [0]*16
        arr[i] = 2
        wc_name = WC_NAMES[i]
        config2index[tuple(arr)] = SINGLE2_MAPPING[wc_name]

    # Pairs=1,1 -> from KNOWN_PAIRS
    for i in range(16):
        for j in range(i+1, 16):
            arr = [0]*16
            arr[i] = 1
            arr[j] = 1
            config2index[tuple(arr)] = KNOWN_PAIRS[(i,j)]

    return config2index

CONFIG2INDEX = build_config_to_index()

def print_config_mapping():
    print("=== Configuration to MG index mapping ===")
    for cfg, idx in sorted(CONFIG2INDEX.items(), key=lambda x: x[1]):
        # Just print some subset
        if idx < 210 or (230 < idx < 240) or idx > 340:
            print("Config %s -> MG index %d" % (str(cfg), idx))
    print("===========================================")

# Build a name dictionary for convenience
WEIGHT_NAMES = {
    "sm_point": 201,
    "sm_point_alt": 202
}
def initialize_weight_names():
    # single=1
    for i in range(16):
        wc_name = WC_NAMES[i]
        WEIGHT_NAMES["%s_1" % wc_name] = 203 + i
    # single=2
    for wc_name, idx in SINGLE2_MAPPING.items():
        WEIGHT_NAMES["%s_2" % wc_name] = idx
    # pairs
    all_indices = set(range(201, 355))
    used = {201, 202}.union(set(range(203, 219))).union(set(SINGLE2_MAPPING.values()))
    pair_indices = sorted(list(all_indices - used))
    offset = 0
    for i in range(16):
        for j in range(i+1,16):
            WEIGHT_NAMES["%s_%s_1_1" % (WC_NAMES[i], WC_NAMES[j])] = pair_indices[offset]
            offset += 1
    print("Initialized WEIGHT_NAMES with %d entries." % len(WEIGHT_NAMES))

def print_available_weights():
    print("\nAvailable weights:")
    print("%-30s %-10s" % ("Weight Name", "Index"))
    print("-"*40)
    for name, idx in sorted(WEIGHT_NAMES.items(), key=lambda x: x[1]):
        print("%-30s %-10d" % (name, idx))

# 3) Generate the 153 configurations
def generate_weight_configurations(num_WCs):
    # 1 SM + 16 single=1 + 16 single=2 + 120 pairs=1,1 => 153
    configs = []
    # SM
    configs.append([0]*num_WCs)
    # single=1
    for i in range(num_WCs):
        arr = [0]*num_WCs
        arr[i] = 1
        configs.append(arr)
    # single=2
    for i in range(num_WCs):
        arr = [0]*num_WCs
        arr[i] = 2
        configs.append(arr)
    # pairs=1,1
    for i in range(num_WCs):
        for j in range(i+1,num_WCs):
            arr = [0]*num_WCs
            arr[i] = 1
            arr[j] = 1
            configs.append(arr)
    if len(configs) != 153:
        raise RuntimeError("Expected 153, got %d" % len(configs))
    return configs

# 4) Associate weights to each config
def associate_weights_to_configs(weight_configs, mg_weights):
    out = []
    for cfg in weight_configs:
        idx = CONFIG2INDEX[tuple(cfg)]
        col = mg_weights[:, idx]
        out.append(col)
    return out

# 5) Solve for structure constants
def obtain_structure_constant(num_WCs, mg_weights):
    configs = generate_weight_configurations(num_WCs)   # 153
    all_cols = associate_weights_to_configs(configs, mg_weights)  # list of 153 arrays
    weight_matrix = np.stack(all_cols, axis=1)  # shape (nEvents, 153)
    nEvents = mg_weights.shape[0]

    # Build design matrix (153 x poly_dim)
    poly_dim = 1 + num_WCs + num_WCs + (num_WCs*(num_WCs-1))//2
    A_rows = []
    for cfg in configs:
        row = [1] + cfg[:]  # constant + linear
        # squares
        for i in range(num_WCs):
            row.append(cfg[i]**2)
        # cross
        for i in range(num_WCs):
            for j in range(i+1,num_WCs):
                row.append(cfg[i]*cfg[j])
        A_rows.append(row)
    A_design = np.array(A_rows)  # shape (153, poly_dim)

    # Fit event by event
    out_structures = []
    for iEvt in range(nEvents):
        wvec = weight_matrix[iEvt]  # shape (153,)
        s, resid, rank, sv = np.linalg.lstsq(A_design, wvec, rcond=None)
        out_structures.append(s)
    return out_structures

# 6) Evaluate polynomial
def event_weights_lin_quad(structure_constants, wc_values):
    """
    structure_constants: shape (nEvents, poly_dim)
    wc_values: length=16
    returns: total_weight, linear_plusSM, quad_plusSM
    """
    sc_array = np.array(structure_constants)
    nEvt = sc_array.shape[0]
    num_WCs = len(wc_values)
    c0 = sc_array[:,0]
    # linear part
    s_linear = sc_array[:, 1:1+num_WCs]
    w_linear = np.dot(s_linear, wc_values)
    # quad part
    quad_list = []
    for i in range(num_WCs):
        quad_list.append(wc_values[i]**2)
    for i in range(num_WCs):
        for j in range(i+1,num_WCs):
            quad_list.append(wc_values[i]*wc_values[j])
    idx_quad_start = 1 + num_WCs
    s_quad = sc_array[:, idx_quad_start:]
    w_quad = np.dot(s_quad, quad_list)
    total_w = c0 + w_linear + w_quad
    return total_w, c0 + w_linear, c0 + w_quad

def print_structure_constants(struct_s, event_idx):
    num_WCs = 16
    print("\nStructure constants for event %d:" % event_idx)
    print("Constant term (SM part):", struct_s[0])
    print("\nLinear terms:")
    for i in range(num_WCs):
        print("  %s: %g" % (WC_NAMES[i], struct_s[1 + i]))
    print("\nQuadratic diag terms:")
    for i in range(num_WCs):
        val = struct_s[1 + num_WCs + i]
        print("  %s^2: %g" % (WC_NAMES[i], val))
    idx = 1 + num_WCs + num_WCs
    print("\nCross terms:")
    for i in range(num_WCs):
        for j in range(i+1, num_WCs):
            val = struct_s[idx]
            print("  %s*%s: %g" % (WC_NAMES[i], WC_NAMES[j], val))
            idx += 1

def save_structure_constants(structs, fname):
    arr = np.array(structs)
    np.save(fname, arr)
    print("Saved structure constants to", fname)

def load_structure_constants(fname):
    arr = np.load(fname)
    print("Loaded shape:", arr.shape)
    return arr

def calculate_new_weights(structs, wc_vals):
    tw,_,_ = event_weights_lin_quad(structs, wc_vals)
    return tw

# MAIN
def main():
    if len(sys.argv) < 3:
        print("Usage: python calc_structure_constants.py <input.root> <output.npy>")
        sys.exit(1)

    rootfile = sys.argv[1]
    outnpy = sys.argv[2]
    f = ROOT.TFile.Open(rootfile)
    if not f or f.IsZombie():
        print("Error opening file:", rootfile)
        sys.exit(1)

    # init
    initialize_weight_names()
    print_available_weights()
    print_config_mapping()

    t = f.Get("AnalysisTree")
    if not t:
        print("Error: no TTree 'AnalysisTree'")
        sys.exit(1)
    nentries = t.GetEntries()
    print("Found %d events" % nentries)

    # check size
    t.GetEntry(0)
    syst0 = t.genInfo.systweights()
    print("Number of weights per event:", syst0.size())

    # store indices 201..354
    mg_weights = np.zeros((nentries, 355), dtype=np.float64)
    for iEvt in range(nentries):
        t.GetEntry(iEvt)
        sw = t.genInfo.systweights()
        for j in range(201,355):
            mg_weights[iEvt, j] = sw[j]
    print("mg_weights shape:", mg_weights.shape)

    # solve
    num_WCs = 16
    structures = obtain_structure_constant(num_WCs, mg_weights)
    print("Got structure constants for %d events" % len(structures))

    # save
    save_structure_constants(structures, outnpy)

    # Print first event
    print_structure_constants(structures[0], 0)

    # Example usage
    print("\nExample reweighting with loaded constants...")
    loaded_s = load_structure_constants(outnpy)
    wc_sm = [0]*num_WCs
    w_sm = calculate_new_weights(loaded_s, wc_sm)
    print("SM weight, event 0:", w_sm[0])

    wc_test = [2.0] + [0.0]*(num_WCs-1)
    w_2 = calculate_new_weights(loaded_s, wc_test)
    print("ctGRe=2, event 0:", w_2[0])

    wc_test2 = [1.0,1.0] + [0.0]*(num_WCs-2)
    w_11 = calculate_new_weights(loaded_s, wc_test2)
    print("ctGRe=1, ctGIm=1, event 0:", w_11[0])

    f.Close()

if __name__ == "__main__":
    main()
