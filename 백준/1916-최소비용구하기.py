import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, target, cost = map(int, input().split())
    graph[start].append((target, cost))

s, e = map(int, input().split())

cost = [INF for _ in range(n + 1)]
cost[s] = 0
q = []
heapq.heappush(q, (0, s))

while q:
    pay, now = heapq.heappop(q)
    if cost[now] < pay:
        continue
    for c_node, c_pay in graph[now]:
        new_cost = pay + c_pay
        if new_cost < cost[c_node]:
            cost[c_node] = new_cost
            heapq.heappush(q, (new_cost, c_node))

print(cost[e])
