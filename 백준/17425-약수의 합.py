import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    answer = 0

    for i in range(1, int(N ** 0.5) + 1):
        answer += i * (N // i)
    
    print(answer)
