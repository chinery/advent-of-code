import sys

node_dict = {}


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def sum_orbits(self, acc=-1):
        return 1 + sum(x.sum_orbits(acc+1) for x in self.children) + acc

    def add_parent(self, name):
        if name in node_dict:
            node = node_dict[name]
        else:
            node = Node(name)
        self.parent = node
        node_dict[name] = node
        node.children.append(self)

    def add_child(self, name):
        if name in node_dict:
            node = node_dict[name]
            node.parent = self
        else:
            node = Node(name, self)
            node_dict[name] = node
        self.children.append(node)

    def __eq__(self, other):
        return False if other is None else self.name == other.name


class PathNode:
    def __init__(self, node, parent=None):
        self.node = node
        self.parent = parent

    def __eq__(self, other):
        return self.node == other.node


def main():
    try:
        sys.setrecursionlimit(sys.getrecursionlimit() * 2)
        # node_dict["COM"] = Node("COM")
        while True:
            line = input()
            data = line.split(')')
            if data[0] in node_dict:
                node_dict[data[0]].add_child(data[1])
            elif data[1] in node_dict:
                node_dict[data[1]].add_parent(data[0])
            else:
                parent = Node(data[0])
                parent.add_child(data[1])
                node_dict[data[0]] = parent
    except EOFError:
        pass

    # breadth first search from YOU to SAN
    frontier = [PathNode(node_dict["YOU"])]
    explored = []

    current_state = frontier.pop(0)
    while current_state.node != node_dict["SAN"]:
        explored.append(current_state)
        for child in current_state.node.children + [current_state.node.parent]:
            if child is None:
                continue
            path_child = PathNode(child, current_state)
            if path_child not in explored:
                frontier.append(path_child)
        current_state = frontier.pop(0)

    steps = 0
    while current_state.node != node_dict["YOU"]:
        steps += 1
        current_state = current_state.parent

    print(steps-2)


if __name__ == "__main__":
    main()
