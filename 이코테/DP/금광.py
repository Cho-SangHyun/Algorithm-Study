import sys
input = sys.stdin.readline


def solution(n, m, locations):
    board = []
    i = 0
    while i < len(locations):
        board.append(locations[i:i+m])
        i += m

    dp = [[0 for j in range(m)] for i in range(n)]
    for r in range(n):
        dp[r][0] = board[r][0]

    for c in range(1, m):
        for r in range(n):
            s = r - 1 if r > 0 else r
            e = r + 1 if r < n - 1 else r
            hoobo = [dp[i][c - 1] for i in range(s, e + 1)]
            dp[r][c] = max(hoobo) + board[r][c]

    answer = -1
    for r in range(n):
        answer = max(answer, dp[r][-1])

    return answer


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    print(solution(N, M, L))

# 1
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7