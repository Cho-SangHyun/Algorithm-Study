"""
무식하게 풀기 : 
홍준이가 하는 질문들에 대해 그 때 그 때마다 팰린드롬 여부 따지기
주어진 수열의 크기가 2,000이고 질문을 1,000,000개 하고 홍준이가 S, E를 계속 1, 2000을 줄 때 시간복잡도가 최대
팰린드롬 여부를 따지는 것은 주어진 범위의 반까지만 탐색하면 되므로 10^6 * 10^3 = 대략 10억번 정도의 연산을 함
-> 0.5초 내에 통과 불가 

s부터 e까지가 팰린드롬?
-> s번째 숫자, e번째 숫자가 같으면 s + 1번째 ~ e - 1번째가 팰린드롬?
-> s번째 숫자, e번째 숫자가 다르면 팰린드롬 X

2차원 dp테이블을 만든다 dp[s][e]는 s번째부터 e번째가 팰린드롬인지 여부를 가짐
0이면 안 구함, 1이면 아님, 2이면 팰린드롬 맞음
dp테이블 크기 = 최대 2000 * 2000 = 4,000,000이라 메모리 제한엔 안 걸릴 듯함
"""

import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())

data = [0] + list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())

dp = [[0 for i in range(N + 1)] for j in range(N + 1)]

# 범위가 1이면 무조건 팰린드롬이므로 dp테이블에 초기화해주기
for i in range (1, N + 1):
    dp[i][i] = 2

def solution(s, e):
    if dp[s][e]:
        return dp[s][e]
    # dp[s][e] == 0 즉 안 구했을 때
    if data[s] == data[e]:
        # s == e + 1이면 s + 1번째 숫자부터 e - 1번째 숫자까지의 팰린드롬을 구할 시 범위가 꼬이므로 예외처리
        dp[s][e] = solution(s + 1, e - 1) if e != (s + 1) else 2
    else:
        dp[s][e] = 1
    return dp[s][e]

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(solution(S, E) - 1)