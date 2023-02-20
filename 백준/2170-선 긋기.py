import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))

lines.sort()

answer = 0
cur_s, cur_e = -9876543210, -9876543210

for line in lines:
    s, e = min(line), max(line)
    if cur_e < s:
        answer += (cur_e - cur_s)
        cur_s = s
        cur_e = e
    elif s <= cur_e < e:
        cur_e = e

answer += (cur_e - cur_s)

print(answer)
