from collections import deque
import sys
input = sys.stdin.readline

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, input().split())
board =[[]]
for _ in range(n):
    row = [0] + list(map(int, input().strip()))
    board.append(row)

q = deque([])
visited = set()
q.append((1, 1, 1, False))
visited.add((1, 1, False))

while q:
    r, c, step, used_weapon = q.popleft()
    if (r, c) == (n, m):
        print(step)
        exit()
    for direction in directions:
        nr, nc = r + direction[0], c + direction[1]
        if nr < 1 or nr > n or nc < 1 or nc > m:
            continue
        if (nr, nc, used_weapon) not in visited and not board[nr][nc]:
            visited.add((nr, nc, used_weapon))
            q.append((nr, nc, step + 1, used_weapon))
            continue
        if (nr, nc, True) not in visited and board[nr][nc] and not used_weapon:
            visited.add((nr, nc, True))
            q.append((nr, nc, step + 1, True))

print(-1)
