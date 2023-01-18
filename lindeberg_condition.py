import numpy as np
import matplotlib.pyplot as plt

# Generate the random variables
sample_size = 100
random_vars = np.random.normal(0, 1, sample_size)

# Define a threshold epsilon
epsilon = 0.1

# calculate the sum of variances of the outliers
sample_sizes = np.arange(10, 1000, 10)
variances = []
for n in sample_sizes:
    outliers = random_vars[np.abs(random_vars) > epsilon]
    variances.append(np.var(outliers))

# Plot the sum of variances of the outliers as a function of sample size
plt.plot(sample_sizes, variances)
plt.xlabel('Sample size')
plt.ylabel('Sum of variances of outliers')
plt.show()

# If the sum of variances of the outliers converges to 0 as the sample size increases, 
# then the Lindeberg condition holds for the given sequence of random variables.
