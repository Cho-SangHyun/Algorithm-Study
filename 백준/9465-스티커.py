"""
무식하게 풀기 : 
각 열에서 최대 1개씩 고를 수 있음. 뽑을 수 있는 스티커는 최대 n개, 

N번째 열에서 Up스티커를 골랐을 때의 최대값 = N - 1번째 열에서 Down을 골랐을 때의 최대와 N - 2번째 열까지의 최대 중 더 큰 값 + N번째 열에서 UP
"""

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    sticker = [[0]]
    sticker.append([0] + list(map(int, sys.stdin.readline().split())))
    sticker.append([0] + list(map(int, sys.stdin.readline().split())))

    dp = [[-1, 0, 0], [-1, sticker[1][1], sticker[2][1]]]
    # dp[n][1] = 1번째 ~ n번째 열까지 스티커 뽑을 때, n번째 열에서 1번째 행의 스티커 뽑을 때 최대
    # dp[n][2] = 1번째 ~ n번째 열까지 스티커 뽑을 때, n번째 열에서 2번째 행의 스티커 뽑을 때 최대

    for i in range(2, n + 1):
        dp.append([
            -1,
            max(dp[i - 1][2], max(dp[i - 2])) + sticker[1][i],
            max(dp[i - 1][1], max(dp[i - 2])) + sticker[2][i]
        ])

    print(max(dp[n]))

"""
sticke
"""
