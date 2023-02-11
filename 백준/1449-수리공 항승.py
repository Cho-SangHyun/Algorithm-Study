import sys
input = sys.stdin.readline

N, L = map(int, input().split())

locations = list(map(int, input().split()))
locations.sort()

answer = 0
new_tape_start = locations[0]
answer = 1

for i in range(1, N):
    if locations[i] - new_tape_start + 1 > L:
        answer += 1
        new_tape_start = locations[i]

print(answer)
