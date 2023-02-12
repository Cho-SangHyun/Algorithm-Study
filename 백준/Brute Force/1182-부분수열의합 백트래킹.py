import sys
sys.setrecursionlimit(10**7)

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
parts = []


def dfs(i):
    global answer

    if i == n:
        if parts and sum(parts) == s:
            answer += 1
        return

    parts.append(numbers[i])
    dfs(i + 1)

    parts.pop()
    dfs(i + 1)


parts.append(numbers[0])
dfs(1)

parts.pop()
dfs(1)

print(answer)
