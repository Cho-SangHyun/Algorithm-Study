# N이 주어지면 크기가 N * N인 배열이 만들어지고, A[i][j]의 값은 i * j가 된다.
# 이 2차원 배열을 1차원 배열로 펼치고 오름차순 정렬했을 때 k번째 값은?

# 문제에서 주어진대로 N * N배열을 만들고 각 항들의 값을 구한 후 정렬하는 식으로 가면
# O(n^2)만큼의 시간복잡도가 걸림
# n은 최대 10^5이므로 최대 nlogn이 걸리는 방법을 찾아야 함

N = int(input())
K = int(input())

st, ed = 1, N * N

ans = 0

while st <= ed:
    mid = (st + ed) // 2

    count = 0
    for r in range(1, N + 1):
        if r * N < mid:
            count += N
        else:
            count += (mid - 1) // r
    
    if count < K:
        ans = mid
        st = mid + 1
    else:
        ed = mid - 1

print(ans)
