import sys
input = sys.stdin.readline

n = int(input())
costs = [[]]
# 0 : R, 1 : G, 2 : B

for _ in range(n):
    costs.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(n + 1)]
dp[1][0], dp[1][1], dp[1][2] = costs[1][0], costs[1][1], costs[1][2]

for i in range(2, n + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

print(min(dp[n]))
