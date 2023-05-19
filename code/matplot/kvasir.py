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
#               [0.407, 0.268, 0.277, 0.263, 0.314, 0.000, 0.001, 0.003, 0.107], 
#               [0.461, 0.269, 0.274, 0.264, 0.313, 0.000, 0.000, 0.003, 0.117], 
#               [0.532, 0.277, 0.249, 0.262, 0.288, 0.000, 0.000, 0.003, 0.110], 
#               [0.665, 0.266, 0.240, 0.251, 0.298, 0.000, 0.000, 0.003, 0.111]])

y = np.array([[43.7, 27.1, 26.2, 25.9, 32.8, 00.0, 00.0, 00.4, 12.2], 
              [40.7, 26.8, 27.7, 26.3, 31.4, 00.0, 00.1, 00.3, 10.7], 
              [46.1, 26.9, 27.4, 26.4, 31.3, 00.0, 00.0, 00.3, 11.7], 
              [53.2, 27.7, 24.9, 26.2, 28.8, 00.0, 00.0, 00.3, 11.0], 
              [66.5, 26.6, 24.0, 25.1, 29.8, 00.0, 00.0, 00.3, 11.1]])

y = np.array([[4.3, 27.1, 26.2, 25.9, 32.8, 00.0, 00.0, 00.4, 12.2], 
              [29.0, 26.8, 27.7, 26.3, 31.4, 00.0, 00.1, 00.3, 10.7], 
              [45.0, 26.9, 27.4, 26.4, 31.3, 00.0, 00.0, 00.3, 11.7], 
              [57.8, 27.7, 24.9, 26.2, 28.8, 00.0, 00.0, 00.3, 11.0], 
              [68.1, 26.6, 24.0, 25.1, 29.8, 00.0, 00.0, 00.3, 11.1]])
# plt.figure()


# height = 9
# width = 1.2*height
height = 10.85
width = 1.1*height

fig, ax = plt.subplots()
# fig.subplots_adjust(left=.075, bottom=.1, right=.99, top=.99)
fig.subplots_adjust(left=.09, bottom=.05, right=.97, top=.89)

plt.xticks(np.linspace(0,4,5),fontsize=26)

# ax.set_xlabel(['zero-shot', '1-shot','10-shot', '100-shot', 'full-data'], fontsize=20,)
ax.set_xticklabels(['zero-shot', '1-shot','10-shot', '100-shot', 'full data'], rotation = 0, fontsize=28)


plt.ylim((-2.5,72.5))
plt.yticks(np.linspace(0,70,8,),fontsize=26)
plt.grid(linestyle='-.', linewidth = 0.5)
# set tick labels

# plt.title('')
# plt.xlabel('shot', fontsize=24)
plt.ylabel('AP(%)', fontsize=28)

# plt.annotate("Train", xy=(2.7,53.2), xytext=(1.5,62), color='black', fontsize=28, arrowprops=dict(facecolor='gray', width=2, shrink=0.05))

l1, = plt.plot(x, y[:,0], '-', marker=' ', label='Polyp BM', linewidth=4.5, ms=3.8)
l2, = plt.plot(x, y[:,1], '-', marker=' ', label='BCCD',       linewidth=3, ms=3.8)
l3, = plt.plot(x, y[:,2], '-', marker=' ', label='CPM-17',     linewidth=3, ms=3.8)
l9, = plt.plot(x, y[:,3], '-', marker=' ', label='DFUC',       linewidth=3, ms=3.8)
l4, = plt.plot(x, y[:,4], '-', marker=' ', label='ISIC2016',   linewidth=3, ms=3.8)
l5, = plt.plot(x, y[:,5], '-', marker=' ', label='ADNI',       linewidth=3, ms=3.8)
l6, = plt.plot(x, y[:,6], '-', marker=' ', label='LUNA16',     linewidth=3, ms=3.8)
l7, = plt.plot(x, y[:,7], '-', marker=' ', label='TBX11k',     linewidth=3, ms=3.8)
l8, = plt.plot(x, y[:,8], '-', marker=' ', label='TN3K',       linewidth=3, ms=3.8)



# plt.legend(loc='best',fontsize=16)
plt.legend(loc=2, fontsize=20, ncol=5, bbox_to_anchor=(-0.072, 1.11), borderaxespad = 0.) 


fig.set_size_inches(width, height)
fig.savefig('kvasir.pdf',dpi=144)

plt.show()