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
    def check_all_against_output(input_registers, a, b, c, expected_output):
        all_fns = (Operations.addr, Operations.addi, Operations.mulr, Operations.muli,
                   Operations.banr, Operations.bani, Operations.borr, Operations.bori,
                   Operations.setr, Operations.seti,
                   Operations.gtir, Operations.gtri, Operations.gtrr,
                   Operations.eqir, Operations.eqri, Operations.eqrr)

        total = 0
        for f in all_fns:
            if f(input_registers, a, b, c) == expected_output:
                total += 1

        return total


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

    totalgt3 = 0
    for instruction in part_one:
        a = instruction[1][1]
        b = instruction[1][2]
        c = instruction[1][3]
        num = Operations.check_all_against_output(instruction[0], a, b, c, instruction[2])
        if num >= 3:
            totalgt3 += 1

    print(totalgt3)
