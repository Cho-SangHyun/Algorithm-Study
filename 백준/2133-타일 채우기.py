N = int(input())

if N % 2 == 1:
    print(0)
else:
    dp = [0 for _ in range(N + 3)]
    dp[0] = 1
    dp[2] = 3
    dp[4] = 11

    for i in range(6, N + 1, 2):
        dp[i] += dp[i - 2] * 3
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2
    
    print(dp[N])
    