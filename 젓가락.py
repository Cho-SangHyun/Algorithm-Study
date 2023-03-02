import sys
sys.setrecursionlimit(10**7)
answer = 987654321


def dfs(n, chopsticks, count):
    global answer

    # print(chopsticks, count)

    for chop in chopsticks:
        if chop[0] != chop[1]:
            break
    else:
        answer = min(answer, count)
        return

    chopsticks_cp = [chop[:] for chop in chopsticks]

    for i in range(n):
        if chopsticks[i][0] == chopsticks[i][1]:
            continue

        target_left, target_right = chopsticks[i]
        target_left_index, target_left_number = 0, 0
        target_right_index, target_right_number = 0, 0

        for j in range(i + 1, n):
            if chopsticks[j][0] == target_left:
                target_left_index = j
                target_left_number = 0
                break
            if chopsticks[j][1] == target_left:
                target_left_index = j
                target_left_number = 1
                break

        for j in range(i + 1, len(chopsticks)):
            if chopsticks[j][0] == target_right:
                target_right_index = j
                target_right_number = 0
                break
            if chopsticks[j][1] == target_right:
                target_right_index = j
                target_right_number = 1
                break

        # 맞출 수 = i번째 젓가락의 왼쪽, 가져올 놈 = target_left_index
        if target_left_index <= target_right_index:
            if target_left_index == i + 1:
                chopsticks_cp[i][1], chopsticks_cp[target_left_index][target_left_number] = \
                    chopsticks_cp[target_left_index][target_left_number], chopsticks_cp[i][1]
                dfs(n, chopsticks_cp, count + 1)
            else:
                chopsticks_cp[target_left_index - 1][0], chopsticks_cp[target_left_index][target_left_number] = \
                    chopsticks_cp[target_left_index][target_left_number], chopsticks_cp[target_left_index - 1][0]
                dfs(n, chopsticks_cp, count + 1)

                chopsticks_cp = [chop[:] for chop in chopsticks]

                chopsticks_cp[target_left_index - 1][1], chopsticks_cp[target_left_index][target_left_number] = \
                    chopsticks_cp[target_left_index][target_left_number], chopsticks_cp[target_left_index - 1][1]
                dfs(n, chopsticks_cp, count + 1)
        # 맞출 수 = i번째 젓가락의 오른쪽, 가져올 놈 = target_right_index
        elif target_left_index > target_right_index:
            if target_right_index == i + 1:
                chopsticks_cp[i][0], chopsticks_cp[target_right_index][target_right_number] = \
                    chopsticks_cp[target_right_index][target_right_number], chopsticks_cp[i][0]
                dfs(n, chopsticks_cp, count + 1)
            else:
                chopsticks_cp[target_right_index - 1][0], chopsticks_cp[target_right_index][target_right_number] = \
                    chopsticks_cp[target_right_index][target_right_number], chopsticks_cp[target_right_index - 1][0]
                dfs(n, chopsticks_cp, count + 1)

                chopsticks_cp = [chop[:] for chop in chopsticks]

                chopsticks_cp[target_right_index - 1][1], chopsticks_cp[target_right_index][target_right_number] = \
                    chopsticks_cp[target_right_index][target_right_number], chopsticks_cp[target_right_index - 1][1]
                dfs(n, chopsticks_cp, count + 1)

        break


def solution(n, data):
    global answer
    chopsticks = []
    for d in data:
        chopsticks.append(list(d))

    dfs(n, chopsticks, 0)
    return answer



print(solution(4, ["AB", "CD", "BC", "DA"])) # 4
answer = 987654321
print(solution(3, ["AA", "BB", "CC"])) # 0
answer = 987654321
print(solution(4, ['AB', 'DC', 'DA', 'BC'])) # 4
answer = 987654321
print(solution(4, ['AC', 'DB', 'BC', 'DA'])) # 4
answer = 987654321
print(solution(4, ['AC', 'DB', 'BD', 'CA'])) # 4



