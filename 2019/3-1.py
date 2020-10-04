import math


def get_lines(directions):
    wire = []
    location = (0, 0)
    for dir in directions:
        delta = int(dir[1:])
        if dir[0] == "R":
            wire.append((location, (location[0] + delta, location[1])))
        if dir[0] == "D":
            wire.append((location, (location[0], location[1] - delta)))
        if dir[0] == "L":
            wire.append((location, (location[0] - delta, location[1])))
        if dir[0] == "U":
            wire.append((location, (location[0], location[1] + delta)))
        location = wire[-1][1]
    return wire


def lines_intersect(line1, line2):
    x1 = line1[0][0]
    x2 = line1[1][0]
    x3 = line2[0][0]
    x4 = line2[1][0]
    y1 = line1[0][1]
    y2 = line1[1][1]
    y3 = line2[0][1]
    y4 = line2[1][1]

    denom = (((x1 - x2) * (y3 - y4)) - ((y1 - y2) * (x3 - x4)))
    if denom == 0:
        return -1

    t = (((x1 - x3) * (y3 - y4)) - ((y1 - y3) * (x3 - x4)))\
        / denom

    if t < 0 or t > 1:
        return -1

    u = -1 * (((x1 - x2) * (y1 - y3)) - ((y1 - y2) * (x1 - x3))) \
        / denom

    if u < 0 or u > 1:
        return -1

    return x1 + (t * (x2 - x1)), y1 + (t * (y2 - y1))


if __name__ == "__main__":
    line1 = input().split(',')
    line2 = input().split(',')

    wire1 = get_lines(line1)
    wire2 = get_lines(line2)

    mindist = math.inf
    for line1 in wire1:
        for line2 in wire2:
            point = lines_intersect(line1, line2)
            if point != -1:
                dist = abs(point[0]) + abs(point[1])
                if mindist > dist > 0:
                    mindist = dist

    print(mindist)


