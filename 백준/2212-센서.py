import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

locations = list(map(int, input().split()))
locations.sort()

between_distances = []
for i in range(len(locations) - 1):
    between_distances.append(locations[i + 1] - locations[i])

between_distances.sort()
for _ in range(k - 1):
    if not between_distances:
        break
    between_distances.pop()

print(sum(between_distances) if between_distances else 0)
