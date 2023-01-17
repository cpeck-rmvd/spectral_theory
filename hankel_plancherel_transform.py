import numpy as np
from scipy.integrate import quad
from scipy.special import jn

def original_function(r):
    """Example original function"""
    return np.exp(-r**2)

def hankel_plancherel_transform(k, n):
    """Calculates the Hankel-Plancherel transform of the original function"""
    integral = quad(lambda r: original_function(r) * jn(n, k*r) * r**(n+1), 0, np.inf)[0]
    return 2 * np.pi * integral

k = 1
n = 2
print(hankel_plancherel_transform(k, n))
