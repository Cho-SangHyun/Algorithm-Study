from collections import deque
import sys
input = sys.stdin.readline


def solution(n, k, x, edge):
    graph = [[] for _ in range(n + 1)]
    for s, e in edge:
        graph[s].append(e)

    q = deque([(x, 0)])
    visited = set([x])
    distance = [-1 for _ in range(n + 1)]
    distance[x] = 0

    while q:
        now, dist = q.popleft()
        for c_node in graph[now]:
            if c_node not in visited:
                visited.add(c_node)
                q.append((c_node, dist + 1))
                distance[c_node] = dist + 1

    answer = []
    for i in range(1, n + 1):
        if distance[i] == k:
            answer.append(i)

    answer.sort()
    return answer





N, M, K, X = map(int, input().split())
E = []
for _ in range(M):
    E.append(list(map(int, input().split())))

answers = solution(N, K, X, E)
if not answers:
    print(-1)
    exit()
for answer in answers:
    print(answer)
