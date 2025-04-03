##############################################################################
# Author: M.Antonello 
# Date: 29/07/2023
# Input: 2 noise root files from threshold scans 
# Usage: python3 Missing_Full_Analysis_Ph2ACF_CROC_NoXray.py -scurve1 Run000012 -bias1 m30 -scurve2 Run000013 -bias2 p0_45 -outpath ADVCAM -sensor ADV_W_8_64_NoXray -vref 827
# Output: png plots with the main results
# Variables to change: Sensor, Thr, VMAX (only if hot pixels are present) 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################################################
import os
from scipy.optimize import curve_fit
import ROOT; ROOT.gErrorIgnoreLevel = ROOT.kWarning; ROOT.gROOT.SetBatch(True) 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mplhep as hep; hep.style.use("CMS")
import argparse

# Arguments --------------------
parser = argparse.ArgumentParser(description='Do the XRay analysis')
parser.add_argument('-scurve1','--scurve1', help = 'The name of the SCurve.root file', default = 'Run000005', type = str)
parser.add_argument('-scurve2','--scurve2', help = 'The name of the SCurve.root file', default = 'Run000007', type = str)
parser.add_argument('-outpath','--outpath', help = 'The name of the folder to be created in results', default = 'RH0027_13000e_Chip12', type = str)
parser.add_argument('-sensor','--sensor', help = 'The name of the sensor', default = 'Chip12', type = str)
parser.add_argument('-thr_missing','--thr_missing', help = 'The threshold to classify the missing bumps [DVCAL]', default = 0, type = int)
parser.add_argument('-thr_strange','--thr_strange', help = 'The threshold to classify the problematic bumps [DVCAL]', default = 75, type = int)
parser.add_argument('-noise_missing','--noise_missing', help = 'The noise threshold to classify the missing bumps [DVCAL]', default = 0, type = int)
parser.add_argument('-noise_strange','--noise_strange', help = 'The noise threshold to classify the problematic bumps [DVCAL]', default = 25, type = int)
parser.add_argument('-bias1','--bias1', help = 'The bias of the sensor [V]', default = 'm80', type = str)
parser.add_argument('-bias2','--bias2', help = 'The bias of the sensor [V]', default = 'p0_25', type = str)
parser.add_argument('-vref','--vref', help = 'The VRef_ADC [mV]', default = 800, type = int)
args = parser.parse_args()

Sensor=args.sensor
# thr_data_file1='./overlay/'+args.scurve1+'_SCurve.root'
# thr_data_file2='./tunedto4000e/'+args.scurve2+'_SCurve.root'
thr_data_file1='./SCurve_13000_RB.root'
thr_data_file2='./SCurve_13000_FB.root'
Path='FB_13000_FB/'+args.outpath+'/'
Thr=args.thr_missing
Thr_strange=args.thr_strange
Noise=args.noise_missing
Noise_strange=args.noise_strange
Voltage_1=args.bias1
Voltage_2=args.bias2
V_adc=args.vref

####### PARAMETERS TO BE CHANGED MANUALLY: ###################################  
xcut=Thr
ycut=Noise
xcut_strange=Thr_strange
ycut_strange=Noise_strange
BinMaxX=2000.5
BinMaxY=150.5
VMAXDiff=100
ZoomX=800
ZoomY=150
H_ID='0'
C_ID='12'
num_rows = 336
num_cols = 432
FIT=False
el_conv=V_adc/162
Noise_MAX=65*el_conv
Thr_MAX=1800*el_conv
Voltage_Diff='Diff'
step_noise=0.1*el_conv
step_thr=24*el_conv
YMAX=100000
step=10
VMAX=2000
##############################################################################

if not os.path.exists(Path+Sensor):
    os.makedirs(Path+Sensor)

