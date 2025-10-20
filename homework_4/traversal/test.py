from tree import BST, Node

nodes = [Node(val) for val in range(10)]
tree = BST()
for node in nodes:
    tree.insert(node)

tree.display()