# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 10:02:05 2022

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

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import ticker as tk
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D

plt.rcParams.update({'font.size': 8})
plt.rcParams['font.family'] = 'Arial'
fig = plt.figure(figsize=(fig_length[2],fig_height*0.35))
gs1 = gridspec.GridSpec(1, 3, width_ratios=[1, 1, 0.05])
gs1.update(wspace = 0.1, hspace = 0)

avgNG20192020 = 179.83/1000;
avgElec20192020 = 34.07/1000;
avgNG2021 = 720.12/1000;
avgElec2021 = 96.58/1000;
minNG2022= 1216.69/1000;
minElec2022 = 128.78/1000;
maxNG2022= 3129.51/1000;
maxElec2022 = 469.35/1000;

fileName = "Prices sensitivity future.xlsx"

sheetName = "random"
df = pd.read_excel(fileName, sheetName)
naturalGasPrice = df["NG price"]/1000
elecPrice = df["Elec price"]
BAUAmmonia = df["Ammonia price"]/1000
BAUMethanol = df["Methanol price"]/1000

sheetName = "Green"
df = pd.read_excel(fileName, sheetName)
gAWind = df["Wind ammonia"]/1000
gASolar = df["Solar ammonia"]/1000
gMWind = df["Wind methanol"]/1000
gMSolar = df["Solar methanol"]/1000

plt.subplot(gs1[0])
plt.title("a Ammonia", color = "black", fontsize = fontsize_title, fontweight = "bold")

plt.scatter(minNG2022, minElec2022, marker = 's', s = 15, facecolors = "#ffffff", edgecolors = "#000000", zorder = 3)
plt.scatter(maxNG2022, maxElec2022, marker = 's', s = 15, facecolors = "#ffffff", edgecolors = "#000000", zorder = 3)

#plt.scatter(0.5, 0.3, marker = "^", facecolors = "#6DD2EA", edgecolors = "#167F99", zorder = 4)

plt.tricontourf(naturalGasPrice, elecPrice, BAUAmmonia, 100, zorder = 1)
plt.set_cmap('Spectral_r')
plt.clim(0, max(BAUAmmonia))
plt.tricontour(naturalGasPrice, elecPrice, BAUAmmonia, levels = [1430.31/1000], 
               colors = "#167F99", linewidths = 1, zorder = 2)
plt.tricontour(naturalGasPrice, elecPrice, BAUAmmonia, levels = [1590.34/1000], 
               colors = "#167F99", linewidths = 1, zorder = 2)
plt.tricontour(naturalGasPrice, elecPrice, BAUAmmonia, levels = [gAWind[0]], 
               colors = "#167F99", linestyles = '-.', linewidths = 1, zorder = 4)
plt.tricontour(naturalGasPrice, elecPrice, BAUAmmonia, levels = [gAWind[2]], 
               colors = "#167F99", linestyles = '-.', linewidths = 1, zorder = 4)
plt.tricontourf(naturalGasPrice, elecPrice, BAUAmmonia, levels = [gAWind[2], gAWind[0]], 
                alpha = 0.5, colors = "#167F99")
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.xaxis.set_minor_locator(tk.AutoMinorLocator(2))


"""
plt.tricontour(naturalGasPrice, elecPrice, BAUAmmonia, levels = [gASolar[0]], 
               colors = "#B71205", linestyles = ':', linewidths = 1.5, zorder = 4)
plt.tricontour(naturalGasPrice, elecPrice, BAUAmmonia, levels = [gASolar[2]], 
               colors = "#B71205", linestyles = ':', linewidths = 1.5, zorder = 4)
"""
plt.xlabel("Natural gas price [USD kg$^{-1}$]")
plt.ylabel("Grid electricity price [USD kWh$^{-1}$]")

plt.subplot(gs1[1])
plt.title("b Methanol", color = "black", fontsize = fontsize_title, fontweight = "bold")

plt.scatter(minNG2022, minElec2022, marker = 'D', s = 15, facecolors = "#ffffff", edgecolors = "#000000", zorder = 3)
plt.scatter(maxNG2022, maxElec2022, marker = 'D', s = 15, facecolors = "#ffffff", edgecolors = "#000000", zorder = 3)


contour = plt.tricontourf(naturalGasPrice, elecPrice, BAUMethanol, 100, zorder = 1)
plt.set_cmap('Spectral_r')
plt.clim(0, max(BAUAmmonia))
plt.tricontour(naturalGasPrice, elecPrice, BAUMethanol, levels = [1871.97/1000], 
               colors = "#167F99", linewidths = 1, zorder = 2)
plt.tricontour(naturalGasPrice, elecPrice, BAUMethanol, levels = [2273.11/1000], 
               colors = "#167F99", linewidths = 1, zorder = 2)
plt.tricontour(naturalGasPrice, elecPrice, BAUMethanol, levels = [gMWind[0]], 
               colors = "#167F99", linestyles = '-.', linewidths = 1, zorder = 4)
plt.tricontour(naturalGasPrice, elecPrice, BAUMethanol, levels = [gMWind[2]], 
               colors = "#167F99", linestyles = '-.', linewidths = 1, zorder = 4)
plt.tricontourf(naturalGasPrice, elecPrice, BAUMethanol, levels = [gMWind[2], gMWind[0]], 
                alpha = 0.5, colors = "#167F99")
ax = plt.gca()
ax.yaxis.set_minor_locator(tk.AutoMinorLocator(2))
ax.xaxis.set_minor_locator(tk.AutoMinorLocator(2))


"""
plt.tricontour(naturalGasPrice, elecPrice, BAUMethanol, levels = [gASolar[0]], 
               colors = "#B71205", linestyles = ':', linewidths = 1.5, zorder = 4)
plt.tricontour(naturalGasPrice, elecPrice, BAUMethanol, levels = [gASolar[2]], 
               colors = "#B71205", linestyles = ':', linewidths = 1.5, zorder = 4)
"""
plt.xlabel("Natural gas price [USD kg$^{-1}$]")
plt.yticks([])

# Create the color bar
ax_cbar = plt.subplot(gs1[2])
cbar = plt.colorbar(contour, cax=ax_cbar, extend='both')
plt.clim(0, max(BAUAmmonia))
cbar.set_label('Production cost [USD kg$^{-1}$]', rotation = -90, labelpad = 10)
num_ticks = 7
cbar.locator = plt.MaxNLocator(nbins=num_ticks)
cbar.formatter.set_useOffset(False)
cbar.update_ticks()

legend_elements = [Line2D([0], [0], marker='s', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "black",
                                             label = 'Fossil ammonia', markersize = 5),
                   Line2D([0], [0], marker='D', color = "none", 
                                            markerfacecolor ='#ffffff', markeredgecolor = "black",
                                            label = 'Fossil methanol', markersize = 5),
                   Line2D([0], [0], color = "#167F99", linestyle = "-",
                                             label = 'H$_\mathrm{2}$ wind', linewidth = 1)]



legend =  fig.legend(handles = legend_elements, frameon = False, loc = "upper center", ncol = 4, 
           prop={"size":8}, bbox_to_anchor=(0.5, 0.001), handletextpad = 0.1)

for i in range(len(legend.legendHandles)):
    if i == 2:
        handle = legend.legendHandles[i]
        handle.set_xdata([0, 4, 12])

    
plt.savefig('Figure future.jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure future.svg', dpi=600, format='svg', bbox_inches="tight")