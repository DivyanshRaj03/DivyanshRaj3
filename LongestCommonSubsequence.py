def lcs(seq1, seq2):
    m = len(seq1)
    n = len(seq2)

    # Create DP table
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + seq1[i - 1]
            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    return dp[m][n]


# Take input from user
seq1 = input("Enter first sequence: ")
seq2 = input("Enter second sequence: ")

result = lcs(seq1, seq2)

print("\nLongest Common Subsequence:", result)
print("Length of LCS:", len(result))