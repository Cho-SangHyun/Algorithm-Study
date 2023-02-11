import sys
input = sys.stdin.readline

N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

answer = 0

for i in range(len(score) - 2, -1, -1):
    if score[i] < score[i + 1]:
        continue
    answer += (score[i] - score[i + 1] + 1)
    score[i] = score[i + 1] - 1

print(answer)
