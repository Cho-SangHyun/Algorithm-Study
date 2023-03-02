from collections import deque
import sys
input = sys.stdin.readline


def solution(start, target):
    MOD = 10000
    q = deque([(start, "")])
    visited = set()

    while q:
        now, command = q.popleft()
        if now == target:
            return command

        now_d, now_s = (now * 2) % MOD, now - 1 if now > 0 else 9999
        now_l = (now % 1000) * 10 + now // 1000
        now_r = now // 10 + (now % 10) * 1000

        if now_d not in visited:
            visited.add(now_d)
            q.append((now_d, command + "D"))
        if now_s not in visited:
            visited.add(now_s)
            q.append((now_s, command + "S"))
        if now_l not in visited:
            visited.add(now_l)
            q.append((now_l, command + "L"))
        if now_r not in visited:
            visited.add(now_r)
            q.append((now_r, command + "R"))


T = int(input())
for _ in range(T):
    s, e = map(int, input().split())
    print(solution(s, e))