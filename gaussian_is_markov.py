import numpy as np
from scipy.stats import multivariate_normal

# Define the mean and covariance of the Gaussian stationary process
mean = 0
cov = 1

# Define the number of time steps
n_steps = 100

# Generate the Gaussian stationary process
process = np.random.multivariate_normal(mean, cov, size=n_steps)

# Check if the process is a Markov process
for t in range(n_steps-1):
    conditional_dist = multivariate_normal(mean, cov)
    unconditional_dist = multivariate_normal(mean, cov)
    if not (conditional_dist.pdf(process[t+1]) == unconditional_dist.pdf(process[t+1])):
        print("The process is not a Markov process")
        break
else:
    print("The process is a Markov process")
