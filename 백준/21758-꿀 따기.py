# 21758 - 꿀 따기
# 적절한 두 위치에 벌, 한 위치에 벌통을 놓는다
# 벌들은 벌통으로 곧게 나아가며 시작점을 제외한 모든 위치의 꿀을 수집
# 다른 벌이 시작한 지점의 꿀은 딸 수 없다
# 제일 많은 꿀을 채집할 때의 꿀양은?

# 1. 무식한 접근
# 벌들을 위치할 수 있는 2개의 장소, 벌통을 놓는 장소 1개를 고르는 모든 조합을 탐색
# nC2 * (n-2) = 대략 O(n^3), 통과 불가

# 2. 부분문제로 쪼개기 가능?
# 첫 번째 벌을 a라는 칸에 뒀을 때 나오는 부분문제
# 첫 번째 벌을 b라는 칸에 뒀을 때 나오는 부분문제
# 등으로 쪼갤 수 있다

# 3. 중복됨?
# 첫 벌을 a, 두 번째 벌을 b에 둔 것은
# 첫 벌을 b, 두 번째 벌을 a에 둔 것과 같다. 그러나 이걸 이용해 dp스럽게 풀 순 없을 듯

# 4. 그리디?
# 우선 내가 어떻게 선택을 했다고 해서 다음 번 선택에 제약이 걸리는 건 아님
# 그러나 선택하는 단계는 딱 3번(첫 벌, 두 번째 벌, 벌통)뿐이다.

# 우선 직관적으로 벌들 중 한 마리는 양 끝 2개 중 하나에 위치시켜야 함. 그래야 손해가 없음
# 첫 벌을 L에 두고 꿀통을 R에 둔 다음 두 번째 벌을 L + 1 ~ R - 1까지 옮기며 계산
# 첫 벌을 L에 두고 두 번째 벌을 R에 둔 다음 꿀통을 L + 1 ~ R - 1까지 옮기며 계산

# 이렇게 해서 최대치를 찾을 수 있을 것 같은데? 시간복잡도는 누적합을 미리 구해뒀다고 하면
# 대략 O(4n) = O(n)

import sys

input = sys.stdin.readline

N = int(input())

data = [0] + list(map(int, input().split()))

sums = [0]

for i in range(1, N + 1):
    sums.append(sums[i - 1] + data[i])

answer = []

# 첫 벌을 L에 박는 경우
def search_left():
    semi_answer = []
    # 벌통을 R에 박았을 때 : 즉 i가 두 번째 벌
    for i in range(2, N):
        semi_answer.append(
            # 두 번째 벌이 채집하는 꿀들
            (sums[N] - sums[i]) + 
            # 첫 번째 벌이 채집하는 꿀들
            (sums[N] - data[1] - data[i])
        )
    # 두 번째 벌을 R에 박았을 때 : 즉 i가 벌통
    for i in range(2, N):
        semi_answer.append(
            # 첫 번째 벌이 채집하는 꿀들
            (sums[i] - data[1]) + 
            # 두 번째 벌이 채집하는 꿀들
            (sums[N] - sums[i - 1] - data[N])
        )
    
    answer.append(max(semi_answer))

# 첫 벌을 R에 박는 경우
def search_right():
    semi_answer = []
    # 벌통을 L에 박았을 때 즉 i가 두 번째 벌
    for i in range(2, N):
        semi_answer.append(
            # 첫 번째 벌이 채집하는 꿀들
            (sums[N] - data[N] - data[i]) + 
            # 두 번째 벌이 채집하는 꿀들
            (sums[i] - data[i])
        )
    # 두 번째 벌을 L에 박았을 때 : 즉 i가 벌통
    for i in range(2, N):
        semi_answer.append(
            # 첫 번쨰 벌이 채집하는 꿀들
            (sums[N] - sums[i - 1] - data[N]) + 
            # 두 번째 벌이 채집하는 꿀들
            (sums[i] - data[1])
        )
    answer.append(max(semi_answer))

search_left()
search_right()

print(max(answer))
