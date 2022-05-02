# 기존 연속합 문제는 O(N)의 시간이 걸림
# 원소 하나를 제거 가능한데 N은 최대 10만이므로
# 원소를 하나하나 제거하며 dp를 돌리면 N * O(N) = O(N^2) = 시간초과

# 원소를 제거하는 어떠한 방법이 필요
# 1. 음수만 제거대상이다. (그러나 음수가 몇 개만 나온다는 제약 X, 따라서 무용지물)
# 2. 제일 절댓값이 큰 음수를 제거 => 반례 :원소가 1, -2, 2, 2, 2, -3, -4처럼 되어있으면 
#    -2를 제거하는게 이득임


import sys

input = sys.stdin.readline

N = int(input())

data = [0] + list(map(int, input().split()))

dp = [[] for _ in range(100002)]
dp[0] = [-999999999, -999999999, -999999999]
dp[1] = [data[1], -999999999, -999999999]

for i in range(2, N + 1):
    dp[i] = [
        max(dp[i - 1][0] + data[i], data[i]), # 점프없이 이어지는 경우
        dp[i - 2][0] + data[i], # i - 2항에서 점프한 경우
        max(dp[i - 1][2] + data[i], dp[i - 1][1] + data[i]) # 기존에 점프를 한 경우의 최대
    ]

answer = -999999999

for i in range(1, N + 1):
    answer = max(answer, max(dp[i]))

print(answer)
