import numpy as np
from scipy.integrate import nquad

def fourier_transform(k):
    """Example Fourier transform function"""
    return np.exp(-k**2)

def spectral_representation(x):
    """Calculates the spectral representation of the random field"""
    d = len(x)
    integral = nquad(lambda k: fourier_transform(np.linalg.norm(k)) * np.exp(1j * np.dot(k, x)), [np.zeros(d), np.inf * np.ones(d)])[0]
    return (2 * np.pi) ** (-d / 2) * integral

x = np.array([1, 2, 3])
print(spectral_representation(x))
