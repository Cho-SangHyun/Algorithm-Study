"""
2 : 1번
3 : 1번
4 : 2번
5 : 3번
6 : 2번
7 : 3번
8 : 3번
9 : 2번
10 : 3번
11 : 4번
12 : 3번
13 : 4번
14 : 4번
15 : 4번
16 : 4번
17 : 5번
18 : 3번
19 : 4번
20 : 4번
21 : 4번
22 : 5번
23 : 
x가 1



"""

N = int(input())

def solution(x):
    dp = [0, 0, 1, 1]
    for i in range(4, x + 1):
        if i % 6 == 0:
            dp.append(min(dp[i//3] + 1, dp[i//2] + 1))
        elif i % 3 == 0:
            dp.append(min(dp[i//3] + 1, dp[i-1] + 1))
        elif i % 2 == 0:
            dp.append(min(dp[i//2] + 1, dp[i-1] + 1))
        else:
            dp.append(min(dp[i-1] + 1, dp[i-2] + 2))
    
    answer = dp[x]
    return answer

print(solution(N))