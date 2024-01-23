import ROOT

# file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_combine/nominal/Semileptonic.root")
# file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_combine/nominal/Others.root")
# file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_combine/nominal/WJets.root")
# file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_combine/nominal/ST.root")
# file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_combine/nominal/QCD.root")

# file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_combine/nominal/DY.root")
file = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/muon/workdir_AnalysisDNN_UL18_muon_combine/nominal/Diboson.root")


directory1 = file.Get("DNN_output0_General")
directory2 = file.Get("DNN_output0_TopTag_General")
directory3 = file.Get("DNN_output0_NoTopTag_General")
directory4 = file.Get("DNN_output1_General")
directory5 = file.Get("DNN_output2_General")


sum_event_weights_hist1 = directory1.Get("sum_event_weights")
sum_event_weights_hist2 = directory2.Get("sum_event_weights")
sum_event_weights_hist3 = directory3.Get("sum_event_weights")
sum_event_weights_hist4 = directory4.Get("sum_event_weights")
sum_event_weights_hist5 = directory5.Get("sum_event_weights")

# Get the total sum of event weights
total_weighted_events1 = sum_event_weights_hist1.Integral()
total_weighted_events2 = sum_event_weights_hist2.Integral()
total_weighted_events3 = sum_event_weights_hist3.Integral()
total_weighted_events4 = sum_event_weights_hist4.Integral()
total_weighted_events5 = sum_event_weights_hist5.Integral()


# Print the total weighted number of events
print "Total weighted number of events 1: {}".format(total_weighted_events1)
print "Total weighted number of events 2: {}".format(total_weighted_events2)
print "Total weighted number of events 3: {}".format(total_weighted_events3)
print "Total weighted number of events 4: {}".format(total_weighted_events4)
print "Total weighted number of events 5: {}".format(total_weighted_events5)

# Close the ROOT file
file.Close()


