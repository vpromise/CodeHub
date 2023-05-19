import numpy as np
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
plt.rc('font',family='liberation Serif')
# mpl.rcParams['font.sans-serif'] = 'simsun'


x = np.linspace(0, 120, 121)
static8 = np.ones((121))*8
static6 = np.ones((121))*6
static4 = np.ones((121))*4
stage = np.hstack((np.hstack((8*np.ones((1,41)),6*np.ones((1,40)))),4*np.ones((1,40)))).reshape(121)
linear = np.maximum((8-x/20),4)
exp = np.array(np.exp((27.6-x)/20)+4)
exp2 = np.array((np.exp((-1/110)*x))+1)**3

# width as measured in inkscape
width = 3.7*2
height = width / 1.618

fig, ax = plt.subplots()
fig.subplots_adjust(left=.13, bottom=.13, right=.97, top=.95)


# plt.xticks(fontsize=10)
plt.yticks([4, 6, 8],[r'$\sigma_{min}$', r'$\frac{\sigma_{max}+\sigma_{min}}{2}$',r'$\sigma_{max}$'], fontsize=10)
# plt.yticks([6],[r'$\frac{\sigma_{max}+\sigma_{min}}{2}$'], fontsize = 7)
# plt.yticks([4, 5, 6, 7, 8],[r'$\sigma_{min}$', '', r'$\frac{\sigma_{max}+\sigma_{min}}{2}$', '', r'$\sigma_{max}$'], fontsize=10)
plt.xticks([1, 40, 80, 120],[1,r'$N$',r'$2N$',r'$3N$'], fontsize=10)
# plt.yticks(fontsize=10)
# plt.xlabel('training epoch', fontsize=14)
# plt.ylabel('heatmap kernel size (pixel)', fontsize=14)

plt.xlabel('训练周期', fontsize=14)
plt.ylabel('热力图内核尺寸 (pixel)', fontsize=14)

l3, = plt.plot(x, static8, '-',label='fixed', linewidth=1.6)
l4, = plt.plot(x, stage, '--',label='stage', linewidth=1.6)
l5, = plt.plot(x, linear, '-.',label='linear', linewidth=1.6)
l6, = plt.plot(x, exp, ':',label='curve', linewidth=1.6)

# plt.legend(loc='lower left',fontsize=14)

plt.legend(loc='best',fontsize=14)

fig.set_size_inches(width, height)
fig.savefig('shrinking.pdf',dpi=300)
plt.show()