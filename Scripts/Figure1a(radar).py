# Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D
from math import pi
 
fig_length = {1:   3.50394,    # 1 column
          1.5: 5.35433, # 1.5 columns
          2:   7.20472}    # 2 columns
fig_height = 9.72441 # maxium height
fontsize_title = 9
fontsize_label = 8
fontsize_legend = 8
fontsize_axs = 8

plt.rcParams["figure.autolayout"] = True
plt.rcParams['font.family'] = 'Arial'
plt.rcParams.update({'font.size': 8})
fig = plt.figure(figsize=(fig_length[1.5],fig_height*0.8))
gs1 = gridspec.GridSpec(2,1)
#gs1.update(hspace = 0.4)

fileName = "Prices sensitivity 2.xlsx"

sheetName = "Ammonia"
df = pd.read_excel(fileName, sheetName)
index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]/1000
BAUprices = df["BAU"]/1000

sheetName = "Methanol"
df = pd.read_excel(fileName, sheetName)
MBAUprices = df["BAU"]/1000

 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
NGindex = [0,3,7,12,15,19,24,27,31,36,39,43,46]
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
ax = plt.subplot(gs1[0], polar = True)
ax.set_title("a Ammonia", fontsize = fontsize_title, fontweight = "bold")
ax.set_theta_offset(pi/2)  # shift 90 degrees
ax.set_theta_direction(-1)  # clockwise
ax.set_thetamax(36)
ax.patch.set_facecolor("#808080")
ax.patch.set_alpha(0.05)

plt.xticks(angles, timeTicks, color = '#808080')
    
# Draw ylabels
plt.yticks([0,1,2,3,4], ["0","1","2","3","3.5"], color="black")
plt.ylim(-1,3.5)

#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, BAUprices[NGindex], marker = "s", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.fill_between(angleMin, -1, -0.04, color = "white", zorder = 20, clip_on = False)
ax.scatter(angles, NGprices[NGindex], marker = "o", s = 20, color = 'black', zorder = 3, clip_on = False)
ax.scatter(angles, BAUprices[NGindex], marker = "s", s = 20, facecolor = "#ffffff", 
           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.plot(angles, NGprices[NGindex], color = "black", linewidth = 2, zorder = 2)
ax.plot(angles, BAUprices[NGindex], color = "#808080", linewidth = 2, zorder = 4)



ax = plt.subplot(gs1[1], polar=True)
ax.set_title("b Methanol", fontsize = fontsize_title, fontweight = "bold")
ax.set_theta_offset(pi/2)  # shift 90 degrees
ax.set_theta_direction(-1)  # clockwise
ax.set_thetamax(36)
ax.patch.set_facecolor("#808080")
ax.patch.set_alpha(0.05)

plt.xticks(angles, timeTicks, color = '#808080')
    
# Draw ylabels
plt.yticks([0,1,2,3,4], ["0","1","2","3","3.5"], color="black")
plt.ylim(-1,3.5)

#ax.scatter(angles, NGprices[NGindex], marker = "o", color = 'black', zorder = 3, clip_on = False)
#ax.scatter(angles, MBAUprices[NGindex], marker = "D", facecolor = "#ffffff", 
#           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.fill_between(angleMin, -1, -0.04, color = "white", zorder = 20, clip_on = False)
ax.scatter(angles, NGprices[NGindex], marker = "o", s = 20, color = 'black', zorder = 3, clip_on = False)
ax.scatter(angles, MBAUprices[NGindex], marker = "D", s = 20, facecolor = "#ffffff", 
           edgecolor = "#808080", zorder = 5, clip_on = False)
ax.plot(angles, NGprices[NGindex], color = "black", linewidth = 2, zorder = 2)
ax.plot(angles, MBAUprices[NGindex], color = "#808080", linewidth = 2, zorder = 4)


legend_elements = [Line2D([0], [0], marker='o', color = "none", 
                          markerfacecolor ='black', markeredgecolor = "none",
                          label = 'Natural gas price', markersize = 5),
                   Line2D([0], [0], marker='s', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "#808080",
                                             label = 'Fossil ammonia', markersize = 5),
                   Line2D([0], [0], marker='D', color = "none", 
                                             markerfacecolor ='#ffffff', markeredgecolor = "#808080",
                                             label = 'Fossil methanol', markersize = 5)]

fig.legend(handles = legend_elements, frameon = False, loc = "upper center", ncol = 3, 
          prop={"size":8}, bbox_to_anchor=(0.5, 0.02), handletextpad = 0.2)

# Show the graph
plt.show()
plt.savefig('Figure 1a (radar).jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure 1a (radar).svg', dpi=600, format='svg', bbox_inches="tight")