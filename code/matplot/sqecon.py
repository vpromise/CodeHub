import numpy as np
import matplotlib as mpl

import matplotlib.pyplot as plt
plt.rc('font',family='liberation Serif')
from numpy.core.fromnumeric import size
# plt.style.use(['science','ieee','no-latex'])

x = np.linspace(0,3,4)

xx = ['Kvasir_Seg', 'BCCD', 'CPM-17', 'DFUC', 'ISIC2016', 'ADNI', 'LUNA16', 'TBX11k', 'TN3K']

# y = np.array([  [0.759, 0.031, 0.064, 0.000, 0.214],
#                 [0.516, 0.496, 0.175, 0.000, 0.297],
#                 [0.202, 0.072, 0.606, 0.000, 0.220],
#                 [0.015, 0.022, 0.167, 0.488, 0.173],
[0.759, 0.031, 0.064, 0.000]
[0.674, 0.508, 0.154, 0.000]
[0.616, 0.417, 0.605, 0.000]
[0.571, 0.377, 0.492, 0.478]


y = np.array([  [75.9, 03.1, 06.4, 00.0, 21.4, 75.9, 03.1, 06.4, 00.0, 21.4],
                [51.6, 49.6, 17.5, 00.0, 29.7, 67.4, 50.8, 15.4, 00.0, 33.4],
                [20.2, 07.2, 60.6, 00.0, 22.0, 61.6, 41.7, 60.5, 00.0, 41.0],
                [01.5, 02.2, 16.7, 48.8, 17.3, 57.1, 37.7, 49.2, 47.8, 48.0]])
# plt.figure()



height = 10
width = 1.1*height

fig, ax = plt.subplots()
# fig.subplots_adjust(left=.075, bottom=.1, right=.99, top=.99)
fig.subplots_adjust(left=.09, bottom=.05, right=.97, top=.89)

plt.xticks(np.linspace(0,3,4),fontsize=26)

# ax.set_xlabel(['zero-shot', '1-shot','10-shot', '100-shot', 'full-data'], fontsize=20,)
ax.set_xticklabels(['Step-1', 'Step-2','Step-3', 'Step-4'], rotation = 0, fontsize=26)


plt.ylim((-2.5,77.5))
plt.yticks(np.linspace(0,80,9,),fontsize=26)
plt.grid(linestyle='-.', linewidth = 0.5)
# set tick labels

# plt.title('')
# plt.xlabel('shot', fontsize=24)
plt.ylabel('AP(%)', fontsize=26)



l1,  = plt.plot(x, y[:,0], '-.', marker=' ', label='Kvasir-SEG$^{\\ast}$', linewidth=3, ms=3.8, color='tab:blue')
# l2,  = plt.plot(x, y[:,1], '-.', marker=' ', label='DFUC',       linewidth=3, ms=3.8, color='g')
# l3,  = plt.plot(x, y[:,2], '-.', marker=' ', label='TN3K',       linewidth=3, ms=3.8, color='c')
# l4,  = plt.plot(x, y[:,3], '-.', marker=' ', label='ADNI',       linewidth=3, ms=3.8, color='m')

l6,  = plt.plot(x, y[:,5], '-',  marker=' ', label='Kvasir-SEG$^{\\bullet}$', linewidth=3, ms=3.8, color='tab:blue')
l5,  = plt.plot(x, y[:,4], '-.', marker=' ', label='AVG$^{\\ast}$',        linewidth=3, ms=3.8, color='tomato')

# l7,  = plt.plot(x, y[:,6], '-',  marker=' ', label='DFUC',       linewidth=3, ms=3.8, color='g')
# l8,  = plt.plot(x, y[:,7], '-',  marker=' ', label='TN3K',       linewidth=3, ms=3.8, color='c')
# l9,  = plt.plot(x, y[:,8], '-',  marker=' ', label='ADNI',       linewidth=3, ms=3.8, color='m')
l10, = plt.plot(x, y[:,9], '-',  marker=' ', label='AVG$^{\\bullet}$',        linewidth=3, ms=3.8, color='tomato')


# plt.legend(loc='best',fontsize=16, ncol=5)

plt.legend(loc=2, fontsize=21, ncol=4, bbox_to_anchor=(-0.024, 1.1), borderaxespad = 0.) 


fig.set_size_inches(width, height)
fig.savefig('seq_task.pdf',dpi=300)

plt.show()