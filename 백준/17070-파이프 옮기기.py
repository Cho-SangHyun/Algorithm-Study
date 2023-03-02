import sys
input = sys.stdin.readline


def solution(n, board):
    dp = [[[0, 0, 0] for i in range(n)] for j in range(n)]
    # dp[1][1][0] = 1, 1로 오는 방법의 수인데 가로로 온 방법의 수.
    #                     dp[r][c - 1][0] + dp[r][c - 1][2]
    # dp[1][1][1] = 1, 1로 오는 방법의 수인데 세로로 온 방법의 수.
    #                     dp[r - 1][c][1] + dp[r - 1][c][2]
    # dp[1][1][2] = 1, 1로 오는 방법의 수인데 대각으로 온 방법의 수.
    #                     dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]

    for c in range(1, n):
        if board[0][c] == 1:
            break
        dp[0][c][0] = 1

    for r in range(1, n):
        for c in range(n):
            if not board[r][c]:
                if c != 0:
                    dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]
                    if not board[r - 1][c - 1] and not board[r - 1][c] and not board[r][c - 1]:
                        dp[r][c][2] = dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]
                if not board[r - 1][c]:
                    dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]

    return sum(dp[n - 1][n - 1])


N = int(input())
_board = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, _board))
