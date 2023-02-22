import sys
input = sys.stdin.readline


def solution(nums, m):
    size = len(nums)
    if size == 1:
        return 1 if nums[0] == m else 0

    answer = 0
    left, right = 0, 0
    now_sum = nums[left]

    while True:
        if now_sum == m:
            answer += 1
            if left == right:
                left += 1
                right += 1
                if left >= size or right >= size:
                    break
                now_sum = nums[left]
                continue
            now_sum -= nums[left]
            left += 1
            if left >= size:
                break
            continue
        if now_sum < m:
            right += 1
            if right >= size:
                break
            now_sum += nums[right]
            continue
        if now_sum > m:
            if left == right:
                left += 1
                right += 1
                if left >= size or right >= size:
                    break
                now_sum = nums[left]
                continue
            now_sum -= nums[left]
            left += 1
            if left >= size:
                break

    return answer


n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(solution(arr, m))