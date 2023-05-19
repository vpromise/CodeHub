import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# import matplotlib
# print(matplotlib.get_cachedir())
plt.rc('font',family='liberation Serif')

xx = ['Polyp BM', 'CPM-17', 'DFUC', 'ADNI', 'TN3K']
yy = ['Polyp BM', 'CPM-17', 'DFUC', 'ADNI', 'TN3K']


matrix = np.array([[68.1, 24.0, 25.1, 00.0, 11.1],
                   [36.1, 44.2, 29.0, 00.0, 14.0], 
                   [29.4, 16.4, 50.3, 00.0, 13.3], 
                   [00.0, 00.3, 00.0, 48.6, 00.0], 
                   [17.0, 03.2, 06.0, 00.0, 62.1]]
                 )


fig, ax = plt.subplots()
fig.subplots_adjust(left=.02, bottom=0.015, right=1.05, top=.78)
fig.set_size_inches(15,15)
im = ax.imshow(matrix)


# ax.set_title('cross validation results', )
ax.xaxis.tick_top()
# We want to show all ticks...
ax.set_xticks(np.arange(len(xx)))
ax.set_yticks(np.arange(len(yy)))


sns.set(font_scale=2) # 设置cbar字体大小
# g = sns.heatmap(matrix, annot=True, fmt='.3f', annot_kws={"size": 25}, xticklabels=xx, yticklabels=yy, vmax=1, square=True, cmap="Blues")
g = sns.heatmap(matrix, annot=True, fmt='.1f', annot_kws={"size": 34}, xticklabels=xx, yticklabels=yy, vmin=0, vmax=100, square=True, cmap="Oranges")

g.set_xticklabels(g.get_xticklabels(), rotation=0, ha="center", fontsize=28, position=(0,1))
g.set_yticklabels(g.get_yticklabels(), fontsize=28,)

fig.savefig('cross2.pdf',dpi=144)

plt.show()

