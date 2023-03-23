from collections import deque
import sys
input = sys.stdin.readline


def is_melting(maps, outside, r, c, n, m):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    count = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr < 1 or nc < 1 or nr > n or nc > m:
            continue
        if not maps[nr][nc] and outside[nr][nc]:
            count += 1
    return True if count > 1 else False


def solution(n, m, maps):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(n):
        maps[i] = [0] + maps[i]
    maps = [[]] + maps

    outside = [[0 for i in range(m + 1)] for j in range(n + 1)]
    outside[1][1] = 1
    q = deque([(1, 1)])
    visited = set([(1, 1)])

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 1 or nc < 1 or nr > n or nc > m:
                continue
            if maps[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                outside[nr][nc] = 1
                q.append((nr, nc))

    answer = 0
    while True:
        melting_count = 0
        melting_area = []
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if maps[i][j] and is_melting(maps, outside, i, j, n, m):
                    melting_count += 1
                    melting_area.append((i, j))

        if not melting_count:
            break

        for i, j in melting_area:
            maps[i][j] = 0
            outside[i][j] = 1
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 1 or nc < 1 or nr > n or nc > m:
                        continue
                    if not maps[nr][nc] and not outside[nr][nc]:
                        outside[nr][nc] = 1
                        q.append((nr, nc))
        answer += 1

    return answer


N, M = map(int, input().split())
_maps = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, M, _maps))
