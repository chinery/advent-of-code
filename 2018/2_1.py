
def exactly2or3(line):
    counts = [0]*26
    e2 = False
    e3 = False
    for c in line:
        id = ord(c) - ord('a')
        counts[id] += 1

    for count in counts:
        if count == 2:
            e2 = True
        elif count == 3:
            e3 = True

        if e2 and e3:
            break

    return e2, e3


if __name__ == "__main__":
    nume2 = 0
    nume3 = 0
    try:
        while True:
            line = input()
            e2, e3 = exactly2or3(line)
            if e2:
                nume2 += 1
            if e3:
                nume3 += 1
    except EOFError:
        pass

    print(nume2*nume3)
