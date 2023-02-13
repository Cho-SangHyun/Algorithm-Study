import sys
import heapq

INF = 987654321
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

v1, v2 = map(int, input().split())

answer1 = []
answer2 = []

distance = [INF for _ in range(n + 1)]
distance[1] = 0

q = []
heapq.heappush(q, (0, 1))

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for c_node, i in graph[now]:
        new_dist = dist + i
        if new_dist < distance[c_node]:
            distance[c_node] = new_dist
            heapq.heappush(q, (new_dist, c_node))

answer1.append(distance[v1])
answer2.append(distance[v2])

distance = [INF for _ in range(n + 1)]
distance[v1] = 0
heapq.heappush(q, (0, v1))

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for c_node, i in graph[now]:
        new_dist = dist + i
        if new_dist < distance[c_node]:
            distance[c_node] = new_dist
            heapq.heappush(q, (new_dist, c_node))

answer1.append(distance[v2])
answer2.append(distance[n])

distance = [INF for _ in range(n + 1)]
distance[v2] = 0
heapq.heappush(q, (0, v2))

while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for c_node, i in graph[now]:
        new_dist = dist + i
        if new_dist < distance[c_node]:
            distance[c_node] = new_dist
            heapq.heappush(q, (new_dist, c_node))


answer1.append(distance[n])
answer2.append(distance[v1])

if INF in answer1 or INF in answer2:
    print(-1)
    exit()
answer = min(sum(answer1), sum(answer2))
print(answer)
