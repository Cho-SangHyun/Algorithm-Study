import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
answer = 0


def dfs(graph, visited, now):
    global answer
    if len(visited) == 5:
        answer = 1
        return
    for c_node in graph[now]:
        if c_node not in visited:
            visited.add(c_node)
            dfs(graph, visited, c_node)
            visited.remove(c_node)


def solution(n, r, edge_info):
    global answer
    graph = [[] for _ in range(n)]
    for a, b in edge_info:
        graph[a].append(b)
        graph[b].append(a)

    for node in range(n):
        visited = set([node])
        dfs(graph, visited, node)
        if answer == 1:
            return answer

    return answer


N, R = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(R)]

print(solution(N, R, E))
