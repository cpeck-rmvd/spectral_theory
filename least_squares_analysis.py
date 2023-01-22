import numpy as np

def lssa(x, m, k):
    """
    Perform Least-Squares Spectral Analysis (LSSA) on a given dataset.

    Parameters:
        x (numpy array): The input dataset.
        m (int): The order of the autoregressive (AR) model.
        k (int): The number of frequency bins.

    Returns:
        freqs (numpy array): The estimated frequencies.
        amplitudes (numpy array): The estimated amplitudes.
    """
    n = len(x)
    X = np.zeros((n-m, m+1))
    for i in range(m, n):
        X[i-m, :] = [-x[j] for j in range(i-m, i)] + [1]
    _, _, vh = np.linalg.svd(X, full_matrices=False)
    P = vh[m:, :].T
    C = np.dot(P, P.T)
    _, eigenvalues, eigenvectors = np.linalg.svd(C)
    idx = np.argsort(eigenvalues)[::-1][:k]
    freqs = np.arctan2(eigenvectors[idx, 1], eigenvectors[idx, 0]) / (2*np.pi)
    amplitudes = np.sqrt(eigenvalues[idx])
    return freqs, amplitudes

# Example usage:
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
m = 2
k = 2
freqs, amplitudes = lssa(x, m, k)
print(freqs)
print(amplitudes)
