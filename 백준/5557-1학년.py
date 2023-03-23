import sys
input = sys.stdin.readline

n = int(input())
data = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(21)] for i in range(n + 1)]
# dp[x] = x번째 항까지 연결해서 만들어지는 값들
# dp[x][k] = x번째 항까지 연결해서 만들어지는 값들 중 k가 되는 경우의 수

dp[1][data[1]] = 1

for i in range(2, n):
    for j in range(0, 21):
        if dp[i - 1][j]:
            if 0 <= j + data[i] <= 20:
                dp[i][j + data[i]] += dp[i - 1][j]
            if 0 <= j - data[i] <= 20:
                dp[i][j - data[i]] += dp[i - 1][j]

print(dp[n - 1][data[n]])
