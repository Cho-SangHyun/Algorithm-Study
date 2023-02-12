from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
synergy = [[]]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    synergy.append(row)

numbers = set(range(1, n + 1))
results = []

for start_team in combinations(numbers, n // 2):
    link_team = list(numbers - set(start_team))
    start_team_power = 0
    link_team_power = 0

    for i in range(len(start_team) - 1):
        for j in range(i + 1, len(start_team)):
            start_team_power += (synergy[start_team[i]][start_team[j]] + synergy[start_team[j]][start_team[i]])
            link_team_power += (synergy[link_team[i]][link_team[j]] + synergy[link_team[j]][link_team[i]])

    results.append(abs(start_team_power - link_team_power))

print(min(results))

