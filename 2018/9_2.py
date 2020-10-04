
class CircleNode:
    def __init__(self, value, ccwise=None, cwise=None):
        self.value = value
        self.ccwise = ccwise
        self.cwise = cwise


class Circle:
    def __init__(self):
        self.ptr = None
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, value, relative_position):
        if self.size == 0:
            self.head = CircleNode(value)
            self.tail = self.head
            self.ptr = self.head
        elif self.size == 1:
            self.ptr.ccwise = CircleNode(value, cwise=self.ptr)
            self.ptr = self.ptr.ccwise
            self.head = self.ptr
            self.tail = self.ptr.cwise
        else:
            while relative_position > 0:
                if self.ptr.cwise is not None:
                    self.ptr = self.ptr.cwise
                else:
                    self.ptr = self.head
                relative_position -= 1

            while relative_position < 0:
                if self.ptr.ccwise is not None:
                    self.ptr = self.ptr.ccwise
                else:
                    self.ptr = self.tail
                relative_position += 1

            if self.ptr == self.head:
                self.ptr.ccwise = CircleNode(value, cwise=self.ptr)
                self.ptr = self.ptr.ccwise
                self.head = self.ptr
            else:
                self.ptr.ccwise = CircleNode(value, ccwise=self.ptr.ccwise, cwise=self.ptr)
                self.ptr = self.ptr.ccwise
                self.ptr.ccwise.cwise = self.ptr
        self.size += 1

    def remove(self, relative_position):
        while relative_position > 0:
            if self.ptr.cwise is not None:
                self.ptr = self.ptr.cwise
            else:
                self.ptr = self.head
            relative_position -= 1

        while relative_position < 0:
            if self.ptr.ccwise is not None:
                self.ptr = self.ptr.ccwise
            else:
                self.ptr = self.tail
            relative_position += 1

        val = self.ptr.value
        if self.ptr == self.head:
            self.head = self.ptr.cwise
            self.ptr.cwise.ccwise = None
        elif self.ptr == self.tail:
            self.tail = self.tail.ccwise
            self.ptr.ccwise.cwise = None
        else:
            self.ptr.ccwise.cwise = self.ptr.cwise
            self.ptr.cwise.ccwise = self.ptr.ccwise

        if self.ptr.cwise is not None:
            self.ptr = self.ptr.cwise
        else:
            self.ptr = self.head

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
            if i % 10000 == 0:
                print("Marble {}".format(i+1))

    def insert(self):
        if self.next_marble % 23 != 0:
            self.circle.insert(self.next_marble, 2)
        else:
            self.scores[self.next_player] += self.next_marble
            val = self.circle.remove(-7)
            self.scores[self.next_player] += val

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

    # c = Circle()
    # c.insert(10, 0)
    # c.insert(20, 0)
    # c.insert(30, 0)
    # c.insert(40, 0)
    # c.insert(5, -1)
    # c.remove(-2)
    # c.remove(0)
    # c.print()

    game = MarbleGame(players, marbles*100)
    print(game.max_score())



