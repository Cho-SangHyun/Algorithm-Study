import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    max_values = [0 for _ in range(N)]
    max_values[-1] = data[-1]
    max_v = data[-1]
    for i in range(N - 2, -1, -1):
        max_v = max(max_v, data[i])
        max_values[i] = max_v

    answer = 0
    for i in range(N - 1):
        if max_values[i + 1] > data[i]:
            answer += (max_values[i + 1] - data[i])
    print(answer)
