"""
f(1) = 1
f(2) = 1
f(3) = 1
f(4) = 2
f(5) = 2
f(6) = 3
f(7) = 4
f(8) = 5
f(9) = 7
f(n) = f(n - 1) + f(n - 5)  단 n >= 6일때
"""
dp = [0, 1, 1, 1, 2, 2] + [0 for _ in range(100)]
for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

T = int(input())

for _ in range(T):
    N = int(input())
    print(dp[N])

# cache = {
#     1: 1,
#     2: 1,
#     3: 1,
#     4: 2,
#     5: 2
# }

# def solution(x):
#     if x not in cache:
#         cache[x] = solution(x - 1) + solution(x - 5)
#     return cache[x]

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     print(solution(N))