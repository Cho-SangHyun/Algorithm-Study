from collections import defaultdict

n = int(input())
words = [input().strip() for _ in range(n)]

value_per_alpha = defaultdict(int)

for word in words:
    for i in range(len(word)):
        alpha = word[i]
        exponent = len(word) - i - 1
        value_per_alpha[alpha] += 10 ** exponent

numbers = list(range(10))
values = []
for k, v in value_per_alpha.items():
    values.append(v)

values.sort(reverse=True)

answer = 0
for value in values:
    answer += (value * numbers.pop())

print(answer)