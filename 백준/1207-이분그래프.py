from collections import deque
import sys
input = sys.stdin.readline

k = int(input())


def bfs(graph, check, start):
    q = deque([])
    group_a = set()
    group_b = set()
    q.append((start, 'a'))
    group_a.add(start)

    answer = "YES"

    while q:
        node, team = q.popleft()

        for child in graph[node]:
            if team == 'a':
                if child in group_b:
                    continue
                if child in group_a:
                    answer = "NO"
                    continue
                group_b.add(child)
                check.add(child)
                q.append((child, "b"))
            elif team == 'b':
                if child in group_a:
                    continue
                if child in group_b:
                    answer = "NO"
                    continue
                group_a.add(child)
                check.add(child)
                q.append((child, "a"))

    return answer


for _ in range(k):
    v, e = map(int, input().split())

    graph = [[] for i in range(v + 1)]
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    check = set()

    for i in range(1, v + 1):
        if i not in check:
            check.add(i)
            if bfs(graph, check, i) == "NO":
                print("NO")
                break
    else:
        print("YES")
