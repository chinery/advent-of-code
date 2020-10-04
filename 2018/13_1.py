from operator import attrgetter


class Direction:
    def __init__(self, direction):
        if direction == '>':
            self.direction = 3
        elif direction == '<':
            self.direction = 1
        elif direction == '^':
            self.direction = 0
        else:  # direction == 'v'
            self.direction = 2
        self.turns = 0

    def turn_left(self):
        self.direction = (self.direction + 1) % 4

    def turn_right(self):
        self.direction = (self.direction - 1) if self.direction > 0 else 3

    def move_forward(self, position):
        if self.direction == 3:
            return position[0], position[1] + 1
        elif self.direction == 1:
            return position[0], position[1] - 1
        elif self.direction == 0:
            return position[0] - 1, position[1]
        else:
            return position[0] + 1, position[1]

    def turn(self, corner):
        if (corner == '/' and (self.direction == 0 or self.direction == 2)) \
                or (corner == '\\' and (self.direction == 1 or self.direction == 3)):
            self.turn_right()
        else:
            self.turn_left()

    def intersection(self):
        if self.turns == 0:
            self.turn_left()
        elif self.turns == 2:
            self.turn_right()

        self.turns = (self.turns + 1) % 3

    def get_direction_char(self):
        if self.direction == 3:
            return '>'
        elif self.direction == 1:
            return '<'
        elif self.direction == 0:
            return '^'
        else:
            return 'v'


class Cart:
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.direction = Direction(direction)

    def move_forward(self, mapgrid):
        nextmove = self.direction.move_forward((self.row, self.col))

        self.row = nextmove[0]
        self.col = nextmove[1]

        if mapgrid[nextmove[0]][nextmove[1]] in ['/', '\\']:
            self.direction.turn(mapgrid[nextmove[0]][nextmove[1]])
        elif mapgrid[nextmove[0]][nextmove[1]] == '+':
            self.direction.intersection()


def print_grid(grid, carts):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pcart = False
            for cart in carts:
                if (i, j) == (cart.row, cart.col):
                    print(cart.direction.get_direction_char(), end='')
                    pcart = True
                    break
            if not pcart:
                print(grid[i][j], end='')
        print()
    print()


if __name__ == "__main__":
    mapgrid = []
    try:
        while True:
            line = input()
            mapgrid.append(list(line))
    except EOFError:
        pass

    carts = []

    for i in range(0, len(mapgrid)):
        for j in range(0, len(mapgrid[i])):
            if mapgrid[i][j] in ['>', '<', '^', 'v']:
                carts.append(Cart(i, j, mapgrid[i][j]))
                if mapgrid[i][j] in ['>', '<']:
                    mapgrid[i][j] = '-'
                else:
                    mapgrid[i][j] = '|'

    nocrash = True
    while nocrash:
        # print_grid(mapgrid, carts)

        # sort by row then col
        carts.sort(key=attrgetter('row', 'col'))

        for i in range(0, len(carts)):
            carts[i].move_forward(mapgrid)

            for j in range(0, len(carts)):
                if i == j:
                    continue
                if (carts[i].row, carts[i].col) == (carts[j].row, carts[j].col):
                    nocrash = False
                    print(carts[j].col, carts[j].row)
                    break
            if not nocrash:
                break
