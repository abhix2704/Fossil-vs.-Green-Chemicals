# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:02:05 2022

@author: anabera
"""


from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams.update({'font.size': 16})

fileName = "Prices sensitivity.xlsx"

sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
NGprices = df["NG price"]
BAUprices = df["BAU"]
windPrices = df["DAC + wind"]
solarPrices = df["DAC + solar"]
nuclearPrices = df["DAC + nuclear"]
prices = np.array([windPrices,solarPrices,nuclearPrices])
CO2AWind = df["CO2 DAC + wind"]
CO2ASolar = df["CO2 DAC + solar"]
CO2ANuclear = df["CO2 DAC + nuclear"]

myLabelsY = ["Wind", "Solar", "Nuclear"]
colors = ["green", "orange", "red"]

sheetName = "Methanol high low"
df = pd.read_excel(fileName, sheetName)
windLow = df["DAC + wind low"]
windHigh = df["DAC + wind high"]
solarLow = df["DAC + solar low"]
solarHigh = df["DAC + solar high"]
nuclearLow = df["DAC + nuclear low"]
nuclearHigh = df["DAC + nuclear high"]


markers = ["X", "*", "p"]
myLabels = ["BAU","DAC + wind", "DAC + solar", "DAC + nuclear"]

xScatter = [2595,4307,2301]
yScatter = [2024,3223,1808]
pricesLow = [1454.2495,1673.2388,1337.17013]
pricesHigh = [3573.9280,5494.5652,2303.7918]
xmin = 0
xmax = 5000

highest2022 = 345*13.1
lowest2022 = 67.542*13.1
secondHalf2021 = 40*13.1
start2021 = 17.709*13.1
current2022 = 232.1*13.1
NGCat = np.array([highest2022, lowest2022, secondHalf2021, start2021, current2022])
myLabelsX = ["Highest - 2022", "Lowest - 2022", "Late - 2021", "Early - 2021", 
              "Sep' - 2022"]

plt.subplot(1,2,1)
plt.plot(NGprices, BAUprices, color = "black", linewidth = 1.5)
plt.plot(NGprices, windPrices, color = "green", linewidth = 1.5, linestyle = "--")
plt.plot(NGprices, solarPrices, color = "orange", linewidth = 1.5, linestyle = "--")
plt.plot(NGprices, nuclearPrices, color = "red", linewidth = 1.5, linestyle = "--")
plt.legend(myLabels, ncol = 4)
plt.vlines(NGCat, min(BAUprices), max(BAUprices), linestyles = "--", linewidth = 1.5, color = "black")
for yp, x1, x2, c in zip(xScatter, pricesLow, pricesHigh, colors):
    plt.vlines(yp, x1, x2, linestyles = "-.", linewidth = 1.5, color = c)

for xp, yp, m, c in zip(xScatter, pricesLow, markers, colors):
    plt.scatter(xp,yp, marker = m, color = c, s = 150)    
for xp, yp, m, c in zip(xScatter, pricesHigh, markers, colors):
    plt.scatter(xp,yp, marker = m, color = c, s = 150)  
for xp, yp, m, c in zip(xScatter, yScatter, markers, colors):
    plt.scatter(xp,yp, marker = m, color = c, s = 150)  


"""
for i in range(0,len(myLabelsY)):
    plt.text(1200, prices[i] + 20, myLabelsY[i], fontsize = 14, color = colors[i])
"""
plt.text(850, 1765, "DAC + wind electrolysis", 
         color = "green", rotation = 14, fontsize = 14)
plt.text(850, 2690, "DAC + solar electrolysis", 
         color = "orange", rotation = 14, fontsize = 14)
plt.text(850, 1615, "DAC + nuclear electrolysis", 
         color = "red", rotation = 14, fontsize = 14)
for j in range(0,len(myLabelsX)):
    plt.text(NGCat[j] + 40, 1000, myLabelsX[j], fontsize = 14, rotation = 90)
    

plt.xlim(xmin, xmax)
plt.ylim(min(BAUprices), max(BAUprices))
plt.xlabel("Natural gas price [\$ t$^\mathrm{-1}$]")
plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")


plt.subplot(1,2,2)
plt.plot(NGprices, CO2AWind, linewidth = 1.5, color = "green", linestyle = "--")
plt.plot(NGprices, CO2ANuclear, linewidth = 1.5, color = "red", linestyle = "--")
plt.plot(NGprices, CO2ASolar, linewidth = 1.5, color = "orange", linestyle = "--")
plt.hlines(0, xmin, xmax, linestyles = "--", linewidth = 1.5, color = "black")
plt.xlim(xmin, xmax)
plt.xlabel("Natural gas price [\$ t$^\mathrm{-1}$]")
plt.ylabel("CO$_\mathrm{2}$ avoidance costs [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")

plt.show()
