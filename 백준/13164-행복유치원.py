# 13164 - 행복유치원
# n개의 학생들이 키순서대로 일렬로 서있고, 이들을 k조로 나눈다.
# 각 조는 최소 1명이고, 서로 키 순서대로 서있을 때 인접해있던 애들이다.
# 각 조별로 반티를 만드는데, 그 조에서 가장 큰 인원의 키 - 가장 작은 인원의 키만큼 돈이 든다
# 조원이 한명이면 드는 돈은 0원
# k개의 조를 만들어야 할 때 생길 수 있는 전체반티비용 중 최소는?

# 1. 무식하게 접근
# N명을 K개의 조로 만드는 모든 방법을 조사
# N - 1명의 인원에서 K-1개의 인원만 고르면 조를 만들 수 있다.
# (N-1)C(K-1)만큼의 연산을 하며, 당연히 시간초과

# 2. 부분문제로 쪼갤 수 있는지?
# 마지막 조가 1명일 때, 마지막 조에서 드는 비용 + <부분문제>N - 1명을 K - 1개의 조로 나눌 때 드는 비용
# 마지막 조가 2명일 때, 마지막 조에서 드는 비용 + <부분문제>N - 2명을 K - 1개의 조로 나눌 때 드는 비용
# 마지막 조가 3명일 때, 마지막 조에서 드는 비용 + <부분문제>N - 3명을 K - 1개의 조로 나눌 때 드는 비용
# 이 중 최소가 정답

# 3. 중복되는가? 
# Yes. 근데 문제가 있다. 공간복잡도가 너무 커서 메모리 제한에 걸릴 듯함

# 4. Greedy : 
# 인접한 애들끼리의 차이 값을 구한다. 그 중 가장 큰 값 k - 1개를 빼고 더하면 답이다.

import sys

N, K = map(int, sys.stdin.readline().split())

babies = list(map(int, sys.stdin.readline().split()))

diff = []

for i in range(N - 1):
    diff.append(babies[i + 1] - babies[i])

diff.sort()

print(sum(diff[:N - K]))