import numpy as np

dependencies = []
try:
    while True:
        line = input()
        dependencies.append((line[36], line[5]))
except EOFError:
    pass

dependencies.sort()
num = ord(dependencies[-1][0])-ord('A')+1


depmat = np.zeros((num,num))

for dep in dependencies:
    task = ord(dep[0])-ord('A')
    depon = ord(dep[1])-ord('A')

    depmat[task, depon] = 1

order = ''
left = num
while left > 0:
    ix = np.where(np.sum(depmat, axis=1) == 0)
    index = ix[0][0]
    order += chr(index + ord('A'))

    for i in range(0,num):
        depmat[i, index] = 0
        depmat[index, i] = 99

    left -= 1

print(order)
