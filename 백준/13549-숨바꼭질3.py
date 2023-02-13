import heapq

INF = 987654321

n, k = map(int, input().split())
times = [INF for _ in range(200002)]
times[n] = 0

q = []
heapq.heappush(q, (0, n))

while q:
    t, now = heapq.heappop(q)
    if times[now] < t:
        continue

    if now < k:
        if t < times[2 * now]:
            times[2 * now] = t
            heapq.heappush(q, (t, 2 * now))
        if t + 1 < times[now + 1]:
            times[now + 1] = t + 1
            heapq.heappush(q, (t + 1, now + 1))

    if now != 0:
        if t + 1 < times[now - 1]:
            times[now - 1] = t + 1
            heapq.heappush(q, (t + 1, now - 1))


print(times[k])
