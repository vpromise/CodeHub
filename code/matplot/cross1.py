import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# import matplotlib
# print(matplotlib.get_cachedir())
plt.rc('font',family='liberation Serif')

# xx = ['BKAI', 'CVC_ClinicDB', 'Kvasir-SEG', 'Kvasir-Sessile', 'SinGAN-Seg-polyps', 'CVC-300', 'CVC-ColonDB', 'ETIS-LaribPolypDB']
xx = ['BKAI', 'CVC-ClinicDB', 'Kvasir-SEG', 'Kvasir-Sessile', 'SinGAN']
yy = ['BKAI', 'CVC-ClinicDB', 'Kvasir-SEG', 'Kvasir-Sessile', 'SinGAN']
yy = ['BKAI', 'CVC-ClinicDB', 'Kvasir-SEG', 'Kvasir-Sessile', 'SinGAN']
# yy = ['SinGAN-Seg-polyps', 'Kvasir-Sessile', 'Kvasir-SEG', 'CVC_ClinicDB', 'BKAI']


# matrix = np.array( [[0.010, 0.100, 0.010, 0.100, 0.010],
#                     [0.793, 0.658, 0.691, 0.608, 0.644],
#                     [0.645, 0.822, 0.616, 0.604, 0.628],
#                     [0.621, 0.596, 0.759, 0.600, 0.668],
#                     [0.591, 0.545, 0.692, 0.627, 0.599],
#                     [0.268, 0.099, 0.180, 0.033, 0.931]]
#                  )
matrix = np.array( [[79.3, 65.8, 69.1, 60.8, 64.4],
                    [64.5, 82.2, 61.6, 60.4, 62.8],
                    [62.1, 59.6, 75.9, 60.0, 66.8],
                    [59.1, 54.5, 69.2, 62.7, 59.9],
                    [26.8, 09.9, 18.0, 03.3, 93.1]]
                 )


fig, ax = plt.subplots()
# fig.subplots_adjust(left=.05, bottom=0.03, right=0.99, top=.94)
# fig.set_size_inches(17,14)

fig.subplots_adjust(left=.02, bottom=0.015, right=1.05, top=.78)
fig.set_size_inches(15,15)

im = ax.imshow(matrix)


# ax.set_title('cross validation results', )
ax.xaxis.tick_top()
# We want to show all ticks...
ax.set_xticks(np.arange(len(xx)))
ax.set_yticks(np.arange(len(yy)))


#Rotate the tick labels and set their alignment.
# plt.setp(ax.get_xticklabels(), rotation=45, ha="center",
#          rotation_mode="anchor")



# ... and label them with the respective list entries
# ax.set_ylabel(yy, fontsize=15, color='r')

#Rotate the tick labels and set their alignment.
# plt.setp(ax.get_xticklabels(), rotation=-45, ha="center",
#          rotation_mode="anchor")
sns.set(font_scale=2)

g = sns.heatmap(matrix, annot=True, fmt='.1f', annot_kws={"size": 34}, xticklabels=xx, yticklabels=yy, vmin=0, vmax=100, cbar=True, square=True, cmap="Blues")
# g = sns.heatmap(matrix, annot=True, fmt='.3f', annot_kws={"size": 25}, xticklabels=xx, yticklabels=yy, vmax=1, square=True, cmap="YlOrBr")


g.set_xticklabels(g.get_xticklabels(), rotation=0, ha="center", fontsize=28, position=(0,1))
g.set_yticklabels(g.get_yticklabels(), fontsize=28,)

fig.savefig('cross1.pdf',dpi=144)

plt.show()

