import numpy as np
from scipy.stats import spearmanr

def compute_fiber_weights(X, y):

    n_fibers = X.shape[1]
    weights = np.zeros(n_fibers)

    for i in range(n_fibers):
        rho, _ = spearmanr(X[:, i], y)
        weights[i] = rho

    return weights
