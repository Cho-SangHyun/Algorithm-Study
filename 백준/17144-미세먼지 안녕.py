import sys
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def clean_upside(r, c, board):
    for nr in range(r - 1, -1, -1):
        value = board[nr][0]
        board[nr][0] = 0
        if nr + 1 != r:
            board[nr + 1][0] = value

    for nc in range(1, len(board[0])):
        value = board[0][nc]
        board[0][nc] = 0
        board[0][nc - 1] = value

    for nr in range(1, r + 1):
        value = board[nr][-1]
        board[nr][-1] = 0
        board[nr - 1][-1] = value

    for nc in range(len(board[0]) - 2, 0, -1):
        value = board[r][nc]
        board[r][nc] = 0
        board[r][nc + 1] = value


def clean_downside(r, c, board):
    for nr in range(r + 1, len(board)):
        value = board[nr][0]
        board[nr][0] = 0
        if nr - 1 != r:
            board[nr - 1][0] = value

    for nc in range(1, len(board[0])):
        value = board[-1][nc]
        board[-1][nc] = 0
        board[-1][nc - 1] = value

    for nr in range(len(board) - 2, r - 1, -1):
        value = board[nr][-1]
        board[nr][-1] = 0
        board[nr + 1][-1] = value

    for nc in range(len(board[0]) - 2, 0, -1):
        value = board[r][nc]
        board[r][nc] = 0
        board[r][nc + 1] = value


def solution(r, c, t, board):
    air_row_index = []
    for i in range(r):
        if board[i][0] == -1:
            air_row_index.append(i)

    upside_air = (min(air_row_index), 0)
    downside_air = (max(air_row_index), 0)

    for _ in range(t):
        add_num = [[0 for i in range(c)] for j in range(r)]
        # 확산
        for i in range(r):
            for j in range(c):
                if board[i][j] > 4:
                    add_count = 0
                    for dr, dc in directions:
                        nr, nc = i + dr, j + dc
                        if nr < 0 or nc < 0 or nr >= r or nc >= c or board[nr][nc] == -1:
                            continue
                        add_num[nr][nc] += (board[i][j] // 5)
                        add_count += 1
                    board[i][j] -= (board[i][j] // 5) * add_count

        for i in range(r):
            for j in range(c):
                board[i][j] += add_num[i][j]

        clean_upside(upside_air[0], upside_air[1], board)
        clean_downside(downside_air[0], downside_air[1], board)

    answer = 0
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                answer += board[i][j]

    return answer


R, C, T = map(int, input().split())
_board = [list(map(int, input().split())) for _ in range(R)]


print(solution(R, C, T, _board))
