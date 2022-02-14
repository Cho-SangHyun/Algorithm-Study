import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

E = int(input())

graph = [[] for i in range(101)]

for _ in range(E):
    st, ed = map(int, input().split())
    graph[st].append(ed)
    graph[ed].append(st)

visited = [0 for _ in range(101)]

q = deque([1])

while q:
    node = q.popleft()
    if not visited[node]:
        visited[node] = 1
        for c_node in graph[node]:
            if not visited[c_node]:
                q.append(c_node)

print(sum(visited) - 1)
