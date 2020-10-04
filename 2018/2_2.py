
def differbyatmostone(line1, line2):
    one = False
    ix = 0
    for i in range(0, len(line1)):
        if line1[i] != line2[i]:
            if not one:
                one = True
                ix = i
            else:
                return -1
    return ix

if __name__ == "__main__":
    words = []
    try:
        while True:
            line = input()
            words.append(line)
    except EOFError:
        pass

    # n^2... I'm sure it could be quicker, but the list isn't that long
    for i in range(0, len(words)):
        for j in range(i, len(words)):
            if i != j:
                ix = differbyatmostone(words[i], words[j])
                if ix != -1:
                    print(words[i][:ix] + words[i][ix+1:])
