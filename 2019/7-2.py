import itertools
import math


class IntCodeComputer:
    def __init__(self, phase, machine):
        self.inputs = [phase]
        self.machine = machine
        self.pc = 0

    def get_parameter(self, value, mode):
        if mode == 0:
            return self.machine[self.machine[value]]
        else:
            return self.machine[value]

    def get_param_mode(self, instruction, param):
        if len(instruction) > param + 1:
            return int(instruction[-2 - param])
        return 0

    def run(self, in_val):
        self.inputs.append(in_val)
        while self.machine[self.pc] != 99:
            instruction = str(self.machine[self.pc])
            opcode = int(instruction[-2:])
            if opcode == 1:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(self.pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_parameter(self.pc + 3, 1)
                self.machine[param3] = param1 + param2
                self.pc += 4
            elif opcode == 2:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(self.pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_parameter(self.pc + 3, 1)
                self.machine[param3] = param1 * param2
                self.pc += 4
            elif opcode == 3:
                # "input"
                in_val = self.inputs.pop(0)
                self.machine[self.machine[self.pc + 1]] = in_val
                self.pc += 2
            elif opcode == 4:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                self.pc += 2
                return param1
            elif opcode == 5:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(self.pc + 2, self.get_param_mode(instruction, 2))
                if param1 != 0:
                    self.pc = param2
                else:
                    self.pc += 3
            elif opcode == 6:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(self.pc + 2, self.get_param_mode(instruction, 2))
                if param1 == 0:
                    self.pc = param2
                else:
                    self.pc += 3
            elif opcode == 7:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(self.pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_parameter(self.pc + 3, 1)
                if param1 < param2:
                    self.machine[param3] = 1
                else:
                    self.machine[param3] = 0
                self.pc += 4
            elif opcode == 8:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(self.pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_parameter(self.pc + 3, 1)
                if param1 == param2:
                    self.machine[param3] = 1
                else:
                    self.machine[param3] = 0
                self.pc += 4
            else:
                raise RuntimeError(f"unknown opcode {self.machine[self.pc]}")
        return None  # halt


def main():
    machine = []
    try:
        while True:
            line = input()
            line = map(int, line.split(','))
            machine.extend(line)
    except EOFError:
        pass

    max_out = -math.inf
    max_settings = 0
    for amp_settings in itertools.permutations((5, 6, 7, 8, 9)):
        in_val = 0
        iccs = []
        output_e = 0
        i = -1
        while True:
            i = (i + 1) % 5
            if len(iccs) <= i:
                iccs.append(IntCodeComputer(amp_settings[i], machine.copy()))
            out_val = iccs[i].run(in_val)

            if out_val is None:
                final_val = output_e
                break
            if i == 4:
                output_e = out_val

            in_val = out_val

        if final_val > max_out:
            max_out = final_val
            max_settings = amp_settings

    print(max_out)
    print(max_settings)


if __name__ == "__main__":
    main()


