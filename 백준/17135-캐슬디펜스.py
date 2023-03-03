from itertools import combinations
import sys
input = sys.stdin.readline


def solution(n, m, d, maps):
    possible_locations = list(range(m))
    answer = 0

    for comb in combinations(possible_locations, 3):
        enemy = []
        for r in range(n):
            for c in range(m):
                if maps[r][c]:
                    enemy.append((r, c))

        arrow_location = list(comb)
        removed = 0

        while enemy:
            remove_target = set()
            for arrow in arrow_location:
                target = (0, 0)
                target_dist = 987654321
                for r, c in enemy:
                    dist = abs(n - r) + abs(arrow - c)
                    if dist <= d and dist < target_dist:
                        target_dist = dist
                        target = (r, c)
                    elif dist <= d and dist == target_dist and c < target[1]:
                        target = (r, c)
                if target_dist < 987654321:
                    remove_target.add(target)
            removed += len(remove_target)
            enemy = [location for location in enemy if location not in remove_target]
            enemy = [(r + 1, c) for r, c in enemy if r + 1 != n]
        answer = max(answer, removed)
    return answer


N, M, D = map(int, input().split())
_maps = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, M, D, _maps))
