import sys
sys.setrecursionlimit(10**9)

N = int(input())
M = int(input())

broken_buttons = set()
if M:
    broken_buttons = set(map(int, input().split()))

if N == 100:
    print(0)
    exit()

available = list(set(range(10)) - broken_buttons)
answer = abs(N - 100)


def dfs(num, size):
    global answer

    if len(num) == size:
        number = int(num)
        answer = min(answer, len(num) + abs(number - N))
        return

    for n in available:
        num += str(n)
        dfs(num, size)
        num = num[:-1]


for i in range(1, 7):
    dfs('', i)

print(answer)
