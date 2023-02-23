def solution(n):
    dp = [987654321 for i in range(n + 1)]
    for i in range(1, n + 1):
        if i ** 2 > n:
            break
        dp[i ** 2] = 1

    count = 0
    for i in range(1, n + 1):
        if dp[i] == 1:
            count += 1
        for j in range(1, count + 1):
            dp[i] = min(dp[i], dp[i - j ** 2] + 1)

    return dp[n]


N = int(input())
print(solution(N))
