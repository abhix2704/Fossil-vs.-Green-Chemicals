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
BAUprices = df["BAU price"]
windPrices = df["DAC + wind"]
solarPrices = df["DAC + solar"]
nuclearPrices = df["DAC + nuclear"]
coalPrices = df["Coal"]
CO2avoidance = df["CO2 DAC + wind"]

sheetName = "Methanol high low"
df = pd.read_excel(fileName, sheetName)
windPricesLow = df["DAC + wind low"]
windPricesHigh = df["DAC + wind high"]
solarPricesLow = df["DAC + solar low"]
solarPricesHigh = df["DAC + solar high"]
nuclearPricesLow = df["DAC + nuclear low"]
nuclearPricesHigh = df["DAC + nuclear high"]
CO2avoidanceLow = df["CO2 DAC + wind low"]
CO2avoidanceHigh = df["CO2 DAC + wind high"]

xmin = 0
xmax = 5000
ymin = 0
ymax = max(BAUprices)

highest2022 = 345*13.1
lowest2022 = 67.542*13.1
secondHalf2021 = 40*13.1
start2021 = 17.709*13.1
current2022 = 232.1*13.1
NGCat = np.array([highest2022, lowest2022, secondHalf2021, start2021, current2022])
NGLabels = ["NG - highest - 2022", "NG - lowest - 2022", "NG - late - 2021", "NG - early - 2021", 
              "NG - Sep' - 2022"]

highest2022 = 457.8
lowest2022 = 157.5
coalCat = np.array([highest2022, lowest2022])
coalLabels = ["Coal - highest - 2022", "Coal - lowest - 2022"]

plt.subplot(1, 1, 1)
plt.plot(NGprices, BAUprices, color = "black")
plt.plot(NGprices, windPrices, color = "green")
plt.plot(NGprices, windPricesLow, color = "green", linestyle = "--")
plt.plot(NGprices, windPricesHigh, color = "green", linestyle = "-.")
plt.plot(NGprices, solarPrices, color = "orange")
plt.plot(NGprices, solarPricesLow, color = "orange", linestyle = "--")
plt.plot(NGprices, solarPricesHigh, color = "orange", linestyle = "-.")
plt.plot(NGprices, nuclearPrices, color = "red")
plt.plot(NGprices, nuclearPricesLow, color = "red", linestyle = "--")
plt.plot(NGprices, nuclearPricesHigh, color = "red", linestyle = "-.")
#plt.fill_between(NGprices, windPricesHigh, windPricesLow, facecolor = 'green', alpha = 0.2)
plt.plot(NGprices[0:16], coalPrices[0:16], color = "brown")
plt.plot(NGprices[15:len(NGprices)], coalPrices[15:len(NGprices)], color = "brown", linestyle = "--")
#plt.plot(NGprices, CO2avoidance())
plt.xlabel("Natural gas or coal price [$/t]")
plt.ylabel("Methanol price [$/t]")
plt.xlim(xmin, xmax)
#plt.hlines(coalPrices[15], xmin, xmax, colors = "peru", linestyles = "--")
plt.ylim(ymin,ymax)

plt.text(NGprices[xmax/100] - 100, BAUprices[xmax/100] + 100, "BAU")
plt.text(180, 1000, "Coal", color = "brown")
plt.text(NGprices[xmax/100] + 650, windPrices[len(windPrices) - 1] - 400, "DAC + wind electrolysis", 
         color = "green", rotation = 7)
plt.text(NGprices[xmax/100] + 650, solarPrices[len(solarPrices) - 1] - 400, "DAC + solar electrolysis", 
         color = "orange", rotation = 7)
plt.text(NGprices[xmax/100] + 650, nuclearPrices[len(nuclearPrices) - 1] - 400, "DAC + nuclear electrolysis", 
         color = "red", rotation = 7)

plt.vlines(NGCat, ymin, ymax, colors = "grey", linestyles = "--", linewidth = 1.5)
for i in range(0,len(NGLabels)):
    plt.text(NGCat[i] + 30, ymax - 800, NGLabels[i], rotation = 90, fontsize = 12, color = "grey")
    
plt.vlines(coalCat, ymin, ymax, colors = "peru", linestyles = "--", linewidth = 1.5)
for i in range(0,len(coalLabels)):
    plt.text(coalCat[i] - 80, ymax - 800, coalLabels[i], rotation = 90, fontsize = 12, color = "peru")

"""
plt.subplot(1, 2, 2)
ymin = -1500
ymax = max(CO2avoidance)
plt.plot(NGprices, CO2avoidance, color = "green")
plt.fill_between(NGprices, CO2avoidanceHigh, CO2avoidanceLow, facecolor = 'green', alpha = 0.2)
plt.hlines(0, xmin, xmax, color = "black", linestyles="--")
plt.xlabel("Natural gas price [$/t]")
plt.ylabel("CO$_\mathrm{2}$ avoidance costs [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")
plt.xlim(0, xmax)

plt.text(NGprices[xmax/100], CO2avoidance[(len(CO2avoidance)-1)/2] + 25, "DAC + wind electrolysis", color = "green")

plt.ylim(ymin,ymax)
"""

plt.show()
