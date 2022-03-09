from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

chicken, house = [], []
# 치킨집, 일반집들의 좌표를 따로 따로 저장
for r in range(N):
    row = list(map(int, input().split()))

    for c in range(N):
        if row[c] == 1:
            house.append([r, c])
        elif row[c] == 2:
            chicken.append([r, c])

anses = []
# 치킨 집을 1개 ~ M개 남길 때의 상황들에 대해 순회
for m in range(1, M + 1):
    survived_chicken = list(combinations(chicken, m))
    
    for comb in survived_chicken:
        ans = 0
        for H in house:
            # 특정 집에서부터의 치킨 거리
            chicken_diameter = 987654321
            for C in comb:
                chicken_diameter = min(chicken_diameter, abs(C[0] - H[0]) + abs(C[1] - H[1]))
            ans += chicken_diameter
        anses.append(ans)

print(min(anses))
