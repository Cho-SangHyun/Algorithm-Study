import sys

input = sys.stdin.readline

N = int(input())

tips = []

for _ in range(N):
    tips.append(int(input()))

tips.sort(reverse=True)

last = N

for i in range(0, N):
    tips[i] -= i
    if tips[i] <= 0:
        last = i
        break

print(sum(tips[:last]))