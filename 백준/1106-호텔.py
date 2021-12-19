import sys
sys.setrecursionlimit(100000)

C, N = map(int, sys.stdin.readline().split())

data = [[0, 0]]

dp1 = 101

for _ in range(N):
    new_data = list(map(int, sys.stdin.readline().split()))
    dp1 = min(dp1, new_data[0])
    data.append(new_data)
# dp[x] : x명을 늘리기 위해 들이는 최소비용, dp1 = 가장 적은 비용이 들어가는 도시
dp = [0 for _ in range(C + 1)]
dp[1] = dp1

def solution(x):
    if x <= 0:
        return 0
    if not dp[x]:
        Hoobo = [data[i][0] + solution(x - data[i][1]) for i in range(1, len(data))]
        dp[x] = min(Hoobo)
    return dp[x]

print(solution(C))

