import sys
import heapq
input = sys.stdin.readline


def solution(n, m, r, items, edge_info):
    graph = [[] for _ in range(n)]

    for a, b, dist in edge_info:
        graph[a - 1].append((b - 1, dist))
        graph[b - 1].append((a - 1, dist))

    answer = 0

    for start in range(n):
        distance = [987654321 for _ in range(n)]
        distance[start] = 0
        q = [(0, start)]
        mid_answer = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for c_node, c_dist in graph[now]:
                if dist + c_dist < distance[c_node]:
                    distance[c_node] = dist + c_dist
                    heapq.heappush(q, (distance[c_node], c_node))

        for i in range(n):
            if distance[i] <= m:
                mid_answer += items[i]

        answer = max(answer, mid_answer)

    return answer


N, M, R = map(int, input().split())
_items = list(map(int, input().split()))
_edge_info = [list(map(int, input().split())) for _ in range(R)]

print(solution(N, M, R, _items, _edge_info))
