def create_datacard(year, mass_range, lepton_flavor):
    filename = 'datacard_{}_{}_{}.txt'.format(year, lepton_flavor, mass_range)
    filepath = 'combine_input/dY_{}_{}_{}.root'.format(year, lepton_flavor, mass_range)

    bins = ["SR", "CR1", "CR2"]
    processes = ["TTbar_1", "TTbar_2", "WJets", "QCD", "DY", "Diboson", "ST"]
    num_processes = len(processes) - 1  # jmax is number of processes minus 1
    rates = ["-1"] * len(processes)
    
    with open(filename, 'w') as file:
        file.write("imax {} number of bins\n".format(len(bins)))
        file.write("jmax {} number of processes minus 1\n".format(len(processes) - 1))
        file.write("kmax * number of nuisance parameters\n")
        file.write("-" * 150 + "\n")
        file.write("shapes data_obs     *       {} $PROCESS\n".format(filepath))
        file.write("shapes *            *       {} $PROCESS $PROCESS_$SYSTEMATIC\n".format(filepath))
        file.write("-" * 150 + "\n")
        
        # Alignment calculations
        bin_names = ["{}_{}_{}_{}".format(lepton_flavor, year, mass_range, bin) for bin in bins]
        max_bin_length = max(len(name) for name in bin_names) + 1
        max_process_name_length = max(len(proc) for proc in processes) + 1

        file.write("bin          " + " ".join(name.ljust(max_bin_length) for name in bin_names) + "\n")
        file.write("observation  " + " ".join("-1".ljust(max_bin_length) for _ in bin_names) + "\n")
        file.write("-" * 150 + "\n")

        file.write("bin         " + " ".join(name.ljust(max_bin_length) for name in bin_names for _ in processes) + "\n")
        file.write("process     " + " ".join(proc.ljust(max_process_name_length) for _ in bin_names for proc in processes) + "\n")
        file.write("process     " + " ".join(str(i).ljust(max_process_name_length) for i in range(-1, num_processes + 1) for _ in bin_names) + "\n")
        file.write("rate        " + " ".join(str(rate).ljust(max_process_name_length) for _ in bin_names for rate in rates) + "\n")
        file.write("-" * 150 + "\n")

        # file.write("bin          " + "    ".join(["{}_{}_{}_{}".format(lepton_flavor, year, mass_range, bin) for bin in bins]) + "\n")
        # file.write("observation  " + "    ".join(["-1"] * len(bins)) + "\n")
        # file.write("-" * 150 + "\n")
        
        # # Process lines
        # file.write("bin         " + " ".join(["{}_{}_{}_{}".format(lepton_flavor, year, mass_range, bin) for bin in bins for _ in processes]) + "\n")
        # file.write("process     " + " ".join(processes * len(bins)) + "\n")
        # file.write("process     " + " ".join([str(i) for i in range(-1, num_processes + 1)]) * len(bins) + "\n")
        # file.write("rate        " + " ".join(["-1"] * len(processes) * len(bins)) + "\n")
        # file.write("-" * 150 + "\n")
        
        # Systematics
        electron_systematics = [
            "lumi_corr_161718    lnN     1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02     1.02      1.02      1.02      1.02      1.02      1.02      1.02",
            "lumi_corr_1718      lnN     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002    1.002     1.002     1.002     1.002     1.002     1.002     1.002",
            "lumi_uncorr_18      lnN     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015    1.015     1.015     1.015     1.015     1.015     1.015     1.015",
            "lumi_corr_161718    lnN     1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02     1.02      1.02      1.02      1.02      1.02      1.02      1.02",
            "lumi_corr_1718      lnN     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002    1.002     1.002     1.002     1.002     1.002     1.002     1.002",
            "lumi_uncorr_18      lnN     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015    1.015     1.015     1.015     1.015     1.015     1.015     1.015",
            "lumi_uncorr_17      lnN     -         -         -         -         -         -         -         -         -         -         -         -         -         -        -         -         -         -         -         -         - ",            
            "lumi_uncorr_16      lnN     -         -         -         -         -         -         -         -         -         -         -         -         -         -        -         -         -         -         -         -         - ",            
            "lumi                lnN     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016    1.016     1.016     1.016     1.016     1.016     1.016     1.016",
            "pu                  shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "prefiringWeight     shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "electronID          shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "electronTrigger     shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "electronReco        shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "isr                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "fsr                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "btagCferr1          shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagCferr2          shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagHf              shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagHfstats1        shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagHfstats2        shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagLf              shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagLfstats1        shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagLfstats2        shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "ttagCorr            shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "ttagUncorr          shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "tmistag             shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "murmuf              shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "pdf                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "jer                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "jec                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "TTbar_norm          lnN     1.05      1.05      -         -         -         -         -         1.05      1.05      -         -         -         -         -        1.05      1.05      -         -         -         -         -",
            "Wjets_norm          lnN     -         -         1.3       -         -         -         -         -         -         1.3       -         -         -         -        -         -         1.3       -         -         -         -",
            "QCD_norm            lnN     -         -         -         1.5       -         -         -         -         -         -         1.5       -         -         -        -         -         -         1.5       -         -         -",
            "DY_norm             lnN     -         -         -         -         1.3       -         -         -         -         -         -         1.3       -         -        -         -         -         -         1.3       -         -",
            "Diboson_norm        lnN     -         -         -         -         -         1.3       -         -         -         -         -         -         1.3       -        -         -         -         -         -         1.3       -",
            "ST_norm             lnN     -         -         -         -         -         -         1.3       -         -         -         -         -         -         1.3      -         -         -         -         -         -         1.3",
            
        ]
        
        muon_systematics = [
            "lumi_corr_161718    lnN     1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02     1.02      1.02      1.02      1.02      1.02      1.02      1.02",
            "lumi_corr_1718      lnN     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002    1.002     1.002     1.002     1.002     1.002     1.002     1.002",
            "lumi_uncorr_18      lnN     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015    1.015     1.015     1.015     1.015     1.015     1.015     1.015",
            "lumi_corr_161718    lnN     1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02      1.02     1.02      1.02      1.02      1.02      1.02      1.02      1.02",
            "lumi_corr_1718      lnN     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002     1.002    1.002     1.002     1.002     1.002     1.002     1.002     1.002",
            "lumi_uncorr_18      lnN     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015     1.015    1.015     1.015     1.015     1.015     1.015     1.015     1.015",
            "lumi_uncorr_17      lnN     -         -         -         -         -         -         -         -         -         -         -         -         -         -        -         -         -         -         -         -         - ",            
            "lumi_uncorr_16      lnN     -         -         -         -         -         -         -         -         -         -         -         -         -         -        -         -         -         -         -         -         - ",            
            "lumi                lnN     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016     1.016    1.016     1.016     1.016     1.016     1.016     1.016     1.016",
            "pu                  shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "prefiringWeight     shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "muonID              shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "muonIso             shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "muonTrigger         shape   1         1         1         1         1         1         1         1         1         1         1         1         1         1        1         1         1         1         1         1         1",
            "isr                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "fsr                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "btagCferr1          shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagCferr2          shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagHf              shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagHfstats1        shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagHfstats2        shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagLf              shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagLfstats1        shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "btagLfstats2        shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "ttagCorr            shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "ttagUncorr          shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "tmistag             shape   1         1         1         1         1         -         1         1         1         1         1         1         -         1        1         1         1         1         1         -         1",
            "murmuf              shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "pdf                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "jer                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "jec                 shape   1         1         -         -         -         -         -         1         1         -         -         -         -         -        1         1         -         -         -         -         -",
            "TTbar_norm          lnN     1.05      1.05      -         -         -         -         -         1.05      1.05      -         -         -         -         -        1.05      1.05      -         -         -         -         -",
            "Wjets_norm          lnN     -         -         1.3       -         -         -         -         -         -         1.3       -         -         -         -        -         -         1.3       -         -         -         -",
            "QCD_norm            lnN     -         -         -         1.5       -         -         -         -         -         -         1.5       -         -         -        -         -         -         1.5       -         -         -",
            "DY_norm             lnN     -         -         -         -         1.3       -         -         -         -         -         -         1.3       -         -        -         -         -         -         1.3       -         -",
            "Diboson_norm        lnN     -         -         -         -         -         1.3       -         -         -         -         -         -         1.3       -        -         -         -         -         -         1.3       -",
            "ST_norm             lnN     -         -         -         -         -         -         1.3       -         -         -         -         -         -         1.3      -         -         -         -         -         -         1.3",
            
        ]

        systematics = muon_systematics if lepton_flavor == "muon" else electron_systematics
        
        for bin in bins:
            systematics.append("{}_{}_{}_{} autoMCStats 1e06 1 1".format(lepton_flavor, year, mass_range, bin))

        # Repeat systematics for each bin
        for bin in bins:
            for syst in systematics:
                file.write(syst + "\n")

        file.close()

# years = ["UL18", "UL17", "preUL16", "postUL16"]
years = ["UL18"]
# mass_ranges = ["0_500", "500_750", "750_1000", "1000_1500", "1500Inf"]
mass_ranges = ["750_1000"]
lepton_flavors = ["muon"]

for year in years:
    for mass_range in mass_ranges:
        for lepton_flavor in lepton_flavors:
            create_datacard(year, mass_range, lepton_flavor)
