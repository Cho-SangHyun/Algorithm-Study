import sys
input = sys.stdin.readline


def solution(n, nums):
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


N = int(input())
data = list(map(int, input().split()))

print(solution(N, data))
