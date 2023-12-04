#! /usr/bin/env python
from ROOT import *
import ROOT
import sys
import numpy

'''
This script pulls the up/down variations of a given systematic uncertainty 
and plots them on the same histogram with the nominal of a given source
'''

# This script only focuses on the hdamp systematic
systematics = {'hdamp'}


## In file name Lo->mass-cut=750-900 and Hi->mass-cut>900

# 2016 electron-channel with mass cut of 750-900 GeV
fin_16eleLo = TFile('DeltaY_2016_electron_750_900.root', 'open')
# 2016 electron-channel with mass cut of <900 GeV
fin_16eleHi = TFile('DeltaY_2016_electron_900.root', 'open')
# 2016 muon-channel with mass cut of 750-900 GeV
fin_16muLo = TFile('DeltaY_2016_muon_750_900.root', 'open')
# 2016 muon-channel with mass cut of <900 GeV
fin_16muHi = TFile('DeltaY_2016_muon_900.root', 'open')

# 2017 electron-channel with mass cut of 750-900 GeV
fin_17eleLo = TFile('DeltaY_electron_2017_750_900.root', 'open')
# 2017 electron-channel with mass cut of <900 GeV
fin_17eleHi = TFile('DeltaY_electron_2017_900.root', 'open')
# 2017 muon-channel with mass cut of 750-900 GeV
fin_17muLo = TFile('DeltaY_muon_2017_750_900.root', 'open')
# 2017 muon-channel with mass cut of <900 GeV
fin_17muHi = TFile('DeltaY_muon_2017_900.root', 'open')

# 2018 electron-channel with mass cut of 750-900 GeV
fin_18eleLo = TFile('DeltaY_electron_750_900_2018.root', 'open')
# 2018 electron-channel with mass cut of <900 GeV
fin_18eleHi = TFile('DeltaY_electron_900_2018.root', 'open')
# 2018 muon-channel with mass cut of 750-900 GeV
fin_18muLo = TFile('DeltaY_muon_750_900_2018.root', 'open')
# 2018 muon-channel with mass cut of <900 GeV
fin_18muHi = TFile('DeltaY_muon_900_2018.root', 'open')


## Create a lists of files and file names so we can loop over them and label the files with sensible names
#input_files = [fin_16eleLo, fin_16eleHi, fin_16muLo, fin_16muHi, fin_17eleLo, fin_17eleHi, fin_17muLo, fin_17muHi, fin_18eleLo, fin_18eleHi, fin_18muLo, fin_18muHi]
input_files = [fin_16eleLo]

#file_names = ['2016 ejets 750<Mtt<900GeV', '2016 ejets Mtt>900', '2016 mujets 750<Mtt<900GeV', '2016 mujets Mtt>900', '2017 ejets 750<Mtt<900GeV', '2017 ejets Mtt>900', '2017 mujets 750<Mtt<900GeV', '2017 mujets Mtt>900', '2018 ejets 750<Mtt<900GeV', '2018 ejets Mtt>900', '2018 mujets 750<Mtt<900GeV', '2018 mujets Mtt>900']
file_names = ['2016 ejets 750<Mtt<900GeV']
zipped_files = zip(input_files, file_names)


# Ttbar_1 is ttbar with a DeltaY < 0 cut
# Ttbar_2 is ttbar with a DeltaY > 0 cut
sample = {'Ttbar_1', 'Ttbar_2'}


# Initializing variables needed later
nominalhist = {}
nominalhistDraw = {}
systvarhist = {}
systvarhistDraw = {}
systvarhistRatio = {}
systvarhistRatioDraw = {}
canvas_Bkg = {}
pad1 = {}
pad2 = {}

hsys = {}
hsystUp = {}
hsystDown = {}
hsysDraw = {}
hsystUpDraw = {}
hsystDownDraw = {}

# Needed for histo aesthetics
padRatio = 0.25
padOverlap = 0.15
padGap = 0.01
H = 600;
W = 800;
T = 0.08*H
B = 0.12*H
L = 0.12*W
R = 0.1*W
gROOT.SetBatch(kTRUE)
gROOT.UseCurrentStyle()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetLegendTextSize(0.05)

# Define histogram generating functions

