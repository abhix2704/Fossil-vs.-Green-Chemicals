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
from matplotlib.lines import Line2D


plt.rcParams.update({'font.size': 8})
plt.rcParams['font.family'] = 'Arial'
fig = plt.figure(figsize=(fig_length[2],fig_height*0.7))
gs1 = gridspec.GridSpec(2, 2)
gs1.update(wspace = 0.075, hspace = 0.1)

fileName = "Prices regionalization.xlsx"

sheetName = "US"
USdf = pd.read_excel(fileName, sheetName)

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Ammonia"
EURAdf = pd.read_excel(fileName, sheetName)
NGprices = EURAdf["NG price"]/1000
BAUAprices = EURAdf["BAU"]/1000
gAWind = EURAdf["Wind"]/1000
gASolar = EURAdf["Solar"]/1000

sheetName = "Methanol"
EURMdf = pd.read_excel(fileName, sheetName)
BAUMprices = EURMdf["BAU"]/1000
gMWind = EURMdf["DAC + wind"]/1000
gMSolar = EURMdf["DAC + solar"]/1000

l = len(USdf.Time)
labels = USdf.Time

mi = []
miLabels = []
ma = []
maLabels = []
for i in range(0,len(USdf.Time)):
    if i == 0 or i % 12 == 0:
        labels[i] = USdf.Time[i]
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

plt.subplot(gs1[0])
#plt.title("(c) Ammonia - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.title("a Europe", color = "black", fontsize = fontsize_title, fontweight = "bold")


plt.plot(USdf.Index[NGindex], BAUAprices[NGindex], color = "black", linewidth = 1, zorder = 1, linestyle = "-")
plt.scatter(USdf.Index[NGindex], BAUAprices[NGindex], facecolors = "#ffffff", edgecolors = "black", 
            marker = "s", s = 15, zorder = 2)


plt.plot(USdf.Index[NGindex][NGindex], gASolar[NGindex], 
         color = "#B71205", linewidth = 1, zorder = 3, linestyle = "-")
plt.scatter(USdf.Index[NGindex][NGindex], gASolar[NGindex], 
            marker = "h", facecolors = "#FB7B71", edgecolors = "#B71205", s = 15, zorder = 4)


plt.plot(USdf.Index[NGindex], gAWind[NGindex], color = "#167F99", linewidth = 1, zorder = 5, linestyle = "-")
plt.scatter(USdf.Index[NGindex], gAWind[NGindex], marker = "^", facecolors = "#6DD2EA", 
            edgecolors = "#167F99", s = 15, zorder = 6)


plt.ylabel("Ammonia production cost [USD kg$^\mathrm{-1}$]")
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))

plt.xlim(-1,USdf.Index[len(USdf.Index)-1]+2)
plt.ylim([0, 2.7])
plt.xticks([])

plt.subplot(gs1[1])
#plt.title("(c) Ammonia - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.title("b United States", color = "black", fontsize = fontsize_title, fontweight = "bold")


