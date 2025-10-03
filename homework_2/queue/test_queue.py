import pytest
from homework_2.queue.queue import Queue

def test_empty_queue():
    queue = Queue()
    assert queue.is_empty()
    with pytest.raises(IndexError):
        queue.pop()
    with pytest.raises(IndexError):
        queue.peek()

def test_one_element_queue():
    queue = Queue()
    queue.push(42)

    assert not queue.is_empty()
    assert queue.peek() == 42

    popped = queue.pop()

    assert popped == 42
    assert queue.is_empty()
    with pytest.raises(IndexError):
        queue.pop()

def test_five_element_queue():
    queue = Queue()
    elements = [1, 2, 3, 4, 5]
    for e in elements:
        queue.push(e)
    assert not queue.is_empty()
    assert queue.peek() == 5

    # Pop and check order (FIFO)
    for expected in elements:
        assert queue.pop() == expected
    assert queue.is_empty()
    with pytest.raises(IndexError):
        queue.pop()