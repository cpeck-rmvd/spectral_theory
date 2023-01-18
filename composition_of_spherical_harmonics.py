# Theorem: any function on the surface of a sphere can be represented as a linear combination of spherical harmonics.


import numpy as np
from scipy.special import sph_harm
from numpy.polynomial.legendre import P

# Define the degree and order of the spherical harmonics
l = 3
m = 2

# Define the spherical coordinates (theta, phi)
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2*np.pi, 100)

# Generate the spherical harmonics
Y = sph_harm(m, l, phi, theta)

# Generate the associated Legendre polynomials
P = P(np.cos(theta))

# Plot the spherical harmonics
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta), rstride=1, cstride=1, facecolors=Y)
plt.show()
