# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:27:19 2022

@author: anabera
"""

fig_length = {1:   3.50394,    # 1 column
          1.5: 5.35433, # 1.5 columns
          2:   7.20472}    # 2 columns
fig_height = 9.72441 # maximum height
fontsize_title = 9
fontsize_label = 8
fontsize_legend = 8
fontsize_axs = 8

from matplotlib import pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 8})
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(fig_length[2],fig_height*0.75))
colors = ["#da5552","#7371fc","#ffd60a","#60d394","#ee9b00","#94d2bd","#005f73",
            "#fec89a"]
ranges = [3.5, 6.5, 9.5, 12.5, 15.5, 18.5, 21.5, 24.5, 27.5, 30.5]
t = ["Avg 19", "Avg 20", "Jul '21", "Oct '21", "Jan '22", "Apr '22", "Jul '22", "Aug '22", "Sep '22", "Nov '22"]

plt.subplot(2,1,1)
fileName = "Prices sensitivity 2.xlsx"
sheetName = "Ammonia avoidance"
df = pd.read_excel(fileName, sheetName)
categories = ["Average"]
average = df["Average"]/1000
myLabels = list(range(1, len(average) + 1))

errorsLow = df["Low"]/1000
errorsLow1 = errorsLow[0::4]
errorsLow2 = errorsLow[1::4]
errorsHigh = df["High"]/1000
errorsHigh1 = errorsHigh[0::4]
errorsHigh2 = errorsHigh[1::4]

errors1 = [errorsLow1,errorsHigh1]
errors2 = [errorsLow2,errorsHigh2]

width = 0.75 # the width of the bars: can also be len(x) sequence
ax = plt.gca()
plt.axhline(0, color = "#808080", linewidth = 0.5)
for i in range(0, len(average), 4):
    reacts = ax.bar(myLabels[i + 2], average[i], width, label = "Wind", color="#167F99")
    reacts = ax.bar(myLabels[i + 1], average[i + 1], width, label = "Solar", color="#B71205")
    reacts = ax.bar(myLabels[i], average[i + 2], width, label = "H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", 
                    color="#52318E")
    
for i in range(0, len(errorsLow1)):
    errorsLowTemp = average[4*i] - errorsLow[4*i]
    if average[4*i] > 0 and errorsLowTemp > 0: 
        plt.plot([myLabels[4*i+2]]*2,[errorsLowTemp, average[4*i]], color = "#ffffff", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#ffffff")
    elif average[4*i] < 0 and errorsLowTemp < 0:
        plt.plot([myLabels[4*i+2]]*2,[errorsLowTemp, average[4*i]], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")
    else:
        plt.plot([myLabels[4*i+2]]*2,[average[4*i], 0], color = "#ffffff", linewidth = 0.5)
        plt.plot([myLabels[4*i+2]]*2,[0, errorsLowTemp], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")

for i in range(0, len(errorsLow2)):
    errorsLowTemp = average[4*i+1] - errorsLow[4*i+1]
    if average[4*i+1] > 0 and errorsLowTemp > 0: 
        plt.plot([myLabels[4*i+1]]*2,[errorsLowTemp, average[4*i+1]], color = "#ffffff", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#ffffff")
    elif average[4*i+1] < 0 and errorsLowTemp < 0:
        plt.plot([myLabels[4*i+1]]*2,[errorsLowTemp, average[4*i+1]], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")
    else:
        plt.plot([myLabels[4*i+1]]*2,[average[4*i+1], 0], color = "#ffffff", linewidth = 0.5)
        plt.plot([myLabels[4*i+1]]*2,[0, errorsLowTemp], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")

for i in range(0, len(errorsHigh1)):
    errorsHighTemp = errorsHigh[4*i] + average[4*i]
    if average[4*i] > 0 and errorsHighTemp > 0: 
        plt.plot([myLabels[4*i+2]]*2,[errorsHighTemp, average[4*i]], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")
    elif average[4*i] < 0 and errorsHighTemp < 0:
        plt.plot([myLabels[4*i+2]]*2,[errorsHighTemp, average[4*i]], color = "#ffffff", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#ffffff")
    else:
        plt.plot([myLabels[4*i+2]]*2,[average[4*i], 0], color = "#ffffff", linewidth = 0.5)
        plt.plot([myLabels[4*i+2]]*2,[0, errorsHighTemp], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")  

for i in range(0, len(errorsHigh2)):
    errorsHighTemp = errorsHigh[4*i+1] + average[4*i+1]
    if average[4*i+1] > 0 and errorsHighTemp > 0: 
        plt.plot([myLabels[4*i+1]]*2,[errorsHighTemp, average[4*i+1]], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")
    elif average[4*i] < 0 and errorsHighTemp < 0:
        plt.plot([myLabels[4*i+1]]*2,[errorsHighTemp, average[4*i+1]], color = "#ffffff", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#ffffff")
    else:
        plt.plot([myLabels[4*i+1]]*2,[average[4*i+1], 0], color = "#ffffff", linewidth = 0.5)
        plt.plot([myLabels[4*i+1]]*2,[0, errorsHighTemp], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")  

"""
plotline2, caplines2, barlinecols2 = ax.errorbar(
                    myLabels[2::4], average[0::4], yerr = errors1, elinewidth = 0.5, ls = "none",
                    capsize = 2, color='#808080')
