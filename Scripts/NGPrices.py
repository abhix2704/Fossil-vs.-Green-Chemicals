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

fig_length = {1:   3.50394,    # 1 column
              1.5: 5.35433,    # 1.5 columns
              2:   7.20472}    # 2 columns
fig_height = 9.72441 # maxium height

from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_excel("Prices sensitivity 2.xlsx", sheet_name="Ammonia", usecols="A:E")

plt.rcParams["figure.autolayout"] = True
fig = plt.figure(figsize=(fig_length[2],fig_height*0.35), tight_layout=True)

index = df["Index"]
times = df["Time"]
NGprices = df["NG price"]
BAUprices = df["BAU"]
l = len(times)

labels = [times[i] if i == 0 or i % 3 == 0 else "" for i in range(len(times))]
labels[-3:] = ["", "", "Nov '22"]

mi = [i+1 for i, label in enumerate(labels) if label == ""]
miLabels = [label for label in labels if label == ""]
ma = [i+1 for i, label in enumerate(labels) if label != ""]
maLabels = [label for label in labels if label != ""]
        
ax = plt.subplot(1,2,1)
plt.title("(a) Ammonia", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "*", s = 10,label = 'Ammonia')
plt.scatter(index[0:l], NGprices[0:l], marker = "o", color = "#da5552", s = 10,label='Natural gas')
plt.ylabel("Production cost / price [USD t$^\mathrm{-1}$]")

ax.set_xticks(ma, labels = maLabels, rotation = 45, ha = "right")
ax.set_xticks(mi, minor=True)
plt.xlim(0,index.max()+1)

for i in [13,23,38,41.5]:
    plt.axvline(i, color = "grey", linewidth = 0.5, linestyle = "--")
    
annotations = [("COVID pandemic \nstarts in Europe",9),("Rising inflation",21),("Russian war \non ukraine",34),("Russia cuts \nsupply",42.5)]
for txt,x in annotations:
    ax.text(x, 2000, txt, color = "grey", rotation = 90, fontsize = fontsize_label)

plt.legend(loc = "center left", ncol = 1, prop={"size":8})

sheetName = "Methanol"
df = pd.read_excel("Prices sensitivity 2.xlsx", sheet_name="Methanol", usecols="A:E")
BAUprices = df["BAU"]

ax = plt.subplot(1,2,2)
plt.title("(b) Methanol", color = "black", fontsize = fontsize_title, fontweight = "bold")
plt.scatter(index[0:l], BAUprices[0:l], color = "black", marker = "p", s = 10,label = 'Methanol')
plt.scatter(index[0:l], NGprices[0:l], marker = "o", color = "#da5552", s = 10,label='Natural gas')

ax.set_xticks(ma, labels = maLabels, rotation = 45, ha = "right")
ax.set_xticks(mi, minor=True)
plt.xlim(0,index.max()+1)
plt.yticks([])

for i in [13,23,38,41.5]:
    plt.axvline(i, color = "grey", linewidth = 0.5, linestyle = "--")
    
annotations = [("COVID pandemic \nstarts in Europe",9),("Rising inflation",21),("Russian war \non ukraine",34),("Russia cuts \nsupply",42.5)]
for txt,x in annotations:
    ax.text(x, 2000, txt, color = "grey", rotation = 90, fontsize = fontsize_label)

plt.legend(loc = "center left", ncol = 1, prop={"size":8})


plt.savefig('Figure 1.jpg', dpi=600, format='jpg', bbox_inches="tight")
plt.savefig('Figure 1.svg', dpi=600, format='svg', bbox_inches="tight")

