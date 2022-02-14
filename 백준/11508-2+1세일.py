import sys

N = int(input())

dc = N // 3

cost = []

for _ in range(N):
    cost.append(int(sys.stdin.readline()))

cost.sort(reverse=True)

i = 0

while i != dc:
    cost[2 + 3*i] = 0
    i += 1

print(sum(cost))