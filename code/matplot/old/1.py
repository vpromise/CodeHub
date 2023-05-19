import matplotlib.pyplot as plt
import numpy as np
import math
# plt.style.use(['science','ieee','no-latex'])

x = np.linspace(0, 120, 121)
static8 = np.ones((121))*8
static6 = np.ones((121))*6
static4 = np.ones((121))*4
stage = np.hstack((np.hstack((8*np.ones((1,40)),6*np.ones((1,40)))),4*np.ones((1,41)))).reshape(121)
linear = np.maximum((8-x/20),4)
exp = np.array(np.exp((27.6-x)/20)+4)
exp2 = np.array((np.exp((-1/110)*x))+1)**3

plt.figure()
# set x limits
# plt.xlim((-1, 2))
# plt.ylim((-2, 3))

# set new sticks
# new_sticks = np.linspace(-1, 2, 5)
# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
# plt.grid(linestyle='-.')
# set tick labels

# plt.title('')
plt.xlabel('train epoch', fontsize=12)
plt.ylabel('heatmap kernel size (pixel)', fontsize=12)



# l1, = plt.plot(x, static4, label='static 4')
# l2, = plt.plot(x, static6, label='static 6')
l3, = plt.plot(x, static8, '-',label='fixed', linewidth=1.6)
l4, = plt.plot(x, stage, '--',label='stage', linewidth=1.6)
l5, = plt.plot(x, linear, '-.',label='linear', linewidth=1.6)
l6, = plt.plot(x, exp, ':',label='curve', linewidth=1.6)
# l7, = plt.plot(x, exp2, label='linear line')
# l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')




plt.legend(loc='best',fontsize=12)
# plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
# the "," is very important in here l1, = plt... and l2, = plt... for this step
"""legend( handles=(line1, line2, line3),
           labels=('label1', 'label2', 'label3'),
           'upper right')
    The *loc* location codes are::

          'best' : 0,          (currently not supported for figure legends)
          'upper right'  : 1,
          'upper left'   : 2,
          'lower left'   : 3,
          'lower right'  : 4,
          'right'        : 5,
          'center left'  : 6,
          'center right' : 7,
          'lower center' : 8,
          'upper center' : 9,
          'center'       : 10,"""

fig.set_size_inches(width, height)
fig.savefig('plot.pdf')

plt.show()
