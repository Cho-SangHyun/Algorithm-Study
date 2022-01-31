import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

stones = [0] + list(map(int, sys.stdin.readline().split()))
# start_node = 인덱스값
def bfs(start_node):
    queue = deque([start_node])
    visited = [0 for _ in range(N + 1)]

    while queue:
        node = queue.popleft()
        for i in range(node + 1, N + 1):
            if not visited[i] and (i - node) * (1 + abs(stones[node] - stones[i])) <= K:
                visited[i] = 1
                queue.append(i)
                if i == N: 
                    return True
    
    return False

if bfs(1):
    print("YES")
else:
    print("NO")