# my doubly linked list worked in 'absolute' mode rather than 'relative'
# so was far too slow! Hence a rewrite for part 2, which is the better
# code to use to solve part 1 as well.


class CircleNode:
    def __init__(self, value, ccwise=None, cwise=None):
        self.value = value
        self.ccwise = ccwise
        self.cwise = cwise


class Circle:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, value, position):
        if position > self.size or position < 0:
            raise OverflowError

        if position == 0:
            if self.size == 0:
                self.head = CircleNode(value)
            else:
                self.head.ccwise = CircleNode(value, cwise=self.head)
                self.head = self.head.ccwise
        else:
            ptr = self.head
            for i in range(0, position-1):
                ptr = ptr.cwise

            ptr.cwise = CircleNode(value, ccwise=ptr, cwise=ptr.cwise)
            if ptr.cwise.cwise is not None:
                ptr.cwise.cwise.ccwise = ptr.cwise

        self.size += 1

    def remove(self, position):
        if position >= self.size or position < 0 or self.size == 0:
            raise OverflowError

        if position == 0:
            val = self.head.value
            self.head = self.head.cwise
            self.head.ccwise = None
        else:
            ptr = self.head
            for i in range(0, position):
                ptr = ptr.cwise

            val = ptr.value
            ptr.ccwise.cwise = ptr.cwise
            ptr.cwise.ccwise = ptr.ccwise

        self.size -= 1
        return val

    def print(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.value, end=' ')
            ptr = ptr.cwise
        print()


class MarbleGame:
    def __init__(self, players, marbles):
        self.circle = Circle()
        self.circle.insert(0, 0)
        self.current_marble = 0
        self.scores = [0]*players
        self.next_player = 0
        self.players = players
        self.next_marble = 1
        self.insert_marbles(marbles)

    def max_score(self):
        return max(self.scores)

    def insert_marbles(self, number):
        for i in range(0, number):
            self.insert()
            if i % 1000 == 0:
                print("Marble {}".format(i+1))

    def insert(self):
        if self.next_marble % 23 != 0:
            position = (self.current_marble + 2) % self.circle.size

            self.circle.insert(self.next_marble, position)
            self.current_marble = position
        else:
            self.scores[self.next_player] += self.next_marble

            remove_position = self.current_marble - 7
            if remove_position < 0:
                remove_position += self.circle.size

            val = self.circle.remove(remove_position)
            self.scores[self.next_player] += val
            self.current_marble = remove_position

        self.next_marble += 1
        self.next_player = (self.next_player + 1) % self.players


if __name__ == "__main__":
    try:
        while True:
            line = input()
            tokens = line.split(' ')
            players = int(tokens[0])
            marbles = int(tokens[6])
    except EOFError:
        pass

    game = MarbleGame(players, marbles)
    print(game.max_score())



