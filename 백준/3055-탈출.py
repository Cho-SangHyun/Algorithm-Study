from collections import deque
import sys
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution(n, m, board):
    water_locations = [set() for _ in range(5000)]
    water = set()
    human_r, human_c = 0, 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] == "*":
                water_locations[0].add((i, j))
                water.add((i, j))
            elif board[i][j] == "S":
                human_r, human_c = i, j

    q = deque([(human_r, human_c, 0)])
    visited = set([(human_r, human_c)])

    while q:
        r, c, second = q.popleft()

        if board[r][c] == "D":
            return second

        for wr, wc in water_locations[second]:
            for dr, dc in directions:
                nr, nc = wr + dr, wc + dc
                if nr < 1 or nr > n or nc < 1 or nc > m:
                    continue
                if board[nr][nc] not in ("D", "X") and (nr, nc) not in water:
                    water.add((nr, nc))
                    water_locations[second + 1].add((nr, nc))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 1 or nr > n or nc < 1 or nc > m:
                continue
            if (nr, nc) in visited:
                continue
            if board[nr][nc] not in ("*", "X") and (nr, nc) not in water:
                visited.add((nr, nc))
                q.append((nr, nc, second + 1))

    return "KAKTUS"


R, C = map(int, input().split())
game_board =[[]]
for _ in range(R):
    game_board.append([''] + list(map(str, input().strip())))

print(solution(R, C, game_board))
