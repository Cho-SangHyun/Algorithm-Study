import sys
input = sys.stdin.readline


def check_path(path, k):
    length = len(path)
    check = [0 for _ in range(length)]

    for i in range(length - 1):
        if abs(path[i] - path[i + 1]) > 1:
            return False
        if path[i] + 1 == path[i + 1]:
            for j in range(i, i - k, -1):
                if j < 0 or check[j] or path[j] != path[i]:
                    return False
                check[j] = 1
            continue
        if path[i] == path[i + 1] + 1:
            for j in range(i + 1, i + 1 + k):
                if j >= length or check[j] or path[j] != path[i + 1]:
                    return False
                check[j] = 1
    return True


def solution(n, k, board):
    answer = 0

    for row in board:
        if check_path(row, k):
            answer += 1

    for c in range(n):
        if check_path([board[i][c] for i in range(n)], k):
            answer += 1

    return answer


N, L = map(int, input().split())
_board = []
for _ in range(N):
    _board.append(list(map(int, input().split())))

print(solution(N, L, _board))
