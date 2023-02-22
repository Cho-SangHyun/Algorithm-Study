import sys
input = sys.stdin.readline


def solution(n, m, data):
    data.sort()
    answer = 0

    i, j = 1, n

    while i < j:
        res = data[i] + data[j]
        if res == m:
            answer += 1
            if data[i] == data[i + 1]:
                i += 1
            else:
                j -= 1
        elif res < m:
            i += 1
        elif res > m:
            j -= 1

    return answer


N = int(input())
M = int(input())
costs = [0] + list(map(int, input().split()))

print(solution(N, M, costs))
