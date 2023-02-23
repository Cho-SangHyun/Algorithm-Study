import sys
input = sys.stdin.readline


def solution(n, board):
    dp = [[0 for i in range(n)] for j in range(n)]
    dp[0][0] = 1

    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                break
            nr = r + board[r][c]
            nc = c + board[r][c]
            if nr < n:
                dp[nr][c] += dp[r][c]
            if nc < n:
                dp[r][nc] += dp[r][c]

    return dp[n - 1][n - 1]


N = int(input())
game_board =[]
for _ in range(N):
    game_board.append(list(map(int, input().split())))

print(solution(N, game_board))
