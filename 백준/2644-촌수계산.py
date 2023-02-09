import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

a, b = map(int, input().split())

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = set()
visited.add(a)
stack = [(a, 0)]

while stack:
    node, step = stack.pop()
    if node == b:
        print(step)
        exit()
    for connected_node in graph[node]:
        if connected_node not in visited:
            visited.add(connected_node)
            stack.append((connected_node, step + 1))

print(-1)
