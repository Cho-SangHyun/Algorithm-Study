import sys

input = sys.stdin.readline

N = int(input())

length = list(map(int, input().split()))

cost = list(map(int, input().split()))

ans = cost[0] * length[0]
now_cost = cost[0]

for i in range(1, N - 1):
    new_cost = cost[i]
    now_cost = min(now_cost, cost[i])
    ans += now_cost * length[i]

print(ans)