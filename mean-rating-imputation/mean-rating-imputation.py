import numpy as np

def mean_rating_imputation(ratings_matrix: list, mode: str) -> list:
    R = np.asarray(ratings_matrix, dtype=float)
    observed = R != 0
    axis = 1 if mode == "user" else 0
    sums = R.sum(axis=axis, keepdims=True)
    counts = observed.sum(axis=axis, keepdims=True)
    means = np.divide(sums, counts, out=np.zeros_like(sums), where=counts > 0)
    return np.where(observed, R, means).tolist()