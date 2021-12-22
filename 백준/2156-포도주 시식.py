n = int(input())

data = [0]

for _ in range(n):
    data.append(int(input()))

"""
dp[n][0] : n번째 잔까지 마시는데 그냥 마시는
dp[n][1] : n번째 잔까지 마시는데 연속으로 마시는
"""
dp = [[0, 0] for _ in range(n + 1)]

dp[1][0], dp[1][1] = data[1], data[1]

for i in range(2, n + 1):
    dp[i][0] = max(dp[i - 3] + dp[i - 2]) + data[i]
    dp[i][1] = dp[i - 1][0] + data[i]

print(max(
    max(dp[n - 1]),
    max(dp[n])
))
