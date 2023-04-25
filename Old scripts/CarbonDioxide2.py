# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:02:05 2022

@author: anabera
"""


from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

fig_length = {1:   3.50394,    # 1 column
          1.5: 5.35433, # 1.5 columns
          2:   7.20472}    # 2 columns
fig_height = 9.72441 # maxium height
fontsize_title = 9
fontsize_label = 8
fontsize_legend = 8
fontsize_axs = 8

plt.rcParams.update({'font.size': 8})
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(fig_length[2],fig_height*0.75))

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]
CBiomass = df["CO2 Biomass"]
CWind = df["CO2 Wind"]
CSolar = df["CO2 Solar"]
CNuclear = df["CO2 Nuclear"]
CSMRCCS = df["CO2 SMR CCS"]

sheetName = "Ammonia high low"
df = pd.read_excel(fileName, sheetName)
CWindLow = df["CO2 Wind low"]
CWindHigh = df["CO2 Wind high"]
CSolarLow = df["CO2 Solar low"]
CSolarHigh = df["CO2 Solar high"]
CNuclearLow = df["CO2 Nuclear low"]
CNuclearHigh = df["CO2 Nuclear high"]

sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
NGprices = df["NG price"]
CMBiomass = df["CO2 DAC + biomass"]
CMWind = df["CO2 DAC + wind"]
CMSolar = df["CO2 DAC + solar"]
CMNuclear = df["CO2 DAC + nuclear"]
CMSMRCCS = df["CO2 SMR CCS"]

sheetName = "Methanol high low"
df = pd.read_excel(fileName, sheetName)
CMWindLow = df["CO2 DAC + wind low"]
CMWindHigh = df["CO2 DAC + wind high"]
CMSolarLow = df["CO2 DAC + solar low"]
CMSolarHigh = df["CO2 DAC + solar high"]
CMNuclearLow = df["CO2 DAC + nuclear low"]
CMNuclearHigh = df["CO2 DAC + nuclear high"]

l = len(times)
labels = times[0:l]
for i in range(0,len(times)-4):
    if i == 0 or i % 3 == 0:
        labels[i] = times[i]
    else:
        labels[i] = ""
    
plt.subplot(2,1,1)
plt.scatter(index[0:l-3], CWind[0:l-3], color = "#007f5f", marker = "^")
plt.scatter(index[0:l-3], CSolar[0:l-3], color = "#f26419", marker = "h")
#plt.scatter(index[0:l-3], CNuclear[0:l-3], color = "#da5552", linewidth = 2)
#plt.scatter(index[0:l-3], CBiomass[0:l-3], color = "blue", linewidth = 2)
plt.scatter(index[0:l-3], CSMRCCS[0:l-3], color = "#420169", marker = "X")
plt.xlim(0, 47)
plt.hlines(0, 0, 47, linestyles = "--", color = "black")
#plt.fill_between(index[0:l-3], CWindLow[0:l-3], CWindHigh[0:l-3], color = "green", alpha = 0.2)
#plt.fill_between(index[0:l-3], CSolarLow[0:l-3], CSolarHigh[0:l-3], color = "orange", alpha = 0.2)
#plt.fill_between(index[0:l-3], CNuclearLow[0:l-3], CNuclearHigh[0:l-3], color = "#da5552", alpha = 0.2)
yerr = np.array([CWind[0:l-3] - CWindLow[0:l-3], CWindHigh[0:l-3] - CWind[0:l-3]])
plt.errorbar(index[0:l-3], CWind[0:l-3], yerr, color = '#007f5f', fmt = "^", linewidth = 0.75, capsize = 2)
yerr = np.array([CSolar[0:l-3] - CSolarLow[0:l-3], CSolarHigh[0:l-3] - CSolar[0:l-3]])
plt.errorbar(index[0:l-3], CSolar[0:l-3], yerr, color = '#f26419', fmt = "h", linewidth = 0.75, capsize = 2)
ax = plt.gca()
a = ax.get_ylim()
plt.ylabel("Avoidance cost [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")
plt.xticks(index[0:l-3], labels[0:l-3], rotation = 45)
plt.twinx()
#plt.plot(index[0:l-3], NGprices[0:l-3], color = "black")
plt.scatter(index[0:l-3], NGprices[0:l-3], color = "#da5552", s = 20)
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.98)
plt.title("Ammonia", y = 0.93, fontsize = fontsize_title)

plt.subplot(2,1,2)
plt.scatter(index[0:l-3], CMWind[0:l-3], color = "#007f5f", marker = "^")
plt.scatter(index[0:l-3], CMSolar[0:l-3], color = "#f26419", marker = "h")
#plt.scatter(index[0:l-3], CMNuclear[0:l-3], color = "#da5552", linewidth = 2)
#plt.scatter(index[0:l-3], CMBiomass[0:l-3], color = "blue", linewidth = 2)
plt.scatter(index[0:l-3], CMSMRCCS[0:l-3], color = "#420169", marker = "X")
labelsr = ["Wind", "Solar", "SMR + CCS"]
#plt.legend(labelsr, ncol = len(labelsr))
plt.xlim(0, 47)
plt.hlines(0, 0, 47, linestyles = "--", color = "black")
#plt.fill_between(index[0:l-3], CMWindLow[0:l-3], CMWindHigh[0:l-3], color = "green", alpha = 0.2)
#plt.fill_between(index[0:l-3], CMSolarLow[0:l-3], CMSolarHigh[0:l-3], color = "orange", alpha = 0.2)
#plt.fill_between(index[0:l-3], CMNuclearLow[0:l-3], CMNuclearHigh[0:l-3], color = "#da5552", alpha = 0.2)
yerr = np.array([CMWind[0:l-3] - CMWindLow[0:l-3], CMWindHigh[0:l-3] - CMWind[0:l-3]])
plt.errorbar(index[0:l-3], CMWind[0:l-3], yerr, color = '#007f5f', fmt = "^", linewidth = 0.75, capsize = 2)
yerr = np.array([CSolar[0:l-3] - CSolarLow[0:l-3], CSolarHigh[0:l-3] - CSolar[0:l-3]])
plt.errorbar(index[0:l-3], CMSolar[0:l-3], yerr, color = '#f26419', fmt = "h", linewidth = 0.75, capsize = 2)
ax = plt.gca()
a = ax.get_ylim()
plt.ylabel("Avoidance cost [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")
plt.xticks(index[0:l-3], labels[0:l-3], rotation = 45)
plt.twinx()
plt.scatter(index[0:l-3], NGprices[0:l-3], color = "#da5552", s = 20)
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.98)
plt.title("Methanol", y = 0.93, fontsize = fontsize_title)

#plt.savefig('Figure 3.svg', dpi=600, bbox_inches='tight')
#plt.savefig('Figure 3.jpg', dpi=600, bbox_inches='tight')