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
from matplotlib import ticker as tk
import matplotlib.gridspec as gridspec
from math import pi
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 8})
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(fig_length[2],fig_height*0.5))
colors = ["#da5552","#7371fc","#ffd60a","#60d394","#ee9b00","#94d2bd","#005f73",
            "#fec89a"]


gs1 = gridspec.GridSpec(1, 2)

fileName = "Prices sensitivity 2.xlsx"
sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
NGprices = df["NG price"]/1000
times = df["Time"]
CO2Wind = df["CO2 Wind"]/1000
CO2Solar = df["CO2 Solar"]/1000
CO2SMRCCS = df["CO2 SMR CCS"]/1000

NGindex = [18,21,24,27,30,33,36,39,42,43,44,46]
timeTicks = times[NGindex]
N = len(NGindex)
angles = [n / float(N) * 2 * pi for n in range(int(N))]

# Plot data
angleMin = [0]
for i in range(0, len(NGprices)):
    if i > 0 and i < 4:
        angleMin.append(angleMin[i-1] + (360/N)/3 * pi / 180)
    elif i >= 4 and i < 8:
        angleMin.append(angleMin[i-1] + (360/N)/4 * pi / 180)
    elif i >= 8 and i < 13:
        angleMin.append(angleMin[i-1] + (360/N)/5 * pi / 180)
    elif i >= 13 and i < 16:
        angleMin.append(angleMin[i-1] + (360/N)/3 * pi / 180)
    elif i >= 16 and i < 20:
        angleMin.append(angleMin[i-1] + (360/N)/4 * pi / 180)
    elif i >= 20 and i < 25:
        angleMin.append(angleMin[i-1] + (360/N)/5 * pi / 180)
    elif i >= 25 and i < 28:
        angleMin.append(angleMin[i-1] + (360/N)/3 * pi / 180)
    elif i >= 28 and i < 32:
        angleMin.append(angleMin[i-1] + (360/N)/4 * pi / 180)
    elif i >= 32 and i < 37:
        angleMin.append(angleMin[i-1] + (360/N)/5 * pi / 180)
    elif i >= 37 and i < 40:
        angleMin.append(angleMin[i-1] + (360/N)/3 * pi / 180)
    elif i >= 40 and i < 44:
        angleMin.append(angleMin[i-1] + (360/N)/4 * pi / 180)
    elif i >= 44 and i < 47:
        angleMin.append(angleMin[i-1] + (360/N)/3 * pi / 180)


ax = plt.subplot(gs1[0], polar=True)
ax.set_title("a Ammonia [USD kg$^\mathrm{-1}$ CO$_\mathrm{2}$-eq]", fontsize = fontsize_title, fontweight = "bold")
ax.set_theta_offset(pi/2)  # shift 90 degrees
ax.set_theta_direction(-1)  # clockwise
ax.set_thetamax(36)
ax.patch.set_facecolor("#ffffff")
ax.patch.set_alpha(0.05)

plt.xticks(angles, timeTicks, color = '#808080')
for i, label in enumerate(ax.get_xticklabels()):
    angle = angles[i]
    if angle == 0:
        ha = 'center'
    elif 0 < angle < np.pi:
        ha = 'left'
    elif angle == np.pi:
        ha = 'center'
    else:
        ha = 'right'
    label.set_horizontalalignment(ha)
    label.set_position((angle, 0.09))  # Adjust the position of the labels
    
# Draw ylabels
plt.yticks([0,0.5,1,1.5], ["0","0.5","1","1.5"], color="black")
plt.ylim(-1,1.5)

#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, BAUprices[NGindex], marker = "s", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.fill_between(angleMin, -1, -0.04, color = "white",zorder = 16, clip_on = False)
ax.scatter(angles, CO2Wind[NGindex], marker = "^", s = 15, facecolor = "#6DD2EA", 
           edgecolor = "#167F99", zorder = 22, clip_on = False)
ax.scatter(angles, CO2Solar[NGindex], marker = "h", s = 15, facecolor = "#FB7B71", 
           edgecolor = "#B71205", zorder = 21, clip_on = False)
