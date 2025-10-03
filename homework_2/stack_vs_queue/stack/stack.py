from homework_2.node import Node

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_ = 0

    def push(self, element):
        new_node = Node(element)
        self.size_ += 1
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_ = new_node
            new_node.previous_ = self.tail
            self.tail = new_node

    def pop(self):
        self.size_ -= 1
        if self.tail is None:
            raise IndexError("pop from empty stack")
        last = self.tail
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = last.previous_
            self.tail.next_ = None
        return last.val

    def is_empty(self):
        return self.tail is None

    def size(self):
        return self.size_

    def peek(self):
        if self.tail is None:
            raise IndexError("peek from empty stack")
        return self.tail.val