# Setting canvas and legend
# defining separate legends for Ttbar_1 and Ttbar_2 to avoid overlap with histogram
def set_canvleg1():
    global canvas_Bkg
    canvas_Bkg = TCanvas("SystVariation_"+samp+syst,"SystVariation_"+samp+syst,800,600)
    global legend
    legend = TLegend(.6,.6,.9,.9)

def set_canvleg2():
    global canvas_Bkg
    canvas_Bkg = TCanvas("SystVariation_"+samp+syst,"SystVariation_"+samp+syst,800,600)
    global legend
    legend = TLegend(.15,.6,.45,.9)


# Setting pad for nominal and up/down hisotgrams
def set_pad1():
    global pad1
    pad1 = TPad("pad1", "pad1", 0., 0.4, 1., 1.) #Upper plot will be in pad1
    pad1.SetLeftMargin( L/W )
    pad1.SetRightMargin( R/W )
    pad1.SetTopMargin(T/H/(1-padRatio+padOverlap))
    pad1.SetBottomMargin( (padOverlap+padGap)/(1-padRatio+padOverlap) )
    pad1.SetFillColor(0)
    pad1.SetBorderMode(0)
    pad1.SetFrameFillStyle(0)
    pad1.SetFrameBorderMode(0)
    pad1.SetTickx(0)
    pad1.SetTicky(0)
    pad1.SetBottomMargin(0.01) # Upper and lower plot are not joined
    pad1.SetGridx()
    pad1.Draw()             # Draw the upper pad: pad1
    pad1.cd()

# Drawing up/down/nominal histogarams and setting axes/title/marker
def draw_histos():
    global hsystUpDraw
    hsystUpDraw = hsystUp.DrawClone('e1')
    global a
    a = hsystUpDraw.GetMaximum()
    hsystUpDraw.GetYaxis().SetRangeUser(0,a*1.20)
    #hsystUpDraw.GetXaxis().SetTitle("| #Delta y |")
    hsystUpDraw.GetXaxis().SetLabelSize(0)
    hsystUpDraw.GetYaxis().SetTitle('Events')
    hsystUpDraw.GetYaxis().CenterTitle(True)
    #hsystUpDraw.GetYaxis().SetTitleOffset(1)
    #hsystUpDraw.GetYaxis().SetTitleFont(43)
    hsystUpDraw.GetYaxis().SetTitleSize(0.05)
    hsystUpDraw.SetLineColor(kRed)
    global hsystDownDraw
    hsystDownDraw = hsystDown.DrawClone('e1 same')
    hsystDownDraw.SetLineColor(kBlue)
    global hsystDraw
    hsystDraw = hsyst.DrawClone('ep same')
    hsystDraw.SetMarkerStyle(24)
    hsystDraw.SetMarkerSize(1)
    hsystDraw.SetMarkerColorAlpha(kBlack, 0.45)
    hsystDraw.SetLineColor(kBlack)

#Drawing legend
def draw_legend():
    #customize to gen-cut
    if samp == 'Ttbar_1': 
        legend.AddEntry(hsystDraw, 'nominal (\Delta|y_{gen}|<0)', 'lp')
    if samp == 'Ttbar_2':
        legend.AddEntry(hsystDraw, 'nominal (\Delta|y_{gen}|>0)', 'lp')
    legend.AddEntry(hsystUpDraw, syst+'Up', 'lp')
    legend.AddEntry(hsystDownDraw, syst+'Down', 'lp')
    legend.Draw()

#Create latex object for CMS title info in upper-left of plot
def latexCMStitle():
    latexCMStitle = ROOT.TLatex()
    latexCMStitle.SetTextSize(0.045)
    latexCMStitle.SetTextAlign(11)
    latexCMStitle.DrawLatex(-2, a*1.21,"CMS simulation"+" "+file_name)

#Create latex object for Lumi info in upper-right of plot
#def latex2():
#    latex2 = ROOT.TLatex()
#    latex2.SetTextSize(0.045)
#    latex2.SetTextAlign(11)
#    latex2.DrawLatex(1.1,a*1.21,"138 fb^{-1} (13 TeV)")

