import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

visited = set()

for d in data:
    if d not in visited:
        visited.add(d)

arr = sorted(list(visited))

def binarySearch(target):
    st, ed = 0, len(arr) - 1
    while st <= ed:
        mid = (st + ed) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            ed = mid - 1
        else:
            st = mid + 1
    return -1

for d in data:
    print(binarySearch(d), end=" ")


