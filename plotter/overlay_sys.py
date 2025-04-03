
import ROOT

file_nominal = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/ele/nominal/TTbar.root")
file_jec_up = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/ele/workdir_AnalysisDNN_UL18_ele_JEC_up_doublecheck/TTbar.root")
file_jec_down = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/ele/workdir_AnalysisDNN_UL18_ele_JEC_down_doublecheck/TTbar.root")
file_jer_up = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/ele/workdir_AnalysisDNN_UL18_ele_JER_up_doublecheck/TTbar.root")
file_jer_down = ROOT.TFile("/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/output_DNN/UL18/ele/workdir_AnalysisDNN_UL18_ele_JER_down_doublecheck/TTbar.root")

hist_nominal = file_nominal.Get("DNN_output0_General/pt_jet1")  
hist_jec_up = file_jec_up.Get("DNN_output0_General/pt_jet1") 
hist_jec_down = file_jec_down.Get("DNN_output0_General/pt_jet1")
hist_jer_up = file_jer_up.Get("DNN_output0_General/pt_jet1")    
hist_jer_down = file_jer_down.Get("DNN_output0_General/pt_jet1") 

canvas_jec = ROOT.TCanvas("canvas_jec", "Leading Jet pT - JEC Systematics", 800, 600)
canvas_jer = ROOT.TCanvas("canvas_jer", "Leading Jet pT - JER Systematics", 800, 600)



# ---------- JEC Plot ----------

hist_nominal.SetLineColor(ROOT.kOrange)
hist_jec_up.SetLineColor(ROOT.kRed)
hist_jec_down.SetLineColor(ROOT.kBlue)

canvas_jec.cd()
hist_nominal.Draw("HIST")      
hist_jec_up.Draw("HIST SAME")   
hist_jec_down.Draw("HIST SAME")

legend_jec = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend_jec.AddEntry(hist_nominal, "Nominal", "l")
legend_jec.AddEntry(hist_jec_up, "JEC Up", "l")
legend_jec.AddEntry(hist_jec_down, "JEC Down", "l")
legend_jec.Draw()

hist_nominal.SetTitle("Leading Jet p_{T} Distribution - JEC Systematics; Leading Jet p_{T} (GeV); Events")
hist_nominal.GetXaxis().SetTitle("Leading Jet p_{T} (GeV)")
hist_nominal.GetYaxis().SetTitle("Events")

canvas_jec.SaveAs("jet_pt_jec_overlay_dnn0_ele_aftermodel.png")


# ---------- JER Plot ----------

hist_nominal.SetLineColor(ROOT.kOrange)
hist_jer_up.SetLineColor(ROOT.kRed)
hist_jer_down.SetLineColor(ROOT.kBlue)

canvas_jer.cd()
hist_nominal.Draw("HIST")      
hist_jer_up.Draw("HIST SAME") 
hist_jer_down.Draw("HIST SAME")

legend_jer = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
legend_jer.AddEntry(hist_nominal, "Nominal", "l")
legend_jer.AddEntry(hist_jer_up, "JER Up", "l")
legend_jer.AddEntry(hist_jer_down, "JER Down", "l")
legend_jer.Draw()

hist_nominal.SetTitle("Leading Jet p_{T} Distribution - JER Systematics; Leading Jet p_{T} (GeV); Events")
hist_nominal.GetXaxis().SetTitle("Leading Jet p_{T} (GeV)")
hist_nominal.GetYaxis().SetTitle("Events")

canvas_jer.SaveAs("jet_pt_jer_overlay_dnn1_ele.png")
