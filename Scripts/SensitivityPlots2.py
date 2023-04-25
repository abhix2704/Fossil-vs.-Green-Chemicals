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
BAUprices = df["BAU"]
gAWind = df["Wind"]
gASolar = df["Solar"]
gASMRCCS = df["SMR CCS"]

sheetName = "Ammonia high low"
df = pd.read_excel(fileName, sheetName)
gAWindLow = df["Wind low"]
gAWindHigh = df["Wind high"]
gASolarLow = df["Solar low"]
gASolarHigh = df["Solar high"]

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
plt.title("(a) Ammonia - H$_\mathrm{2}$ wind", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "*", s = 10)
plt.scatter(index[0:l], gAWind[0:l], marker = "^", color = "#007f5f", s = 10)
plt.fill_between(index[0:l], gAWindHigh[0:l], gAWindLow[0:l], facecolor = '#007f5f', alpha = 0.2)
yerr = np.array([gAWind[0:l] - gAWindLow[0:l], gAWindHigh[0:l] - gAWind[0:l]])
#plt.errorbar(index[0:l], gAWind[0:l], yerr, color = '#007f5f', fmt = "None", linewidth = 0.75, capsize = 2)
plt.xlim(0,index[len(index)-1]+2)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.xticks([])

plt.subplot(3,2,3)
plt.title("(b) Ammonia - H$_\mathrm{2}$ solar", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "*", s = 10)
plt.scatter(index[0:l], gASolar[0:l], marker = "h", color = "#f26419", s = 10)
plt.fill_between(index[0:l], gASolarHigh[0:l], gASolarLow[0:l], facecolor = '#f26419', alpha = 0.2)
yerr = np.array([gASolar[0:l] - gASolarLow[0:l], gASolarHigh[0:l] - gASolar[0:l]])
#plt.errorbar(index[0:l], gASolar[0:l], yerr, color = '#f26419', fmt = "None", linewidth = 0.75, capsize = 2)
plt.xlim(0,index[len(index)-1]+2)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.xticks([])

plt.subplot(3,2,5)
plt.title("(c) Ammonia - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", color = "black", fontsize = fontsize_title, fontweight = "bold")
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
ax.legend(handles = legend_elements, loc = "upper center", ncol = 2, prop={"size":8}, bbox_to_anchor=(0.5, -0.25))

sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
BAUprices = df["BAU"]
gMWind = df["DAC + wind"]
gMSolar = df["DAC + solar"]
gMSMRCCS = df["SMR CCS"]

sheetName = "Methanol high low"
df = pd.read_excel(fileName, sheetName)
gMWindLow = df["DAC + wind low"]
gMWindHigh = df["DAC + wind high"]
gMSolarLow = df["DAC + solar low"]
gMSolarHigh = df["DAC + solar high"]

plt.subplot(3,2,2)
plt.title("(d) Methanol - H$_\mathrm{2}$ wind", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "p", s = 10)
plt.scatter(index[0:l], gMWind[0:l], marker = "^", color = "#007f5f", s = 10)
plt.fill_between(index[0:l], gMWindHigh[0:l], gMWindLow[0:l], facecolor = '#007f5f', alpha = 0.2)
yerr = np.array([gMWind[0:l] - gMWindLow[0:l], gMWindHigh[0:l] - gMWind[0:l]])
#plt.errorbar(index[0:l], gMWind[0:l], yerr, color = '#007f5f', fmt = "None", linewidth = 0.75, capsize = 2)
plt.xlim(0,index[len(index)-1]+2)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.xticks([])

plt.subplot(3,2,4)
plt.title("(e) Methanol - H$_\mathrm{2}$ solar", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "p", s = 10)
plt.scatter(index[0:l], gMSolar[0:l], marker = "h", color = "#f26419", s = 10)
plt.fill_between(index[0:l], gMSolarHigh[0:l], gMSolarLow[0:l], facecolor = '#f26419', alpha = 0.2)
yerr = np.array([gMSolar[0:l] - gMSolarLow[0:l], gMSolarHigh[0:l] - gMSolar[0:l]])
#plt.errorbar(index[0:l], gMSolar[0:l], yerr, color = '#f26419', fmt = "None", linewidth = 0.75, capsize = 2)
plt.xlim(0,index[len(index)-1]+2)
plt.ylabel("Production cost [USD t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 90)
plt.xticks([])

plt.subplot(3,2,6)
plt.title("(f) Methanol - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", color = "black", fontsize = fontsize_title, fontweight = "bold")
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
ax.legend(handles = legend_elements, loc = "upper center", ncol = 2, prop={"size":8}, bbox_to_anchor=(0.5, -0.25))

plt.savefig('Figure 2 (Antonio).jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure 2 (Antonio).svg', dpi=600, format='svg', bbox_inches="tight")


