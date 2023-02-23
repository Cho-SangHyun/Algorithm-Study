from collections import deque


def solution(f, s, g, u, d):
    q = deque([(s, 0)])
    visited = [0 for _ in range(f + 1)]
    visited[s] = 1

    while q:
        now, count = q.popleft()
        if now == g:
            return count
        if now + u <= f and not visited[now + u]:
            visited[now + u] = 1
            q.append((now + u, count + 1))
        if now - d >= 1 and not visited[now - d]:
            visited[now - d] = 1
            q.append((now - d, count + 1))

    return "use the stairs"


F, S, G, U, D = map(int, input().split())
print(solution(F, S, G, U, D))
