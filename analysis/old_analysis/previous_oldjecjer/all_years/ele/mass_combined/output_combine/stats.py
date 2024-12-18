import ROOT

root_file_path = "higgsCombine_paramFit_Test_allConstrainedNuisancesFrozen.MultiDimFit.mH125.root"

file = ROOT.TFile.Open(root_file_path)

if not file or file.IsZombie():
    print("Error opening file:", root_file_path)
else:
    print("Successfully opened file:", root_file_path)

    tree = file.Get("limit")

    if not tree:
        print("Error: 'limit' tree not found in the file.")
    else:
        tree.Print()
        
        Ac = ROOT.Double(0)
        r_neg = ROOT.Double(0)

        tree.SetBranchAddress("Ac", Ac)
        tree.SetBranchAddress("r_neg", r_neg)

        for i in range(tree.GetEntries()):
            tree.GetEntry(i)
            print("Stat-Only Post-Fit Values (Entry {i}):".format(i))
            print("  Ac: {}".format(Ac))
            print("  r_neg: {}".format(r_neg))

    file.Close()