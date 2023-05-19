import numpy as np
import matplotlib as mpl
# mpl.use('pdf')
import matplotlib.pyplot as plt
plt.rc('font',family='liberation Serif')
from numpy.core.fromnumeric import size
# plt.style.use(['science','ieee','no-latex'])
x = np.linspace(0,4,5)

xx = ['PolypBenchmark', 'BCCD', 'CPM-17', 'DFUC', 'ISIC2016', 'ADNI', 'LUNA16', 'TBX11k', 'TN3K']
y1 = np.array([[4.3, 27.1, 26.2, 25.9, 32.8, 00.0, 00.0, 00.4, 12.2], 
              [29.0, 26.8, 27.7, 26.3, 31.4, 00.0, 00.1, 00.3, 10.7], 
              [45.0, 26.9, 27.4, 26.4, 31.3, 00.0, 00.0, 00.3, 11.7], 
              [57.8, 27.7, 24.9, 26.2, 28.8, 00.0, 00.0, 00.3, 11.0], 
              [68.1, 26.6, 24.0, 25.1, 29.8, 00.0, 00.0, 00.3, 11.1]])
y2 = np.array([[38.4, 27.1, 26.2, 25.9, 32.8, 00.0, 00.0, 00.4, 12.2],
              [36.8, 22.7, 27.8, 26.5, 32.2, 01.7, 00.0, 00.3, 05.8],
              [32.5, 22.3, 28.8, 27.6, 30.9, 15.1, 00.0, 00.1, 04.2],
              [24.3, 15.8, 25.7, 26.1, 26.2, 39.5, 00.2, 00.0, 02.3],
              [00.0, 00.2, 00.3, 00.0, 00.1, 48.6, 00.0, 00.0, 00.0]])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24,14), )


plt.xticks(np.linspace(0,4,5),fontsize=26)
ax1.set_xticklabels(['zero-shot', '1-shot','10-shot', '100-shot', 'full data'], rotation = 0, fontsize=27)


plt.ylim((-2.5,72.5))
plt.yticks(np.linspace(0,70,8,),fontsize=26)
plt.grid(linestyle='-.', linewidth = 0.5)
plt.ylabel('AP(%)', fontsize=26)

l1, = ax1.plot(x, y1[:,0], '-', marker=' ', label='PolypBenchmark', linewidth=3, ms=3.8)
l2, = ax1.plot(x, y1[:,1], '-', marker=' ', label='BCCD',           linewidth=3, ms=3.8)
l3, = ax1.plot(x, y1[:,2], '-', marker=' ', label='CPM-17',         linewidth=3, ms=3.8)
l9, = ax1.plot(x, y1[:,3], '-', marker=' ', label='DFUC',           linewidth=3, ms=3.8)
l4, = ax1.plot(x, y1[:,4], '-', marker=' ', label='ISIC2016',       linewidth=3, ms=3.8)
l5, = ax1.plot(x, y1[:,5], '-', marker=' ', label='ADNI',           linewidth=3, ms=3.8)
l6, = ax1.plot(x, y1[:,6], '-', marker=' ', label='LUNA16',         linewidth=3, ms=3.8)
l7, = ax1.plot(x, y1[:,7], '-', marker=' ', label='TBX11k',         linewidth=3, ms=3.8)
l8, = ax1.plot(x, y1[:,8], '-', marker=' ', label='TN3K',           linewidth=3, ms=3.8)

# plt.legend(loc=2, fontsize=19, ncol=9, bbox_to_anchor=(-0.072, 1.11), borderaxespad = 0.) 


# fig.savefig('kvasir.pdf',dpi=144)
# plt.show()




plt.xticks(np.linspace(0,4,5),fontsize=26)
ax2.set_xticklabels(['zero-shot', '1-shot','10-shot', '100-shot', 'full data'], rotation = 0, fontsize=27)

plt.ylim((-2.5,52.5))
plt.yticks(np.linspace(0,50,6,),fontsize=26)
plt.grid(linestyle='-.', linewidth = 0.5)

l1, = ax2.plot(x, y2[:,0], '-', marker=' ', label='Polyp BM', linewidth=3, ms=3.8)
l2, = ax2.plot(x, y2[:,1], '-', marker=' ', label='BCCD',           linewidth=3, ms=3.8)
l3, = ax2.plot(x, y2[:,2], '-', marker=' ', label='CPM-17',         linewidth=3, ms=3.8)
l9, = ax2.plot(x, y2[:,3], '-', marker=' ', label='DFUC',           linewidth=3, ms=3.8)
l4, = ax2.plot(x, y2[:,4], '-', marker=' ', label='ISIC2016',       linewidth=3, ms=3.8)
l5, = ax2.plot(x, y2[:,5], '-', marker=' ', label='ADNI',           linewidth=3, ms=3.8)
l6, = ax2.plot(x, y2[:,6], '-', marker=' ', label='LUNA16',         linewidth=3, ms=3.8)
l7, = ax2.plot(x, y2[:,7], '-', marker=' ', label='TBX11k',         linewidth=3, ms=3.8)
l8, = ax2.plot(x, y2[:,8], '-', marker=' ', label='TN3K',           linewidth=3, ms=3.8)



# plt.legend(loc='best',fontsize=16)
plt.legend(loc=2, fontsize=22, ncol=9, bbox_to_anchor=(-1.5, 1.12), borderaxespad = 0.) 


# fig.set_size_inches(width, height)
plt.savefig('new.pdf',dpi=144)

plt.show()