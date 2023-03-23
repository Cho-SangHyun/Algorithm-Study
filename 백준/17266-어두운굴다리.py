import sys
input = sys.stdin.readline


def solution(n, m, locations):
    left, right = locations[0], n
    answer = -1

    while left <= right:
        height = (left + right) // 2
        s, e = 0, locations[0] + height
        for i in range(1, m):
            ns, ne = max(0, locations[i] - height), min(n, locations[i] + height)
            if ns > e:
                left = height + 1
                break
            else:
                e = ne
        else:
            if e < n:
                left = height + 1
            else:
                answer = height
                right = height - 1
    return answer


N = int(input())
M = int(input())
L = list(map(int, input().split()))

print(solution(N, M, L))
