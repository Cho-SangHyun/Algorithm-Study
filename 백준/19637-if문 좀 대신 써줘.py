# 각 점수별 영역에 따라 특정 칭호가 주어질 때,
# 모든 인원의 칭호를 출력하는 문제

# 무식한 방법으로 하면 100억번 정도 연산을 하므로
# 시간을 줄여야 함.

# 이분탐색을 통해 nlogn으로 컷 가능

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data = []
already = set([])

for _ in range(N):
    title, max_value = input().split()
    if int(max_value) not in already:
        data.append([int(max_value), title])
        already.add(int(max_value))

for _ in range(M):
    value = int(input())
    st, ed = 0, len(data) - 1

    while st < ed:
        mid = (st + ed) // 2

        if data[mid][0] == value:
            ed = mid
            break
        elif data[mid][0] < value:
            st = mid + 1
        else:
            ed = mid
    
    print(data[ed][1])