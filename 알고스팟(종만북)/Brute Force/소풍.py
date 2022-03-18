# 주어지는 유치원생들을 친구인 애들끼리만 짝지을 때, 전부다 짝지어 줄 수 있는 방법의 수 구하기

# 무식하게 풀려고 한다면,
# N명의 친구들이 서로 죄다 친구인 경우에 연산을 가장 많이 하게 된다. 이땐 아무렇게나 지어줘도 짝이 될 수 있으니.
# 이 경우 9 * 7 * 5 * 3 번만 연산하면 됨

# import sys  

# input = sys.stdin.readline

# C = int(input())

# for _ in range(C):
#     n, m = map(int, input().split())
#     between = list(map(int, input().split()))
#     # friend[x] = x와 친구인 애들
#     friend = [set() for _ in range(n)]

#     for i in range(0, m):
#         friend[between[2 * i]].add(between[2 * i + 1])
#         friend[between[2 * i + 1]].add(between[2 * i])

#     answer = 0
#     matched = [0 for _ in range(n)]

#     def matching(now, matched_count):
#         global answer
#         if matched_count == n // 2: 
#             answer += 1
#             return

#         if matched[now]:
#             if now < n - 1:
#                 matching(now + 1, matched_count)
#             return

#         for fr in friend[now]:
#             if not matched[fr]:
#                 matched[now], matched[fr] = 1, 1
#                 matching(now + 1, matched_count + 1)
#                 matched[now], matched[fr] = 0, 0
    
#     matching(0, 0)
#     print(answer)

import sys  

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    n, m = map(int, input().split())
    between = list(map(int, input().split()))
    # friend[x] = x와 친구인 애들
    friend = [set() for _ in range(n)]

    for i in range(0, m):
        friend[between[2 * i]].add(between[2 * i + 1])
        friend[between[2 * i + 1]].add(between[2 * i])

    matched = [0 for _ in range(n)]

    def matching(cnt):
        if cnt == n // 2:
            return 1
        now, answer = -1, 0

        for i in range(n):
            if not matched[i]:
                now = i
                break
        
        if now != -1:
            for fr in range(now + 1, n):
                if not matched[fr] and fr in friend[now]:
                    matched[now], matched[fr] = 1, 1
                    answer += matching(cnt + 1)
                    matched[now], matched[fr] = 0, 0

        return answer

    print(matching(0))
        