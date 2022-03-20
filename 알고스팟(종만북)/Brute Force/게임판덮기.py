# 주어진 보드판에서 흰색 영역들을 ㄴ자 블록들로만 덮는 방법의 수 구하기
# ㄴ자 블록은 자유롭게 회전이나 뒤집기가 가능하지만, 보드판을 넘어서거나 검은색 영역을 덮으면 안됨

import sys
sys.setrecursionlimit(10**9)

block_set = [
    # [(0, 0), (-1, 0), (-1, 1)],  # 기역 자 1
    # [(0, 0), (0, 1), (1, 1)],    # 기역 자 2
    # [(0, 0), (1, 0), (1, -1)],   # 기역 자 3
    # [(0, 0), (0, -1), (-1, -1)], # 기역 자 4
    # [(0, 0), (-1, 0), (-1, -1)], # 니은 자 1
    # [(0, 0), (0, 1), (-1, 1)],   # 니은 자 2
    # [(0, 0), (1, 0), (1, 1)],    # 니은 자 3
    # [(0, 0), (0, -1), (1, -1)]   # 니은 자 4
    [(0, 0), (0, 1), (1, 1)],    
    [(0, 0), (1, 0), (1, 1)],    
    [(0, 0), (1, 0), (1, -1)],
    [(0, 0), (1, 0), (0, 1)]
]

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    H, W = map(int, input().split())
    white_count = 0
    # 파이썬 특성상 문자열의 일부만 인덱싱으로 수정하는 것은 불가능
    # 그냥 배열로 받기
    board = []
    for i in range(H):
        line = []
        _input = input().rstrip()

        for ch in _input:
            if ch == '.': white_count += 1
            line.append(ch)

        board.append(line)

    def put_block():
        # 채워야 할 흰 칸 찾기 - 우측하단 방향으로 탐색
        r, c = -1, -1
        for i in range(H):
            for j in range(W):
                if board[i][j] == '.':
                    r, c = i, j
                    break
            if r != -1:
                break
        # 흰 칸이 없다면 r, c값이 -1, -1에서 변화 없음 -> 보드를 전부다 채운거니까 1을 리턴 
        if r + c == -2:
            return 1
        # 여기까지 진행되면 r, c = 현재 블록을 놓아야 할 r, c값
        answer = 0

        break_point = 0

        for block in block_set:
            # 블록 놓기 - 놓다가 놓을 수 없는 부분이면 break
            for dr, dc in block:
                nr, nc = r + dr, c + dc
                if (0 <= nr and nr < H) and (0 <= nc and nc < W) and board[nr][nc] == ".":
                    board[nr][nc] = '#'
                    break_point += 1
                else:
                    break
            # 이 else문이 실행되는 상황 => ㄴ자 블록을 무사히 다 두게 된 상황
            else:
                answer += put_block()
            # 뒀던 블록 다시 거두기
            for dr, dc in block:
                if break_point == 0:
                    break
                else:
                    board[r + dr][c + dc] = "."
                    break_point -= 1
        
        return answer
        
    if white_count % 3 == 0:
        print(put_block())
    else:
        print(0)
                
    