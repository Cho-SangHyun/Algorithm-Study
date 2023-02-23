from collections import deque
import sys
input = sys.stdin.readline


def solution(initial_status, k, rotations):
    connected = [
        [],
        [(2, 6, 2)],
        [(1, 2, 6), (3, 6, 2)],
        [(2, 2, 6), (4, 6, 2)],
        [(3, 2, 6)]
    ]

    chain = [[]]
    for s in initial_status:
        chain.append(deque(list(map(int, s))))

    for start, direction in rotations:
        q = deque([(start, direction)])
        visited = set([start])
        rotation_chain = [(start, direction)]

        while q:
            node, direction = q.popleft()
            for c_node, c_point, n_point in connected[node]:
                if c_node in visited:
                    continue
                if chain[node][n_point] != chain[c_node][c_point]:
                    visited.add(c_node)
                    if direction == 1:
                        q.append((c_node, -1))
                        rotation_chain.append((c_node, -1))
                    else:
                        q.append((c_node, 1))
                        rotation_chain.append((c_node, 1))

        for n, d in rotation_chain:
            if d == 1:
                chain[n].appendleft(chain[n].pop())
            else:
                chain[n].append(chain[n].popleft())

    answer = 0
    for i in range(1, 5):
        if chain[i][0] == 1:
            answer += 2 ** (i - 1)

    return answer


status = []
for _ in range(4):
    status.append(input().strip())

K = int(input())
ways = []
for _ in range(K):
    ways.append(list(map(int, input().split())))

print(solution(status, K, ways))
