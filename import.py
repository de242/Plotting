
import itertools
import os
import numpy as np

import utils

# Settings
base_dir = 'C:\Users\de242\Desktop\Teslatron RUS\BaFe2As2\mag sweep at low temp\Oct 2016\Waves for 3D fitting'
filename = 'Decreasing field for 5K.csv'
freq_window = (80, 160)
threshold = 0.02


# # Load data files
# with open(os.path.join(base_dir, 'temps.csv'), 'r') as f:
#     temps = [float(l) for l in f.readlines()]
#
# with open(os.path.join(base_dir, 'freqs.csv'), 'r') as f:
#     freqs = [float(l) for l in f.readlines()]
#
# with open(os.path.join(base_dir, 'Amp data.csv'), 'r') as f:
#     data = f.readlines()
#
# num_rows = len(data)
# num_cols = len(data[0].split(','))
#
# X = np.ndarray(shape=(num_rows, num_cols))
# Y = np.ndarray(shape=(num_rows, num_cols))
# Z = np.ndarray(shape=(num_rows, num_cols))

Field, Freq, Amp = utils.load_datafile(os.path.join(base_dir, filename))

# for x, y in itertools.product(range(num_rows), range(num_cols)):
#     X[x, y] = freqs[x]
#     Y[x, y] = temps[y]
#
# for line_number, line in enumerate(data):
#     values = line.split(',')
#     for col_number, cell in enumerate(values):
#         Z[line_number, col_number] = float(cell)

print "Loaded data"

window_indices = utils.window_indices(Freq[:, 0], freq_window)
Freq = Freq[window_indices[0]:window_indices[1], :]
Field = Field[window_indices[0]:window_indices[1], :]
Amp = Amp[window_indices[0]:window_indices[1], :]

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

use_freq = []
use_field = []
use_amp = []

for fr, fi, a in zip(Freq.flatten(), Field.flatten(), Amp.flatten()):
    if a > threshold:
        use_freq.append(fr)
        use_field.append(fi)
        use_amp.append(a)

print "Filtered to {} items".format(len(use_amp))

fig = plt.figure()
ax = fig.gca(projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)
# ax.contour(Freq, Field, Amp, rstride=8, cstride=8, levels=np.linspace(0.005, 0.2, 200), alpha=0.5)
ax.scatter(use_freq, use_field, use_amp)
# ax.plot_trisurf(X.flatten(), Y.flatten(), Z.flatten())
# ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
# ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
# ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
# ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlabel('Freqency')
ax.get_xaxis().get_major_formatter().set_scientific(False)
# ax.set_xlim(1140, 1150)
ax.set_ylabel('Field Strength')
# ax.set_ylim(1140, 1150)
ax.set_zlabel('Amplitude')
# ax.set_zlim(-100, 100)

ax.set_title(filename)
plt.show()