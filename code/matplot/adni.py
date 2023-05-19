import numpy as np
import matplotlib as mpl
# mpl.use('pdf')
import matplotlib.pyplot as plt
plt.rc('font',family='liberation Serif')
from numpy.core.fromnumeric import size
# plt.style.use(['science','ieee','no-latex'])

x = np.linspace(0,4,5)

xx = ['Kvasir_Seg', 'BCCD', 'CPM-17', 'DFUC', 'ISIC2016', 'ADNI', 'LUNA16', 'TBX11k', 'TN3K']

# y = np.array([[0.437, 0.271, 0.262, 0.259, 0.328, 0.000, 0.000, 0.004, 0.122],
#               [0.323, 0.227, 0.278, 0.265, 0.322, 0.017, 0.000, 0.003, 0.058],
#               [0.284, 0.223, 0.288, 0.276, 0.309, 0.151, 0.000, 0.001, 0.042],
#               [0.252, 0.158, 0.257, 0.261, 0.262, 0.395, 0.002, 0.000, 0.023],
#               [0.000, 0.002, 0.003, 0.000, 0.001, 0.486, 0.000, 0.000, 0.000]])

y = np.array([[43.7, 27.1, 26.2, 25.9, 32.8, 00.0, 00.0, 00.4, 12.2],
              [32.3, 22.7, 27.8, 26.5, 32.2, 01.7, 00.0, 00.3, 05.8],
              [28.4, 22.3, 28.8, 27.6, 30.9, 15.1, 00.0, 00.1, 04.2],
              [25.2, 15.8, 25.7, 26.1, 26.2, 39.5, 00.2, 00.0, 02.3],
              [00.0, 00.2, 00.3, 00.0, 00.1, 48.6, 00.0, 00.0, 00.0]])
y = np.array([[38.4, 27.1, 26.2, 25.9, 32.8, 00.0, 00.0, 00.4, 12.2],
              [36.8, 22.7, 27.8, 26.5, 32.2, 01.7, 00.0, 00.3, 05.8],
              [32.5, 22.3, 28.8, 27.6, 30.9, 15.1, 00.0, 00.1, 04.2],
              [24.3, 15.8, 25.7, 26.1, 26.2, 39.5, 00.2, 00.0, 02.3],
              [00.0, 00.2, 00.3, 00.0, 00.1, 48.6, 00.0, 00.0, 00.0]])

# plt.figure()


height = 10.85
width = 1.1*height

fig, ax = plt.subplots()
# fig.subplots_adjust(left=.075, bottom=.1, right=.99, top=.99)
fig.subplots_adjust(left=.09, bottom=.05, right=.97, top=.89)

plt.xticks(np.linspace(0,4,5),fontsize=26)

# ax.set_xlabel(['zero-shot', '1-shot','10-shot', '100-shot', 'full-data'], fontsize=20,)
ax.set_xticklabels(['zero-shot', '1-shot','10-shot', '100-shot', 'full data'], rotation = 0, fontsize=28)


plt.ylim((-2.5,52.5))
plt.yticks(np.linspace(0,50,6,),fontsize=26)
plt.grid(linestyle='-.', linewidth = 0.5)
# set tick labels

# plt.title('')
# plt.xlabel('shot', fontsize=24)
plt.ylabel('AP(%)', fontsize=28)



l1, = plt.plot(x, y[:,0], '-', marker=' ', label='Polyp BM', linewidth=3, ms=3.8)
l2, = plt.plot(x, y[:,1], '-', marker=' ', label='BCCD',       linewidth=3, ms=3.8)
l3, = plt.plot(x, y[:,2], '-', marker=' ', label='CPM-17',     linewidth=3, ms=3.8)
l9, = plt.plot(x, y[:,3], '-', marker=' ', label='DFUC',       linewidth=3, ms=3.8)
l4, = plt.plot(x, y[:,4], '-', marker=' ', label='ISIC2016',   linewidth=3, ms=3.8)
l5, = plt.plot(x, y[:,5], '-', marker=' ', label='ADNI',     linewidth=4.5, ms=3.8)
l6, = plt.plot(x, y[:,6], '-', marker=' ', label='LUNA16',     linewidth=3, ms=3.8)
l7, = plt.plot(x, y[:,7], '-', marker=' ', label='TBX11k',     linewidth=3, ms=3.8)
l8, = plt.plot(x, y[:,8], '-', marker=' ', label='TN3K',       linewidth=3, ms=3.8)



# plt.legend(loc='best',fontsize=16, ncol=5)

plt.legend(loc=2, fontsize=20, ncol=5, bbox_to_anchor=(-0.072, 1.11), borderaxespad = 0.) 


fig.set_size_inches(width, height)
fig.savefig('adni.pdf',dpi=144)

plt.show()