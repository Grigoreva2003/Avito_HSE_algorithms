import pytest

from main import rabin_karp


@pytest.mark.parametrize(
    "text, pattern, expected",
    [
        ("abracadabra", "abra", [0, 7]),
        ("aaaaa", "aa", [0, 1, 2, 3]),  # overlapping occurrences
        ("hello world", "test", []),
        ("pattern", "pattern", [0]),
        ("short", "longer_pattern", []),
    ],
)
def test_rabin_karp(text, pattern, expected):
    assert rabin_karp(text, pattern) == expected


def test_empty_pattern_returns_empty():
    assert rabin_karp("anything", "") == []

