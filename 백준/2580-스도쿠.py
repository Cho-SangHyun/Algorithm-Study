import sys
sys.setrecursionlimit(10**9)

board = [[0]]
zero_index = []

for r in range(1, 10):
    line = list(map(int, sys.stdin.readline().split()))
    for c in range(9):
        if line[c] == 0: zero_index.append([r, c + 1])
    board.append([0] + line)

def printBoard():
    for r in range(1, 10):
        for c in range(1, 10):
            if c != 9:
                print(board[r][c], end=' ')
            else:
                print(board[r][c])
    exit(0)

def fillBoard(i):
    # print(i)
    if i == len(zero_index):
        printBoard()
    r, c = zero_index[i]
    possible_nums = set(range(1, 10))
    possible_nums -= set(board[r])

    ret = set([])
    for k in range(1, 10):
        ret.add(board[k][c])

    possible_nums -= (ret - set([0]))

    if r <= 3:
        r_zone = [1, 2, 3]
    elif r <= 6:
        r_zone = [4 ,5, 6]
    else:
        r_zone = [7, 8, 9]
    
    if c <= 3:
        c_zone = [1, 2, 3]
    elif c <= 6:
        c_zone = [4, 5, 6]
    else:
        c_zone = [7, 8, 9]
    
    ret2 = set([])
    for nr in r_zone:
        for nc in c_zone:
            ret2.add(board[nr][nc])

    possible_nums -= (ret2 - set([0]))

    for num in possible_nums:
        board[r][c] = num
        fillBoard(i + 1)
    board[r][c] = 0
    return

fillBoard(0)
