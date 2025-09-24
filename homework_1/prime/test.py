import pytest
from main import count_primes_less_than_n

@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),          # 2
        (5, 2),          # 2, 3
        (10, 4),         # 2, 3, 5, 7
        (20, 8),         # 2, 3, 5, 7, 11, 13, 17, 19
        (100, 25),
        (101, 25),
    ]
)
def test_count_primes(n, expected):
    assert count_primes_less_than_n(n) == expected
