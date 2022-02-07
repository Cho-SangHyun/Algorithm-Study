def solution(n):
    x = int(n ** 0.5)
    return (x + 1) ** 2 if x ** 2 == n else -1 

print(int(121 ** 0.5))
