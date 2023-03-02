import sys
input = sys.stdin.readline


def solution(target, data):
    left, right = 0, len(data) - 1
    start_index = -1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            start_index = mid
            right = mid - 1
        elif data[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    left, right = 0, len(data) - 1
    end_index = -1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            end_index = mid
            left = mid + 1
        elif data[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if start_index == -1 and end_index == - 1:
        return -1
    return end_index - start_index + 1


N, X = map(int, input().split())
nums = list(map(int, input().split()))

print(solution(X, nums))
