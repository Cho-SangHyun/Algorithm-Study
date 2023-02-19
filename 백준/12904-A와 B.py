s = list(map(str, input().strip()))
t = list(map(str, input().strip()))

while len(s) != len(t):
    if t[-1] == "A":
        t = t[:-1]
    else:
        t = t[:-1]
        t.reverse()

if s == t:
    print(1)
else:
    print(0)

