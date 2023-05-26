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
fig = plt.figure(figsize=(fig_length[1],fig_height*0.35))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(wspace = 0.075, hspace = 0)



fileName = "Prices regionalization.xlsx"

sheetName = "Wind LCOH 2022"
df = pd.read_excel(fileName, sheetName)
onlyInflationWind = df["Europe"][0:11]
onlyNGWind = df["Europe"][11:22]
inflationNGWind = df["Europe"][22:33]
times = df["LCOH"][0:11]

sheetName = "Solar LCOH 2022"
df = pd.read_excel(fileName, sheetName)
onlyInflationSolar = df["Europe"][0:11]
onlyNGSolar = df["Europe"][11:22]
inflationNGSolar = df["Europe"][22:33]


l = len(times)
labels = times

mi = []
miLabels = []
ma = []
maLabels = []
for i in range(0,len(times)):
    if i == 0 or i % 2 == 0:
        labels[i] = times[i]
        ma.append(i + 1)
        maLabels.append(labels[i])
    else:
        labels[i] = ""
        mi.append(i + 1)
        miLabels.append(labels[i])

labels[l-3] = ""
labels[l-2] = ""
labels[l-1] = "Nov '22"
ma.append(i + 1)
maLabels.append(labels[l-1])

index = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
subIndex = np.array([0, 2, 4, 6, 8, 10])

plt.subplot(gs1[0])
plt.title("Levelised cost of hydrogen", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.plot(index, onlyInflationWind, color = "#167F99", linewidth = 1, zorder = 4, linestyle = "-")
plt.scatter(index[subIndex], onlyInflationWind[subIndex], marker = "^", facecolors = "#6DD2EA", edgecolors = "#167F99", s = 15, zorder = 4)
plt.plot(index, inflationNGWind, color = "#808080", linewidth = 1, zorder = 3, linestyle = "-")
plt.scatter(index[subIndex], inflationNGWind[subIndex + 22], marker = "^", facecolors = "#ffffff", edgecolors = "#808080", s = 15, zorder = 3)
plt.plot(index, onlyInflationSolar, color = "#B71205", linewidth = 1, zorder = 4, linestyle = "-")
plt.scatter(index[subIndex], onlyInflationSolar[subIndex], marker = "h", facecolors = "#FB7B71", edgecolors = "#B71205", s = 15, zorder = 4)
plt.plot(index, inflationNGSolar, color = "#808080", linewidth = 1, zorder = 3, linestyle = "-")
plt.scatter(index[subIndex], inflationNGSolar[subIndex + 22], marker = "h", facecolors = "#ffffff", edgecolors = "#808080", s = 15, zorder = 3)
plt.ylabel("LCOH [USD kg$^\mathrm{-1}$]")
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
plt.xlim(0, index[len(index)-1] + 1)
plt.ylim([5.5,10.5])


legend_elements = [Line2D([0], [0], marker='^', color = "none", 
                                             markerfacecolor ='#6DD2EA', markeredgecolor = "#167F99",
                                             label = 'H$_\mathrm{2}$ wind (only inflation)', markersize = 5),
                   Line2D([0], [0], marker='h', color = "none", 
                                             markerfacecolor ='#FB7B71', markeredgecolor = "#B71205",
                                             label = 'H$_\mathrm{2}$ solar (only inflation)', markersize = 5),
                   Line2D([0], [0], marker='^', color = "none", 
                                            markerfacecolor ='#ffffff', markeredgecolor = "#808080",
                                            label = 'H$_\mathrm{2}$ wind (inflation and NG price)', markersize = 5),
                   Line2D([0], [0], marker='h', color = "none", 
                                            markerfacecolor ='#ffffff', markeredgecolor = "#808080",
                                            label = 'H$_\mathrm{2}$ solar (inflation and NG price)', markersize = 5)]

fig.legend(handles = legend_elements, frameon = False, loc = "upper center", ncol = 2, 
           prop={"size":8}, bbox_to_anchor=(0.5, 0.05), handletextpad = 0.1)

plt.savefig('LCOH NG.jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('LCOH NG.svg', dpi=600, format='svg', bbox_inches="tight")


