import sys

N = int(input())

data = [0] + list(map(int, sys.stdin.readline().split()))

answers = []
# dp[x] : x번째 수를 마지막 원소로 갖는 LIS의 길이
dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = 1
    for j in range(1, i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))