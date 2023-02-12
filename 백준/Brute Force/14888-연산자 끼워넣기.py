from itertools import combinations

n = int(input())
numbers = list(map(int, input().split()))
operands = list(map(int, input().split()))

locations = set(range(1, n))
results = []


for plus_location in combinations(locations, operands[0]):
    for minus_location in combinations(locations - set(plus_location), operands[1]):
        for mul_location in combinations(locations - set(plus_location) - set(minus_location), operands[2]):
            for div_location in combinations(locations - set(plus_location) - set(minus_location) - set(mul_location), operands[3]):
                operand_orders = [0 for _ in range(n)]

                for i in plus_location:
                    operand_orders[i] = 1
                for i in minus_location:
                    operand_orders[i] = 2
                for i in mul_location:
                    operand_orders[i] = 3
                for i in div_location:
                    operand_orders[i] = 4

                res = numbers[0]
                for i in range(1, n):
                    if res < 0 < numbers[i] and operand_orders[i] == 4:
                        res = -(-res // numbers[i])
                        continue
                    if operand_orders[i] == 1:
                        res += numbers[i]
                    elif operand_orders[i] == 2:
                        res -= numbers[i]
                    elif operand_orders[i] == 3:
                        res *= numbers[i]
                    else:
                        res //= numbers[i]
                results.append(res)

print(max(results))
print(min(results))
