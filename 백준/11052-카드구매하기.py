import sys, copy
input = sys.stdin.readline

n = int(input())
costs = [0] + list(map(int, input().split()))
dp = copy.deepcopy(costs)

for i in range(2, n + 1):
    temp = [dp[i]]
    for j in range(1, i // 2 + 1):
        temp.append(dp[j] + dp[i - j])
    dp[i] = max(temp)

print(dp[n])
