import sys

N, data = int(input()), [[0, 0]]

for _ in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))

data.sort()

dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = 1
    for j in range(1, i):
        if data[j][1] < data[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
