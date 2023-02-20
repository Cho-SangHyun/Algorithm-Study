import sys
import heapq
input = sys.stdin.readline
INF = 987654321
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
i = 1

while True:
    n = int(input())
    if not n:
        exit()
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    distance = [[INF for i in range(n)] for j in range(n)]
    distance[0][0] = board[0][0]

    q = []
    heapq.heappush(q, (board[0][0], 0, 0))

    while q:
        dist, r, c = heapq.heappop(q)
        if distance[r][c] < dist:
            continue
        for direction in directions:
            nr, nc = r + direction[0], c + direction[1]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if dist + board[nr][nc] < distance[nr][nc]:
                distance[nr][nc] = dist + board[nr][nc]
                heapq.heappush(q, (distance[nr][nc], nr, nc))

    print(f'Problem {i}:', distance[n - 1][n - 1])
    i += 1


