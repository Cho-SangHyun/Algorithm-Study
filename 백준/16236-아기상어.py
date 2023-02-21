from collections import deque
import sys

input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n = int(input())
board = [[]]

for _ in range(n):
    row = [0] + list(map(int, input().split()))
    board.append(row)

shark_r, shark_c, shark_size, eating_count = 0, 0, 2, 0
answer = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if board[i][j] == 9:
            shark_r, shark_c = i, j


def get_small_fish_locations(r, c, size):
    locations = []
    visited = [[0 for k in range(n + 1)] for m in range(n + 1)]
    visited[r][c] = 1

    q = deque([(r, c, 0)])

    while q:
        cur_r, cur_c, dist = q.popleft()
        if board[cur_r][cur_c] and board[cur_r][cur_c] < size and not (cur_r == r and cur_c == c):
            locations.append([cur_r, cur_c, dist])
        for direction in directions:
            nr, nc = cur_r + direction[0], cur_c + direction[1]
            if nr < 1 or nr > n or nc < 1 or nc > n:
                continue
            if not visited[nr][nc] and board[nr][nc] <= size:
                visited[nr][nc] = 1
                q.append((nr, nc, dist + 1))

    if locations:
        locations.sort(key=lambda x: (x[2], x[0], x[1]))
    return locations


while True:
    # 먹을 수 있는 물고기 위치들
    small_fish_locations = get_small_fish_locations(shark_r, shark_c, shark_size)
    # 먹을 수 있는 고기가 한 마리도 없을 때
    if len(small_fish_locations) == 0:
        print(answer)
        exit()

    board[shark_r][shark_c] = 0
    eating_count += 1
    if eating_count == shark_size:
        shark_size += 1
        eating_count = 0
    shark_r, shark_c, = small_fish_locations[0][0], small_fish_locations[0][1]
    answer += small_fish_locations[0][2]
    board[shark_r][shark_c] = 9
