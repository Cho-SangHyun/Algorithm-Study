import sys
input = sys.stdin.readline

n = int(input())
time, pay = [0], [0]
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

results = []


def pick_day(day, sum_of_pay):
    min_pickable_day = day + time[day]
    if min_pickable_day == n + 1:
        results.append(sum_of_pay)
        return
    if min_pickable_day > n + 1:
        results.append(sum_of_pay - pay[day])
        return
    for j in range(min_pickable_day, n + 1):
        pick_day(j, sum_of_pay + pay[j])


for i in range(1, n + 1):
    pick_day(i, pay[i])

print(max(results))
