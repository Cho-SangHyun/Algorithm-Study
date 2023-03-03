from collections import deque
import sys
input = sys.stdin.readline


def solution(n, m, k, a, trees_info):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    rice = [[5 for i in range(n)] for j in range(n)]
    tree = [[deque([]) for i in range(n)] for j in range(n)]
    dead = [[[] for i in range(n)] for j in range(n)]

    for r, c, old in trees_info:
        tree[r - 1][c - 1].append(old)

    for _ in range(k):
        # 봄, 여름
        for r in range(n):
            for c in range(n):
                next_tree_old = deque([])
                while tree[r][c]:
                    old = tree[r][c].popleft()
                    if rice[r][c] >= old:
                        rice[r][c] -= old
                        next_tree_old.append(old + 1)
                    else:
                        dead[r][c].append(old)
                        while tree[r][c]:
                            dead[r][c].append(tree[r][c].pop())
                        break
                while next_tree_old:
                    tree[r][c].append(next_tree_old.popleft())
                while dead[r][c]:
                    rice[r][c] += (dead[r][c].pop() // 2)
        # 가을, 겨울
        for r in range(n):
            for c in range(n):
                rice[r][c] += a[r][c]
                count = 0
                for old in tree[r][c]:
                    if old % 5 == 0:
                        count += 1
                if count:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if nr < 0 or nc < 0 or nr >= n or nc >= n:
                            continue
                        for j in range(count):
                            tree[nr][nc].appendleft(1)

    answer = 0

    for r in range(n):
        for c in range(n):
            if tree[r][c]:
                answer += len(tree[r][c])

    return answer


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
_trees = [list(map(int, input().split())) for _ in range(M)]

print(solution(N, M, K, A, _trees))
