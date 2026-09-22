def double_exponential_smoothing(series, alpha, beta):
    n = len(series)
    level = [0.0] * n
    trend = [0.0] * n
    level[0] = series[0]
    trend[0] = series[1] - series[0]
    for t in range(1, n):
        level[t] = alpha * series[t] + (1 - alpha) * (level[t - 1] + trend[t - 1])
        trend[t] = beta * (level[t] - level[t - 1]) + (1 - beta) * trend[t - 1]
    return level