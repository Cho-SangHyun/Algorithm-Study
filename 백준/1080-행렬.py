import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [list(map(int, input().strip())) for _ in range(n)]
B = [list(map(int, input().strip())) for _ in range(n)]

if (n < 3 or m < 3) and A != B:
    print(-1)
    exit()


def is_match_row(row):
    if A[row] != B[row]:
        return False
    return True


def flip(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            A[i][j] = 1 - A[i][j]


answer = 0
for r in range(n - 2):
    for c in range(m - 2):
        if A[r][c] != B[r][c]:
            answer += 1
            flip(r, c)
    if not is_match_row(r):
        print(-1)
        exit()

if is_match_row(n - 2) and is_match_row(n - 1):
    print(answer)
else:
    print(-1)
