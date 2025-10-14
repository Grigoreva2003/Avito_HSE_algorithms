import pytest
from script import anagrams

@pytest.mark.parametrize("strings, expected", [
    (["eat","tea","tan","ate","nat","bat"],
        [["bat"], ["nat","tan"], ["ate","eat","tea"]]),
    (["aba","baa","bab"],
        [["bab"], ["aba", "baa"]]),
    ([""], [[""]]),
])
def test_two_sum(strings, expected):
    result = anagrams(strings)

    # prevent order comparison
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])