# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:02:05 2022

@author: anabera
"""


from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(9.5,7.5), dpi=96)

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Hydrogen"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]
CBiomass = df["CO2 Biomass"]
CWind = df["CO2 Wind"]
CSolar = df["CO2 Solar"]
CNuclear = df["CO2 Nuclear"]

sheetName = "Hydrogen high low"
df = pd.read_excel(fileName, sheetName)
CWindLow = df["CO2 Wind low"]
CWindHigh = df["CO2 Wind high"]
#CSolar = df["CO2 Solar"]
CNuclearLow = df["CO2 Nuclear low"]
CNuclearHigh = df["CO2 Nuclear high"]



l = len(times)
labels = times[0:l]
for i in range(0,len(times)-4):
    if i == 0 or i % 3 == 0:
        labels[i] = times[i]
    else:
        labels[i] = ""
    
plt.plot(index[0:l-3], CWind[0:l-3], color = "green", linewidth = 2)
#plt.plot(times, CSolar, color = "orange", linewidth = 2)
plt.plot(index[0:l-3], CNuclear[0:l-3], color = "red", linewidth = 2)
plt.plot(index[0:l-3], CBiomass[0:l-3], color = "blue", linewidth = 2)
plt.xlim(0, 47)
plt.hlines(0, 0, 47, linestyles = "--", color = "black")
plt.fill_between(index[0:l-3], CWindLow[0:l-3], CWindHigh[0:l-3], color = "green", alpha = 0.2)
plt.fill_between(index[0:l-3], CNuclearLow[0:l-3], CNuclearHigh[0:l-3], color = "red", alpha = 0.2)
a = plt.ylim()
plt.ylabel("Avoidance cost [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")
plt.xticks(index[0:l-3], labels[0:l-3], rotation = 45)
plt.twinx()
plt.plot(index[0:l-3], NGprices[0:l-3], color = "black")
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
plt.scatter(index[0:l-3], NGprices[0:l-3], color = "black")
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)
plt.title("Hydrogen")
