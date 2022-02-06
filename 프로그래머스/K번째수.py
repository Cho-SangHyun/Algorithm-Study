def solution(array, commands):
    array = [0] + array
    answer = []
    for cmd in commands:
        i, j, k = cmd
        new_arr = sorted(array[i:j + 1])
        print(new_arr)
        answer.append(new_arr[k - 1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))