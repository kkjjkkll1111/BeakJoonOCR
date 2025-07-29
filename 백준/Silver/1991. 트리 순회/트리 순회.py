class Node:
    def __init__(self, data):
        self.data = data
        self.left = '.'
        self.right= '.'
        
    def __str__(self):
        return f"[{self.data}\n({self.data}'s l){self.left}\n({self.data}'s r){self.right}]"

class Btree:
    def __init__(self):
        self.root = None
        self.set = set()

    def add(self, node_list):
        nodes = []
        for i in node_list:
            if i == ".":
                nodes.append(Node(None))    
            else:
                nodes.append(Node(i)) 
        if not self.root:
            self.root = nodes[0]
            self.root.left = nodes[1]
            self.root.right = nodes[2]
        else:
            for i in self.set:
                if i.data == nodes[0].data:
                    i.left = nodes[1]
                    i.right = nodes[2]
        for i in nodes:
            self.set.add(i)

    def post_order(self, root):
        if root.data:
            print(root.data,end="")
            self.post_order(root.left)
            self.post_order(root.right)
            
    def in_order(self, root):
        if root.data:
            self.in_order(root.left)
            print(root.data,end="")
            self.in_order(root.right)
            
    def pre_order(self, root):
        if root.data:
            self.pre_order(root.left)
            self.pre_order(root.right)
            print(root.data,end="")
        

n = int(input())
btree = Btree()
for i in range(n):
    li = list(input().split())
    btree.add(li)

btree.post_order(btree.root)
print()
btree.in_order(btree.root)
print()
btree.pre_order(btree.root)
