
def find_path(source, destination, mesh):
    sx, sy = source
    dx, dy = destination
    visited = []
    for box in mesh['boxes']:
        x1, x2, y1, y2 = box
        if x1 < sx and x2 > sx and y1 < sy and y2 > sy:
            visited.append(box)
        if x1 < dx and x2 > dx and y1 < dy and y2 > dy:
            visited.append(box)
    return [], visited