import sys

def func(x, y, z):
    if y==0:
        return 1
    mid_answer = func(x, y//2, z)
    if y%2 == 0:
        return mid_answer * mid_answer % z
    else:
        return mid_answer * mid_answer * x % z

A, B, C = map(int, sys.stdin.readline().split())
print(func(A, B, C))