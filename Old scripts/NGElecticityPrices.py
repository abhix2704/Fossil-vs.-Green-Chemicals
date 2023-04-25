# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:46:03 2022

@author: anabera
"""

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import matplotlib 

matplotlib.rc('xtick', labelsize=16) 
matplotlib.rc('ytick', labelsize=16) 

fig = plt.figure(figsize=(13.33,7.5), dpi=96)
fileName = "Prices sensitivity 2.xlsx"

sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]
BAUprices = df["BAU"]
elecPrices = df["Electricity"]

l = len(times)
labels = times[0:l]
for i in range(0,len(times)-4):
    if i == 0 or i % 3 == 0:
        labels[i] = times[i]
    else:
        labels[i] = ""
        
plt.plot(index[0:l-3], NGprices[0:l-3], color = "black")
plt.xlim(0,index[len(index)-3])
a = plt.ylim()
plt.ylabel("Natural gas price [\$ t$^\mathrm{-1}$]", fontsize = 18)
plt.xticks(index[0:l-3], labels[0:l-3], rotation = 45, fontsize = 18)
plt.arrow(index[l-10], NGprices[l-10], -1, 0, head_width = 40, head_length = 0.5, color = "black")
plt.twinx()
plt.plot(index[0:l-3], elecPrices[0:l-3], color = "black", linestyle = "--")
ax = plt.gca()
plt.ylabel("Electricity price [\$ MWh$^\mathrm{-1}$]", fontsize = 18)
plt.arrow(index[l-9], elecPrices[l-9], 1, 0, head_width = 6, head_length = 0.5, color = "black")

