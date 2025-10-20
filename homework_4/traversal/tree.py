# Реализовать все обходы дерева:
#
# pre-order
# post-order
# in-order
# reverse pre-order
# reverse post-order
# reverse in-order
#
# Важно!
# Решение сопроводить тестами
# Класс BST реализуем самостоятельно
# В классе BST необходимо поддержать вставку для удобства тестирования

class Node:
    def __init__(self, val):
        self.val: int = val
        self.left: Node = None
        self.right: Node = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node: Node):
        if self.root is None:
            self.root = node
            return self.root
        return self._insert(self.root, node)

    def _insert(self, root: Node, node: Node):
        if root is None:
            root = node
        elif root.val > node.val:
            root.left = self._insert(root.left, node)
        elif root.val <= node.val:
            root.right = self._insert(root.right, node)

        return root

    def display(self):
        return self._display(self.root)

    def _display(self, root: Node):
        if root != None:
            self._display(root.left)
            print(root.val)
            self._display(root.right)
        return

    def search(self, val: int):
        pass

    def _search(self, root: Node, node: Node):
        pass

    def remove(self, val):
        pass

    def _remove(self, node: Node, val):
        pass

    def successor(self):
        pass

    def predecessor(self):
        pass