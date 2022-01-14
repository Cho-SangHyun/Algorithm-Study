# M개의 문자열들과 N개의 문자열(S)들이 주어진다
# M개의 문자열들 중 S에 있는 애들의 수?

# 1. 단순히 배열에 넣어서 하기
# ==의 시간복잡도는 O(n)이므로 최악의 경우
# 10,000 * 10,000 * 500번의 연산 -> 시간초과

# 2. 배열 말고 딕셔너리로 한다면?
# in을 활용하면 시간복잡도가 O(1)으로 줄어드므로 시간단축이 가능할 것 같다

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for _ in range(N):
    dict[input()] = ''

count = 0

for _ in range(M):
    keyword = input()
    if keyword in dict:
        count += 1

print(count)