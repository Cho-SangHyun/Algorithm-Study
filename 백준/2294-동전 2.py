# 2294 - 동전 2
# n가지 종류 동전을 조합해 가치가 k원이 되게 하는 경우 중 동전이 최소가 될 땐?
# 불가능한 경우는 -1 출력

# 1. 무식하게 접근
# 가능한 모든 동전조합에서 최소 개수가 되는 케이스 찾기

# 2. 부분문제로 쪼개기 가능?
# 가치가 n1, n2, n3인 동전들이 있고 k를 만들어야 할 때,
# k - n1을 만들어내는 경우 + 1
# k - n2를 만들어내는 경우 + 1
# k - n3를 만들어내는 경우 + 1
# 중 가장 작은 값을 취하면 됨

# 3. 중복되는 경우 있음?
# ㅇㅇ

# DP go. 전형적인 DP문제라는 것이 보인다.

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
# n : 동전 수, k : 만들어야 할 가치
n, k = map(int, input().split())

dp = [0 for i in range(k + 1)]
calculated = [0 for i in range(k + 1)]
coin_values = []

calculated[0] = 1

for _ in range(n):
    coin_values.append(int(input()))

def solution(x):
    # dp[x]를 구한 적 없다면, 구해라
    if not calculated[x]:
        ways = []
        for v in coin_values:
            if x - v >= 0:
                w = solution(x - v)
                # dp[x - v]가 불가능한 값이 아니라면, 후보목록 추가
                if w != -1:
                    ways.append(w)
        if ways:
            dp[x] = min(ways) + 1
        # ways가 빔 -> 모든 후보가 불가능한 것이므로 dp[x]는 불가능 처리
        else:
            dp[x] = -1
        calculated[x] = 1
    return dp[x]

print(solution(k))




    
    


