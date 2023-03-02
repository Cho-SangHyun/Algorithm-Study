import sys
input = sys.stdin.readline


def solution(n, curve_info):
    generation = [[[], [], [], []] for _ in range(11)]
    # generation[x][0] x세대 오른쪽으로
    # generation[x][1] 위
    # generation[x][2] 좌
    # generation[x][3] 하
    generation[0][0] = [(0, 0), (0, 1)]
    generation[0][1] = [(0, 0), (-1, 0)]
    generation[0][2] = [(0, 0), (0, -1)]
    generation[0][3] = [(0, 0), (1, 0)]

    for i in range(1, 11):
        for j in range(4):
            rotate = []
            sr, sc = generation[i - 1][j][-1]
            for k in range(len(generation[i - 1][j]) - 2, -1, -1):
                r, c = generation[i - 1][j][k]
                diff_r, diff_c = abs(sr - r), abs(sc - c)

                if r < sr and c >= sc:
                    nr, nc = sr + diff_c, sc + diff_r
                elif r >= sr and c > sc:
                    nr, nc = sr + diff_c, sc - diff_r
                elif r > sr and sc >= c:
                    nr, nc = sr - diff_c, sc - diff_r
                elif r <= sr and sc > c:
                    nr, nc = sr - diff_c, sc + diff_r

                rotate.append((nr, nc))

            generation[i][j] = generation[i - 1][j] + rotate

    maps = [[0 for i in range(101)] for j in range(101)]

    for c, r, d, g in curve_info:
        for dr, dc in generation[g][d]:
            nr, nc = r + dr, c + dc
            maps[nr][nc] = 1

    answer = 0
    for i in range(0, 100):
        for j in range(0, 100):
            if maps[i][j] and maps[i + 1][j] and maps[i][j + 1] and maps[i + 1][j + 1]:
                answer += 1

    return answer


N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

print(solution(N, info))
