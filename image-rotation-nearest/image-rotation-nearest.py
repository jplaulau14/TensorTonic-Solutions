import math

def rotate_image(image: list, angle_degrees: float) -> list:
    height = len(image)
    width = len(image[0])
    cy = (height - 1) / 2
    cx = (width - 1) / 2
    theta = angle_degrees * math.pi / 180
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    output = []
    for i in range(height):
        dy = i - cy
        row = []
        for j in range(width):
            dx = j - cx
            sy = cy + dy * cos_theta + dx * sin_theta
            sx = cx - dy * sin_theta + dx * cos_theta
            ry = round(sy)
            rx = round(sx)
            if 0 <= ry < height and 0 <= rx < width:
                row.append(image[ry][rx])
            else:
                row.append(0)
        output.append(row)
    return output