import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [[]]

for _ in range(N):
    row = [0] + list(map(int, input().split()))
    board.append(row)

answer = -1


def check_type_1():
    global answer
    # 가로
    for r in range(1, N + 1):
        for c in range(1, M - 2):
            mid_sum = sum(board[r][c:c + 4])
            answer = max(answer, mid_sum)

    # 세로
    for r in range(1, N - 2):
        for c in range(1, M + 1):
            mid_sum = 0
            for nr in range(r, r + 4):
                mid_sum += board[nr][c]
            answer = max(answer, mid_sum)


def check_type_2():
    global answer
    for r in range(1, N):
        for c in range(1, M):
            mid_sum = board[r][c] + board[r][c + 1] + board[r + 1][c] + board[r + 1][c + 1]
            answer = max(answer, mid_sum)


def check_type_3():
    global answer
    # X X X
    # X X X
    for r in range(1, N):
        for c in range(1, M - 1):
            mid_answer1 = board[r][c] + board[r + 1][c] + board[r + 1][c + 1] + board[r + 1][c + 2]
            mid_answer2 = board[r + 1][c] + board[r + 1][c + 1] + board[r + 1][c + 2] + board[r][c + 2]
            mid_answer3 = board[r][c] + board[r][c + 2] + board[r][c + 1] + board[r + 1][c]
            mid_answer4 = board[r][c] + board[r][c + 2] + board[r][c + 1] + board[r + 1][c + 2]
            answer = max(answer, mid_answer1, mid_answer2, mid_answer3, mid_answer4)
    # X X
    # X X
    # X X
    for r in range(1, N - 1):
        for c in range(1, M):
            mid_answer1 = board[r][c] + board[r + 1][c] + board[r + 2][c] + board[r][c + 1]
            mid_answer2 = board[r][c] + board[r + 1][c] + board[r + 2][c] + board[r + 2][c + 1]
            mid_answer3 = board[r][c + 1] + board[r + 1][c + 1] + board[r + 2][c + 1] + board[r][c]
            mid_answer4 = board[r][c + 1] + board[r + 1][c + 1] + board[r + 2][c + 1] + board[r + 2][c]
            answer = max(answer, mid_answer1, mid_answer2, mid_answer3, mid_answer4)


def check_type_4():
    global answer
    # X X
    # X X
    # X X
    for r in range(1, N - 1):
        for c in range(1, M):
            mid_answer1 = board[r][c] + board[r + 1][c] + board[r + 1][c + 1] + board[r + 2][c + 1]
            mid_answer2 = board[r][c + 1] + board[r + 1][c] + board[r + 1][c + 1] + board[r + 2][c]
            answer = max(answer, mid_answer1, mid_answer2)
    # X X X
    # X X X
    for r in range(1, N):
        for c in range(1, M - 1):
            mid_answer1 = board[r + 1][c] + board[r + 1][c + 1] + board[r][c + 1] + board[r][c + 2]
            mid_answer2 = board[r][c] + board[r + 1][c + 1] + board[r][c + 1] + board[r + 1][c + 2]
            answer = max(answer, mid_answer1, mid_answer2)


def check_type_5():
    global answer
    # X X X
    # X X X
    for r in range(1, N):
        for c in range(1, M - 1):
            mid_answer1 = board[r][c] + board[r][c + 1] + board[r][c + 2] + board[r + 1][c + 1]
            mid_answer2 = board[r + 1][c] + board[r + 1][c + 1] + board[r + 1][c + 2] + board[r][c + 1]
            answer = max(answer, mid_answer1, mid_answer2)
    # X X
    # X X
    # X X
    for r in range(1, N - 1):
        for c in range(1, M):
            mid_answer1 = board[r][c] + board[r + 1][c] + board[r + 2][c] + board[r + 1][c + 1]
            mid_answer2 = board[r][c + 1] + board[r + 1][c + 1] + board[r + 2][c + 1] + board[r + 1][c]
            answer = max(answer, mid_answer1, mid_answer2)


check_type_1()
check_type_2()
check_type_3()
check_type_4()
check_type_5()

print(answer)
