import math


class Character:
    def __init__(self, faction):
        self.hp = 200
        self.attack = 3
        self.faction = faction


class Game:
    def __init__(self, text):
        self.ADJ_MODIFIERS = ((-1, 0), (0, -1), (0, 1), (1, 0))
        self.grid = [[c for c in row] for row in text]
        self.characters = []
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[0])):
                if self.grid[i][j] == 'G':
                    self.characters.append([i, j, Character('G')])
                elif self.grid[i][j] == 'E':
                    self.characters.append([i, j, Character('E')])

    def shortest_path(self, source, destination):
        distance = [[-1 for i in range(len(self.grid[0]))] for j in range(len(self.grid))]
        distance[source[0]][source[1]] = 0
        live = [source]
        while distance[destination[0]][destination[1]] == -1 and len(live) > 0:
            newlive = []
            for active in live:
                for mod in self.ADJ_MODIFIERS:
                    cell = [active[0]+mod[0], active[1]+mod[1]]
                    if self.in_bounds(cell) and \
                            self.grid[cell[0]][cell[1]] == '.' and \
                            cell not in newlive and distance[cell[0]][cell[1]] == -1:
                        distance[cell[0]][cell[1]] = distance[active[0]][active[1]] + 1
                        newlive.append(cell)
                        # don't think we need an else, should never be shorter?
            live = newlive

        return distance[destination[0]][destination[1]], distance

    def move(self, character, position):
        self.grid[character[0]][character[1]] = '.'
        self.grid[position[0]][position[1]] = character[2].faction
        character[0:2] = position

    def attack(self, attacker, attacked):
        attacked[2].hp -= attacker[2].attack
        print("{}{} attacked {}{}, new HP {}".format(attacker[2].faction,
                                                     attacker[0],
                                                     attacked[2].faction,
                                                     attacked[0],
                                                     attacked[2].hp))
        if attacked[2].hp < 0:
            self.grid[attacked[0]][attacked[1]] = '.'
            return [attacked]
        return []

    def in_bounds(self, cell):
        return 0 <= cell[0] < len(self.grid) and 0 <= cell[1] < len(self.grid[0])

    def play_round(self):
        self.characters.sort()
        killed = []
        for char in self.characters:
            if char in killed:
                continue
            # self.print_grid()
            # identify targets
            targets = [x for x in self.characters if x[2].faction != char[2].faction]
            for kill in killed:
                if kill in targets:
                    targets.remove(kill)
            if len(targets) == 0:
                for kill in killed:
                    self.characters.remove(kill)
                return True

            # adjacent free squares
            adjacents = []
            for target in targets:
                for mod in self.ADJ_MODIFIERS:
                    cell = [target[0]+mod[0], target[1]+mod[1]]
                    if self.in_bounds(cell) and \
                            cell not in adjacents \
                            and (self.grid[cell[0]][cell[1]] == '.'
                                 or cell == char[0:2]):
                        adjacents.append([cell[0], cell[1]])
            if len(adjacents) == 0:
                continue

            if char[0:2] not in adjacents:
                # move
                # find adjacent sq with shortest path, reading order for tie-breaks
                shortest = math.inf
                bestadj = 0
                bestgraph = 0
                for adjacent in adjacents:
                    dist, graph = self.shortest_path(char[0:2], adjacent)
                    if dist != -1 and \
                            dist < shortest or (dist == shortest and adjacent < bestadj):
                        shortest = dist
                        bestadj = adjacent
                        bestgraph = graph

                if math.isinf(shortest):
                    continue

                # check path to closest sq, reading order for tie-breaks
                live = [bestadj]
                bestgraph[bestadj[0]][bestadj[1]] = 0
                steps = shortest
                done = False
                while len(live) > 0 and not done:
                    newlive = []
                    for active in live:
                        for mod in self.ADJ_MODIFIERS:
                            cell = [active[0]+mod[0], active[1]+mod[1]]
                            if self.in_bounds(cell) and \
                                    cell not in newlive \
                                    and bestgraph[cell[0]][cell[1]] == steps - 1:
                                bestgraph[cell[0]][cell[1]] = 0
                                newlive.append(cell)
                                if cell == char[:2]:
                                    done = True
                    live = newlive
                    steps -= 1

                moved = False
                for mod in self.ADJ_MODIFIERS:
                    cell = [char[0] + mod[0], char[1] + mod[1]]
                    if self.in_bounds(cell) and \
                            bestgraph[cell[0]][cell[1]] == 0:
                        self.move(char, cell)
                        moved = True
                        break
                if not moved:
                    raise RuntimeError

            # attack!
            adjacents = [[char[0]+mod[0], char[1]+mod[1]] for mod in self.ADJ_MODIFIERS]
            newtargets = [x for x in targets if x[0:2] in adjacents]
            if len(newtargets) > 0:
                newtargets.sort()  # probably unnecessary but ensures reading order
                target = min(newtargets, key=lambda x: x[2].hp)
                killed.extend(self.attack(char, target))
        for kill in killed:
            self.characters.remove(kill)
        return False

    def print_grid(self):
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid[0])):
                print(self.grid[i][j], end='')
            print()

    def play(self):
        rounds = 0
        while True:
            self.print_grid()
            if self.play_round():
                break
            rounds += 1

        hp_sum = sum([x[2].hp for x in self.characters])
        print("rounds: {}".format(rounds))
        print([x[2].hp for x in self.characters])
        print("Outcome: {}".format(rounds*hp_sum))


if __name__ == "__main__":
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    game = Game(lines)
    game.play()
