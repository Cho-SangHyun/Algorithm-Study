import sys
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

n, m = map(int, input().split())
cur_r, cur_c, cur_direction = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = 0


def can_clean_side(r, c):
    for direction in directions:
        nr, nc = r + direction[0], c + direction[1]
        if nr < 0 or nr >= n or nc < 0 or nc >= m:
            continue
        if board[nr][nc] == 0:
            return True
    return False


def can_go_back(r, c, direction):
    nr, nc = 0, 0
    if direction == 0:
        nr, nc = r + 1, c
    elif direction == 1:
        nr, nc = r, c - 1
    elif direction == 2:
        nr, nc = r - 1, c
    elif direction == 3:
        nr, nc = r, c + 1

    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        return False
    if board[nr][nc] == 1:
        return False
    return True


def go_back(r, c, direction):
    nr, nc = 0, 0
    if direction == 0:
        nr, nc = r + 1, c
    elif direction == 1:
        nr, nc = r, c - 1
    elif direction == 2:
        nr, nc = r - 1, c
    elif direction == 3:
        nr, nc = r, c + 1

    return (nr, nc)


def can_go_forward(r, c, direction):
    nr, nc = 0, 0
    if direction == 0:
        nr, nc = r - 1, c
    elif direction == 1:
        nr, nc = r, c + 1
    elif direction == 2:
        nr, nc = r + 1, c
    elif direction == 3:
        nr, nc = r, c - 1

    if nr < 0 or nr >= n or nc < 0 or nc >= m:
        return False
    if board[nr][nc] == 0:
        return True
    return False


def go_forward(r, c, direction):
    nr, nc = 0, 0
    if direction == 0:
        nr, nc = r - 1, c
    elif direction == 1:
        nr, nc = r, c + 1
    elif direction == 2:
        nr, nc = r + 1, c
    elif direction == 3:
        nr, nc = r, c - 1
    return (nr, nc)


while True:
    if board[cur_r][cur_c] == 0:
        answer += 1
        board[cur_r][cur_c] = -1
    if can_clean_side(cur_r, cur_c):
        cur_direction -= 1
        if cur_direction == -1:
            cur_direction = 3

        while not can_go_forward(cur_r, cur_c, cur_direction):
            cur_direction -= 1
            if cur_direction == -1:
                cur_direction = 3

        cur_r, cur_c = go_forward(cur_r, cur_c, cur_direction)
        continue
    if can_go_back(cur_r, cur_c, cur_direction):
        cur_r, cur_c = go_back(cur_r, cur_c, cur_direction)
        continue
    break

print(answer)
