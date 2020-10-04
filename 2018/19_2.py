class Operations:
    @staticmethod
    def addr(input_registers, a, b, c):
        reg = input_registers
        reg[c] = reg[a] + reg[b]

    @staticmethod
    def addi(input_registers, a, b, c):
        reg = input_registers
        reg[c] = reg[a] + b

    @staticmethod
    def mulr(input_registers, a, b, c):
        reg = input_registers
        reg[c] = reg[a] * reg[b]

    @staticmethod
    def muli(input_registers, a, b, c):
        reg = input_registers
        reg[c] = reg[a] * b

    @staticmethod
    def banr(input_registers, a, b, c):
        reg = input_registers
        reg[c] = reg[a] & reg[b]

    @staticmethod
    def bani(input_registers, a, b, c):
        reg = input_registers
        reg[c] = reg[a] & b

    @staticmethod
    def borr(input_registers, a, b, c):
        reg = input_registers
        reg[c] = reg[a] | reg[b]

    @staticmethod
    def bori(input_registers, a, b, c):
        reg = input_registers
        reg[c] = reg[a] | b

    @staticmethod
    def setr(input_registers, a, b, c):
        reg = input_registers
        reg[c] = reg[a]

    @staticmethod
    def seti(input_registers, a, b, c):
        reg = input_registers
        reg[c] = a

    @staticmethod
    def gtir(input_registers, a, b, c):
        reg = input_registers
        reg[c] = 1 if a > reg[b] else 0

    @staticmethod
    def gtri(input_registers, a, b, c):
        reg = input_registers
        reg[c] = 1 if reg[a] > b else 0

    @staticmethod
    def gtrr(input_registers, a, b, c):
        reg = input_registers
        reg[c] = 1 if reg[a] > reg[b] else 0

    @staticmethod
    def eqir(input_registers, a, b, c):
        reg = input_registers
        reg[c] = 1 if a == reg[b] else 0

    @staticmethod
    def eqri(input_registers, a, b, c):
        reg = input_registers
        reg[c] = 1 if reg[a] == b else 0

    @staticmethod
    def eqrr(input_registers, a, b, c):
        reg = input_registers
        reg[c] = 1 if reg[a] == reg[b] else 0

    @staticmethod
    def apply_op(op, input_registers, a, b, c):
        eval(f"Operations.{op}(input_registers, a, b, c)")


class Computer:
    def __init__(self):
        self.instruction_ptr = 0
        self.instruction_register = None
        self.registers = [0]*6
        self.registers[0] = 1

    def bind_ip(self, register):
        self.instruction_register = register

    def compute(self, instructions):
        while True:
            ipbound = self.instruction_register is not None
            ipreg = self.instruction_register
            if ipbound:
                self.registers[ipreg] = self.instruction_ptr

            if self.instruction_ptr > len(instructions):
                break

            ops = instructions[self.instruction_ptr]
            Operations.apply_op(ops[0], self.registers, ops[1], ops[2], ops[3])

            if ipbound:
                self.instruction_ptr = self.registers[ipreg]

            self.instruction_ptr += 1


if __name__ == "__main__":
    instructions = []
    try:
        while True:
            line = input()
            if line[:3] == "#ip":
                ipreg = int(line.split(' ')[1])
            else:
                ops = line.split(' ')
                instructions.append((ops[0], int(ops[1]), int(ops[2]), int(ops[3])))
    except EOFError:
        pass

    comp = Computer()
    comp.bind_ip(ipreg)
    comp.compute(instructions)
    print(comp.registers[0])