# Implementing for the case of a Gaussian distribution, for which we already know KL Theorem holds. 
# (Turns out it holds for more general distributions, eg stationary and ergodic random fields.)

import numpy as np
from scipy import linalg

# Define the size of the random field
size = 100

# Generate the random field
random_field = np.random.normal(0, 1, (size, size))

# Perform the KL decomposition
eigenvalues, eigenvectors = linalg.eigh(random_field)

# Sort the eigenvalues and eigenvectors in descending order
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# Print the eigenvalues and eigenvectors
print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)
