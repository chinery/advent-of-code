import math

def oppositepolarity(one, two):
    return (abs(ord(one) - ord(two)) == lowertoupper)

try:
    while True:
        line = input()
except EOFError:
    pass

lowertoupper = ord('a') - ord('A')

minscore = math.inf

remove = [[False] * len(line) for i in range(26)]

for char in range(0, 26):
    removechar = ord('a') + char
    i = 0
    if ord(line[0]) == removechar or ord(line[0])+lowertoupper == removechar:
        remove[char][0] = True

    while i < len(line)-1:
        i += 1

        if ord(line[i]) == removechar or ord(line[i])+lowertoupper == removechar:
            remove[char][i] = True
            continue

        a = i-1
        while a >= 0 and remove[char][a]:
            a -= 1

        b = i
        # don't think this does anything but for symmetry!
        while b < len(line) and remove[char][b]:
            b += 1

        if a >= 0 and b < len(line) and (remove[char][a] or remove[char][b]):
            continue

        while a >= 0 and b < len(line) and oppositepolarity(line[a], line[b]):
            remove[char][a] = True
            remove[char][b] = True

            while a >= 0 and remove[char][a]:
                a -= 1
            while b < len(line) and remove[char][b]:
                b += 1
    minscore = min(minscore, remove[char].count(False))

print(minscore)
