import sys
input = sys.stdin.readline


def solution(n, data):
    answer = 0
    count = [0 for _ in range(n + 1)]

    for num in data:
        count[num] += 1

    group = []
    for i in range(1, n + 1):
        if count[i]:
            group.append((i, count[i]))
    group.sort()

    rest = 0
    for g in group:
        rest += g[1] % g[0]
        if g[0] <= g[1]:
            answer += g[1] // g[0]
        if g[0] <= rest:
            answer += rest // g[0]
            rest = rest % g[0]

    return answer


N = int(input())
nums = list(map(int, input().split()))

print(solution(N, nums))


# 최적해: 공포도가 작은 순대로 인원수를 최소화해 팀을 꾸려 출발한다.
# 귀류 : 공포도가 작은 순이 아닌 순으로 인원수를 최소화한 것이 답이다
#       -> 각 그룹 안에서 공포도가 낮은 애들로 다른 그룹을 결성한다고 해도 총 그룹 수는 같다.
#       ex ) 어떤 그룹의 공포도가 2, 2, 3 -> 2, 2인 애들로 그룹을 만든다고 해도 전체 그룹 수는 같음


