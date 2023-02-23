import sys
input = sys.stdin.readline
directions = [(0, 1), (1, 0), (1, 1)]

N, M = map(int, input().split())
board = [[]]
for _ in range(N):
    board.append([0] + list(map(int, input().split())))

dp = [[-1 for i in range(M + 1)] for j in range(N + 1)]
dp[1][1] = board[1][1]

for i in range(2, M + 1):
    dp[1][i] = board[1][i] + dp[1][i - 1]

for i in range(2, N + 1):
    for j in range(1, M + 1):
        if j == 1:
            dp[i][j] = dp[i - 1][j] + board[i][j]
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + board[i][j]

print(dp[N][M])
