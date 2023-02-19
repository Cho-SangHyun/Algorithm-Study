from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    commands = list(map(str, input().strip()))
    n = int(input())
    _input = input().strip()
    if len(_input) == 2:
        nums = []
    else:
        _input = _input[1:-1]
        nums = list(map(int, _input.split(",")))
    nums = deque(nums)
    reverse_flag = False
    for cmd in commands:
        if cmd == "R":
            reverse_flag = not reverse_flag
        elif not nums:
            print("error")
            break
        elif reverse_flag:
            nums.pop()
        else:
            nums.popleft()
    else:
        answer = list(nums)
        if reverse_flag:
            answer.reverse()
        print("[", end='')
        for i in range(len(answer)):
            if i == len(answer) - 1:
                print(answer[i], end='')
            else:
                print(answer[i], end=',')
        print("]")
