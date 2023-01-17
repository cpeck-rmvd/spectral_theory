import numpy as np
import matplotlib.pyplot as plt

# Define a function to calculate the correlation between two sets
def corr(x, y):
    return np.corrcoef(x, y)[0, 1]

# Define the sphere
n_points = 1000
points = np.random.normal(0, 1, (n_points, 3))

# Define the sets C and D
set_c = points[points[:, 0] < 0]
set_d = points[points[:, 0] > 0]

# Calculate the distance between C and D
distances = np.arange(1, n_points)
correlations = []
for d in distances:
    c_subset = set_c[:d]
    d_subset = set_d[:d]
    correlation = corr(c_subset, d_subset)
    correlations.append(correlation)

# Plot the correlation as a function of distance
plt.plot(distances, correlations)
plt.xlabel('Distance')
plt.ylabel('Correlation')
plt.show()
