# <문제>
# 4 x 4 격자 형태로 16개의 시계가 주어짐, 각 시계의 시간은 12/3/6/9시 중 하나
# 모든 시계의 시간을 12시로 세팅하고 싶다. 
# 특정 스위치를 누르면 그 스위치에 연결된 시계들의 시간들이 3시간씩 추가됨
# 각 스위치에는 3 ~ 5개의 스위치가 연결되어있음
# 모든 시계를 12시로 돌리기 위해 스위치를 최소 몇 번 눌러야 하는가?

# 각 스위치와 연결된 시계는 정해져 있다.
# 0번 스위치 - 0, 1, 2번 시계와 연결
# 1번 스위치 - 3, 7, 9, 11번 시계와 연결
# ...

# 한 스위치를 여러 번 누르는 것도 누른 만큼 카운트에 포함함
# 스위치들의 순서는 관련이 없다. 어느 스위치를 몇 번 누를건지만 결정하면 됨
# 왜 순서가 관련이 없는지 : A시계 입장에서는 결국 한 번 바뀔 때마다 3시간씩 늘어남. 
# 어떤 순서로 눌리던 간에 N번 눌리면 3시간씩 늘어나는 작업이 N번 수행되는 것이니 순서가 중요치 않음

# 스위치는 최대 3번까지만 누를 수 있다고 생각할 수 있다. 4번 눌리면 처음 상태로 돌아가는 거니까 의미가 없기 때문
# 따라서 각 스위치 별로 0번 ~ 3번까지 중 몇 번씩 누를건지만 결정해주며 탐색하면 됨
# 따라서 모든 경우의 수는 4^10 = 1,000,000 정도

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

SWITCH = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]

C = int(input())

for _ in range(C):
    times = list(map(lambda x: int(x) // 3, input().split()))
    # 특정 시계에 대해 p_count번 눌렀을 때의 새로운 시간 리턴
    # sign이 False면 반대로 돌림
    def get_new_clock(clock, p_count, sign=True):
        if sign:
            return (clock + p_count) % 4 if clock + p_count != 4 else 4
        new_clock = clock - p_count
        return new_clock if new_clock > 0 else 4 + new_clock

    answer = []

    def get_clock_count(count, cur):
        ret = 9999999
        if sum(times) == 64:
            return min(ret, count)

        if cur == 10:
            return ret

        # pc = 누를 횟수 : 0 ~ 3
        for pc in range(4):
            # i번째 스위치에 연결된 시계들에 pc번만큼 시간 늘리기
            for clock in SWITCH[cur]:
                times[clock] = get_new_clock(times[clock], pc, True)
            # i번째 스위치를 pc번 누른 경우에 나올 수 있는 최소한의 횟수 구하기
            ret = min(ret, get_clock_count(count + pc, cur + 1))
            # i번째 스위치에 연결된 시계들에 pc번만큼 늘리기 전으로 돌리기
            for clock in SWITCH[cur]:
                times[clock] = get_new_clock(times[clock], pc, False)
        
        return ret

    answer = get_clock_count(0, 0)
    print(answer if answer != 9999999 else -1)
        
