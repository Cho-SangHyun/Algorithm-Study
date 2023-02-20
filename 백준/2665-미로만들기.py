import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().strip())))

q = []
heapq.heappush(q, (0, 0, 0))
distance = [[INF for j in range(n)] for i in range(n)]
distance[0][0] = 0

while q:
    dist, r, c = heapq.heappop(q)
    if distance[r][c] < dist:
        continue
    for direction in directions:
        nr, nc = r + direction[0], c + direction[1]
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        new_dist = dist + 1 if board[nr][nc] == 0 else dist
        if new_dist < distance[nr][nc]:
            distance[nr][nc] = new_dist
            heapq.heappush(q, (new_dist, nr, nc))

print(distance[n - 1][n - 1])
