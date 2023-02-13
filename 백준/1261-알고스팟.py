import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

m, n = map(int, input().split())
board = [[]]

for _ in range(n):
    row = [0] + list(map(int, input().strip()))
    board.append(row)

costs = [[INF for i in range(m + 1)] for j in range(n + 1)]
costs[1][1] = 0

q = []
heapq.heappush(q, (0, 1, 1))

while q:
    cost, r, c = heapq.heappop(q)
    if costs[r][c] < cost:
        continue
    for direction in directions:
        nr, nc = r + direction[0], c + direction[1]
        if nr < 1 or nr > n or nc < 1 or nc > m:
            continue

        if board[nr][nc] == 0 and cost < costs[nr][nc]:
            costs[nr][nc] = cost
            heapq.heappush(q, (cost, nr, nc))
        if board[nr][nc] == 1 and cost + 1 < costs[nr][nc]:
            costs[nr][nc] = cost + 1
            heapq.heappush(q, (cost + 1, nr, nc))

print(costs[n][m])
