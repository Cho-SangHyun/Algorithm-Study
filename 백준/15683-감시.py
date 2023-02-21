import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = [[]]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

cctv_s = []

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if 0 < board[i][j] < 6:
            cctv_s.append((i, j, board[i][j]))


answer = 987654321


def solution(index):
    global cctv_s
    global answer

    if index == len(cctv_s):
        count = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if board[i][j] == 0:
                    count += 1
        answer = min(answer, count)
        return

    r, c, num = cctv_s[index]

    if num == 1:
        # 위쪽
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        solution(index + 1)
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1
        # 오른쪽
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        solution(index + 1)
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        # 아래쪽
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        solution(index + 1)
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1
        # 왼쪽
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        solution(index + 1)
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1

    elif num == 2:
        # 가로
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        solution(index + 1)
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        # 세로
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        solution(index + 1)
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1

    elif num == 3:
        # 위, 오른쪽
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        solution(index + 1)
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1
        # 오른쪽, 아래
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        solution(index + 1)
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        # 아래, 왼쪽
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        solution(index + 1)
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1
        # 왼쪽, 위
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        solution(index + 1)
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1

    elif num == 4:
        # 왼, 위, 오
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        solution(index + 1)
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        # 위, 오, 아
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        solution(index + 1)
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1
        # 오, 아, 왼
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        solution(index + 1)
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        # 아, 왼, 위
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        solution(index + 1)
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1

    elif num == 5:
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] -= 1
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] -= 1
        solution(index + 1)
        for nc in range(c + 1, m + 1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        for nc in range(c - 1, 0, -1):
            if board[r][nc] == 6:
                break
            if board[r][nc] > 0:
                continue
            board[r][nc] += 1
        for nr in range(r - 1, 0, -1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1
        for nr in range(r + 1, n + 1):
            if board[nr][c] == 6:
                break
            if board[nr][c] > 0:
                continue
            board[nr][c] += 1


solution(0)
print(answer)
