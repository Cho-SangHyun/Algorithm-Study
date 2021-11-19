"""
참고 링크 : https://www.youtube.com/watch?v=rhda6lR5kyQ

무식하게 풀기 : N개의 물건들에 대해 하나하나 챙기는지 안 챙기는지 따져보기
    >> 2^N개의 케이스가 나오며 이들 중 K를 넘지 않으며 최대 가치를 찾아야 함
    >> 2^N개의 케이스를 하나하나 보며 따져야하고, N은 최대 100이므로 최대 2^100번 탐색
    >> >> 2^31이 대략 21억, 문제의 제한시간은 2초 >> 이 방법으론 통과 불가

다른 방법:
    >> N개에 물건들에 대해 정답이 되는 것은 N번째 물건을 가져갈 경우의 답vs안가져갈 경우의 답 중 더 큰 것
    >> 1 ~ N개의 물건들 무게를 w[1] ~ w[n], 가치를 v[1] ~ v[n]이라 하면
    1) N번째 물건 가져감 : 정답 = v[n] + 1 ~ N-1번째 물건들로 K - w[n]가 되는 최대
        -> N-1번째 물건을 챙길 경우의 답vs안챙길 경우의 답 중 더 큰 것
        1-1) N-1번째 물건 가져감 : v[n] + v[n+1] + 1 ~ N-2번째 물건들로 k - w[n] - w[n+1]이 되는 최대 
        1-2) N-1번째 물건 안가져감 : v[n] + 1 ~ N-2번째 물건들로 k - w[n]이 되는 최대 
    2) N번째 물건 안가져감 : 정답 = 1 ~ N-1번째 물건들로 K가 되는 최대
        -> N-1번째 물건을 챙길 경우의 답vs안챙길 경우의 답 중 더 큰 것
        2-1) N-1번째 물건 가져감 : 1 ~ N-2번째 물건들로 k - w[n+1]이 되는 최대 
        2-2) N-1번째 물건 안가져감 : 1 ~ N-2번째 물건들로 K이 되는 최대
    
    func(N, K) : 1부터 N번까지의 물건들로 낼 수 있는 최대 가치, 최대 무게는 K라 할때
    func(N, K) = max(func(N - 1, K - w[N]) + v[n], func(N - 1, K))
    
    -> dp는 계속해서 중복계산되는 부분?들을 한 번씩만 계산해주도록 하는 방법으로 알고있는데
    위 방법은 중복되는 부분들이 잘 보이지 않아 어떻게 해야 하는지 많이 헤메다가 영상을 보고 힌트를 얻었다. 

"""

import sys

N, K = map(int, sys.stdin.readline().split())

data = [0]

for _ in range(N):
    wv = list(map(int, sys.stdin.readline().split()))
    data.append(wv)

# ns[i][j] = 1부터 i까지의 물건들을 챙길 때 낼 수 있는 최대 가치, j는 무게제한 . -1은 계산되지 않았음을 의미
ns = [[-1 for _ in range(K + 1)] for _ in range(N + 1)] 

def solution(N, K):
    # N이 0이거나 K가 0이면 물건을 안 넣는다는 뜻이므로 0 리턴
    if N == 0 or K == 0:
        return 0
    # ns[N][K]가 계산되지 않았다면 계산함
    if ns[N][K] == -1:
        if K - data[N][0] >= 0:
            ns[N][K] = max(solution(N - 1, K - data[N][0]) + data[N][1], solution(N - 1, K))
        # N번째 물건을 골랐을 때의 무게 제한이 음수로 바뀌면 그 물건을 골랐을 때의 경우를 고려할 수 없음
        else:
            ns[N][K] = solution(N - 1, K)
    return ns[N][K]


print(solution(N, K))
