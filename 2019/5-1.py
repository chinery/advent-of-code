def get_parameter(machine, value, mode):
    if mode == 0:
        return machine[machine[value]]
    else:
        return machine[value]


def get_param_mode(instruction, param):
    if len(instruction) > param + 1:
        return int(instruction[-2 - param])
    return 0


def process_machine(machine):
    pc = 0
    while machine[pc] != 99:
        instruction = str(machine[pc])
        opcode = int(instruction[-2:])
        if opcode == 1:
            param1 = get_parameter(machine, pc + 1, get_param_mode(instruction, 1))
            param2 = get_parameter(machine, pc + 2, get_param_mode(instruction, 2))
            param3 = get_parameter(machine, pc + 3, 1)
            machine[param3] = param1 + param2
            pc += 4
        elif opcode == 2:
            param1 = get_parameter(machine, pc + 1, get_param_mode(instruction, 1))
            param2 = get_parameter(machine, pc + 2, get_param_mode(instruction, 2))
            param3 = get_parameter(machine, pc + 3, 1)
            machine[param3] = param1 * param2
            pc += 4
        elif opcode == 3:
            # "input"
            in_val = 1
            machine[machine[pc + 1]] = in_val
            pc += 2
        elif opcode == 4:
            param1 = get_parameter(machine, pc + 1, get_param_mode(instruction, 1))
            print(param1)
            pc += 2
        else:
            raise RuntimeError(f"unknown opcode {machine[pc]}")


def main():
    machine = []
    try:
        while True:
            line = input()
            line = map(int, line.split(','))
            machine.extend(line)
    except EOFError:
        pass

    process_machine(machine)


if __name__ == "__main__":
    main()
