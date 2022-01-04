# 11000 - 강의실 배정
# N개의 강의들이 시작시간&종료시간과 함께 주어짐
# 최소의 강의실을 사용해 모든 수업을 가능하게 해야 함
# 정답의 범위 : 1이상 200,000 이하

# 1. 무식하게 접근
# 가능한 모든 조합 중 가장 적게 쓰는 때를 찾음.
# 모든 강의가 서로 겹치지 않을 때 제일 많은 조합을 탐색하게 될 것 같다.
# N은 최대 200,000이므로, 20만^20만 정도의 탐색을 할 것 같음 -> 통과 불가

# 2. DP나 그리디 의심

# 2.1 부분문제로 쪼갤 수 있는지?
# O. 각 강의를 L1 ~ Ln이라 할 때
# L2 ~ Ln까지의 강의를 최소한의 강의실만 사용하는 경우를 구하면
# 구한 강의실들에 L1을 넣을 수 있는지 없는지 따져서 +1하거나 그대로 쓰거나 하면 됨

# 2.2 중복되는 구조가 있는지?
# 없는 것 같다. L1 ~ Ln을 구하기 위해 L2 ~ Ln을 구하고, L2 ~ Ln을 구하기 위해 
# L3 ~ Ln을 구하는 식이므로..

# 2.3 그리디?
# 내가 지금 단계에서 내리는 선택이 나중 단계에서 내리는 선택에 영향을 주지 않음
# (내가 지금단계에서 가장 빨리 끝나는 걸 골랐다고 다음 단계에서 가장 빨리 끝나는 걸 못 고르지 않음)
# 내가 내린 선택이 그 자체로 부분문제가 된다 -> 그리디 속성들이 있는 것 같다.
# 가장 빨리 시작하는 대로 고르던가 가장 빨리 끝나는대로 고르던가 해야 할 듯 하다
# 가장 빨리 ~하는 강의를 강의실에 배정. 그 다음에 가장 빨리 ~하는 애를 골라 이미 사용중인 강의실에 배정
# 직감으론 가장 먼저 시작하는 강의를 해야 하나 증명하지 못하고, 일단 코드로 옮겨보리고 함..

# 3. 또다른 문제점
# 가장 빨리 시작하는 강의를 강의실에 배정하는데, 이미 사용중인 특정 강의실에 배정가능한지는 내가 배정하려고 하는 강의가
# 그 강의실에 배정된 강의 중 가장 나중에 끝나는 강의 이후에 시작하는지를 판단해야 알 수 있음. 
# 제 1강의실, 2강의실 등등이 있다고 하면 최악의 경우 첫 번째 배정에선 1 ~ 1강의실까지, 
# 두 번째 배정에선 1 ~ 2강의실까지, 세 번째 배정에선 1 ~ 3번째 강의실까지를 탐색하게 되며 이 경우 n개의 강의들에 대해
# 시간복잡도는 O(n^2)이 되며 시간 내 통과가 불가능해짐(n이 최대 20만이므로)

# 4. 해결법
# 각 강의실별로 가장 나중에 끝나는 강의 중 가장 빨리 끝나는 강의를 a라고 하면
# 내가 고른 강의가 a이후에 시작하는지만 판단하면 됨
# a이후에 시작 : a를 하는 강의실에 내가 고른 강의를 배정
# a이전에 시작 : 현재 사용중인 모든 강의실에서 내가 고른 강의를 진행불가, 새 강의실을 배정

# 각 강의실의 강의 중 가장 나중에 끝나는 강의들만 heapq로 관리해주면 됨. 
# heapq의 pop은 O(1)이고 push는 O(long)이므로 
# 이 경우 최대 시간복잡도는 O(nlogn)이고 시간 내 통과가 가능해진다

import sys
import heapq

input = sys.stdin.readline

N = int(input())

# lectures : 입력받은 강의들
# last_class_per_classroom = 각 강의실의 강의 중 마지막 강의들
lectures = [] 
last_class_per_classroom = []


for _ in range(N):
    lec = list(map(int, input().split()))
    heapq.heappush(lectures, lec)

# 가장 먼저 시작하는 강의를 last_class_per_classroom에 옮기기
first_lec = heapq.heappop(lectures)
# last_class_per_classroom는 pop할 때 가장 먼저 끝나는 강의를 뱉어야 하므로 뒤집어서 넣어줌
first_lec.reverse()

heapq.heappush(last_class_per_classroom, first_lec)

answer = 1

for _ in range(N - 1):
    # data = 배정되지 않은 강의 중 가장 먼저 시작하는 강의
    data = heapq.heappop(lectures)
    a = heapq.heappop(last_class_per_classroom)
    # a[0] = 사용중인 각 강의실에 배정된 강의 중 마지막강의들의 집합에서 가장 빨리 끝나는 쉅의 종료시간
    # data[0] = 남은 수업 중 가장 먼저 시작하는 쉅의 시작시간
    if data[0] < a[0]:
        answer += 1
        heapq.heappush(last_class_per_classroom, a)
    data.reverse()
    heapq.heappush(last_class_per_classroom, data)

print(answer)

        