
def fill(grid, coords, size, id):
    for row in range(coords[1], coords[1]+size[1]):
        for col in range(coords[0], coords[0]+size[0]):
            if grid[row][col] == 0:
                grid[row][col] = id
            else:
                iddict[id] = True
                iddict[grid[row][col]] = True

allcoords = []
allsizes = []
allids = []
iddict = {}
maxleft = 0
maxtop = 0
try:
    while True:
        line = input()

        s = line.split(' ')

        id = int(s[0][1:])
        allids.append(id)
        iddict[id] = False

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
    fill(grid, allcoords[i], allsizes[i], allids[i])

count = 0
for id in iddict.keys():
    if not iddict[id]:
        print(id)
