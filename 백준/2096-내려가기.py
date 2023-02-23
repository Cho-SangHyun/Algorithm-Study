import sys
input = sys.stdin.readline


def solution(n, data):
    dp = [0, 0, 0]
    dp[0], dp[1], dp[2] = data[0][0], data[0][1], data[0][2]

    for i in range(1, n):
        new_dp = [0, 0, 0]
        new_dp[0] = data[i][0] + max(dp[0], dp[1])
        new_dp[1] = data[i][1] + max(dp[0], dp[1], dp[2])
        new_dp[2] = data[i][2] + max(dp[2], dp[1])
        dp = new_dp

    max_answer = max(dp)

    dp = [0, 0, 0]
    dp[0], dp[1], dp[2] = data[0][0], data[0][1], data[0][2]

    for i in range(1, n):
        new_dp = [0, 0, 0]
        new_dp[0] = data[i][0] + min(dp[0], dp[1])
        new_dp[1] = data[i][1] + min(dp[0], dp[1], dp[2])
        new_dp[2] = data[i][2] + min(dp[2], dp[1])
        dp = new_dp

    min_answer = min(dp)

    print(max_answer, min_answer)


N = int(input())
DATA = []
for _ in range(N):
    DATA.append(list(map(int, input().split())))

solution(N, DATA)
