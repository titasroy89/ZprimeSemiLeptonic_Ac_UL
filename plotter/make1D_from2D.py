from ROOT import TFile, TLegend, TCanvas, TPad, THStack, TF1, TPaveText, TGaxis, SetOwnership, TObject, gStyle,TH1F
from ROOT import *
import os
import math
import sys
from optparse import OptionParser
from sys import argv
from numpy import log10
from array import array
from collections import OrderedDict


import CMS_lumi

from Style import *

thestyle = Style()

HasCMSStyle = False
style = None
if os.path.isfile('tdrstyle.C'):
    ROOT.gROOT.ProcessLine('.L tdrstyle.C')
    ROOT.setTDRStyle()
    #print ("Found tdrstyle.C file, using this style.")
    HasCMSStyle = True
    if os.path.isfile('CMSTopStyle.cc'):
        gROOT.ProcessLine('.L CMSTopStyle.cc+')
        style = CMSTopStyle()
        style.setupICHEPv1()
        #print "Found CMSTopStyle.cc file, use TOP style if requested in xml file."
if not HasCMSStyle:
    #print "Using default style defined in cuy package."
    thestyle.SetStyle()
ROOT.gROOT.ForceStyle()


parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel",default="muon",type='str',
                  help="what channel?")
parser.add_option("-y", "--year", dest="year", default="2018",type='str',
                  help="don't print status messages to stdout")
# parser.add_option("-eft", "--eft", dest="eft", action='store_false',type='str',
#                   help="print eft vars?")

H = 600;
W = 800;


# references for T, B, L, R                                                                                                             
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W

(options, args) = parser.parse_args()
canvas = TCanvas('c1','c1',W,H)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetLeftMargin( L/W )
canvas.SetRightMargin( R/W )
canvas.SetTopMargin( T/H )
canvas.SetBottomMargin( B/H )
canvas.SetTickx(1)

channel = options.channel
year=options.year

if channel=="muon":
	_channelText = "#mu+jets"
elif(channel=="electron"):
	_channelText="e+jets"
CMS_lumi.channelText = _channelText
CMS_lumi.writeChannelText = True
CMS_lumi.writeExtraText = True
period=0
if year=="2018":
	period=6
elif year=="2017":
	period=5
elif "2016" in year:
	period=4
elif "all" in year:
	period=8
histos={}
samples=["TTbar","WJets","QCD","DY"]

for j in range(2,21):
    histos[j]=TH1D("1D_ttbar_%s"%j,"",50,0,7000)


file_ = TFile("/nfs/dust/cms/user/deleokse/RunII_106_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/macros/src/files_BTagSF/customBtagSF_%s_%s.root"%(channel,year),"read")
hist=file_.Get("N_Jets_vs_HT_TTbar")
y=hist.GetYaxis().GetLast()
x=hist.GetXaxis().GetLast()

# for i in range(1,x+1):
for i in range(4,21):
    val=[]
    err=[]
    for r in range(1,y+1):
        j=i-2
        val.append(hist.GetBinContent(i,r))
        err.append(hist.GetBinError(i,r))
        
        histos[j].SetBinContent(r,float(val[r-1]))
        histos[j].SetBinError(r,float(err[r-1]))
    histos[j].SetLineColor(kBlack)
    histos[j].GetXaxis().SetTitle("SF as function of HT for nJet=%s"%j)
    histos[j].Draw()
    CMS_lumi.CMS_lumi(canvas, period, 11)
    canvas.SaveAs("1D_ttbar_%s_%s_%s.pdf"%(channel,year,j))
      

        
