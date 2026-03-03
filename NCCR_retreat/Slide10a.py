# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 21:27:19 2022

@author: anabera
"""

fig_length = {1:   3.50394,    # 1 column
          1.5: 5.35433, # 1.5 columns
          2:   7.20472}    # 2 columns
fig_height = 9.72441 # maxium height
fontsize_title = 9
fontsize_label = 8
fontsize_legend = 8
fontsize_axs = 8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams["figure.autolayout"] = True
plt.rcParams.update({'font.size': 12})
plt.rcParams['font.family'] = 'Arial'
fig = plt.figure(figsize=(fig_length[2],fig_height*0.5))
colors = ["#808080","#167f99","#a9d898","#6dd2ea","#fb7b71","#b71205",
            "#52318e","#A78DD8"]
categories = ["Natural gas", "Water", "Hydrogen", "Nitrogen or CO$_\mathrm{2}$", "Electricity", "Other utilities", "Fixed costs", "CAPEX"]
ranges = [3.25, 6.25, 9.25, 12.25, 15.25, 18.25, 21.25, 24.25, 27.25,30.25]
t = ["Avg 19", "Avg 20", "Jul '21", "Oct '21", "Jan '22", "Apr '22", "Jul '22", "Aug '22", "Sep '22", "Nov '22"]

plt.subplot(1,1,1)
fileName = "Ammonia breakdown.xlsx"

sheetName = "Summary"
df = pd.read_excel(fileName, sheetName)
naturalGas = df["Natural gas"]/1000
myLabels = list(range(1, len(naturalGas) + 1))
water = df["Water"]/1000
nitrogen = df["Nitrogen"]/1000
hydrogen = df["Hydrogen"]/1000
elec = df["Electricity"]/1000
otherUti = df["Other utilities"]/1000
CAPEX = df["CAPEX"]/1000
fixedCosts = df["Fixed costs"]/1000
total = df["Total"]/1000

errorsLow = df["Low"]/1000
errorsLow = errorsLow[1::3]
errorsHigh = df["High"]/1000
errorsHigh = errorsHigh[1::3]


width = 0.75 # the width of the bars: can also be len(x) sequence
df = pd.DataFrame({"Natural gas" : naturalGas, "Water" : water, "Hydrogen" : hydrogen, "Nitrogen" : nitrogen, 
                   "Electricity" : elec, "Other utilities" : otherUti, 
                   "Fixed costs" : fixedCosts, "CAPEX" : CAPEX})
data = np.array(list(df.values))
data_cum = data.cumsum(axis = 1)
ax = plt.gca()

for i, (colname, color) in enumerate(zip(categories, colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        if i != len(categories) - 1:
            rects = ax.bar(myLabels, widths, width, bottom=starts, label = colname, color=color, edgecolor = 'none')
        else:
            reacts = ax.bar(myLabels, widths, width, bottom=starts, label = colname, color=color, edgecolor = 'none')
            plotline2, caplines2, barlinecols2 = ax.errorbar(
                                myLabels[1::3], total[1::3], yerr = errorsHigh, lolims = True, ls = "none",
                                capsize = 0, elinewidth = 0.5, color='#808080')
            caplines2[0].set_marker('_')
            caplines2[0].set_markersize(4)
            plotline3, caplines3, barlinecols3 = ax.errorbar(
                                myLabels[1::3], total[1::3], yerr = errorsLow, uplims = True, ls = "none",
                                capsize = 0, elinewidth = 0.5, color='#ffffff')
            caplines3[0].set_marker('_')
            caplines3[0].set_markersize(4)
    

#ax.set_ylim(0,round(max(total)) + 600)

#for i in range(0,len(ranges)-1):
    #plt.axvline(x = ranges[i], linestyle = "--", color = "black")
 #   plt.text(x = ranges[i] - 1.7, y = 0, s = t[i], color = "black", rotation = 0, ha = "center")
    
#plt.text(x = ranges[i + 1] - 1.7, y = 0, s = t[i+1], color = "black",  ha = "center")
plt.xlim([0.25,29.75])
plt.ylabel("Production cost [USD kg$^\mathrm{-1}$]")



            
#ax.set_ylim(0,round(max(total)) + round(max(errorsHigh)) + 650)
#for i in range(0,len(ranges)-1):
    #plt.axvline(x = ranges[i], linestyle = "--", color = "black")
 #   plt.text(x = ranges[i] - 1.7, y = 0, s = t[i], color = "black", rotation = 0, ha = "center")
    
#plt.text(x = ranges[i + 1] - 1.7, y = 0, s = t[i+1], color = "black", ha = "center")
#plt.xticks(myLabels, ["Fossil", "H$_\mathrm{2}$ Wind"]*10, rotation = 45, ha = "right")
ranges2 = [1.5,4.5,7.5,10.5,13.5,16.5,19.5,22.5,25.5,28.5]
plt.xticks(ranges2, t)
legend = ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=4, frameon = False, handletextpad = 0.1)
for i in range(0, len(legend.legendHandles)):
    legend.legendHandles[i].set_width(12)

plt.savefig('Figure 3.svg', dpi=600, bbox_inches='tight')
plt.savefig('Figure 3.jpg', dpi=600, bbox_inches='tight')