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

sheetName = "Propanol"
df = pd.read_excel(fileName, sheetName)
NGprices = df["NG price"]
BAUprices = df["BAU"]
windBPrices = df["DAC + wind + BAU ethylene"]
solarBPrices = df["DAC + solar + BAU ethylene"]
nuclearBPrices = df["DAC + nuclear + BAU ethylene"]
windGPrices = df["DAC + wind + gEthylene"]
solarGPrices = df["DAC + solar + gEthylene"]
nuclearGPrices = df["DAC + nuclear + gEthylene"]

CO2ABWind = df["CO2 DAC + wind + BAU ethylene"]
CO2ABSolar = df["CO2 DAC + solar + BAU ethylene"]
CO2ABNuclear = df["CO2 DAC + nuclear + BAU ethylene"]
CO2AGWind = df["CO2 DAC + wind + gEthylene"]
CO2AGSolar = df["CO2 DAC + solar + gEthylene"]
CO2AGNuclear = df["CO2 DAC + nuclear + gEthylene"]

myLabelsY = ["Wind", "Nuclear"]
colors = ["green", "red"]
"""
sheetName = "Methanol high low"
df = pd.read_excel(fileName, sheetName)
windLow = df["DAC + wind low"]
windHigh = df["DAC + wind high"]
solarLow = df["DAC + solar low"]
solarHigh = df["DAC + solar high"]
nuclearLow = df["DAC + nuclear low"]
nuclearHigh = df["DAC + nuclear high"]
"""

markers = ["X", "p"]
myLabels = ["BAU","DAC + wind + BAU ethylene", "DAC + solar + BAU ethylene", "DAC + nuclear + BAU ethylene",
            "DAC + wind + gEthylene", "DAC + solar + gEthylene", "DAC + nuclear + gEthylene"]

xScatter = [4923,345*13.1]
yScatter = [2581,2455]
pricesLow = [2351.2049,2270.8320]
pricesHigh = [3307.2597,2629.0233]
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
plt.plot(NGprices, windBPrices, color = "green", linewidth = 1.5, linestyle = "--")
plt.plot(NGprices, solarBPrices, color = "orange", linewidth = 1.5, linestyle = "--")
plt.plot(NGprices, nuclearBPrices, color = "red", linewidth = 1.5, linestyle = "--")
#plt.plot(NGprices, windGPrices, color = "green", linewidth = 1.5)
#plt.plot(NGprices, solarGPrices, color = "orange", linewidth = 1.5)
#plt.plot(NGprices, nuclearGPrices, color = "red", linewidth = 1.5)

plt.legend(myLabels, ncol = 2)
plt.vlines(NGCat, min(BAUprices), 3500, linestyles = "--", linewidth = 1.5, color = "black")

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

plt.text(900, 2150, "DAC + wind electrolysis + BAU ethylene", 
         color = "green", rotation = 14, fontsize = 14)
plt.text(900, 2625, "DAC + solar electrolysis + BAU ethylene", 
         color = "orange", rotation = 14, fontsize = 14)
plt.text(900, 2075, "DAC + nuclear electrolysis + BAU ethylene", 
         color = "red", rotation = 14, fontsize = 14)

for j in range(0,len(myLabelsX)):
    plt.text(NGCat[j] + 40, 1600, myLabelsX[j], fontsize = 14, rotation = 90)
   

plt.xlim(xmin, xmax)
plt.ylim(min(BAUprices), 3500)
plt.xlabel("Natural gas price [\$ t$^\mathrm{-1}$]")
plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")


plt.subplot(1,2,2)
plt.plot(NGprices, CO2ABWind, linewidth = 1.5, color = "green", linestyle = "--")
plt.plot(NGprices, CO2ABNuclear, linewidth = 1.5, color = "red", linestyle = "--")
plt.plot(NGprices, CO2ABSolar, linewidth = 1.5, color = "orange", linestyle = "--")
#plt.plot(NGprices, CO2AGWind, linewidth = 1.5, color = "green")
#plt.plot(NGprices, CO2AGNuclear, linewidth = 1.5, color = "red")
#plt.plot(NGprices, CO2AGSolar, linewidth = 1.5, color = "orange")
plt.hlines(0, xmin, xmax, linestyles = "--", linewidth = 1.5, color = "black")
plt.xlim(xmin, xmax)
plt.xlabel("Natural gas price [\$ t$^\mathrm{-1}$]")
plt.ylabel("CO$_\mathrm{2}$ avoidance costs [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")

plt.show()
