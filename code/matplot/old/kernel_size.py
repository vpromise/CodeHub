import numpy as np
import matplotlib as mpl
# mpl.use('pdf')
import matplotlib.pyplot as plt
plt.rc('font',family='liberation Serif')

x = np.linspace(4,20,17)
# print(x)
y = np.array([19.2341232,12.8358197,10.9665258,10.44656872,10.01027201,10.42559279,10.71222695,11.5734564,11.90967922,12.29723346,13.03401585,13.26521621,13.90301256,14.30221215,15.08611497,15.83918312,17.01944148])
yy = np.array([16.2341232,12.8358197,10.9665258,10.44656872,10.01027201,10.42559279,10.71222695,11.5734564,11.90967922,12.29723346,13.03401585,13.26521621,13.90301256,14.30221215,15.08611497,15.83918312,17.01944148])
y1 = np.array([33, 16, 12.71, 11.91, 10.66, 11.67, 12.2, 13.49, 13.55, 14.74, 13.89, 14.95, 16.57, 17.39, 17.35, 17.53, 17.44])
y2 = np.array([0.35525, 0.45375, 0.5035, 0.52675, 0.575, 0.51075, 0.49475, 0.3855, 0.37625, 0.349, 0.3515, 0.35625, 0.2495, 0.23575, 0.24575, 0.24175, 0.289])
# plt.figure()
# plt.plot(x, y)

width = 3.487*2
height = width / 1.618

fig, ax = plt.subplots()
fig.subplots_adjust(left=.10, bottom=.13, right=.97, top=.95)
# plot the second curve in this figure with certain parameters

plt.plot(x, y, color='C1', linewidth=1.6, linestyle='-')
plt.scatter([x, ], [y, ], marker='o', color='C1',s=20)

plt.xlabel('heatmap kernel size $\sigma$ (pixel)', fontsize=14)
plt.ylabel('2DPE (pixel)', fontsize=14)

# plt.grid(linestyle='--',axis='y')
plt.grid(linestyle='--', linewidth = 0.6)
new_ticks = np.linspace(9,20,12)
print(new_ticks)
plt.yticks(new_ticks,fontsize=10)
plt.xticks(np.linspace(3,21,19),fontsize=10)

for j, k in zip(x[0:4], y[0:4]):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(j-0.4, k-0.7 , '%.2f' % k, ha='center', va='bottom',fontsize=12)

for j, k in zip(x[5:17], y[5:17]):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(j+0.4, k-0.7, '%.2f' % k, ha='center', va='bottom',fontsize=12)
plt.text(x[4], y[4]-0.7 , '%.2f' % y[4], ha='center', va='bottom',fontsize=12)

fig.set_size_inches(width, height)
plt.show()
fig.savefig('./vis/start_kernel_size.pdf',dpi=300)

