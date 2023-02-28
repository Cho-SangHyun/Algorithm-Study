from itertools import combinations
import sys
input = sys.stdin.readline


def match(n, h, sadari):
    for i in range(1, n + 1):
        sero = i
        j = 1
        while j <= h:
            if sadari[sero][j]:
                sero = sadari[sero][j]
            j += 1
        if sero != i:
            return False
    else:
        return True


def solution(n, m, h, info):
    sadari = [[0 for i in range(h + 1)] for j in range(n + 1)]
    for a, b in info:
        sadari[b][a] = b + 1
        sadari[b + 1][a] = b

    new_infos = []
    for i in range(1, n):
        for j in range(1, h + 1):
            if not sadari[i][j] and not sadari[i + 1][j]:
                new_infos.append((j, i))

    for answer in range(4):
        for picked_info in combinations(new_infos, answer):
            for a, b in picked_info:
                if sadari[b][a] or sadari[b + 1][a]:
                    break
                sadari[b][a] = b + 1
                sadari[b + 1][a] = b
            else:
                if match(n, h, sadari):
                    return answer

            for a, b in picked_info:
                sadari[b][a] = 0
                sadari[b + 1][a] = 0

    return -1


N, M, H = map(int, input().split())
_info = []
for _ in range(M):
    _info.append(list(map(int, input().split())))

print(solution(N, M, H, _info))
