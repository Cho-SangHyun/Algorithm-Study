from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


def solution(n, m, board):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    empty_count = 0
    virus = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 2:
                virus.append((r, c))
            elif board[r][c] == 0:
                empty_count += 1

    answers = []

    for activate_viruses in combinations(virus, m):
        q = deque([])
        visited = set()
        for r, c in activate_viruses:
            q.append((r, c, 0))
            visited.add((r, c))

        empty_to_virus_count = 0

        while q:
            r, c, h = q.popleft()
            if board[r][c] == 0:
                empty_to_virus_count += 1
            if empty_to_virus_count == empty_count:
                answers.append(h)
                break
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                if board[nr][nc] != 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    q.append((nr, nc, h + 1))

    if answers:
        return min(answers)
    return -1


N, M = map(int, input().split())
_board = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, M, _board))
