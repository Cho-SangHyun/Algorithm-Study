from collections import deque


def solution(n, wires):
    answer = 987654321
    tree = [set() for _ in range(n + 1)]
    for a, b in wires:
        tree[a].add(b)
        tree[b].add(a)

    for a, b in wires:
        tree[a].remove(b)
        tree[b].remove(a)

        visited = set()
        count, i = [0, 0], 0

        for node in range(1, n + 1):
            if node not in visited:
                visited.add(node)
                count[i] += 1
                q = deque([node])

                while q:
                    now = q.popleft()
                    for c_node in tree[now]:
                        if c_node not in visited:
                            visited.add(c_node)
                            q.append(c_node)
                            count[i] += 1

                i += 1

        answer = min(answer, abs(count[0] - count[1]))
        tree[a].add(b)
        tree[b].add(a)

    return answer