import sys
from itertools import combinations
from collections import deque
import copy

input = sys.stdin.readline

field = [[0, 0, 0, 0, 0, 0, 0, 0]]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())

areas, virus = [], []

for r in range(1, N + 1):
    field.append([0] + list(map(int, input().split())))
    for c in range(1, M + 1):
        if field[r][c] == 0:
            areas.append([r, c])
        elif field[r][c] == 2:
            virus.append([r, c])

test_field = copy.deepcopy(field)

new_walls = list(combinations(areas, 3))

def bfs():
    q = deque(virus)
    ret = 0

    while q:
        nd = q.popleft()
        r, c = nd
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 1 <= nr and nr <= N and 1 <= nc and nc <= M and test_field[nr][nc] == 0:
                test_field[nr][nc] = 2
                q.append([nr, nc])
    
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if test_field[i][j] == 0:
                ret += 1
    
    return ret

ans = []

for nw in new_walls:
    for cd in nw:
        test_field[cd[0]][cd[1]] = 1

    ans.append(bfs())

    test_field = copy.deepcopy(field)


print(max(ans))