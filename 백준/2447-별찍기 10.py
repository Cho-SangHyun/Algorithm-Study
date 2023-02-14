import sys
sys.setrecursionlimit(10**9)

n = int(input())

board = [[" " for i in range(n + 1)] for j in range(n + 1)]


def draw_star(r, c, length):
    if length == 3:
        for i in range(r, r + length):
            for j in range(c, c + length):
                if i == r + 1 and j == c + 1:
                    continue
                board[i][j] = "*"
        return

    divided_length = length // 3
    # 좌상
    draw_star(r, c, divided_length)
    # 상단
    draw_star(r, c + divided_length, divided_length)
    # 우상
    draw_star(r, c + 2 * divided_length, divided_length)
    # 우측
    draw_star(r + divided_length, c + 2 * divided_length, divided_length)
    # 우하
    draw_star(r + 2 * divided_length, c + 2 * divided_length, divided_length)
    # 하
    draw_star(r + 2 * divided_length, c + divided_length, divided_length)
    # 좌하
    draw_star(r + 2 * divided_length, c, divided_length)
    # 좌
    draw_star(r + divided_length, c, divided_length)


draw_star(1, 1, n)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(board[i][j], end='')
    print()
