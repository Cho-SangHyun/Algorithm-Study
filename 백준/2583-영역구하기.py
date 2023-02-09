import sys

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = sys.stdin.readline

m, n, k = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            board[r][c] = 1

area_count = 0
area_spaces = []
visited = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

for i in range(m):
    for j in range(n):
        if not visited[i][j] and not board[i][j]:
            area_count += 1
            space = 1
            stack = [(i, j)]
            visited[i][j] = 1
            while stack:
                r, c = stack.pop()
                for direction in directions:
                    nr, nc = r + direction[0], c + direction[1]
                    if 0 > nr or nr >= m or 0 > nc or nc >= n:
                        continue
                    if not visited[nr][nc] and not board[nr][nc]:
                        space += 1
                        visited[nr][nc] = 1
                        stack.append((nr, nc))
            area_spaces.append(space)

area_spaces.sort()
print(area_count)
for space in area_spaces:
    print(space)
