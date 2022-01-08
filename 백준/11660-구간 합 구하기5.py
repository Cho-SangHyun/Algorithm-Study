# 11660 - 주어진 정사각형 꼴 표에서 (x1, y1)부터 (x2, y2)까지의 합 구하기
# x1 <= x2, y1 <= y2로 주어진다.
# N은 최대 24, 구해야할 횟수 M은 최대 10만

# 1. 무식하게 접근
# M번의 트라이에 대해 그 때 그 때마다 반복문돌며 처리
# 최악의 경우 100,000 * 1024 * 1024번의 연산
# 시간 내 통과불가

# 2. M번의 트라이에 대해 중복되는 구조 찾기?
# 애매~하다. M번의 트라이 중에 중복될 확률이 몇이나 될지
# 또한 전의 결과를 쓸 수 있다고 해도 전의 결과를 저장하려면 4개의 좌표값이 필요한데
# 이에 대응하는 배열을 만드려면 1024 * 1024 * 1024 * 1024 개의 값을 담을 수 있는
# 배열을 만들어야 하는데 메모리 초과가 난다.

# 3. 누적합을 이용해보자
# (x1, y1)부터 (x2, y2)까지의 누적합
# = (0, 0)부터 (x2, y2)까지의 누적합
# - (0, 0)부터 (x2, y1 - 1)까지의 누적합
# - (0, y2)부터 (x1 - 1, y2)까지의 누적합

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dp = [[0 for i in range(N + 1)] for j in range(N + 1)]

for r in range(1, N + 1):
    new_line = [0] + list(map(int, input().split()))
    accumalated_sum = 0
    for c in range(1, N + 1):
        accumalated_sum += new_line[c]
        dp[r][c] = dp[r - 1][c] + accumalated_sum

for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    answer = (
        dp[r2][c2] -
        dp[r1 - 1][c2] -
        (dp[r2][c1 - 1] - dp[r1 - 1][c1 - 1])
    )
    print(answer)

