import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# dp[r][c]를 계산하고 세팅해주는 함수
def dfs(maps, dp, r, c, n):
    global directions

    if not dp[r][c]:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 1 or nc < 1 or nr > n or nc > n:
                continue
            if maps[nr][nc] > maps[r][c]:
                dp[r][c] = max(dp[r][c], 1 + dfs(maps, dp, nr, nc, n))
            else:
                dp[r][c] = max(dp[r][c], 1)
    return dp[r][c]


def solution(n, maps):
    global directions

    for i in range(n):
        maps[i] = [0] + maps[i]
    maps = [[]] + maps

    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dfs(maps, dp, i, j, n)

    answer = 0
    for row in dp:
        answer = max(answer, max(row))
    return answer


N = int(input())
_maps = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, _maps))
