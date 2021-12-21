data = input()
# data의 마지막이 K면 마지막 원소는 '', 마지막이 M이면 마지막 원소는 M
words = data.split('K')

if not words[-1]:
    is_end_K = 1
    del words[-1]
else:
    is_end_K = 0

max_value, min_value = '', ''

for i in range(len(words)):
    if i == len(words) - 1 and not is_end_K:
        for _ in range(len(words[i])):
            max_value += '1'
        min_value += str(10 ** (len(words[i]) - 1))
    else:
        if words[i]:
            max_value += str(5 * (10 ** len(words[i])))
            min_value += str(5 + (10 ** len(words[i])))
        else:
            max_value += '5'
            min_value += '5'


print(max_value)
print(min_value)

