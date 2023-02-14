n, r, c = map(int, input().split())
r += 1
c += 1

def calculate(start_number, exp, r, c):
    width = 2 ** exp

    if width == 1:
        return start_number

    half = width // 2

    if r <= half and c <= half:
        return calculate(start_number, exp - 1, r, c)
    if r <= half and c > half:
        return calculate(start_number + 4 ** (exp - 1), exp - 1, r, c - width // 2)
    if r > half and c <= half:
        return calculate(start_number + 2 * (4 ** (exp - 1)), exp - 1, r - width // 2, c)
    if r > half and c > half:
        return calculate(start_number + 3 * (4 ** (exp - 1)), exp - 1, r - width // 2, c - width // 2)


print(calculate(0, n, r, c))



