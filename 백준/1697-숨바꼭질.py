from collections import deque
import sys
sys.setrecursionlimit(10**9)

s, e = map(int, input().split())
visited = [0 for _ in range(1000000)]

q = deque([])
q.append((s, 0))

while q:
    location, second = q.popleft()
    if location == e:
        print(second)
        exit()
    if location < e:
        if not visited[location * 2]:
            q.append((location * 2, second + 1))
            visited[location * 2] = 1
        if not visited[location + 1]:
            q.append((location + 1, second + 1))
            visited[location + 1] = 1
    if location != 0 and not visited[location - 1]:
        q.append((location - 1, second + 1))
        visited[location - 1] = 1
