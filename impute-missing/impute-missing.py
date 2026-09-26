import numpy as np

def impute_missing(X: list, strategy: str = "mean") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as X.
    """
    values = np.asarray(X, dtype=float)
    one_dimensional = values.ndim == 1
    if one_dimensional:
        values = values.reshape(-1, 1)
    result = values.copy()
    for column in range(values.shape[1]):
        observed = values[~np.isnan(values[:, column]), column]
        fill = 0.0
        if observed.size:
            fill = np.mean(observed) if strategy == "mean" else np.median(observed)
        missing = np.isnan(values[:, column])
        result[missing, column] = fill
    return result.ravel() if one_dimensional else result