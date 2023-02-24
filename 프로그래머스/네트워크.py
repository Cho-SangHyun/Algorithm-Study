from collections import deque


def solution(n, computers):
    answer = 0
    visited = set()

    for node in range(n):
        if node not in visited:
            answer += 1

            q = deque([node])
            visited.add(node)

            while q:
                i = q.popleft()
                for j in range(n):
                    if i == j:
                        continue
                    if computers[i][j] and j not in visited:
                        visited.add(j)
                        q.append(j)

    return answer