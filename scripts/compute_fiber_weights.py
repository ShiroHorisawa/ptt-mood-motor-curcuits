import numpy as np

def compute_raw_score(X, weights):
    return np.dot(X, weights)

def compute_balance_score(X, weights):

    pos = weights > 0
    neg = weights < 0

    P = np.dot(X[:, pos], weights[pos])
    N = np.dot(X[:, neg], np.abs(weights[neg]))

    return (P - N) / (P + N + 1e-8)