def Ph2_ACFRootExtractor(infile, Scan_n, type):
    canvas = infile.Get("Detector/Board_0/OpticalGroup_0/Hybrid_"+H_ID+"/Chip_"+str(int(C_ID))+"/D_B(0)_O(0)_H("+H_ID+")_"+Scan_n+"_Chip("+str(int(C_ID))+")")
    map_r = canvas.GetPrimitive("D_B(0)_O(0)_H("+H_ID+")_"+Scan_n+"_Chip("+str(int(C_ID))+")")
    if "2D" in type:
        # Convert the TH2F histogram to np array (NB: bin numbering in root starts from 1, numpy from 0)
        map = np.zeros((map_r.GetNbinsX(), map_r.GetNbinsY()))
        for i in range(1, map_r.GetNbinsX()+1):
            for j in range(1, map_r.GetNbinsY()+1):
                map[i-1][j-1] = map_r.GetBinContent(i, j)
        map=map.T
    else:
        map = map_r.GetEntries()
    return map

def To50x50SensorCoordinates(npArray):
    # For a 50x50 sensor, the coordinates are likely direct mapping without complex transformation
    return npArray

def ExtractThrData(fthr_data_file):
    inFile = ROOT.TFile.Open(fthr_data_file, "READ")
    ThrMap = Ph2_ACFRootExtractor(inFile, 'Threshold2D', '2D')
    ThrMap = To50x50SensorCoordinates(ThrMap)
    NoiseMap = Ph2_ACFRootExtractor(inFile, 'Noise2D', '2D')
    NoiseMap = To50x50SensorCoordinates(NoiseMap)
    ToTMap = Ph2_ACFRootExtractor(inFile, 'ToT2D', '2D')
    ToTMap = To50x50SensorCoordinates(ToTMap)
    ReadoutErrors = Ph2_ACFRootExtractor(inFile, 'ReadoutErrors', 'Entries')
    FitErrors = Ph2_ACFRootExtractor(inFile, 'FitErrors', 'Entries')
    inFile.Close()
    Noise_L = NoiseMap.flatten()
    Thr_L = ThrMap.flatten()
    return ThrMap, NoiseMap, ToTMap, ReadoutErrors, FitErrors, Noise_L, Thr_L

def gaus(X, A, X_mean, sigma):
    return A * np.exp(-(X - X_mean) ** 2 / (2 * sigma ** 2))

def GAUSS_FIT(x_hist, y_hist, color):
    mean = sum(x_hist * y_hist) / sum(y_hist)
    sigma = sum(y_hist * (x_hist - mean) ** 2) / sum(y_hist)
    param_optimised, param_covariance_matrix = curve_fit(gaus, x_hist, y_hist, p0=[1, mean, sigma])
    x_hist_2 = np.linspace(np.min(x_hist), np.max(x_hist), 500)
    # plt.plot(x_hist_2, gaus(x_hist_2, *param_optimised), color, label='FIT: $\mu$ = '+str(round(param_optimised[1], 1))+' e$^-$ $\sigma$ = '+str(abs(round(param_optimised[2], 1)))+' e$^-$')
    plt.plot(x_hist_2, gaus(x_hist_2, *param_optimised), color, label=r'FIT: $\mu$ = '+str(round(param_optimised[1], 1))+' e$^-$ $\sigma$ = '+str(abs(round(param_optimised[2], 1)))+' e$^-$')

def NoXRayAnalysis(ThrMap1, NoiseMap1, ThrMap2, NoiseMap2):
    # NoiseMap_Diff = abs(NoiseMap2 - NoiseMap1)
    # Noise_Diff = np.array(NoiseMap_Diff.flatten())
    # ThrMap_Diff = abs(ThrMap2 - ThrMap1)

    NoiseMap_Diff = NoiseMap2 - NoiseMap1  # Removed absolute value
    Noise_Diff = np.array(NoiseMap_Diff.flatten())
    ThrMap_Diff = ThrMap2 - ThrMap1  # Removed absolute value


    Thr_Diff = np.array(ThrMap_Diff.flatten())
    Missing_mat = np.zeros((num_rows, num_cols)) + 3

    Missing = np.where((ThrMap_Diff < xcut) & (NoiseMap_Diff < ycut))
    Perc_missing = float("{:.4f}".format((Missing[0].size / (num_rows * num_cols)) * 100))
    
    # Missing_strange = np.where(((ThrMap_Diff >= xcut) & (ThrMap_Diff < xcut_strange) & (NoiseMap_Diff < ycut_strange)) | ((ThrMap_Diff < xcut) & (NoiseMap_Diff >= ycut) & (NoiseMap_Diff < ycut_strange)))
    # Perc_missing_strange = float("{:.4f}".format((Missing_strange[0].size / (num_rows * num_cols)) * 100))
    
    Missing_mat[Missing[0], Missing[1]] = 1
    # Missing_mat[Missing_strange[0], Missing_strange[1]] = -1
    
    # return Thr_Diff, Noise_Diff, Perc_missing, Perc_missing_strange, Missing_mat, Missing, Missing_strange
    return Thr_Diff, Noise_Diff, Perc_missing, Missing_mat, Missing



