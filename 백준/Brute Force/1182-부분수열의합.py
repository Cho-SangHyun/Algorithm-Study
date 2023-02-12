from itertools import combinations

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

for i in range(1, n + 1):
    sub_numbers_comb = combinations(numbers, i)
    for comb in sub_numbers_comb:
        if sum(comb) == s:
            answer += 1

print(answer)
