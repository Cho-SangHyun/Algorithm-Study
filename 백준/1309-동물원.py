# 1309 - 동물원
# 2*N 크기 우리에 사자들을 상하좌우로 서로 안 붙어있게 배치
# 0 ~ N마리까지의 사자들을 배치가능

# 1. 무식하게 풀기
# 직접 0 ~ N마리의 사자들을 우리 하나하나에 배치해봄, 가로세로로 붙는 경우를 제외한 케이스만 카운트하기
# 대략 2^2N정도의 연산, N은 최대 100,000이므로 시간초과

# 2. 그리디 / DP로 접근해볼 수 있을 것 같다.

# 2.1 부분문제로 쪼갤 수 있는지?
# -> 2*N 사이즈 우리에 K마리(K <= N)의 사자를 배치하는 경우의 수
# = 첫 사자를 첫 줄 왼쪽에 배치하는 경우
# + 첫 사자를 첫 줄 오른쪽에 배치하는 경우
# + 첫 사자를 첫 줄에 배치하지 않는 경우

# 로 쪼갤 수 있다.

# 2.2 중복되는 구조가 있는지?
# 첫 사자를 첫 줄 왼쪽에 배치할 경우, 두 번째 사자를 다음 줄(두 번째 줄) 오른쪽에 배치하거나 아예 두 번째 줄에 안 하거나
# 첫 사자를 첫 줄 오른쪽에 배치할 경우, 두 번째 사자를 다음 줄(두 번째 줄) 왼쪽에 배치하거나 아예 두 번째 줄에 안 하거나
# 첫 사자를 첫 줄에 배치하지 않을 경우, 다음 줄 왼쪽/오른쪽에 첫 사자를 배치하거나 아예 두번째 줄도 안하거나

# 위 관계에서 중복되는 구조를 관찰가능

# 3. 점화식의 형태
# dp[N] = 1 ~ N번째 줄에 사자들을 배치하는 방법
# dp[N][0] = 첫 번째 줄의 왼쪽에 사자를 배치하는 법
# dp[N][1] = 첫 번째 줄의 오른쪽에 사자를 배치하는 법
# dp[N][2] = 첫 번째 줄에 사자를 배치하지 않는 법

# dp[N][0] = dp[N-1][1] + dp[N-1][2]
# dp[N][1] = dp[N-1][0] + dp[N-1][2]
# dp[N][2] = dp[N-1][0] + dp[N-1][1] + dp[N-1][2]

N = int(input())

mod = 9901

dp = [[0, 0, 0] for _ in range(N + 1)]
dp[1] = [1, 1, 1]

for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % mod
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % mod

print(sum(dp[N]) % mod)

# DP로 풀어야 한다는 건 알아냈지만, 적절한 점화식을 유도하는데 시간이 많이 소요된 문제..
# 1마리 사자를 배치하는 경우, 2마리 사자를 배치하는 경우, 3마리 사자를 배치하는 경우 등을 다르게 구하고
# 그 답을 구해야 된다고 생각해서 마리 수를 포함하는 점화식을 처음에 구상했지만 마리수를 포함해서 할 경우
# 메모리 제한에 걸리는 문제가 생겨서 어떻게 해야 하나 고민하다가 인터넷을 보고 마리수를 고려할 필요가 없음
# 을 알게 되고 푼 문제