def Plot_Distributions(Thr_Diff, Noise_Diff):
    # Delta Noise Distribution
    fig_noise = plt.figure(figsize=(1050 / 96, 750 / 96), dpi=96)
    plt.rcParams.update({'font.size': 16})
    ax_noise = fig_noise.add_subplot(111)
    h_noise = plt.hist(Noise_Diff, bins=np.arange(-BinMaxY, BinMaxY, 1), color='blue', histtype='step')
    ax_noise.set_xlabel(r'$\Delta_{Noise}$ [$\Delta$VCAL]')
    ax_noise.set_ylabel('Entries')
    plt.title("ΔNoise Distribution")
    fig_noise.savefig(Path + Sensor + '/Delta_Noise_Distribution.png', format='png', dpi=300)
    
    # Delta Threshold Distribution
    fig_thr = plt.figure(figsize=(1050 / 96, 750 / 96), dpi=96)
    plt.rcParams.update({'font.size': 16})
    ax_thr = fig_thr.add_subplot(111)
    h_thr = plt.hist(Thr_Diff, bins=np.arange(-BinMaxX, BinMaxX, 1), color='green', histtype='step')
    ax_thr.set_xlabel(r'$\Delta_{Threshold}$ [$\Delta$VCAL]')
    ax_thr.set_ylabel('Entries')
    plt.title("ΔThreshold Distribution")
    fig_thr.savefig(Path + Sensor + '/Delta_Threshold_Distribution.png', format='png', dpi=300)