#Create latex object for positive Gen-cut label
#def latexPosGenCut():
#    latexPosGenCut = ROOT.TLatex()
#    latexPosGenCut.SetTextSize(0.045)
#    latexPosGenCut.SetTextAlign(11)
#    latexPosGenCut.DrawLatex(-1.2, 9000, "\Delta|y_{gen}|>0")

#Create latex object for negaitive Gen-cut label
#def latexNegGenCut():
#    latexNegGenCut = ROOT.TLatex()
#    latexNegGenCut.SetTextSize(0.045)
#    latexNegGenCut.SetTextAlign(11)
#    latexNegGenCut.DrawLatex(0.8, 9000, "\Delta|y_{gen}|<0")

#Create latex object for Bin Error info
def latexBinErrorInfo():
    latexBineError = ROOT.TLatex()
    latexBineError.SetTextSize(0.068)
    latexBineError.SetTextAlign(11)
    latexBineError.DrawLatex(-0.98, 1.33, 'first and second-bin errors are:')
    latexBineError.DrawLatex(-0.98, 1.25, 'nominal (' + str(hsyst.GetBinError(1)) + ',' + str(hsyst.GetBinError(2)) + ')')
    latexBineError.DrawLatex(-0.98, 1.17, 'up (' + str(hsystUp.GetBinError(1)) + ',' + str(hsystUp.GetBinError(2)) + ')')
    latexBineError.DrawLatex(-0.98, 1.09, 'down (' + str(hsystDown.GetBinError(1)) + ',' + str(hsystDown.GetBinError(2)) + ')')
    latexBineError.DrawLatex(-0.98, 1.01, 'ratioUp (' + str(systvarhistRatio[samp+syst+'__plus__ratio'].GetBinError(1)) + ',' + str(systvarhistRatio[samp+syst+'__plus__ratio'].GetBinError(2)) + ')')
    latexBineError.DrawLatex(-0.98, 0.93, 'ratioDown (' + str(systvarhistRatio[samp+syst+'__minus__ratio'].GetBinError(1)) + ',' + str(systvarhistRatio[samp+syst+'__minus__ratio'].GetBinError(2)) + ')')

#Creating 2nd pad
def set_pad2():
    canvas_Bkg.cd()          # Go back to the main canvas before defining pad2
    global pad2
    pad2 = TPad("pad2", "pad2", 0, 0.01, 1, 0.4)
#pad2 = TPad("pad2", "pad2", 0., 0., 1., 0.29)
#pad2 = TPad("qwe_p2","qwe_p2",0,0,1,padRatio+padOverlap)
    pad2.SetLeftMargin( L/W )
    pad2.SetRightMargin( R/W )
    pad2.SetTopMargin(0)
#pad2.SetTopMargin( (padOverlap)/(padRatio+padOverlap) )
    pad2.SetBottomMargin( B/H/(padRatio+padOverlap) )
    pad2.SetFillColor(0)
    pad2.SetFillStyle(4000)
    pad2.SetBorderMode(0)
    pad2.SetFrameFillStyle(0)
    pad2.SetFrameBorderMode(0)
    pad2.SetTickx(0)
    pad2.SetTicky(0)
    pad2.SetGridx() # vertical grid
    pad2.Draw()
    pad2.cd()      # pad2 becomes the current pad

