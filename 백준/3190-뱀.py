from collections import deque
import sys

input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상(0) 우(1) 하(2) 좌(3)

n = int(input())
k = int(input())
board = [[0 for i in range(n + 1)] for j in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

m = int(input())
snake_move_per_second = {}

for _ in range(m):
    s, d = map(str, input().split())
    snake_move_per_second[int(s)] = d

cur_direction = 1
tail_locations = deque([(1, 1)])
head_r, head_c = 1, 1
second = 0

while True:
    if second in snake_move_per_second:
        if snake_move_per_second[second] == "L":
            cur_direction -= 1
            if cur_direction == -1:
                cur_direction = 3
        else:
            cur_direction += 1
            if cur_direction == 4:
                cur_direction = 0

    second += 1

    head_nr, head_nc = head_r + directions[cur_direction][0], head_c + directions[cur_direction][1]
    if head_nr < 1 or head_nr > n or head_nc < 1 or head_nc > n or board[head_nr][head_nc] == -1:
        print(second)
        break

    tail_locations.append((head_nr, head_nc))

    if board[head_nr][head_nc] == 0:
        tail_r, tail_c = tail_locations.popleft()
        board[tail_r][tail_c] = 0

    board[head_nr][head_nc] = -1
    head_r, head_c = head_nr, head_nc
