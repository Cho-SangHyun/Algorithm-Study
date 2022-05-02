# 무식한 방법 : 1항 ~ N항까지 순회하며 각 항에서 시작하는 연속합들 중 가장 큰 거 찾기
# 시간복잡도는 N^2이 걸리며 시간초과

# 부분문제로 쪼개기 : 
# 1항으로 끝나는 최대연속합
# 2항으로 끝나는 최대연속합
# 3항으로 끝는 최대연속합
# 이런 거 에서 max찾기

# dp[x] = x항으로 끝나는 최대연속합 = 1) x - 1항으로 끝나는 최대연속합 + 자기자신
#                              2)자기자신. 
#                              이 둘 중 더 큰 값

# ex) 데이터 : 1 -2 2 2 2 
#      dp값 : 1 -1 2 4 6


import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

dp = [-1000 for _ in range(N)]
dp[0] = data[0]

for i in range(1, N):
    dp[i] = max(data[i], dp[i - 1] + data[i])

print(max(dp))
