import math

def sobel_edges(image: list) -> list:
    height = len(image)
    width = len(image[0])
    padded = [[0.0] * (width + 2) for _ in range(height + 2)]
    for i in range(height):
        source = image[i]
        dest = padded[i + 1]
        for j in range(width):
            dest[j + 1] = source[j]
    output = []
    for i in range(height):
        row = []
        above = padded[i]
        center = padded[i + 1]
        below = padded[i + 2]
        for j in range(width):
            gx = (
                -above[j] + above[j + 2]
                - 2 * center[j] + 2 * center[j + 2]
                - below[j] + below[j + 2]
            )
            gy = (
                -above[j] - 2 * above[j + 1] - above[j + 2]
                + below[j] + 2 * below[j + 1] + below[j + 2]
            )
            row.append(math.hypot(gx, gy))
        output.append(row)
    return output