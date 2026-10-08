def weighted_moving_average(values: list, weights: list) -> list:
    window = len(weights)
    weight_sum = sum(weights)
    averages = []
    for start in range(len(values) - window + 1):
        window_values = values[start:start + window]
        weighted = sum(weight * value for weight, value in zip(weights, window_values))
        averages.append(weighted / weight_sum)
    return averages