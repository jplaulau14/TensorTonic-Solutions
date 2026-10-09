import math

def winsorize(values: list, lower_pct: float, upper_pct: float) -> list:
    ordered = sorted(values)
    lower = _percentile(ordered, lower_pct)
    upper = _percentile(ordered, upper_pct)
    clipped = []
    for value in values:
        if value < lower:
            clipped.append(lower)
        elif value > upper:
            clipped.append(upper)
        else:
            clipped.append(value)
    return clipped

def _percentile(ordered: list, pct: float):
    last = len(ordered) - 1
    k = last * pct / 100.0
    left = max(0, min(math.floor(k), last))
    right = max(0, min(math.ceil(k), last))
    if left == right:
        return ordered[left]
    fraction = k - left
    return ordered[left] + fraction * (ordered[right] - ordered[left])