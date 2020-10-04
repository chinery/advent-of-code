if __name__ == "__main__":
    machine = []
    try:
        while True:
            line = input()
            line = map(int, line.split(','))
            machine.extend(line)
    except EOFError:
        pass

    machine[1] = 12
    machine[2] = 2

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

    print(machine[0])
