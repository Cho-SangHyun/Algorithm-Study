# 9372 - 상근이의 여행
# 나라의 수와 비행기 종류의 수가 주어졋을 때
# 가장 적은 종류의 비행기들로 모든 국가들을 여행할 수 있도록 하는 수

# 그래프 형태로 주어지며, 모든 노드가 연결된 형태라면 정답 : N - 1
# 끊긴 그래프 형태라면 정답 : 0
# 판별 : DFS or BFS를 돌려서 모든 노드가 방문처리되는지 확인
# 최악의 경우 시간복잡도 : 
# 테스트 케이스의 최대수 X (DFS돌리고 루프돌며 방문처리 따지는 연산)
# 100 * (O(N + M) + O(N))
# = 100 * O(2N + M)
# = 1,200,000 : 시간 내에 통과

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    graph = {}
    N, M = map(int, input().split())
    visited = [0 for i in range(N + 1)]

    for i in range(M):
        a, b = map(int, input().split())
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]
    # DFS
    stack = [1]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            stack += graph[node]
    # 1 ~ N이 방문처리됐는지 따지며 안됐으면 즉시 0출력, 다 방문됐으면 N - 1출력
    for i in range(1, N + 1):
        if not visited[i]:
            print(0)
            break
    else:
        print(N - 1)

