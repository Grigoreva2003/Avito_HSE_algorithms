import pytest
from script import two_sum

@pytest.mark.parametrize("arr, k, expected", [
    ([1, 3, 4, 10], 7, [1, 2]),         # 3 + 4 = 7
    ([5, 5, 1, 4], 10, [0, 1]),         # 5 + 5 = 10
    ([2, 7, 11, 15], 9, [0, 1]),        # 2 + 7 = 9
    ([3, 2, 4], 6, [1, 2]),             # 2 + 4 = 6
    ([0, 4, 3, 0], 0, [0, 3]),          # 0 + 0 = 0
    ([1, -3, 2, 4, 3], 0, [1, 4]),      # -3 + 3 = 0
    ([0], 1, None),
])
def test_two_sum(arr, k, expected):
    assert two_sum(arr, k) == expected
