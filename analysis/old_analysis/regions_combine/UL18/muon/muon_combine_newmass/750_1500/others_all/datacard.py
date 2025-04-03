def create_datacard(year, mass_range, lepton_flavor):
    filename = 'datacard_{}_{}_{}.txt'.format(year, lepton_flavor, mass_range)
    filepath = 'combine_input/dY_{}_{}_{}.root'.format(year, lepton_flavor, mass_range)
    bins = ["SR", "CR1", "CR2"]
    processes = ["TTbar_1", "TTbar_2", "ST", "Others"]
    num_processes = len(processes) - 1  # jmax is number of processes minus 1
    
    with open(filename, 'w') as file:
        file.write("imax {} number of bins\n".format(len(bins)))
        file.write("jmax {} number of processes minus 1\n".format(num_processes))
        file.write("kmax * number of nuisance parameters\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        
        for bin in bins:
            file.write("shapes * muon_UL18_{2}_{1} {0} {1}/$PROCESS {1}/$PROCESS_$SYSTEMATIC\n".format(filepath, bin, mass_range))
        file.write("shapes data_obs * {0} {1}/data_obs\n".format(filepath, bins[0])) 
        
        # file.write("shapes data_obs     *       {} $PROCESS\n".format(filepath))
        # file.write("shapes *            *       {} $PROCESS $PROCESS_$SYSTEMATIC\n".format(filepath))
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        
        # Bin and observation section
        file.write("bin                     {0}_{1}_{2}_SR          {0}_{1}_{2}_CR1           {0}_{1}_{2}_CR2\n".format(lepton_flavor, year, mass_range))
        file.write("observation             -1                            -1                              -1\n")
        
        # bin_names = ["{}_{}_{}_{}".format(lepton_flavor, year, mass_range, bin) for bin in bins]
        # file.write("observation  -1\n")
        
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("bin                     " + "          ".join(["{}_{}_{}_{}".format(lepton_flavor, year, mass_range, bin) for bin in bins for _ in processes]) + "\n")
        file.write("process                 " + "          ".join(processes * len(bins)) + "\n")
        file.write("process                 " + "          ".join([str(i-1) for i in range(len(processes))]) * len(bins) + "\n")
        file.write("rate                    " + "          ".join(["-1"] * len(processes) * len(bins)) + "\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")

        # Systematics
        
        electron_systematics = [
            "lumi_corr_161718    lnN     " + "1.02    " * (len(processes) * len(bins)),
            "lumi_corr_1718      lnN     " + "1.002   " * (len(processes) * len(bins)),
            "lumi_uncorr_18      lnN     " + "1.015   " * (len(processes) * len(bins)),
            "lumi_corr_161718    lnN     " + "1.02    " * (len(processes) * len(bins)),
            "lumi_corr_1718      lnN     " + "1.002   " * (len(processes) * len(bins)),
            "lumi_uncorr_18      lnN     " + "1.015   " * (len(processes) * len(bins)),
            "lumi_uncorr_17      lnN     " + "-" * (len(processes) * len(bins)),
            "lumi_uncorr_16      lnN     " + "-" * (len(processes) * len(bins)),
            "lumi                lnN     " + "1.016   " * (len(processes) * len(bins)),
            "pu                  shape   " + "1       " * (len(processes) * len(bins)),
            "prefiringWeight     shape   " + "1       " * (len(processes) * len(bins)),
            "electronID          shape   " + "1       " * (len(processes) * len(bins)),
            "electronTrigger     shape   " + "1       " * (len(processes) * len(bins)),
            "electronReco        shape   " + "1       " * (len(processes) * len(bins)),
            "isr                 shape   " + "1       " * (len(processes) * len(bins)),
            "fsr                 shape   " + "1       " * (len(processes) * len(bins)),
            "btagCferr1          shape   " + "1       " * (len(processes) * len(bins)),
            "btagCferr2          shape   " + "1       " * (len(processes) * len(bins)),
            "btagHf              shape   " + "1       " * (len(processes) * len(bins)),
            "btagHfstats1        shape   " + "1       " * (len(processes) * len(bins)),
            "btagHfstats2        shape   " + "1       " * (len(processes) * len(bins)),
            "btagLf              shape   " + "1       " * (len(processes) * len(bins)),
            "btagLfstats1        shape   " + "1       " * (len(processes) * len(bins)),
            "btagLfstats2        shape   " + "1       " * (len(processes) * len(bins)),
            "ttagCorr            shape   " + "1       " * (len(processes) * len(bins)),
            "ttagUncorr          shape   " + "1       " * (len(processes) * len(bins)),
            "tmistag             shape   " + "1       " * (len(processes) * len(bins)),
            "murmuf              shape   " + "1       " * (len(processes) * len(bins)),
            "pdf                 shape   " + "1       " * (len(processes) * len(bins)),
            "jer                 shape   " + "1       " * (len(processes) * len(bins)),
            "jec                 shape   " + "1       " * (len(processes) * len(bins)),
            "TTbar_norm          lnN     " + "1.05       1.05       -          -          1.05       1.05       -          -          1.05       1.05       -          -",
            "ST_norm             lnN     " + "-          -          1.3        -          -          -          1.3        -          -          -          1.3        -",
            "Others_norm         lnN     " + "-          -          -          1.3        -          -          -          1.3        -          -          -          1.3",
        ] 

        muon_systematics = [
            "lumi_corr_161718    lnN     " + "1.02    " * (len(processes) * len(bins)),
            "lumi_corr_1718      lnN     " + "1.002   " * (len(processes) * len(bins)),
            "lumi_uncorr_18      lnN     " + "1.015   " * (len(processes) * len(bins)),
            "lumi_corr_161718    lnN     " + "1.02    " * (len(processes) * len(bins)),
            "lumi_corr_1718      lnN     " + "1.002   " * (len(processes) * len(bins)),
            "lumi_uncorr_18      lnN     " + "1.015   " * (len(processes) * len(bins)),
            "lumi_uncorr_17      lnN     " + "-" * (len(processes) * len(bins)),
            "lumi_uncorr_16      lnN     " + "-" * (len(processes) * len(bins)),
            "lumi                lnN     " + "1.016   " * (len(processes) * len(bins)),
            "pu                  shape   " + "1       " * (len(processes) * len(bins)),
            "prefiringWeight     shape   " + "1       " * (len(processes) * len(bins)),
            "muonID              shape   " + "1       " * (len(processes) * len(bins)),
            "muonIso             shape   " + "1       " * (len(processes) * len(bins)),
            "muonTrigger         shape   " + "1       " * (len(processes) * len(bins)),
            "isr                 shape   " + "1       " * (len(processes) * len(bins)),
            "fsr                 shape   " + "1       " * (len(processes) * len(bins)),
            "btagCferr1          shape   " + "1       " * (len(processes) * len(bins)),
            "btagCferr2          shape   " + "1       " * (len(processes) * len(bins)),
            "btagHf              shape   " + "1       " * (len(processes) * len(bins)),
            "btagHfstats1        shape   " + "1       " * (len(processes) * len(bins)),
            "btagHfstats2        shape   " + "1       " * (len(processes) * len(bins)),
            "btagLf              shape   " + "1       " * (len(processes) * len(bins)),
            "btagLfstats1        shape   " + "1       " * (len(processes) * len(bins)),
            "btagLfstats2        shape   " + "1       " * (len(processes) * len(bins)),
            "ttagCorr            shape   " + "1       " * (len(processes) * len(bins)),
            "ttagUncorr          shape   " + "1       " * (len(processes) * len(bins)),
            "tmistag             shape   " + "1       " * (len(processes) * len(bins)),
            "murmuf              shape   " + "1       " * (len(processes) * len(bins)),
            "pdf                 shape   " + "1       " * (len(processes) * len(bins)),
            "jer                 shape   " + "1       " * (len(processes) * len(bins)),
            "jec                 shape   " + "1       " * (len(processes) * len(bins)),
            "TTbar_norm          lnN     " + "1.05       1.05       -          -          1.05       1.05       -          -          1.05       1.05       -          -",
            "ST_norm             lnN     " + "-          -          1.3        -          -          -          1.3        -          -          -          1.3        -",
            "Others_norm         lnN     " + "-          -          -          1.3        -          -          -          1.3        -          -          -          1.3",
        ] 
        

        systematics = muon_systematics if lepton_flavor == "muon" else electron_systematics
        
        for bin in bins:
            systematics.append("{}_{}_{}_{} autoMCStats 1e06 1 1".format(lepton_flavor, year, mass_range, bin))
        
        for syst in systematics:
            file.write(syst + '\n')

        
        file.close()

# years = ["UL18", "UL17", "preUL16", "postUL16"]
years = ["UL18"]
mass_ranges = ["0_750", "750_1500", "1500Inf"]
# mass_ranges = ["1500Inf"]
lepton_flavors = ["muon"]

for year in years:
    for mass_range in mass_ranges:
        for lepton_flavor in lepton_flavors:
            create_datacard(year, mass_range, lepton_flavor)
