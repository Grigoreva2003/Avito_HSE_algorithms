def two_sum(arr: list, k: int):
    result = {}

    for i in range(len(arr)):
        result.setdefault(arr[i], i) # fill arr[i] = i, if it was absent

        if result.get(k - arr[i], -1) != -1 and result[k - arr[i]] != i:
            return [result[k - arr[i]], i]
    return None
