import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

a, b = map(int, input().split())

distance = [INF for _ in range(n + 1)]
distance[a] = 0
shortest_path = []
q = []
heapq.heappush(q, (0, a, [a]))

while q:
    dist, now, path = heapq.heappop(q)
    if now == b:
        print(distance[now])
        print(len(path))
        for p in path:
            print(p, end=' ')
        exit()
    if distance[now] < dist:
        continue
    for c_node, c_dist in graph[now]:
        if dist + c_dist < distance[c_node]:
            distance[c_node] = dist + c_dist
            new_path = path + [c_node]
            heapq.heappush(q, (distance[c_node], c_node, new_path))
