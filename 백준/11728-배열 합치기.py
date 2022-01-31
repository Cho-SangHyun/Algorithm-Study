import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

i, j = 0, 0
C = []

while i < len(A) and j < len(B):
    if A[i] < B[j]:
        C.append(A[i])
        i += 1
    else:
        C.append(B[j])
        j += 1

if i < len(A):
    C += A[i:]

if j < len(B):
    C += B[j:]

for num in C:
    print(num)
