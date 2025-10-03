import pytest
from validate import validate

def test_examples():
    # Example 1 - Valid sequence
    pushed1 = [1, 2, 3, 4, 5]
    popped1 = [1, 3, 5, 4, 2]
    assert validate(pushed1, popped1) == True

    # Example 2 - Invalid sequence
    pushed2 = [1, 2, 3]
    popped2 = [3, 1, 2]
    assert validate(pushed2, popped2) == False


def test_basic_cases():
    # Single element
    assert validate([1], [1]) == True

    # Empty arrays
    assert validate([], []) == True

    # Simple valid case - push all, pop all in reverse
    assert validate([1, 2, 3], [3, 2, 1]) == True

    # Simple invalid case - different elements
    assert validate([1, 2, 3], [4, 5, 6]) == False


def test_edge_cases():
    # Same elements but different orders (not a permutation)
    assert validate([1, 2, 2], [1, 2, 2]) == True
    assert validate([1, 2, 3], [1, 3, 2]) == True

    # Larger test case
    large_pushed = list(range(1, 101))
    large_popped = list(range(100, 0, -1))
    assert validate(large_pushed, large_popped) == True

