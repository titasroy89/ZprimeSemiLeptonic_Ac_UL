import ROOT

# Open the ROOT file
file = ROOT.TFile.Open("Ntuple_1211.root")
if not file or file.IsZombie():
    print("Error opening file")
    exit()

# Get the TTree
tree = file.Get("AnalysisTree")
if not tree:
    print("Error getting TTree")
    file.Close()
    exit()

# Set up the GenParticles branch
genparticles = ROOT.std.vector('GenParticle')()
tree.SetBranchAddress("GenParticles", genparticles)

# Loop over entries
n_entries = tree.GetEntries()
for entry in range(min(10, n_entries)):  # Let's just look at the first 10 entries
    tree.GetEntry(entry)
    print("Entry:", entry)
    for idx, particle in enumerate(genparticles):
        pdgId = particle.pdgId()
        status = particle.status()
        statusFlags = particle.statusFlags()
        print("Index: {}, PDG ID: {}, Status: {}, StatusFlags: {}".format(idx, pdgId, status, statusFlags))
        # Print the bits of statusFlags
        flags = bin(statusFlags)[2:].zfill(15)  # Convert to binary string, pad with zeros
        print("StatusFlags (bits):", flags)
    print("\n")

file.Close()
