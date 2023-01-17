import numpy as np
from scipy.integrate import quad

def power_spectrum(k):
    """Example power spectrum function"""
    return k**(-3)

def correlation_function(x):
    """Calculates the correlation function using the spectral representation"""
    d = len(x)
    integral = quad(lambda k: power_spectrum(np.linalg.norm(k)) * np.exp(-1j * np.dot(k, x)), np.zeros(d), np.inf * np.ones(d))[0]
    return (2 * np.pi) ** (-d / 2) * integral

x = np.array([1, 2, 3])
print(correlation_function(x))
