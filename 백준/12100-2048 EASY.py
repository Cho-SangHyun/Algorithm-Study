from collections import deque
import sys
input = sys.stdin.readline
answer = 0
directions = [(), (-1, 0), (0, 1), (1, 0), (0, -1)]


def get_q(direction, board):
    q = [deque([]) for _ in range(len(board))]
    if direction == 1:
        for c in range(len(board)):
            for r in range(len(board)):
                if board[r][c]:
                    q[c].append((r, c))
    elif direction == 2:
        for r in range(len(board)):
            for c in range(len(board) - 1, -1, -1):
                if board[r][c]:
                    q[r].append((r, c))
    elif direction == 3:
        for c in range(len(board)):
            for r in range(len(board) - 1, -1, -1):
                if board[r][c]:
                    q[c].append((r, c))
    else:
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c]:
                    q[r].append((r, c))

    return q


def move(direction, _board):
    queues = get_q(direction, _board)
    board = [row[:] for row in _board]
    changed = [[0 for i in range(len(_board))] for j in range(len(_board))]

    for q in queues:
        while q:
            r, c = q.popleft()
            value = board[r][c]
            dr, dc = directions[direction]
            while True:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board):
                    break
                if not board[nr][nc]:
                    board[r][c] = 0
                    board[nr][nc] = value
                    r, c = nr, nc
                    continue
                if board[nr][nc] == value and not changed[nr][nc]:
                    board[r][c] = 0
                    board[nr][nc] = value * 2
                    r, c = nr, nc
                    changed[nr][nc] = 1
                    continue
                break

    return board


def dfs(count, board):
    global answer
    if count == 5:
        for row in board:
            answer = max(answer, max(row))
        return

    for d in range(1, 5):
        _board = move(d, board)
        dfs(count + 1, _board)


def solution(n, board):
    global answer
    for d in range(1, 5):
        _board = move(d, board)
        dfs(1, _board)
    return answer


N = int(input())
_board = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, _board))
