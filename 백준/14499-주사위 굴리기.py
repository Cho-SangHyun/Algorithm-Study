import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
r, c = x + 1, y + 1

board = [[]]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    board.append(row)

commands = list(map(int, input().split()))
          # 상 하  앞 뒤 좌 우
play_box = [0, 0, 0, 0, 0, 0]


def move(command):
    top, bottom, front, back, left, right = play_box

    if command == 1: # 동쪽
        play_box[0] = left
        play_box[1] = right
        play_box[2] = front
        play_box[3] = back
        play_box[4] = bottom
        play_box[5] = top
    elif command == 2: # 서쪽
        play_box[0] = right
        play_box[1] = left
        play_box[2] = front
        play_box[3] = back
        play_box[4] = top
        play_box[5] = bottom
    elif command == 3: # 북쪽
        play_box[0] = front
        play_box[1] = back
        play_box[2] = bottom
        play_box[3] = top
        play_box[4] = left
        play_box[5] = right
    elif command == 4: # 남쪽
        play_box[0] = back
        play_box[1] = front
        play_box[2] = top
        play_box[3] = bottom
        play_box[4] = left
        play_box[5] = right


for cmd in commands:
    nr, nc = 0, 0
    if cmd == 1:
        nr, nc = r, c + 1
        if nc > m:
            continue

    elif cmd == 2:
        nr, nc = r, c - 1
        if nc < 1:
            continue

    elif cmd == 3:
        nr, nc = r - 1, c
        if nr < 1:
            continue

    elif cmd == 4:
        nr, nc = r + 1, c
        if nr > n:
            continue

    move(cmd)
    print(play_box[0])

    if board[nr][nc]:
        play_box[1] = board[nr][nc]
        board[nr][nc] = 0
    else:
        board[nr][nc] = play_box[1]

    r, c = nr, nc
