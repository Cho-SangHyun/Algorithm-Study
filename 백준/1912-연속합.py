# 무식한 방법 : 1항 ~ N항까지 순회하며 각 항에서 시작하는 연속합들 중 가장 큰 거 찾기
# 시간복잡도는 N^2이 걸리며 시간초과

# 부분문제로 쪼개기 : 
# 1항으로 시작하는 최대연속합
# 2항으로 시작하는 최대연속합
# 3항으로 시작하는 최대연속합
# 이런 거 에서 max찾기

# 1항에서 시작하는 최대연속합 = 자기자신 + 2항에서 시작하는 최대연속합
#                      또는 자기자신. 이 둘 중 더 큰 값

# 이 논리로 푼다. 2항에서 시작하는 최대연속합이 음수라면 자기자신이 더 큰 경우가 됨


import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))
# 주석과는 반대로 DP테이블을 i항으로 끝나는 최대부분합으로 정의
dp = [-1000 for _ in range(N)]
dp[0] = data[0]

for i in range(1, N):
    dp[i] = max(data[i], dp[i - 1] + data[i])

print(max(dp))
