N = int(input())

score = [0]

for _ in range(N):
    score.append(int(input()))

# dp[i][0] = i번째 계단까지 올라오는 최대점수 중 직전에 1칸 올라온 경우의 값
# dp[i][1] = i번째 계단까지 올라오는 최대점수 중 직전에 2칸 올라온 경우의 값

dp = [[0, 0], [score[1], score[1]]]

for i in range(2, N + 1):
    dp.append([
        dp[i - 1][1] + score[i],
         max(dp[i - 2]) + score[i]
    ])

print(max(dp[N]))

