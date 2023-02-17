import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, input().split())

board =[[]]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    board.append(row)

answer_count = 0
answer_width = 0
stack = []
visited = [[0 for i in range(m + 1)] for j in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if not visited[i][j] and board[i][j]:
            answer_count += 1
            visited[i][j] = 1
            mid_answer_width = 1
            stack.append((i, j))

            while stack:
                r, c = stack.pop()
                for direction in directions:
                    nr, nc = r + direction[0], c + direction[1]
                    if nr < 1 or nr > n or nc < 1 or nc > m:
                        continue
                    if not visited[nr][nc] and board[nr][nc]:
                        visited[nr][nc] = 1
                        mid_answer_width += 1
                        stack.append((nr, nc))

            answer_width = max(answer_width, mid_answer_width)

print(answer_count)
print(answer_width)
