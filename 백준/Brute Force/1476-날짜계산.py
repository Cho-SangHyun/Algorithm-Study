e, s, m = map(int, input().split())
answer = 1
_e, _s, _m = 1, 1, 1

while True:
    if e == _e and s == _s and m == _m:
        print(answer)
        exit()
    answer += 1
    _e += 1
    _s += 1
    _m += 1

    if _e == 16:
        _e = 1
    if _s == 29:
        _s = 1
    if _m == 20:
        _m = 1
