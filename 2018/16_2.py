class Operations:
    @staticmethod
    def addr(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = reg[a] + reg[b]
        return reg

    @staticmethod
    def addi(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = reg[a] + b
        return reg

    @staticmethod
    def mulr(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = reg[a] * reg[b]
        return reg

    @staticmethod
    def muli(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = reg[a] * b
        return reg

    @staticmethod
    def banr(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = reg[a] & reg[b]
        return reg

    @staticmethod
    def bani(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = reg[a] & b
        return reg

    @staticmethod
    def borr(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = reg[a] | reg[b]
        return reg

    @staticmethod
    def bori(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = reg[a] | b
        return reg

    @staticmethod
    def setr(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = reg[a]
        return reg

    @staticmethod
    def seti(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = a
        return reg

    @staticmethod
    def gtir(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = 1 if a > reg[b] else 0
        return reg

    @staticmethod
    def gtri(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = 1 if reg[a] > b else 0
        return reg

    @staticmethod
    def gtrr(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = 1 if reg[a] > reg[b] else 0
        return reg

    @staticmethod
    def eqir(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = 1 if a == reg[b] else 0
        return reg

    @staticmethod
    def eqri(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = 1 if reg[a] == b else 0
        return reg

    @staticmethod
    def eqrr(input_registers, a, b, c):
        reg = input_registers.copy()
        reg[c] = 1 if reg[a] == reg[b] else 0
        return reg

    @staticmethod
    def get_all_fns():
        return (Operations.addr, Operations.addi, Operations.mulr, Operations.muli,
                Operations.banr, Operations.bani, Operations.borr, Operations.bori,
                Operations.setr, Operations.seti,
                Operations.gtir, Operations.gtri, Operations.gtrr,
                Operations.eqir, Operations.eqri, Operations.eqrr)

    @staticmethod
    def check_all_against_output(input_registers, a, b, c, expected_output):
        all_fns = Operations.get_all_fns()
        possibles = [False]*len(all_fns)
        for i, f in enumerate(all_fns):
            if f(input_registers, a, b, c) == expected_output:
                possibles[i] = True

        return possibles

    @staticmethod
    def apply_fn_by_num(input_registers, a, b, c, op):
        all_fns = Operations.get_all_fns()
        return all_fns[op](input_registers, a, b, c)


if __name__ == "__main__":
    try:
        part_one = []
        part_two = []
        while True:
            line = input()
            if line[0:6] == 'Before':
                before = [int(line[9]), int(line[12]), int(line[15]), int(line[18])]
                line = input()
                code = line.split(' ')
                code = [int(code[0]), int(code[1]), int(code[2]), int(code[3])]
                line = input()
                after = [int(line[9]), int(line[12]), int(line[15]), int(line[18])]
                part_one.append((before, code, after))
                line = input()
            else:
                line = input()
                while True:
                    line = input()
                    code = line.split(' ')
                    code = [int(code[0]), int(code[1]), int(code[2]), int(code[3])]
                    part_two.append(code)
    except EOFError:
        pass

    possible_opcodes = {}
    for op in range(0, 16):
        possible_opcodes[op] = [True]*16

    for instruction in part_one:
        op = instruction[1][0]
        a = instruction[1][1]
        b = instruction[1][2]
        c = instruction[1][3]
        possibles = Operations.check_all_against_output(instruction[0], a, b, c, instruction[2])
        for i in range(0, 16):
            if not possibles[i]:
                possible_opcodes[op][i] = False

    actual_ops = [-1]*16
    while actual_ops.count(-1) != 0:
        for op in range(0, 16):
            if possible_opcodes[op].count(True) == 1:
                ix = possible_opcodes[op].index(True)
                actual_ops[op] = ix
                for inner_op in range(0, 16):
                    possible_opcodes[inner_op][ix] = False

    registers = [0, 0, 0, 0]
    for instruction in part_two:
        op = instruction[0]
        actual_op = actual_ops[op]
        a = instruction[1]
        b = instruction[2]
        c = instruction[3]
        registers = Operations.apply_fn_by_num(registers, a, b, c, actual_op)

    print(registers[0])
