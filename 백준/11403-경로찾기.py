from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
matrix = [[]]

for i in range(1, n + 1):
    info = [0] + list(map(int, input().split()))
    matrix.append(info)

answer = [[0 for i in range(n + 1)] for j in range(n + 1)]


def bfs(start, answer):
    visited = set()
    q = deque([start])

    while q:
        node = q.popleft()
        for i in range(1, n + 1):
            if matrix[node][i] == 1 and i not in visited:
                visited.add(i)
                answer[start][i] = 1
                q.append(i)


for i in range(1, n + 1):
    bfs(i, answer)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(answer[i][j], end=' ')
    print()
