import sys

input = sys.stdin.readline

K = int(input())
stack = []

for _ in range(K):
    c = int(input())
    if c:
        stack.append(c)
    else:
        stack.pop()

print(sum(stack))