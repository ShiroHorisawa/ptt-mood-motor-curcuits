import numpy as np
from scipy.stats import spearmanr

def permutation_test(score, outcome, n_perm=10000, seed=0):

    rng = np.random.default_rng(seed)

    observed = spearmanr(score, outcome)[0]

    null = np.zeros(n_perm)

    for i in range(n_perm):
        perm = rng.permutation(outcome)
        null[i] = spearmanr(score, perm)[0]

    p = (np.sum(np.abs(null) >= np.abs(observed)) + 1) / (n_perm + 1)

    return observed, p, null
