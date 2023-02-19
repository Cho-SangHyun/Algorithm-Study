def solution(n, m):
    if n == 1 or m == 1:
        return 1
    if n <= 2 and m <= 2:
        return 1
    if n == 2:
        return (m - 1) // 2 + 1 if m <= 8 else 4
    if m == 2:
        return 2
    if m <= 4:
        return m
    if m == 5:
        return 4
    return 3 + m - 5


N, M = map(int, input().split())
print(solution(N, M))
