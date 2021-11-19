"""
길이가 1 : 1
길이가 2 : 10
길이가 3 : 101, 100
길이가 4 : 1010, 1000, 1001
길이가 5 : 10100, 10101, 10000, 100001, 10010
길이가 n인 이친수들: 길이가 n-1인 이친수 중 마지막이 1로 끝나는 이친수에 0 붙인 수
                    + 길이가 n-1인 이친수 중 마지막이 0으로 끝나는 이친수에 0이나 1을 붙인 수들

"""

N = int(input())

# dp[x][0] = 마지막이 0으로 끝나는 길이가 x인 이친수
# dp[x][1] = 마지막이 1로 끝나는 길이가 x인 이친수
dp = [[0, 0], [0, 1], [1, 0]]

for i in range(3, N + 1):
    # count1 = 길이가 i-1이면서 마지막이 0으로 끝나는 수의 개수, count2 = 마지막이 1로 끝나는 이친수 개수
    count1 = dp[i - 1][1] + dp[i - 1][0]
    count2 = dp[i - 1][0]
    dp.append([count1, count2])

print(sum(dp[N]))