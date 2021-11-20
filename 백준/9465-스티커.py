"""
RGB거리 문제랑 유사해서 비슷한 방법으로 풀었다. 

1번 열부터 스티커를 뽑는다고 할 때,
N번째 열에서 위쪽스티커를 골랐을 때의 최대값 = N - 1번째 열에서 아래쪽을 골랐을 때의 최대와 
                                N - 2번째 열까지의 최대 중 더 큰 값 + N번째 열에서 위쪽스티커의 값
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
sticker배열은 이 풀이에선
[
    [0],
    [100, 200, 300, 400, 500],  # 1번째 줄(행) 스티커들의 값
    [121, 212, 411, 123, 345]   # 2번째 줄(행) 스티커들의 값
]
와 같은 모양이다. 따라서 sticker[i][j]는 스티커들의 표현에 있어서 i행 j열 스티커처럼 행->열 순서로
접근하지만 dp배열은 
[
    [-1, 0, 0],
    [-1, V1, V2],         # 1번째 열의 스티커를 뽑았을 때의 최대값 
    [-1, V3, V4]          # 2번째 열의 스티커를 뽑았을 때의 최대값
                          # ex) dp[2][1] = 2번째 열의 1번째 행의 스티커를 뽑았을 때의 최대값  
]
와 같은 모양으로, dp[i][j]가 스티커들에 대해 열->행 순서로 접근하는 식으로 만드는 바람에 많이 헷갈렸다.
통일시킬 필요가 있을 듯 하다.

dp배열을
dp = [[0 for i in range(n + 1)] for j in range(3)] 으로 하고 했으면
통일성있게 접근할 수 있었을 것 같다.

아니면, 애시당초 입력받을 때 잘 조작을 해서
sticker = [
    [0, 0, 0]
    [0, 100, 200],  # 1번째 행의 스티커
    [0, 200, 212],  # 2번째 행의 스티커
]
처럼 했으면 됐을 것 같다 

↓↓↓
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    sticker = [[0]]
    sticker.append([0] + list(map(int, sys.stdin.readline().split())))
    sticker.append([0] + list(map(int, sys.stdin.readline().split())))

    dp = [[0 for i in range(n + 1)] for j in range(3)]
    dp[1][1] = sticker[1][1]
    dp[2][1] = sticker[2][1]

    for i in range(2, n + 1):
        dp[1][i] = max(dp[2][i - 1], max(dp[1][i - 2], dp[2][i - 2])) + sticker[1][i]
        dp[2][i] = max(dp[1][i - 1], max(dp[1][i - 2], dp[2][i - 2])) + sticker[2][i]

    print(max(dp[1][n], dp[2][n]))

"""