plotline2, caplines2, barlinecols2 = ax.errorbar(
                    myLabels[1::4], average[1::4], yerr = errors2, elinewidth = 0.5, ls = "none",
                    capsize = 2, color='#808080')        

"""
plt.xticks(myLabels, ["Wind", "Solar", "SMR$_\mathrm{CCS}$", ""]*10, rotation = 45, ha = "right")    
plt.xticks([])
plt.xlim([0.5,39.5])

#for i in range(0,len(ranges)-1):
 #   plt.axvline(x = ranges[i], linestyle = "--", color = "black")
  #  plt.text(x = ranges[i] - 2.5, y = 2650, s = t[i], color = "k", rotation = 0)
#plt.text(x = ranges[i + 1] - 2.5, y = 2650, s = t[i+1], color = "k")
plt.title("a Ammonia", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.ylabel("Avoidance cost [USD kg$^\mathrm{-1}$ CO$_\mathrm{2}$-eq]")

plt.subplot(2,1,2)
sheetName = "Methanol avoidance"
df = pd.read_excel(fileName, sheetName)
categories = ["Average"]
average = df["Average"]/1000
myLabels = list(range(1, len(average) + 1))

errorsLow = df["Low"]/1000
errorsLow1 = errorsLow[0::4]
errorsLow2 = errorsLow[1::4]
errorsHigh = df["High"]/1000
errorsHigh1 = errorsHigh[0::4]
errorsHigh2 = errorsHigh[1::4]

errors1 = [errorsLow1,errorsHigh1]
errors2 = [errorsLow2,errorsHigh2]

width = 0.75 # the width of the bars: can also be len(x) sequence
ax = plt.gca()
plt.axhline(0, color = "#808080", linewidth = 0.5)
for i in range(0, len(average), 4):
    reacts = ax.bar(myLabels[i + 2], average[i], width, label = "Wind", color="#167F99")
    reacts = ax.bar(myLabels[i + 1], average[i + 1], width, label = "Solar", color="#B71205")
    reacts = ax.bar(myLabels[i], average[i + 2], width, label = "H$_\mathrm{2}$ SMR$_\mathrm{CCS}$", 
                    color="#52318E")
    
for i in range(0, len(errorsLow1)):
    errorsLowTemp = average[4*i] - errorsLow[4*i]
    if average[4*i] > 0 and errorsLowTemp > 0: 
        plt.plot([myLabels[4*i+2]]*2,[errorsLowTemp, average[4*i]], color = "#ffffff", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#ffffff")
    elif average[4*i] < 0 and errorsLowTemp < 0:
        plt.plot([myLabels[4*i+2]]*2,[errorsLowTemp, average[4*i]], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")
    else:
        plt.plot([myLabels[4*i+2]]*2,[average[4*i], 0], color = "#ffffff", linewidth = 0.5)
        plt.plot([myLabels[4*i+2]]*2,[0, errorsLowTemp], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")

for i in range(0, len(errorsLow2)):
    errorsLowTemp = average[4*i+1] - errorsLow[4*i+1]
    if average[4*i+1] > 0 and errorsLowTemp > 0: 
        plt.plot([myLabels[4*i+1]]*2,[errorsLowTemp, average[4*i+1]], color = "#ffffff", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#ffffff")
    elif average[4*i+1] < 0 and errorsLowTemp < 0:
        plt.plot([myLabels[4*i+1]]*2,[errorsLowTemp, average[4*i+1]], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")
    else:
        plt.plot([myLabels[4*i+1]]*2,[average[4*i+1], 0], color = "#ffffff", linewidth = 0.5)
        plt.plot([myLabels[4*i+1]]*2,[0, errorsLowTemp], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsLowTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")

for i in range(0, len(errorsHigh1)):
    errorsHighTemp = errorsHigh[4*i] + average[4*i]
    if average[4*i] > 0 and errorsHighTemp > 0: 
        plt.plot([myLabels[4*i+2]]*2,[errorsHighTemp, average[4*i]], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")
    elif average[4*i] < 0 and errorsHighTemp < 0:
        plt.plot([myLabels[4*i+2]]*2,[errorsHighTemp, average[4*i]], color = "#ffffff", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#ffffff")
    else:
        plt.plot([myLabels[4*i+2]]*2,[average[4*i], 0], color = "#ffffff", linewidth = 0.5)
        plt.plot([myLabels[4*i+2]]*2,[0, errorsHighTemp], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+2], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")  

for i in range(0, len(errorsHigh2)):
    errorsHighTemp = errorsHigh[4*i+1] + average[4*i+1]
    if average[4*i+1] > 0 and errorsHighTemp > 0: 
        plt.plot([myLabels[4*i+1]]*2,[errorsHighTemp, average[4*i+1]], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")
    elif average[4*i] < 0 and errorsHighTemp < 0:
        plt.plot([myLabels[4*i+1]]*2,[errorsHighTemp, average[4*i+1]], color = "#ffffff", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#ffffff")
    else:
        plt.plot([myLabels[4*i+1]]*2,[average[4*i+1], 0], color = "#ffffff", linewidth = 0.5)
        plt.plot([myLabels[4*i+1]]*2,[0, errorsHighTemp], color = "#808080", linewidth = 0.5)
        plt.errorbar(myLabels[4*i+1], errorsHighTemp, yerr = 0, capsize = 2, elinewidth = 0.5, color = "#808080")  

    
#plotline2, caplines2, barlinecols2 = ax.errorbar(
 #                   myLabels[2::4], average[0::4], yerr = errors1, elinewidth = 0.5, ls = "none",
  #                  capsize = 2, color='#808080')
#plotline2, caplines2, barlinecols2 = ax.errorbar(
 #                   myLabels[1::4], average[1::4], yerr = errors2, elinewidth = 0.5, ls = "none",
  #                  capsize = 2, color='#808080')      
#plt.xticks(myLabels, ["Wind", "Solar", "SMR$_\mathrm{CCS}$", ""]*10, rotation = 45, ha = "right")    
plt.xticks([])
plt.xlim([0.5,39.5])


ranges2 = [2,6,10,14,18,22,26,30,34,38]
plt.xticks(ranges2, t)

#for i in range(0,len(ranges)-1):
    #plt.axvline(x = ranges[i], linestyle = "--", color = "black")
    #plt.text(x = ranges[i] - 2.5, y = 13500, s = t[i], color = "k", rotation = 0)
    
#plt.text(x = ranges[i + 1] - 2.5, y = 13500, s = t[i+1], color = "k")
plt.title("b Methanol", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.ylabel("Avoidance cost [USD kg$^\mathrm{-1}$ CO$_\mathrm{2}$-eq]")


from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#52318E', label='H$_\mathrm{2}$ SMR$_\mathrm{CCS}$'),
                   Patch(facecolor='#B71205', label='H$_\mathrm{2}$ solar'),
                   Patch(facecolor='#167F99', label='H$_\mathrm{2}$ wind')]
legend = ax.legend(handles = legend_elements, loc = "upper center", ncol = 3, 
                   prop={"size":8}, bbox_to_anchor=(0.5, -0.1), frameon = False, handletextpad = 0.1)
for i in range(0, len(legend.legendHandles)):
    legend.legendHandles[i].set_width(9)
    
plt.savefig('Figure 4.svg', dpi=600, bbox_inches='tight')
plt.savefig('Figure 4.jpg', dpi=600, bbox_inches='tight')
