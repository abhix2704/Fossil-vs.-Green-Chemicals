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
from matplotlib import ticker as tk
import scipy.stats

plt.rcParams.update({'font.size': 8})
plt.rcParams['font.family'] = 'Arial'
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(fig_length[2],fig_height*0.35))

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Ammonia MP"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
ICIS = df["ICIS"]/1000
bloomberg = df["Bloomberg"]/1000
modelEUR = df["Model (EUR)"]/1000
NGindex = [0,3,7,12,15,19,24,27,31,36,39,43,46]

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
        
legends1 = ["Green Markets\u00AE", "Model"]

plt.subplot(1,2,1)
plt.title("a Time evolution", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.xticks(index, labels)
plt.scatter(index, bloomberg, marker = "8", facecolor = "#f69c58", edgecolor = "#c75c0b", s = 15, zorder = 0)
plt.scatter(index, modelEUR, facecolor = "white", edgecolor = "black", marker = "s", s = 15, zorder = 1)
plt.ylabel("Production cost or market price [USD kg$^\mathrm{-1}$]")
ax = plt.gca()
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xlim(-1,index[len(index)-1]+2)
plt.legend(legends1, loc = "upper left", frameon = False)

plt.subplot(1,2,2)
plt.title("b Validation", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(modelEUR[6:43], bloomberg[6:43], s = 15, facecolor = "white", edgecolor = "black")
plt.ylabel("Market price [USD kg$^\mathrm{-1}$]")
plt.xlabel("Production cost (model) [USD kg$^\mathrm{-1}$]")
ax = plt.gca()
ax.xaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
"""
xlim,ylim =plt.xlim(), plt.ylim()
minx = min(*xlim, *ylim)
maxx = max(*xlim,*ylim)
plt.xlim(minx, maxx)
plt.ylim(minx, maxx)
plt.plot([minx, maxx], [minx, maxx], "--k")
SSR = ((modelEUR[6:23] - bloomberg[6:23])**2).sum()
SST = ((bloomberg[6:23] - bloomberg[6:23].mean())**2).sum()
R2_manual = 1 - SSR/SST
print(R2_manual, "coamscoascmsa")
"""
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score, mean_absolute_error
#rint(r2_score(bloomberg[6:23],modelEUR[6:23]))
error = mean_absolute_percentage_error(bloomberg[6:43],modelEUR[6:43])

coeff = scipy.stats.pearsonr(modelEUR[6:43], bloomberg[6:43])[0]
legends2 = "r = " + str(round(coeff,4))
legends3 = "MAPE = " + str(round(error*100,1)) + "%"
plt.text(400/1000, 2000/1000, legends2)
plt.text(400/1000, 1500/1000, legends3)


plt.savefig('Ammonia validation.svg', dpi=600, bbox_inches='tight')
plt.savefig('Ammonia validation.png', dpi=600, bbox_inches='tight')
