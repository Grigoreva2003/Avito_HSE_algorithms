def anagrams(strs: list[str]):
    hash_table = {}

    for word in strs:
        word_sorted = "".join(sorted(word))
        hash_table.setdefault(word_sorted, []).append(word)

    return list(hash_table.values())
