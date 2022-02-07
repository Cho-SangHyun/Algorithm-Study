def solution(numbers):
    answer_nums = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    answer_nums -= set(numbers)
    return sum(list(answer_nums))