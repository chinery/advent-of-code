import math

banned = []

def setsymbol(row, col, grid, distance, marker):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return False
    elif grid[row][col][0] != '.' and grid[row][col][0] != marker:
        if grid[row][col][1] == distance:
            grid[row][col] = ('X', distance)
            return False
        else:
            return False
    else:
        grid[row][col] = (marker, distance)
        return True


def drawatdistance(row, col, distance, grid, marker):
    changedsomething = False

    for r in range(row-distance, row+distance+1):
        rdist = abs(row-r)
        ccomplement = distance-rdist

        if setsymbol(r, col+ccomplement, grid, distance, marker):
            changedsomething = True
        if ccomplement != 0 and setsymbol(r, col-ccomplement, grid, distance, marker):
            changedsomething = True

    return changedsomething

def printgrid(grid):
    for row in grid:
        for element in row:
            if element[0] != 'X' and element[0] != '.' and element[1] == 0:
                print(chr(ord('A')+element[0]), end='')
            else:
                print(element[0], end='')
        print()

coords = []
minmaxrow = [math.inf, 0]
minmaxcol = [math.inf, 0]
try:
    while True:
        line = input()
        xy = line.split(", ")
        coord = (int(xy[1]), int(xy[0]))
        coords.append(coord)

        minmaxrow[0] = min(minmaxrow[0], coord[0])
        minmaxrow[1] = max(minmaxrow[1], coord[0])
        minmaxcol[0] = min(minmaxcol[0], coord[1])
        minmaxcol[1] = max(minmaxcol[1], coord[1])
except EOFError:
    pass

if __name__ == '__main__':
    grid = [[('.',0) for i in range(0, minmaxcol[1]-minmaxcol[0]+1)] for j in range(0, minmaxrow[1]-minmaxrow[0]+1)]

    print(len(grid))
    print(len(grid[0]))
    distance = 0
    done = []
    while len(done) != len(coords):
        # printgrid(grid)
        # print()
        for id in range(0, len(coords)):
            if id not in done:
                coord = coords[id]
                row = coord[0] - minmaxrow[0]
                col = coord[1] - minmaxcol[0]

                changedsomething = drawatdistance(row, col, distance, grid, id)
                if not changedsomething:
                    done.append(id)
        distance += 1

    banned = []
    # ban the edges
    for c in range(0, len(grid[0])):
        if grid[0][c][0] != 'X' and grid[0][c][0] not in banned:
            banned.append(grid[0][c][0])
        if grid[len(grid)-1][c][0] != 'X' and grid[len(grid)-1][c][0] not in banned:
            banned.append(grid[len(grid)-1][c][0])

    for r in range(1, len(grid)-1):
        if grid[r][0][0] != 'X' and grid[r][0][0] not in banned:
            banned.append(grid[r][0][0])
        if grid[r][len(grid[0])-1][0] != 'X' and grid[r][len(grid[0])-1][0] not in banned:
            banned.append(grid[r][len(grid[0])-1][0])

    counts = [0] * len(coords)
    for row in grid:
        for element in row:
            if element[0] != 'X' and element[0] not in banned:
                counts[element[0]] += 1
    print()
    print(counts)
    print(banned)
    print(max(counts))
