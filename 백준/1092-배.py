import sys
input = sys.stdin.readline


def is_all_clear(boxes):
    for box in boxes:
        if box:
            return False
    return True


def remove_box(assigned_box, index):
    if assigned_box[index]:
        assigned_box[index].pop()
        return
    if index == 0:
        return
    remove_box(assigned_box, index - 1)


def solution(n, cranes, m, boxes):
    if max(cranes) < max(boxes):
        return -1

    cranes.sort()
    assigned_box = [[] for _ in range(n)]
    for weight in boxes:
        for i in range(n):
            if weight <= cranes[i]:
                assigned_box[i].append(weight)
                break
    for i in range(n):
        assigned_box[i].sort()

    answer = 0

    while not is_all_clear(assigned_box):
        answer += 1
        for i in range(n - 1, -1, -1):
            remove_box(assigned_box, i)

    return answer


N = int(input())
_cranes = list(map(int, input().split()))
M = int(input())
_boxes = list(map(int, input().split()))

print(solution(N, _cranes, M, _boxes))
