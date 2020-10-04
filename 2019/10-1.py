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

    for candidate_roid in asteroids:
        gradients = []
        num = 0
        for test_roid in asteroids:
            if candidate_roid == test_roid:
                continue
            if test_roid[1] == candidate_roid[1] and test_roid[0] > candidate_roid[0]:
                gradient = math.inf, False
            elif test_roid[1] == candidate_roid[1]:
                gradient = -math.inf, True
            else:
                gradient = frac(test_roid[0] - candidate_roid[0], test_roid[1] - candidate_roid[1]), test_roid[1] > candidate_roid[1]

            if gradient not in gradients:
                num += 1
                gradients.append(gradient)

        if num > max_num:
            max_num = num
            max_position = candidate_roid

    print(f"{max_position} can see {max_num}")
