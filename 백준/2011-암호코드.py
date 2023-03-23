import sys
input = sys.stdin.readline


def solution(crypto):
    if crypto[0] == "0" or "00" in crypto:
        return 0

    MOD = 1000000
    length = len(crypto)
    crypto = ' ' + crypto

    dp = [[0, 0, 0] for i in range(length + 1)]
    # dp[x][1] = x자리까지로 암호를 만드는데 마지막은 1글자
    # dp[x][1] = x자리까지로 암호를 만드는데 마지막은 2글자
    dp[1][1] = 1

    for i in range(2, length + 1):
        prev = crypto[i - 1]
        cur = crypto[i]
        if cur != "0":
            dp[i][1] = (dp[i - 1][1] + dp[i - 1][2]) % MOD
        if (prev == "1" or prev == "2") and int(prev + cur) <= 26:
            dp[i][2] = dp[i - 1][1]

    return sum(dp[length]) % MOD


_crypto = input().strip()
print(solution(_crypto))
