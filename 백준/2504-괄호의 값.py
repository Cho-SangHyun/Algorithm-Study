def solution(parenthesis, s, e):
    if e == s + 1:
        if parenthesis[s] == "(":
            return 2
        else:
            return 3

    group, stack = [], []
    little_s, little_e = 0, 0

    for i in range(s + 1, e):
        if parenthesis[i] in ("(", "["):
            if not stack:
                little_s = i
            stack.append(parenthesis[i])
            continue
        if len(stack) == 1:
            little_e = i
            group.append([little_s, little_e])
        stack.pop()
        continue

    result = 0
    for ns, ne in group:
        result += solution(parenthesis, ns, ne)
    return 2 * result if parenthesis[s] == "(" else 3 * result


parenthesis = "(" + input().strip() + ")"
stack = []
for i in range(len(parenthesis)):
    if parenthesis[i] in ("(", "["):
        stack.append(parenthesis[i])
        continue
    if not stack:
        print(0)
        exit()
    if (parenthesis[i] == ")" and stack[-1] == "[") or (parenthesis[i] == "]" and stack[-1] == "("):
        print(0)
        exit()
    stack.pop()

print(solution(parenthesis, 0, len(parenthesis) - 1) // 2)


