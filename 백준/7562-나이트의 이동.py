from collections import deque
import sys
input = sys.stdin.readline

directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
T = int(input())

for _ in range(T):
    board_length = int(input())
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())

    visited = set()
    q = deque([])
    q.append((sr, sc, 0))
    visited.add((sr, sc))

    answer = 987654321
    while q:
        r, c, step = q.popleft()
        if (r, c) == (er, ec):
            answer = min(answer, step)
            break
        for direction in directions:
            nr, nc = r + direction[0], c + direction[1]
            if 0 > nr or nr >= board_length or 0 > nc or nc >= board_length:
                continue
            if (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, step + 1))
    print(answer)
