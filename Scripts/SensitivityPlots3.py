# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:02:05 2022

@author: anabera
"""

fig_length = {1:   3.50394,    # 1 column
          1.5: 5.35433, # 1.5 columns
          2:   7.20472}    # 2 columns
fig_height = 9.72441 # maxium height
fontsize_title = 9
fontsize_label = 8
fontsize_legend = 8
fontsize_axs = 8

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams.update({'font.size': 8})
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(fig_length[2],fig_height*0.8))

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]
market = df["Market"]
BAUprices = df["BAU"]
gABiomassCCS = df["Biomass"]
gAWind = df["Wind"]
gASolar = df["Solar"]
gANuclear = df["Nuclear"]
gASMRCCS = df["SMR CCS"]

sheetName = "Ammonia high low"
df = pd.read_excel(fileName, sheetName)
gAWindLow = df["Wind low"]
gAWindHigh = df["Wind high"]
gASolarLow = df["Solar low"]
gASolarHigh = df["Solar high"]
gANuclearLow = df["Nuclear low"]
gANuclearHigh = df["Nuclear high"]

l = len(times)
labels = times
for i in range(0,len(times)):
    if i == 0 or i % 3 == 0:
        labels[i] = times[i]
    else:
        labels[i] = ""
labels[l-3] = ""
labels[l-2] = ""
labels[l-1] = "Nov '22"

mi = []
miLabels = []
ma = []
maLabels = []
for i in range(0,len(labels)):
    if labels[i] == "":
        mi.append(i + 1)
        miLabels.append(labels[i])
    else:
        ma.append(i + 1)
        maLabels.append(labels[i])

plt.subplot(3,2,1)
plt.title("(a) Ammonia - H$_\mathrm{2}$ wind", y = 0.9, color = "#007f5f", fontsize = fontsize_title, fontweight = "bold")
#plt.plot(index[0:l], market[0:l], "--", color = "brown", linewidth = 2)
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "*", s = 10)
plt.scatter(index[0:l], gAWind[0:l], marker = "^", color = "#007f5f", s = 10)
#plt.fill_between(index[0:l], gAWindLow[0:l], gAWindHigh[0:l], color = "#007f5f", alpha = 0.2)
yerr = np.array([gAWind[0:l] - gAWindLow[0:l], gAWindHigh[0:l] - gAWind[0:l]])
#plt.errorbar(index[0:l], gAWind[0:l], yerr, color = '#007f5f', fmt = "None", linewidth = 0.75, capsize = 2)
plt.fill_between(NGprices, gAWindHigh, gAWindLow, facecolor = '#007f5f', alpha = 0.2)
plt.xlim(0,index[len(index)-1]+2)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.xticks([])


plt.subplot(3,2,3)
plt.title("(b) Ammonia - H$_\mathrm{2}$ solar", y = 0.9, color = "#f26419", fontsize = fontsize_title, fontweight = "bold")
#plt.plot(index[0:l], market[0:l], "--", color = "brown", linewidth = 2)
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "*", s = 10)
plt.scatter(index[0:l], gASolar[0:l], marker = "h", color = "#f26419", s = 10)
yerr = np.array([gASolar[0:l] - gASolarLow[0:l], gASolarHigh[0:l] - gASolar[0:l]])
plt.errorbar(index[0:l], gASolar[0:l], yerr, color = '#f26419', fmt = "None", linewidth = 0.75, capsize = 2)
plt.xlim(0,index[len(index)-1]+2)
#plt.fill_between(index[0:l], gASolarLow[0:l], gASolarHigh[0:l], color = "#f26419", alpha = 0.2)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.xticks([])


plt.subplot(3,2,5)
plt.title("(c) Ammonia - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", y = 0.9, color = "#420169", 
          fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "*", s = 10)
plt.xlim(0,index[len(index)-1]+2)
plt.scatter(index[0:l], gASMRCCS[0:l], color = "#420169", marker = "X", s = 10)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
ax = plt.gca()
ax.set_xticks(ma, labels = maLabels, rotation = 45, ha = "right")
ax.set_xticks(mi, minor=True)
plt.xlim(0,index[len(index)-1]+1)

legend_elements = [Line2D([0], [0], marker='*', color='w', label = 'Fossil',
                          markerfacecolor='k', markersize = 10),
                   Line2D([0], [0], marker='^', color='w', label='H$_\mathrm{2}$ Wind',
                                             markerfacecolor='#007f5f', markersize = 7.5),
                   Line2D([0], [0], marker='h', color='w', label='H$_\mathrm{2}$ Solar',
                                             markerfacecolor='#f26419', markersize = 7.5),
                   Line2D([0], [0], marker='X', color='w', label='H$_\mathrm{2}$ SMR$_\mathrm{CCS}$',
                                             markerfacecolor='#420169', markersize = 7.5),]
ax.legend(handles = legend_elements, loc = "upper center", ncol = 2, prop={"size":8}, bbox_to_anchor=(0.5, -0.2))


sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]
market = df["Market"]
BAUprices = df["BAU"]
gMBiomassCCS = df["DAC + biomass"]
gMWind = df["DAC + wind"]
gMSolar = df["DAC + solar"]
gMNuclear = df["DAC + nuclear"]
gMSMRCCS = df["SMR CCS"]

sheetName = "Methanol high low"
df = pd.read_excel(fileName, sheetName)
gMWindLow = df["DAC + wind low"]
gMWindHigh = df["DAC + wind high"]
gMSolarLow = df["DAC + solar low"]
gMSolarHigh = df["DAC + solar high"]
gMNuclearLow = df["DAC + nuclear low"]
gMNuclearHigh = df["DAC + nuclear high"]

l = len(times)
labels = times
for i in range(0,len(times)):
    if i == 0 or i % 3 == 0:
        labels[i] = times[i]
    else:
        labels[i] = ""
labels[l-3] = ""
labels[l-2] = ""
labels[l-1] = "Nov '22"

plt.subplot(3,2,2)
plt.title("(d) Methanol - H$_\mathrm{2}$ wind", y = 0.9, color = "#007f5f", fontsize = fontsize_title, fontweight = "bold")
#plt.plot(index[0:l], market[0:l], "--", color = "brown", linewidth = 2)
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "p", s = 10)
plt.scatter(index[0:l], gMWind[0:l], marker = "^", color = "#007f5f", s = 10)
#plt.fill_between(index[0:l], gAWindLow[0:l], gAWindHigh[0:l], color = "#007f5f", alpha = 0.2)
yerr = np.array([gMWind[0:l] - gMWindLow[0:l], gMWindHigh[0:l] - gMWind[0:l]])
plt.errorbar(index[0:l], gMWind[0:l], yerr, color = '#007f5f', fmt = "None", linewidth = 0.75, capsize = 2)
plt.xlim(0,index[len(index)-1]+2)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.xticks([])


plt.subplot(3,2,4)
plt.title("(e) Methanol - H$_\mathrm{2}$ solar", y = 0.9, color = "#f26419", fontsize = fontsize_title, fontweight = "bold")
#plt.plot(index[0:l], market[0:l], "--", color = "brown", linewidth = 2)
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "p", s = 10)
plt.scatter(index[0:l], gMSolar[0:l], marker = "h", color = "#f26419", s = 10)
yerr = np.array([gMSolar[0:l] - gMSolarLow[0:l], gMSolarHigh[0:l] - gMSolar[0:l]])
plt.errorbar(index[0:l], gMSolar[0:l], yerr, color = '#f26419', fmt = "None", linewidth = 0.75, capsize = 2)
plt.xlim(0,index[len(index)-1]+2)
#plt.fill_between(index[0:l], gASolarLow[0:l], gASolarHigh[0:l], color = "#f26419", alpha = 0.2)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 90)
plt.xticks([])


plt.subplot(3,2,6)
plt.title("(f) Methanol - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", y = 0.9, color = "#420169", 
          fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "p", s = 10)
plt.xlim(0,index[len(index)-1]+2)
plt.scatter(index[0:l], gMSMRCCS[0:l], color = "#420169", marker = "X", s = 10)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
ax = plt.gca()
ax.set_xticks(ma, labels = maLabels, rotation = 45, ha = "right")
ax.set_xticks(mi, minor=True)
plt.xlim(0,index[len(index)-1]+1)


legend_elements = [Line2D([0], [0], marker='p', color='w', label = 'Fossil',
                          markerfacecolor='k', markersize = 7.5),
                   Line2D([0], [0], marker='^', color='w', label='H$_\mathrm{2}$ Wind',
                                             markerfacecolor='#007f5f', markersize = 7.5),
                   Line2D([0], [0], marker='h', color='w', label='H$_\mathrm{2}$ Solar',
                                             markerfacecolor='#f26419', markersize = 7.5),
                   Line2D([0], [0], marker='X', color='w', label='H$_\mathrm{2}$ SMR$_\mathrm{CCS}$',
                                             markerfacecolor='#420169', markersize = 7.5),]
ax.legend(handles = legend_elements, loc = "upper center", ncol = 2, prop={"size":8}, bbox_to_anchor=(0.5, -0.2))
plt.savefig('Figure 1b.jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure 1b.svg', dpi=600, format='svg', bbox_inches="tight")
#plt.savefig('Figure 1.svg', dpi=600, bbox_inches='tight')
#plt.savefig('Figure 1.jpg', dpi=600, bbox_inches='tight')


"""
plt.subplot(3,2,4)
plt.title("(d) Biomass", y = 0.9, color = "blue", fontsize = 18)
plt.plot(index[0:l], market[0:l], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l], BAUprices[0:l], color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.plot(index[0:l], gABiomassCCS[0:l], color = "blue", linewidth = 2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.ylim(a)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l]), (NGprices[l-4], NGprices[l]), color = "black", linewidth = 2)
plt.plot((index[l], index[l-2]), (NGprices[l], NGprices[l-2]), color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [USD t$^\mathrm{-1}$]", x = 0.97)

plt.subplot(3,2,5)
plt.title("(e) H$_\mathrm{2}$ SMR + CCS", y = 0.9, color = "#420169", fontsize = 18)
plt.plot(index[0:l], market[0:l], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l], BAUprices[0:l], color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.plot(index[0:l], gASMRCCS[0:l], color = "#420169", linewidth = 2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l]), (NGprices[l-4], NGprices[l]), color = "black", linewidth = 2)
plt.plot((index[l], index[l-2]), (NGprices[l], NGprices[l-2]), color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
plt.ylim(b[0], 4000)
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [USD t$^\mathrm{-1}$]", x = 0.97)



fileName = "Model validation.xlsx"

sheetName = "Ammonia validation"
df = pd.read_excel(fileName, sheetName)
Aindex = df["Index"]
Atimes = df["Time"]
AlitPrice = df["Lit price"]
ABAUPrice = df["BAU price"]


l = len(Atimes)
labels = Atimes[0:l]
for i in range(0,len(Atimes)):
    if i == 0 or i % 2 == 0:
        labels[i] = Atimes[i]
    else:
        labels[i] = ""
        
plt.subplot(3,2,6)
plt.plot(Aindex, AlitPrice, "--", color = "black", linewidth = 2)
plt.plot(Aindex, ABAUPrice, color = "black", linewidth = 2)
#plt.plot(times, CSolar, color = "#f26419", linewidth = 2)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(Aindex, labels, rotation = 45)
plt.title("(f) Model validation", y = 0.9, fontsize = 18)
labelsLegend = ["Market", "Model"]
plt.legend(labelsLegend)
"""