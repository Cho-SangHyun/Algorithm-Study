from collections import deque
import sys
input = sys.stdin.readline




def solution(n, maps):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    i = 1
    for r in range(n):
        for c in range(n):
            if maps[r][c] and (r, c) not in visited:
                visited.add((r, c))
                maps[r][c] = i
                q = deque([(r, c)])
                while q:
                    now_r, now_c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = now_r + dr, now_c + dc
                        if nr < 0 or nc < 0 or nc >= n or nr >= n:
                            continue
                        if maps[nr][nc] and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            maps[nr][nc] = i
                            q.append((nr, nc))
                i += 1

    answer = 987654321

    for i in range(n):
        for j in range(n):
            if maps[i][j]:
                start = maps[i][j]
                q = deque([(i, j, 0)])
                visited = set([(i, j)])

                while q:
                    r, c, dist = q.popleft()
                    if maps[r][c] and maps[r][c] != start:
                        answer = min(answer, dist - 1)
                        break
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nc >= n or nr >= n:
                            continue
                        if maps[nr][nc] != start and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc, dist + 1))

    return answer


N = int(input())
_maps = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, _maps))
