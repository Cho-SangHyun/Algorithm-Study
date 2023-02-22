from collections import deque
import sys
input = sys.stdin.readline

directions = [(), (-1, 0), (0, 1), (1, 0), (0, -1)]


def move(board, d, red, blue):
    rr, rc = red
    br, bc = blue

    red_stopped = True if board[rr + directions[d][0]][rc + directions[d][1]] == "#" else False
    blue_stopped = True if board[br + directions[d][0]][bc + directions[d][1]] == "#" else False

    while not (red_stopped and blue_stopped):
        nrr, nrc = rr + directions[d][0], rc + directions[d][1]
        nbr, nbc = br + directions[d][0], bc + directions[d][1]

        if board[nrr][nrc] == "#":
            red_stopped = True
        if board[nbr][nbc] == "#":
            blue_stopped = True

        if not red_stopped:
            if board[nrr][nrc] == "O":
                rr, rc = nrr, nrc
                red_stopped = True
            elif blue_stopped and nrr == br and nrc == bc:
                red_stopped = True
            else:
                rr, rc = nrr, nrc

        if not blue_stopped:
            if board[nbr][nbc] == "O":
                br, bc = nbr, nbc
                blue_stopped = True
            elif red_stopped and nbr == rr and nbc == rc:
                blue_stopped = True
            else:
                br, bc = nbr, nbc

    return (rr, rc), (br, bc)


def solution(n, m, board):
    blue, red, goal = (), (), ()

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] == 'B':
                blue = (i, j)
            elif board[i][j] == 'R':
                red = (i, j)
            elif board[i][j] == 'O':
                goal = (i, j)

    q = deque([(blue, red, 0)])
    visited = set()
    visited.add((blue[0], blue[1], red[0], red[1]))
    # blue_visited, red_visited = set(), set()
    # blue_visited.add(blue)
    # red_visited.add(red)

    while q:
        blue_location, red_location, count = q.popleft()
        if count > 10:
            return -1
        if red_location == goal:
            return count
        for i in range(1, 5):
            new_red_location, new_blue_location = move(board, i, red_location, blue_location)
            if new_blue_location == goal:
                continue
            # if new_red_location in red_visited and new_blue_location in blue_visited:
            #     continue
            # red_visited.add(new_red_location)
            # blue_visited.add(new_blue_location)
            if (new_blue_location[0], new_blue_location[1], new_red_location[0], new_red_location[1]) not in visited:
                q.append((new_blue_location, new_red_location, count + 1))
                visited.add((new_blue_location[0], new_blue_location[1], new_red_location[0], new_red_location[1]))
    return -1


N, M = map(int, input().split())
game_board = [[]]
for _ in range(N):
    game_board.append([''] + list(map(str, input().strip())) + [''])
game_board.append([])

print(solution(N, M, game_board))
