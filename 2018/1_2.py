
total = 0
allchanges = []
allfreqs = [0]*1000000
offset = 50000

try:
    while True:
        line = input()
        num = int(line[1:])
        if line[0] == '+':
            total += num
            allchanges.append(num)
        elif line[0] == '-':
            total -= num
            allchanges.append(-1 * num)

        if allfreqs[total+offset] == 1:
            print(total)
            quit()
        else:
            allfreqs[total+offset] = 1
except EOFError:
    pass


while True:
    for delta in allchanges:
        total += delta
        if allfreqs[total+offset] == 1:
            print(total)
            quit()
        else:
            allfreqs[total+offset] = 1
