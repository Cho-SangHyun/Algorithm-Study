answer = 0


def dfs(numbers, target, index, picked):
    global answer

    if index == len(numbers):
        if sum(picked) == target:
            answer += 1
        return

    picked.append(numbers[index])
    dfs(numbers, target, index + 1, picked)
    picked.pop()
크
    picked.append(-numbers[index])
    dfs(numbers, target, index + 1, picked)
    picked.pop()


def solution(numbers, target):
    global answer

    dfs(numbers, target, 1, [numbers[0]])
    dfs(numbers, target, 1, [-numbers[0]])

    return answer