from collections import deque
import sys
input = sys.stdin.readline


def solution(n, d, k, c, table):
    count = [0 for _ in range(d + 1)]

    q = deque([])
    now_length = 0

    for i in range(1, k + 1):
        if not count[table[i]]:
            now_length += 1
        count[table[i]] += 1
        q.append(table[i])

    answer = now_length if count[c] else now_length + 1

    i = k + 1
    while i != k:
        exit_node = q.popleft()
        if count[exit_node] == 1:
            now_length -= 1
        count[exit_node] -= 1

        if not count[table[i]]:
            now_length += 1
        count[table[i]] += 1
        q.append(table[i])

        mid_answer = now_length if count[c] else now_length + 1
        answer = max(answer, mid_answer)

        i += 1
        if i > n:
            i = 1

    return answer


N, D, K, C = map(int, input().split())
tables = [0]
for _ in range(N):
    tables.append(int(input()))

print(solution(N, D, K, C, tables))
