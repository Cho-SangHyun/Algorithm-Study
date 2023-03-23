from collections import deque


def solution(n):
    descending = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    q = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    while q:
        number = q.popleft()
        for i in range(0, number % 10):
            new_number = number * 10 + i
            q.append(new_number)
            descending.append(new_number)

    descending.sort()
    return descending[n] if n < len(descending) else -1


N = int(input())
print(solution(N))
