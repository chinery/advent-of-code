# ha. sure enough. let's look for a pattern instead...

# from trying 200 generations and looking at the differences, it was clear the system stablised adding 51 per generation
# think there might be a cleverer way still, but it would require me to know more about cellular automata than I do.

import numpy as np


def count_pots(state):
    numbers = list(range(-10, -10+len(state)))
    sum = 0
    for i in range(0, len(state)):
        pot = state[i]
        if pot == '#':
            sum += numbers[i]

    return sum


if __name__ == "__main__":
    i = 0
    rules = []
    try:
        while True:
            line = input()
            if i == 0:
                initial_state = list(line[15:])
            elif i == 1:
                pass
            else:
                rules.append((list(line[:5]), line[9]))
            i += 1
    except EOFError:
        pass

    generations = 200

    state = list('.'*(len(initial_state)+(generations*2)))
    state[10:10+len(initial_state)] = initial_state

    counts = np.array([0]*generations)

    for generation in range(0, generations):
        nextstate = state.copy()

        for index in range(0, len(state) - 4):
            for rule in rules:
                if state[index:index+5] == rule[0]:
                    nextstate[index+2] = rule[1]

        state = nextstate
        # print(state)
        counts[generation] = count_pots(state)

    print(counts)
    print()
    diff = counts[1:]-counts[:-1]
    print(diff)

    totalgenerations = 50000000000
    genleft = totalgenerations-generations
    final = counts[-1] + genleft*diff[-1]
    print(final)




