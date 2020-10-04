import itertools
import math
from collections import defaultdict


class IntCodeComputer:
    def __init__(self, machine, in_val=None):
        if in_val is not None:
            self.inputs = [in_val]
        else:
            self.inputs = []
        self.machine = defaultdict(lambda: 0)
        for ix, val in enumerate(machine):
            self.machine[ix] = val
        self.pc = 0
        self.base = 0

    def get_parameter(self, value, mode):
        if mode == 0:
            return self.machine[self.machine[value]]
        elif mode == 1:
            return self.machine[value]
        elif mode == 2:
            return self.machine[self.machine[value] + self.base]
        else:
            raise RuntimeError("Unknown mode")

    def get_position_param(self, value, mode):
        if mode == 0:
            return self.machine[value]
        elif mode == 2:
            return self.machine[value] + self.base
        else:
            raise RuntimeError("Unknown or incompatible mode")

    def get_param_mode(self, instruction, param):
        if len(instruction) > param + 1:
            return int(instruction[-2 - param])
        return 0

    def run(self, in_val=None):
        if in_val is not None:
            self.inputs.append(in_val)
        while self.machine[self.pc] != 99:
            instruction = str(self.machine[self.pc])
            opcode = int(instruction[-2:])
            if opcode == 1:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(self.pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_position_param(self.pc + 3, self.get_param_mode(instruction, 3))
                self.machine[param3] = param1 + param2
                self.pc += 4
            elif opcode == 2:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(self.pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_position_param(self.pc + 3, self.get_param_mode(instruction, 3))
                self.machine[param3] = param1 * param2
                self.pc += 4
            elif opcode == 3:
                # "input"
                param1 = self.get_position_param(self.pc + 1, self.get_param_mode(instruction, 1))
                in_val = self.inputs.pop(0)
                self.machine[param1] = in_val
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
                param3 = self.get_position_param(self.pc + 3, self.get_param_mode(instruction, 3))
                if param1 < param2:
                    self.machine[param3] = 1
                else:
                    self.machine[param3] = 0
                self.pc += 4
            elif opcode == 8:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                param2 = self.get_parameter(self.pc + 2, self.get_param_mode(instruction, 2))
                param3 = self.get_position_param(self.pc + 3, self.get_param_mode(instruction, 3))
                if param1 == param2:
                    self.machine[param3] = 1
                else:
                    self.machine[param3] = 0
                self.pc += 4
            elif opcode == 9:
                param1 = self.get_parameter(self.pc + 1, self.get_param_mode(instruction, 1))
                self.base += param1
                self.pc += 2
            else:
                raise RuntimeError(f"unknown opcode {self.machine[self.pc]}")
        return None  # halt


class PaintingRobot:
    def __init__(self, program):
        self.paint = defaultdict(lambda: 0)
        self.location = (0, 0)
        self.direction = (0, 1)
        self.turn_right = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
        self.turn_left = {(0, 1): (-1, 0), (1, 0): (0, 1), (0, -1): (1, 0), (-1, 0): (0, -1)}
        self.icc = IntCodeComputer(program)

    def run(self):
        while True:
            colour = self.paint[self.location]
            new_colour = self.icc.run(colour)
            if new_colour is None:
                break
            self.paint[self.location] = new_colour

            new_dir = self.icc.run()
            if new_dir is None:
                break
            if new_dir == 0:
                self.direction = self.turn_left[self.direction]
            else:
                self.direction = self.turn_right[self.direction]
            self.location = (self.location[0] + self.direction[0], self.location[1] + self.direction[1])

        print(len(self.paint))


def main():
    machine = []
    try:
        while True:
            line = input()
            line = map(int, line.split(','))
            machine.extend(line)
    except EOFError:
        pass

    painter = PaintingRobot(machine)
    painter.run()


if __name__ == "__main__":
    main()


