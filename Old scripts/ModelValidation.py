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
fig = plt.figure(figsize=(19,10), dpi=96)

fileName = "Model validation.xlsx"

sheetName = "Ammonia validation"
df = pd.read_excel(fileName, sheetName)
Aindex = df["Index"]
Atimes = df["Time"]
AlitPrice = df["Lit price"]
ABAUPrice = df["BAU price"]

sheetName = "Methanol validation"
df = pd.read_excel(fileName, sheetName)
Mindex = df["Index"]
Mtimes = df["Time"]
MlitPrice = df["Lit price"]
MBAUPrice = df["BAU price"]

l = len(Atimes)
labels = Atimes[0:l]
for i in range(0,len(Atimes)):
    if i == 0 or i % 2 == 0:
        labels[i] = Atimes[i]
    else:
        labels[i] = ""
        
plt.subplot(1,2,1)
plt.plot(Aindex, AlitPrice, "--", color = "black", linewidth = 2)
plt.plot(Aindex, ABAUPrice, color = "black", linewidth = 2)
#plt.plot(times, CSolar, color = "orange", linewidth = 2)
plt.ylabel("Ammonia price [\$ t$^\mathrm{-1}$]")
plt.xticks(Aindex, labels, rotation = 45)
plt.title("Ammonia")
labelsLegend = ["Market", "Model"]
plt.legend(labelsLegend)

l = len(Mtimes)
labels = Mtimes[0:l]
for i in range(0,len(Mtimes)):
    if i == 0 or i % 2 == 0:
        labels[i] = Mtimes[i]
    else:
        labels[i] = ""
        
plt.subplot(1,2,2)
plt.plot(Mindex, MlitPrice, "--", color = "black", linewidth = 2)
plt.plot(Mindex, MBAUPrice, color = "black", linewidth = 2)
#plt.plot(times, CSolar, color = "orange", linewidth = 2)
plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")
plt.xticks(Mindex, labels, rotation = 45)
plt.title("Methanol")
labelsLegend = ["Market", "Model"]
plt.legend(labelsLegend)
plt.ylim([200,450])