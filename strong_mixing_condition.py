"""
Methodology: calculate the correlation between different parts of the system and plot the correlation as a function of the distance between those parts. 
If the plot shows that the correlation decreases exponentially with distance, then the strong mixing condition holds for that family of random variables.
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate a family of random variables
n_vars = 1000
random_vars = np.random.normal(0, 1, n_vars)

# Define a function to calculate the correlation between two parts of the system
def corr(x, y):
    return np.corrcoef(x, y)[0, 1]

# Calculate the correlation between different parts of the system
correlations = []
distances = np.arange(1, n_vars)
for d in distances:
    corr_sum = 0
    for i in range(n_vars - d):
        corr_sum += corr(random_vars[i], random_vars[i + d])
    correlation = corr_sum / (n_vars - d)
    correlations.append(correlation)

# Plot the correlation as a function of distance
plt.plot(distances, correlations)
plt.xlabel('Distance')
plt.ylabel('Correlation')
plt.show()
