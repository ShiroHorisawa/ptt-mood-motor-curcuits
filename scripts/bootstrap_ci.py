import numpy as np
from scipy.stats import spearmanr

def bootstrap_ci(score, outcome, n_boot=10000, seed=0):

    rng = np.random.default_rng(seed)

    n = len(outcome)
    vals = np.zeros(n_boot)

    for i in range(n_boot):
        idx = rng.integers(0, n, n)
        vals[i] = spearmanr(score[idx], outcome[idx])[0]

    lower, upper = np.quantile(vals, [0.025, 0.975])

    return lower, upper, vals
