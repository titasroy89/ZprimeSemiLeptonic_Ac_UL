import os

template = """imax 1 number of bins
jmax 3 number of processes minus 1
kmax * number of nuisance parameters
----------------------------------------------------------------------------------------------------------------------------------
shapes data_obs     {lepton}_{year}_{mass_range}_SR      /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/newmatching/UL16postVFP/combine_input/individual_files/dY_{year}_{lepton}_{mass_range}_SR.root data_obs
shapes *            {lepton}_{year}_{mass_range}_SR      /nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/newmatching/UL16postVFP/combine_input/individual_files/dY_{year}_{lepton}_{mass_range}_SR.root $PROCESS $PROCESS_$SYSTEMATIC
----------------------------------------------------------------------------------------------------------------------------------
bin                     {lepton}_{year}_{mass_range}_SR
observation             -1
----------------------------------------------------------------------------------------------------------------------------------
bin                     {lepton}_{year}_{mass_range}_SR  {lepton}_{year}_{mass_range}_SR  {lepton}_{year}_{mass_range}_SR  {lepton}_{year}_{mass_range}_SR
process                 TTbar_1                           TTbar_2                           ST                              Others
process                 -1                                0                                 1                               2
rate                    -1                                -1                                -1                              -1
----------------------------------------------------------------------------------------------------------------------------------
lumi_corr_161718    lnN     1.02       1.02       1.02       1.02
lumi_corr_1718      lnN     1.002      1.002      1.002      1.002
lumi_uncorr_16      lnN     1.01       1.01       1.01       1.01 
lumi                lnN     1.016      1.016      1.016      1.016
pu                  shape   1          1          1          1
prefiringWeight     shape   1          1          1          1
{leptonID}               shape   1          1          1          1
{leptonRecoIso}             shape   1          1          1          1
{leptonTrigger}          shape   1          1          1          1
isr                 shape   1          1          -          -
fsr                 shape   1          1          -          -
btagCferr1          shape   1          1          1          1
btagCferr2          shape   1          1          1          1
btagHf              shape   1          1          1          1
btagHfstats1        shape   1          1          1          1
btagHfstats2        shape   1          1          1          1
btagLf              shape   1          1          1          1
btagLfstats1        shape   1          1          1          1
btagLfstats2        shape   1          1          1          1
ttagCorr            shape   1          1          1          1
ttagUncorr          shape   1          1          1          1
tmistag             shape   1          1          1          1
murmuf              shape   1          1          -          -
pdf                 shape   1          1          -          -
jer                 shape   1          1          -          -
jec                 shape   1          1          -          -
TTbar_norm          lnN     1.05       1.05       -          -
ST_norm             lnN     -          -          1.2        -
Others_norm         lnN     -          -          -          1.2
{lepton}_{year}_{mass_range}_SR autoMCStats 1e06 1 1
"""

leptons = ["muon", "ele"]
mass_ranges = ["0_500", "500_750", "750_1000", "1000_1500", "1500_Inf"]
year = "UL16postVFP"

systematics = {
    "muon": {
        "leptonID": "muonID",
        "leptonRecoIso": "muonIso",
        "leptonTrigger": "muonTrigger"
    },
    "ele": {
        "leptonID": "eleID",
        "leptonRecoIso": "eleReco",
        "leptonTrigger": "eleTrigger"
    }
}

for lepton in leptons:
    for mass_range in mass_ranges:
        datacard_content = template.format(
            lepton=lepton,
            year=year,
            mass_range=mass_range,
            leptonID=systematics[lepton]["leptonID"],
            leptonRecoIso=systematics[lepton]["leptonRecoIso"],
            leptonTrigger=systematics[lepton]["leptonTrigger"]
        )
        filename = "datacard_{}_{}_{}_SR.txt".format(lepton, year, mass_range)
        with open(filename, "w") as file:
            file.write(datacard_content)
        print("Datacard created: {}".format(filename))
