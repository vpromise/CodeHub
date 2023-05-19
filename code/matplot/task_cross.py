import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.rc('font',family='liberation Serif')
# import matplotlib
# print(matplotlib.get_cachedir())

xx = ['Step-1', 'Step-2','Step-3', 'Step-4']
yy = ['Kvasir-SEG', 'DFUC', 'TN3K', 'ADNI']


# matrix1 = np.array([[75.9, 03.1, 06.4, 00.0, 21.4],
#                     [51.6, 49.6, 17.5, 00.0, 29.7],
#                     [20.2, 07.2, 60.6, 00.0, 22.0],
#                     [01.5, 02.2, 16.7, 48.8, 17.3]]
#                  )

# matrix2 = np.array([[75.9, 03.1, 06.4, 00.0, 21.4],
#                     [67.4, 50.8, 15.4, 00.0, 33.4],
#                     [61.6, 41.7, 60.5, 00.0, 41.0],
#                     [57.1, 37.7, 49.2, 47.8, 48.0]]
#                  )
# matrix1 = np.array([[75.9, 03.1, 06.4, 00.0],
#                     [51.6, 49.6, 17.5, 00.0],
#                     [20.2, 07.2, 60.6, 00.0],
#                     [01.5, 02.2, 16.7, 48.8]]
#                  ).T

# matrix2 = np.array([[75.9, 03.1, 06.4, 00.0],
#                     [67.4, 50.8, 15.4, 00.0],
#                     [61.6, 41.7, 60.5, 00.0],
#                     [57.1, 37.7, 49.2, 47.8]]
#                  ).T

matrix1 = np.array([[75.9, 0,0,0],
                    [51.6, 49.6, 0, 00.0],
                    [20.2, 07.2, 60.6, 00.0],
                    [01.5, 02.2, 16.7, 48.8]]
                 ).T

matrix2 = np.array([[75.9, 0, 0, 00.0],
                    [67.4, 50.8, 0, 00.0],
                    [61.6, 41.7, 60.5, 00.0],
                    [57.1, 37.7, 49.2, 47.8]]
                 ).T

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.06, bottom=0.06, right=0.97, top=.94)
fig.set_size_inches(12,12)
# im = ax.imshow(matrix1)

# ax.set_title('Sequential Training', fontsize=36)
ax.set_title('Rehearsal Training', fontsize=36)

sns.set(font_scale=4)

g = sns.heatmap(matrix2, annot=True, fmt='.1f', vmin=0, vmax=100, annot_kws={"size": 40}, xticklabels=xx, yticklabels=yy, square=True, cmap="YlOrRd", cbar=False, linewidths=3,linecolor="white")

# g.set_xticklabels(g.get_xticklabels(), rotation=0, ha="center", fontsize=22, position=(0,1))
g.set_xticklabels(g.get_xticklabels(), fontsize=34,)
g.set_yticklabels(g.get_yticklabels(), fontsize=34,)


fig.savefig('task_reh.pdf',dpi=144)

plt.show()

