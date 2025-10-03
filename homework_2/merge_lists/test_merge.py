import pytest
from typing import Optional, List

from homework_2.merge_lists.dummy_node import dummy_merge
from homework_2.merge_lists.no_dummies import no_dummy_merge
from homework_2.node import Node

# Helper function to create a doubly linked list from a regular list
def create_doubly_linked_list(values: List[int]) -> Optional[Node]:
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        new_node = Node(val)
        current.next_ = new_node
        new_node.prev_ = current
        current = new_node

    return head


# Helper function to convert a doubly linked list to a regular list for verification
def doubly_linked_list_to_list(head: Optional[Node]) -> List[int]:
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next_

    return result


# Helper function to check if prev pointers are correctly set
def check_prev_pointers(head: Optional[Node]) -> bool:
    if not head:
        return True

    # Head's prev should be None
    if head.prev_ is not None:
        return False

    current = head
    while current.next_:
        if current.next_.prev_ != current:
            return False
        current = current.next_

    return True


# Test cases
@pytest.mark.parametrize("merge_function", [
    dummy_merge,
    no_dummy_merge
])
class TestMergeLists:

    def test_example_case(self, merge_function):
        list1 = create_doubly_linked_list([1, 2, 4])
        list2 = create_doubly_linked_list([1, 3, 4])

        merged = merge_function(list1, list2)

        # Check values
        assert doubly_linked_list_to_list(merged) == [1, 1, 2, 3, 4, 4]
        # Check prev pointers
        assert check_prev_pointers(merged)

    def test_non_overlapping_lists(self, merge_function):
        list1 = create_doubly_linked_list([1, 2, 3])
        list2 = create_doubly_linked_list([4, 5, 6])

        merged = merge_function(list1, list2)
        assert doubly_linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6]
        assert check_prev_pointers(merged)

        # Reverse order
        list1 = create_doubly_linked_list([4, 5, 6])
        list2 = create_doubly_linked_list([1, 2, 3])

        merged = merge_function(list1, list2)
        assert doubly_linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6]
        assert check_prev_pointers(merged)

    def test_single_element_lists(self, merge_function):
        list1 = create_doubly_linked_list([1])
        list2 = create_doubly_linked_list([2])

        merged = merge_function(list1, list2)
        assert doubly_linked_list_to_list(merged) == [1, 2]
        assert check_prev_pointers(merged)

        # Reverse order
        list1 = create_doubly_linked_list([2])
        list2 = create_doubly_linked_list([1])

        merged = merge_function(list1, list2)
        assert doubly_linked_list_to_list(merged) == [1, 2]
        assert check_prev_pointers(merged)

    def test_duplicate_values(self, merge_function):
        list1 = create_doubly_linked_list([1, 1, 2, 3, 3])
        list2 = create_doubly_linked_list([1, 2, 2, 3])

        merged = merge_function(list1, list2)
        assert doubly_linked_list_to_list(merged) == [1, 1, 1, 2, 2, 2, 3, 3, 3]
        assert check_prev_pointers(merged)

    def test_different_length_lists(self, merge_function):
        list1 = create_doubly_linked_list([1, 3, 5, 7, 9])
        list2 = create_doubly_linked_list([2, 4, 6])

        merged = merge_function(list1, list2)
        assert doubly_linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6, 7, 9]
        assert check_prev_pointers(merged)

    def test_negative_numbers(self, merge_function):
        list1 = create_doubly_linked_list([-5, -3, 0, 2])
        list2 = create_doubly_linked_list([-4, -2, 1, 3])

        merged = merge_function(list1, list2)
        assert doubly_linked_list_to_list(merged) == [-5, -4, -3, -2, 0, 1, 2, 3]
        assert check_prev_pointers(merged)

    def test_large_lists(self, merge_function):
        list1 = create_doubly_linked_list([i for i in range(0, 100, 2)])  # Even numbers
        list2 = create_doubly_linked_list([i for i in range(1, 100, 2)])  # Odd numbers

        merged = merge_function(list1, list2)
        assert doubly_linked_list_to_list(merged) == list(range(100))
        assert check_prev_pointers(merged)
