# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:04:27 2022

@author: anabera
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fileName = "Methanol breakdown.xlsx"


colors = ["#da5552","#7371fc","#ffd60a","#60d394","#ee9b00","#94d2bd","#005f73",
            "#fec89a"]

sheetName = "Summary"
df = pd.read_excel(fileName, sheetName)
categories = ["Natural gas", "Water", "Nitrogen / CO$_\mathrm{2}$", "Hydrogen", "Electricity", "Other utilities", "Fixed costs", "CAPEX"]
naturalGas = df["Natural gas"]
myLabels = list(range(1, len(naturalGas) + 1))
water = df["Water"]
nitrogen = df["Nitrogen"]
hydrogen = df["Hydrogen"]
elec = df["Electricity"]
otherUti = df["Other utilities"]
CAPEX = df["CAPEX"]
fixedCosts = df["Fixed costs"]
total = df["Total"]

errors = np.array([df["Low"],df["High"]])

width = 0.75 # the width of the bars: can also be len(x) sequence

df = pd.DataFrame({"Natural gas" : naturalGas, "Water" : water, "Nitrogen" : nitrogen, "Hydrogen" : hydrogen, 
                   "Electricity" : elec, "Other utilities" : otherUti, 
                   "Fixed costs" : fixedCosts, "CAPEX" : CAPEX})

data = np.array(list(df.values))
data_cum = data.cumsum(axis = 1)
fig, ax = plt.subplots()



for i, (colname, color) in enumerate(zip(categories, colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        if i != len(categories) - 1:
            rects = ax.bar(myLabels, widths, width, bottom=starts, label = colname, color=color, edgecolor = 'w')
        else:
            reacts = ax.bar(myLabels, widths, width, bottom=starts, label = colname, color=color, edgecolor = 'w',
                             yerr = errors, capsize = 5)

ranges = [2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5]
for i in ranges:
    plt.axvline(x = i, linestyle = "--", color = "black")
    
plt.scatter(myLabels, total, s = 30, marker = 'D', color = 'black')

plt.xticks(myLabels, ["BAU", "Wind", "BAU", "Wind", "BAU", "Wind", "BAU", "Wind", "BAU", "Wind", "BAU", "Wind", "BAU", "Wind", "BAU", "Wind", "BAU", "Wind"], rotation = 45)
#plt.legend(loc = "upper left")

plt.ylabel("Methanol price [\$ t$^\mathrm{-1}$]")