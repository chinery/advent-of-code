def process_machine(machine):
    pc = 0
    while machine[pc] != 99:
        if machine[pc] == 1:
            machine[machine[pc + 3]] = machine[machine[pc + 1]] + machine[machine[pc + 2]]
            pc += 4
        elif machine[pc] == 2:
            machine[machine[pc + 3]] = machine[machine[pc + 1]] * machine[machine[pc + 2]]
            pc += 4
        else:
            raise RuntimeError(f"unknown opcode {machine[pc]}")
    return machine[0]


if __name__ == "__main__":
    machine = []
    try:
        while True:
            line = input()
            line = map(int, line.split(','))
            machine.extend(line)
    except EOFError:
        pass

    base_machine = machine.copy()

    for x in range(0, 100):
        for y in range(0, 100):
            machine = base_machine.copy()
            machine[1] = x
            machine[2] = y

            if process_machine(machine) == 19690720:
                print(100 * x + y)
                break

