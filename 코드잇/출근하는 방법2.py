# 총 계단 수 n과 한 번에 올라갈 수 있는 계단 수가 리스트 형태로 주어졌을 때
# n번째 계단까지 가는 방법의 수는?

# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(n, possible_steps):
    possible_steps.sort()

    dp = [0 for i in range(n + 1)]
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        for step in possible_steps:
            if i - step >= 0:
                dp[i] += dp[i - step]
            else:
                break
    return dp[n]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))