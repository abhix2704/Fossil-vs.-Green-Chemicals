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

plt.rcParams.update({'font.size': 8})
plt.rcParams['font.family'] = 'Arial'
fig = plt.figure(figsize=(fig_length[2], fig_height*0.8))

gs1 = gridspec.GridSpec(3, 3)
gs1.update(wspace = 0.075, hspace = 0.2)

fileName = "Prices regionalization.xlsx"

sheetName = "BAU ammonia"
BAUAdf = pd.read_excel(fileName, sheetName)

sheetName = "Wind ammonia"
windAdf = pd.read_excel(fileName, sheetName)

sheetName = "Solar ammonia"
solarAdf = pd.read_excel(fileName, sheetName)

l = len(BAUAdf["$/ton"])
labels = BAUAdf["$/ton"]

mi = []
miLabels = []
ma = []
maLabels = []
for i in range(0,l):
    if i == 0 or i % 12 == 0:
        labels[i] = BAUAdf["$/ton"][i]
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

NGindex = [0,3,7,12,15,19,24,27,31,36,39,43,46]


index = BAUAdf.Index

plt.suptitle('Ammonia', color = "black", fontsize = fontsize_title, fontweight = "bold", y = 0.93)

plt.subplot(gs1[0])
plt.title("a Denmark", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUAdf.Denmark[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUAdf.Denmark[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 2)

plt.plot(index[NGindex], windAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windAdf.Denmark[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windAdf.Denmark[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 2.7)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels, rotation = 45)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
#plt.yticks([])
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[1])
plt.title("b Germany", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUAdf.Germany[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUAdf.Germany[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 2)

plt.plot(index[NGindex], solarAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarAdf.Germany[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarAdf.Germany[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "-")
plt.scatter(index[NGindex], windAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windAdf.Germany[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windAdf.Germany[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 2.7)
ax = plt.gca()
#ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels, rotation = 45)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
plt.yticks([])
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[2])
plt.title("c France", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUAdf.France[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUAdf.France[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 2)

plt.plot(index[NGindex], solarAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarAdf.France[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarAdf.France[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windAdf.France[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windAdf.France[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 2.7)
ax = plt.gca()
#ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels, rotation = 45)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
plt.yticks([])
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[3])
plt.title("d Sweden", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUAdf.Sweden[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUAdf.Sweden[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 2)

plt.plot(index[NGindex], windAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windAdf.Sweden[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windAdf.Sweden[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 2.7)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
#plt.yticks([])
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[4])
plt.title("e Italy", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUAdf.Italy[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUAdf.Italy[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 2)

plt.plot(index[NGindex], solarAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarAdf.Italy[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarAdf.Italy[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windAdf.Italy[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windAdf.Italy[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 2.7)
ax = plt.gca()
#ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.xticks([])
plt.yticks([])
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[5])
plt.title("f Turkey", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUAdf.Turkey[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUAdf.Turkey[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 2)

plt.plot(index[NGindex], solarAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarAdf.Turkey[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarAdf.Turkey[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windAdf.Turkey[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windAdf.Turkey[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 2.7)
ax = plt.gca()
#ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
plt.yticks([])
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[6])
plt.title("g Spain", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUAdf.Spain[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUAdf.Spain[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 2)

plt.plot(index[NGindex], solarAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarAdf.Spain[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarAdf.Spain[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windAdf.Spain[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windAdf.Spain[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 2.7)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.xticks([])
#plt.yticks([])
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[8])
plt.title("h Netherlands", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUAdf.Netherlands[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUAdf.Netherlands[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "s", s = 15, zorder = 2)

plt.plot(index[NGindex], solarAdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarAdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarAdf.Netherlands[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarAdf.Netherlands[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 2.7)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.xticks([])
plt.yticks([])
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")


legend_elements = [Line2D([0], [0], marker='s', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "black",
                                             label = 'Fossil ammonia', markersize = 5),
                   Line2D([0], [0], marker='h', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "#808080",
                                             label = 'H$_\mathrm{2}$ solar (avg. Europe)', markersize = 5),
                   Line2D([0], [0], marker='^', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "#808080",
                                             label = 'H$_\mathrm{2}$ wind (avg. Europe)', markersize = 5),
                   Line2D([0], [0], marker='h', color = "none", 
                                             markerfacecolor ='#FB7B71', markeredgecolor = "#B71205",
                                             label = 'H$_\mathrm{2}$ solar', markersize = 5),
                   Line2D([0], [0], marker='^', color = "none", 
                                             markerfacecolor ='#6DD2EA', markeredgecolor = "#167F99",
                                             label = 'H$_\mathrm{2}$ wind', markersize = 5)]

fig.legend(handles = legend_elements, frameon = False, loc = "lower right", ncol = 1, 
           prop={"size":8}, bbox_to_anchor=(0.6, 0.175), handletextpad = 0.1)


plt.savefig('Figure regionalization ammonia.jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure regionalization ammonia.svg', dpi=600, format='svg', bbox_inches="tight")

