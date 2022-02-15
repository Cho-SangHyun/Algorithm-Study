T = int(input())

for _ in range(T):
    stack = []
    ps = input()
    for ch in ps:
        if ch == "(":
            stack.append("(")
        elif stack:
            stack.pop()
        else:
            print("NO")
            break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")