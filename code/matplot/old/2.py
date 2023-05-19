import numpy as np
import matplotlib as mpl
# mpl.use('pdf')
import matplotlib.pyplot as plt
plt.rc('font',family='liberation Serif')
from numpy.core.fromnumeric import size
# plt.style.use(['science','ieee','no-latex'])

x = np.linspace(10,120,12)
# static8 = np.array([7.23,6.86,6.65,6.53,6.44,6.40,6.25,6.23,6.14,6.10])
# stage = np.array([7.40,6.90,6.21,5.86,5.80,5.59,5.46,5.44,5.34,5.41])
# linear = np.array([7.08,6.41,6.11,5.85,5.67,5.55,5.51,5.47,5.48,5.43])
# exp = np.array([6.75,5.99,5.66,5.49,5.43,5.40,5.40,5.39,5.33,5.31])

static8 = np.array([7.27,6.86,6.65,6.53,6.44,6.38,6.32,6.27,6.23,6.21,6.20,6.20])
stage   = np.array([7.40,6.90,6.51,6.26,6.08,5.92,5.86,5.74,5.62,5.58,5.56,5.55])
# stage   = np.array([7.40,6.90,6.21,5.86,5.80,5.59,5.46,5.44,5.34,5.41])
linear  = np.array([7.08,6.41,6.11,5.85,5.67,5.55,5.51,5.47,5.46,5.43,5.42,5.42])
exp     = np.array([6.75,5.99,5.66,5.49,5.41,5.36,5.33,5.31,5.30,5.30,5.30,5.30])

# plt.figure()

width = 3.487*2
height = width / 1.618

fig, ax = plt.subplots()
fig.subplots_adjust(left=.115, bottom=.13, right=.97, top=.95)

plt.xticks(np.linspace(0,130,14),fontsize=10)

plt.ylim((5, 7.75))
plt.yticks(np.linspace(5,7.75,12),fontsize=10)
plt.grid(linestyle='-.', linewidth = 0.5)
# set tick labels

# plt.title('')
# plt.xlabel('train epoch', fontsize=14)
# plt.ylabel('2D pose error (pixel)', fontsize=14)
plt.xlabel('训练周期', fontsize=14)
plt.ylabel('2D pose error (pixel)', fontsize=14)


# l1, = plt.plot(x, static4, label='static 4')
# l2, = plt.plot(x, static6, label='static 6')
l3, = plt.plot(x, static8, '-', marker='o', label='fixed',linewidth=1.6, ms=3.8)
l4, = plt.plot(x, stage, '--', marker='s',label='stage',linewidth=1.6, ms=3.8)
l5, = plt.plot(x, linear, '-.', marker='^', label='linear',linewidth=1.6, ms=3.8)
l6, = plt.plot(x, exp, ':', marker='x',label='curve',linewidth=1.6, ms=3.8)
# l7, = plt.plot(x, exp2, label='linear line')
# l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='square line')


plt.legend(loc='best',fontsize=12)


fig.set_size_inches(width, height)
fig.savefig('training1.pdf',dpi=300)

plt.show()