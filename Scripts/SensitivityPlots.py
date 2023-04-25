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
from matplotlib import ticker as tk
import matplotlib.gridspec as gridspec
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams["figure.autolayout"] = True
plt.rcParams.update({'font.size': 8})
plt.rcParams['font.family'] = 'Arial'
fig = plt.figure(figsize=(fig_length[2],fig_height*0.8))

gs1 = gridspec.GridSpec(3, 2)
gs1.update(wspace = 0.2, hspace = 0.1)

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]/1000
BAUprices = df["BAU"]/1000
gAWind = df["Wind"]/1000
gASolar = df["Solar"]/1000
gASMRCCS = df["SMR CCS"]/1000

sheetName = "Ammonia high low"
df = pd.read_excel(fileName, sheetName)
gAWindLow = df["Wind low"]/1000
gAWindHigh = df["Wind high"]/1000
gASolarLow = df["Solar low"]/1000
gASolarHigh = df["Solar high"]/1000

sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
BAUprices = df["BAU"]/1000
gMWind = df["DAC + wind"]/1000
gMSolar = df["DAC + solar"]/1000
gMSMRCCS = df["SMR CCS"]/1000

sheetName = "Methanol high low"
df = pd.read_excel(fileName, sheetName)
gMWindLow = df["DAC + wind low"]/1000
gMWindHigh = df["DAC + wind high"]/1000
gMSolarLow = df["DAC + solar low"]/1000
gMSolarHigh = df["DAC + solar high"]/1000

max1 = max(gASolarHigh) + 150/1000
max2 = max(gMSolarHigh) + 150/1000

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

plt.subplot(gs1[0])
#plt.title("(c) Ammonia - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.title("a Ammonia", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 1)
plt.xlim(0,index[len(index)-1]+2)
plt.scatter(index[0:l], gASMRCCS[0:l], facecolors = "#A78DD8", edgecolors = "#52318E", marker = "d", s = 15, zorder = 2)
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")
plt.ylim(0, max1)
ax = plt.gca()
plt.yticks(np.arange(0,max1,1))
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xticks([])


plt.subplot(gs1[2])
#plt.title("(b) Ammonia - H$_\mathrm{2}$ solar", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.title("b", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 1)
plt.scatter(index[0:l], gASolar[0:l], marker = "h", facecolors = "#FB7B71", edgecolors = "#B71205", s = 15, zorder = 2)
plt.plot(index[0:l], gASolarLow[0:l], color = '#FB7B71', zorder = 0, linewidth = 0.5)
plt.plot(index[0:l], gASolarHigh[0:l], color = '#FB7B71', zorder = 0, linewidth = 0.5)
plt.fill_between(index[0:l], gASolarHigh[0:l], gASolarLow[0:l], facecolor = '#FB7B71', alpha = 0.15, zorder = 0)
mid = round(len(index)/2)+1
yerr = np.array([gASolar[mid:mid+1] - gASolarLow[mid:mid+1], gASolarHigh[mid:mid+1] - gASolar[mid:mid+1]])
plt.errorbar(index[mid:mid+1], gASolar[mid:mid+1], yerr, color = '#B71205', fmt = "none", capsize = 2, 
             elinewidth = 0.5, zorder = 1)
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")
plt.ylim(0, max1)
plt.yticks(np.arange(0,max1,1))
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xticks([])


plt.subplot(gs1[4])
#plt.title("(a) Ammonia - H$_\mathrm{2}$ wind", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.title("c", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 1)
plt.scatter(index[0:l], gAWind[0:l], marker = "^", facecolors = "#6DD2EA", edgecolors = "#167F99", s = 15, zorder = 2)
plt.plot(index[0:l], gAWindLow[0:l], color = '#6DD2EA', zorder = 0, linewidth = 0.5)
plt.plot(index[0:l], gAWindHigh[0:l], color = '#6DD2EA', zorder = 0, linewidth = 0.5)
plt.fill_between(index[0:l], gAWindHigh[0:l], gAWindLow[0:l], facecolor = '#6DD2EA', alpha = 0.15, zorder = 0)
mid = round(len(index)/2)+1
yerr = np.array([gAWind[mid:mid+1] - gAWindLow[mid:mid+1], gAWindHigh[mid:mid+1] - gAWind[mid:mid+1]])
plt.errorbar(index[mid:mid+1], gAWind[mid:mid+1], yerr, color = '#167F99', fmt = "none", capsize = 2, 
             elinewidth = 0.5, zorder = 1)
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")
plt.ylim(0, max1)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xticks([])
plt.yticks(np.arange(0,max1,1))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
plt.xlim(0,index[len(index)-1]+1)

