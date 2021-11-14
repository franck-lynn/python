import numpy as np
import matplotlib.pyplot as plt

# a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
# # https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

# plt.plot(a)
# plt.show()

# x = np.linspace(0, 5, 20)
# y = np.linspace(0, 10, 20)
# plt.plot(x, y, 'purple') # line
# plt.plot(x, y, 'o')      # dots
# plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
plt.show()