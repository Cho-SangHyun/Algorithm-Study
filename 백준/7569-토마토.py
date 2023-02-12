from collections import deque
import sys

input = sys.stdin.readline
directions = [(1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (-1, 0, 0)]

M, N, H = map(int, input().split())
boxes = [[]]
for i in range(H):
    box = [[]]
    for _ in range(N):
        row = [0] + list(map(int, input().split()))
        box.append(row)
    boxes.append(box)

q = deque([])
visited = set()

for i in range(1, H + 1):
    for j in range(1, N + 1):
        for k in range(1, M + 1):
            if boxes[i][j][k] == 1:
                q.append((i, j, k, 0))
                visited.add((i, j, k))

if not q:
    print(-1)
    exit()

answer = -1

while q:
    h, r, c, day = q.popleft()
    answer = max(answer, day)
    for direction in directions:
        nh, nr, nc = h + direction[0], r + direction[1], c + direction[2]
        if nh < 1 or nh > H or nr < 1 or nr > N or nc < 1 or nc > M:
            continue
        if (nh, nr, nc) not in visited and boxes[nh][nr][nc] == 0:
            visited.add((nh, nr, nc))
            q.append((nh, nr, nc, day + 1))
            boxes[nh][nr][nc] = 1


for i in range(1, H + 1):
    for j in range(1, N + 1):
        for k in range(1, M + 1):
            if boxes[i][j][k] == 0:
                print(-1)
                exit()

print(answer)
