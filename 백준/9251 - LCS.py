"""
두 문자열 str1, str2에 대해
LCS(i, j) = str1[:i]과 str2[:j]의 LCS길이

이 때 정답은
1) str1[i] == str2[j]이면 LCS(i - 1, j - 1) + 1
    >> 두 문자열로부터 얻어지는 최장공통부분문자열이 str1[i](=str2[j])를 무조건 포함하므로
2_ str1[i] != str2[j]이면 LCS(i - 1, j)와 LCS(i, j - 1) 중 더 큰 값
    >> 두 문자열로부터 얻어지는 최장공통부분문자열은 마지막이 str1[i]로 끝나거나,
        str2[j]로 끝나거나, 둘 다 아니거나이므로. 따라서 LCS(i, j)는 LCS(i - 1, j)나
        LCS(i, j - 1)중 더 큰 값을 가짐
"""
import sys
sys.setrecursionlimit(10000)

str1 = input()
str2 = input()

dp = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)] 

# def LCS(i, j):
#     if i == -1 or j == -1:
#         return 0
    
#     if not dp[j][i]:
#         if str1[i] == str2[j]:
#             dp[j][i] = LCS(i - 1, j - 1) + 1
#         else:
#             dp[j][i] = max(LCS(i - 1, j), LCS(i, j - 1))
#     return dp[j][i]

# print(LCS(len(str1) - 1, len(str2) - 1))

for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(str2)][len(str1)])

"""
초기엔 top-down방식으로 풀었고, LCS함수는 열의 값, 행의 값 순서로 파라미터를 받게 했지만
dp[i][j]와 같은 배열의 접근은 행의 값, 열의 값 순서로 접근하므로 이 부분에서 많이 헤멨다.
LCS함수 내에서 dp배열 접근 시 j, i의 위치를 바꿔치기해서 해결했지만 애시당초에 함수를 작성할 때
파라미터를 행의 값, 열의 값 순서로 받도록 통일하면 좋을 것 같다.

이와는 별개로, top-down방식으로 풀이한 것은 시간초과가 나서 bottom-up방식으로 바꿔보니까
통과과 됐다. bottom-up방식은 답을 구하기 위해 모든 배열값을 채우며 나가야 하는 반면 top-dowm방식은
필요한 것들만 계산해나가기 때문에 top-dowm방식이 더 시간이 짧게 걸릴 거라 생각했는데 아닌 것 같다.
찾아보니까 bottom-up방식이 재귀호출을 사용하지 않기 때문에 시간이 더 적게 걸린다고 함"""


"""
>> bottom-up 방식이 더 빠른 게 맞다면 dp문제를 처음부터 bottom-up방식으로 풀어나가야 하는지,
또 실제 코딩테스트에서도 top-down방식으로 접근하면 시간초과가 나는 경우가 있는지 궁금합니다!
"""