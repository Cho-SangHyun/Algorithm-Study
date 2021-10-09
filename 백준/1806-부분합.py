# 백준 1806 - 부분합(https://www.acmicpc.net/problem/1806)

"""
접근 방식 : 
    첫 번째 원소부터 시작해 부분합이 S이상이 되는 구간을 찾고, 그 구간의 길이를 length리스트에 푸시
    두 번째 원소부터 시작해 부분합이 S이상이 되는 구간을 찾고, 그 구간의 길이를 length리스트에 푸시
    세 번쩨 원소부터 시작해 부분합이 S이상이 되는 구간을 찾고, 그 구간의 길이를 length리스트에 푸시
    ...마지막에 min(length)를 통해 length리스트에서 최솟값을 출력
"""

# import sys

# N, S = map(int, sys.stdin.readline().split())
# length = []

# arr = list(map(int, sys.stdin.readline().split()))

# for i in range(len(arr)):
#     j, sum = i + 1, arr[i]

#     while(sum < S and j < len(arr)):
#             sum += arr[j]
#             j += 1
#     if sum >= S:
#         length.append(j - i)

# if length:
#     print(min(length))
# else:
#     print(0)

"""
처음에 위처럼 코드를 짜서 했는데 시간초과가 뜸
j라는 변수를 활용해 j와 i의 인덱스 차이를 이용해 길이를 재는데 매번 시작점(i)을 세팅할 때마다 j를 시작점 + 1로 하는게 문제인듯
사실 어떤 측정에서 j의 위치가 정해지면 그 다음 측정에서의 j의 위치는 바로 전에 측정한 위치와 같거나 그 후이기 때문에
j를 매번 세팅해주는게 아니라 전에 썼던 위치 그대로를 다시 사용하면 될 것 같았다
"""

import sys

N, S = map(int, sys.stdin.readline().split())
length = []

arr = list(map(int, sys.stdin.readline().split()))
sum_arr, j = arr[0], 1

for i in range(len(arr)):           # i : 측정할 구간의 시작점, sum_arr : 현재 구간의 부분합
    while(sum_arr < S and j < len(arr)):   # 이 반복문 안에서 부분합 >= S가 되는 구간의 길이 측정
        sum_arr += arr[j]             
        j += 1
    if sum_arr >= S:                      # 측정된 부분합이 S이상이면 length배열에 구간의 길이를 추가
        length.append(j - i)
    sum_arr -= arr[i]                     # 다음 번 측정에선 시작점이 i + 1이 되므로 현재의 시작점에 해당하는 값을 부분합에서 뺌

if length:                                
    print(min(length))
else:                                     # 합을 만드는 게 불가능해서 측정된 게 없으면 문제의 요구에 따라 0을 출력
    print(0)

"""
피드백 코멘트 :
주석에 남겨주신 풀이 과정이 인상적이네요. 대부분의 알고리즘 문제는 브루트한 방법으로 먼저 풀다가 최적화하는 방향으로 진행합니다.
물론 처음부터 좋은 성능으로 풀어도 좋지요. 하지만 안풀린다고 포기하지말고 이번 문제처럼 조금씩 개선해나가면 풀릴때가 많습니다.
고생하셨습니다!
"""
