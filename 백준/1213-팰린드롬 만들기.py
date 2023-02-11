from collections import defaultdict

word = input().strip()
count_per_alpha = defaultdict(int)

for i in range(len(word)):
    ch = word[i]
    count_per_alpha[ch] += 1

alpha_counts = []
for k, v in count_per_alpha.items():
    alpha_counts.append((k, v))

alpha_counts.sort()
answer = ""
last_insert_alpha = ""

for alpha_count in alpha_counts:
    alpha, count = alpha_count
    if count % 2 == 0:
        answer += alpha * (count // 2)
    else:
        answer += alpha * (count // 2)
        last_insert_alpha += alpha

if not last_insert_alpha:
    half_answer = list(map(str, answer))
    half_answer.reverse()
    answer = answer + ''.join(half_answer)
    print(answer)
elif len(last_insert_alpha) == 1:
    half_answer = list(map(str, answer))
    half_answer.reverse()
    answer = answer + last_insert_alpha + ''.join(half_answer)
    print(answer)
else:
    print("I'm Sorry Hansoo")

