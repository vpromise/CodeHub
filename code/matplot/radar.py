# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
plt.rc('font',family='liberation Serif')

# Set data
# df = pd.DataFrame({
# 'group':         ['upper-bound','joint','sequential','continual'],
# 'Polyp\n(Kvasir-SEG)':    [79.3,          65.7,         18.4,       65.6],
# 'Polyp\n(BKAI)':         [82.2,          79.8,         26.8,       68.9],
# 'Polyp\n(CVC-ClinicDB)':  [80.0,          72.5,         19.2,       64.5],
# 'Polyp\n(SinGAN) ':       [93.1,          86.2,         85.2,       84.4],
# 'Diabetic Foot Ulcer\n(DFUC)':   [50.3,          49.9,          2.2,       37.7],
# 'Thyroid Nodule\n(TN3K)':         [62.1,          61.0,         16.7,       49.2],
# 'Hippocampus\n(ADNI) ':         [48.6,          47.9,         48.8,       47.8]
# })

df = pd.DataFrame({
'group':         ['upper-bound','joint','sequential','continual'],
'A':    [79.3,          65.7,         18.4,       65.6],
'B':         [82.2,          79.8,         26.8,       68.9],
'C':  [80.0,          72.5,         19.2,       64.5],
'D':       [93.1,          86.2,         85.2,       84.4],
'E':   [50.3,          49.9,          2.2,       37.7],
'F':         [62.1,          61.0,         16.7,       49.2],
'G':         [48.6,          47.9,         48.8,       47.8]
})

# ------- PART 1: Create background
import seaborn as sns
sns.set_theme(style="whitegrid", palette="pastel")
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)

 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels

 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30,40, 50, 60, 70, 80, 90, 100], ["10","20","30", "40", "50", "60", "70", "80", "90", "100"], color="grey", size=6)
plt.ylim(0,100)
 
plt.xticks(angles[:-1], categories)

# # ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't make a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=0.5, linestyle='dashdot', color="tab:pink",label="upper-bound")
ax.fill(angles, values, 'tab:pink', alpha=0.15)
 
# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=0.5, linestyle='solid',  color="darkorange", label="joint")
ax.fill(angles, values, 'darkorange', alpha=0.15)
 
 
values=df.loc[2].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=0.5, linestyle='solid', color="tab:green", label="sequential")
ax.fill(angles, values, 'tab:green', alpha=0.2)



values=df.loc[3].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=0.5, linestyle='solid', color="deeppink", label="continual")
ax.fill(angles, values, 'deeppink', alpha=0.2)
# Add legend

# plt.legend(loc=2, fontsize=10, ncol=4, bbox_to_anchor=(0, -0.02), borderaxespad = 0.) 
plt.legend(loc='best', bbox_to_anchor=(1.3, 0.15))
plt.savefig('framework3.pdf', dpi=144)
# Show the graph
plt.show()