import sys, heapq
input = sys.stdin.readline


def solution(nums, m):
    q = []
    for num in nums:
        heapq.heappush(q, num)
    for _ in range(m):
        n1 = heapq.heappop(q)
        n2 = heapq.heappop(q)
        heapq.heappush(q, n1 + n2)
        heapq.heappush(q, n1 + n2)
    return sum(q)


n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(nums, m))
