# ans: 11546

def oppositepolarity(one, two):
    return (abs(ord(one) - ord(two)) == lowertoupper)

try:
    while True:
        line = input()
except EOFError:
    pass

lowertoupper = ord('a') - ord('A')

remove = [False] * len(line)

i = 0
while i < len(line):
    i += 1
    a = i-1
    b = i
    if a >= 0 and b < len(line) and (remove[a] or remove[b]):
        continue
    while a >= 0 and b < len(line) and oppositepolarity(line[a], line[b]):
        remove[a] = True
        remove[b] = True

        while a >= 0 and remove[a]:
            a -= 1
        while b < len(line) and remove[b]:
            b += 1

# print(remove)
print(remove.count(False))
