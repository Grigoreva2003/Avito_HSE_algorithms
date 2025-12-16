def prefix_func(s: str):
    n = len(s)
    prefix = [0] * n

    for i in range(1, n):
        j = prefix[i - 1]
        while (j > 0 and s[i] != s[j]):
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j

    return prefix

def kmp(text: str, pattern: str):
    prefixes = prefix_func(pattern + "#" + text)
    len_pattern = len(pattern)

    indexes = []
    for i in range(len_pattern + 1, len(prefixes)):
        if prefixes[i] == len_pattern:
            indexes.append(i - 2 * len_pattern)
    return indexes

if __name__ == "__main__":
    print(prefix_func("aaba#aabaaba"))
    print(kmp("aabaaba", "aaba"))
