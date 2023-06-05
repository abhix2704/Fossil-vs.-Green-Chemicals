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
from matplotlib import ticker as tk
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 8})
fig = plt.figure(figsize=(fig_length[2],fig_height*0.35))
gs1 = gridspec.GridSpec(1, 2)
gs1.update(wspace = 0.075, hspace = 0)

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]/1000
market = df["Market"]
elecPrices = df["Electricity"]/1000
BAUprices = df["BAU"]/1000
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

mi = []
miLabels = []
ma = []
maLabels = []

for i in range(0,len(times)):
    if i == 0 or i % 12 == 0:
        labels[i] = times[i]
        ma.append(i + 1)
        maLabels.append(labels[i])
    elif i % 2 == 0 and i % 12 != 0:
        labels[i] = ""
        mi.append(i + 1)
        miLabels.append(labels[i])

labels[l-3] = ""
labels[l-2] = ""
labels[l-1] = "Nov '22"
ma.append(i + 1)
maLabels.append(labels[l-1])
        
        
ylist = list(range(0,round(max(NGprices)+200)))
NGindex = [0,3,7,12,15,19,24,27,31,36,39,43,46]

plt.subplot(gs1[0])
plt.title("a", color = "black", fontsize = fontsize_title, fontweight = "bold")
#plt.plot([12.5]*len(ylist), ylist, color = "grey", linewidth = 0.2, linestyle = "--", zorder = 0)
#plt.plot([22.5]*len(ylist), ylist, color = "grey", linewidth = 0.2, linestyle = "--", zorder = 0)
#plt.plot([37.5]*len(ylist), ylist, color = "grey", linewidth = 0.2, linestyle = "--", zorder = 0)
#plt.plot([41.5]*len(ylist), ylist, color = "grey", linewidth = 0.2, linestyle = "--", zorder = 0)
#plt.plot(index[0:l], market[0:l], "--", color = "brown", linewidth = 2)
plt.plot(index[NGindex], NGprices[NGindex], color = "#808080", linewidth = 1.5, zorder = 2, linestyle = "--")
plt.plot(index[NGindex], BAUprices[NGindex], color = "black", linewidth = 2, zorder = 3, linestyle = "-")
plt.scatter(index[NGindex], NGprices[NGindex], marker = "o", facecolors = '#808080', edgecolors = "none", s = 20, zorder = 4)
plt.scatter(index[NGindex], BAUprices[NGindex], facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 5)
plt.ylabel("Production cost or price [USD kg$^\mathrm{-1}$]")
ax = plt.gca()
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0,max(NGprices)+0.2)

plt.text(12, 0.870, "Supply chain\ndisruption by\nCOVID", color = "grey", fontsize = fontsize_label, ha = "right")
plt.text(22, 1.400, "Rising\ninflation", color = "grey", fontsize = fontsize_label, ha = "right")
plt.text(37, 2.080, "Russia-Ukraine\nconflict", color = "grey", fontsize = fontsize_label, ha = "right")
plt.text(41, 2.700, "Russia cuts\nsupply", color = "grey", fontsize = fontsize_label, ha = "right")

plt.twinx()
plt.ylim(0,1)
plt.yticks([])
plt.plot(index[NGindex], elecPrices[NGindex], color = "#3D5A80", linewidth = 1.5, zorder = 0, linestyle = ":", alpha = 1.0)
plt.scatter(index[NGindex], elecPrices[NGindex], facecolors = "#3D5A80", edgecolors = "#3D5A80", marker = "P", s = 15, zorder = 1)


sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]/1000
market = df["Market"]
BAUprices = df["BAU"]/1000
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
    if i == 0 or i % 12 == 0:
        labels[i] = times[i]
    else:
        labels[i] = ""
labels[l-3] = ""
labels[l-2] = ""
labels[l-1] = "Nov '22"

#ylist = list(range(0,round(max(NGprices)+200)))

