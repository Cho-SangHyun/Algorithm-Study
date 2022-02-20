import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

tree = [set([]) for _ in range(N)]

_input = list(map(int, input().split()))

delete_node = int(input())

root = 0

for i, data in enumerate(_input):
    if data != -1:
        tree[data].add(i)
    else:
        root = i

q = deque([delete_node])

while q:
    nd = q.popleft()
    q += list(tree[nd])
    tree[nd] = set([])

ans = 0
q = deque([root])

while q:
    nd = q.popleft()

    if delete_node in tree[nd]: 
        tree[nd].remove(delete_node)

    if delete_node != nd and not tree[nd]:
        ans += 1
    else:
        q += tree[nd]

print(ans)