# def Plots(Missing_mat, Thr_Diff, Noise_Diff, Missing, Missing_strange, Perc_missing, Perc_missing_strange, FitErrors1):
def Plots(Missing_mat, Thr_Diff, Noise_Diff, Missing, Perc_missing, FitErrors1):
    
    
    fig13 = plt.figure(figsize=(1050/96, 750/96), dpi=96)
    plt.rcParams.update({'font.size': 16})
    ax = fig13.add_subplot(111)

    # imgplot = plt.hist2d(Thr_Diff, Noise_Diff, bins=[np.arange(-0.5, BinMaxX, 1), np.arange(-0.5, BinMaxY, 1)], cmin=1, vmax=VMAXDiff)
    imgplot = plt.hist2d(Thr_Diff, Noise_Diff, bins=[np.arange(-BinMaxX, BinMaxX, 1), np.arange(-BinMaxY, BinMaxY, 1)], cmin=1, vmax=VMAXDiff)  # Extend bin range to negative values

    plt.plot([-xcut, xcut], [ycut, ycut], 'r')  # Top horizontal line
    plt.plot([-xcut, xcut], [-ycut, -ycut], 'r')  # Bottom horizontal line
    plt.plot([xcut, xcut], [-ycut, ycut], 'r')  # Right vertical line
    plt.plot([-xcut, -xcut], [-ycut, ycut], 'r')  # Left vertical line

    # plt.plot([xcut_strange, xcut_strange], [0, ycut_strange], 'orange')
    # plt.plot([0, xcut_strange], [ycut_strange, ycut_strange], 'orange')

    # plt.plot([xcut, xcut], [-BinMaxY, ycut], 'r')  # Adjust to allow plotting across the negative Y range
    # plt.plot([-BinMaxX, xcut], [ycut, ycut], 'r')
    # plt.plot([xcut, xcut], [0, ycut], 'r')
    # plt.plot([0, xcut], [ycut, ycut], 'r')

    # ax.set_xlabel(r'|$\Delta_{Threshold}$| [$\Delta$VCAL]')
    # ax.set_ylabel(r'|$\Delta_{Noise}$| [$\Delta$VCAL]')
    ax.set_xlabel(r'$\Delta_{Threshold}$ [$\Delta$VCAL]')
    ax.set_ylabel(r'$\Delta_{Noise}$ [$\Delta$VCAL]')
    
    plt.colorbar()
    fig13.savefig(Path + Sensor + '/MAP_diff_Noise_Hist.png', format='png', dpi=300)

    # ZOOM
    fig13 = plt.figure(figsize=(1050/96, 750/96), dpi=96)
    plt.rcParams.update({'font.size': 16})
    ax = fig13.add_subplot(111)
    # imgplot = plt.hist2d(Thr_Diff, Noise_Diff, bins=[np.arange(-0.5, BinMaxX, 1), np.arange(-0.5, BinMaxY, 1)], cmin=1, vmax=VMAXDiff)
    imgplot = plt.hist2d(Thr_Diff, Noise_Diff, bins=[np.arange(-ZoomX, ZoomX, 1), np.arange(-ZoomY, ZoomY, 1)], cmin=1, vmax=VMAXDiff)  # Extend to include negative values


    # plt.plot([xcut_strange, xcut_strange], [0, ycut_strange], 'orange')
    # plt.plot([0, xcut_strange], [ycut_strange, ycut_strange], 'orange')

    plt.plot([-xcut, xcut], [ycut, ycut], 'r')  # Top horizontal line
    plt.plot([-xcut, xcut], [-ycut, -ycut], 'r')  # Bottom horizontal line
    plt.plot([xcut, xcut], [-ycut, ycut], 'r')  # Right vertical line
    plt.plot([-xcut, -xcut], [-ycut, ycut], 'r')  # Left vertical line

    # plt.plot([xcut, xcut], [0, ycut], 'r')
    # plt.plot([0, xcut], [ycut, ycut], 'r')
    # plt.plot([xcut, xcut], [-ZoomY, ycut], 'r')
    # plt.plot([-ZoomX, xcut], [ycut, ycut], 'r')

    # ax.set_xlabel(r'|$\Delta_{Threshold}$| [$\Delta$VCAL]')
    # ax.set_ylabel(r'|$\Delta_{Noise}$| [$\Delta$VCAL]')
    ax.set_xlabel(r'$\Delta_{Threshold}$ [$\Delta$VCAL]')
    ax.set_ylabel(r'$\Delta_{Noise}$ [$\Delta$VCAL]')
    plt.colorbar()
    ax.set_xlim(right=ZoomX)
    ax.set_ylim(top=ZoomY)
    fig13.savefig(Path+Sensor+'/MAP_diff_Noise_Hist_zoom.png', format='png', dpi=300)
    
    # MISSING BUMPS FINAL MAPS
    fig8 = plt.figure(figsize=(1050/96, 750/96), dpi=96)
    plt.rcParams.update({'font.size': 16})
    ax = fig8.add_subplot(111)
    ax.spines["bottom"].set_linewidth(1)
    ax.spines["left"].set_linewidth(1)
    ax.spines["top"].set_linewidth(1)
    ax.spines["right"].set_linewidth(1)

    fig8.suptitle("Sensor " + Sensor + " -- Fit errors: " + str(FitErrors1) + "\nMissing bumps: " + str(Missing[0].size) + " (" + str(Perc_missing) + "%)")

    # Updated colormap and bounds: remove references to strange or problematic bumps
    cmap = matplotlib.colors.ListedColormap(['red', 'white'])  # Only 'Missing' and 'Good'
    bounds = [0, 1.9, 3.1]  # Only include Missing (red) and Good (white)
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)

    # Update the imshow to reflect the correct bounds and cmap
    imgplot2 = ax.imshow(Missing_mat, cmap=cmap, norm=norm, origin='lower')
    ax.set_aspect(1)

    # Update the colorbar label to remove problematic bumps
    bar2 = plt.colorbar(imgplot2, ticks=[1, 3], orientation='horizontal', label='Missing (Red)           Good (White)', spacing='proportional', shrink=0.7)
    bar2.set_ticks([])

    # Save the figure without problematic bumps
    fig8.savefig(Path + Sensor + '/Missing_Bumps_Thr_' + str(xcut) + '_Noise_' + str(ycut) + '.png', format='png', dpi=300, bbox_inches='tight')

    

    # # MISSING BUMPS FINAL MAPS
    # fig8 = plt.figure(figsize=(1050/96, 750/96), dpi=96)
    # plt.rcParams.update({'font.size': 16})
    # ax = fig8.add_subplot(111)
    # ax.spines["bottom"].set_linewidth(1); ax.spines["left"].set_linewidth(1); ax.spines["top"].set_linewidth(1); ax.spines["right"].set_linewidth(1)
    # # fig8.suptitle("Sensor " + Sensor + " -- Fit errors: " + str(FitErrors1) + "\nMissing bumps: " + str(Missing[0].size) + " (" + str(Perc_missing) + "%) -- Problematic bumps: " + str(Missing_strange[0].size) + " (" + str(Perc_missing_strange) + "%)")
    # fig8.suptitle("Sensor " + Sensor + " -- Fit errors: " + str(FitErrors1) + "\nMissing bumps: " + str(Missing[0].size) + " (" + str(Perc_missing) + "%) -- Problematic bumps: " )
    # cmap = matplotlib.colors.ListedColormap(['orange', 'blue', 'red', 'white'])
    # bounds = [-1, 0, 0.9, 1.9, 2.9]
    # norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    # imgplot2 = ax.imshow(Missing_mat, cmap=cmap, norm=norm)
    # ax.set_aspect(1)
    # bar2 = plt.colorbar(imgplot2, ticks=bounds, orientation='horizontal', label='Problematic         Masked           Missing            Good         ', spacing='proportional', shrink=0.7)
    # bar2.set_ticks([])
    # fig8.savefig(Path + Sensor + '/Missing_Bumps_Thr_' + str(xcut) + '_Noise_' + str(ycut) + '.png', format='png', dpi=300, bbox_inches='tight')

    return

