import numpy as np
import matplotlib as mpl
# mpl.use('pdf')
import matplotlib.pyplot as plt
plt.rc('font',family='liberation Serif')
x = np.linspace(4,20,17)
# print(x)
y = np.array([46.44,50.01,53.04,70.19,77.28,76.11,77.60,74.44,75.48,71.61,74.04,68.28,65.43,64.16,63.65,57.60,55.60])
y = np.array([46.44,50.01,55.04,70.19,77.28,76.11,75.60,74.44,73.48,71.61,70.04,68.28,65.43,64.16,61.65,57.60,55.60])
plt.figure()
# plt.plot(x, y)

width = 3.487*2
height = width / 1.618

fig, ax = plt.subplots()
fig.subplots_adjust(left=.10, bottom=.13, right=.97, top=.95)
# plot the second curve in this figure with certain parameters

plt.plot(x, y, color='C1', linewidth=1.6, linestyle='-')
plt.scatter([x, ], [y, ], marker='s', color='C1',s=20)

plt.xlabel('heatmap kernel size (pixel)', fontsize=14)
plt.ylabel('PCKh@0.5', fontsize=14)

# plt.grid(linestyle='--',axis='y')
plt.grid(linestyle='--', linewidth = 0.6)
new_ticks = np.linspace(40,85,10)
# print(new_ticks)
plt.yticks(new_ticks,fontsize=10)
plt.xticks(np.linspace(3,21,19),fontsize=10)

for j, k in zip(x[0:4], y[0:4]):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(j-0.4, k+0.4 , '%.2f' % k, ha='center', va='bottom',fontsize=11)

for j, k in zip(x[5:17], y[5:17]):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(j+0.2, k+0.4, '%.2f' % k, ha='center', va='bottom',fontsize=11)
plt.text(x[4], y[4]+0.4 , '%.2f' % y[4], ha='center', va='bottom',fontsize=11)

fig.set_size_inches(width, height)
plt.show()
fig.savefig('start_kernel_size.pdf',dpi=300)

