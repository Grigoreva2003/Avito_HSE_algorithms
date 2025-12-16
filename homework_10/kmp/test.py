import pytest

from main import kmp


@pytest.mark.parametrize(
    "text, pattern, expected",
    [
        ("abracadabra", "abra", [0, 7]),
        ("aaaaa", "aa", [0, 1, 2, 3]),  # overlapping matches
        ("hello world", "test", []),  # no occurrence
        ("pattern", "pattern", [0]),  # full-string match
        ("short", "longer_pattern", []),  # pattern longer than text
    ],
)
def test_kmp(text, pattern, expected):
    assert kmp(text, pattern) == expected


def test_single_character_repeats():
    assert kmp("bbbbbbb", "bbb") == [0, 1, 2, 3, 4]

