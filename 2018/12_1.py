# something tells me this lazy code isn't going to be good enough for part 2

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

    state = list('.'*(len(initial_state)+80))
    state[40:40+len(initial_state)] = initial_state

    numbers = list(range(-40, -40+len(state)))

    for generation in range(0, 20):
        nextstate = state.copy()

        for index in range(0, len(state) - 4):
            for rule in rules:
                if state[index:index+5] == rule[0]:
                    nextstate[index+2] = rule[1]

        state = nextstate

    sum = 0
    for i in range(0, len(state)):
        pot = state[i]
        if pot == '#':
            sum += numbers[i]

    print(sum)