plt.plot(USdf.Index[NGindex], USdf.BAUAmmonia[NGindex]/1000, color = "black", linewidth = 1, zorder = 1, linestyle = "-")
plt.scatter(USdf.Index[NGindex], USdf.BAUAmmonia[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", 
            marker = "s", s = 15, zorder = 2)


plt.plot(USdf.Index[NGindex][NGindex], USdf.SolarAmmonia[NGindex]/1000, 
         color = "#B71205", linewidth = 1, zorder = 3, linestyle = "-")
plt.scatter(USdf.Index[NGindex][NGindex], USdf.SolarAmmonia[NGindex]/1000, 
            marker = "h", facecolors = "#FB7B71", edgecolors = "#B71205", s = 15, zorder = 4)


plt.plot(USdf.Index[NGindex], USdf.WindAmmonia[NGindex]/1000, color = "#167F99", linewidth = 1, zorder = 5, linestyle = "-")
plt.scatter(USdf.Index[NGindex], USdf.WindAmmonia[NGindex]/1000, marker = "^", facecolors = "#6DD2EA", 
            edgecolors = "#167F99", s = 15, zorder =6)


ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xlim(-1,USdf.Index[len(USdf.Index)-1]+2)
plt.ylim([0, 2.7])
plt.yticks([])
plt.xticks([])



plt.subplot(gs1[2])
#plt.title("(c) Ammonia - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", color = "black", fontsize = fontsize_title, fontweight = "bold")

plt.plot(USdf.Index[NGindex], BAUMprices[NGindex], color = "black", linewidth = 1, zorder = 1, linestyle = "-")
plt.scatter(USdf.Index[NGindex], BAUMprices[NGindex], facecolors = "#ffffff", edgecolors = "black", 
            marker = "D", s = 15, zorder = 2)


plt.plot(USdf.Index[NGindex][NGindex], gMSolar[NGindex], 
         color = "#B71205", linewidth = 1, zorder = 3, linestyle = "-")
plt.scatter(USdf.Index[NGindex][NGindex], gMSolar[NGindex], 
            marker = "h", facecolors = "#FB7B71", edgecolors = "#B71205", s = 15, zorder = 4)


plt.plot(USdf.Index[NGindex], gMWind[NGindex], color = "#167F99", linewidth = 1, zorder = 5, linestyle = "-")
plt.scatter(USdf.Index[NGindex], gMWind[NGindex], marker = "^", facecolors = "#6DD2EA", 
            edgecolors = "#167F99", s = 15, zorder = 6)


ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
plt.xlim(-1,USdf.Index[len(USdf.Index)-1]+2)
plt.ylim([0, 3])
plt.ylabel("Methanol production cost [USD kg$^\mathrm{-1}$]")


plt.subplot(gs1[3])
#plt.title("(c) Ammonia - H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", color = "black", fontsize = fontsize_title, fontweight = "bold")


plt.plot(USdf.Index[NGindex], USdf.BAUMethanol[NGindex]/1000, color = "black", linewidth = 1, zorder = 3, linestyle = "-")
plt.scatter(USdf.Index[NGindex], USdf.BAUMethanol[NGindex]/1000, facecolors = "#ffffff", edgecolors = "black", 
            marker = "D", s = 15, zorder = 4)


plt.plot(USdf.Index[NGindex][NGindex], USdf.SolarMethanol[NGindex]/1000, 
         color = "#B71205", linewidth = 1, zorder = 9, linestyle = "-")
plt.scatter(USdf.Index[NGindex][NGindex], USdf.SolarMethanol[NGindex]/1000, 
            marker = "h", facecolors = "#FB7B71", edgecolors = "#B71205", s = 15, zorder = 10)



plt.plot(USdf.Index[NGindex], USdf.WindMethanol[NGindex]/1000, color = "#167F99", linewidth = 1, zorder = 13, linestyle = "-")
plt.scatter(USdf.Index[NGindex], USdf.WindMethanol[NGindex]/1000, marker = "^", facecolors = "#6DD2EA", 
            edgecolors = "#167F99", s = 15, zorder = 14)

ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
plt.xlim(-1,USdf.Index[len(USdf.Index)-1]+2)
plt.ylim([0, 3])
plt.yticks([])


legend_elements = [Line2D([0], [0], marker='s', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "black",
                                             label = 'Fossil ammonia', markersize = 5), 
                   Line2D([0], [0], marker='D', color = "none", 
                                            markerfacecolor ='#ffffff', markeredgecolor = "black",
                                            label = 'Fossil methanol', markersize = 5), 
                   Line2D([0], [0], marker='h', color = "none", 
                                             markerfacecolor ='#FB7B71', markeredgecolor = "#B71205",
                                             label = 'H$_\mathrm{2}$ solar', markersize = 5),            
                   Line2D([0], [0], marker='^', color = "none", 
                                             markerfacecolor ='#6DD2EA', markeredgecolor = "#167F99",
                                             label = 'H$_\mathrm{2}$ wind', markersize = 5)
                   ]

fig.legend(handles = legend_elements, frameon = False, loc = "upper center", ncol = 4, 
           prop={"size":8}, bbox_to_anchor=(0.5, 0.05), handletextpad = 0.1)

plt.savefig('Figure regionalization country.jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure regionalization country.svg', dpi=600, format='svg', bbox_inches="tight")


