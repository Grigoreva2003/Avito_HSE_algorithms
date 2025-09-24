import pytest
from palindrome import is_palindrome

@pytest.mark.parametrize(
    "num,expected",
    [
        (1, True),
        (11, True),
        (121, True),
        (1221, True),
        (12321, True),
        (10, False),
        (12, False),
        (123, False),
        (1231, False),
        (1001, True),
        (100001, True),
        (2147447412, True),  # большой палиндром
        (123456789, False),
        (0, True),
    ]
)
def test_is_palindrome(num, expected):
    length = len(str(num)) - 1 if num != 0 else 0
    assert is_palindrome(num, length) == expected
