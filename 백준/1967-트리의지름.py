import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

leaf_node = 1
distance_to_leaf = -1


def dfs(node, weight_sum, graph, visited):
    global leaf_node
    global distance_to_leaf

    for c_node, c_weight in graph[node]:
        if c_node not in visited:
            visited.add(c_node)
            dfs(c_node, weight_sum + c_weight, graph, visited)

    if distance_to_leaf < weight_sum:
        leaf_node = node
        distance_to_leaf = weight_sum


def solution(n, edges):
    global distance_to_leaf

    graph = [[] for _ in range(n + 1)]
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))

    visited = set([1])
    dfs(1, 0, graph, visited)

    distance_to_leaf = -1
    visited = set([leaf_node])
    dfs(leaf_node, 0, graph, visited)

    answer = distance_to_leaf
    return answer


N = int(input())
E = []
for _ in range(N - 1):
    E.append(list(map(int, input().split())))

print(solution(N, E))
