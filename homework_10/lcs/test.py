import pytest

from main import lcs


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("AGGTAB", "GXTXAYB", "GTAB"),  # классический пример
        ("abcde", "ace", "ace"),  # подпоследовательность внутри
        ("aaaa", "aa", "aa"),  # повторяющиеся символы
        ("abcdef", "uvwxyz", ""),  # нет общих символов
        ("ABCDEF", "abc", ""),  # чувствительность к регистру
    ],
)
def test_lcs_examples(s1, s2, expected):
    assert lcs(s1, s2) == expected


def test_identical_strings():
    assert lcs("dynamic", "dynamic") == "dynamic"

