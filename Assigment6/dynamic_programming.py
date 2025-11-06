def maximizeROI(budget, projects):
    n = len(projects)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = projects[i - 1]['cost']
        roi = projects[i - 1]['roi']
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], roi + dp[i - 1][b - cost])
            else:
                dp[i][b] = dp[i - 1][b]
