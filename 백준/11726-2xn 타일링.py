# N = int(input())

# MOD = 10007
# # dp[x][0] : x번째 열까지 채우는데 마지막이 세로로 끝나는 경우
# # dp[x][1] : x번째 열까지 채우는데 마지막이 가로로 끝나는 경우
# dp = [[0, 0], [1, 0], [1, 1], [2, 1]]

# for i in range(4, 1001):
#     dp.append(
#         [(sum(dp[i - 2]) + dp[i - 1][1]) % MOD, sum(dp[i - 2]) % MOD]
#     )

# print(sum(dp[N]) % MOD)

N = int(input())

MOD = 10007

dp = [0, 1, 2, 3]

for i in range(4, N + 1):
    dp.append((dp[i - 2] + dp[i - 1]) % MOD)

print(dp[N])