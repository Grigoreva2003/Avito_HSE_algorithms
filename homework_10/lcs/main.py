def lcs(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # fill lengths table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # reconstruct subsequence from dp table
    i, j = m, n
    result_chars = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result_chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result_chars))


if __name__ == "__main__":
    print(lcs("AGGTAB", "GXTXAYB"))
