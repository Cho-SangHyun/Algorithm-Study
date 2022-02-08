N = int(input())

i = 1

dp = [0 for _ in range(N + 1)]

while i ** 2 <= N:
    dp[i ** 2] = 1
    i += 1

for j in range(1, N + 1):
    if not dp[j]:
        temp = 987654321
        for k in range(1, int(j ** 0.5) + 1):
            temp = min(temp, 1 + dp[j - (k ** 2)])
        dp[j] = temp

print(dp[N])
