alllines = []

try:
    while True:
        line = input()
        alllines.append(line)
except EOFError:
    pass

alllines.sort()
guardtime = {}
guardmins = {}

for line in alllines:
    if line[19] == 'G':
        guard = int(line[26:30])
        if guard not in guardtime:
            guardtime[guard] = 0
            guardmins[guard] = [0]*60
        # print('starting guard {}'.format(guard))
    elif line[19] == 'f':
        start = int(line[15:17])
        # print('sleep at {}'.format(start))
    elif line[19] == 'w':
        end = int(line[15:17])
        time = end-start
        guardtime[guard] += time
        for i in range(start, end):
            guardmins[guard][i] += 1
        # print('wake at {} time {} total for {} is {}'.format(end, time, guard, guardtime[guard]))

maxg = 0
maxmins = 0
maxmin = 0
for g in guardtime.keys():
    for i in range(0, 60):
        if guardmins[g][i] > maxmins:
            maxmins = guardmins[g][i]
            maxmin = i
            maxg = g

print(maxmin * maxg)
