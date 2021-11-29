"""
각 줄의 놓을 수 있는 위치에 퀸을 두며 N개의 퀸이 다 놓이는 순간을 센다
2차원 보드판 만들고 퀸이 놓일 때마다 퀸이 놓을 수 없는 위치들에 -1씩 해줌
퀸을 판에서 떼면 그 퀸 때문에 놓을 수 없던 위치들이 됐던 칸들에 +1씩 해줌
"""

# import sys
# sys.setrecursionlimit(10000)

# N = int(input())

# # board[r][c] == 1 -> 말 놓기 가능, 아니면 불가능
# board = [[1 for i in range(N + 1)] for j in range(N + 1)]
# answer = 0

# def take_off_queen(r, c):
#     board[r][c] += 1
#     # 아래, 대각선 아래(좌우)로 놓을 수 없던 위치들 +1씩
#     j = 1
#     for nr in range(r + 1, N + 1):
#         board[nr][c] += 1
#         if c + j <= N:
#             board[nr][c + j] += 1
#         if c - j >= 1:
#             board[nr][c - j] += 1
#         j += 1
 
# def put_queen(r, c):
#     global answer
#     board[r][c] -= 1
#     # N번째 열에 두게 됐다면 N개의 퀸을 두게 된 것이므로 answer + 1
#     if r == N:
#         answer += 1
#     else:
#         # 아래, 대각선 아래(좌우)로 놓을 수 없는 위치들 -1씩
#         j = 1
#         for nr in range(r + 1, N + 1):
#             board[nr][c] -= 1
#             if c + j <= N:
#                 board[nr][c + j] -= 1
#             if c - j >= 1:
#                 board[nr][c - j] -= 1
#             j += 1
        
#         for i in range(1, N + 1):
#             if board[r + 1][i] == 1: # 다음 행의 i번째 칸에 둘 수 있다면
#                 put_queen(r + 1, i)
#     take_off_queen(r, c)

# # 첫째 줄에 말 놓으면서 카운트 시작
# for i in range(1, N + 1):
#     put_queen(1, i); 

# print(answer)

"""
시간초과가 뜸. 반복문을 돌며 하나하나 둘 수 없는 칸으로 지정하고, 이걸 풀고 하는 작업들에서
시간이 오래 걸린 것이라 생각해서 1차원 배열을 쓰는 방법으로 바꿈
"""
import sys
sys.setrecursionlimit(10000)

N = int(input())
# board[i] = i번째 행에 둔 퀸의 열 값
board = [0 for _ in range(N + 1)]
answer = 0

def solution(r, c):
    global answer
    # r번째 열까지 온 것이면 N개의 퀸을 서로 공격할 수 없게 둔 것이므로 answer++
    if r == N:
        answer += 1
    else:
        board[r] = c
        # nc = 다음 행에 놓일 퀸의 열 값
        for nc in range(1, N + 1):
            # 다음 행(r + 1)의 nc에 퀸이 놓일 수 있는 지 검증
            for i in range(1, r + 1):
                # 이미 그 열에 어떤 퀸이 놓여져있거나 다른 퀸과 대각선 위치에 놓인다면
                if board[i] == nc or abs(i - (r + 1)) == abs(board[i] - nc):
                    break
            else:
                solution(r + 1, nc)
        board[r] = 0
    
for i in range(1, N + 1):
    solution(1, i)

print(answer)

"""
이 방법도 시간초과가 떠서 구글링해서 알아보다가,
pypy3로 내면 된다고 해서 통과됐다.
"""





    