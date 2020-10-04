import math

def draw_grid(positions):
    minx = min([pos[0] for pos in positions])
    miny = min([pos[1] for pos in positions])
    maxx = max([pos[0] for pos in positions])
    maxy = max([pos[1] for pos in positions])

    for y in range(miny, maxy+1):
        for x in range(minx, maxx+1):
            if (x,y) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print()


if __name__ == "__main__":
    positions = []
    velocities = []

    try:
        while True:
            line = input()
            positions.append((int(line[10:16]), int(line[18:24])))
            velocities.append((int(line[36:38]), int(line[40:42])))
    except EOFError:
        pass

    consider = 100000
    offset = 10000

    prevspan = math.inf
    for time in range(offset, offset+consider):
        modpositions = [(pos[0] + time * vel[0], pos[1] + time * vel[1]) for pos, vel in zip(positions, velocities)]
        minx = min([pos[0] for pos in modpositions])
        miny = min([pos[1] for pos in modpositions])
        maxx = max([pos[0] for pos in modpositions])
        maxy = max([pos[1] for pos in modpositions])

        span = maxx-minx + maxy-miny
        if span > prevspan:
            break
        prevspan = span

    time = time - 1

    modpositions = [(pos[0]+time*vel[0], pos[1]+time*vel[1]) for pos, vel in zip(positions, velocities)]
    draw_grid(modpositions)
    print(time)
