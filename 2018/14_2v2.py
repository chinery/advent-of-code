# pure list version...


def check_recents(scores, target):
    if len(scores) > len(target):
        recent = scores[len(scores) - len(target):]
        if recent == target:
            print(len(scores) - len(target))
            quit()


if __name__ == "__main__":
    try:
        while True:
            line = input()
            target = [int(x) for x in list(line)]
    except EOFError:
        pass

    scores = [3, 7]

    elf1 = 0
    elf2 = 1

    while True:
        combined = scores[elf1] + scores[elf2]
        if combined > 9:
            scores.append(combined // 10)
            check_recents(scores, target)

            scores.append(combined % 10)
            check_recents(scores, target)
        else:
            scores.append(combined)
            check_recents(scores, target)

        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)

