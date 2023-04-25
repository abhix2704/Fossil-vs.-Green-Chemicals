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

sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
NGprices = df["NG price"]
BAUprices = df["BAU"]
biomassPrices = df["Biomass"]
windPrices = df["Wind"]
solarPrices = df["Solar"]
nuclearPrices = df["Nuclear"]
prices = np.array([windPrices[0],solarPrices[0],nuclearPrices[0],biomassPrices[0]])
CO2ABiomass = df["CO2 Biomass"]
CO2AWind = df["CO2 Wind"]
CO2ASolar = df["CO2 Solar"]
CO2ANuclear = df["CO2 Nuclear"]

myLabelsY = ["Wind", "Solar", "Nuclear", "Biomass"]
colors = ["green", "orange", "red", "blue"]

sheetName = "Ammonia high low"
df = pd.read_excel(fileName, sheetName)
windLow = df["Wind low"]
windHigh = df["Wind high"]
solarLow = df["Solar low"]
solarHigh = df["Solar high"]
nuclearLow = df["Nuclear low"]
nuclearHigh = df["Nuclear high"]
pricesSe = np.array([windPrices[0],solarPrices[0],nuclearPrices[0], biomassPrices[0]])
pricesLow = np.array([windLow[0], solarLow[0], nuclearLow[0], biomassPrices[0]])
pricesHigh = np.array([windHigh[0], solarHigh[0], nuclearHigh[0], biomassPrices[0]])
markers = ["X", "*", "p", "h"]
myLabels = ["BAU","Wind", "Solar", "Nuclear", "Biomass"]

xScatter = [2130,3745,1850,825]
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
for xp, c in zip(prices, colors):
    plt.hlines(xp, xmin, xmax, linestyles = "--", linewidth = 1.5, color = c)
plt.legend(myLabels, ncol = 5)
plt.vlines(NGCat, min(BAUprices), max(BAUprices), linestyles = "--", linewidth = 1.5, color = "black")
for yp, x1, x2, c in zip(xScatter, pricesLow, pricesHigh, colors):
    plt.vlines(yp, x1, x2, linestyles = "-.", linewidth = 1.5, color = c)

for xp, yp, m, c in zip(xScatter, pricesLow, markers, colors):
    plt.scatter(xp,yp, marker = m, color = c, s = 150)    
for xp, yp, m, c in zip(xScatter, pricesHigh, markers, colors):
    plt.scatter(xp,yp, marker = m, color = c, s = 150)  
for xp, yp, m, c in zip(xScatter, pricesSe, markers, colors):
    plt.scatter(xp,yp, marker = m, color = c, s = 150)  



for i in range(0,len(myLabelsY)):
    plt.text(1200, prices[i] + 20, myLabelsY[i], fontsize = 14, color = colors[i])

for j in range(0,len(myLabelsX)):
    plt.text(NGCat[j] + 40, 1750, myLabelsX[j], fontsize = 14, rotation = 90)
    

plt.xlim(xmin, xmax)
plt.ylim(min(BAUprices), max(BAUprices))
plt.xlabel("Natural gas price [\$ t$^\mathrm{-1}$]")
plt.ylabel("Ammonia price [\$ t$^\mathrm{-1}$]")

plt.subplot(1,2,2)
plt.plot(NGprices, CO2AWind, linewidth = 1.5, color = "green", linestyle = "--")
plt.plot(NGprices, CO2ANuclear, linewidth = 1.5, color = "red", linestyle = "--")
plt.plot(NGprices, CO2ABiomass, linewidth = 1.5, color = "blue", linestyle = "--")
plt.hlines(0, xmin, xmax, linestyles = "--", linewidth = 1.5, color = "black")
plt.xlim(xmin, xmax)
plt.xlabel("Natural gas price [\$ t$^\mathrm{-1}$]")
plt.ylabel("CO$_\mathrm{2}$ avoidance costs [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")
plt.show()
