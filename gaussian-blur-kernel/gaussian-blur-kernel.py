import math

def gaussian_kernel(size: int, sigma: float) -> list:
    center = size // 2
    denom = 2.0 * sigma * sigma
    kernel = []
    total = 0.0
    for i in range(size):
        y = i - center
        row = []
        for j in range(size):
            x = j - center
            weight = math.exp(-(x * x + y * y) / denom)
            row.append(weight)
            total += weight
        kernel.append(row)
    for i in range(size):
        for j in range(size):
            kernel[i][j] /= total
    return kernel