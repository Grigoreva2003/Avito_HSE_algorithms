import pytest
from homework_2.stack_vs_queue.stack.stack import Stack

def test_empty_stack():
    stack = Stack()
    assert stack.is_empty()

    with pytest.raises(IndexError):
        stack.pop()
    with pytest.raises(IndexError):
        stack.peek()

def test_one_element_stack():
    stack = Stack()
    stack.push(42)

    assert not stack.is_empty()
    assert stack.peek() == 42

    popped = stack.pop()

    assert popped == 42
    assert stack.is_empty()
    with pytest.raises(IndexError):
        stack.pop()

def test_five_element_stack():
    stack = Stack()
    elements = [1, 2, 3, 4, 5]
    for e in elements:
        stack.push(e)

    assert not stack.is_empty()
    assert stack.peek() == 5

    # Pop and check order (LIFO)
    for expected in reversed(elements):
        assert stack.pop() == expected

    assert stack.is_empty()
    with pytest.raises(IndexError):
        stack.pop()
