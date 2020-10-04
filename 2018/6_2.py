import math

banned = []

def setsymbol(row, col, grid, distance, marker):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return True
    else:
        grid[row][col] += distance
        return False


def drawatdistance(row, col, distance, grid, marker):
    allhitedges = True

    for r in range(row-distance, row+distance+1):
        rdist = abs(row-r)
        ccomplement = distance-rdist

        if not setsymbol(r, col+ccomplement, grid, distance, marker):
            allhitedges = False
        if ccomplement != 0:
            if not setsymbol(r, col-ccomplement, grid, distance, marker):
                allhitedges = False

    return allhitedges

def printgrid(grid):
    for row in grid:
        for element in row:
            print(element, end='\t')
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
    grid = [[0 for i in range(0, minmaxcol[1]-minmaxcol[0]+1)] for j in range(0, minmaxrow[1]-minmaxrow[0]+1)]

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

                allhitedges = drawatdistance(row, col, distance, grid, id)
                if allhitedges:
                    done.append(id)
        distance += 1

    count = 0
    for row in grid:
        for element in row:
            if element < 10000:
                count += 1

    # printgrid(grid)
    print(count)
