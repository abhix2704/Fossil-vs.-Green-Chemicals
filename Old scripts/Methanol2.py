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

sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]
market = df["Market"]
BAUprices = df["BAU"]
gABiomassCCS = df["DAC + biomass"]
gAWind = df["DAC + wind"]
gASolar = df["DAC + solar"]
gANuclear = df["DAC + nuclear"]
gASMRCCS = df["SMR CCS"]

sheetName = "Methanol high low"
df = pd.read_excel(fileName, sheetName)
gAWindLow = df["DAC + wind low"]
gAWindHigh = df["DAC + wind high"]
gASolarLow = df["DAC + solar low"]
gASolarHigh = df["DAC + solar high"]
gANuclearLow = df["DAC + nuclear low"]
gANuclearHigh = df["DAC + nuclear high"]

l = len(times)
labels = times
for i in range(0,len(times)-4):
    if i == 0 or i % 3 == 0:
        labels[i] = times[i]
    else:
        labels[i] = ""

plt.subplot(3,2,1)
plt.title("(a) Wind", y = 0.9, color = "green", fontsize = 18)
plt.plot(index[0:l-3], market[0:l-3], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.plot(index[0:l-3], gAWind[0:l-3], color = "green", linewidth = 2)
plt.fill_between(index[0:l-3], gAWindLow[0:l-3], gAWindHigh[0:l-3], color = "green", alpha = 0.2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.xlim(0,index[len(index)-1]+2)
a = plt.ylim()
plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l-3]), (NGprices[l-4], NGprices[l-3]), color = "black", linewidth = 2)
plt.plot((index[l-3], index[l-2]), (NGprices[l-3], NGprices[l-2]), color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
b = plt.ylim()
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)

plt.subplot(3,2,2)
plt.title("(b) Solar", y = 0.9, color = "orange", fontsize = 18)
plt.plot(index[0:l-3], market[0:l-3], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.plot(index[0:l-3], gASolar[0:l-3], color = "orange", linewidth = 2)
plt.fill_between(index[0:l-3], gASolarLow[0:l-3], gASolarHigh[0:l-3], color = "orange", alpha = 0.2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l-3]), (NGprices[l-4], NGprices[l-3]), color = "black", linewidth = 2)
plt.plot((index[l-3], index[l-2]), (NGprices[l-3], NGprices[l-2]), color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
plt.ylim(b[0],4275)
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)

plt.subplot(3,2,3)
plt.title("(c) Nuclear", y = 0.9, color = "red", fontsize = 18)
plt.plot(index[0:l-3], market[0:l-3], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.plot(index[0:l-3], gANuclear[0:l-3], color = "red", linewidth = 2)
plt.fill_between(index[0:l-3], gANuclearLow[0:l-3], gANuclearHigh[0:l-3], color = "red", alpha = 0.2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.ylim(a)
plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")
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

plt.subplot(3,2,4)
plt.title("(d) Biomass", y = 0.9, color = "blue", fontsize = 18)
plt.plot(index[0:l-3], market[0:l-3], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.plot(index[0:l-3], gABiomassCCS[0:l-3], color = "blue", linewidth = 2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.ylim(a)
plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")
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
plt.title("(e) H$_\mathrm{2}$ SMR + CCS", y = 0.9, color = "indigo", fontsize = 18)
plt.plot(index[0:l-3], market[0:l-3], "--", color = "brown", linewidth = 2)
plt.plot(index[0:l-3], BAUprices[0:l-3], color = "black")
plt.plot(index[0:l-3], gASMRCCS[0:l-3], color = "indigo", linewidth = 2)
plt.arrow(index[l-6]+0.1, BAUprices[l-6]+100, -1, 0, head_width = 30, head_length = 0.5, color = "black")
plt.xlim(0,index[len(index)-1]+2)
plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")
plt.xticks(index, labels, rotation = 45)
plt.twinx()
plt.scatter(index, NGprices, color = "black", linestyle = "--")
plt.plot((index[l-4], index[l-3]), (NGprices[l-4], NGprices[l-3]), color = "black", linewidth = 2)
plt.plot((index[l-3], index[l-2]), (NGprices[l-3], NGprices[l-2]), color = "black", linewidth = 2)
plt.plot((index[l-2], index[l-1]), (NGprices[l-2], NGprices[l-1]), color = "black", linewidth = 2)
plt.arrow(index[l-4], NGprices[l-4], 1, 0, head_width = 40, head_length = 0.5, color = "black")
plt.ylim(b[0],4350)
ax = plt.gca()
ax.yaxis.set_label_coords(0.1,0.95)
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", x = 0.97)

"""
fileName = "Model validation.xlsx"

sheetName = "Methanol validation"
df = pd.read_excel(fileName, sheetName)
Mindex = df["Index"]
Mtimes = df["Time"]
MlitPrice = df["Lit price"]
MBAUPrice = df["BAU price"]

l = len(Mtimes)
labels = Mtimes[0:l]
for i in range(0,len(Mtimes)):
    if i == 0 or i % 2 == 0:
        labels[i] = Mtimes[i]
    else:
        labels[i] = ""
        
plt.subplot(3,2,6)
plt.plot(Mindex, MlitPrice, "--", color = "black", linewidth = 2)
plt.plot(Mindex, MBAUPrice, color = "black", linewidth = 2)
#plt.plot(times, CSolar, color = "orange", linewidth = 2)
plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")
plt.xticks(Mindex, labels, rotation = 45)
plt.title("Model validation", y = 0.9, fontsize = 18)
labelsLegend = ["Market", "Model"]
plt.legend(labelsLegend)
plt.ylim([200,450])
"""