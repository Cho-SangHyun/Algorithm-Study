import sys
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, input().split())
board = [[]]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))


def check_side(r, c):
    res = 0
    for direction in directions:
        nr, nc = r + direction[0], c + direction[1]
        if nr < 1 or nr > n or nc < 1 or nc > m:
            continue
        if not board[nr][nc]:
            res += 1
    return res


def down():
    down_locations = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] > 0:
                down_locations.append((i, j, check_side(i, j)))

    for location in down_locations:
        r, c, h = location
        board[r][c] -= h
        if board[r][c] < 0:
            board[r][c] = 0


def dfs():
    stack = []
    visited = set()
    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] and (i, j) not in visited:
                res += 1
                stack.append((i, j))
                visited.add((i, j))

                while stack:
                    r, c = stack.pop()
                    for direction in directions:
                        nr, nc = r + direction[0], c + direction[1]
                        if nr < 1 or nr > n or nc < 1 or nc > m:
                            continue
                        if board[nr][nc] and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            stack.append((nr, nc))

    return res


if dfs() != 1:
    print(0)
    exit()

answer = 1
down()

while True:
    dfs_res = dfs()
    if dfs_res > 1:
        print(answer)
        exit()
    if dfs_res == 0:
        print(0)
        exit()
    down()
    answer += 1