plt.subplot(gs1[1])
plt.title("b", color = "black", fontsize = fontsize_title, fontweight = "bold")
#plt.plot([10.5,12.5], [700,700], color = "grey", linewidth = 0.2, linestyle = "--", zorder = 0)
#plt.plot([22.5]*len(ylist), ylist, color = "grey", linewidth = 0.2, linestyle = "--", zorder = 0)
#plt.plot([37.5]*len(ylist), ylist, color = "grey", linewidth = 0.2, linestyle = "--", zorder = 0)
#plt.plot([41.5]*len(ylist), ylist, color = "grey", linewidth = 0.2, linestyle = "--", zorder = 0)
#plt.plot(index[0:l], market[0:l], "--", color = "brown", linewidth = 2)
plt.plot(index[NGindex], NGprices[NGindex], color = "#808080", linewidth = 1.5, zorder = 0, linestyle = "--")
plt.plot(index[NGindex], BAUprices[NGindex], color = "black", linewidth = 2, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], NGprices[NGindex], marker = "o", facecolors = '#808080', edgecolors = "none", s = 20, zorder = 2)
plt.scatter(index[NGindex], BAUprices[NGindex], facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 3)
#plt.scatter(index[0:l], NGprices[0:l], marker = "o", facecolors = 'black', edgecolors = "none", s = 15, zorder = 0)
#plt.scatter(index[0:l], BAUprices[0:l], facecolors = "#1DABCD", edgecolors = "#167F99", marker = "D", s = 15, zorder = 1)
#plt.scatter(index[0:l], BAUprices[0:l], facecolors = "#ffffff", edgecolors = "#808080", marker = "D", s = 15, zorder = 1)

ax = plt.gca()
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0,max(NGprices)+0.2)
plt.yticks([])

plt.text(12, 0.870, "Supply chain\ndisruption by\nCOVID", color = "grey", fontsize = fontsize_label, ha = "right")
plt.text(22, 1.400, "Rising\ninflation", color = "grey", fontsize = fontsize_label, ha = "right")
plt.text(37, 2.080, "Russia-Ukraine\nconflict", color = "grey", fontsize = fontsize_label, ha = "right")
plt.text(41, 2.700, "Russia cuts\nsupply", color = "grey", fontsize = fontsize_label, ha = "right")

plt.twinx()
ax2 = plt.gca()
plt.ylim(0,1)
#plt.yticks([])
plt.ylabel("Electricity price [USD kWh$^\mathrm{-1}$]", color = "#3D5A80")
plt.plot(index[NGindex], elecPrices[NGindex], color = "#3D5A80", linewidth = 1.5, zorder = 0, linestyle = ":", alpha = 1.0)
plt.scatter(index[NGindex], elecPrices[NGindex], facecolors = "#3D5A80", edgecolors = "#3D5A80", marker = "P", s = 15, zorder = 1)
ax2.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax2.tick_params(axis = 'y', colors = "#3D5A80", which = "both")


legend_elements = [Line2D([0], [0], marker='o', color = "none", 
                          markerfacecolor ='#808080', markeredgecolor = "none",
                          label = 'Natural gas price', markersize = 5),
                   Line2D([0], [0], marker='P', color = "none", 
                                             markerfacecolor ='#3D5A80', markeredgecolor = "#3D5A80",
                                             label = 'Grid electrictiy', markersize = 5),
                   Line2D([0], [0], marker='s', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "black",
                                             label = 'Fossil ammonia', markersize = 5),
                   Line2D([0], [0], marker='D', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "black",
                                             label = 'Fossil methanol', markersize = 5)]

fig.legend(handles = legend_elements, frameon = False, loc = "upper center", ncol = 4, 
           prop={"size":8}, bbox_to_anchor=(0.5, 0.05), handletextpad = 0.1)


plt.savefig('Figure 1a (version 2).jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure 1a (version 2).svg', dpi=600, format='svg', bbox_inches="tight")
#plt.savefig('Figure 1.svg', dpi=600, bbox_inches='tight')
#plt.savefig('Figure 1.jpg', dpi=600, bbox_inches='tight')


"""
plt.subplot(3,2,4)
plt.title("(d) Biomass", y = 0.9, color = "#3D5A80", fontsize = 18)
plt.plot(index[0:l], market[0:l], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l], BAUprices[0:l], color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.plot(index[0:l], gABiomassCCS[0:l], color = "#3D5A80", linewidth = 2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.ylim(a)
plt.ylabel("Ammonia price [USD t$^\mathrm{-1}$]")
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
plt.ylabel("Ammonia price [USD t$^\mathrm{-1}$]")
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
plt.ylabel("Ammonia price [USD t$^\mathrm{-1}$]")
plt.xticks(Aindex, labels, rotation = 45)
plt.title("(f) Model validation", y = 0.9, fontsize = 18)
labelsLegend = ["Market", "Model"]
plt.legend(labelsLegend)
"""