ax.scatter(angles, CO2SMRCCS[NGindex], marker = "d", s = 15, facecolor = "#A78DD8", 
           edgecolor = "#52318E", zorder = 20, clip_on = False)
ax.plot(angles, CO2Wind[NGindex], color = "#167F99", linewidth = 1.5, zorder = 19)
ax.plot(angles, CO2Solar[NGindex], color = "#B71205", linewidth = 1.5, zorder = 18)
ax.plot(angles, CO2SMRCCS[NGindex], color = "#52318E", linewidth = 1.5, zorder = 17)

sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
NGprices = df["NG price"]/1000
times = df["Time"]
CO2Wind = df["CO2 DAC + wind"]/1000
CO2Solar = df["CO2 DAC + solar"]/1000
CO2SMRCCS = df["CO2 SMR CCS"]/1000

ax = plt.subplot(gs1[1], polar=True)
ax.set_title("b Methanol [USD kg$^\mathrm{-1}$ CO$_\mathrm{2}$-eq]", fontsize = fontsize_title, fontweight = "bold")
ax.set_theta_offset(pi/2)  # shift 90 degrees
ax.set_theta_direction(-1)  # clockwise
ax.set_thetamax(36)
ax.patch.set_facecolor("#ffffff")
ax.patch.set_alpha(0.05)

plt.xticks(angles, timeTicks, color = '#808080')
for i, label in enumerate(ax.get_xticklabels()):
    angle = angles[i]
    if angle == 0:
        ha = 'center'
    elif 0 < angle < np.pi:
        ha = 'left'
    elif angle == np.pi:
        ha = 'center'
    else:
        ha = 'right'
    label.set_horizontalalignment(ha)
    label.set_position((angle, 0.09))  # Adjust the position of the labels
    
# Draw ylabels
plt.yticks([0,3,6,9], ["0","3","6","9"], color="black")
plt.ylim(-6,9)


#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, BAUprices[NGindex], marker = "s", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.fill_between(angleMin, -6, -0.24, color = "white",zorder = 16, clip_on = False)
ax.scatter(angles, CO2Wind[NGindex], marker = "^", s = 20, facecolor = "#6DD2EA", 
           edgecolor = "#167F99", zorder = 22, clip_on = False)
ax.scatter(angles, CO2Solar[NGindex], marker = "h", s = 20, facecolor = "#FB7B71", 
           edgecolor = "#B71205", zorder = 21, clip_on = False)
ax.scatter(angles, CO2SMRCCS[NGindex], marker = "d", s = 20, facecolor = "#A78DD8", 
           edgecolor = "#52318E", zorder = 20, clip_on = False)
ax.plot(angles, CO2Wind[NGindex], color = "#167F99", linewidth = 1.5, zorder = 19)
ax.plot(angles, CO2Solar[NGindex], color = "#B71205", linewidth = 1.5, zorder = 18)
ax.plot(angles, CO2SMRCCS[NGindex], color = "#52318E", linewidth = 1.5, zorder = 17)

legend_elements = [Line2D([0], [0], marker='d', color = "none", 
                                             markerfacecolor ='#A78DD8', markeredgecolor = "#52318E",
                                             label = 'H$_\mathrm{2}$ SMR$_\mathrm{CCS}$', markersize = 5),
                   Line2D([0], [0], marker='h', color = "none", 
                                             markerfacecolor ='#FB7B71', markeredgecolor = "#B71205",
                                             label = 'H$_\mathrm{2}$ solar', markersize = 5),
                   Line2D([0], [0], marker='^', color = "none", 
                                             markerfacecolor ='#6DD2EA', markeredgecolor = "#167F99",
                                             label = 'H$_\mathrm{2}$ wind', markersize = 5)]

fig.legend(handles = legend_elements, frameon = False, loc = "upper center", ncol = 5, 
          prop={"size":8}, bbox_to_anchor=(0.5, 0.2), handletextpad = 0.1)

plt.savefig('Figure 4 (radar).svg', dpi=600, bbox_inches='tight')
plt.savefig('Figure 4 (radar).jpg', dpi=600, bbox_inches='tight')
