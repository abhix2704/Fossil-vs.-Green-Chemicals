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
from matplotlib import ticker as tk
import matplotlib.gridspec as gridspec
from math import pi
import numpy as np
from matplotlib.lines import Line2D

plt.rcParams["figure.autolayout"] = True
plt.rcParams.update({'font.size': 8})
plt.rcParams['font.family'] = 'Arial'
fig = plt.figure(figsize=(fig_length[2],fig_height*0.3))

gs1 = gridspec.GridSpec(1, 2)
gs1.update(wspace = 0.4)

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]/1000
BAUprices = df["BAU"]/1000
gAWind = df["Wind"]/1000
gASolar = df["Solar"]/1000
gASMRCCS = df["SMR CCS"]/1000

sheetName = "Ammonia high low"
df = pd.read_excel(fileName, sheetName)
gAWindLow = df["Wind low"]/1000
gAWindHigh = df["Wind high"]/1000
gASolarLow = df["Solar low"]/1000
gASolarHigh = df["Solar high"]/1000

sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
MBAUprices = df["BAU"]/1000
gMWind = df["DAC + wind"]/1000
gMSolar = df["DAC + solar"]/1000
gMSMRCCS = df["SMR CCS"]/1000

sheetName = "Methanol high low"
df = pd.read_excel(fileName, sheetName)
gMWindLow = df["DAC + wind low"]/1000
gMWindHigh = df["DAC + wind high"]/1000
gMSolarLow = df["DAC + solar low"]/1000
gMSolarHigh = df["DAC + solar high"]/1000



# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
NGindex = [18,21,24,27,30,33,36,39,42,43,44,46]
timeTicks = times[NGindex]
N = len(NGindex)
angles = [n / float(N) * 2 * pi for n in range(N)]

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

# Initialise the spider plot
ax = plt.subplot(gs1[0], polar=True)
ax.set_title("a Ammonia [USD kg$^\mathrm{-1}$]", fontsize = fontsize_title, fontweight = "bold")
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
plt.yticks([0,1,2,3,4], ["","1","2","3","4"], color="black")
plt.ylim(-1,3.2)

#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, BAUprices[NGindex], marker = "s", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
"""
ax.fill_between(angleMin, -1, -0.04, color = "white",zorder = 20, clip_on = False)
ax.scatter(angles, BAUprices[NGindex], marker = "s", s = 15, facecolor = "#ffffff", 
           edgecolor = "#000000", zorder = 22, clip_on = False)
ax.scatter(angles, gASMRCCS[NGindex], marker = "d", s = 15, facecolor = "#A78DD8", 
           edgecolor = "#52318E", zorder = 24, clip_on = False)
ax.plot(angles, BAUprices[NGindex], color = "#000000", linewidth = 1.5, zorder = 2)
ax.plot(angles, gASMRCCS[NGindex], color = "#52318E", linewidth = 1.5, zorder = 2)
"""
"""
# Initialise the spider plot
ax = plt.subplot(gs1[2], polar=True)
ax.set_title("b", fontsize = fontsize_title, fontweight = "bold")
ax.set_theta_offset(pi/2)  # shift 90 degrees
ax.set_theta_direction(-1)  # clockwise
ax.set_thetamax(36)
ax.patch.set_facecolor("#ffffff")
ax.patch.set_alpha(0.05)


    
# Draw ylabels
plt.yticks([0,1,2,3], ["","1","2","3"], color="black")
plt.ylim(-1,3.2)

plt.xticks(angles, timeTicks, color = '#808080', fontsize = 7)
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
    label.set_position((angle, 0.18))  # Adjust the position of the labels
    

#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, BAUprices[NGindex], marker = "s", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.fill_between(angleMin, -1, -0.04, color = "white", zorder = 20, clip_on = False)
ax.scatter(angles, BAUprices[NGindex], marker = "s", s = 15, facecolor = "#ffffff", 
           edgecolor = "#000000", zorder = 22, clip_on = False)
ax.scatter(angles, gASolar[NGindex], marker = "h", s = 15, facecolor = "#FB7B71", 
           edgecolor = "#B71205", zorder = 24, clip_on = False)
ax.plot(angles, BAUprices[NGindex], color = "#000000", linewidth = 1.5, zorder = 2)
ax.plot(angles, gASolar[NGindex], color = "#B71205", linewidth = 1.5, zorder = 2)

# Initialise the spider plot
ax = plt.subplot(gs1[4], polar=True)
ax.set_title("c", fontsize = fontsize_title, fontweight = "bold")
ax.set_theta_offset(pi/2)  # shift 90 degrees
ax.set_theta_direction(-1)  # clockwise
ax.set_thetamax(36)
ax.patch.set_facecolor("#ffffff")
ax.patch.set_alpha(0.05)

plt.xticks(angles, timeTicks, color = '#808080', fontsize = 7)
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
    label.set_position((angle, 0.18))  # Adjust the position of the labels
    
# Draw ylabels
plt.yticks([0,1,2,3], ["","1","2","3"], color="black")
plt.ylim(-1,3.2)
"""
#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, BAUprices[NGindex], marker = "s", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.fill_between(angleMin, -1, -0.04, color = "white", zorder = 20, clip_on = False)
ax.scatter(angles, BAUprices[NGindex], marker = "s", s = 15, facecolor = "#ffffff", 
           edgecolor = "#000000", zorder = 22, clip_on = False)
ax.scatter(angles, gAWind[NGindex], marker = "^", s = 15, facecolor = "#6DD2EA", 
           edgecolor = "#167F99", zorder = 24, clip_on = False)
