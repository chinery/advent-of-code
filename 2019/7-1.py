import itertools


class IntCodeComputer:
    def __init__(self, phase, in_value):
        self.inputs = [phase, in_value]

    def get_parameter(self, machine, value, mode):
        if mode == 0:
            return machine[machine[value]]
        else:
            return machine[value]

    def get_param_mode(self, instruction, param):
        if len(instruction) > param + 1:
            return int(instruction[-2 - param])
        return 0

    def process_machine(self, machine):
        pc = 0
        while machine[pc] != 99:
            instruction = str(machine[pc])
            opcode = int(instruction[-2:])
            if opcode == 1:
                param1 = self.get_parameter(machine, pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(machine, pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_parameter(machine, pc + 3, 1)
                machine[param3] = param1 + param2
                pc += 4
            elif opcode == 2:
                param1 = self.get_parameter(machine, pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(machine, pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_parameter(machine, pc + 3, 1)
                machine[param3] = param1 * param2
                pc += 4
            elif opcode == 3:
                # "input"
                in_val = self.inputs.pop(0)
                machine[machine[pc + 1]] = in_val
                pc += 2
            elif opcode == 4:
                param1 = self.get_parameter(machine, pc + 1, self.get_param_mode(instruction, 1))
                return param1
                # pc += 2
            elif opcode == 5:
                param1 = self.get_parameter(machine, pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(machine, pc + 2, self.get_param_mode(instruction, 2))
                if param1 != 0:
                    pc = param2
                else:
                    pc += 3
            elif opcode == 6:
                param1 = self.get_parameter(machine, pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(machine, pc + 2, self.get_param_mode(instruction, 2))
                if param1 == 0:
                    pc = param2
                else:
                    pc += 3
            elif opcode == 7:
                param1 = self.get_parameter(machine, pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(machine, pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_parameter(machine, pc + 3, 1)
                if param1 < param2:
                    machine[param3] = 1
                else:
                    machine[param3] = 0
                pc += 4
            elif opcode == 8:
                param1 = self.get_parameter(machine, pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(machine, pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_parameter(machine, pc + 3, 1)
                if param1 == param2:
                    machine[param3] = 1
                else:
                    machine[param3] = 0
                pc += 4
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

    max_out = 0
    max_settings = 0
    for amp_settings in itertools.permutations((0, 1, 2, 3, 4)):
        in_val = 0
        for i in range(0, 5):
            icc = IntCodeComputer(amp_settings[i], in_val)
            out_val = icc.process_machine(machine.copy())
            in_val = out_val

        if out_val > max_out:
            max_out = out_val
            max_settings = amp_settings

    print(max_out)
    print(max_settings)




if __name__ == "__main__":
    main()


