import sys
input = sys.stdin.readline


def solution(n, locations):
    locations.sort()
    if n % 2 == 1:
        return locations[n // 2]

    n1, n2 = n // 2, n // 2 - 1
    a1, a2 = 0, 0
    for i in range(n):
        if i != n1:
            a1 += abs(locations[i] - locations[n1])
        if i != n2:
            a2 += abs(locations[i] - locations[n2])

    if a1 >= a2:
        return locations[n2]
    return locations[n1]


N = int(input())
L = list(map(int, input().split()))

print(solution(N, L))
