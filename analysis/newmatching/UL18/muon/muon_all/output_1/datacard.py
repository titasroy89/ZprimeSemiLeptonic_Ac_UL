def create_datacard(year, mass_range, lepton_flavor):
    filename = 'datacard_{}_{}_{}.txt'.format(year, lepton_flavor, mass_range)
    filepath = 'combine_input/dY_{}_{}_{}.root'.format(year, lepton_flavor, mass_range)
    channels = ["SR", "CR1", "CR2"]
    processes = ["TTbar_1                 ", "TTbar_2                  ", "ST                  ", "Others                   "]
    num_processes = len(processes) - 1  # jmax is number of processes minus 1
    
    with open(filename, 'w') as file:
        file.write("imax {} number of bins\n".format(len(channels)))
        file.write("jmax {} number of processes minus 1\n".format(num_processes))
        file.write("kmax * number of nuisance parameters\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        
        for channel in channels:
            file.write("shapes data_obs     {}_{}_{}_{}      {}/{}_{}_{}_{}.root {}/data_obs\n".format(lepton_flavor, year, mass_range, channel, filepath, lepton_flavor, year, mass_range, channel, channel))
            file.write("shapes *            {}_{}_{}_{}      {}/{}_{}_{}_{}.root {}/$PROCESS {}/$PROCESS_$SYSTEMATIC\n".format(lepton_flavor, year, mass_range, channel, filepath, lepton_flavor, year, mass_range, channel, channel, channel))
        
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        
        # Bin and observation section
        file.write("bin                     {0}_{1}_{2}_SR          {0}_{1}_{2}_CR1           {0}_{1}_{2}_CR2\n".format(lepton_flavor, year, mass_range))
        file.write("observation             -1                            -1                              -1\n")
                
        # Processes and rates
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("bin                     muon_UL18_{0}_SR          muon_UL18_{0}_SR          muon_UL18_{0}_SR          muon_UL18_{0}_SR          muon_UL18_{0}_CR1          muon_UL18_{0}_CR1          muon_UL18_{0}_CR1          muon_UL18_{0}_CR1          muon_UL18_{0}_CR2          muon_UL18_{0}_CR2          muon_UL18_{0}_CR2          muon_UL18_{0}_CR2\n".format(mass_range))
        file.write("process                 TTbar_1                     TTbar_2                     ST                          Others                      TTbar_1                      TTbar_2                      ST                           Others                       TTbar_1                      TTbar_2                      ST                           Others\n")
        file.write("process                 -1                          0                           1                           2                           -1                           0                            1                            2                            -1                           0                            1                            2\n")
        file.write("rate                    -1                          -1                          -1                          -1                          -1                           -1                           -1                           -1                           -1                           -1                           -1                           -1\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")

        # Systematics
        
        electron_systematics = [
            "lumi_corr_161718    lnN     " + "1.02       " * 12,
            "lumi_corr_1718      lnN     " + "1.002      " * 12,
            "lumi_uncorr_18      lnN     " + "1.015      " * 12,
            "lumi_corr_161718    lnN     " + "1.02       " * 12,
            "lumi_corr_1718      lnN     " + "1.002      " * 12,
            "lumi_uncorr_18      lnN     " + "1.015      " * 12,
            "lumi_uncorr_17      lnN     " + "-          " * 12,
            "lumi_uncorr_16      lnN     " + "-          " * 12,
            "lumi                lnN     " + "1.016      " * 12,
            "pu                  shape   " + "1          " * 12,
            "prefiringWeight     shape   " + "1          " * 12,
            "electronID          shape   " + "1          " * 12,
            "electronTrigger     shape   " + "1          " * 12,
            "electronReco        shape   " + "1          " * 12,
            "isr                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "fsr                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "btagCferr1          shape   " + "1          " * 12,
            "btagCferr2          shape   " + "1          " * 12,
            "btagHf              shape   " + "1          " * 12,
            "btagHfstats1        shape   " + "1          " * 12,
            "btagHfstats2        shape   " + "1          " * 12,
            "btagLf              shape   " + "1          " * 12,
            "btagLfstats1        shape   " + "1          " * 12,
            "btagLfstats2        shape   " + "1          " * 12,
            "ttagCorr            shape   " + "1          " * 12,
            "ttagUncorr          shape   " + "1          " * 12,
            "tmistag             shape   " + "1          " * 12,
            "upup                shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "upnone              shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "noneup              shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "downdown            shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "downnone            shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "nonedown            shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "pdf                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "jer                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "jec                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "TTbar_norm          lnN     " + "1.05       1.05       -          -          1.05       1.05       -          -          1.05       1.05       -          -          ",
            "ST_norm             lnN     " + "-          -          1.3        -          -          -          1.3        -          -          -          1.3        -          ",
            "Others_norm         lnN     " + "-          -          -          1.3        -          -          -          1.3        -          -          -          1.3        ",
        ] 

        muon_systematics = [
            "lumi_corr_161718    lnN     " + "1.02       " * 12,
            "lumi_corr_1718      lnN     " + "1.002      " * 12,
            "lumi_uncorr_18      lnN     " + "1.015      " * 12,
            "lumi_corr_161718    lnN     " + "1.02       " * 12,
            "lumi_corr_1718      lnN     " + "1.002      " * 12,
            "lumi_uncorr_18      lnN     " + "1.015      " * 12,
            "lumi_uncorr_17      lnN     " + "-          " * 12,
            "lumi_uncorr_16      lnN     " + "-          " * 12,
            "lumi                lnN     " + "1.016      " * 12,
            "pu                  shape   " + "1          " * 12,
            "prefiringWeight     shape   " + "1          " * 12,
            "muonID              shape   " + "1          " * 12,
            "muonIso             shape   " + "1          " * 12,
            "muonTrigger         shape   " + "1          " * 12,
            "isr                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "fsr                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "btagCferr1          shape   " + "1          " * 12,
            "btagCferr2          shape   " + "1          " * 12,
            "btagHf              shape   " + "1          " * 12,
            "btagHfstats1        shape   " + "1          " * 12,
            "btagHfstats2        shape   " + "1          " * 12,
            "btagLf              shape   " + "1          " * 12,
            "btagLfstats1        shape   " + "1          " * 12,
            "btagLfstats2        shape   " + "1          " * 12,
            "ttagCorr            shape   " + "1          " * 12,
            "ttagUncorr          shape   " + "1          " * 12,
            "tmistag             shape   " + "1          " * 12,
            "upup                shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "upnone              shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "noneup              shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "downdown            shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "downnone            shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "nonedown            shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "pdf                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "jer                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "jec                 shape   " + "1          1          -          -          1          1          -          -          1          1          -          -          ",
            "TTbar_norm          lnN     " + "1.05       1.05       -          -          1.05       1.05       -          -          1.05       1.05       -          -          ",
            "ST_norm             lnN     " + "-          -          1.3        -          -          -          1.3        -          -          -          1.3        -          ",
            "Others_norm         lnN     " + "-          -          -          1.3        -          -          -          1.3        -          -          -          1.3        ",
        ] 
        

        systematics = muon_systematics if lepton_flavor == "muon" else electron_systematics
        
        for bin in channels:
            systematics.append("{}_{}_{}_{} autoMCStats 1e06 1 1".format(lepton_flavor, year, mass_range, bin))
        
        for syst in systematics:
            file.write(syst + '\n')

        
        file.close()

# years = ["UL18", "UL17", "preUL16", "postUL16"]
years = ["UL18"]
mass_ranges = ["0_500", "500_750", "750_1000", "1000_1500", "1500Inf"]
# mass_ranges = ["1000_1500"]
lepton_flavors = ["muon"]

for year in years:
    for mass_range in mass_ranges:
        for lepton_flavor in lepton_flavors:
            create_datacard(year, mass_range, lepton_flavor)
