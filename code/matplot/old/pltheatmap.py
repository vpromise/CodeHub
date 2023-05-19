import numpy as np

import matplotlib.pyplot as plt

path = '/home/v/Work/caren-pose-2d.hg/saver/plt/24.npy'

a = np.load(path)
print(a.shape)
plt.imshow(a[0][0])
plt.show()