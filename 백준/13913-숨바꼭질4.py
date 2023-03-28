from collections import deque

N, K = map(int, input().split())
q = deque([])
q.append((N, 0))
visited = set()
visited.add(N)

prev = [i for i in range(200002)]

while q:
    now, time = q.popleft()
    if now == K:
        print(time)
        path = []
        while prev[now] != now:
            path.append(now)
            now = prev[now]
        path.append(N)
        for i in range(len(path) - 1, -1, -1):
            print(path[i], end=' ')
        exit()
    if now - 1 >= 0 and now - 1 not in visited:
        visited.add(now - 1)
        q.append((now - 1, time + 1))
        prev[now - 1] = now
    if now + 1 <= K and now + 1 not in visited:
        visited.add(now + 1)
        q.append((now + 1, time + 1))
        prev[now + 1] = now
    if now * 2 <= 2 * K and now * 2 not in visited:
        visited.add(now * 2)
        q.append((now * 2, time + 1))
        prev[now * 2] = now