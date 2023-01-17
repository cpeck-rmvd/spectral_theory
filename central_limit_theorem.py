"""
Theorem: for any homogeneous isotropic random field, as the number of realizations increases, 
the distribution of the means will converge to a normal distribution with a mean equal to the true mean of the random field 
and a standard deviation equal to the true standard deviation divided by the square root of the number of realizations.

Approach: simulate a large number of realizations of the random field, calculate the mean and standard deviation of each realization, 
and then just plot the distribution of these values. 
"""

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

# Calculate the mean and standard deviation of each realization
means = np.mean(random_field, axis=1)
stds = np.std(random_field, axis=1)

# Plot the distribution of means
plt.hist(means, bins=50, density=True)
plt.xlabel('Mean')
plt.ylabel('Probability')
plt.show()
