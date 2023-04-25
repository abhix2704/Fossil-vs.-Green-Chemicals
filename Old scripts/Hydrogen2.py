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
fig = plt.figure(figsize=(18.5,12.5), dpi=96)

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Hydrogen"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]
BAUprices = df["BAU"]
gABiomassCCS = df["Biomass"]
gAWind = df["Wind"]
gASolar = df["Solar"]
gANuclear = df["Nuclear"]

sheetName = "Hydrogen high low"
df = pd.read_excel(fileName, sheetName)
gAWindLow = df["Wind low"]
gAWindHigh = df["Wind high"]
gASolarLow = df["Solar low"]
gASolarHigh = df["Solar high"]
gANuclearLow = df["Nuclear low"]
gANuclearHigh = df["Nuclear high"]

l = len(times)
labels = times
for i in range(0,len(times)-4):
    if i == 0 or i % 3 == 0:
        labels[i] = times[i]
    else:
        labels[i] = ""

plt.subplot(2,2,1)
plt.title("Wind", y = 0.9, color = "green", fontsize = 18)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.plot(index[0:l-3], gAWind[0:l-3], color = "green", linewidth = 2)
plt.fill_between(index[0:l-3], gAWindLow[0:l-3], gAWindHigh[0:l-3], color = "green", alpha = 0.2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 200, head_length = 0.5, color = "black")
plt.xlim(0,index[len(index)-1]+2)
a = plt.ylim()
plt.ylabel("Hydrogen price [\$ t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l-3]), (NGprices[l-4], NGprices[l-3]), "--", color = "black", linewidth = 2)
plt.plot((index[l-3], index[l-2]), (NGprices[l-3], NGprices[l-2]), "--", color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), "--", color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
b = plt.ylim()
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)

plt.subplot(2,2,2)
plt.title("Solar", y = 0.9, color = "orange", fontsize = 18)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.plot(index[0:l-3], gASolar[0:l-3], color = "orange", linewidth = 2)
plt.xlim(0,index[len(index)-1]+2)
plt.fill_between(index[0:l-3], gASolarLow[0:l-3], gASolarHigh[0:l-3], color = "orange", alpha = 0.2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 200, head_length = 0.5, color = "black")
plt.ylabel("Hydrogen price [\$ t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l-3]), (NGprices[l-4], NGprices[l-3]), "--", color = "black", linewidth = 2)
plt.plot((index[l-3], index[l-2]), (NGprices[l-3], NGprices[l-2]), "--", color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), "--", color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
plt.ylim(b[0], 3500)
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)

plt.subplot(2,2,3)
plt.title("Nuclear", y = 0.9, color = "red", fontsize = 18)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.plot(index[0:l-3], gANuclear[0:l-3], color = "red", linewidth = 2)
plt.xlim(0,index[len(index)-1]+2)
plt.fill_between(index[0:l-3], gANuclearLow[0:l-3], gANuclearHigh[0:l-3], color = "red", alpha = 0.2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 200, head_length = 0.5, color = "black")
plt.ylim(a)
plt.ylabel("Hydrogen price [\$ t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l-3]), (NGprices[l-4], NGprices[l-3]), "--", color = "black", linewidth = 2)
plt.plot((index[l-3], index[l-2]), (NGprices[l-3], NGprices[l-2]), "--", color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), "--", color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)

plt.subplot(2,2,4)
plt.title("Biomass", y = 0.9, color = "blue", fontsize = 18)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.plot(index[0:l-3], gABiomassCCS[0:l-3], color = "blue", linewidth = 2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 200, head_length = 0.5, color = "black")
plt.ylim(a)
plt.ylabel("Hydrogen price [\$ t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l-3]), (NGprices[l-4], NGprices[l-3]), "--", color = "black", linewidth = 2)
plt.plot((index[l-3], index[l-2]), (NGprices[l-3], NGprices[l-2]), "--", color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), "--", color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)

