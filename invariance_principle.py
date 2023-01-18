# Theorem: for a large class of random fields, the distribution of the spherical averages at a fixed radius 
# converges to a Gaussian distribution as the radius increases.

import numpy as np
import matplotlib.pyplot as plt

# Number of realizations
n_realizations = 10000

# Size of each realization
size = 100

# True mean and standard deviation of the random field
true_mean = 0
true_std = 1

# Generate the random field
random_field = np.random.normal(true_mean, true_std, (n_realizations, size))

# Define a function to calculate the spherical averages
def spherical_average(field, radius):
    n_points = field.shape[1]
    spherical_avgs = []
    for i in range(n_points):
        dist = np.abs(np.arange(n_points) - i)
        dist = np.where(dist > n_points/2, n_points - dist, dist)
        idx = np.where(dist <= radius)
        avg = np.mean(field[:, idx], axis=1)
        spherical_avgs.append(avg)
    return spherical_avgs

# Calculate the spherical averages at different radii
radii = [10, 20, 50, 100]
spherical_avgs = []
for radius in radii:
    spherical_avgs.append(spherical_average(random_field, radius))

# Plot the distribution of the spherical averages
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(8,8))
axs = axs.ravel()
for i, avg in enumerate(spherical_avgs):
    axs[i].hist(avg, bins=50, density=True)
    axs[i].set_title("Radius = {}".format(radii[i]))
plt.show()
