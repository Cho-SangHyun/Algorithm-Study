import sys
input = sys.stdin.readline


def get_leader(leaders, n):
    if leaders[n] != n:
        leaders[n] = get_leader(leaders, leaders[n])
    return leaders[n]


def union_leader(leaders, x, y):
    leader_x, leader_y = get_leader(leaders, x), get_leader(leaders, y)
    if leader_x < leader_y:
        leaders[leader_y] = leader_x
    elif leader_x > leader_y:
        leaders[leader_x] = leader_y


def solution(n, edge_info, cities):
    for i in range(len(cities)):
        cities[i] -= 1

    leaders = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if edge_info[i][j]:
                union_leader(leaders, i, j)

    for i in range(len(cities) - 1):
        if get_leader(leaders, cities[i]) != get_leader(leaders, cities[i + 1]):
            return "NO"

    return "YES"


N = int(input())
M = int(input())

edge = [list(map(int, input().split())) for _ in range(N)]
_cities = list(map(int, input().split()))

print(solution(N, edge, _cities))
