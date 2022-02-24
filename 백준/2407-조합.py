def get_factorial(num):
    ans = 1
    for i in range(2, num + 1):
        ans *= i
    return ans

n, m = map(int, input().split())

if m == 0:
    print(1)
    exit(0)
print(int(get_factorial(n) // (get_factorial(n - m) * get_factorial(m))))