from collections import deque
import sys
input = sys.stdin.readline


def solution(n, min_d, max_d, board):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    answer = 0

    while True:
        grouped = [[0for i in range(n + 1)] for j in range(n + 1)]
        union_groups = []

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if not grouped[i][j]:
                    q = deque([(i, j)])
                    group = set()

                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if nr < 1 or nr > n or nc < 1 or nc > n:
                                continue
                            if min_d <= abs(board[r][c] - board[nr][nc]) <= max_d and not grouped[nr][nc]:
                                group.add((r, c))
                                group.add((nr, nc))
                                grouped[r][c] = 1
                                grouped[nr][nc] = 1
                                q.append((nr, nc))
                    if group:
                        union_groups.append(group)

        if not union_groups:
            break

        for group in union_groups:
            total_people = 0
            for r, c in group:
                total_people += board[r][c]
            for r, c in group:
                board[r][c] = total_people // len(group)

        answer += 1

    return answer


N, L, R = map(int, input().split())
game_board =[[]]

for _ in range(N):
    row = [0] + list(map(int, input().split()))
    game_board.append(row)

print(solution(N, L, R, game_board))
