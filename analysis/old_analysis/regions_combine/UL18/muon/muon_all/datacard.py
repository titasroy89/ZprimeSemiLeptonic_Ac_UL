def create_datacard(year, mass_range, lepton_flavor):
    filename = 'datacard_{}_{}_{}.txt'.format(year, lepton_flavor, mass_range)
    filepath = '/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/regions_combine/UL18/muon/{}/combine_input/dY_{}_{}_{}.root'.format(mass_range, year, lepton_flavor, mass_range)
    bins = ["SR", "CR1", "CR2"]
    processes = ["TTbar_1", "TTbar_2", "W_DYJets", "ST", "Others"]
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
        file.write("bin                     {}_{}_{}_{}          {}_{}_{}_{}           {}_{}_{}_{}           {}_{}_{}_{}          {}_{}_{}_{}           {}_{}_{}_{}          {}_{}_{}_{}           {}_{}_{}_{}          {}_{}_{}_{}           {}_{}_{}_{}          {}_{}_{}_{}           {}_{}_{}_{}          {}_{}_{}_{}           {}_{}_{}_{}          {}_{}_{}_{}\n".format(lepton_flavor, year, mass_range, "SR", lepton_flavor, year, mass_range, "SR",lepton_flavor, year, mass_range, "SR",lepton_flavor, year, mass_range, "SR",lepton_flavor, year, mass_range, "SR",lepton_flavor, year, mass_range, "CR1", lepton_flavor, year, mass_range, "CR1",lepton_flavor, year, mass_range, "CR1",lepton_flavor, year, mass_range, "CR1",lepton_flavor, year, mass_range, "CR1", lepton_flavor, year, mass_range, "CR2",lepton_flavor, year, mass_range, "CR2",lepton_flavor, year, mass_range, "CR2",lepton_flavor, year, mass_range, "CR2",lepton_flavor, year, mass_range, "CR2"))
        file.write("process                 TTbar_1                        TTbar_2                         W_DYJets                        ST                             Others                          TTbar_1                         TTbar_2                          W_DYJets                        ST                               Others                          TTbar_1                          TTbar_2                         W_DYJets                         ST                              Others\n")
        file.write("process                 -1                             0                               1                               2                              3                               -1                              0                                1                               2                                3                               -1                               0                               1                                2                               3\n")
        file.write("rate                    -1                             -1                              -1                              -1                             -1                              -1                              -1                               -1                              -1                               -1                              -1                               -1                              -1                               -1                              -1\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")

        # Systematics
        
        electron_systematics = [
            "lumi_corr_161718    lnN     " + "1.02       " * 15,
            "lumi_corr_1718      lnN     " + "1.002      " * 15,
            "lumi_uncorr_18      lnN     " + "1.015      " * 15,
            "lumi_corr_161718    lnN     " + "1.02       " * 15,
            "lumi_corr_1718      lnN     " + "1.002      " * 15,
            "lumi_uncorr_18      lnN     " + "1.015      " * 15,
            "lumi_uncorr_17      lnN     " + "-          " * 15,
            "lumi_uncorr_16      lnN     " + "-          " * 15,
            "lumi                lnN     " + "1.016      " * 15,
            "pu                  shape   " + "1          " * 15,
            "prefiringWeight     shape   " + "1          " * 15,
            "electronID          shape   " + "1          " * 15,
            "electronTrigger     shape   " + "1          " * 15,
            "electronReco        shape   " + "1          " * 15,
            "isr                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "fsr                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "btagCferr1          shape   " + "1          " * 15,
            "btagCferr2          shape   " + "1          " * 15,
            "btagHf              shape   " + "1          " * 15,
            "btagHfstats1        shape   " + "1          " * 15,
            "btagHfstats2        shape   " + "1          " * 15,
            "btagLf              shape   " + "1          " * 15,
            "btagLfstats1        shape   " + "1          " * 15,
            "btagLfstats2        shape   " + "1          " * 15,
            "ttagCorr            shape   " + "1          " * 15,
            "ttagUncorr          shape   " + "1          " * 15,
            "tmistag             shape   " + "1          " * 15,
            "murmuf              shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "pdf                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "jer                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "jec                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "TTbar_norm          lnN     " + "1.05       1.05       -          -          -          1.05       1.05       -          -          -          1.05       1.05       -          -          -",
            "W_DYJets_norm       lnN     " + "-          -          1.3        -          -          -          -          1.3        -          -          -          -          1.3        -          -",
            "ST_norm             lnN     " + "-          -          -          1.3        -          -          -          -          1.3        -          -          -          -          1.3        -",
            "Others_norm         lnN     " + "-          -          -          -          1.3        -          -          -          -          1.3        -          -          -          -          1.3",
        ] 

        muon_systematics = [
            "lumi_corr_161718    lnN     " + "1.02       " * 15,
            "lumi_corr_1718      lnN     " + "1.002      " * 15,
            "lumi_uncorr_18      lnN     " + "1.015      " * 15,
            "lumi_corr_161718    lnN     " + "1.02       " * 15,
            "lumi_corr_1718      lnN     " + "1.002      " * 15,
            "lumi_uncorr_18      lnN     " + "1.015      " * 15,
            "lumi_uncorr_17      lnN     " + "-          " * 15,
            "lumi_uncorr_16      lnN     " + "-          " * 15,
            "lumi                lnN     " + "1.016      " * 15,
            "pu                  shape   " + "1          " * 15,
            "prefiringWeight     shape   " + "1          " * 15,
            "muonID              shape   " + "1          " * 15,
            "muonIso             shape   " + "1          " * 15,
            "muonTrigger         shape   " + "1          " * 15,
            "isr                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "fsr                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "btagCferr1          shape   " + "1          " * 15,
            "btagCferr2          shape   " + "1          " * 15,
            "btagHf              shape   " + "1          " * 15,
            "btagHfstats1        shape   " + "1          " * 15,
            "btagHfstats2        shape   " + "1          " * 15,
            "btagLf              shape   " + "1          " * 15,
            "btagLfstats1        shape   " + "1          " * 15,
            "btagLfstats2        shape   " + "1          " * 15,
            "ttagCorr            shape   " + "1          " * 15,
            "ttagUncorr          shape   " + "1          " * 15,
            "tmistag             shape   " + "1          " * 15,
            "murmuf              shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "pdf                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "jer                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "jec                 shape   " + "1          1          -          -          -          1          1          -          -          -          1          1          -          -          -",
            "TTbar_norm          lnN     " + "1.05       1.05       -          -          -          1.05       1.05       -          -          -          1.05       1.05       -          -          -",
            "W_DYJets_norm       lnN     " + "-          -          1.3        -          -          -          -          1.3        -          -          -          -          1.3        -          -",
            "ST_norm             lnN     " + "-          -          -          1.3        -          -          -          -          1.3        -          -          -          -          1.3        -",
            "Others_norm         lnN     " + "-          -          -          -          1.3        -          -          -          -          1.3        -          -          -          -          1.3",
        ] 
        

        systematics = muon_systematics if lepton_flavor == "muon" else electron_systematics
        
        for bin in bins:
            systematics.append("{}_{}_{}_{} autoMCStats 1e06 1 1".format(lepton_flavor, year, mass_range, bin))
        
        for syst in systematics:
            file.write(syst + '\n')

        
        file.close()

# years = ["UL18", "UL17", "preUL16", "postUL16"]
years = ["UL18"]
mass_ranges = ["0_500", "500_750", "750_1000", "1000_1500", "1500Inf"]
# mass_ranges = ["1500Inf"]
lepton_flavors = ["muon"]

for year in years:
    for mass_range in mass_ranges:
        for lepton_flavor in lepton_flavors:
            create_datacard(year, mass_range, lepton_flavor)
