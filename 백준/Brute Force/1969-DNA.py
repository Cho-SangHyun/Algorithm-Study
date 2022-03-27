# 길이가 M인 문자열 N개가 주어진다. 이 중 임의의 문자열 S에 대하여 hamming distance가 가장 작은 S는?
# 찐 무식하게 만들 수 있는 모든 문자열 탐색하는 건 ㄹㅇ 미친 짓임. 4의 50승이 걸린다.
# 주어진 문자열들에 대해 인덱스별로 가장 많이 등장한 알파벳을 취한다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data = []

for _ in range(N):
    data.append(input())

answer_dna, answer_count = '', 0

for c in range(M):
    count = [0, 0, 0, 0]
    for r in range(N):
        if data[r][c] == 'A':
            count[0] += 1
        elif data[r][c] == 'C':
            count[1] += 1
        elif data[r][c] == 'G':
            count[2] += 1
        else:
            count[3] += 1
    max_idx, max_count = -1, -1
    for i in range(4):
        if count[i] > max_count:
            max_count = count[i]
            max_idx = i
    if max_idx == 0:
        answer_dna += 'A'
    elif max_idx == 1:
        answer_dna += 'C'
    elif max_idx == 2:
        answer_dna += 'G'
    else:
        answer_dna += 'T'
    answer_count += N - max_count

print(answer_dna)
print(answer_count)

# 주어진 데이터들 각각에 대한 어떠한 값들의 합이 ~가 되는 특정 답을 찾는 문제
# 주어진 데이터들 각각에 대한 어떤 값들을 구하는 작업이 필요하므로
# 주어진 데이터들 모두를 연산해야 하는 것은 필수적인 작업임.