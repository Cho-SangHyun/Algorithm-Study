import sys
input = sys.stdin.readline


def solution(n, data):
    answer = 0
    count = [0 for _ in range(n + 1)]

    for num in data:
        count[num] += 1

    group = []
    for i in range(1, n + 1):
        if count[i]:
            group.append((i, count[i]))
    group.sort()

    rest = 0
    for g in group:
        rest += g[1] % g[0]
        if g[0] <= g[1]:
            answer += g[1] // g[0]
        if g[0] <= rest:
            answer += rest // g[0]
            rest = rest % g[0]

    return answer


N = int(input())
nums = list(map(int, input().split()))

print(solution(N, nums))
