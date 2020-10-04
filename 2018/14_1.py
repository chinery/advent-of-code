if __name__ == "__main__":
    try:
        while True:
            line = input()
            recipes = int(line)
    except EOFError:
        pass

    scores = [0] * (recipes+10)
    scores[0] = 3
    scores[1] = 7

    elf1 = 0
    elf2 = 1
    endptr = 2

    while endptr < len(scores):
        combined = scores[elf1] + scores[elf2]
        if combined > 9:
            scores[endptr] = combined // 10
            scores[endptr+1] = combined % 10
            endptr += 2
        else:
            scores[endptr] = combined
            endptr += 1

        elf1 = (elf1 + scores[elf1] + 1) % endptr
        elf2 = (elf2 + scores[elf2] + 1) % endptr

    print(scores[recipes:])
