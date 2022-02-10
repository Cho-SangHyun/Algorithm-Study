# 백트래킹으로 해보기(가지치기)
# 시간초과 나겠지만, 그냥 이걸 구현하면 어떻게 할 수 있을까에서 시도함
# ?? 이거도 통과되네,,

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

T = int(input())

ans = 0

def solution(target, cur):
    global ans
    if target == cur:
        ans += 1

    for num in [3, 2, 1]:
        if cur + num <= target:
            solution(target, cur + num)

for _ in range(T):
    N = int(input())
    if N == 1:
        print(1)
    elif N == 2:
        print(2)
    elif N == 3:
        print(4)
    else:
        solution(N, 3)
        solution(N, 2)
        solution(N, 1)
        print(ans)
        ans = 0

