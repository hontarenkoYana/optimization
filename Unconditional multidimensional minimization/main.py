import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

from function import f_for_plot
from Nelder_Mead import *
from coordinate_descent import *
from Huk import *
from gradient_descent import *
from conjugate_gradients import *


def grid(xlim, ylim):
    x, y = np.meshgrid(xlim, ylim)
    return x, y


fig = plt.figure(figsize=(15.0, 8.0))
ax = fig.add_subplot(121, projection='3d')
ax.set_aspect('equal')
x, y = grid(np.linspace(-5, 5), np.linspace(-5, 5))
ax.plot_surface(x, y, f_for_plot(x, y), cmap=cm.coolwarm, lw=0.5)

ax = fig.add_subplot(122)
ax.set_aspect('equal')
x, y = grid(np.linspace(-5, 5), np.linspace(-5, 5))
ax.pcolormesh(np.linspace(-5, 5), np.linspace(-5, 5), f_for_plot(x, y), cmap=cm.coolwarm)
plt.show()

print(Nelder_Mead([8, 9], [10, 11], [8, 11], 0.2))
print(Coordinate(np.array([4., 4.]), 10**-6))
print(huk([8., 9.], 10**-6))
print(gradient_descent([8., 9.], 10**-6, 10**-6, 100))
print(Gradient([8., 9.], 10**-6))
