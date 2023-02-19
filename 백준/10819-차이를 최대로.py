import sys
sys.setrecursionlimit(10**9)

N = int(input())
nums = list(map(int, input().split()))
answer = -1


def dfs(selected, arr):
    global answer
    if len(arr) == N:
        mid_answer = 0
        for i in range(N - 1):
            mid_answer += abs(arr[i] - arr[i + 1])
        answer = max(answer, mid_answer)
        return

    for i in range(N):
        if i not in selected:
            selected.add(i)
            arr.append(nums[i])
            dfs(selected, arr)
            arr.pop()
            selected.remove(i)


dfs(set(), [])
print(answer)
