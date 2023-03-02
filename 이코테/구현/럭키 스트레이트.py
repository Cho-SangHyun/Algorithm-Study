def solution(n):
    length = len(str(n))
    left, right = str(n)[:length // 2], str(n)[length // 2:]

    left_sum, right_sum = 0, 0
    for i in range(len(left)):
        left_sum += int(left[i])
        right_sum += int(right[i])

    return "LUCKY" if left_sum == right_sum else "READY"


N = int(input())
print(solution(N))
