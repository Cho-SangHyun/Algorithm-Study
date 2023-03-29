from collections import deque
import sys
input = sys.stdin.readline

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

maps = [list(map(str, input().strip())) for _ in range(12)]
answer = 0

while True:
    visited = set()
    puyo_group = []
    for i in range(11, -1, -1):
        for j in range(6):
            if maps[i][j] != "." and (i, j) not in visited:
                closest_same_color_group = [(i, j)]
                visited.add((i, j))
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nr >= 12 or nc < 0 or nc >= 6:
                            continue
                        if (nr, nc) not in visited and maps[nr][nc] == maps[i][j]:
                            visited.add((nr, nc))
                            closest_same_color_group.append((nr, nc))
                            q.append((nr, nc))

                if len(closest_same_color_group) >= 4:
                    puyo_group += closest_same_color_group

    if puyo_group:
        puyo_group.sort()
        for r, c in puyo_group:
            maps[r][c] = "."
            for nr in range(r - 1, -1, -1):
                maps[nr + 1][c] = maps[nr][c]
            maps[0][c] = "."
        answer += 1
    else:
        break

print(answer)


