def solution(board, moves):
    size = len(board)
    col = [[]]
    for i in range(size):
        line = [row[i] for row in board if row[i]]
        line.reverse()
        col.append(line)
    stack, answer = [], 0

    for mv in moves:
        if col[mv]:
            pick = col[mv].pop()
            if stack and stack[-1] == pick:
                stack.pop()
                answer += 2
            else:
                stack.append(pick)

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))