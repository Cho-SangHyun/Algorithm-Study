import heapq
import sys

INF = 987654321
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

distance = [INF for _ in range(v + 1)]
distance[start] = 0

q = []
heapq.heappush(q, (0, start))

while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue
    for c_node, c_dist in graph[node]:
        new_dist = dist + c_dist
        if new_dist < distance[c_node]:
            distance[c_node] = new_dist
            heapq.heappush(q, (new_dist, c_node))

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
        continue
    print(distance[i])
