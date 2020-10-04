def fill(grid, coords, size):
    for row in range(coords[1], coords[1]+size[1]):
        for col in range(coords[0], coords[0]+size[0]):
            grid[row][col] += 1

allcoords = []
allsizes = []
maxleft = 0
maxtop = 0
try:
    while True:
        line = input()

        s = line.split(' ')

        coords = s[2].split(',')
        coords = (int(coords[0]), int(coords[1][:-1]))
        allcoords.append(coords)

        size = s[3].split("x")
        size = (int(size[0]), int(size[1]))
        allsizes.append(size)

        if coords[0]+size[0]+1 > maxleft:
            maxleft = coords[0]+size[0]+1
        if coords[1]+size[1] > maxtop:
            maxtop = coords[1]+size[1]+1
except EOFError:
    pass

grid = [x[:] for x in [[0] * maxtop] * maxleft]

for i in range(0, len(allcoords)):
    fill(grid, allcoords[i], allsizes[i])

count = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i][j] > 1:
            count += 1

print(count)
