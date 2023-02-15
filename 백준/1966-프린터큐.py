from collections import deque
import sys
input = sys.stdin.readline

T = int(input())


def has_high_priority(q, node):
    for i in range(len(q)):
        if q[i][0] > node[0]:
            return True
    return False


for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    q = deque([])
    for i in range(N):
        q.append((priority[i], i))
    count = 0

    while q:
        node = q.popleft()
        if has_high_priority(q, node):
            q.append(node)
            continue
        count += 1
        if node[1] == M:
            print(count)
            break




