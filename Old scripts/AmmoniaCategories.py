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
coalPrices = df["Coal"]
windCO2avoidance = df["CO2 Wind"]
biomassCO2avoidance = df["CO2 Biomass"]
solarCO2avoidance = df["CO2 Solar"]
nuclearCO2avoidance = df["CO2 Nuclear"]

sheetName = "Ammonia high low"
df = pd.read_excel(fileName, sheetName)
windPricesLow = df["Wind low"]
windPricesHigh = df["Wind high"]
solarPricesLow = df["Solar low"]
solarPricesHigh = df["Solar high"]
nuclearPricesLow = df["Nuclear low"]
nuclearPricesHigh = df["Nuclear high"]
CO2avoidanceLow = df["CO2 Wind low"]
CO2avoidanceHigh = df["CO2 Wind high"]

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
myLabels = ["BAU", "Wind electrolysis", "Coal"]
NGLabels = ["NG - highest - 2022", "NG - lowest - 2022", "NG - late - 2021", "NG - early - 2021", 
              "NG - Sep' - 2022"]

highest2022 = 457.8
lowest2022 = 157.5
coalCat = np.array([highest2022, lowest2022])
coalLabels = ["Coal - highest - 2022", "Coal - lowest - 2022"]

plt.plot(NGprices, BAUprices, color = "black")
plt.plot(NGprices, windPrices, color = "green")
plt.hlines(windPricesLow.tail(1), xmin, xmax, color = "green", linestyles = '--')
plt.hlines(windPricesHigh.tail(1), xmin, xmax, color = "green", linestyles = '-.')
#plt.fill_between(NGprices, windPricesHigh, windPricesLow, facecolor = 'green', alpha = 0.2)
plt.plot(NGprices, biomassPrices, color = "blue")
plt.plot(NGprices, solarPrices, color = "orange")
plt.hlines(solarPricesLow.tail(1), xmin, xmax, color = "orange", linestyles = '--')
plt.hlines(solarPricesHigh.tail(1), xmin, xmax, color = "orange", linestyles = '-.')
#.fill_between(NGprices, solarPricesHigh, solarPricesLow, facecolor = 'orange', alpha = 0.2)
plt.plot(NGprices, nuclearPrices, color = "red")
plt.hlines(nuclearPricesLow.tail(1), xmin, xmax, color = "red", linestyles = '--')
plt.hlines(nuclearPricesHigh.tail(1), xmin, xmax, color = "red", linestyles = '-.')
#plt.fill_between(NGprices, nuclearPricesHigh, nuclearPricesLow, facecolor = 'red', alpha = 0.2)
#plt.fill_between(NGprices, windPricesHigh, windPricesLow, facecolor = 'green', alpha = 0.2)
plt.plot(NGprices[0:16], coalPrices[0:16], color = "brown")
plt.plot(NGprices[15:len(NGprices)], coalPrices[15:len(NGprices)], color = "brown", linestyle = "--")
#plt.plot(NGprices[10:len(NGprices)], coalPrices[10:len(coalPrices)], color = "brown", linestyle = '--')
#plt.plot(NGprices, CO2avoidance())
plt.xlabel("Natural gas or coal price [$/t]")
plt.ylabel("Ammonia price [$/t]")
plt.xlim(xmin, xmax)
#plt.vlines(1390, ymin, ymax, color = "black", linestyles = "--", linewidth = 1.5 )
#plt.hlines(coalPrices[15], xmin, xmax, colors = "peru", linestyles = "--")
plt.ylim(ymin,ymax)

plt.text(NGprices[xmax/100] - 100, BAUprices[xmax/100], "BAU")
plt.text(250, 900, "Coal", color = "brown")
plt.text(NGprices[xmax/100]-50, windPrices[len(windPrices) - 1] + 25, "Wind electrolysis", color = "green")
plt.text(NGprices[xmax/100]-50, solarPrices[len(solarPrices) - 1] + 25, "Solar electrolysis", color = "orange")
plt.text(NGprices[xmax/100]-50, biomassPrices[len(biomassPrices) - 1] + 25, "Biomass electrolysis", color = "blue")
plt.text(NGprices[xmax/100]-50, nuclearPrices[len(nuclearPrices) - 1] + 25, "Nuclear electrolysis", color = "red")


plt.vlines(NGCat, ymin, ymax, colors = "grey", linestyles = "--", linewidth = 1.5)
for i in range(0,len(NGLabels)):
    plt.text(NGCat[i] + 30, ymax - 800, NGLabels[i], rotation = 90, fontsize = 12, color = "grey")
    
plt.vlines(coalCat, ymin, ymax, colors = "peru", linestyles = "--", linewidth = 1.5)
for i in range(0,len(coalLabels)):
    plt.text(coalCat[i] - 80, ymax - 800, coalLabels[i], rotation = 90, fontsize = 12, color = "peru")
"""
plt.subplot(1, 2, 2)
ymin = -5000
ymax = max(solarCO2avoidance)
plt.plot(NGprices, windCO2avoidance, color = "green")
plt.plot(NGprices, biomassCO2avoidance, color = "blue")
plt.plot(NGprices, solarCO2avoidance, color = "orange")
plt.plot(NGprices, nuclearCO2avoidance, color = "red")
#plt.fill_between(NGprices, CO2avoidanceHigh, CO2avoidanceLow, facecolor = 'green', alpha = 0.2)
plt.hlines(0, xmin, xmax, color = "black", linestyles="--")
plt.xlabel("Natural gas price [$/t]")
plt.ylabel("CO$_\mathrm{2}$ avoidance costs [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")
plt.xlim(0, xmax)
#plt.vlines(1390, ymin, ymax, color = "black", linestyles = "--", linewidth = 1.5 )

plt.text(NGprices[xmax/100], windCO2avoidance[(len(windCO2avoidance)-1)/2] + 25, "Wind electrolysis", color = "green")
plt.text(NGprices[xmax/100], solarCO2avoidance[(len(solarCO2avoidance)-1)/2] + 25, "Solar electrolysis", color = "orange")
plt.text(NGprices[xmax/100], windCO2avoidance[(len(windCO2avoidance)-1)/2] + 25, "Wind electrolysis", color = "green")
plt.text(NGprices[xmax/100], windCO2avoidance[(len(windCO2avoidance)-1)/2] + 25, "Wind electrolysis", color = "green")

plt.ylim(ymin,ymax)
"""

plt.show()
