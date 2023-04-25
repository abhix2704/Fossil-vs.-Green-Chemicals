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
BAUprices = df["BAU price"]
windPrices1 = df["DAC + wind + BAU ethylene"]
windPrices2 = df["DAC + wind + gEthylene"]
solarPrices1 = df["DAC + solar + BAU ethylene"]
solarPrices2 = df["DAC + solar + gEthylene"]
CO2avoidance1 = df["CO2 DAC + wind + BAU ethylene"]
CO2avoidance2 = df["CO2 DAC + wind + gEthylene"]

sheetName = "Propanol high low"
df = pd.read_excel(fileName, sheetName)
windPricesLow = df["DAC + wind + BAU ethylene low"]
windPricesHigh = df["DAC + wind + BAU ethylene high"]
solarPricesLow = df["DAC + solar + BAU ethylene low"]
solarPricesHigh = df["DAC + solar + BAU ethylene high"]
CO2avoidanceLow = df["CO2 DAC + wind + BAU ethylene low"]
CO2avoidanceHigh = df["CO2 DAC + wind + BAU ethylene high"]
gWindPricesLow = df["DAC + wind + gEthylene low"]
gWindPricesHigh = df["DAC + wind + gEthylene high"]
gSolarPricesLow = df["DAC + solar + gEthylene low"]
gSolarPricesHigh = df["DAC + solar + gEthylene high"]
gCO2avoidanceLow = df["CO2 DAC + wind + gEthylene low"]
gCO2avoidanceHigh = df["CO2 DAC + wind + gEthylene high"]

xmin = 0
xmax = 5000
ymin = 1000
ymax = 5500

highest2022 = 345*13.1
lowest2022 = 67.542*13.1
secondHalf2021 = 40*13.1
start2021 = 17.709*13.1
current2022 = 232.1*13.1
NGCat = np.array([highest2022, lowest2022, secondHalf2021, start2021, current2022])
NGLabels = ["NG - highest - 2022", "NG - lowest - 2022", "NG - late - 2021", "NG - early - 2021", 
              "NG - Sep' - 2022"]

plt.subplot(1, 1, 1)
plt.plot(NGprices, BAUprices, color = "black")
plt.plot(NGprices, windPrices1, color = "blue")
plt.plot(NGprices, windPricesLow, color = "blue", linestyle = '--')
plt.plot(NGprices, windPricesHigh, color = "blue", linestyle = '-.')
plt.plot(NGprices, windPrices2, color = "green")
plt.plot(NGprices, solarPrices1, color = "purple")
plt.plot(NGprices, solarPricesLow, color = "purple", linestyle = '--')
plt.plot(NGprices, solarPricesHigh, color = "purple", linestyle = '-.')
plt.plot(NGprices, solarPrices2, color = "orange")
#plt.fill_between(NGprices, windPricesHigh, windPricesLow, facecolor = 'blue', alpha = 0.2)
#plt.fill_between(NGprices, gWindPricesHigh, gWindPricesLow, facecolor = 'green', alpha = 0.2)
#plt.plot(NGprices, CO2avoidance())
plt.xlabel("Natural gas price [$/t]")
plt.ylabel("Propanol price [$/t]")
plt.xlim(xmin, xmax)
plt.ylim(ymin,ymax)

plt.text(NGprices[xmax/100] - 100, BAUprices[xmax/100] + 50, "BAU")
plt.text(NGprices[xmax/100] - 1300, windPrices1[len(windPrices1) - 1] - 400, "DAC + wind electrolysis + BAU ethylene", 
         color = "blue", rotation = 3.5)
plt.text(NGprices[xmax/100] - 1300, windPrices2[len(windPrices2) - 1] - 1100, "DAC + wind electrolysis + green ethylene", 
         color = "green", rotation = 10)
plt.text(NGprices[xmax/100] - 1300, solarPrices1[len(solarPrices1) - 1] - 400, "DAC + solar electrolysis + BAU ethylene", 
         color = "purple", rotation = 3.5)
plt.text(NGprices[xmax/100] - 1300, solarPrices2[len(solarPrices2) - 1] - 1100, "DAC + solar electrolysis + green ethylene", 
         color = "orange", rotation = 10)

plt.vlines(NGCat, ymin, ymax, colors = "grey", linestyles = "--", linewidth = 1.5)
for i in range(0,len(NGLabels)):
    plt.text(NGCat[i] + 50, ymax - 1000, NGLabels[i], rotation = 90, fontsize = 14, color = "grey")

"""
plt.subplot(1, 2, 2)
ymin = -100
ymax = 400
plt.plot(NGprices, CO2avoidance1, color = "blue")
plt.plot(NGprices, CO2avoidance2, color = "green")
plt.fill_between(NGprices, CO2avoidanceHigh, CO2avoidanceLow, facecolor = 'blue', alpha = 0.2)
plt.fill_between(NGprices, gCO2avoidanceHigh, gCO2avoidanceLow, facecolor = 'green', alpha = 0.2)
plt.hlines(0, xmin, xmax, color = "black", linestyles="--")
plt.xlabel("Natural gas price [$/t]")
plt.ylabel("CO$_\mathrm{2}$ avoidance costs [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")
plt.xlim(0, xmax)

plt.text(NGprices[xmax/100] - 2100, CO2avoidance1[(len(CO2avoidance1)-1)/2] - 30, "DAC + wind electrolysis + BAU ethylene", 
         color = "blue", rotation = -28)
plt.text(NGprices[xmax/100] - 2000, CO2avoidance1[(len(CO2avoidance1)-1)/2] + 250, "DAC + wind electrolysis + green ethylene", 
         color = "green", rotation = -1)

plt.ylim(ymin,ymax)
"""

plt.show()
