"""
두 문자열 str1, str2가 있을 때
LCS(i, j) = str2[:i]와 str1[:j]의 최장공통부분문자열

if str2[i] == str1[i]면
    LCS(i, j) = LCS(i - 1, j - 1) + str2[i]
str2[i] != str1[j]면
    LCS(i, j) = LCS(i - 1, j)와 LCS(i, j - 1) 중 더 큰 문자열

여기서 큰 문자열 >>
1) 길이가 더 긴 문자열
2) 길이가 같다면 사전 순으로 뒤에 위치한 문자열
"""

str1 = input()
str2 = input()

dp = [["" for i in range(len(str1) + 1)] for j in range(len(str2) + 1)] 

# 두 문자열 중 더 큰 문자열을 리턴하는 함수
# 파이썬은 문자열끼리 <, >같은 연산을 할 땐 첫글자부터 사전순 비교를 한다
# max의 파라미터로 문자열 두 개를 주면 사전순으로 더 뒤에 있는 문자열을 받을 수 있음
def str_compare(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else:
        return max(str1, str2) 

for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + str2[i - 1]
        else:
            dp[i][j] = str_compare(dp[i - 1][j], dp[i][j - 1])

print(len(dp[len(str2)][len(str1)]))
print(dp[len(str2)][len(str1)])

