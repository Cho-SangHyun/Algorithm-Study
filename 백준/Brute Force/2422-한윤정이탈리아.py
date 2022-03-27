# N개의 아이스크림이 주어진다. 같이 먹으면 노맛인 조합 M개가 주어진다.
# 3개의 아이스크림을 고를 때 노맛조합이 없는 3개가 골라지는 경우의 수 모두 구하기

# 나올 수 있는 최대 조합의 수 = 200C3 = 대략 천만개
# 첫 아이스크림에 대해 두 번째, 세 번째 아이스크림이 가능한지 보고
# 두 번째 아이스크림에 대해 세 번째 아이스크림이 가능한지 보면 된다

from itertools import combinations
import sys

input = sys.stdin.readline

N, M = map(int, (input().split()))

nono = [[1 for i in range(202)] for j in range(202)]

for _ in range(M):
    ic1, ic2 = map(int, input().split())
    nono[ic1][ic2] = 0
    nono[ic2][ic1] = 0

all_comb = combinations(list(range(1, N + 1)), 3)

answer = 0

for comb in all_comb:
    if nono[comb[0]][comb[1]] and nono[comb[0]][comb[2]] and nono[comb[1]][comb[2]]:
        answer += 1

print(answer)
