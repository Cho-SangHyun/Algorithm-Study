import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra_go_x(start, x):
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for c_node, i in graph[now]:
            new_dist = dist + i
            if new_dist < distance[c_node]:
                distance[c_node] = new_dist
                heapq.heappush(q, (new_dist, c_node))

    return distance[x]


def dijkstra_come_from_x(x):
    distance = [INF for _ in range(n + 1)]
    distance[x] = 0
    q = []
    heapq.heappush(q, (0, x))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for c_node, i in graph[now]:
            new_dist = dist + i
            if new_dist < distance[c_node]:
                distance[c_node] = new_dist
                heapq.heappush(q, (new_dist, c_node))

    return distance


dists = [0]
for i in range(1, n + 1):
    dists.append(dijkstra_go_x(i, x))

come_dists = dijkstra_come_from_x(x)
for i in range(1, n + 1):
    dists[i] += come_dists[i]

print(max(dists))
