from collections import deque
import sys
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_there_cheese(n, m, board):
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                return True
    return False


def count_cheese(n, m, board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                count += 1
    return count


def solution(n, m, board):
    outside = [[0 for i in range(m)] for j in range(n)]
    q = deque([(0, 0)])
    outside[0][0] = 1

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            if not board[nr][nc] and not outside[nr][nc]:
                outside[nr][nc] = 1
                q.append((nr, nc))

    hour = 0
    last_remained = 0

    while is_there_cheese(n, m, board):
        last_remained = count_cheese(n, m, board)
        hour += 1
        remove_cheese = []
        for r in range(n):
            for c in range(m):
                if board[r][c]:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if outside[nr][nc]:
                            remove_cheese.append((r, c))
                            break
        for r, c in remove_cheese:
            board[r][c] = 0
            outside[r][c] = 1
            q = deque([(r, c)])

            while q:
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if not board[ni][nj] and not outside[ni][nj]:
                        outside[ni][nj] = 1
                        q.append((ni, nj))

    return [hour, last_remained]


N, M = map(int, input().split())
_board = [list(map(int, input().split())) for _ in range(N)]

answers = solution(N, M, _board)

for ans in answers:
    print(ans)
