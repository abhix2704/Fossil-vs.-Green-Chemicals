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
import pandas as pd
from matplotlib.lines import Line2D

plt.rcParams.update({'font.size': 12})
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(fig_length[1.5],fig_height*0.5))

fileName = "Prices sensitivity 2.xlsx"
sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]
elecPrices = df["Electricity"]/1000

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

NGindex = range(0,47)
plt.subplot(1,1,1)
plt.plot(index[NGindex], elecPrices[NGindex], color = "#000000", linewidth = 1.5, zorder = 0, linestyle = "-")
plt.scatter(index[NGindex], elecPrices[NGindex], marker = "o", facecolor = "#ffffff", edgecolor = "#000000", s = 20, zorder = 1)
plt.ylabel("Electricity price [USD kWh$^\mathrm{-1}$]")
ax = plt.gca()
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xlim(0,48)
plt.ylim(0,max(elecPrices)+0.05)

legend_elements = [Line2D([0], [0], marker='s', color='w', label='Electricity',
                                             markerfacecolor='#ee9b00', markersize = 6),]
plt.savefig('Slide 2d.png', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Slide 2d.svg', dpi=600, format='svg', bbox_inches="tight")


