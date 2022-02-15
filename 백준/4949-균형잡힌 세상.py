while True:
    s = input()
    if s == ".": break
    stack = []
    for ch in s:
        if ch in ["(", "["]:
            stack.append(ch)
        elif ch == ")":
            if not stack or stack.pop() != "(":
                print("no")
                break
        elif ch == "]":
            if not stack or stack.pop() != "[":
                print("no")
                break
    else:
        print("yes" if not stack else "no")
