def solution(n, k):
    check = [False for _ in range(n + 1)]
    count = 0
    removed = []

    for i in range(2, n + 1):
        if not check[i]:
            check[i] = True
            removed.append(i)
            count += 1
            if count == k:
                return removed.pop()
            for j in range(2 * i, n + 1, i):
                if not check[j]:
                    check[j] = True
                    removed.append(j)
                    count += 1
                    if count == k:
                        return removed.pop()

    return -1


N, K = map(int, input().split())
print(solution(N, K))
