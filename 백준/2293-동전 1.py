import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

value = []

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for i in range(n):
    _input = int(input())
    value.append(_input)

for v in value:
    for i in range(1, k + 1):
        if i - v >= 0:
            dp[i] += dp[i - v]

print(dp[k])
