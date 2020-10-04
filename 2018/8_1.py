class TreeNode:
    def __init__(self, num_children, num_metadata):
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.children = []
        self.metadata = []

    def sum_metadata(self):
        sum = 0
        for child in self.children:
            sum += child.sum_metadata()
        for val in self.metadata:
            sum += val
        return sum


def consume_node(line, i):
    node = TreeNode(int(line[i]), int(line[i+1]))
    i += 2
    for j in range(0, node.num_children):
        child, i = consume_node(line, i)
        node.children.append(child)
    for j in range(0, node.num_metadata):
        node.metadata.append(int(line[i]))
        i += 1
    return node, i


if __name__ == "__main__":
    try:
        while True:
            line = input()
    except EOFError:
        pass

    tokens = line.split(' ')
    head = consume_node(tokens, 0)[0]
    print(head.sum_metadata())