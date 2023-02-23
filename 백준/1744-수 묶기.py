import sys
input = sys.stdin.readline


def solution(n, nums):
    positive, negative, zero = [], [], 0
    answer = 0

    for num in nums:
        if num == 1:
            answer += 1
        elif num == 0:
            zero += 1
        elif num > 1:
            positive.append(num)
        else:
            negative.append(num)

    positive.sort()
    negative.sort(reverse=True)

    while positive:
        if len(positive) == 1:
            answer += positive.pop()
        else:
            answer += positive.pop() * positive.pop()

    while negative:
        if len(negative) == 1:
            if zero:
                negative.pop()
                zero -= 1
                continue
            answer += negative.pop()
        else:
            answer += negative.pop() * negative.pop()

    return answer


N = int(input())
data = []
for _ in range(N):
    data.append(int(input()))

print(solution(N, data))