def Plots_Thr(ToTMap, NoiseMap, Noise_L, ThrMap, Thr_L, VoltageN):
    # Noise Map
    fig1 = plt.figure()
    ax = fig1.add_subplot(111)
    ax.spines["bottom"].set_linewidth(1); ax.spines["left"].set_linewidth(1); ax.spines["top"].set_linewidth(1); ax.spines["right"].set_linewidth(1)
    imgplot = ax.imshow(NoiseMap * el_conv, vmax=Noise_MAX, vmin=0)
    ax.set_aspect(1)
    bar1 = plt.colorbar(imgplot, orientation='horizontal', extend='max', label='electrons')
    fig1.savefig(Path + Sensor + '/' + VoltageN + 'V_Noise_Map.png', format='png', dpi=300)

    # Histogram
    fig2 = plt.figure(figsize=(1050/96, 750/96), dpi=96)
    ax = fig2.add_subplot(111)
    ax.spines["bottom"].set_linewidth(1); ax.spines["left"].set_linewidth(1); ax.spines["top"].set_linewidth(1); ax.spines["right"].set_linewidth(1)
    h_S = plt.hist(Noise_L * el_conv, color='black', bins=np.arange(0, Noise_MAX, step_noise), label='Noise', histtype='step')
    if FIT: GAUSS_FIT(h_S[1][:-1], h_S[0], 'red')
    ax.set_ylim([0.1, 10000])
    ax.set_yscale('log')
    ax.set_xlabel('electrons')
    ax.set_ylabel('entries')
    ax.legend(prop={'size': 14}, loc='upper right')
    fig2.savefig(Path + Sensor + '/' + VoltageN + 'V_Noise_Hist.png', format='png', dpi=300)

    # Threshold Map
    fig3 = plt.figure()
    ax = fig3.add_subplot(111)
    ax.spines["bottom"].set_linewidth(1); ax.spines["left"].set_linewidth(1); ax.spines["top"].set_linewidth(1); ax.spines["right"].set_linewidth(1)
    imgplot = ax.imshow(ThrMap * el_conv, vmax=Thr_MAX, vmin=3000)
    ax.set_aspect(1)
    bar2 = plt.colorbar(imgplot, orientation='horizontal', extend='max', label='electrons')
    fig3.savefig(Path + Sensor + '/' + VoltageN + 'V_Threshold_Map.png', format='png', dpi=300)

    # Histogram
    fig4 = plt.figure(figsize=(1050/96, 750/96), dpi=96)
    ax = fig4.add_subplot(111)
    ax.spines["bottom"].set_linewidth(1); ax.spines["left"].set_linewidth(1); ax.spines["top"].set_linewidth(1); ax.spines["right"].set_linewidth(1)
    h_L = plt.hist(Thr_L * el_conv, color='black', bins=np.arange(3000, Thr_MAX, step_thr), label='Threshold', histtype='step')
    if FIT: GAUSS_FIT(h_L[1][:-1], h_L[0], 'red')
    ax.set_ylim([0.1, YMAX])
    ax.set_xlim([3000, Thr_MAX])
    ax.set_yscale('log')
    ax.set_xlabel('electrons')
    ax.set_ylabel('entries')
    ax.legend(prop={'size': 14}, loc='upper left')
    fig4.savefig(Path + Sensor + '/' + VoltageN + 'V_Threshold_Hist.png', format='png', dpi=300)

    # ToT Map
    fig5 = plt.figure()
    ax = fig5.add_subplot(111)
    ax.spines["bottom"].set_linewidth(1); ax.spines["left"].set_linewidth(1); ax.spines["top"].set_linewidth(1); ax.spines["right"].set_linewidth(1)
    imgplot = ax.imshow(ToTMap)
    ax.set_aspect(1)
    bar2 = plt.colorbar(imgplot, orientation='horizontal', extend='max', label='ToT')
    fig5.savefig(Path + Sensor + '/' + VoltageN + 'V_ToT_Map.png', format='png', dpi=300)

    return

