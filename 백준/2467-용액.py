import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

left, right = 0, n - 1
answer_sum = sys.maxsize
answer_min, answer_max = 0, 0
while left < right:
    now_sum = nums[left] + nums[right]
    if abs(now_sum) < answer_sum:
        answer_sum = abs(now_sum)
        answer_min, answer_max = nums[left], nums[right]
    if now_sum == 0:
        break
    elif now_sum > 0:
        right -= 1
    else:
        left += 1

print(answer_min, end=' ')
print(answer_max)