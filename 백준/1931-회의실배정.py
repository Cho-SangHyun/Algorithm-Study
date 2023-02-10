import sys
input = sys.stdin.readline

n = int(input())
lectures = [list(map(int, input().split())) for _ in range(n)]

lectures.sort(key=lambda x: (x[1], x[0]))

last_selected_lecture_end_time = 0
answer = 0

for lecture in lectures:
    if lecture[0] > lecture[1]:
        continue
    if lecture[0] >= last_selected_lecture_end_time:
        answer += 1
        last_selected_lecture_end_time = lecture[1]

print(answer)
