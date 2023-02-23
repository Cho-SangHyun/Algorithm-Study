import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    heights = list(map(int, input().split()))
    heights.sort()
    new_heights = [0 for _ in range(n)]
    i = 0

    for h in heights:
        new_heights[i] = h
        if i < 0:
            i = -i
        else:
            i = -(i + 1)

    answer = -1
    for i in range(n):
        if i == n - 1:
            diff = abs(new_heights[0] - new_heights[-1])
        else:
            diff = abs(new_heights[i] - new_heights[i + 1])
        answer = max(answer, diff)

    print(answer)
