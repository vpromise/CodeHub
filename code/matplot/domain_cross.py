import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.rc('font',family='liberation Serif')
# import matplotlib
# print(matplotlib.get_cachedir())

xx = ['Step-1', 'Step-2','Step-3', 'Step-4']
yy = ['Kvasir-SEG', 'BKAI', 'CVC-ClinicDB', 'SinGAN']


# matrix1 = np.array([[75.9, 62.1, 59.6, 67.8, 62.2],
#                     [73.5, 78.7, 65.1, 66.8, 67.1],
#                     [69.9, 70.3, 80.8, 66.3, 67.9],
#                     [18.4, 26.8, 19.2, 85.2, 27.2]]
#                  )


# matrix2 = np.array([[75.9, 62.1, 59.6, 67.8, 62.2],
#                     [73.8, 78.0, 65.4, 68.5, 67.9],
#                     [71.8, 73.9, 74.6, 68.8, 68.4],
#                     [65.6, 68.9, 64.5, 84.4, 64.9]]
#                  )
# matrix1 = np.array([[75.9, 62.1, 59.6, 67.8],
#                     [73.5, 78.7, 65.1, 66.8],
#                     [69.9, 70.3, 80.8, 66.3],
#                     [18.4, 26.8, 19.2, 85.2]]
#                  ).T


# matrix2 = np.array([[75.9, 62.1, 59.6, 67.8],
#                     [73.8, 78.0, 65.4, 68.5],
#                     [71.8, 73.9, 74.6, 68.8],
#                     [65.6, 68.9, 64.5, 84.4]]
#                  ).T
matrix1 = np.array([[75.9, 0,0,0],
                    [73.5, 78.7, 0,0],
                    [69.9, 70.3, 80.8, 0],
                    [18.4, 26.8, 19.2, 85.2]]
                 ).T


matrix2 = np.array([[75.9, 0,0,0],
                    [73.8, 78.0, 0,0],
                    [71.8, 73.9, 74.6, 0],
                    [65.6, 68.9, 64.5, 84.4]]
                 ).T

fig, ax = plt.subplots()
fig.subplots_adjust(left=0.06, bottom=0.06, right=0.97, top=.94)
fig.set_size_inches(12,12)
# im = ax.imshow(matrix1)


ax.set_title('Sequential Training', fontsize=36)
# ax.set_title('Rehearsal Training', fontsize=36)

sns.set(font_scale=4)

g = sns.heatmap(matrix1, annot=True, fmt='.1f', vmin=0, vmax=100, annot_kws={"size": 40}, xticklabels=xx, yticklabels=yy, square=True, cmap="YlGn", cbar=False, linewidths=3,linecolor="white")

# g.set_xticklabels(g.get_xticklabels(), rotation=0, ha="center", fontsize=22, position=(0,1))
g.set_xticklabels(g.get_xticklabels(), fontsize=34)
g.set_yticklabels(g.get_yticklabels(), fontsize=34)


fig.savefig('domain_seq.pdf',dpi=144)

plt.show()

