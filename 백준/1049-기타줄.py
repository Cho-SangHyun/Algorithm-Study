import sys
input = sys.stdin.readline

MOD = 6
n, m = map(int, input().split())
bundle_costs, unit_costs = [], []

for _ in range(m):
    b_cost, u_cost = map(int, input().split())
    bundle_costs.append(b_cost)
    unit_costs.append(u_cost)

bundle_costs.sort()
unit_costs.sort()

bundle_count, unit_count = n // MOD, n % MOD
answer = 0

if unit_costs[0] * 6 <= bundle_costs[0]:
    answer += unit_costs[0] * 6 * bundle_count
else:
    answer += bundle_costs[0] * bundle_count

if unit_count:
    if unit_costs[0] * unit_count <= bundle_costs[0]:
        answer += unit_costs[0] * unit_count
    else:
        answer += bundle_costs[0]

print(answer)
