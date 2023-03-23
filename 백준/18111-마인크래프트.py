import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
maps = []

heights_cnt = [0 for _ in range(257)]

for _ in range(n):
    row = list(map(int, input().split()))
    for h in row:
        heights_cnt[h] += 1

heights = []

for h in range(256, -1, -1):
    for _ in range(heights_cnt[h]):
        heights.append(h)

for i in range(0, n * m, m):
    maps.append(heights[i:i+m])

max_height, min_height = maps[0][0], maps[n - 1][m - 1]
answer_height, answer_time = 0, 987654321

for h in range(min_height, max_height + 1):
    inventory = b
    up, down = 0, 0
    for r in range(n):
        for c in range(m):
            if maps[r][c] > h:
                up += maps[r][c] - h
            elif maps[r][c] < h:
                down += h - maps[r][c]
    if up + b >= down:
        time = up * 2 + down
        if time <= answer_time:
            answer_height = h
            answer_time = time

print(answer_time, answer_height)