def TerminalInfos(FitErrors1, ReadoutErrors1, FitErrors2, ReadoutErrors2, Missing_mat):
    print('##################################################################################\n INFO\n##################################################################################')
    print('Failed fits (thr 1):\t'+str(FitErrors1)+'\t\t\tReadout Errors (thr 1):\t'+str(ReadoutErrors1))
    print('Failed fits (thr 2):\t'+str(FitErrors2)+'\t\tReadout Errors (thr 2):\t'+str(ReadoutErrors2))
    print('Check from Final matrix:')
    print('Missing:\t\t'+str(np.where(Missing_mat==1)[0].size)+'\t\t\tStrange:\t\t'+str(np.where(Missing_mat==-1)[0].size))
    print('Sum is: \t\t'+str(np.where(Missing_mat==0)[0].size+np.where(Missing_mat==1)[0].size+np.where(Missing_mat==2)[0].size+np.where(Missing_mat==3)[0].size+np.where(Missing_mat==-1)[0].size)+'\t\t\tTotal # of pixels:\t'+str(num_cols*num_rows))
    print('##################################################################################\n')
    return

def main():
    # First Voltage
    ThrMap1, NoiseMap1, ToTMap1, ReadoutErrors1, FitErrors1, Noise_L1, Thr_L1 = ExtractThrData(thr_data_file1)
    Plots_Thr(ToTMap1, NoiseMap1, Noise_L1, ThrMap1, Thr_L1, Voltage_1)
    # Second Voltage
    ThrMap2, NoiseMap2, ToTMap2, ReadoutErrors2, FitErrors2, Noise_L2, Thr_L2 = ExtractThrData(thr_data_file2)
    Plots_Thr(ToTMap2, NoiseMap2, Noise_L2, ThrMap2, Thr_L2, Voltage_2)
    # Difference and final plots
    # Thr_Diff, Noise_Diff, Perc_missing, Perc_missing_strange, Missing_mat, Missing, Missing_strange = NoXRayAnalysis(ThrMap1, NoiseMap1, ThrMap2, NoiseMap2)
    # Plots(Missing_mat, Thr_Diff, Noise_Diff, Missing, Missing_strange, Perc_missing, Perc_missing_strange, FitErrors1)
    Thr_Diff, Noise_Diff, Perc_missing, Missing_mat, Missing = NoXRayAnalysis(ThrMap1, NoiseMap1, ThrMap2, NoiseMap2)
    Plots(Missing_mat, Thr_Diff, Noise_Diff, Missing, Perc_missing, FitErrors1)
    TerminalInfos(FitErrors1, ReadoutErrors1, FitErrors2, ReadoutErrors2, Missing_mat)
    Plot_Distributions(Thr_Diff, Noise_Diff)


if __name__ == "__main__":
    main()
