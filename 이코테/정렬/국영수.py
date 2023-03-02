import sys
input = sys.stdin.readline


def solution(data):
    data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    return data


N = int(input())
score = []
for _ in range(N):
    name, a, b, c = map(str, input().split())
    a, b, c = map(int, [a, b, c])
    score.append([name, a, b, c])

sorted_score = solution(score)
for s in sorted_score:
    print(s[0])