plt.subplot(gs1[1])
#plt.title("(f) Methanol - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.title("d Methanol", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 1)
plt.xlim(0,index[len(index)-1]+2)
plt.scatter(index[0:l], gMSMRCCS[0:l], facecolors = "#A78DD8", edgecolors = "#52318E", marker = "d", s = 15, zorder = 2)
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")
plt.ylim(0, max2)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xticks([])

plt.subplot(gs1[3])
#plt.title("(e) Methanol - H$_\mathrm{2}$ solar", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.title("e", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 1)
plt.scatter(index[0:l], gMSolar[0:l], marker = "h", facecolors = "#FB7B71", edgecolors = "#B71205", s = 15, zorder = 2)
plt.plot(index[0:l], gMSolarLow[0:l], color = '#FB7B71', zorder = 0, linewidth = 0.5)
plt.plot(index[0:l], gMSolarHigh[0:l], color = '#FB7B71', zorder = 0, linewidth = 0.5)
plt.fill_between(index[0:l], gMSolarHigh[0:l], gMSolarLow[0:l], facecolor = '#FB7B71', alpha = 0.15, zorder = 0)
mid = round(len(index)/2)+1
yerr = np.array([gMSolar[mid:mid+1] - gMSolarLow[mid:mid+1], gMSolarHigh[mid:mid+1] - gMSolar[mid:mid+1]])
plt.errorbar(index[mid:mid+1], gMSolar[mid:mid+1], yerr, color = '#B71205', fmt = "none", capsize = 2, 
             elinewidth = 0.5, zorder = 1)
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")
plt.ylim(0, max2)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xticks([])

plt.subplot(gs1[5])
#plt.title("(d) Methanol - H$_\mathrm{2}$ wind", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.title("f", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 1)
plt.scatter(index[0:l], gMWind[0:l], marker = "^", facecolors = "#6DD2EA", edgecolors = "#167F99", s = 15, zorder = 2)
plt.plot(index[0:l], gMWindLow[0:l], color = '#6DD2EA', zorder = 0, linewidth = 0.5)
plt.plot(index[0:l], gMWindHigh[0:l], color = '#6DD2EA', zorder = 0, linewidth = 0.5)
plt.fill_between(index[0:l], gMWindHigh[0:l], gMWindLow[0:l], facecolor = '#6DD2EA', alpha = 0.15, zorder = 0)
mid = round(len(index)/2)+1
yerr = np.array([gMWind[mid:mid+1] - gMWindLow[mid:mid+1], gMWindHigh[mid:mid+1] - gMWind[mid:mid+1]])
plt.errorbar(index[mid:mid+1], gMWind[mid:mid+1], yerr, color = '#167F99', fmt = "none", capsize = 2, 
             elinewidth = 0.5, zorder = 1)
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")
plt.ylim(0, max2)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xticks([])
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
plt.xlim(0,index[len(index)-1]+1)


legend_elements = [Line2D([0], [0], marker='s', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "black",
                                             label = 'Fossil ammonia', markersize = 5),
                   Line2D([0], [0], marker='D', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "black",
                                             label = 'Fossil methanol', markersize = 5),
                   Line2D([0], [0], marker='d', color = "none", 
                                             markerfacecolor ='#A78DD8', markeredgecolor = "#52318E",
                                             label = 'H$_\mathrm{2}$ SMR$_\mathrm{CCS}$', markersize = 5),
                   Line2D([0], [0], marker='h', color = "none", 
                                             markerfacecolor ='#FB7B71', markeredgecolor = "#B71205",
                                             label = 'H$_\mathrm{2}$ solar', markersize = 5),
                   Line2D([0], [0], marker='^', color = "none", 
                                             markerfacecolor ='#6DD2EA', markeredgecolor = "#167F99",
                                             label = 'H$_\mathrm{2}$ wind', markersize = 5)]

fig.legend(handles = legend_elements, frameon = False, loc = "upper center", ncol = 5, 
           prop={"size":8}, bbox_to_anchor=(0.5, 0.08), handletextpad = 0.1)

plt.savefig('Figure 2.jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure 2.svg', dpi=600, format='svg', bbox_inches="tight")


