from itertools import permutations
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
data =[[]]
for _ in range(N):
    row = [0] + list(map(int, input().split()))
    data.append(row)
rotate_info = [list(map(int, input().split())) for _ in range(K)]


def rotate(data, r, c, s):
    garo_length = c + s - (c - s) + 1
    sero_length = r + s - (r - s) + 1
    garo_max_rotate = garo_length // 2
    sero_max_rotate = sero_length // 2

    rotate_count = min(garo_max_rotate, sero_max_rotate)

    for x in range(rotate_count):
        temp = data[r - s + x][c + s - x]
        # 상
        for j in range(c + s - x, c - s + x, -1):
            data[r - s + x][j] = data[r - s + x][j - 1]
        # 좌
        for i in range(r - s + x, r + s - x):
            data[i][c - s + x] = data[i + 1][c - s + x]
        # 하
        for j in range(c - s + x, c + s - x):
            data[r + s - x][j] = data[r + s - x][j + 1]
        # 우
        for i in range(r + s - x, r - s + x, -1):
            if i == r - s + x + 1:
                data[i][c + s - x] = temp
                continue
            data[i][c + s - x] = data[i - 1][c + s - x]


answer = 987654321

for perm in permutations(rotate_info, K):
    _data = [data[i][:] for i in range(N + 1)]
    for r, c, s in perm:
        rotate(_data, r, c, s)
    for i in range(1, N + 1):
        answer = min(answer, sum(_data[i]))

print(answer)
