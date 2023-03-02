def is_crossed_point(board, r, c):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr < 0 or nc < 0 or nr > 100 or nc > 100:
            return False
        if not board[nr][nc]:
            return False
    return True


def is_override_point(r, c, board):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    count = 0
    points = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr < 0 or nc < 0 or nr > 100 or nc > 100:
            continue
        if board[nr][nc]:
            count += 1
            points.append((nr, nc))

    if count == 1:
        return False
    if count > 2:
        return True
    if points[0][0] == points[1][0] or points[0][1] == points[1][1]:
        return False
    return True


def solution(lines):
    board = [[0 for i in range(101)] for j in range(101)]

    for line in lines:
        if line[0] == line[2]:
            for j in range(line[1], line[3] + 1):
                board[line[0]][j] = 1
        else:
            for i in range(line[0], line[2] + 1):
                board[i][line[1]] = 1

    answer = 0

    for r in range(101):
        for c in range(101):
            if board[r][c] and is_crossed_point(board, r, c):
                temp = []
                nr, nc = r - 1, c
                while board[nr][nc] and not is_override_point(nr, nc, board):
                    nr -= 1
                temp.append(abs(nr - r))

                nr, nc = r, c + 1
                while board[nr][nc] and not is_override_point(nr, nc, board):
                    nc += 1
                temp.append(abs(nc - c))

                nr, nc = r + 1, c
                while board[nr][nc] and not is_override_point(nr, nc, board):
                    nr += 1
                temp.append(abs(nr - r))

                nr, nc = r, c - 1
                while board[nr][nc] and not is_override_point(nr, nc, board):
                    nc -= 1
                temp.append(abs(nc - c))

                mid_answer = min(temp)
                answer = max(answer, mid_answer)

    return answer


print(solution([
    [1, 4, 5, 4],
    [2, 3, 2, 7],
    [5, 4, 8, 4],
    [2, 6, 3, 6],
    [3, 2, 7, 2],
    [6, 1, 6, 7],
    [3, 5, 3, 8],
    [3, 2, 3, 6]
]))
