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
gs1.update(wspace = 0.075, hspace = 0.25)

fileName = "Prices regionalization.xlsx"

sheetName = "BAU methanol"
BAUMdf = pd.read_excel(fileName, sheetName)

sheetName = "Wind methanol"
windMdf = pd.read_excel(fileName, sheetName)

sheetName = "Solar methanol"
solarMdf = pd.read_excel(fileName, sheetName)

l = len(BAUMdf["$/ton"])
labels = BAUMdf["$/ton"]

mi = []
miLabels = []
ma = []
maLabels = []
for i in range(0,l):
    if i == 0 or i % 24 == 0:
        labels[i] = BAUMdf["$/ton"][i]
        ma.append(i + 1)
        maLabels.append(labels[i])
    elif i % 2 == 0 and i % 24 != 0:
        labels[i] = ""
        mi.append(i + 1)
        miLabels.append(labels[i])

labels[l-3] = ""
labels[l-2] = ""
labels[l-1] = "Nov '22"
ma.append(i + 1)
maLabels.append(labels[l-1])

NGindex = [0,3,7,12,15,19,24,27,31,36,39,43,46]


index = BAUMdf.Index

plt.suptitle('Methanol', color = "black", fontsize = fontsize_title, fontweight = "bold", y = 0.93)

plt.subplot(gs1[0])
plt.title("a Denmark", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUMdf.Denmark[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUMdf.Denmark[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 2)

plt.plot(index[NGindex], windMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windMdf.Denmark[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windMdf.Denmark[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 3.5)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels, rotation = 45)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.yticks([])
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[1])
plt.title("b Germany", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUMdf.Germany[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUMdf.Germany[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 2)

plt.plot(index[NGindex], solarMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarMdf.Germany[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarMdf.Germany[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "-")
plt.scatter(index[NGindex], windMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windMdf.Germany[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windMdf.Germany[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 3.5)
ax = plt.gca()
#ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels, rotation = 45)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
plt.yticks([])
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[2])
plt.title("c France", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUMdf.France[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUMdf.France[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 2)

plt.plot(index[NGindex], solarMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarMdf.France[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarMdf.France[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windMdf.France[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windMdf.France[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 3.5)
ax = plt.gca()
#ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels, rotation = 45)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
plt.yticks([])
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[3])
plt.title("d Sweden", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUMdf.Sweden[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUMdf.Sweden[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 2)

plt.plot(index[NGindex], windMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windMdf.Sweden[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windMdf.Sweden[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 3.5)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.yticks([])
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[4])
plt.title("e Italy", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUMdf.Italy[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUMdf.Italy[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 2)

plt.plot(index[NGindex], solarMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarMdf.Italy[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarMdf.Italy[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windMdf.Italy[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windMdf.Italy[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 3.5)
ax = plt.gca()
#ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.xticks([])
plt.yticks([])
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[5])
plt.title("f Turkey", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUMdf.Turkey[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUMdf.Turkey[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 2)

plt.plot(index[NGindex], solarMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarMdf.Turkey[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarMdf.Turkey[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windMdf.Turkey[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windMdf.Turkey[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 3.5)
ax = plt.gca()
#ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
#ax.set_xticks(ma, labels = maLabels)
#ax.set_xticks(mi, minor=True)
plt.xticks([])
plt.yticks([])
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[6])
plt.title("g Spain", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUMdf.Spain[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUMdf.Spain[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 2)

plt.plot(index[NGindex], solarMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarMdf.Spain[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarMdf.Spain[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)

plt.plot(index[NGindex], windMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], windMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "^", s = 15, zorder = 4)
plt.plot(index[NGindex], windMdf.Spain[NGindex]/1000, color = "#167F99", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], windMdf.Spain[NGindex]/1000, facecolors = "#6DD2EA", edgecolors = "#167F99", marker = "^", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 3.5)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.xticks([])
#plt.yticks([])
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")

plt.subplot(gs1[8])
plt.title("h Netherlands", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index[NGindex], BAUMdf.Netherlands[NGindex]/1000, color = "black", linewidth = 1.5, zorder = 1, linestyle = "-")
plt.scatter(index[NGindex], BAUMdf.Netherlands[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", marker = "D", s = 15, zorder = 2)

plt.plot(index[NGindex], solarMdf.Europe[NGindex]/1000, color = "#808080", linewidth = 1.5, zorder = 3, linestyle = "--")
plt.scatter(index[NGindex], solarMdf.Europe[NGindex]/1000, facecolors = "#ffffff", edgecolors = "#808080", marker = "h", s = 15, zorder = 4)
plt.plot(index[NGindex], solarMdf.Netherlands[NGindex]/1000, color = "#B71205", linewidth = 1.5, zorder = 5, linestyle = "-")
plt.scatter(index[NGindex], solarMdf.Netherlands[NGindex]/1000, facecolors = "#FB7B71", edgecolors = "#B71205", marker = "h", s = 15, zorder = 6)
plt.xlim(-1,index[len(index)-1]+2)
plt.ylim(0, 3.5)
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
#plt.xticks([])
plt.yticks([])
#plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")


legend_elements = [Line2D([0], [0], marker='D', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "black",
                                             label = 'Fossil methanol', markersize = 5),
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


plt.savefig('Figure regionalization methanol.jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure regionalization methanol.svg', dpi=600, format='svg', bbox_inches="tight")

