from collections import deque

n, k = map(int, input().split())
if n == k:
    print(0)
    print(1)
    exit()

dist = [-1 for _ in range(200001)]
ways = 0
dist[n] = -1

q = deque([(n, 0)])

while q:
    node, d = q.popleft()
    if node == k and d == dist[k]:
        ways += 1
        continue
    for new_node in (node + 1, node - 1, node * 2):
        if new_node < 0 or new_node >= 200000:
            continue
        if dist[new_node] == -1:
            q.append((new_node, d + 1))
            dist[new_node] = d + 1
        elif dist[new_node] == d + 1:
            q.append((new_node, d + 1))

print(dist[k])
print(ways)
