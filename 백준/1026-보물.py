# 길이가 같은 두 배열 A, B에 대해 
# S = A[0] * B[0] + A[1] * B[1] + ... + A[n - 1] * B[n - 1]로 정의
# B는 그대로 냅두고 A의 순서만 건드린다고 할 때 S의 최솟값은??

# 무식하게 풀려면 A의 순서를 놓는 N!개의 경우를 모두 따져야 함 -> time over
# 단순히 A를 오름차순/내림차순 정렬해서 계산한다고 해도 답이 보장되지 않음
# 왜냐? B가 오름차순이나 내림차순으로 주어지는 배열이 아니니까. B도 어떤 순서일지 아무도 모름

# 해결
# A는 오름차순, B는 내림차순 정렬해서 계산한다.
# 곱해서 나오는 값들의 수를 최대한 작게 하는 게 관건이므로
# B의 제일 큰 값에 A의 제일 작은 값을 매칭하는 게 뽀인뜨

# 아니 저기요 B는 건드리지 말라고 돼있는데요? 밑장빼깁니까?
# 결국 A의 가장 작은 값을 B의 가장 큰 값에 매칭하는 작업을 반복해야 하는데
# 이건 결국 A를 오름차순, B를 내림차순해서 인덱스같은 애들끼리 붙이는 것과 같습니다

import sys

input = sys.stdin.readline

N = int(input())

A, B = list(map(int, input().split())), list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

answer = 0

for i in range(N):
    answer += A[i] * B[i]

print(answer)