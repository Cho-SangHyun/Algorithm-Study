import sys
input = sys.stdin.readline


def solution(n, students):
    students = [0] + students
    visited = set()
    answer = 0

    for i in range(1, n + 1):
        if i not in visited:
            visited.add(i)
            stack = [(i, [i])]

            while stack:
                node, path = stack.pop()
                if students[node] in visited:
                    if students[node] != i:
                        for nd in path:
                            if nd == students[node]:
                                break
                            answer += 1
                    break
                visited.add(students[node])
                path.append(students[node])
                stack.append((students[node], path))

    return answer



T = int(input())
for _ in range(T):
    N = int(input())
    _students = list(map(int, input().split()))
    print(solution(N, _students))
