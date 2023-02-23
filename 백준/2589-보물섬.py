from collections import deque
import sys
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(n, m, gold_map):
    answer = -1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if gold_map[i][j] == "L":
                q = deque([(i, j, 0)])
                visited = set()
                visited.add((i, j))

                while q:
                    r, c, dist = q.popleft()
                    answer = max(answer, dist)
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 1 or nr > n or nc < 1 or nc > m:
                            continue
                        if (nr, nc) not in visited and gold_map[nr][nc] == "L":
                            visited.add((nr, nc))
                            q.append((nr, nc, dist + 1))

    return answer


N, M = map(int, input().split())
board = [[]]
for _ in range(N):
    row = [''] + list(map(str, input().strip()))
    board.append(row)

print(solution(N, M, board))
