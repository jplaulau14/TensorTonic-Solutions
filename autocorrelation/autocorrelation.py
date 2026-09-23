import numpy as np

def autocorrelation(series: list, max_lag: int) -> list:
    """
    Returns normalized autocorrelation from lag zero through max_lag.
    """
    x = np.asarray(series, dtype=float)
    d = x - x[0]
    d -= d.mean()
    gamma0 = d @ d
    if gamma0 == 0:
        return [1.0] + [0.0] * max_lag
    n = len(d)
    return [round(float(d[:n - k] @ d[k:] / gamma0), 6) for k in range(max_lag + 1)]