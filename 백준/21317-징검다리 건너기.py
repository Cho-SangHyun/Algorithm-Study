# 징검다리 건너기
# N개의 돌이 주어지고 1번째 돌에서 시작, N번째 돌까지 이동해야 함
# 각 돌로 가는 방법은 작은 점프, 큰 점프, 매우 큰점프가 있다, 매우 큰점프는 전체에서 1회만 사용 가능
# N번째 돌까지 가는 경우 중 에너지를 제일 조금 쓰는 경우는 언제인고?

# 1. 무식한 접근
# N번째 돌로 가는 모든 경우를 조사, 최솟값 찾기

# 2. 부분문제로 쪼개기 가능?
# Yes. N번째 돌로 오는 경우는 N - 1번째 돌까지 오고 작은 점프하거나
# N - 2번째 돌까지 오고 큰 점프하거나
# N - 3번째 돌까지 오고 매우 큰 점프하거나
# 등으로 쪼개기 가능

# 3. 중복되는 구조 O?
# Yes

import sys

input = sys.stdin.readline

N = int(input())
# little_jump[i] = i번째 돌로 작은점프로 갈 때 드는 에너지
# big_jump[i] = i번째 돌로 큰점프로 갈 때 드는 에너지
little_jump, big_jump = [0 for _ in range(23)], [0 for _ in range(23)]

for i in range(1, N):
    little_jump[i + 1], big_jump[i + 2] = map(int, input().split())

k = int(input())
# dp1[i] : i번째 돌까지 오는데 매우 큰 점프 없이 오는 방법 중 최소값
# dp2[i] : i번째 돌까지 오는데 매우 큰 점프 써서 오는 방법 중 최소값
dp1 = [0 for _ in range(23)]
dp2 = [0 for _ in range(23)]

dp1[2] = little_jump[2]
dp1[3] = min(dp1[2] + little_jump[3], big_jump[3])
dp1[4] = min(dp1[3] + little_jump[4], dp1[2] + big_jump[4])
dp1[5] = min(dp1[4] + little_jump[5], dp1[3] + big_jump[5])

dp2[4] = k
dp2[5] = min(dp2[4] + little_jump[5], dp1[2] + k)

for i in range(6, 23):
    dp1[i] = min(dp1[i - 1] + little_jump[i], dp1[i - 2] + big_jump[i])
    dp2[i] = min(dp1[i - 3] + k, dp2[i - 1] + little_jump[i], dp2[i - 2] + big_jump[i])

if N <= 3:
    print(dp1[N])
else:
    print(min(dp1[N], dp2[N]))