ax.plot(angles, BAUprices[NGindex], color = "#000000", linewidth = 1.5, zorder = 20)
ax.plot(angles, gAWind[NGindex], color = "#167F99", linewidth = 1.5, zorder = 21)
"""
"""

# Initialise the spider plot
ax = plt.subplot(gs1[1], polar=True)
ax.set_title("b Methanol [USD kg$^\mathrm{-1}$]", fontsize = fontsize_title, fontweight = "bold")
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
plt.yticks([0,1,2,3,4], ["","1","2","3","4"], color="black")
plt.ylim(-1.19,4)

#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, BAUprices[NGindex], marker = "s", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
"""
ax.fill_between(angleMin, -1.19, -0.04, color = "white", zorder = 20, clip_on = False)
ax.scatter(angles, MBAUprices[NGindex], marker = "D", s = 15, facecolor = "#ffffff", 
           edgecolor = "#000000", zorder = 22, clip_on = False)
ax.scatter(angles, gMSMRCCS[NGindex], marker = "d", s = 15, facecolor = "#A78DD8", 
           edgecolor = "#52318E", zorder = 24, clip_on = False)
ax.plot(angles, MBAUprices[NGindex], color = "#000000", linewidth = 1.5, zorder = 2)
ax.plot(angles, gMSMRCCS[NGindex], color = "#52318E", linewidth = 1.5, zorder = 2)
"""
"""
# Initialise the spider plot
ax = plt.subplot(gs1[3], polar=True)
ax.set_title("e", fontsize = fontsize_title, fontweight = "bold")
ax.set_theta_offset(pi/2)  # shift 90 degrees
ax.set_theta_direction(-1)  # clockwise
ax.set_thetamax(36)
ax.patch.set_facecolor("#ffffff")
ax.patch.set_alpha(0.05)

plt.xticks(angles, timeTicks, color = '#808080', fontsize = 7)
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
    label.set_position((angle, 0.18))  # Adjust the position of the labels
    
# Draw ylabels
plt.yticks([0,1,2,3,4], ["","1","2","3","4"], color="black")
plt.ylim(-1.19,4)

#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, BAUprices[NGindex], marker = "s", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.fill_between(angleMin, -1.19, -0.04, color = "white", zorder = 20, clip_on = False)
ax.scatter(angles, MBAUprices[NGindex], marker = "D", s = 15, facecolor = "#ffffff", 
           edgecolor = "#000000", zorder = 22, clip_on = False)
ax.scatter(angles, gMSolar[NGindex], marker = "h", s = 15, facecolor = "#FB7B71", 
           edgecolor = "#B71205", zorder = 24, clip_on = False)
ax.plot(angles, MBAUprices[NGindex], color = "#000000", linewidth = 1.5, zorder = 2)
ax.plot(angles, gMSolar[NGindex], color = "#B71205", linewidth = 1.5, zorder = 2)

# Initialise the spider plot
ax = plt.subplot(gs1[5], polar=True)
ax.set_title("f", fontsize = fontsize_title, fontweight = "bold")
ax.set_theta_offset(pi/2)  # shift 90 degrees
ax.set_theta_direction(-1)  # clockwise
ax.set_thetamax(36)
ax.patch.set_facecolor("#ffffff")
ax.patch.set_alpha(0.05)

plt.xticks(angles, timeTicks, color = '#808080', fontsize = 7)
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
    label.set_position((angle, 0.18))  # Adjust the position of the labels
    
# Draw ylabels
plt.yticks([0,1,2,3,4], ["","1","2","3","4"], color="black")
plt.ylim(-1.19,4)
"""
#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, BAUprices[NGindex], marker = "s", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.fill_between(angleMin, -1.19, -0.04, color = "white", zorder = 20, clip_on = False)
ax.scatter(angles, MBAUprices[NGindex], marker = "D", s = 15, facecolor = "#ffffff", 
           edgecolor = "#000000", zorder = 22, clip_on = False)
ax.scatter(angles, gMWind[NGindex], marker = "^", s = 15, facecolor = "#6DD2EA", 
           edgecolor = "#167F99", zorder = 24, clip_on = False)
ax.plot(angles, MBAUprices[NGindex], color = "#000000", linewidth = 1.5, zorder = 2)
ax.plot(angles, gMWind[NGindex], color = "#167F99", linewidth = 1.5, zorder = 2)
"""


legend_elements = [Line2D([0], [0], marker='s', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "#000000",
                                             label = 'Fossil ammonia', markersize = 5),
                   Line2D([0], [0], marker='D', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "#000000",
                                             label = 'Fossil methanol', markersize = 5),
                   #Line2D([0], [0], marker='d', color = "none", 
                    #                         markerfacecolor ='#A78DD8', markeredgecolor = "#52318E",
                     #                        label = 'H$_\mathrm{2}$ SMR$_\mathrm{CCS}$', markersize = 5),
                   #Line2D([0], [0], marker='h', color = "none", 
                    #                         markerfacecolor ='#FB7B71', markeredgecolor = "#B71205",
                     #                        label = 'H$_\mathrm{2}$ solar', markersize = 5),
                   Line2D([0], [0], marker='^', color = "none", 
                                             markerfacecolor ='#6DD2EA', markeredgecolor = "#167F99",
                                             label = 'H$_\mathrm{2}$ wind', markersize = 5)
                     ]

#fig.legend(handles = legend_elements, frameon = False, loc = "upper center", ncol = 5, 
        #  prop={"size":12}, bbox_to_anchor=(0.5, 0.2), handletextpad = 0.1)
"""
plt.savefig('Slide 7.jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Slide 7.svg', dpi=600, format='svg', bbox_inches="tight")