# Draw Variation/Nominal histogram
def draw_ratiohisto(): 
    systvarhistRatio[samp+syst+'__plus__ratio'] = hsystUpDraw.Clone(samp+syst+'Up_Ratio')
    print "up sys val:",systvarhistRatio[samp+syst+'__plus__ratio'].GetBinContent(1)
    print "up sys val error:",systvarhistRatio[samp+syst+'__plus__ratio'].GetBinError(1)
    print "nominal sys val:",hsystDraw.GetBinContent(1)
    print "nominal sys val error:",hsystDraw.GetBinError(1)
    systvarhistRatio[samp+syst+'__plus__ratio'].Sumw2()
    systvarhistRatio[samp+syst+'__plus__ratio'].Divide(hsystDraw)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetYaxis().SetRangeUser(0.6,1.4)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetYaxis().SetNdivisions(5,5,0)
    systvarhistRatio[samp+syst+'__plus__ratio'].SetMarkerStyle(1)
    systvarhistRatio[samp+syst+'__plus__ratio'].SetTitle("")
    systvarhistRatio[samp+syst+'__plus__ratio'].Draw('e,x0')
    #systvarhistRatio[samp+syst+'__plus__ratio'].SetTitle("")
    
    systvarhistRatio[samp+syst+'__plus__ratio'].GetXaxis().SetTitle("\Delta|y_{rec}|")
    #systvarhistRatio[samp+syst+'__plus__ratio'].GetXaxis().CenterTitle(True)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetXaxis().SetTitleSize(0.08)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetXaxis().SetTitleOffset(0.8)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetXaxis().SetLabelSize(.05)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetXaxis().SetLabelOffset(0.004)

    systvarhistRatio[samp+syst+'__plus__ratio'].GetYaxis().SetTitle("Ratio")
    systvarhistRatio[samp+syst+'__plus__ratio'].GetYaxis().SetTitleSize(17)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetYaxis().SetTitleFont(43)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetYaxis().SetTitleOffset(1.4)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetYaxis().CenterTitle(True)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetYaxis().SetLabelFont(43)
    systvarhistRatio[samp+syst+'__plus__ratio'].GetYaxis().SetLabelSize(9)

    systvarhistRatio[samp+syst+'__minus__ratio'] = hsystDownDraw.Clone(samp+syst+'Down_Ratio')
    print "down sys val:",systvarhistRatio[samp+syst+'__minus__ratio'].GetBinContent(1)
    print "down sys val error:",systvarhistRatio[samp+syst+'__minus__ratio'].GetBinError(1)
    systvarhistRatio[samp+syst+'__minus__ratio'].Sumw2()
    systvarhistRatio[samp+syst+'__minus__ratio'].Divide(hsystDraw)
    systvarhistRatio[samp+syst+'__minus__ratio'].GetYaxis().SetTitle("")
    systvarhistRatio[samp+syst+'__minus__ratio'].GetYaxis().SetTitleSize(10)
    systvarhistRatio[samp+syst+'__minus__ratio'].SetMarkerStyle(1)
    systvarhistRatio[samp+syst+'__minus__ratio'].SetTitle("")
    print "down sys val error after div:",systvarhistRatio[samp+syst+'__minus__ratio'].GetBinError(1)
    systvarhistRatio[samp+syst+'__minus__ratio'].Draw('e,x0,same')
    pad2.Update()


#Loop over samples and systematic sources and draw their histograms

#This loop handles the 
for samp in sample:
    #This loop iterates through the systematic sources of interest
    for syst in systematics:
	#This loop iterates through the input files for each year-channel-masscut combination
        for input_file, file_name in zipped_files:
            #print 'samp and syst and input_file are', samp,'and', syst, 'and', input_file
            hsyst = input_file.Get(samp+'_'+'nominal')
            hsystUp = input_file.Get(samp+'_'+syst+'Up')
            hsystDown = input_file.Get(samp+'_'+syst+'Down')
            
            print(hsyst, hsystUp, hsystDown)
            
            #Legend is placed on different sides depending on source
            if samp == 'Ttbar_1':
                set_canvleg1()
            if samp == 'Ttbar_2':
                set_canvleg2()
            
            set_pad1()
            draw_histos()
            draw_legend()
            latexCMStitle()
            #latex2()  # Not including Lumi info
            
            #Add gen-cut label on side of lower bin, side depends on source
            #if samp == 'Ttbar_1':
            #    latexNegGenCut()
            #if samp == 'Ttbar_2':
            #    latexPosGenCut()

            set_pad2()
            draw_ratiohisto()
            latexBinErrorInfo()

            #if samp == 'Ttbar_1':
            #    systvarhistRatio[samp+syst+'__plus__ratio'].GetXaxis().SetTitle("| #Delta y | < 0")
            #if samp == 'Ttbar_2':
            #    systvarhistRatio[samp+syst+'__plus__ratio'].GetXaxis().SetTitle("| #Delta y | > 0")

            pad2.Update()

            #Save canvas as pdf with name that corresponds to source
            if samp == 'Ttbar_1':
                canvas_Bkg.SaveAs('SystematicVariation_'+samp+'_'+syst+'DeltaYnegative.pdf')
            if samp == 'Ttbar_2':
                canvas_Bkg.SaveAs('SystematicVariation_'+samp+'_'+syst+'DeltaYpositive.pdf')




