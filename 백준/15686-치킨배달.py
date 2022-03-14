from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pos_chicken, pos_house = [], []
# 치킨집, 일반 집들의 위치를 따로 따로 저장
for r in range(N):
    row = list(map(int, input().split()))

    for c in range(N):
        if row[c] == 1:
            pos_house.append([r, c])
        elif row[c] == 2:
            pos_chicken.append([r, c])

answer = []
# 치킨 집을 1개 ~ M개 남길 때의 상황들에 대해 순회
# 0개부터 순회하는 건 모순(그림 치킨가게가 아예 없게 됨)
for m in range(1, M + 1):
    survived_chicken = list(combinations(pos_chicken, m))
    
    for chickens in survived_chicken:
        # 도시의 치킨거리
        city_chicken_length = 0

        for house in pos_house:
            # 특정 집에서부터의 치킨 거리
            house_chicken_length = 987654321
            for store in chickens:
                # 치킨 거리 중 가장 짧은 값을 취함
                house_chicken_length = min(house_chicken_length, 
                    abs(store[0] - house[0]) + abs(store[1] - house[1]))
            # 도시의 치킨거리에 이 집으로부터의 치킨 거리를 더함
            city_chicken_length += house_chicken_length
        # 이 조합(살아남은 치킨 가게들)에 대한 도시의 치킨 거리를 정답후보로 추가
        answer.append(city_chicken_length)
# 가장 짧은 치킨 거리 출력
print(min(answer))


# 치킨집들 중 M개의 치킨집을 고르고, 각 집으로부터 살아남은 치킨집들에 대한 거리를 하나하나 계산

# 치킨집은 최대 13개 주어지고 M도 최대 13이므로 치킨집들 중 M개의 치킨집을 고르는 최악의 경우 = 2^13 = 10000개 정도의 경우
# 최대 집 개수인 2N = 100개로부터 최대 M개 = 13개의 치킨집에 대한 거리를 구하는 것 = 100 * 13번 = 1300번 연산
# 10000 * 1300 = 13,000,000 -> 시간 내에 통과할 수 있을 것 같다.

