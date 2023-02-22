import sys
input = sys.stdin.readline


def solution(n, m, nums):
    i, j = 1, m

    now_sum = sum(nums[i:j + 1])
    answer = now_sum

    while True:
        now_sum -= nums[i]
        i += 1
        j += 1
        if j > n:
            break
        now_sum += nums[j]
        answer = max(answer, now_sum)

    return answer


N, M = map(int, input().split())
data = [0] + list(map(int, input().split()))

print(solution(N, M, data))
