N = int(input())
data = list(map(int, input().split()))

box = {
    'A': data[0],
    'B': data[1],
    'C': data[2],
    'D': data[3],
    'E': data[4],
    'F': data[5]
}

min_three = min(box['D'] + box['E'] + box['A'], box['D'] + box['A'] + box['B'], box['D'] + box['B'] + box['F'],
                box['D'] + box['F'] + box['E'], box['C'] + box['E'] + box['A'], box['C'] + box['A'] + box['B'],
                box['C'] + box['B'] + box['F'], box['C'] + box['F'] + box['E'])

min_two = min(box['D'] + box['E'], box['D'] + box['A'], box['D'] + box['B'], box['D'] + box['F'],
              box['C'] + box['E'], box['C'] + box['A'], box['C'] + box['B'], box['C'] + box['F'],
              box['E'] + box['A'], box['A'] + box['B'], box['B'] + box['F'], box['F'] + box['E'])

min_one = min(data)

if N == 1:
    print(sum(data) - max(data))
    exit()
elif N == 2:
    answer = 0
    answer += 4 * min_three
    answer += 4 * min_two
    print(answer)
else:
    answer = 0
    answer += 4 * min_three
    answer += (min_two * (N - 1) * 4 + min_two * 4 * (N - 2))
    answer += (min_one * (N - 2) * (N - 1) * 4 + min_one * (N - 2) * (N - 2))
    print(answer)
