import sys
input = sys.stdin.readline

n = int(input())
board = [[]]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    board.append(row)

count = [0, 0]


def is_same(r, c, length):
    pivot = board[r][c]
    for i in range(r, r + length):
        for j in range(c, c + length):
            if pivot != board[i][j]:
                return False
    return True


def calculate(r, c, length):
    if is_same(r, c, length):
        count[board[r][c]] += 1
        return
    calculate(r, c, length // 2)
    calculate(r, c + length // 2, length // 2)
    calculate(r + length // 2, c, length // 2)
    calculate(r + length // 2, c + length // 2, length // 2)


calculate(1, 1, n)
print(count[0])
print(count[1])
