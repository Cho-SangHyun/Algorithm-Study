# 백준 1167 - 트리의 지름(https://www.acmicpc.net/problem/1260)


import sys
sys.setrecursionlimit(10**6) # RecursionError 방지

V = int(sys.stdin.readline())
Tree = [[] for i in range(V + 1)]

for i in range(V):
    c = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(c) - 1, 2):
        Tree[c[0]].append([c[j], c[j + 1]])  # 각 노드에 연결된 노드와 간선의 길이 표현


def DFS(Tree, start_node, distance):
    for node, dis in Tree[start_node]:
        if not distance[node]:               # node까지 가는 거리가 0이라면 (기록되지 않았다면)
            distance[node] = distance[start_node] + dis  # node까지 가는 거리 기록
            DFS(Tree, node, distance)

distance = [0 for i in range(V + 1)]
DFS(Tree, 1, distance)
distance[1] = 0                           # distance는 start_node에서 각 노드까지의 거리를 저장하는 리스트이므로, 자기 자신에서 출발해 자기 자신까지의 거리는 0으로 해야 함.

start_node, max_distance = -1, -1

for i in range(1, V + 1):
    if distance[i] > max_distance:
        max_distance = distance[i]
        start_node = i

distance = [0 for i in range(V + 1)]
DFS(Tree, start_node, distance)
distance[start_node] = 0                  # distance는 start_node에서 각 노드까지의 거리를 저장하는 리스트이므로, 자기 자신에서 출발해 자기 자신까지의 거리는 0으로 해야 함.
print(max(distance))
