from copy import deepcopy
import sys


class Ground:
    def __init__(self, height, width, clay, water):
        self.watercoord = water
        self.grid = [['.' for i in range(width)] for j in range(height)]
        for coords in clay:
            for i in range(coords[0], coords[1]+1):
                for j in range(coords[2], coords[3]+1):
                    self.grid[i][j] = '#'

    def fill_left(self, row, col, symbol):
        if col < 0 or self.grid[row][col] != '.':
            return
        elif self.grid[row + 1][col] not in ['~', '#']:
            self.grid[row][col] = symbol
            return
        else:
            self.grid[row][col] = symbol
            self.fill_left(row, col - 1, symbol)

    def check_left(self, row, col):
        if col < 0:
            return False
        if self.grid[row][col] in ['~', '#']:
            return True
        elif self.grid[row + 1][col] == '.':
            closed_below = self.fill_down(row + 1, col)
            if not closed_below:
                return False
        if self.grid[row + 1][col] == '|':
            return False
        elif self.grid[row + 1][col] in ['~', '#']:
            return self.check_left(row, col - 1)

    def fill_right(self, row, col, symbol):
        if col >= len(self.grid[row]) or self.grid[row][col] != '.':
            return
        elif self.grid[row + 1][col] not in ['~', '#']:
            self.grid[row][col] = symbol
            return
        else:
            self.grid[row][col] = symbol
            self.fill_right(row, col + 1, symbol)

    def check_right(self, row, col):
        if col >= len(self.grid[row]):
            return False
        if self.grid[row][col] in ['~', '#']:
            return True
        elif self.grid[row + 1][col] == '.':
            closed_below = self.fill_down(row + 1, col)
            if not closed_below:
                return False
        if self.grid[row + 1][col] == '|':
            return False
        elif self.grid[row + 1][col] in ['~', '#']:
            return self.check_right(row, col + 1)

    def fill_down(self, row, col):
        if row + 1 >= len(self.grid):
            if row == len(self.grid)-1:
                self.grid[row][col] = '|'
            return False

        if self.grid[row + 1][col] == '.':
            closed_below = self.fill_down(row + 1, col)
        elif self.grid[row + 1][col] == '|':
            closed_below = False
        else:
            closed_below = True

        if not closed_below:
            self.grid[row][col] = '|'
            return False
        else:
            left_closed = self.check_left(row, col - 1)
            right_closed = self.check_right(row, col + 1)
            if left_closed and right_closed:
                self.fill_left(row, col - 1, '~')
                self.fill_right(row, col + 1, '~')
                self.grid[row][col] = '~'
                return True
            else:
                self.fill_left(row, col - 1, '|')
                self.fill_right(row, col + 1, '|')
                self.grid[row][col] = '|'
                return False

    def pour_water(self):
        gridcopy = []
        loc = self.watercoord
        while gridcopy != self.grid:
            # ground.print_grid()
            gridcopy = deepcopy(self.grid)
            self.fill_down(loc[0], loc[1])

    def print_grid(self):
        for row in self.grid:
            for c in row:
                print(c, end='')
            print()
        print()

    def total_water(self):
        count = 0
        for row in self.grid:
            for c in row:
                if c in ['|', '~']:
                    count += 1
        return count

    def total_settled_water(self):
        count = 0
        for row in self.grid:
            for c in row:
                if c == '~':
                    count += 1
        return count


if __name__ == "__main__":
    sys.setrecursionlimit(20000)

    try:
        clay = []
        while True:
            line = input()
            parts = line.split(', ')
            num1 = int(parts[0].split('=')[1])
            num2 = int(parts[1].split('=')[1].split('..')[0])
            num3 = int(parts[1].split('=')[1].split('..')[1])
            if line[0] == 'y':
                clay.append((num1, num1, num2, num3))
            else:
                clay.append((num2, num3, num1, num1))
    except EOFError:
        pass

    minr = min(clay, key=lambda x: x[0])[0]
    maxr = max(clay, key=lambda x: x[1])[1]
    minc = min(clay, key=lambda x: x[2])[2]
    maxc = max(clay, key=lambda x: x[3])[3]

    # leave room for water to flow one left and right of min and max col
    remappedclay = [(x[0] - minr,
                     x[1] - minr,
                     x[2] - minc + 1,
                     x[3] - minc + 1) for x in clay]
    width = maxc-minc+3
    height = maxr-minr+1

    water = (0, 500 - minc + 1)

    ground = Ground(height, width, remappedclay, water)

    ground.pour_water()

    # ground.print_grid()

    print(ground.total_water())
    print(ground.total_settled_water())