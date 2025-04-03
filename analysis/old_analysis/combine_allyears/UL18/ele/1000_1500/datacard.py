def create_datacard(year, mass_range, lepton_flavor):
    filename = 'datacard_{}_{}_{}.txt'.format(year, lepton_flavor, mass_range)
    filepath = 'combine_input/dY_{}_{}_{}.root'.format(year, lepton_flavor, mass_range)
    
    with open(filename, 'w') as file:
        file.write("imax 1 number of bins\n")
        file.write("jmax 6 number of processes minus 1\n")
        file.write("kmax * number of nuisance parameters\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("shapes data_obs     {}_{}_{}       {} $PROCESS\n".format(lepton_flavor, year, mass_range, filepath))
        file.write("shapes *            *       {} $PROCESS $PROCESS_$SYSTEMATIC\n".format(filepath))
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("bin          {}_{}_{}\n".format(lepton_flavor, year, mass_range))
        file.write("observation  -1\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("bin                     {}_{}_{}     {}_{}_{}     {}_{}_{}     {}_{}_{}     {}_{}_{}     {}_{}_{}     {}_{}_{}\n".format(lepton_flavor, year, mass_range, lepton_flavor, year, mass_range, lepton_flavor, year, mass_range, lepton_flavor, year, mass_range, lepton_flavor, year, mass_range, lepton_flavor, year, mass_range, lepton_flavor, year, mass_range))
        file.write("process                 TTbar_1               TTbar_2               WJets                 QCD                   DY                    Diboson               ST\n")
        file.write("process                 -1                    0                     1                     2                     3                     4                     5\n")
        file.write("rate                    -1                    -1                    -1                    -1                    -1                    -1                    -1\n")
        file.write("----------------------------------------------------------------------------------------------------------------------------------\n")
        
        # Systematics
        electron_systematics = [
            "lumi_corr_161718    lnN     1.02      1.02      1.02      1.02      1.02      1.02      1.02",
            "lumi_corr_1718      lnN     1.002     1.002     1.002     1.002     1.002     1.002     1.002",
            "lumi_uncorr_18      lnN     1.015     1.015     1.015     1.015     1.015     1.015     1.015",
            "lumi_corr_161718    lnN     1.02      1.02      1.02      1.02      1.02      1.02      1.02",
            "lumi_corr_1718      lnN     1.002     1.002     1.002     1.002     1.002     1.002     1.002",
            "lumi_uncorr_18      lnN     1.015     1.015     1.015     1.015     1.015     1.015     1.015",
            "lumi_uncorr_17      lnN     -         -         -         -         -         -         - ",            
            "lumi_uncorr_16      lnN     -         -         -         -         -         -         - ",
            "lumi                lnN     1.016     1.016     1.016     1.016     1.016     1.016     1.016",
            "pu                  shape   1         1         1         1         1         1         1",
            "prefiringWeight     shape   1         1         1         1         1         1         1",
            "electronID          shape   1         1         1         1         1         1         1",
            "electronTrigger     shape   1         1         1         1         1         1         1",
            "electronReco        shape   1         1         1         1         1         1         1",
            "isr                 shape   1         1         1         1         1         1         1",
            "fsr                 shape   1         1         1         1         1         1         1",
            "btagCferr1          shape   1         1         1         1         1         1         1",
            "btagCferr2          shape   1         1         1         1         1         1         1",
            "btagHf              shape   1         1         1         1         1         1         1",
            "btagHfstats1        shape   1         1         1         1         1         1         1",
            "btagHfstats2        shape   1         1         1         1         1         1         1",
            "btagLf              shape   1         1         1         1         1         1         1",
            "btagLfstats1        shape   1         1         1         1         1         1         1",
            "btagLfstats2        shape   1         1         1         1         1         1         1",
            "ttagCorr            shape   1         1         1         1         1         1         1",
            "ttagUncorr          shape   1         1         1         1         1         1         1",
            "tmistag             shape   1         1         1         1         1         1         1",
            "murmuf              shape   1         1         1         1         1         1         1",
            "pdf                 shape   1         1         1         1         1         -         1",
            "jer                 shape   1         1         1         1         1         1         1",
            "jec                 shape   1         1         1         1         1         1         1",
            "TTbar_norm          lnN     1.05      1.05         -         -         -         -         - ",     
            "Wjets_norm          lnN     -         -         1.3       -         -         -         -",
            "QCD_norm            lnN     -         -         -         1.5       -         -         -",
            "DY_norm             lnN     -         -         -         -         1.3       -         -",
            "Diboson_norm        lnN     -         -         -         -         -         1.3      -",
            "ST_norm             lnN     -         -         -         -         -         -         1.3",
            
            "{}_{}_{} autoMCStats 10000000 1 1".format(lepton_flavor, year, mass_range)
        ]
        
        muon_systematics = [
            "lumi_corr_161718    lnN     1.02      1.02      1.02      1.02      1.02      1.02      1.02",
            "lumi_corr_1718      lnN     1.002     1.002     1.002     1.002     1.002     1.002     1.002",
            "lumi_uncorr_18      lnN     1.015     1.015     1.015     1.015     1.015     1.015     1.015",
            "lumi_corr_161718    lnN     1.02      1.02      1.02      1.02      1.02      1.02      1.02",
            "lumi_corr_1718      lnN     1.002     1.002     1.002     1.002     1.002     1.002     1.002",
            "lumi_uncorr_18      lnN     1.015     1.015     1.015     1.015     1.015     1.015     1.015",
            "lumi_uncorr_17      lnN     -         -         -         -         -         -         - ",            
            "lumi_uncorr_16      lnN     -         -         -         -         -         -         - ",
            "lumi                lnN     1.016     1.016     1.016     1.016     1.016     1.016     1.016",
            "pu                  shape   1         1         1         1         1         1         1",
            "muonReco            shape   1         1         1         1         1         1         1",
            "prefiringWeight     shape   1         1         1         1         1         1         1",
            "muonID              shape   1         1         1         1         1         1         1",
            "muonIso             shape   1         1         1         1         1         1         1",
            "muonTrigger         shape   1         1         1         1         1         1         1",
            "isr                 shape   1         1         1         1         1         1         1",
            "fsr                 shape   1         1         1         1         1         1         1",
            "btagCferr1          shape   1         1         1         1         1         1         1",
            "btagCferr2          shape   1         1         1         1         1         1         1",
            "btagHf              shape   1         1         1         1         1         1         1",
            "btagHfstats1        shape   1         1         1         1         1         1         1",
            "btagHfstats2        shape   1         1         1         1         1         1         1",
            "btagLf              shape   1         1         1         1         1         1         1",
            "btagLfstats1        shape   1         1         1         1         1         1         1",
            "btagLfstats2        shape   1         1         1         1         1         1         1",
            "ttagCorr            shape   1         1         1         1         1         1         1",
            "ttagUncorr          shape   1         1         1         1         1         1         1",
            "tmistag             shape   1         1         1         1         1         1         1",
            "murmuf              shape   1         1         1         1         1         1         1",
            "pdf                 shape   1         1         1         1         1         -         1",
            "jer                 shape   1         1         1         1         1         1         1",
            "jec                 shape   1         1         1         1         1         1         1",
            "TTbar_norm          lnN     1.05      1.05         -         -         -         -         - ",     
            "Wjets_norm          lnN     -         -         1.3       -         -         -         -",
            "QCD_norm            lnN     -         -         -         1.5       -         -         -",
            "DY_norm             lnN     -         -         -         -         1.3       -         -",
            "Diboson_norm        lnN     -         -         -         -         -         1.3      -",
            "ST_norm             lnN     -         -         -         -         -         -         1.3",
            
            "{}_{}_{} autoMCStats 10000000 1 1".format(lepton_flavor, year, mass_range)

        ]

        systematics = muon_systematics if lepton_flavor == "muon" else electron_systematics
        
        for syst in systematics:
            file.write(syst + '\n')

        file.close()

# years = ["UL18", "UL17", "preUL16", "postUL16"]
years = ["UL18"]
# mass_ranges = ["0_500", "500_750", "750_1000", "1000_1500", "1500Inf"]
mass_ranges = ["1000_1500"]
lepton_flavors = ["ele"]

for year in years:
    for mass_range in mass_ranges:
        for lepton_flavor in lepton_flavors:
            create_datacard(year, mass_range, lepton_flavor)
