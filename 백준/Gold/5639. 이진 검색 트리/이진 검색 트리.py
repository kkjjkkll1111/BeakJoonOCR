import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    new_node = Node(data)
    if node is None:
        return new_node

    current = node
    while True:
        if data > current.data:
            if current.right is None:
                current.right = new_node
                break
            current = current.right
        else:
            if current.left is None:
                current.left = new_node
                break
            current = current.left
    return node

def post_order(node):
    if node is None:
        return

    stack = [node]
    outputs = []

    while stack:
        pop_node = stack.pop()
        outputs.append(pop_node.data)

        if pop_node.left:
            stack.append(pop_node.left)
        if pop_node.right:
            stack.append(pop_node.right)

    for out in reversed(outputs):
        print(out)
    

root = None
for line in sys.stdin:
    val = line.strip()
    if val:
        root = insert(root, int(val))

post_order(root)