# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 11:36:02 2022

@author: anabera
"""
from matplotlib import pyplot as plt
import numpy as np


ammoniaProd = 19 # in million ton per annum
methanolProd = 8.8 # in million ton per annum

ammoniaBAU = 1.040
ammoniaWind = 0.712
ammoniaSolar = 1.140
ammoniaNuclear = 0.126

methanolBAU = 0.658
methanolWind = -0.556
methanolSolar = 0.226
methanolNuclear = -0.686


totalAmmoniaWind = (ammoniaBAU - ammoniaWind) * ammoniaProd
totalAmmoniaSolar = -(ammoniaBAU - ammoniaSolar) * ammoniaProd
totalAmmoniaNuclear = (ammoniaBAU - ammoniaNuclear) * ammoniaProd

totalMethanolWind = (methanolBAU - methanolWind) * methanolProd
totalMethanolSolar = (methanolBAU - methanolSolar) * methanolProd
totalMethanolNuclear = (methanolBAU - methanolNuclear) * methanolProd

late2021AmmoniaWind = 2006
currentAmmoniaWind = -1468
late2021AmmoniaSolar = 0
currentAmmoniaSolar = 0
late2021AmmoniaNuclear = 582
currentAmmoniaNuclear = -686

late2021MethanolWind = 758
currentMethanolWind = -205
late2021MethanolSolar = 4267
currentMethanolSolar = 1588
late2021MethanolNuclear = 570
currentMethanolNuclear = -295

myLabels = np.array(["Ammonia - late 2021", "Ammonia - Sep' 2022", "Methanol - late 2021", "Methanol - Sep' 2022"])
plt.rcParams.update({'font.size': 16})

plt.subplot(1,3,1)
x = [0, totalAmmoniaWind, totalAmmoniaWind*2 , totalAmmoniaWind*2+totalMethanolWind]
h = [late2021AmmoniaWind, currentAmmoniaWind, late2021MethanolWind, currentMethanolWind]
w = [totalAmmoniaWind, totalAmmoniaWind, totalMethanolWind, totalMethanolWind]
hatch = ['/', '.O', 'x', '*']
for i in range(0,4):
    plt.bar(x[i], height = h[i], width = w[i], align = 'edge', color = 'green', hatch = hatch[i], label = myLabels[i])
    if i % 2 == 0:
        plt.text(x[i] + w[i]/2 - 0.6, -900, myLabels[i], rotation = 90)
    else:
        plt.text(x[i] + w[i]/2 - 0.6, 100, myLabels[i], rotation = 90)
plt.xlabel("Annual avoidance [Mt$_\mathrm{CO_\mathrm{2eq}}$ yr$^\mathrm{-1}$]")
plt.ylabel("Avoidance cost [\$ t$_\mathrm{CO_\mathrm{2eq}}$$^\mathrm{-1}$]")
plt.title("Wind electricity")
#plt.legend(ncol = 4)
#plt.xlim(0,totalAmmoniaWind*2+totalMethanolWind*2)

plt.subplot(1,3,2)
x = [0, totalAmmoniaSolar, totalAmmoniaSolar*2 , totalAmmoniaSolar*2+totalMethanolSolar]
h = [late2021AmmoniaSolar, currentAmmoniaSolar, late2021MethanolSolar, currentMethanolSolar]
w = [totalAmmoniaSolar, totalAmmoniaSolar, totalMethanolSolar, totalMethanolSolar]
hatch = ['/', '.O', 'x', '*']
for i in range(0,4):
    plt.bar(x[i], height = h[i], width = w[i], align = 'edge', color = 'orange', hatch = hatch[i], label = myLabels[i])
    if i % 2 == 0 and i != 0:
        plt.text(x[i] + w[i]/2 - 0.3, 1700, myLabels[i], rotation = 90)
    elif i % 2 == 1 and i != 1:
        plt.text(x[i] + w[i]/2 - 0.3, 1700, myLabels[i], rotation = 90)
plt.xlabel("Annual avoidance [Mt$_\mathrm{CO_\mathrm{2eq}}$ yr$^\mathrm{-1}$]")
plt.title("Solar electricity")

#plt.legend(ncol = 4)
#plt.xlim(0,totalAmmoniaSolar*2+totalMethanolSolar*2)

plt.subplot(1,3,3)
x = [0, totalAmmoniaNuclear, totalAmmoniaNuclear*2 , totalAmmoniaNuclear*2+totalMethanolNuclear]
h = [late2021AmmoniaNuclear, currentAmmoniaNuclear, late2021MethanolNuclear, currentMethanolNuclear]
w = [totalAmmoniaNuclear, totalAmmoniaNuclear, totalMethanolNuclear, totalMethanolNuclear]
hatch = ['/', '.O', 'x', '*']
for i in range(0,4):
    plt.bar(x[i], height = h[i], width = w[i], align = 'edge', color = 'red', hatch = hatch[i], label = myLabels[i])
    if i % 2 == 0:
        plt.text(x[i] + w[i]/2 - 0.6, -325, myLabels[i], rotation = 90)
    else:
        plt.text(x[i] + w[i]/2 - 0.6, 35, myLabels[i], rotation = 90)
plt.xlabel("Annual avoidance [Mt$_\mathrm{CO_\mathrm{2eq}}$ yr$^\mathrm{-1}$]")
plt.title("Nuclear electricity")
#plt.legend(ncol = 4)
#plt.xlim(0,totalAmmoniaSolar*2+totalMethanolSolar*2)


plt.show()