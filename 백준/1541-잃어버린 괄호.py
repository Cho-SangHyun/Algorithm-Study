# expression = input()

# def sub(arr):
#     size = len(arr)
#     answer = arr[0]
#     for i in range(1, size):
#         answer -= arr[i]
#     return answer

# def evaluate(exp):
#     nums = list(map(int, exp.split('+')))
#     return sum(nums)

# def solution(exp):
#     temp = []
#     offset, open_p = 0, 0
#     while offset < len(exp):
#         if exp[offset] == '-':
#            temp.append(evaluate(exp[open_p:offset]))
#            open_p = offset + 1
#         offset += 1
#         if offset == len(exp):
#             temp.append(evaluate(exp[open_p:offset]))
#     return sub(temp)

# print(solution(expression))

expressions = input().split('-')
nums = []

# expression은 -를 기준으로 파싱된 애들임. expression의 각 원소들을 계산하고 그 값들로 답을 도출할 수 있음
for exp in expressions:
    nums.append(sum(list(map(int, exp.split('+')))))

# nums엔 expression의 각 원소들의 계산결과가 들어감
# 계산결과는 각 원소들을 +기준으로 파싱한 후, int로 형변환하여 더해주면 얻을 수 있다. -> map을 활용
# int로 형변환할 시 00009같은 것도 정수 9로 바뀜

answer = nums[0]
for i in range(1, len(nums)):
    answer -= nums[i]

print(answer)


"""
수식의 결과가 작으려면
뺄셈으로만 이루어지거나
더할 때 작게 더하거나
뺼셈으로만 이루어지게 하는게 더 쉽다
1 + 2 + 4 + 7 - 8-? 3 - 4 = -1
"""