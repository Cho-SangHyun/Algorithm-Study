import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())
board = [[]]
for _ in range(n):
    row = [0] + list(map(int, input().strip()))
    board.append(row)


def press(r, c, length):
    if length == 1:
        return str(board[r][c])

    press_result1 = press(r, c, length // 2)
    press_result2 = press(r, c + length // 2, length // 2)
    press_result3 = press(r + length // 2, c, length // 2)
    press_result4 = press(r + length // 2, c + length // 2, length // 2)

    if len(press_result1) == 1 and press_result1 == press_result2 and press_result1 == press_result3 and press_result1 == press_result4 and press_result2 == press_result3 and press_result2 == press_result4 and press_result3 == press_result4:
        return str(press_result1)

    return "(" + press_result1 + press_result2 + press_result3 + press_result4 + ")"


print(press(1, 1, n))
