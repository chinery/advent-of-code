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
        else:
            node = Node(name, self)
            node_dict[name] = node
        self.children.append(node)


if __name__ == "__main__":
    try:
        sys.setrecursionlimit(sys.getrecursionlimit()*2)
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

    print(node_dict["COM"].sum_orbits())

