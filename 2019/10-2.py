import math
from fractions import Fraction as frac

if __name__ == "__main__":
    lines = []
    asteroids = []
    row = 0
    try:
        while True:
            line = input()
            lines.append(line)
            asteroids.extend([(row, i) for i, ltr in enumerate(line) if ltr == "#"])
            row += 1
    except EOFError:
        pass

    max_num = 0
    max_position = -1

    candidate_roid = (29, 26)
    roids = []
    for test_roid in asteroids:
        if candidate_roid == test_roid:
            continue

        rowdif = test_roid[0] - candidate_roid[0]
        coldif = test_roid[1] - candidate_roid[1]
        angle = math.atan2(rowdif, coldif) + (math.pi/2)
        if angle < 0:
            angle += 2*math.pi
        distsq = rowdif ** 2 + coldif ** 2
        gradient = angle, distsq, test_roid

        roids.append(gradient)

    roids.sort(key=lambda x: x[0])

    angles = list(dict.fromkeys([roid[0] for roid in roids]).keys())

    count = 1
    while True:
        for current_angle in angles:
            all_roids = [roid for roid in roids if abs(roid[0] - current_angle) < 0.001]
            if len(all_roids) == 0:
                continue

            lasered = min(all_roids, key=lambda x: x[1])
            if count == 200:
                print(lasered[2][1] * 100 + lasered[2][0])
                quit()

            roids.remove(lasered)
            count += 1




