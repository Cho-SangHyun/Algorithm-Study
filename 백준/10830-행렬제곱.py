import sys

input = sys.stdin.readline

MOD = 1000

N, B = map(int, input().split())

data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

# matrix1 * matrix2를 리턴
def multiply(matrix1, matrix2):
    size = len(matrix1)
    ret = [[0 for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            for k in range(size):
                ret[i][j] = (ret[i][j] + (matrix1[i][k] * matrix2[k][j]) % MOD) % MOD

    return ret

def get_base_matrix(size):
    ret = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        ret[i][i] = 1
    return ret

# matrix를 n번 제곱한 행렬을 리턴
def solution(matrix, n):
    if n == 0:
        return get_base_matrix(len(matrix))
    
    if n % 2 == 1:
        return multiply(solution(matrix, n - 1), matrix)

    mid_matrix = solution(matrix, n // 2)
    return multiply(mid_matrix, mid_matrix)

answer = solution(data, B)

for i in range(N):
    for num in answer[i]:
        print(num, end=' ')
    print()