from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


def is_connected(_group, graph):
    group = list(_group)
    visited = set()

    q = deque([group[0]])
    visited.add(group[0])

    while q:
        node = q.popleft()
        for c_node in graph[node]:
            if c_node in _group and c_node not in visited:
                visited.add(c_node)
                q.append(c_node)

    for node in group:
        if node not in visited:
            return False
    return True


N = int(input())
peoples = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
answer = 987654321

for i in range(1, N + 1):
    info = list(map(int, input().split()))
    for j in range(1, len(info)):
        graph[i].append(info[j])

for k in range(1, N // 2 + 1):
    for comb in combinations(list(range(1, N + 1)), k):
        group_a = set(comb)
        group_b = set(range(1, N + 1)) - group_a
        if is_connected(group_a, graph) and is_connected(group_b, graph):
            group_a_people, group_b_people = 0, 0
            for i in group_a:
                group_a_people += peoples[i]
            for i in group_b:
                group_b_people += peoples[i]
            answer = min(answer, abs(group_b_people - group_a_people))

print(answer if answer != 987654321 else -1)
