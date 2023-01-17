"""
Theorem: any stationary and isotropic random process can be represented as a linear combination of 
uncorrelated, zero-mean, and orthonormal random variables (KL eigenfunctions) and the corresponding coefficients (KL eigenvalues).

Example proof for base case of a 1-D random process
"""

import numpy as np

# Define the covariance function
def covariance_function(x, y):
    return np.exp(-abs(x-y))

# Compute the eigenvalues and eigenvectors of the covariance matrix
x = np.linspace(-10, 10, 100)
cov = covariance_function(x[:,None], x)
eigenvalues, eigenvectors = np.linalg.eig(cov)

# Sort the eigenvalues and eigenvectors in descending order
idx = eigenvalues.argsort()[::-1]   
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:,idx]

# The eigenvectors are the KL eigenfunctions and the eigenvalues are the KL eigenvalues
print("KL Eigenvalues:", eigenvalues)
print("KL Eigenfunctions:", eigenvectors)

"""
The random process can then be represented as a linear combination of the KL eigenfunctions, with the coefficients given by the KL eigenvalues:

f(x) = sum(sqrt(lambda_i) * phi_i(x) * epsilon_i)

Where f(x) is the original random process, lambda_i is the i-th KL eigenvalue, phi_i(x) is the i-th KL eigenfunction, 
and epsilon_i is a set of uncorrelated, zero-mean, and mutually orthogonal random variables.
"""
