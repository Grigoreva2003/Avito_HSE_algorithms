from typing import List


DEFAULT_BASE = 257  
DEFAULT_MOD = 1_000_000_007  # large prime 


def hash(s: str, base: int, mod: int) -> int:
    """Polynomial rolling hash for a string."""
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod
    return h


def rabin_karp(text: str, pattern: str, base: int = DEFAULT_BASE, mod: int = DEFAULT_MOD) -> List[int]:
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []

    pattern_hash = hash(pattern, base, mod)
    window_hash = hash(text[:m], base, mod)

    positions: List[int] = []
    if window_hash == pattern_hash and text[:m] == pattern:
        positions.append(0)

    power = pow(base, m - 1, mod)

    for i in range(m, n):
        # remove leftmost char, add new char
        # saves time on recalculating the hash
        left = ord(text[i - m])
        right = ord(text[i])
        window_hash = (window_hash - left * power) % mod
        window_hash = (window_hash * base + right) % mod

        start_idx = i - m + 1
        if window_hash == pattern_hash:
            for j in range(m):
                if text[start_idx + j] != pattern[j]:
                    break
            else:
                positions.append(start_idx)

    return positions


if __name__ == "__main__":
    text_input = input()
    pattern_input = input()
    result = rabin_karp(text_input, pattern_input)
    print(" ".join(map(str, result)))

