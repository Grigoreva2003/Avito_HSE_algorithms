from homework_2.node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, element):
        new_node = Node(element)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_ = new_node
            new_node.previous_ = self.tail
            self.tail = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty queue")
        first = self.head
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.head = first.next_
        return first.val

    def is_empty(self):
        return self.tail is None

    def peek(self):
        if self.tail is None:
            raise IndexError("peek from empty queue")
        return self.tail.val
