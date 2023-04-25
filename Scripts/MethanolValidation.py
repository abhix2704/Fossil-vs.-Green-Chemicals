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
import numpy as np
import scipy.stats

plt.rcParams.update({'font.size': 8})
plt.rcParams['font.family'] = 'Arial'
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(fig_length[2],fig_height*0.35))

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Methanol MP"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
methanex = df["Methanex"]/1000
mmsa = df["MMSA"]/1000
methanexUS = df["Methanex (US)"]/1000
mmsaUS = df["MMSA (US)"]/1000
modelEUR = df["Model (EUR)"]/1000
modelUS = df["Model (US)"]/1000

l = len(times)
labels = times

mi = []
miLabels = []
ma = []
maLabels = []

for i in range(0,len(times)):
    if i == 0 or i % 24 == 0:
        labels[i] = times[i]
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
        
legends1 = ["ICIS (PC)", "Model"]
legends = ["Methanex", "Model"]

plt.subplot(1,2,1)
plt.title("a Time evolution", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.xticks(index, labels)
plt.scatter(index,methanex, marker = "8", facecolor = "#f69c58", edgecolor = "#c75c0b", s = 15, zorder = 0)
plt.scatter(index, modelEUR, facecolor = "white", edgecolor = "black", marker = "D", s = 15, zorder = 1)
plt.ylabel("Production cost or market price [USD kg$^\mathrm{-1}$]")
ax = plt.gca()
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xlim(-2,index[len(index)-1]+3)
plt.legend(legends, loc = "upper left", frameon = False)

plt.subplot(1,2,2)
plt.title("b Validation", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(methanex[0:78],modelEUR[0:78], s = 15, facecolor = "white", edgecolor = "black")
plt.ylabel("Market price [USD kg$^\mathrm{-1}$]")
plt.xlabel("Production cost (model) [USD kg$^\mathrm{-1}$]")
ax = plt.gca()
ax.xaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))

from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score, mean_absolute_error
#rint(r2_score(bloomberg[6:23],modelEUR[6:23]))
error = mean_absolute_percentage_error(modelEUR[0:78], methanex[0:78])
error2 = mean_absolute_percentage_error(modelEUR, methanex)

legends3 = "MAPE = " + str(round(error2*100,1)) + "%"

coeff = scipy.stats.pearsonr(modelEUR[0:78], methanex[0:78])[0]
legends2 = "r = " + str(round(coeff,4))
plt.text(250/1000, 350/1000, legends2)
plt.text(250/1000, 300/1000, legends3)

coeff2 = scipy.stats.pearsonr(modelEUR, methanex)[0]
print(coeff2)


"""
plt.subplot(1,2,2)
plt.title("(b) Model (United States)", y = 0.95, color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.xticks(index, labels, rotation = 45)
plt.plot(index,methanexUS, "--", color = "#03045e")
plt.plot(index,mmsaUS, "-.", color = "#ff7b00")
plt.plot(index,modelUS, color = "#03071e")
plt.legend(legends, loc = "lower right")
plt.xlim(0,index[len(index)-1]+2)
"""
plt.savefig('Methanol validation.svg', dpi=600, bbox_inches='tight')
plt.savefig('Methanol validation.jpg', dpi=600, bbox_inches='tight')

"""
plt.subplot(3,2,4)
plt.title("(d) Biomass", y = 0.9, color = "blue", fontsize = 18)
plt.plot(index[0:l-3], market[0:l-3], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.plot(index[0:l-3], gABiomassCCS[0:l-3], color = "blue", linewidth = 2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.ylim(a)
plt.ylabel("Ammonia price [\$ t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l-3]), (NGprices[l-4], NGprices[l-3]), color = "black", linewidth = 2)
plt.plot((index[l-3], index[l-2]), (NGprices[l-3], NGprices[l-2]), color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)

plt.subplot(3,2,5)
plt.title("(e) H$_\mathrm{2}$ SMR + CCS", y = 0.9, color = "#420169", fontsize = 18)
plt.plot(index[0:l-3], market[0:l-3], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.plot(index[0:l-3], gASMRCCS[0:l-3], color = "#420169", linewidth = 2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.ylabel("Ammonia price [\$ t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l-3]), (NGprices[l-4], NGprices[l-3]), color = "black", linewidth = 2)
plt.plot((index[l-3], index[l-2]), (NGprices[l-3], NGprices[l-2]), color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
plt.ylim(b[0], 4000)
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)



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
plt.ylabel("Ammonia price [\$ t$^\mathrm{-1}$]")
plt.xticks(Aindex, labels, rotation = 45)
plt.title("(f) Model validation", y = 0.9, fontsize = 18)
labelsLegend = ["Market", "Model"]
plt.legend(labelsLegend)
"""