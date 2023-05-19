import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# sphinx_gallery_thumbnail_number = 2


xx = ['BKAI', 'CVC_ClinicDB', 'Kvasir-SEG', 'Kvasir-Sessile', 'SinGAN-Seg-polyps', 'CVC-300', 'CVC-ColonDB', 'ETIS-LaribPolypDB']
yy = ['BKAI', 'CVC_ClinicDB', 'Kvasir-SEG', 'Kvasir-Sessile', 'SinGAN-Seg-polyps']

matrix = np.array( [[0.793, 0.658, 0.691, 0.608, 0.644, 0.715, 0.485, 0.618],
                    [0.645, 0.822, 0.616, 0.604, 0.628, 0.724, 0.611, 0.532],
                    [0.666, 0.612, 0.751, 0.650, 0.647, 0.656, 0.525, 0.465],
                    [0.591, 0.545, 0.692, 0.627, 0.599, 0.457, 0.489, 0.486],
                    [0.268, 0.099, 0.180, 0.033, 0.931, 0.228, 0.164, 0.143]]
                 )





fig, ax = plt.subplots()
im = ax.imshow(matrix)

# We want to show all ticks...
ax.set_xticks(np.arange(len(xx)))
ax.set_yticks(np.arange(len(yy)))

# ... and label them with the respective list entries
ax.set_xticklabels(xx)
ax.set_yticklabels(yy)

#Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

##Loop over data dimensions and create text annotations.
for i in range(len(yy)):
    for j in range(len(xx)):
        text = ax.text(j, i, matrix[i, j],
                       ha="center", va="center", color="w")

ax.set_title("cross validation results")
fig.tight_layout()
plt.show()
