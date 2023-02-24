from collections import deque


def solution(maps):
    answer = -1
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n, m = len(maps), len(maps[0])

    visited = set([(0, 0)])
    q = deque([(0, 0, 1)])

    while q:
        r, c, step = q.popleft()
        if r == n - 1 and c == m - 1:
            return step
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if (nr, nc) not in visited and maps[nr][nc]:
                visited.add((nr, nc))
                q.append((nr, nc, step + 1))

    return answer