import sys

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = sys.stdin.readline

n, m = map(int, input().split())
board = [[]]
for _ in range(n):
    row = ' ' + input().strip()
    board.append(row)

answer = -1
visited = set([board[1][1]])


def dfs(r, c, step):
    global answer
    answer = max(answer, step)

    for direction in directions:
        nr, nc = r + direction[0], c + direction[1]
        if 1 > nr or n < nr or 1 > nc or m < nc:
            continue
        if board[nr][nc] not in visited:
            visited.add(board[nr][nc])
            dfs(nr, nc, step + 1)
            visited.remove(board[nr][nc])


dfs(1, 1, 1)

print(answer)