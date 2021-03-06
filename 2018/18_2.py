# more cellular automata huh?

from copy import deepcopy


def count_adjacent_char(grid, row, col, char):
    count = 0
    for i in range(max(row - 1, 0), min(row + 2, len(grid))):
        for j in range(max(col - 1, 0), min(col + 2, len(grid[i]))):
            if (i != row or j != col) and grid[i][j] == char:
                count += 1
    return count


def open_update(grid, row, col):
    if count_adjacent_char(grid, row, col, '|') >= 3:
        return '|'
    else:
        return '.'


def trees_update(grid, row, col):
    if count_adjacent_char(grid, row, col, '#') >= 3:
        return '#'
    else:
        return '|'


def lumberyard_update(grid, row, col):
    if count_adjacent_char(grid, row, col, '#') >= 1 and count_adjacent_char(grid, row, col, '|') >= 1:
        return '#'
    else:
        return '.'


def cellular_automate(grid, new_grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == '.':
                new_grid[i][j] = open_update(grid, i, j)
            elif grid[i][j] == '|':
                new_grid[i][j] = trees_update(grid, i, j)
            else:
                new_grid[i][j] = lumberyard_update(grid, i, j)


def print_grid(grid):
    # deja vu
    for row in grid:
        for c in row:
            print(c, end='')
        print()


def magic_number(grid):
    num_trees = 0
    num_lumber = 0
    for row in grid:
        for c in row:
            if c == '|':
                num_trees += 1
            elif c == '#':
                num_lumber += 1
    return num_trees*num_lumber


def match_last_five(vec):
    for i in range(0, len(vec)-5):
        if vec[i:i+5] == vec[-5:]:
            return i
    return -1


if __name__ == "__main__":
    grid = []
    try:
        while True:
            line = list(input())
            grid.append(line)
    except EOFError:
        pass

    minutes = 1000000000
    magicnums = []

    for i in range(0, minutes):
        new_grid = deepcopy(grid)

        cellular_automate(grid, new_grid)

        grid = new_grid

        magicnums.append(magic_number(grid))
        diffs = [magicnums[i+1]-magicnums[i] for i in range(0, len(magicnums)-1)]
        ix = match_last_five(diffs)
        if ix != -1:
            print("starts repeating at {}".format(ix))
            loop = diffs[ix+5:]
            magicnum = magicnums[-1]

            left = minutes - i
            loopsleft = left // len(loop)

            # sum(loop) turns out, perhaps predictably, to be 0
            magicnum += loopsleft * sum(loop)
            i += loopsleft * len(loop)

            magicnum += sum(loop[:(minutes-i-1)])
            print(magicnum)
            break





