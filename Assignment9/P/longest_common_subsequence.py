def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    lcs_list = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs_list.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], list(reversed(lcs_list))


A = ["Milk","Bread","Eggs","Butter","Cheese","Apples","Bananas","Yogurt","Coffee","Sugar","Flour","Salt"]
B = ["Bread","Butter","Cheese","Bananas","Yogurt","Orange Juice","Coffee","Sugar","Flour","Olive Oil","Salt"]

length, sequence = lcs(A, B)

print("Sequence A:", A)
print("Sequence B:", B)
print("LCS Length:", length)
print("LCS:", sequence)
