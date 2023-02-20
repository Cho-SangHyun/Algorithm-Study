import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))

lines.sort()

final_lines = []
cur_s, cur_e = -1, -1
for line in lines:
    s, e = min(line), max(line)
    if s > cur_e:
        final_lines.append([cur_s, cur_e])
        cur_s, cur_e = s, e
        continue
    if s <= cur_e < e:
        cur_e = e

final_lines.append([cur_s, cur_e])

answer = 0
last_pan_e = -1

for i, line in enumerate(final_lines):
    if i == 0:
        continue
    s, e = line

    if e <= last_pan_e:
        continue

    if s <= last_pan_e:
        s = last_pan_e

    pan_count = (e - s) // k if (e - s) % k == 0 else (e - s) // k + 1
    answer += pan_count
    last_pan_e = s + k * pan_count

print(answer)
