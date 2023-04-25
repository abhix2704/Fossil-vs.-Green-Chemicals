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
from matplotlib.lines import Line2D

plt.rcParams.update({'font.size': 8})
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(fig_length[1],fig_height*0.35))

fileName = "Prices sensitivity 2.xlsx"
sheetName = "DAC"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
CO2 = df["CO2"]/1000
CO2Low = df["Low"]/1000
CO2High = df["High"]/1000

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

NGindex = [0,3,7,12,15,19,24,27,31,36,39,43,46]


plt.subplot(1,1,1)
#plt.plot(index[NGindex], CO2[NGindex], linewidth = 1.5, color = "#000000", zorder = 1)
plt.scatter(index[NGindex], CO2[NGindex], marker = "o", facecolors = "#ffffff", edgecolors = "#000000", s = 15, zorder = 2)
yerr = np.array([CO2 - CO2Low[NGindex], CO2High[NGindex] - CO2[NGindex]])
#plt.errorbar(index[NGindex], CO2[NGindex], yerr, color = '#808080', fmt = "None", capsize = 2, elinewidth = 0.5, zorder = 0)
plt.fill_between(index[NGindex], CO2Low[NGindex], CO2High[NGindex], color = "000000", alpha = 0.1, zorder = 0)
plt.plot(index[NGindex], CO2Low[NGindex], linewidth = 0.5, color = "#000000", zorder = 1)
plt.plot(index[NGindex], CO2High[NGindex], linewidth = 0.5, color = "#000000", zorder = 1)
mid = 24
yerr = np.array([CO2[mid:mid+1] - CO2Low[mid:mid+1], CO2High[mid:mid+1] - CO2[mid:mid+1]])
plt.errorbar(index[mid:mid+1], CO2[mid:mid+1], yerr, color = '#000000', fmt = "none", capsize = 2, 
             elinewidth = 0.5, zorder = 1)
plt.ylabel("Price [USD kg$^\mathrm{-1}$]")
ax = plt.gca()
ax.set_xticks(ma, labels = maLabels)
ax.set_xticks(mi, minor=True)
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
plt.xlim(-1,index[len(index)-1]+2)

legend_elements = [Line2D([0], [0], marker='s', color='w', label='Electricity',
                                             markerfacecolor='#ee9b00', markersize = 6),]
plt.savefig('Figure S4.png', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure S4.svg', dpi=600, format='svg', bbox_inches="tight")


