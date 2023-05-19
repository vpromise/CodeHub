import numpy as np
import matplotlib as mpl

import matplotlib.pyplot as plt
plt.rc('font',family='liberation Serif')
from numpy.core.fromnumeric import size
# plt.style.use(['science','ieee','no-latex'])

x = np.linspace(0,3,4)

xx = ['Kvasir_SEG', 'BCCD', 'CPM-17', 'DFUC', 'ISIC2016', 'ADNI', 'LUNA16', 'TBX11k', 'TN3K']


y = np.array([  [75.9, 62.2, 75.9, 62.2],
                [73.5, 67.1, 73.8, 67.9],
                [69.9, 67.9, 71.8, 68.4],
                [18.4, 27.2, 65.6, 64.9]])

# plt.figure()



height = 10
width = 1.1*height

fig, ax = plt.subplots()
# fig.subplots_adjust(left=.075, bottom=.1, right=.99, top=.99)
fig.subplots_adjust(left=.09, bottom=.05, right=.97, top=.89)

plt.xticks(np.linspace(0,3,4),fontsize=26)

# ax.set_xlabel(['zero-shot', '1-shot','10-shot', '100-shot', 'full-data'], fontsize=20,)
ax.set_xticklabels(['Step-1', 'Step-2','Step-3', 'Step-4'], rotation = 0, fontsize=27)


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

l6,  = plt.plot(x, y[:,2], '-',  marker=' ', label='Kvasir-SEG$^{\\bullet}$', linewidth=3, ms=3.8, color='tab:blue')
l5,  = plt.plot(x, y[:,1], '-.', marker=' ', label='AVG$^{\\ast}$',        linewidth=3, ms=3.8, color='tomato')

# l7,  = plt.plot(x, y[:,6], '-',  marker=' ', label='DFUC',       linewidth=3, ms=3.8, color='g')
# l8,  = plt.plot(x, y[:,7], '-',  marker=' ', label='TN3K',       linewidth=3, ms=3.8, color='c')
# l9,  = plt.plot(x, y[:,8], '-',  marker=' ', label='ADNI',       linewidth=3, ms=3.8, color='m')
l10, = plt.plot(x, y[:,3], '-',  marker=' ', label='AVG$^{\\bullet}$',        linewidth=3, ms=3.8, color='tomato')


# plt.legend(loc='best',fontsize=16, ncol=5)

plt.legend(loc=2, fontsize=21, ncol=4, bbox_to_anchor=(-0.024, 1.1), borderaxespad = 0.) 


fig.set_size_inches(width, height)
fig.savefig('seq_domain.pdf',dpi=144)

plt.show()