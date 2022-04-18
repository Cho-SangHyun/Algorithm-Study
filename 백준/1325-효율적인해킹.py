from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

answer, max_cnt = [], -1

for i in range(1, N + 1):
    cnt = 0
    q = deque([i])
    visited = set([])

    while q:
        node = q.popleft()
        # 방문한 적 없는 노드면 1증가시키고 자식들 큐에 추가
        if node not in visited:
            visited.add(node)
            cnt += 1
            for cnode in graph[node]:
                if cnode not in visited:
                    q.append(cnode)
    
    if cnt > max_cnt:
        max_cnt = cnt
        answer.clear()
        answer.append(i)
    elif cnt == max_cnt:
        answer.append(i)

print(*answer)

