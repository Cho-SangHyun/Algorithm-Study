import sys

input = sys.stdin.readline
N = int(input())
board = [[0 for i in range(101)] for j in range(101)]

for _ in range(N):
    c, r = map(int, input().split())
    for i in range(r + 1, r + 11):
        for j in range(c + 1, c + 11):
            board[i][j] = 1

answer = 0
for i in range(1, 101):
    for j in range(1, 101):
        if board[i][j]:
            answer += 1

print(answer)
